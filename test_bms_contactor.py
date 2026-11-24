"""Read the module serial number, BMS/CAN settings and main contactor registers.

Usage:
    python test_bms_contactor.py <ip> [--port 502]
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
    main_contactor_command_status_n,
    main_contactor_state_machine_n,
    main_contactor_status_n,
    main_contactor_closing_time_n,
    main_contactor_opening_time_n,
)

REGISTERS = [
    (module_sn_n,                     "Module SN"),
    (bms_manufacturer_info_n,         "BMS Manufacturer Information"),
    (can_baud_rate_non_std_n,         "CAN Baud Rate (Non-standard)"),
    (main_contactor_command_status_n, "Main contactor command status"),
    (main_contactor_state_machine_n,  "Main contactor state machine"),
    (main_contactor_status_n,         "Main contactor status"),
    (main_contactor_closing_time_n,   "Main contactor closing time"),
    (main_contactor_opening_time_n,   "Main contactor opening time"),
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
        return 1 if failures else 0
    finally:
        await client.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read module SN, BMS/CAN settings and main contactor registers"
    )
    parser.add_argument("ip", help="IP address of the PCS")
    parser.add_argument("--port", type=int, default=502, help="Modbus TCP port (default: 502)")
    args = parser.parse_args()
    return asyncio.run(read_registers(args.ip, args.port))


if __name__ == "__main__":
    sys.exit(main())
