import asyncio
import logging
from datetime import datetime
from pypcs import AsyncPcsClient
from pypcs.definition.register_names import *
from pypcs.definition.models import GridState, SourceMode


# Silence pymodbus and asyncio noise, keep only application logs
logging.basicConfig(level=logging.WARNING)
logging.getLogger("pypcs").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

GRID_STATE  = {s.value: s.name for s in GridState}
CHARGE_MODE = {m.value: m.name for m in SourceMode}
OP_MODE     = CHARGE_MODE

REGISTERS = [
    (module_sn_n,           "Module SN",          None),
    (dsp_version_v_n,       "DSP Version V",       None),
    (dsp_version_b_n,       "DSP Version B",       None),
    (dsp_version_d_n,       "DSP Version D",       None),
    (grid_offgrid_state_n,  "Grid/OffGrid State",  GRID_STATE),
    (working_condition_n,   "Working Condition",   None),
    (charge_discharge_mode_n,"Charge/Disch Mode",  CHARGE_MODE),
    (operation_mode_n,      "Operation Mode",      OP_MODE),
    (ac_total_active_power_n,"AC Total Power",     None),
    (battery_voltage_n,     "Battery Voltage",     None),
    (battery_current_n,     "Battery Current",     None),
    (dc_power_n,            "DC Power",            None),
    (set_active_power_n,    "Set Active Power",    None),
    (max_charge_power_n,    "Max Charge Power",    None),
    (max_discharge_power_n, "Max Discharge Power", None),
    (ac_daily_charge_n,     "AC Daily Charge",     None),
    (ac_daily_discharge_n,  "AC Daily Discharge",  None),
    (dc_daily_charge_n,     "DC Daily Charge",     None),
    (dc_daily_discharge_n,  "DC Daily Discharge",  None),
    (hw_fault_word1_n,      "HW Fault Word 1",     None),
    (hw_fault_word2_n,      "HW Fault Word 2",     None),
    (grid_fault_word_n,     "Grid Fault Word",     None),
    (bus_fault_word_n,      "Bus Fault Word",      None),
    (system_fault_word_n,   "System Fault Word",   None),
    (switch_fault_word_n,   "Switch Fault Word",   None),
    (other_fault_word_n,    "Other Fault Word",    None),
]

UNITS = {
    ac_total_active_power_n:  "kW",
    battery_voltage_n:        "V",
    battery_current_n:        "A",
    dc_power_n:               "kW",
    set_active_power_n:       "kW",
    max_charge_power_n:       "kW",
    max_discharge_power_n:    "kW",
    ac_daily_charge_n:        "kWh",
    ac_daily_discharge_n:     "kWh",
    dc_daily_charge_n:        "kWh",
    dc_daily_discharge_n:     "kWh",
}


def is_fault_word(name: str) -> bool:
    return "fault" in name.lower() or "Fault" in name


def fmt_value(reg_name, value, lookup):
    if lookup and value in lookup:
        return f"{lookup[value]} ({value})"
    unit = UNITS.get(reg_name, "")
    if isinstance(value, float):
        value = f"{value:.2f}"
    if unit:
        return f"{value} {unit}"
    return str(value)


def print_status(results: dict):
    print()
    print(f"  {'Register':<22}  {'Value':<30}  Status")
    print(f"  {'-'*22}  {'-'*30}  {'-'*6}")
    for reg_name, label, lookup in REGISTERS:
        if reg_name not in results:
            continue
        value, ok = results[reg_name]
        if not ok:
            print(f"  {label:<22}  {'READ ERROR':<30}  FAIL")
            continue

        display = fmt_value(reg_name, value, lookup)

        # Determine status colour/marker
        if is_fault_word(reg_name):
            has_fault = any(c == '1' for c in str(value))
            status = "FAULT" if has_fault else "OK"
        elif reg_name == grid_offgrid_state_n and value == 5:
            status = "FAULT"
        elif reg_name == working_condition_n:
            bits = str(value)
            status = "FAULT" if len(bits) >= 7 and bits[-7] == '1' else "OK"
        else:
            status = "OK"

        print(f"  {label:<22}  {display:<30}  {status}")
    print()


class BatteryController:
    def __init__(self, host='192.168.1.200', port=502):
        """Initialize the battery controller"""
        self.client = AsyncPcsClient(host=host, port=port)

    async def connect(self):
        """Connect to the PCS"""
        if not await self.client.connect():
            raise ConnectionError("Failed to connect to PCS")
        print("Connected to PCS")

    async def get_battery_status(self):
        """Get current battery status"""
        results = {}
        for reg_name, _, _ in REGISTERS:
            result = await self.client.get(reg_name)
            if result is not None:
                results[reg_name] = (result.value, True)
            else:
                results[reg_name] = (None, False)
        return results

    async def handle_charge_discharge_maintain(
        self,
        operation: str = "charge",
        power_limit: float = 50.0,
    ):
        """
        Handle battery charge/discharge/maintain operations

        Args:
            operation: "charge", "discharge", or "maintain"
            power_limit: Power in kW
        """
        try:
            # positive = discharge, negative = charge
            power_map = {
                "charge": -abs(power_limit),
                "discharge": abs(power_limit),
                "maintain": 0.0,
            }

            power_kw = power_map.get(operation.lower())
            if power_kw is None:
                raise ValueError(f"Invalid operation: {operation}")

            print("\n--- Initial status ---")
            print_status(await self.get_battery_status())

            result = await self.client.set(set_active_power_n, power_kw)
            if not result:
                raise Exception("Failed to set active power")

            await asyncio.sleep(2)

            print("\n--- Updated status ---")
            print_status(await self.get_battery_status())

            return True

        except Exception as e:
            print(f"ERROR in handle_charge_discharge_maintain: {e}")
            return False

    async def close(self):
        """Close the client connection"""
        if hasattr(self, 'client'):
            await self.client.close()


async def main():
    controller = None
    try:
        controller = BatteryController()
        await controller.connect()

        # reset – zero out power setpoints
        await controller.client.set(set_active_power_n, 0.0)
        await controller.client.set(set_reactive_power_n, 0.0)
        await controller.client.set(max_charge_power_n, 0.0)
        await controller.client.set(max_discharge_power_n, 0.0)

        # charge (positive kW = discharge, negative = charge)
        #await controller.client.set(set_active_power_n, -20.0)
        #await controller.client.set(max_charge_power_n, 20.0)

        # discharge
        #await controller.client.set(set_active_power_n, 20.0)
        #await controller.client.set(max_discharge_power_n, 20.0)

        print_status(await controller.get_battery_status())

        # Start charging operation
        #await controller.handle_charge_discharge_maintain(
        #    operation="charge",
        #    power_limit=20.0,
        #)

    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        if controller:
            await controller.close()

if __name__ == "__main__":
    asyncio.run(main())
