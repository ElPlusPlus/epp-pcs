"""Read the PCS module serial number.

Usage:
    python test_module_sn.py <ip> [--port 502]
"""
import argparse
import asyncio
import sys

from pypcs import AsyncPcsClient
from pypcs.definition.register_names import module_sn_n


async def read_module_sn(host: str, port: int) -> int:
    client = AsyncPcsClient(host=host, port=port)
    try:
        if not await client.connect():
            print(f"ERROR: failed to connect to PCS at {host}:{port}")
            return 1

        result = await client.get(module_sn_n)
        if result is None:
            print("ERROR: failed to read Module SN")
            return 1

        print(f"Module SN: {result.value}")
        return 0
    finally:
        await client.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Read the PCS module serial number")
    parser.add_argument("ip", help="IP address of the PCS")
    parser.add_argument("--port", type=int, default=502, help="Modbus TCP port (default: 502)")
    args = parser.parse_args()
    return asyncio.run(read_module_sn(args.ip, args.port))


if __name__ == "__main__":
    sys.exit(main())
