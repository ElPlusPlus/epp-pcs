from pypcs.definition.models import ModbusRegister, ModbusType, ModbusUnit, ModbusAccess

RO = ModbusAccess.RO
RW = ModbusAccess.RW
WO = ModbusAccess.WO

# ─── Read-Only: AC Output Voltages & Currents ────────────────────────────────
# 0x6020-0x602B  I16, FC3
output_voltage_ab   = ModbusRegister(0x6020, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
output_voltage_bc   = ModbusRegister(0x6021, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
output_voltage_ca   = ModbusRegister(0x6022, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
output_voltage_a    = ModbusRegister(0x6023, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
output_voltage_b    = ModbusRegister(0x6024, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
output_voltage_c    = ModbusRegister(0x6025, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
output_current_a    = ModbusRegister(0x6026, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)
output_current_b    = ModbusRegister(0x6027, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)
output_current_c    = ModbusRegister(0x6028, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)
inductance_current_a = ModbusRegister(0x6029, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)
inductance_current_b = ModbusRegister(0x602A, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)
inductance_current_c = ModbusRegister(0x602B, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)

# Grid frequency & phase
grid_frequency       = ModbusRegister(0x602C, 1, 3, ModbusType.I16, ModbusUnit.HERTZ, RO, gain=0.01)
grid_phase_sequence  = ModbusRegister(0x602D, 1, 3, ModbusType.I16, ModbusUnit.NONE,  RO, gain=1)

# PCS derating (software ≥5.13.0)
pcs_derating_coefficient = ModbusRegister(0x602E, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=1)
pcs_derating_mark        = ModbusRegister(0x602F, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=1)

# ─── Read-Only: AC Power ─────────────────────────────────────────────────────
# 0x6030-0x603C  I16, FC3
# positive = discharge, negative = charge
ac_active_power_a    = ModbusRegister(0x6030, 1, 3, ModbusType.I16, ModbusUnit.KW,   RO, gain=0.1)
ac_active_power_b    = ModbusRegister(0x6031, 1, 3, ModbusType.I16, ModbusUnit.KW,   RO, gain=0.1)
ac_active_power_c    = ModbusRegister(0x6032, 1, 3, ModbusType.I16, ModbusUnit.KW,   RO, gain=0.1)
ac_apparent_power_a  = ModbusRegister(0x6033, 1, 3, ModbusType.I16, ModbusUnit.KVA,  RO, gain=0.1)
ac_apparent_power_b  = ModbusRegister(0x6034, 1, 3, ModbusType.I16, ModbusUnit.KVA,  RO, gain=0.1)
ac_apparent_power_c  = ModbusRegister(0x6035, 1, 3, ModbusType.I16, ModbusUnit.KVA,  RO, gain=0.1)
# positive = inductive, negative = capacitive
ac_reactive_power_a  = ModbusRegister(0x6036, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RO, gain=0.1)
ac_reactive_power_b  = ModbusRegister(0x6037, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RO, gain=0.1)
ac_reactive_power_c  = ModbusRegister(0x6038, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RO, gain=0.1)
ac_total_active_power  = ModbusRegister(0x6039, 1, 3, ModbusType.I16, ModbusUnit.KW,   RO, gain=0.1)
ac_total_reactive_power = ModbusRegister(0x603A, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RO, gain=0.1)
ac_total_apparent_power = ModbusRegister(0x603B, 1, 3, ModbusType.I16, ModbusUnit.KVA,  RO, gain=0.1)
ac_power_factor        = ModbusRegister(0x603C, 1, 3, ModbusType.I16, ModbusUnit.NONE,  RO, gain=0.01)

# Per-phase power factor (different address range)
power_factor_a = ModbusRegister(0x0189, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=0.01)
power_factor_b = ModbusRegister(0x018A, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=0.01)
power_factor_c = ModbusRegister(0x018B, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=0.01)

# ─── Read-Only: DC / Bus ─────────────────────────────────────────────────────
total_bus_voltage   = ModbusRegister(0x6050, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
positive_bus_voltage = ModbusRegister(0x6051, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
negative_bus_voltage = ModbusRegister(0x6052, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
battery_voltage     = ModbusRegister(0x6053, 1, 3, ModbusType.I16, ModbusUnit.VOLT,   RO, gain=0.1)
battery_current     = ModbusRegister(0x6054, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)
dc_power            = ModbusRegister(0x6055, 1, 3, ModbusType.I16, ModbusUnit.KW,     RO, gain=0.1)
total_dc_current    = ModbusRegister(0x6056, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RO, gain=0.1)

# ─── Read-Only: Status ───────────────────────────────────────────────────────
# Bit flags – returned as raw U16 (use B16 for binary display)
working_condition       = ModbusRegister(0x6057, 1, 3, ModbusType.B16,  ModbusUnit.NONE, RO, gain=1)
igbt_temperature        = ModbusRegister(0x6058, 1, 3, ModbusType.I16,  ModbusUnit.CELSIUS, RO, gain=0.1)
ambient_temperature     = ModbusRegister(0x6059, 1, 3, ModbusType.I16,  ModbusUnit.CELSIUS, RO, gain=0.1)
inductance_temperature  = ModbusRegister(0x605A, 1, 3, ModbusType.I16,  ModbusUnit.CELSIUS, RO, gain=0.1)
charge_discharge_mode   = ModbusRegister(0x605B, 1, 3, ModbusType.U16,  ModbusUnit.NONE, RO, gain=1)
# 0=Stop 1=PowerOn 2=Standby 3=OffGrid 4=GridConnected 5=Fault 6=Debug
grid_offgrid_state      = ModbusRegister(0x605C, 1, 3, ModbusType.U16,  ModbusUnit.NONE, RO, gain=1)

# ─── Read-Only: Software Versions ────────────────────────────────────────────
dsp_version_v  = ModbusRegister(0x6000, 1, 3, ModbusType.U16, ModbusUnit.NONE, RO, gain=1)
dsp_version_b  = ModbusRegister(0x6001, 1, 3, ModbusType.U16, ModbusUnit.NONE, RO, gain=1)
dsp_version_d  = ModbusRegister(0x6002, 1, 3, ModbusType.U16, ModbusUnit.NONE, RO, gain=1)
cpld_version_v = ModbusRegister(0x6003, 1, 3, ModbusType.U16, ModbusUnit.NONE, RO, gain=1)
cpld_version_b = ModbusRegister(0x6004, 1, 3, ModbusType.U16, ModbusUnit.NONE, RO, gain=1)
cpld_version_d = ModbusRegister(0x6005, 1, 3, ModbusType.U16, ModbusUnit.NONE, RO, gain=1)

# ─── Read-Only: Energy Counters (32-bit, high + low word) ───────────────────
# Each entry uses 2 consecutive registers; read with count=2 → U32 in kWh
dc_history_charge    = ModbusRegister(0x6010, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
dc_daily_charge      = ModbusRegister(0x6012, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
dc_history_discharge = ModbusRegister(0x6014, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
dc_daily_discharge   = ModbusRegister(0x6016, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
ac_history_charge    = ModbusRegister(0x6018, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
ac_daily_charge      = ModbusRegister(0x601A, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
ac_history_discharge = ModbusRegister(0x601C, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)
ac_daily_discharge   = ModbusRegister(0x601E, 2, 3, ModbusType.U32, ModbusUnit.KWH, RO, gain=1)

# ─── Read-Only: Insulation ────────────────────────────────────────────────────
insulation_rx = ModbusRegister(0x0913, 1, 3, ModbusType.U16, ModbusUnit.KOHM, RO, gain=1)
insulation_ry = ModbusRegister(0x0914, 1, 3, ModbusType.U16, ModbusUnit.KOHM, RO, gain=1)

# ─── Read-Only: Module SN (16 registers = 32 ASCII chars) ────────────────────
module_sn = ModbusRegister(0x6070, 16, 3, ModbusType.STRING, ModbusUnit.NONE, RO, gain=1)

# ─── Read-Only: Fault Words ──────────────────────────────────────────────────
hw_fault_word1   = ModbusRegister(0x1700, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
hw_fault_word2   = ModbusRegister(0x1701, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
grid_fault_word  = ModbusRegister(0x1702, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
bus_fault_word   = ModbusRegister(0x1703, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
ac_cap_fault_word   = ModbusRegister(0x1704, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
system_fault_word   = ModbusRegister(0x1705, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
switch_fault_word   = ModbusRegister(0x1706, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
other_fault_word    = ModbusRegister(0x1707, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)

# ─── Read/Write: BMS / CAN Settings ──────────────────────────────────────────
# 0x0C52-0x0C56  U16, FC3
bms_manufacturer_info = ModbusRegister(0x0C52, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
can_baud_rate_non_std = ModbusRegister(0x0C56, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)

# ─── Main Contactor ──────────────────────────────────────────────────────────
# 0x0E00-0x0E04  FC3
main_contactor_command_status = ModbusRegister(0x0E00, 1, 3, ModbusType.B16, ModbusUnit.NONE, RO, gain=1)
main_contactor_state_machine  = ModbusRegister(0x0E01, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=1)
main_contactor_status         = ModbusRegister(0x0E02, 1, 3, ModbusType.I16, ModbusUnit.NONE, RO, gain=1)
main_contactor_closing_time   = ModbusRegister(0x0E03, 1, 3, ModbusType.I16, ModbusUnit.NONE, RW, gain=1)
main_contactor_opening_time   = ModbusRegister(0x0E04, 1, 3, ModbusType.I16, ModbusUnit.NONE, RW, gain=1)

# ─── Read/Write: Power Setpoints ─────────────────────────────────────────────
# positive = discharge, negative = charge
set_active_power   = ModbusRegister(0x0D57, 1, 3, ModbusType.I16, ModbusUnit.KW,   RW, gain=0.1)
set_reactive_power = ModbusRegister(0x0D58, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RW, gain=0.1)

# Single-phase power control (enabled via 0x5060)
set_phase_a_active_power   = ModbusRegister(0x02A6, 1, 3, ModbusType.I16, ModbusUnit.KW,   RW, gain=0.1)
set_phase_a_reactive_power = ModbusRegister(0x02A7, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RW, gain=0.1)
set_phase_b_active_power   = ModbusRegister(0x02A8, 1, 3, ModbusType.I16, ModbusUnit.KW,   RW, gain=0.1)
set_phase_b_reactive_power = ModbusRegister(0x02A9, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RW, gain=0.1)
set_phase_c_active_power   = ModbusRegister(0x02AA, 1, 3, ModbusType.I16, ModbusUnit.KW,   RW, gain=0.1)
set_phase_c_reactive_power = ModbusRegister(0x02AB, 1, 3, ModbusType.I16, ModbusUnit.KVAR, RW, gain=0.1)

# ─── Read/Write: Mode & Configuration ────────────────────────────────────────
offgrid_mode              = ModbusRegister(0x5066, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
operation_mode            = ModbusRegister(0x501B, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
single_phase_power_control = ModbusRegister(0x5060, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
module_host               = ModbusRegister(0x5068, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
current_source_parallel_enable = ModbusRegister(0x5054, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
dehumidification_enable   = ModbusRegister(0x506A, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
parallel_module_count     = ModbusRegister(0x5021, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
# default 4096 = 400 V, 3891 = 380 V
offgrid_voltage           = ModbusRegister(0x2227, 1, 3, ModbusType.I16, ModbusUnit.NONE, RW, gain=1)
# unit Hz, ×100 (e.g. 5000 = 50 Hz)
offgrid_frequency         = ModbusRegister(0x0103, 1, 3, ModbusType.I16, ModbusUnit.HERTZ, RW, gain=0.01)
insulation_detection_enable = ModbusRegister(0x0900, 1, 3, ModbusType.I16, ModbusUnit.NONE, RW, gain=1)
max_charge_power          = ModbusRegister(0x5078, 1, 3, ModbusType.I16, ModbusUnit.KW,   RW, gain=0.1)
max_discharge_power       = ModbusRegister(0x5079, 1, 3, ModbusType.I16, ModbusUnit.KW,   RW, gain=0.1)
max_charge_current_battery    = ModbusRegister(0x163F, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RW, gain=0.1)
max_discharge_current_battery = ModbusRegister(0x1640, 1, 3, ModbusType.I16, ModbusUnit.AMPERE, RW, gain=0.1)
# Bus voltage (DC voltage source mode, parallel)
dc_source_bus_voltage     = ModbusRegister(0x0D16, 1, 3, ModbusType.U16, ModbusUnit.VOLT, RW, gain=0.1)
# Bus voltage (DC voltage source mode, single module)
bus_voltage               = ModbusRegister(0x0D10, 1, 3, ModbusType.U16, ModbusUnit.VOLT, RW, gain=0.1)

# ─── Read/Write: Protection Parameters ───────────────────────────────────────
grid_overfreq_protection      = ModbusRegister(0x1604, 1, 3, ModbusType.U16, ModbusUnit.HERTZ,   RW, gain=0.01)
grid_underfreq_protection     = ModbusRegister(0x1605, 1, 3, ModbusType.U16, ModbusUnit.HERTZ,   RW, gain=0.01)
island_overfreq_protection    = ModbusRegister(0x1631, 1, 3, ModbusType.U16, ModbusUnit.HERTZ,   RW, gain=0.01)
island_underfreq_protection   = ModbusRegister(0x1632, 1, 3, ModbusType.U16, ModbusUnit.HERTZ,   RW, gain=0.01)
battery_overvoltage_protection  = ModbusRegister(0x1633, 1, 3, ModbusType.U16, ModbusUnit.VOLT,  RW, gain=0.1)
battery_undervoltage_protection = ModbusRegister(0x1634, 1, 3, ModbusType.U16, ModbusUnit.VOLT,  RW, gain=0.1)
busbar_overvoltage_protection   = ModbusRegister(0x1611, 1, 3, ModbusType.U16, ModbusUnit.VOLT,  RW, gain=0.1)
busbar_undervoltage_protection  = ModbusRegister(0x1612, 1, 3, ModbusType.U16, ModbusUnit.VOLT,  RW, gain=0.1)
dc_overcurrent_protection       = ModbusRegister(0x1641, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, RW, gain=0.1)
ac_overvoltage_protection       = ModbusRegister(0x1600, 1, 3, ModbusType.U16, ModbusUnit.VOLT,  RW, gain=0.1)
ac_undervoltage_protection      = ModbusRegister(0x1601, 1, 3, ModbusType.U16, ModbusUnit.VOLT,  RW, gain=0.1)
ac_overcurrent_protection       = ModbusRegister(0x1603, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, RW, gain=0.1)
overtemperature_protection      = ModbusRegister(0x1620, 1, 3, ModbusType.U16, ModbusUnit.CELSIUS, RW, gain=0.1)

# ─── Read/Write: Battery Charging Parameters ─────────────────────────────────
cc_cv_battery_voltage = ModbusRegister(0x1643, 1, 3, ModbusType.U16, ModbusUnit.VOLT,   RW, gain=0.1)
constant_voltage_charging = ModbusRegister(0x1644, 1, 3, ModbusType.U16, ModbusUnit.VOLT,   RW, gain=0.1)
max_cv_time           = ModbusRegister(0x1650, 1, 3, ModbusType.U16, ModbusUnit.MINUTE, RW, gain=0.1)
cv_to_float_current   = ModbusRegister(0x1651, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, RW, gain=0.1)
float_charge_voltage  = ModbusRegister(0x1653, 1, 3, ModbusType.U16, ModbusUnit.VOLT,   RW, gain=0.1)
float_to_cc_current   = ModbusRegister(0x1654, 1, 3, ModbusType.U16, ModbusUnit.AMPERE, RW, gain=0.1)

# ─── Read/Write: Control Commands ────────────────────────────────────────────
# write 1 = on, write 0 = off
power_on_off    = ModbusRegister(0x0291, 1, 3, ModbusType.I16, ModbusUnit.NONE, RW, gain=1)
# set Bit15 to 1 to reset (in off state)
fault_reset     = ModbusRegister(0x1400, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
# write 0x0100 to cure; auto-clears; one-time only
cure_parameter  = ModbusRegister(0x1405, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
# write 1 to clear charge history (off state only)
charge_reset    = ModbusRegister(0x508C, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
safety_one_key  = ModbusRegister(0x508D, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)

# ─── Read/Write: Communication ───────────────────────────────────────────────
remodbus_address  = ModbusRegister(0x1010, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
remodbus_baud_rate = ModbusRegister(0x1007, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
hmi_modbus_address = ModbusRegister(0x1011, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
hmi_modbus_baud_rate = ModbusRegister(0x1004, 1, 3, ModbusType.U16, ModbusUnit.NONE, RW, gain=1)
ems_comm_timeout  = ModbusRegister(0x1648, 1, 3, ModbusType.U16, ModbusUnit.SECOND, RW, gain=1)

# ─── Write-Only: Timing ──────────────────────────────────────────────────────
time_year   = ModbusRegister(0x1020, 1, 3, ModbusType.U16, ModbusUnit.NONE, WO, gain=1)
time_month  = ModbusRegister(0x1021, 1, 3, ModbusType.U16, ModbusUnit.NONE, WO, gain=1)
time_day    = ModbusRegister(0x1022, 1, 3, ModbusType.U16, ModbusUnit.NONE, WO, gain=1)
time_hour   = ModbusRegister(0x1023, 1, 3, ModbusType.U16, ModbusUnit.NONE, WO, gain=1)
time_minute = ModbusRegister(0x1024, 1, 3, ModbusType.U16, ModbusUnit.NONE, WO, gain=1)
time_second = ModbusRegister(0x1025, 1, 3, ModbusType.U16, ModbusUnit.NONE, WO, gain=1)
