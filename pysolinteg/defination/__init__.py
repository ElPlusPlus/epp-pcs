from pysolinteg.defination.register_names import *
from pysolinteg.defination.register_values import *

modbus_map = {
    # Device Information
    device_sn_n: device_sn,
    device_model_n: device_model,
    firmware_major_version_n: firmware_major_version,
    firmware_minor_version_n: firmware_minor_version,
    inverter_rated_power_n: inverter_rated_power,
    inverter_max_power_output_n: inverter_max_power_output,

    # Time Related
    time_year_month_n: time_year_month,
    time_day_hour_n: time_day_hour,
    time_minute_second_n: time_minute_second,

    # System Status
    safety_code_n: safety_code,
    inverter_status_n: inverter_status,
    inverter_flags_n: inverter_flags,
    fault_flag1_n: fault_flag1,
    fault_flag2_n: fault_flag2,
    fault_flag3_n: fault_flag3,

    meter_current_phase_a_n: meter_current_phase_a,
    meter_current_phase_b_n: meter_current_phase_b,
    meter_current_phase_c_n: meter_current_phase_c,

    # Meter Reactive Power
    meter_reactive_power_a_n: meter_reactive_power_a,
    meter_reactive_power_b_n: meter_reactive_power_b,
    meter_reactive_power_c_n: meter_reactive_power_c,
    meter_reactive_power_total_n: meter_reactive_power_total,

    # Meter Active Power
    meter_active_power_a_n: meter_active_power_a,
    meter_active_power_b_n: meter_active_power_b,
    meter_active_power_c_n: meter_active_power_c,
    meter_active_power_total_n: meter_active_power_total,

    # Energy Meters
    meter_export_energy_n: meter_export_energy,
    meter_import_energy_n: meter_import_energy,

    # Inverter Side Voltages and Currents
    inverter_voltage_ab_n: inverter_voltage_ab,
    inverter_voltage_bc_n: inverter_voltage_bc,
    inverter_voltage_ca_n: inverter_voltage_ca,
    inverter_voltage_a_n: inverter_voltage_a,
    inverter_current_a_n: inverter_current_a,
    inverter_voltage_b_n: inverter_voltage_b,
    inverter_current_b_n: inverter_current_b,
    inverter_voltage_c_n: inverter_voltage_c,
    inverter_current_c_n: inverter_current_c,

    # System Parameters
    grid_frequency_n: grid_frequency,
    ac_power_n: ac_power,
    daily_energy_n: daily_energy,
    total_energy_n: total_energy,
    total_runtime_n: total_runtime,
    apparent_power_n: apparent_power,
    reactive_power_n: reactive_power,
    pv_input_power_n: pv_input_power,
    backup_total_power_n: backup_total_power,
    daily_grid_export_n: daily_grid_export,
    daily_grid_import_n: daily_grid_import,
    daily_backup_energy_n: daily_backup_energy,
    daily_battery_charge_n: daily_battery_charge,
    daily_battery_discharge_n: daily_battery_discharge,
    daily_pv_generation_n: daily_pv_generation,
    daily_load_consumption_n: daily_load_consumption,
    daily_grid_import_inverter_n: daily_grid_import_inverter,

    total_grid_export_n: total_grid_export,
    total_grid_import_n: total_grid_import,
    total_backup_energy_n: total_backup_energy,
    total_battery_charge_n: total_battery_charge,
    total_battery_discharge_n: total_battery_discharge,
    total_pv_generation_n: total_pv_generation,
    total_load_consumption_n: total_load_consumption,
    total_grid_import_inverter_n: total_grid_import_inverter,

    load_power_a_n: load_power_a,
    load_power_b_n: load_power_b,
    load_power_c_n: load_power_c,
    load_power_total_n: load_power_total,

    # Power Factor and Temperature
    power_factor_n: power_factor,
    temperature_1_n: temperature_1,
    temperature_2_n: temperature_2,
    temperature_3_n: temperature_3,
    temperature_4_n: temperature_4,

    # Bus Voltage
    bus_voltage_n: bus_voltage,
    nbus_voltage_n: nbus_voltage,

    # PV Input Parameters
    pv1_voltage_n: pv1_voltage,
    pv1_current_n: pv1_current,
    pv2_voltage_n: pv2_voltage,
    pv2_current_n: pv2_current,
    pv3_voltage_n: pv3_voltage,
    pv3_current_n: pv3_current,
    pv4_voltage_n: pv4_voltage,
    pv4_current_n: pv4_current,

    # PV Power
    pv1_power_n: pv1_power,
    pv2_power_n: pv2_power,
    pv3_power_n: pv3_power,
    pv4_power_n: pv4_power,

    # ARM Fault Flags
    arm_fault_flag1_n: arm_fault_flag1,
    arm_fault_flag2_n: arm_fault_flag2,

    # RTC Time Settings
    rtc_year_month_n: rtc_year_month,
    rtc_day_hour_n: rtc_day_hour,
    rtc_minute_second_n: rtc_minute_second,

    # Communication Settings
    comm_watchdog_n: comm_watchdog,
    duocom_work_mode_n: duocom_work_mode,
    modbus_tcp_internet_n: modbus_tcp_internet,

    # DO and Load Management
    do1_definition_n: do1_definition,
    load_control_mode_n: load_control_mode,
    manual_relay_status_n: manual_relay_status,

    # Battery Parameters
    battery_voltage_n: battery_voltage,
    battery_current_n: battery_current,
    battery_mode_n: battery_mode,
    battery_power_n: battery_power,
    battery_soc_n: battery_soc,
    battery_max_charge_current_n: battery_max_charge_current,
    battery_max_discharge_current_n: battery_max_discharge_current,
    battery_type_n: battery_type,
    battery_status_n: battery_status,
    battery_pack_temperature_n: battery_pack_temperature,
    battery_rated_capacity_n: battery_rated_capacity,

    # Storage System Parameters
    working_mode_n: working_mode,
    parallel_mode_n: parallel_mode,
    npe_detection_n: npe_detection,
    min_soc_protect_n: min_soc_protect,
    off_grid_parallel_num_n: off_grid_parallel_num,
    off_grid_parallel_addr_n: off_grid_parallel_addr,

    # ToU parameters
    tou_subwork_mode_n: tou_subwork_mode,

    # Grid Connection Parameters
    grid_export_power_switch_n: grid_export_power_switch,
    grid_export_power_percent_n: grid_export_power_percent,
    meter_comm_status_n: meter_comm_status,
    meter_power_phase_a_n: meter_power_phase_a,
    meter_power_phase_b_n: meter_power_phase_b,
    meter_power_phase_c_n: meter_power_phase_c,

    # Reactive Power Control
    reactive_q_setpoint_n: reactive_q_setpoint,
    reactive_pf_setpoint_n: reactive_pf_setpoint,
    reactive_control_mode_n: reactive_control_mode,

    # SG-Ready Settings
    sg_ready_mode3_min_runtime_n: sg_ready_mode3_min_runtime,
    sg_ready_mode3_max_runtime_n: sg_ready_mode3_max_runtime,
    sg_ready_mode3_smart_mode_n: sg_ready_mode3_smart_mode,
    sg_ready_mode3_start_power_n: sg_ready_mode3_start_power,
    sg_ready_mode3_exit_power_n: sg_ready_mode3_exit_power,
    sg_ready_mode3_start_soc_n: sg_ready_mode3_start_soc,
    sg_ready_mode3_exit_soc_n: sg_ready_mode3_exit_soc,

    # BMS Parameters
    bms_version_n: bms_version,
    bms_status_n: bms_status,
    bms_error1_code_n: bms_error1_code,
    bms_error2_code_n: bms_error2_code,
    bms_info_code_n: bms_info_code,
    bms_charge_volt_limit_n: bms_charge_volt_limit,
    bms_charge_curr_max_n: bms_charge_curr_max,
    bms_discharge_volt_limit_n: bms_discharge_volt_limit,
    bms_discharge_curr_max_n: bms_discharge_curr_max,
    bms_soh_n: bms_soh,
    bms_voltage_n: bms_voltage,
    bms_current_n: bms_current,
    bms_temperature_n: bms_temperature,
    bms_soc_n: bms_soc,

    # Power Control Settings
    pc_ac_power_scheduling_mode_setting_n: pc_ac_power_scheduling_mode_setting,
    pc_total_ac_power_target_n: pc_total_ac_power_target,
    pc_phase_a_power_target_n: pc_phase_a_power_target,
    pc_phase_b_power_target_n: pc_phase_b_power_target,
    pc_phase_c_power_target_n: pc_phase_c_power_target,
    pc_battery_power_target_n: pc_battery_power_target,
    pc_ac_power_max_limit_n: pc_ac_power_max_limit,
    pc_ac_power_min_limit_n: pc_ac_power_min_limit,
    pc_power_output_priority_n: pc_power_output_priority,
    pc_pv_power_target_n: pc_pv_power_target,



    # Grid Protection Settings - Level 1
    grid_undervoltage1_limit_n: grid_undervoltage1_limit,
    grid_undervoltage1_time_n: grid_undervoltage1_time,
    grid_overvoltage1_limit_n: grid_overvoltage1_limit,
    grid_overvoltage1_time_n: grid_overvoltage1_time,

    # Grid Protection Settings - Level 2
    grid_undervoltage2_limit_n: grid_undervoltage2_limit,
    grid_undervoltage2_time_n: grid_undervoltage2_time,
    grid_overvoltage2_limit_n: grid_overvoltage2_limit,
    grid_overvoltage2_time_n: grid_overvoltage2_time,

    # Frequency Protection Settings
    freq_underfreq1_limit_n: freq_underfreq1_limit,
    freq_underfreq1_time_n: freq_underfreq1_time,
    freq_overfreq1_limit_n: freq_overfreq1_limit,
    freq_overfreq1_time_n: freq_overfreq1_time,
    freq_underfreq2_limit_n: freq_underfreq2_limit,
    freq_underfreq2_time_n: freq_underfreq2_time,
    freq_overfreq2_limit_n: freq_overfreq2_limit,
    freq_overfreq2_time_n: freq_overfreq2_time,

    # Q(U) Mode Settings
    qu_lock_in_power_n: qu_lock_in_power,
    qu_lock_out_power_n: qu_lock_out_power,
    qu_v1_point_n: qu_v1_point,
    qu_q1_value_n: qu_q1_value,
    qu_v2_point_n: qu_v2_point,
    qu_q2_value_n: qu_q2_value,
    qu_v3_point_n: qu_v3_point,
    qu_q3_value_n: qu_q3_value,
    qu_v4_point_n: qu_v4_point,
    qu_q4_value_n: qu_q4_value,

    # Cos(φ)(P) Mode Settings
    cos_p_point_a_power_n: cos_p_point_a_power,
    cos_p_point_b_power_n: cos_p_point_b_power,
    cos_p_point_c_power_n: cos_p_point_c_power,
    cos_p_point_a_pf_n: cos_p_point_a_pf,
    cos_p_point_b_pf_n: cos_p_point_b_pf,
    cos_p_point_c_pf_n: cos_p_point_c_pf,
    cos_p_lock_in_voltage_n: cos_p_lock_in_voltage,
    cos_p_lock_out_voltage_n: cos_p_lock_out_voltage,
    cos_p_exit_power_n: cos_p_exit_power,

    # Grid Connection Settings
    grid_connection_enable_n: grid_connection_enable,
    grid_connection_startup_time_n: grid_connection_startup_time,
    grid_connection_reconnect_time_n: grid_connection_reconnect_time,
    grid_startup_min_voltage_n: grid_startup_min_voltage,
    grid_startup_max_voltage_n: grid_startup_max_voltage,
    grid_startup_min_freq_n: grid_startup_min_freq,
    grid_startup_max_freq_n: grid_startup_max_freq,
    grid_reconnect_min_voltage_n: grid_reconnect_min_voltage,
    grid_reconnect_max_voltage_n: grid_reconnect_max_voltage,
    grid_reconnect_min_freq_n: grid_reconnect_min_freq,
    grid_reconnect_max_freq_n: grid_reconnect_max_freq,

    # P(U) Settings
    pu_curve_enable_n: pu_curve_enable,
    pu_curve_start_voltage_n: pu_curve_start_voltage,
    pu_curve_start_power_n: pu_curve_start_power,
    pu_curve_end_voltage_n: pu_curve_end_voltage,
    pu_curve_end_power_n: pu_curve_end_power,

    # LFSM-O Settings
    lfsm_o_enable_n: lfsm_o_enable,
    lfsm_o_start_freq_n: lfsm_o_start_freq,
    lfsm_o_start_power_n: lfsm_o_start_power,
    lfsm_o_end_freq_n: lfsm_o_end_freq,
    lfsm_o_end_power_n: lfsm_o_end_power,
    lfsm_o_recovery_freq_n: lfsm_o_recovery_freq,
    lfsm_o_recovery_time_n: lfsm_o_recovery_time,
    lfsm_o_recovery_power_ref_n: lfsm_o_recovery_power_ref,
    lfsm_o_recovery_rate_n: lfsm_o_recovery_rate,

    # UVRT Settings
    uvrt_zero_current_voltage_n: uvrt_zero_current_voltage,
    uvrt_recovery_voltage_n: uvrt_recovery_voltage,
    uvrt_point1_voltage_n: uvrt_point1_voltage,
    uvrt_point2_voltage_n: uvrt_point2_voltage,
    uvrt_point3_voltage_n: uvrt_point3_voltage,
    uvrt_point4_voltage_n: uvrt_point4_voltage,
    uvrt_point5_voltage_n: uvrt_point5_voltage,
    uvrt_point1_time_n: uvrt_point1_time,
    uvrt_point2_time_n: uvrt_point2_time,
    uvrt_point3_time_n: uvrt_point3_time,
    uvrt_point4_time_n: uvrt_point4_time,
    uvrt_point5_time_n: uvrt_point5_time,
    uvrt_enable_n: uvrt_enable,

    # OVRT Settings
    ovrt_zero_current_voltage_n: ovrt_zero_current_voltage,
    ovrt_recovery_voltage_n: ovrt_recovery_voltage,
    ovrt_point1_voltage_n: ovrt_point1_voltage,
    ovrt_point2_voltage_n: ovrt_point2_voltage,
    ovrt_point3_voltage_n: ovrt_point3_voltage,
    ovrt_point1_time_n: ovrt_point1_time,
    ovrt_point2_time_n: ovrt_point2_time,
    ovrt_point3_time_n: ovrt_point3_time,
    ovrt_enable_n: ovrt_enable,

    # Additional Protection Settings
    ten_min_overvoltage_enable_n: ten_min_overvoltage_enable,
    ten_min_overvoltage_threshold_n: ten_min_overvoltage_threshold,
    qu_minimum_power_factor_n: qu_minimum_power_factor,
    qu_time_constant_n: qu_time_constant,
    pu_time_constant_n: pu_time_constant,
    overfreq_droop_n: overfreq_droop,

    # Battery Configuration
    battery_config_n: battery_config,
    battery_protocol_config_n: battery_protocol_config,
    on_grid_soc_protection_n: on_grid_soc_protection,
    on_grid_battery_soc_limit_n: on_grid_battery_soc_limit,
    off_grid_soc_protection_n: off_grid_soc_protection,
    off_grid_battery_soc_limit_n: off_grid_battery_soc_limit,
    end_soc_of_charging_n: end_soc_of_charging,

    # Time Period Control Parameters
    time_period_control_n: time_period_control,
    period_enable_flags_n: period_enable_flags,

    # Period 1 Settings
    period1_charge_discharge_n: period1_charge_discharge,
    period1_charge_source_n: period1_charge_source,
    period1_power_limit_n: period1_power_limit,
    period1_start_time_n: period1_start_time,
    period1_end_time_n: period1_end_time,

    # Periods 2-6 Settings (following the same pattern)
    period2_charge_discharge_n: period2_charge_discharge,
    period2_charge_source_n: period2_charge_source,
    period2_power_limit_n: period2_power_limit,
    period2_start_time_n: period2_start_time,
    period2_end_time_n: period2_end_time,

    # Parallel System Control
    parallel_system_mode_n: parallel_system_mode,
    parallel_ac_power_control_n: parallel_ac_power_control,
    parallel_total_ac_power_n: parallel_total_ac_power,
    parallel_phase_a_power_n: parallel_phase_a_power,
    parallel_phase_b_power_n: parallel_phase_b_power,
    parallel_phase_c_power_n: parallel_phase_c_power,
    parallel_battery_power_n: parallel_battery_power,
    parallel_export_power_limit_n: parallel_export_power_limit,
    parallel_import_power_limit_n: parallel_import_power_limit,
    parallel_rated_power_n: parallel_rated_power,

    # Write-Only Operation Registers
    aux_power_switch_n: aux_power_switch,
    clear_overload_flag_n: clear_overload_flag,
}
