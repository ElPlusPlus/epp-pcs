"""
pypcs – Async Modbus client for the EPP PCS (Power Conversion System).

Physical interface : RS485 (A/B)
Protocol           : Standard Modbus, FC03 read / FC06 write single register
Serial settings    : 9600 bps, 8 data bits, No parity, 1 stop bit
Max read length    : 16 registers per request
"""
from pymodbus.client import AsyncModbusTcpClient, AsyncModbusSerialClient
from typing import Union, Optional
import logging

from pypcs.definition import modbus_map
from pypcs.definition.register_names import *
from pypcs.definition.models import Result, ModbusType, ModbusAccess
from pypcs.definition.fault_codes import fault_bits_map, decode_fault_word
from pypcs.utils import (
    convert_to_s16, convert_to_s32, convert_to_u32,
    decode_registers_to_chars, encode_string_to_registers,
    split_s32_to_registers, split_u32_to_registers,
    convert_to_i16, convert_to_i32, split_i32_to_registers,
)

logger = logging.getLogger(__name__)


class AsyncPcsClient:
    """
    Async Modbus client for an EPP PCS module.

    Usage – serial (RS485):
        client = AsyncPcsClient(serial_port="COM3", unit_id=1)

    Usage – TCP (e.g. Modbus-TCP gateway):
        client = AsyncPcsClient(host="192.168.1.10", port=502, unit_id=1)
    """

    def __init__(
        self,
        host: str = "192.168.1.10",
        port: int = 502,
        unit_id: int = 1,
        serial_port: Optional[str] = None,
    ):
        self.unit_id = unit_id
        if serial_port:
            self.client = AsyncModbusSerialClient(
                port=serial_port,
                baudrate=9600,
                bytesize=8,
                parity="N",
                stopbits=1,
                timeout=1,
            )
        else:
            self.client = AsyncModbusTcpClient(host=host, port=port, timeout=3)

    # ── Connection ────────────────────────────────────────────────────────────

    async def connect(self) -> bool:
        try:
            connected = await self.client.connect()
            if connected:
                logger.info("PCS connected")
            else:
                logger.error("PCS connection failed")
            return connected
        except Exception as exc:
            logger.error(f"PCS connection error: {exc}")
            return False

    async def close(self):
        self.client.close()

    async def _ensure_connection(self):
        if not self.client.connected:
            if not await self.client.connect():
                raise ConnectionError("PCS not connected")

    # ── Low-level I/O ─────────────────────────────────────────────────────────

    async def read_register(self, address: int, count: int = 1) -> Optional[list]:
        """Read *count* holding registers starting at *address* (FC03)."""
        try:
            await self._ensure_connection()
            result = await self.client.read_holding_registers(
                address=address, count=count, slave=self.unit_id
            )
            if hasattr(result, "isError") and result.isError():
                logger.error(f"Read error @{hex(address)}: {result}")
                return None
            return result.registers if hasattr(result, "registers") else None
        except Exception as exc:
            logger.error(f"Read exception @{hex(address)}: {exc}")
            return None

    async def write_register(self, address: int, value: int) -> bool:
        """Write a single register (FC06)."""
        try:
            await self._ensure_connection()
            result = await self.client.write_register(
                address=address, value=value, slave=self.unit_id
            )
            if hasattr(result, "isError") and result.isError():
                logger.error(f"Write error @{hex(address)}: {result}")
                return False
            return True
        except Exception as exc:
            logger.error(f"Write exception @{hex(address)}: {exc}")
            return False

    # ── High-level API ────────────────────────────────────────────────────────

    async def get(self, register_name: str) -> Optional[Result]:
        """Read a named register and return a typed :class:`Result`."""
        reg = modbus_map.get(register_name)
        if reg is None:
            logger.error(f"Unknown register: {register_name}")
            return None

        for attempt in range(3):
            raw = await self.read_register(reg.register, reg.count)
            if raw is not None:
                break
            logger.warning(f"Retry {attempt + 1} reading {register_name}")
        else:
            logger.error(f"Failed to read {register_name} after 3 attempts")
            return None

        try:
            if reg.modbus_type == ModbusType.STRING:
                value = decode_registers_to_chars(raw)
            elif reg.modbus_type == ModbusType.U16:
                value = raw[0]
            elif reg.modbus_type in (ModbusType.S16, ModbusType.I16):
                value = convert_to_i16(raw[0])
            elif reg.modbus_type == ModbusType.U32:
                value = convert_to_u32(raw)
            elif reg.modbus_type == ModbusType.S32:
                value = convert_to_s32(raw)
            elif reg.modbus_type == ModbusType.I32:
                value = convert_to_i32(raw)
            elif reg.modbus_type == ModbusType.B16:
                value = bin(raw[0])[2:].zfill(16)
            elif reg.modbus_type == ModbusType.E16:
                value = hex(raw[0])[2:].upper().zfill(4)
            else:
                raise ValueError(f"Unsupported type: {reg.modbus_type}")

            if isinstance(value, (int, float)) and reg.modbus_type not in (
                ModbusType.STRING, ModbusType.B16, ModbusType.E16
            ):
                value = value * reg.gain

            return Result(
                name=register_name,
                value=value,
                modbus_type=reg.modbus_type,
                register=reg.register,
                count=reg.count,
                function_code=3,
                modbus_unit=reg.modbus_unit,
            )
        except Exception as exc:
            logger.error(f"Decode error for {register_name}: {exc}")
            return None

    async def set(self, register_name: str, value: Union[int, float]) -> bool:
        """Write a named register (FC06 – single register only)."""
        reg = modbus_map.get(register_name)
        if reg is None:
            logger.error(f"Unknown register: {register_name}")
            return False
        if reg.access == ModbusAccess.RO:
            logger.error(f"{register_name} is read-only")
            return False

        # round() rather than int(): e.g. 2.3 / 0.1 == 22.999… must become 23
        if isinstance(value, (int, float)) and reg.modbus_type not in (
            ModbusType.STRING, ModbusType.B16, ModbusType.E16
        ):
            value = round(value / reg.gain)

        # Encode signed integers into unsigned 16-bit for the wire
        if reg.modbus_type in (ModbusType.S16, ModbusType.I16) and value < 0:
            value = value + 0x10000

        if not 0 <= value <= 0xFFFF:
            logger.error(f"Value {value} out of 16-bit range for {register_name}")
            return False

        for attempt in range(3):
            if await self.write_register(reg.register, value):
                return True
            logger.warning(f"Retry {attempt + 1} writing {register_name}")
        logger.error(f"Failed to write {register_name} after 3 attempts")
        return False

    # ── Convenience helpers ───────────────────────────────────────────────────

    async def power_on(self) -> bool:
        """Send boot command (write 1 → 0x0291)."""
        return await self.set(power_on_off_n, 1)

    async def power_off(self) -> bool:
        """Send shutdown command (write 0 → 0x0291)."""
        return await self.set(power_on_off_n, 0)

    async def fault_reset(self) -> bool:
        """Reset faults: set Bit15 of 0x1400 (device must be off)."""
        return await self.write_register(0x1400, 0x8000)

    async def set_charge_power_kw(self, kw: float) -> bool:
        """
        Set charging power in kW (negative value → charge).
        E.g. set_charge_power_kw(20) → 20 kW charge.
        """
        return await self.set(set_active_power_n, -abs(kw))

    async def set_discharge_power_kw(self, kw: float) -> bool:
        """
        Set discharge power in kW (positive value → discharge).
        E.g. set_discharge_power_kw(20) → 20 kW discharge.
        """
        return await self.set(set_active_power_n, abs(kw))

    async def get_status(self) -> dict:
        """Return a dict with the most common monitoring registers."""
        names = [
            grid_offgrid_state_n,
            working_condition_n,
            battery_voltage_n,
            battery_current_n,
            dc_power_n,
            ac_total_active_power_n,
            ac_total_reactive_power_n,
            ac_total_apparent_power_n,
            ac_power_factor_n,
            grid_frequency_n,
            igbt_temperature_n,
            ambient_temperature_n,
            hw_fault_word1_n,
            hw_fault_word2_n,
            grid_fault_word_n,
            bus_fault_word_n,
            system_fault_word_n,
            switch_fault_word_n,
            other_fault_word_n,
        ]
        status = {}
        for name in names:
            result = await self.get(name)
            status[name] = result.value if result else None
        return status

    async def get_faults(self) -> dict:
        """
        Read all eight fault words (0x1700-0x1707) and decode the set bits.

        Returns {register_name: [fault descriptions]} for every word that has
        at least one bit set, or None for a word that could not be read.
        """
        faults = {}
        for name in fault_bits_map:
            result = await self.get(name)
            if result is None:
                faults[name] = None
                continue
            active = decode_fault_word(name, int(result.value, 2))
            if active:
                faults[name] = active
        return faults
