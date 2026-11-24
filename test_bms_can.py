"""Read the module serial number, the BMS/CAN settings and the BMS parameters.

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

SETTINGS = [
    module_sn_n,
    bms_manufacturer_info_n,
    can_baud_rate_non_std_n,
    harmonic_control_config4_n,
]

# All read-only BMS parameters (0x0C00-0x0C1C, 0x0C50), in address order.
# Raw values: units and gain are not documented yet.
BMS_PARAMETERS = sorted(
    (name for name, reg in modbus_map.items()
     if 0x0C00 <= reg.register <= 0x0C50 and name not in SETTINGS),
    key=lambda name: modbus_map[name].register,
)


async def read_section(client: AsyncPcsClient, title: str, names: list) -> int:
    print(title)
    failures = 0
    for name in names:
        address = modbus_map[name].register
        result = await client.get(name)
        if result is None:
            print(f"  0x{address:04X}  {name:<32} ERROR: read failed")
            failures += 1
        else:
            print(f"  0x{address:04X}  {name:<32} {result.value}")
    return failures


async def read_registers(host: str, port: int) -> int:
    client = AsyncPcsClient(host=host, port=port)
    try:
        if not await client.connect():
            print(f"ERROR: failed to connect to PCS at {host}:{port}")
            return 1

        failures = await read_section(client, "Settings", SETTINGS)
        failures += await read_section(client, "\nBMS parameters (raw values)", BMS_PARAMETERS)
        return 1 if failures else 0
    finally:
        await client.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read module SN, BMS/CAN settings and BMS parameters"
    )
    parser.add_argument("ip", help="IP address of the PCS")
    parser.add_argument("--port", type=int, default=502, help="Modbus TCP port (default: 502)")
    args = parser.parse_args()
    return asyncio.run(read_registers(args.ip, args.port))


if __name__ == "__main__":
    sys.exit(main())
