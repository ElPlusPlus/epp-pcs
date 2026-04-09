from pysolinteg.defination.models import ModbusRegister, ModbusType, ModbusUnit, ModbusAccess

max_cell_temperature = ModbusRegister(33009, 1, 3, ModbusType.U16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10

# Additional Battery Cell Parameters
min_cell_temp_id = ModbusRegister(33010, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
min_cell_temperature = ModbusRegister(33011, 1, 3, ModbusType.U16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10
max_cell_voltage_id = ModbusRegister(33012, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
max_cell_voltage = ModbusRegister(33013, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.001)  # gain=1000
min_ceperiod1_end_time = ModbusRegister(53013, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period 2-6 Settings 
period2_charge_discharge = ModbusRegister(53014, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_charge_source = ModbusRegister(53015, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_reserved1 = ModbusRegister(53016, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_power_limit = ModbusRegister(53017, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period2_reserved2 = ModbusRegister(53018, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_start_time = ModbusRegister(53019, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_end_time = ModbusRegister(53020, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period 3
period3_charge_discharge = ModbusRegister(53021, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period3_charge_source = ModbusRegister(53022, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period3_reserved1 = ModbusRegister(53023, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period3_power_limit = ModbusRegister(53024, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period3_reserved2 = ModbusRegister(53025, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period3_start_time = ModbusRegister(53026, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period3_end_time = ModbusRegister(53027, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period 4
period4_charge_discharge = ModbusRegister(53028, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period4_charge_source = ModbusRegister(53029, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period4_reserved1 = ModbusRegister(53030, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period4_power_limit = ModbusRegister(53031, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period4_reserved2 = ModbusRegister(53032, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period4_start_time = ModbusRegister(53033, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period4_end_time = ModbusRegister(53034, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period 5
period5_charge_discharge = ModbusRegister(53035, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period5_charge_source = ModbusRegister(53036, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period5_reserved1 = ModbusRegister(53037, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period5_power_limit = ModbusRegister(53038, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period5_reserved2 = ModbusRegister(53039, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period5_start_time = ModbusRegister(53040, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period5_end_time = ModbusRegister(53041, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period 6
period6_charge_discharge = ModbusRegister(53042, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period6_charge_source = ModbusRegister(53043, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period6_reserved1 = ModbusRegister(53044, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period6_power_limit = ModbusRegister(53045, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period6_reserved2 = ModbusRegister(53046, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period6_start_time = ModbusRegister(53047, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period6_end_time = ModbusRegister(53048, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# BMS Parameters
bms_version = ModbusRegister(53500, 8, 3, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
bms_status = ModbusRegister(53508, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
bms_error1_code = ModbusRegister(53509, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
bms_error2_code = ModbusRegister(53511, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
bms_info_code = ModbusRegister(53513, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
bms_charge_volt_limit = ModbusRegister(53515, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.WO, gain=0.1)  # gain=10
bms_charge_curr_max = ModbusRegister(53516, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, ModbusAccess.WO, gain=0.1)  # gain=10
bms_discharge_volt_limit = ModbusRegister(53517, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.WO, gain=0.1)  # gain=10
bms_discharge_curr_max = ModbusRegister(53518, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, ModbusAccess.WO, gain=0.1)  # gain=10
bms_soc = ModbusRegister(53519, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.WO, gain=0.01)  # gain=100
bms_soh = ModbusRegister(53520, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.WO, gain=0.01)  # gain=100
bms_voltage = ModbusRegister(53521, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.WO, gain=0.1)  # gain=10
bms_current = ModbusRegister(53522, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, ModbusAccess.WO, gain=0.1)  # gain=10
bms_temperature = ModbusRegister(53523, 1, 3, ModbusType.I16, ModbusUnit.CELSIUS, ModbusAccess.WO, gain=0.1)  # gain=10
bms_warning_code = ModbusRegister(53525, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)

# Battery Management System Info
battery_type = ModbusRegister(32000, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_strings = ModbusRegister(32001, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_protocol = ModbusRegister(32002, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_software_version = ModbusRegister(32003, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_hardware_version = ModbusRegister(32004, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_max_charge_current = ModbusRegister(32005, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
battery_max_discharge_current = ModbusRegister(32006, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
battery_rated_capacity = ModbusRegister(32007, 2, 3, ModbusType.U32, ModbusUnit.WH, gain=1)
battery_manufacturer = ModbusRegister(32020, 8, 3, ModbusType.STRING, ModbusUnit.NONE, gain=1)

# Battery Status
battery_soc = ModbusRegister(33000, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.01)  # gain=100
battery_soh = ModbusRegister(33001, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.01)  # gain=100
battery_status = ModbusRegister(33002, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_pack_temperature = ModbusRegister(33003, 1, 3, ModbusType.U16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10
max_cell_temp_id = ModbusRegister(33008, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
max_cell_temperature = ModbusRegister(33009, 1, 3, ModbusType.U16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10

# Period 2
period2_charge_discharge = ModbusRegister(53014, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_charge_source = ModbusRegister(53015, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_reserved1 = ModbusRegister(53016, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_power_limit = ModbusRegister(53017, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period2_reserved2 = ModbusRegister(53018, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_start_time = ModbusRegister(53019, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period2_end_time = ModbusRegister(53020, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period 3
period3_charge_discharge = ModbusRegister(53021, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period3_charge_source = ModbusRegister(53022, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW)

# Device Information Registers (10000-10999)
device_sn = ModbusRegister(10000, 8, 3, ModbusType.STRING, ModbusUnit.NONE, gain=1)
device_model = ModbusRegister(10008, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
firmware_major_version = ModbusRegister(10011, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)
firmware_minor_version = ModbusRegister(10013, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)
inverter_rated_power = ModbusRegister(10070, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=1)
inverter_max_power_output = ModbusRegister(10072, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=1)

# Time Registers
time_year_month = ModbusRegister(10100, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
time_day_hour = ModbusRegister(10101, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
time_minute_second = ModbusRegister(10102, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)

# System Status Registers
safety_code = ModbusRegister(10104, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
inverter_status = ModbusRegister(10105, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
inverter_flags = ModbusRegister(10110, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)
fault_flag1 = ModbusRegister(10112, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)
fault_flag2 = ModbusRegister(10114, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)
fault_flag3 = ModbusRegister(10120, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)

meter_current_phase_a = ModbusRegister(10983, 1, 3, ModbusType.S16, ModbusUnit.AMPERE, gain=0.1)
meter_current_phase_b = ModbusRegister(10984, 1, 3, ModbusType.S16, ModbusUnit.AMPERE, gain=0.1)
meter_current_phase_c = ModbusRegister(10985, 1, 3, ModbusType.S16, ModbusUnit.AMPERE, gain=0.1)

# Meter Reactive Power (gain=1000 based on accuracy column)
meter_reactive_power_a = ModbusRegister(10986, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)
meter_reactive_power_b = ModbusRegister(10988, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)
meter_reactive_power_c = ModbusRegister(10990, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)
meter_reactive_power_total = ModbusRegister(10992, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)

# Meter Active Power (gain=1000)
meter_active_power_a = ModbusRegister(10994, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)
meter_active_power_b = ModbusRegister(10996, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)
meter_active_power_c = ModbusRegister(10998, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)
meter_active_power_total = ModbusRegister(11000, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)

# Energy Meters (gain=100)
meter_export_energy = ModbusRegister(11002, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.01)
meter_import_energy = ModbusRegister(11004, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.01)

# Inverter Side Voltage and Current (gain=10)
inverter_voltage_ab = ModbusRegister(11006, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
inverter_voltage_bc = ModbusRegister(11007, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
inverter_voltage_ca = ModbusRegister(11008, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
inverter_voltage_a = ModbusRegister(11009, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
inverter_current_a = ModbusRegister(11010, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)
inverter_voltage_b = ModbusRegister(11011, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
inverter_current_b = ModbusRegister(11012, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)
inverter_voltage_c = ModbusRegister(11013, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
inverter_current_c = ModbusRegister(11014, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)

# System Parameters
grid_frequency = ModbusRegister(11015, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, gain=0.01)  # gain=100
ac_power = ModbusRegister(11016, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
daily_energy = ModbusRegister(11018, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_energy = ModbusRegister(11020, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_runtime = ModbusRegister(11022, 2, 3, ModbusType.U32, ModbusUnit.HOUR, gain=1)
apparent_power = ModbusRegister(11024, 2, 3, ModbusType.U32, ModbusUnit.VA, gain=0.001)  # gain=1000
reactive_power = ModbusRegister(11026, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000
pv_input_power = ModbusRegister(11028, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=0.001)  # gain=1000

# Power Factor and Temperature
power_factor = ModbusRegister(11030, 1, 3, ModbusType.S16, ModbusUnit.NONE, gain=0.001)  # gain=1000
temperature_1 = ModbusRegister(11032, 1, 3, ModbusType.S16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10
temperature_2 = ModbusRegister(11033, 1, 3, ModbusType.S16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10
temperature_3 = ModbusRegister(11034, 1, 3, ModbusType.S16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10
temperature_4 = ModbusRegister(11035, 1, 3, ModbusType.S16, ModbusUnit.CELSIUS, gain=0.1)  # gain=10

# Bus Voltage (gain=10)
bus_voltage = ModbusRegister(11036, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
nbus_voltage = ModbusRegister(11037, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)

# PV Input Parameters (gain=10)
pv1_voltage = ModbusRegister(11038, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
pv1_current = ModbusRegister(11039, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)
pv2_voltage = ModbusRegister(11040, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
pv2_current = ModbusRegister(11041, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)
pv3_voltage = ModbusRegister(11042, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
pv3_current = ModbusRegister(11043, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)
pv4_voltage = ModbusRegister(11044, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)
pv4_current = ModbusRegister(11045, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)

# PV Power (gain=1000)
pv1_power = ModbusRegister(11062, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=0.001)
pv2_power = ModbusRegister(11064, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=0.001)
pv3_power = ModbusRegister(11066, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=0.001)
pv4_power = ModbusRegister(11068, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=0.001)

# ARM Fault Flags
arm_fault_flag1 = ModbusRegister(18000, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)
arm_fault_flag2 = ModbusRegister(18004, 2, 3, ModbusType.U32, ModbusUnit.NONE, gain=1)

# Backup Parameters
backup_a_voltage = ModbusRegister(30200, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)  # gain=10
backup_a_current = ModbusRegister(30201, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
backup_a_frequency = ModbusRegister(30202, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, gain=0.01)  # gain=100
backup_a_power = ModbusRegister(30204, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
backup_a_reactive_power = ModbusRegister(30208, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000

# Battery Parameters
battery_voltage = ModbusRegister(30254, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)  # gain=10
battery_current = ModbusRegister(30255, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
battery_mode = ModbusRegister(30256, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
battery_power = ModbusRegister(30258, 2, 3, ModbusType.I32, ModbusUnit.WATT, gain=0.001)  # gain=1000

# Additional parameters for other registers follow the same pattern
# Time Group Settings
time_group_enable = ModbusRegister(21071, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group1_start = ModbusRegister(21072, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group1_end = ModbusRegister(21073, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group1_mode = ModbusRegister(21074, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Grid Protection Settings
grid_undervoltage1_limit = ModbusRegister(28004, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_undervoltage1_time = ModbusRegister(28005, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
grid_overvoltage1_limit = ModbusRegister(28006, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_overvoltage1_time = ModbusRegister(28007, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Frequency Protection Settings (gain=100 for frequency)
freq_underfreq1_limit = ModbusRegister(28012, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)
freq_underfreq1_time = ModbusRegister(28013, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
freq_overfreq1_limit = ModbusRegister(28014, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)
freq_overfreq1_time = ModbusRegister(28015, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Q(U) Mode Settings
qu_lock_in_power = ModbusRegister(28022, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_lock_out_power = ModbusRegister(28023, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_v1_point = ModbusRegister(28025, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
qu_q1_value = ModbusRegister(28026, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_v2_point = ModbusRegister(28027, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
qu_q2_value = ModbusRegister(28028, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_v3_point = ModbusRegister(28029, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
qu_q3_value = ModbusRegister(28030, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_v4_point = ModbusRegister(28031, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
qu_q4_value = ModbusRegister(28032, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10

# Cos(φ)(P) Mode Settings
cos_p_point_a_power = ModbusRegister(28035, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
cos_p_point_b_power = ModbusRegister(28036, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
cos_p_point_c_power = ModbusRegister(28037, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
cos_p_point_a_pf = ModbusRegister(28038, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.001)  # gain=1000
cos_p_point_b_pf = ModbusRegister(28039, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.001)  # gain=1000
cos_p_point_c_pf = ModbusRegister(28040, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.001)  # gain=1000
cos_p_lock_in_voltage = ModbusRegister(28041, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
cos_p_lock_out_voltage = ModbusRegister(28042, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
cos_p_exit_power = ModbusRegister(28043, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10

# Grid Connection Settings
grid_connection_enable = ModbusRegister(28044, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
grid_connection_startup_time = ModbusRegister(28045, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=1)
grid_connection_reconnect_time = ModbusRegister(28046, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=1)

# Grid Connection Voltage and Frequency Limits
grid_startup_min_voltage = ModbusRegister(28047, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_startup_max_voltage = ModbusRegister(28048, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_startup_min_freq = ModbusRegister(28049, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
grid_startup_max_freq = ModbusRegister(28050, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100

# Grid Reconnection Limits
grid_reconnect_min_voltage = ModbusRegister(28051, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_reconnect_max_voltage = ModbusRegister(28052, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_reconnect_min_freq = ModbusRegister(28053, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
grid_reconnect_max_freq = ModbusRegister(28054, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100

# P(U) Settings
pu_curve_enable = ModbusRegister(28055, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
pu_curve_start_voltage = ModbusRegister(28057, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
pu_curve_start_power = ModbusRegister(28058, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
pu_curve_end_voltage = ModbusRegister(28059, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
pu_curve_end_power = ModbusRegister(28060, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10

# LFSM-O Settings
lfsm_o_enable = ModbusRegister(28061, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
lfsm_o_start_freq = ModbusRegister(28063, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
lfsm_o_start_power = ModbusRegister(28064, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
lfsm_o_end_freq = ModbusRegister(28065, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
lfsm_o_end_power = ModbusRegister(28066, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
lfsm_o_recovery_freq = ModbusRegister(28067, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
lfsm_o_recovery_time = ModbusRegister(28068, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=1)
lfsm_o_recovery_power_ref = ModbusRegister(28069, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
lfsm_o_recovery_rate = ModbusRegister(28070, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10

# Power Ramp Rate
active_power_gradient = ModbusRegister(28072, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10

# UVRT and OVRT Settings
uvrt_zero_current_voltage = ModbusRegister(28073, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_recovery_voltage = ModbusRegister(28074, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_point1_voltage = ModbusRegister(28075, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_point2_voltage = ModbusRegister(28076, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_point3_voltage = ModbusRegister(28077, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_point4_voltage = ModbusRegister(28078, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_point5_voltage = ModbusRegister(28079, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
uvrt_point1_time = ModbusRegister(28080, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)  # accuracy=2
uvrt_point2_time = ModbusRegister(28081, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)
uvrt_point3_time = ModbusRegister(28082, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)
uvrt_point4_time = ModbusRegister(28083, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)
uvrt_point5_time = ModbusRegister(28084, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)
uvrt_enable = ModbusRegister(28085, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# OVRT Settings
ovrt_zero_current_voltage = ModbusRegister(28088, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
ovrt_recovery_voltage = ModbusRegister(28089, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
ovrt_point1_voltage = ModbusRegister(28090, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
ovrt_point2_voltage = ModbusRegister(28091, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
ovrt_point3_voltage = ModbusRegister(28092, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)
ovrt_point1_time = ModbusRegister(28093, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=1)
ovrt_point2_time = ModbusRegister(28094, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=1)
ovrt_point3_time = ModbusRegister(28095, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=1)
ovrt_enable = ModbusRegister(28096, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Additional Protection Settings
ten_min_overvoltage_enable = ModbusRegister(28101, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
ten_min_overvoltage_threshold = ModbusRegister(28102, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
qu_minimum_power_factor = ModbusRegister(28110, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.01)  # gain=100
qu_time_constant = ModbusRegister(28111, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=0.1)  # gain=10
pu_time_constant = ModbusRegister(28112, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=0.1)  # gain=10
overfreq_droop = ModbusRegister(28113, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RO, gain=0.1)  # gain=10

# Battery Configuration
battery_config = ModbusRegister(52500, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
battery_protocol_config = ModbusRegister(52501, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
on_grid_soc_protection = ModbusRegister(52502, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
on_grid_battery_soc_limit = ModbusRegister(52503, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
off_grid_soc_protection = ModbusRegister(52504, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
off_grid_battery_soc_limit = ModbusRegister(52505, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
end_soc_of_charging = ModbusRegister(52506, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10

# BMS Charge/Discharge Limits
bms_charge_end_voltage = ModbusRegister(52600, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
bms_charge_current_limit = ModbusRegister(52601, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, ModbusAccess.RW, gain=0.1)  # gain=10
bms_discharge_end_voltage = ModbusRegister(52602, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
bms_discharge_current_limit = ModbusRegister(52603, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, ModbusAccess.RW, gain=0.1)  # gain=10

# Parallel System Control
parallel_system_mode = ModbusRegister(52620, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
parallel_ac_power_control = ModbusRegister(52621, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
parallel_total_ac_power = ModbusRegister(52622, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10
parallel_phase_a_power = ModbusRegister(52623, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10
parallel_phase_b_power = ModbusRegister(52624, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10
parallel_phase_c_power = ModbusRegister(52625, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10
parallel_battery_power = ModbusRegister(52626, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10
parallel_export_power_limit = ModbusRegister(52627, 1, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10
parallel_import_power_limit = ModbusRegister(52628, 1, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.1)  # gain=10

# Time Period Control Parameters
time_period_control = ModbusRegister(53000, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
period_enable_flags = ModbusRegister(53006, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Period Settings (1-6)
# Period 1
period1_charge_discharge = ModbusRegister(53007, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period1_charge_source = ModbusRegister(53008, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period1_reserved1 = ModbusRegister(53009, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period1_power_limit = ModbusRegister(53010, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
period1_reserved2 = ModbusRegister(53011, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period1_start_time = ModbusRegister(53012, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
period1_end_time = ModbusRegister(53013, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# UVRT Settings
uvrt_zero_current_voltage = ModbusRegister(28073, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_recovery_voltage = ModbusRegister(28074, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_point1_voltage = ModbusRegister(28075, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_point2_voltage = ModbusRegister(28076, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_point3_voltage = ModbusRegister(28077, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_point4_voltage = ModbusRegister(28078, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_point5_voltage = ModbusRegister(28079, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=1/22.624)  # accuracy=22.624
uvrt_point1_time = ModbusRegister(28080, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)  # accuracy=2
uvrt_point2_time = ModbusRegister(28081, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)  # accuracy=2
uvrt_point3_time = ModbusRegister(28082, 1, 3, ModbusType.U16, ModbusUnit.MILLISECOND, ModbusAccess.RW, gain=0.5)  # accuracy=2
# Backup Parameters for Phase B
backup_b_voltage = ModbusRegister(30210, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)  # gain=10
backup_b_current = ModbusRegister(30211, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
backup_b_frequency = ModbusRegister(30212, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, gain=0.01)  # gain=100
backup_b_power = ModbusRegister(30214, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
backup_b_reactive_power = ModbusRegister(30218, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000

# Backup Parameters for Phase C
backup_c_voltage = ModbusRegister(30220, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)  # gain=10
backup_c_current = ModbusRegister(30221, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
backup_c_frequency = ModbusRegister(30222, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, gain=0.01)  # gain=100
backup_c_power = ModbusRegister(30224, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
backup_c_reactive_power = ModbusRegister(30228, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000

# Total Backup Power
backup_total_power = ModbusRegister(30230, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
backup_total_reactive_power = ModbusRegister(30234, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000

# Daily Energy Statistics
daily_grid_export = ModbusRegister(31000, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_grid_import = ModbusRegister(31001, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_backup_energy = ModbusRegister(31002, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_battery_charge = ModbusRegister(31003, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_battery_discharge = ModbusRegister(31004, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_pv_generation = ModbusRegister(31005, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_load_consumption = ModbusRegister(31006, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10
daily_grid_import_inverter = ModbusRegister(31008, 1, 3, ModbusType.U16, ModbusUnit.KWH, gain=0.1)  # gain=10

# Total Energy Statistics
total_grid_export = ModbusRegister(31102, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_grid_import = ModbusRegister(31104, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_backup_energy = ModbusRegister(31106, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_battery_charge = ModbusRegister(31108, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_battery_discharge = ModbusRegister(31110, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_pv_generation = ModbusRegister(31112, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_load_consumption = ModbusRegister(31114, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10
total_grid_import_inverter = ModbusRegister(31118, 2, 3, ModbusType.U32, ModbusUnit.KWH, gain=0.1)  # gain=10

# Load Power by Phase
load_power_a = ModbusRegister(31300, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
load_power_b = ModbusRegister(31302, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
load_power_c = ModbusRegister(31304, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
load_power_total = ModbusRegister(31306, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000

# Parallel System Statistics
parallel_pv_power = ModbusRegister(31308, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_battery_power = ModbusRegister(31310, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_ac_power = ModbusRegister(31312, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_phase_a_power = ModbusRegister(31314, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_phase_b_power = ModbusRegister(31316, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_phase_c_power = ModbusRegister(31318, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_rated_power = ModbusRegister(31320, 2, 3, ModbusType.U32, ModbusUnit.WATT, gain=0.001)  # gain=1000
parallel_total_soc = ModbusRegister(31322, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, gain=0.01)  # gain=100
parallel_slave_count = ModbusRegister(31323, 1, 3, ModbusType.U16, ModbusUnit.NONE, gain=1)
# Grid Export and Meter Settings
grid_export_power_switch = ModbusRegister(25100, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
grid_export_power_percent = ModbusRegister(25103, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
meter_comm_status = ModbusRegister(25104, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
meter_power_phase_a = ModbusRegister(25105, 2, 3, ModbusType.I32, ModbusUnit.WATT, ModbusAccess.WO, gain=1)
meter_power_phase_b = ModbusRegister(25107, 2, 3, ModbusType.I32, ModbusUnit.WATT, ModbusAccess.WO, gain=1)
meter_power_phase_c = ModbusRegister(25109, 2, 3, ModbusType.I32, ModbusUnit.WATT, ModbusAccess.WO, gain=1)

# Reactive Power Control
reactive_q_setpoint = ModbusRegister(25118, 1, 3, ModbusType.I16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
reactive_pf_setpoint = ModbusRegister(25120, 1, 3, ModbusType.I16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.001)  # gain=1000
reactive_control_mode = ModbusRegister(25121, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Storage System Parameters
working_mode = ModbusRegister(50000, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
parallel_mode = ModbusRegister(50010, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
npe_detection = ModbusRegister(50011, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
min_soc_protect = ModbusRegister(50012, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
off_grid_parallel_num = ModbusRegister(50013, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
off_grid_parallel_addr = ModbusRegister(50014, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Write-Only Operation Registers
aux_power_switch = ModbusRegister(50200, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
clear_overload_flag = ModbusRegister(50201, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)

# ToU parameters
tou_subwork_mode = ModbusRegister(53076, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Additional Battery Cell Parameters
battery_charge_cutoff_voltage = ModbusRegister(33020, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)  # gain=10
battery_charge_current_limit = ModbusRegister(33021, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10
battery_discharge_cutoff_voltage = ModbusRegister(33022, 1, 3, ModbusType.U16, ModbusUnit.VOLT, gain=0.1)  # gain=10
battery_discharge_current_limit = ModbusRegister(33023, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, gain=0.1)  # gain=10

# Inverter Phase Power Parameters
inverter_phase_a_power = ModbusRegister(30236, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
inverter_phase_a_apparent_power = ModbusRegister(30238, 2, 3, ModbusType.U32, ModbusUnit.VA, gain=0.001)  # gain=1000
inverter_phase_a_reactive_power = ModbusRegister(30240, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000
inverter_phase_b_power = ModbusRegister(30242, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
inverter_phase_b_apparent_power = ModbusRegister(30244, 2, 3, ModbusType.U32, ModbusUnit.VA, gain=0.001)  # gain=1000
inverter_phase_b_reactive_power = ModbusRegister(30246, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000
inverter_phase_c_power = ModbusRegister(30248, 2, 3, ModbusType.S32, ModbusUnit.WATT, gain=0.001)  # gain=1000
inverter_phase_c_apparent_power = ModbusRegister(30250, 2, 3, ModbusType.U32, ModbusUnit.VA, gain=0.001)  # gain=1000
inverter_phase_c_reactive_power = ModbusRegister(30252, 2, 3, ModbusType.S32, ModbusUnit.VAR, gain=0.001)  # gain=1000

# Power Control Settings
pc_ac_power_scheduling_mode_setting = ModbusRegister(50202, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
pc_total_ac_power_target = ModbusRegister(50203, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_phase_a_power_target = ModbusRegister(50204, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_phase_b_power_target = ModbusRegister(50205, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_phase_c_power_target = ModbusRegister(50206, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_battery_power_target = ModbusRegister(50207, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_ac_power_max_limit = ModbusRegister(50208, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_ac_power_min_limit = ModbusRegister(50209, 1, 3, ModbusType.I16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
pc_power_output_priority = ModbusRegister(50210, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
pc_pv_power_target = ModbusRegister(50211, 1, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100
# Time Group Settings for Additional Groups
time_group2_start = ModbusRegister(21076, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group2_end = ModbusRegister(21077, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group2_mode = ModbusRegister(21078, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group3_start = ModbusRegister(21080, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group3_end = ModbusRegister(21081, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
time_group3_mode = ModbusRegister(21082, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Grid Protection Settings - Level 2 Frequency
freq_underfreq2_limit = ModbusRegister(28016, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
freq_underfreq2_time = ModbusRegister(28017, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
freq_overfreq2_limit = ModbusRegister(28018, 1, 3, ModbusType.U16, ModbusUnit.HERTZ, ModbusAccess.RW, gain=0.01)  # gain=100
freq_overfreq2_time = ModbusRegister(28019, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Q(U) Settings
qu_lock_in_power = ModbusRegister(28022, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_lock_out_power = ModbusRegister(28023, 1, 3, ModbusType.U16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
qu_minimum_power_factor = ModbusRegister(28110, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.01)  # gain=100
qu_time_constant = ModbusRegister(28111, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=0.1)  # gain=10

# Additional Control Parameters
power_switch = ModbusRegister(25008, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
aux_power_restart = ModbusRegister(25009, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
overload_mode = ModbusRegister(25015, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
system_control = ModbusRegister(25016, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
shadow_scan = ModbusRegister(25020, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
pv_module_control = ModbusRegister(25021, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Communication Configuration
comm_watchdog = ModbusRegister(20085, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
duocom_work_mode = ModbusRegister(20151, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
modbus_tcp_internet = ModbusRegister(20152, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
comm_module_reset = ModbusRegister(20153, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)

# DO and Load Management
do1_definition = ModbusRegister(21034, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
load_control_mode = ModbusRegister(21037, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# SG-Ready Mode Settings
sg_ready_mode3_min_runtime = ModbusRegister(21042, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
sg_ready_mode3_max_runtime = ModbusRegister(21044, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
sg_ready_mode3_smart_mode = ModbusRegister(21045, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
sg_ready_mode3_start_power = ModbusRegister(21046, 2, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=1)
sg_ready_mode3_exit_power = ModbusRegister(21048, 2, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=1)
sg_ready_mode3_start_soc = ModbusRegister(21050, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
sg_ready_mode3_exit_soc = ModbusRegister(21051, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Device RTC Time Registers
rtc_year_month = ModbusRegister(20000, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
rtc_day_hour = ModbusRegister(20001, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
rtc_minute_second = ModbusRegister(20002, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Safety Parameters
safety_code = ModbusRegister(25000, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
safety_parameters_save = ModbusRegister(28300, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)

# Battery and BMS Parameters
battery_config = ModbusRegister(52500, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
battery_protocol_config = ModbusRegister(52501, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
battery_version = ModbusRegister(53500, 8, 3, ModbusType.STRING, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
battery_error1_code = ModbusRegister(53509, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
battery_error2_code = ModbusRegister(53511, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
battery_info_code = ModbusRegister(53513, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)
battery_warning_code = ModbusRegister(53525, 2, 3, ModbusType.U32, ModbusUnit.NONE, ModbusAccess.WO, gain=1)

# Time Period Control Parameters
time_period_control = ModbusRegister(53000, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.WO, gain=1)

# Reactive Power Control
reactive_q_setpoint = ModbusRegister(25118, 1, 3, ModbusType.I16, ModbusUnit.PERCENTAGE, ModbusAccess.RW, gain=0.1)  # gain=10
reactive_pf_setpoint = ModbusRegister(25120, 1, 3, ModbusType.I16, ModbusUnit.NONE, ModbusAccess.RW, gain=0.001)  # gain=1000
reactive_control_mode = ModbusRegister(25121, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)

# Grid Protection Settings - Additional Parameters
grid_connection_enable = ModbusRegister(28044, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
grid_connection_startup_time = ModbusRegister(28045, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=1)
grid_connection_reconnect_time = ModbusRegister(28046, 1, 3, ModbusType.U16, ModbusUnit.SECOND, ModbusAccess.RW, gain=1)

# Grid Protection Settings - Voltage and Frequency Limits
grid_undervoltage1_limit = ModbusRegister(28004, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_overvoltage1_limit = ModbusRegister(28006, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_undervoltage2_limit = ModbusRegister(28008, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10
grid_overvoltage2_limit = ModbusRegister(28010, 1, 3, ModbusType.U16, ModbusUnit.VOLT, ModbusAccess.RW, gain=0.1)  # gain=10

# Power Control Settings
power_output_priority = ModbusRegister(50210, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
pv_power_setpoint = ModbusRegister(50211, 1, 3, ModbusType.U16, ModbusUnit.WATT, ModbusAccess.RW, gain=0.01)  # gain=100

# Communication and System Management
comm_watchdog = ModbusRegister(20085, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
do1_definition = ModbusRegister(21034, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
manual_relay_status = ModbusRegister(21038, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
grid_undervoltage2_time = ModbusRegister(28009, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)
grid_overvoltage2_time = ModbusRegister(28011, 1, 3, ModbusType.U16, ModbusUnit.NONE, ModbusAccess.RW, gain=1)