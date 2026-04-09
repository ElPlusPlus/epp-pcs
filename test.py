import asyncio
import logging
from datetime import datetime
from pysolinteg import AsyncSolintegClient
from pysolinteg.defination.register_names import *


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class BatteryController:
    def __init__(self, host='192.168.1.6', port=502):
        """Initialize the battery controller"""
        self.client = AsyncSolintegClient(host=host, port=port)
        
    async def connect(self):
        """Connect to the inverter"""
        if not await self.client.connect():
            raise ConnectionError("Failed to connect to inverter")
        logger.info("Successfully connected to inverter")

    async def get_battery_status(self):
        """Get current battery status"""
        try:
            status = {
                device_model_n: (await  self.client.get(device_model_n)).value,
                device_sn_n: (await self.client.get(device_sn_n)).value,
                firmware_major_version_n: (await self.client.get(firmware_major_version_n)).value,
                firmware_minor_version_n: (await self.client.get(firmware_minor_version_n)).value,
                #inverter_rated_power_n: (await self.client.get(inverter_rated_power_n)).value,
                #inverter_max_power_output_n: (await self.client.get(inverter_max_power_output_n)).value,
                ac_power_n: float((await self.client.get(ac_power_n)).value) * 1000,
                battery_soc_n: (await self.client.get(battery_soc_n)).value,
                battery_power_n: float((await self.client.get(battery_power_n)).value) * 1000,
                battery_voltage_n: (await self.client.get(battery_voltage_n)).value,
                battery_current_n: (await self.client.get(battery_current_n)).value,
                battery_mode_n: (await self.client.get(battery_mode_n)).value,
                battery_type_n: (await self.client.get(battery_type_n)).value,
                battery_status_n: (await self.client.get(battery_status_n)).value,
                battery_config_n: (await self.client.get(battery_config_n)).value,
                battery_protocol_config_n: (await self.client.get(battery_protocol_config_n)).value,
                battery_rated_capacity_n: (await self.client.get(battery_rated_capacity_n)).value,
                working_mode_n: (await self.client.get(working_mode_n)).value,
                pc_battery_power_target_n: (await self.client.get(pc_battery_power_target_n)).value,
                pc_ac_power_max_limit_n: (await self.client.get(pc_ac_power_max_limit_n)).value,
                pc_ac_power_min_limit_n: (await self.client.get(pc_ac_power_min_limit_n)).value,
                pc_power_output_priority_n: (await self.client.get(pc_power_output_priority_n)).value,
                daily_grid_export_n: (await self.client.get(daily_grid_export_n)).value,
                daily_grid_import_n: (await self.client.get(daily_grid_import_n)).value,
                daily_battery_charge_n: (await self.client.get(daily_battery_charge_n)).value,
                daily_battery_discharge_n: (await self.client.get(daily_battery_discharge_n)).value,
                period_enable_flags_n: (await self.client.get(period_enable_flags_n)).value,
                period1_charge_discharge_n: (await self.client.get(period1_charge_discharge_n)).value,
                on_grid_battery_soc_limit_n: (await self.client.get(on_grid_battery_soc_limit_n)).value,
                end_soc_of_charging_n: (await self.client.get(end_soc_of_charging_n)).value
            }
            return status
        except Exception as e:
            logger.error(f"Error getting battery status: {e}")
            return None

    async def handle_charge_discharge_maintain(
        self,
        operation: str = "charge",
        power_limit: float = 50.0,
        duration_hours: float = 2.0  # Default duration of 2 hours
    ):
        """
        Handle battery charge/discharge/maintain operations
        
        Args:
            operation: "charge", "discharge", or "maintain"
            power_limit: Power limit percentage (0-100)
            start_time: Start time in HH:MM format (optional)
            end_time: End time in HH:MM format (optional)
        """
        try:
            # Convert operation to charge_discharge value
            charge_discharge_map = {
                "charge": 1,
                "discharge": 2,
                "maintain": 0
            }
            
            charge_discharge = charge_discharge_map.get(operation.lower())
            if charge_discharge is None:
                raise ValueError(f"Invalid operation: {operation}")

            # Calculate start and end times based on current time
            from datetime import datetime, timedelta
            
            start_dt = datetime.now()
            end_dt = start_dt + timedelta(hours=duration_hours)
            
            # Convert to HHMM format
            start_time_val = int(start_dt.strftime("%H%M"))
            end_time_val = int(end_dt.strftime("%H%M"))

            # Print initial battery status
            logger.info("Initial battery status:")
            initial_status = await self.get_battery_status()
            if initial_status:
                for key, value in initial_status.items():
                    logger.info(f"{key}: {value}")

            # Set charging parameters
            result = await self.client.handle_charge_discharge_maintain(
                charge_discharge=charge_discharge,
                charge_source=1,  # Default source
                power_limit=power_limit,
                start_time=start_time_val,
                end_time=end_time_val
            )

            if not result:
                raise Exception("Failed to set charging parameters")

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

        # reset
        # await controller.client.set(battery_config_n, 3)

        await controller.client.set(working_mode_n, 0x0101)
        await controller.client.set(pc_battery_power_target_n, 0)
        await controller.client.set(pc_ac_power_max_limit_n, 0)
        await controller.client.set(pc_ac_power_min_limit_n, 0)
        await controller.client.set(pc_power_output_priority_n, 0)

        # charge
        # EMS_BattCtrlMode 0x0303
        #await controller.client.set(working_mode_n, 0x0303)
        #await controller.client.set(pc_battery_power_target_n, -5)
        #await controller.client.set(pc_ac_power_max_limit_n, 0)
        #await controller.client.set(pc_ac_power_min_limit_n, -5)
        #await controller.client.set(pc_power_output_priority_n, 0)

        # Discharge
        # EMS_BattCtrlMode 0x0303
        #await controller.client.set(on_grid_battery_soc_limit_n, 5)
        #await controller.client.set(end_soc_of_charging_n, 100)

        #await controller.client.set(working_mode_n, 0x0303)
        #await controller.client.set(pc_battery_power_target_n, 5)
        #await controller.client.set(pc_ac_power_max_limit_n, 5)
        #await controller.client.set(pc_ac_power_min_limit_n, 0)
        #await controller.client.set(pc_power_output_priority_n, 0)


        status = await controller.get_battery_status()

        logger.info(f"Status: {status}")

        # Start charging operation
        #logger.info("\nStarting charging operation...")
        #await controller.handle_charge_discharge_maintain(
        #    operation="charge",
        #    power_limit=100,
        #    duration_hours=2.0
        #)

    except Exception as e:
        logger.error(f"Error in main: {e}")
    finally:
        if controller:
            await controller.close()

if __name__ == "__main__":
    asyncio.run(main())