import asyncio
import logging
from datetime import datetime
from pyepppcs import AsyncPcsClient
from pyepppcs.defination.register_names import *


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class BatteryController:
    def __init__(self, host='192.168.1.200', port=502):
        """Initialize the battery controller"""
        self.client = AsyncPcsClient(host=host, port=port)

    async def connect(self):
        """Connect to the PCS"""
        if not await self.client.connect():
            raise ConnectionError("Failed to connect to PCS")
        logger.info("Successfully connected to PCS")

    async def get_battery_status(self):
        """Get current battery status"""
        try:
            status = {
                module_sn_n: (await self.client.get(module_sn_n)).value,
                dsp_version_v_n: (await self.client.get(dsp_version_v_n)).value,
                dsp_version_b_n: (await self.client.get(dsp_version_b_n)).value,
                dsp_version_d_n: (await self.client.get(dsp_version_d_n)).value,
                ac_total_active_power_n: (await self.client.get(ac_total_active_power_n)).value,
                battery_voltage_n: (await self.client.get(battery_voltage_n)).value,
                battery_current_n: (await self.client.get(battery_current_n)).value,
                dc_power_n: (await self.client.get(dc_power_n)).value,
                charge_discharge_mode_n: (await self.client.get(charge_discharge_mode_n)).value,
                working_condition_n: (await self.client.get(working_condition_n)).value,
                grid_offgrid_state_n: (await self.client.get(grid_offgrid_state_n)).value,
                operation_mode_n: (await self.client.get(operation_mode_n)).value,
                set_active_power_n: (await self.client.get(set_active_power_n)).value,
                max_charge_power_n: (await self.client.get(max_charge_power_n)).value,
                max_discharge_power_n: (await self.client.get(max_discharge_power_n)).value,
                ac_daily_discharge_n: (await self.client.get(ac_daily_discharge_n)).value,
                ac_daily_charge_n: (await self.client.get(ac_daily_charge_n)).value,
                dc_daily_charge_n: (await self.client.get(dc_daily_charge_n)).value,
                dc_daily_discharge_n: (await self.client.get(dc_daily_discharge_n)).value,
            }
            return status
        except Exception as e:
            logger.error(f"Error getting battery status: {e}")
            return None

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

            # Print initial battery status
            logger.info("Initial battery status:")
            initial_status = await self.get_battery_status()
            if initial_status:
                for key, value in initial_status.items():
                    logger.info(f"{key}: {value}")

            # Set active power target
            result = await self.client.set(set_active_power_n, power_kw)

            if not result:
                raise Exception("Failed to set active power")

            # Wait a moment for changes to take effect
            await asyncio.sleep(2)

            # Print updated battery status
            logger.info("\nUpdated battery status:")
            updated_status = await self.get_battery_status()
            if updated_status:
                for key, value in updated_status.items():
                    logger.info(f"{key}: {value}")

            return True

        except Exception as e:
            logger.error(f"Error in handle_charge_discharge_maintain: {e}")
            return False

    async def close(self):
        """Close the client connection"""
        if hasattr(self, 'client'):
            await self.client.close()

async def main():
    controller = None
    try:
        # Create and connect controller
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

        status = await controller.get_battery_status()

        logger.info(f"Status: {status}")

        # Start charging operation
        #logger.info("\nStarting charging operation...")
        #await controller.handle_charge_discharge_maintain(
        #    operation="charge",
        #    power_limit=20.0,
        #    duration_hours=2.0
        #)

    except Exception as e:
        logger.error(f"Error in main: {e}")
    finally:
        if controller:
            await controller.close()

if __name__ == "__main__":
    asyncio.run(main())
