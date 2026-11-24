# ─── Read-Only: AC Output ───────────────────────────────────────────────────
output_voltage_ab_n = "OutputVoltageAB"
output_voltage_bc_n = "OutputVoltageBC"
output_voltage_ca_n = "OutputVoltageCA"
output_voltage_a_n = "OutputVoltageA"
output_voltage_b_n = "OutputVoltageB"
output_voltage_c_n = "OutputVoltageC"
output_current_a_n = "OutputCurrentA"
output_current_b_n = "OutputCurrentB"
output_current_c_n = "OutputCurrentC"
inductance_current_a_n = "InductanceCurrentA"
inductance_current_b_n = "InductanceCurrentB"
inductance_current_c_n = "InductanceCurrentC"
grid_frequency_n = "GridFrequency"
grid_phase_sequence_n = "GridPhaseSequence"
pcs_derating_coefficient_n = "PcsDeratingCoefficient"
pcs_derating_mark_n = "PcsDeratingMark"

# ─── Read-Only: AC Power ─────────────────────────────────────────────────────
ac_active_power_a_n = "AcActivePowerA"
ac_active_power_b_n = "AcActivePowerB"
ac_active_power_c_n = "AcActivePowerC"
ac_apparent_power_a_n = "AcApparentPowerA"
ac_apparent_power_b_n = "AcApparentPowerB"
ac_apparent_power_c_n = "AcApparentPowerC"
ac_reactive_power_a_n = "AcReactivePowerA"
ac_reactive_power_b_n = "AcReactivePowerB"
ac_reactive_power_c_n = "AcReactivePowerC"
ac_total_active_power_n = "AcTotalActivePower"
ac_total_reactive_power_n = "AcTotalReactivePower"
ac_total_apparent_power_n = "AcTotalApparentPower"
ac_power_factor_n = "AcPowerFactor"
power_factor_a_n = "PowerFactorA"
power_factor_b_n = "PowerFactorB"
power_factor_c_n = "PowerFactorC"

# ─── Read-Only: DC / Bus ─────────────────────────────────────────────────────
total_bus_voltage_n = "TotalBusVoltage"
positive_bus_voltage_n = "PositiveBusVoltage"
negative_bus_voltage_n = "NegativeBusVoltage"
battery_voltage_n = "BatteryVoltage"
battery_current_n = "BatteryCurrent"
dc_power_n = "DcPower"
total_dc_current_n = "TotalDcCurrent"

# ─── Read-Only: Status & Temperature ─────────────────────────────────────────
working_condition_n = "WorkingCondition"
igbt_temperature_n = "IgbtTemperature"
ambient_temperature_n = "AmbientTemperature"
inductance_temperature_n = "InductanceTemperature"
charge_discharge_mode_n = "ChargeDischargeMode"
grid_offgrid_state_n = "GridOffGridState"

# ─── Read-Only: Version ───────────────────────────────────────────────────────
dsp_version_v_n = "DspVersionV"
dsp_version_b_n = "DspVersionB"
dsp_version_d_n = "DspVersionD"
cpld_version_v_n = "CpldVersionV"
cpld_version_b_n = "CpldVersionB"
cpld_version_d_n = "CpldVersionD"

# ─── Read-Only: Energy (32-bit pairs) ────────────────────────────────────────
dc_history_charge_n = "DcHistoryCharge"
dc_daily_charge_n = "DcDailyCharge"
dc_history_discharge_n = "DcHistoryDischarge"
dc_daily_discharge_n = "DcDailyDischarge"
ac_history_charge_n = "AcHistoryCharge"
ac_daily_charge_n = "AcDailyCharge"
ac_history_discharge_n = "AcHistoryDischarge"
ac_daily_discharge_n = "AcDailyDischarge"

# ─── Read-Only: Insulation ────────────────────────────────────────────────────
insulation_rx_n = "InsulationRx"
insulation_ry_n = "InsulationRy"

# ─── Read-Only: Module SN ────────────────────────────────────────────────────
module_sn_n = "ModuleSN"

# ─── Read-Only: Fault Words ──────────────────────────────────────────────────
hw_fault_word1_n = "HwFaultWord1"
hw_fault_word2_n = "HwFaultWord2"
grid_fault_word_n = "GridFaultWord"
bus_fault_word_n = "BusFaultWord"
ac_cap_fault_word_n = "AcCapFaultWord"
system_fault_word_n = "SystemFaultWord"
switch_fault_word_n = "SwitchFaultWord"
other_fault_word_n = "OtherFaultWord"

# ─── Read/Write: BMS / CAN Settings ──────────────────────────────────────────
bms_manufacturer_info_n = "BmsManufacturerInfo"
can_baud_rate_non_std_n = "CanBaudRateNonStd"
harmonic_control_config4_n = "HarmonicControlConfig4"

# ─── Main Contactor ──────────────────────────────────────────────────────────
main_contactor_command_status_n = "MainContactorCommandStatus"
main_contactor_state_machine_n = "MainContactorStateMachine"
main_contactor_status_n = "MainContactorStatus"
main_contactor_closing_time_n = "MainContactorClosingTime"
main_contactor_opening_time_n = "MainContactorOpeningTime"

# ─── Read/Write: Power Setpoints ─────────────────────────────────────────────
set_active_power_n = "SetActivePower"
set_reactive_power_n = "SetReactivePower"
set_phase_a_active_power_n = "SetPhaseAActivePower"
set_phase_a_reactive_power_n = "SetPhaseAReactivePower"
set_phase_b_active_power_n = "SetPhaseBActivePower"
set_phase_b_reactive_power_n = "SetPhaseBReactivePower"
set_phase_c_active_power_n = "SetPhaseCActivePower"
set_phase_c_reactive_power_n = "SetPhaseCReactivePower"

# ─── Read/Write: Mode & Configuration ────────────────────────────────────────
offgrid_mode_n = "OffGridMode"
operation_mode_n = "OperationMode"
single_phase_power_control_n = "SinglePhasePowerControl"
module_host_n = "ModuleHost"
current_source_parallel_enable_n = "CurrentSourceParallelEnable"
dehumidification_enable_n = "DehumidificationEnable"
parallel_module_count_n = "ParallelModuleCount"
offgrid_voltage_n = "OffGridVoltage"
offgrid_frequency_n = "OffGridFrequency"
insulation_detection_enable_n = "InsulationDetectionEnable"
max_charge_power_n = "MaxChargePower"
max_discharge_power_n = "MaxDischargePower"
max_charge_current_battery_n = "MaxChargeCurrentBattery"
max_discharge_current_battery_n = "MaxDischargeCurrentBattery"
dc_source_bus_voltage_n = "DcSourceBusVoltage"
bus_voltage_n = "BusVoltage"

# ─── Read/Write: Protection Parameters ───────────────────────────────────────
grid_overfreq_protection_n = "GridOverfreqProtection"
grid_underfreq_protection_n = "GridUnderfreqProtection"
island_overfreq_protection_n = "IslandOverfreqProtection"
island_underfreq_protection_n = "IslandUnderfreqProtection"
battery_overvoltage_protection_n = "BatteryOvervoltageProtection"
battery_undervoltage_protection_n = "BatteryUndervoltageProtection"
busbar_overvoltage_protection_n = "BusbarOvervoltageProtection"
busbar_undervoltage_protection_n = "BusbarUndervoltageProtection"
dc_overcurrent_protection_n = "DcOvercurrentProtection"
ac_overvoltage_protection_n = "AcOvervoltageProtection"
ac_undervoltage_protection_n = "AcUndervoltageProtection"
ac_overcurrent_protection_n = "AcOvercurrentProtection"
overtemperature_protection_n = "OvertemperatureProtection"

# ─── Read/Write: Battery Charging Parameters ─────────────────────────────────
cc_cv_battery_voltage_n = "CcCvBatteryVoltage"
constant_voltage_charging_n = "ConstantVoltageCharging"
max_cv_time_n = "MaxCvTime"
cv_to_float_current_n = "CvToFloatCurrent"
float_charge_voltage_n = "FloatChargeVoltage"
float_to_cc_current_n = "FloatToCcCurrent"

# ─── Read/Write: Control Commands ────────────────────────────────────────────
power_on_off_n = "PowerOnOff"
fault_reset_n = "FaultReset"
cure_parameter_n = "CureParameter"
charge_reset_n = "ChargeReset"
safety_one_key_n = "SafetyOneKey"

# ─── Read/Write: Communication ───────────────────────────────────────────────
remodbus_address_n = "RemodbusAddress"
remodbus_baud_rate_n = "RemodbusBaudRate"
hmi_modbus_address_n = "HmiModbusAddress"
hmi_modbus_baud_rate_n = "HmiModbusBaudRate"
ems_comm_timeout_n = "EmsCommTimeout"

# ─── Write-Only: Timing ──────────────────────────────────────────────────────
time_year_n = "TimeYear"
time_month_n = "TimeMonth"
time_day_n = "TimeDay"
time_hour_n = "TimeHour"
time_minute_n = "TimeMinute"
time_second_n = "TimeSecond"
