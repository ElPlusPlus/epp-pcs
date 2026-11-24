"""Read the module serial number, the BMS/CAN setting registers and 0x0C00.

Usage:
    python test_bms_can.py <ip> [--port 502]
"""
import argparse
import asyncio
import sys

from pypcs import AsyncPcsClient
from pypcs.definition import modbus_map
from pypcs.definition.register_names import (
    module_sn_n,
    bms_manufacturer_info_n,
    can_baud_rate_non_std_n,
    harmonic_control_config4_n,
)

REGISTERS = [
    (module_sn_n,                     "Module SN"),
    (bms_manufacturer_info_n,         "BMS Manufacturer Information"),
    (can_baud_rate_non_std_n,         "CAN Baud Rate (Non-standard)"),
    (harmonic_control_config4_n,      "Harmonic Control Configuration 4"),
]

# Registers without a library definition yet (meaning/type unknown):
# read raw and shown as decimal, hex and binary.
RAW_REGISTERS = [
    (0x0C00, "Unknown (0x0C00)"),
]


async def read_registers(host: str, port: int) -> int:
    client = AsyncPcsClient(host=host, port=port)
    try:
        if not await client.connect():
            print(f"ERROR: failed to connect to PCS at {host}:{port}")
            return 1

        failures = 0
        for name, label in REGISTERS:
            address = modbus_map[name].register
            result = await client.get(name)
            if result is None:
                print(f"0x{address:04X}  {label:<32} ERROR: read failed")
                failures += 1
            else:
                print(f"0x{address:04X}  {label:<32} {result.value}")

        for address, label in RAW_REGISTERS:
            raw = await client.read_register(address, 1)
            if raw is None:
                print(f"0x{address:04X}  {label:<32} ERROR: read failed")
                failures += 1
            else:
                v = raw[0]
                print(f"0x{address:04X}  {label:<32} {v} (0x{v:04X}, {v:016b})")
        return 1 if failures else 0
    finally:
        await client.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read module SN, BMS/CAN settings, 0x0206 and 0x0C00"
    )
    parser.add_argument("ip", help="IP address of the PCS")
    parser.add_argument("--port", type=int, default=502, help="Modbus TCP port (default: 502)")
    args = parser.parse_args()
    return asyncio.run(read_registers(args.ip, args.port))


if __name__ == "__main__":
    sys.exit(main())
