"""Configure the PCS for the non-standard BMS / CAN setup and save it.

Procedure (from the PCS vendor):
    1. 0x0291 PowerOnOff            write 0 -> shut the PCS down
    2. 0x0C52 BmsManufacturerInfo   write 9
       0x0C56 CanBaudRateNonStd     write 250
       0x0206 HarmonicControlConfig4  set Bit14 (other bits are kept)
    3. 0x1405 CureParameter         set Bit8 (0x0100) -> save the parameters
    4. 0x0291 PowerOnOff            write 1 -> start the PCS

The PCS is only started again if every write and read-back succeeded;
otherwise it is left shut down so the problem can be looked at.

Usage:
    python configure_bms_can.py <ip> [--port 502] [--yes] [--dry-run]
"""
import argparse
import asyncio
import sys
import time

from pypcs import AsyncPcsClient
from pypcs.definition.models import GridState
from pypcs.definition.register_names import (
    module_sn_n,
    grid_offgrid_state_n,
    power_on_off_n,
    bms_manufacturer_info_n,
    can_baud_rate_non_std_n,
    harmonic_control_config4_n,
    cure_parameter_n,
)

BMS_MANUFACTURER = 9
CAN_BAUD_RATE = 250
HARMONIC_CFG4_BIT = 14
CURE_SAVE_BIT = 8
STOP_TIMEOUT_S = 30


async def read_int(client: AsyncPcsClient, name: str) -> int:
    """Read a single-register value as an int (B16 comes back as a bit string)."""
    result = await client.get(name)
    if result is None:
        raise RuntimeError(f"failed to read {name}")
    value = result.value
    return int(value, 2) if isinstance(value, str) else int(value)


async def write_checked(client: AsyncPcsClient, name: str, value: int) -> None:
    """Write a register and verify it by reading it back."""
    if not await client.set(name, value):
        raise RuntimeError(f"failed to write {name} = {value}")
    readback = await read_int(client, name)
    if readback != value:
        raise RuntimeError(f"{name}: wrote {value}, read back {readback}")
    print(f"  {name} = {value} (verified)")


async def wait_for_stop(client: AsyncPcsClient) -> None:
    deadline = time.monotonic() + STOP_TIMEOUT_S
    while time.monotonic() < deadline:
        state = await read_int(client, grid_offgrid_state_n)
        if state == GridState.STOP.value:
            print("  PCS is stopped")
            return
        await asyncio.sleep(1)
    raise RuntimeError(f"PCS did not reach STOP within {STOP_TIMEOUT_S}s")


async def print_current(client: AsyncPcsClient) -> int:
    sn = await client.get(module_sn_n)
    print(f"Module SN: {sn.value if sn else 'read failed'}")
    cfg4 = await read_int(client, harmonic_control_config4_n)
    print(f"  {bms_manufacturer_info_n} = {await read_int(client, bms_manufacturer_info_n)}")
    print(f"  {can_baud_rate_non_std_n} = {await read_int(client, can_baud_rate_non_std_n)}")
    print(f"  {harmonic_control_config4_n} = {cfg4:016b} (Bit14 = {(cfg4 >> HARMONIC_CFG4_BIT) & 1})")
    return cfg4


async def configure(host: str, port: int, assume_yes: bool, dry_run: bool) -> int:
    client = AsyncPcsClient(host=host, port=port)
    try:
        if not await client.connect():
            print(f"ERROR: failed to connect to PCS at {host}:{port}")
            return 1

        print("Current values:")
        cfg4 = await print_current(client)
        new_cfg4 = cfg4 | (1 << HARMONIC_CFG4_BIT)

        print("\nPlanned changes:")
        print(f"  {bms_manufacturer_info_n} -> {BMS_MANUFACTURER}")
        print(f"  {can_baud_rate_non_std_n} -> {CAN_BAUD_RATE}")
        print(f"  {harmonic_control_config4_n} -> {new_cfg4:016b}")
        if dry_run:
            print("\nDry run: nothing written.")
            return 0

        if not assume_yes:
            answer = input("\nThis will SHUT DOWN the PCS, write and save the settings, "
                           "then start it again. Continue? [y/N] ")
            if answer.strip().lower() != "y":
                print("Aborted.")
                return 1

        print("\n1. Shutting down PCS (0x0291 = 0)")
        if not await client.power_off():
            raise RuntimeError("failed to send shutdown command")
        await wait_for_stop(client)

        try:
            print("2. Writing parameters")
            await write_checked(client, bms_manufacturer_info_n, BMS_MANUFACTURER)
            await write_checked(client, can_baud_rate_non_std_n, CAN_BAUD_RATE)
            await write_checked(client, harmonic_control_config4_n, new_cfg4)

            print("3. Saving parameters (0x1405 Bit8)")
            if not await client.set(cure_parameter_n, 1 << CURE_SAVE_BIT):
                raise RuntimeError("failed to write save command")
            await asyncio.sleep(2)
        except Exception as exc:
            print(f"ERROR: {exc}")
            print("PCS has been LEFT SHUT DOWN. Fix the problem and start it manually.")
            return 1

        print("4. Starting PCS (0x0291 = 1)")
        if not await client.power_on():
            print("ERROR: failed to send start command; PCS is still shut down.")
            return 1

        print("\nDone. Final values:")
        await print_current(client)
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    finally:
        await client.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Configure non-standard BMS/CAN settings on the PCS")
    parser.add_argument("ip", help="IP address of the PCS")
    parser.add_argument("--port", type=int, default=502, help="Modbus TCP port (default: 502)")
    parser.add_argument("--yes", action="store_true", help="do not ask for confirmation")
    parser.add_argument("--dry-run", action="store_true", help="only read and show the planned changes")
    args = parser.parse_args()
    return asyncio.run(configure(args.ip, args.port, args.yes, args.dry_run))


if __name__ == "__main__":
    sys.exit(main())
