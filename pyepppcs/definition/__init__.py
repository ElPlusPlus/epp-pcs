from pyepppcs.definition.register_names import *
from pyepppcs.definition.register_values import *

modbus_map = {
    # AC Output Voltages & Currents
    output_voltage_ab_n:    output_voltage_ab,
    output_voltage_bc_n:    output_voltage_bc,
    output_voltage_ca_n:    output_voltage_ca,
    output_voltage_a_n:     output_voltage_a,
    output_voltage_b_n:     output_voltage_b,
    output_voltage_c_n:     output_voltage_c,
    output_current_a_n:     output_current_a,
    output_current_b_n:     output_current_b,
    output_current_c_n:     output_current_c,
    inductance_current_a_n: inductance_current_a,
    inductance_current_b_n: inductance_current_b,
    inductance_current_c_n: inductance_current_c,
    grid_frequency_n:        grid_frequency,
    grid_phase_sequence_n:   grid_phase_sequence,
    pcs_derating_coefficient_n: pcs_derating_coefficient,
    pcs_derating_mark_n:     pcs_derating_mark,

    # AC Power
    ac_active_power_a_n:     ac_active_power_a,
    ac_active_power_b_n:     ac_active_power_b,
    ac_active_power_c_n:     ac_active_power_c,
    ac_apparent_power_a_n:   ac_apparent_power_a,
    ac_apparent_power_b_n:   ac_apparent_power_b,
    ac_apparent_power_c_n:   ac_apparent_power_c,
    ac_reactive_power_a_n:   ac_reactive_power_a,
    ac_reactive_power_b_n:   ac_reactive_power_b,
    ac_reactive_power_c_n:   ac_reactive_power_c,
    ac_total_active_power_n:  ac_total_active_power,
    ac_total_reactive_power_n: ac_total_reactive_power,
    ac_total_apparent_power_n: ac_total_apparent_power,
    ac_power_factor_n:        ac_power_factor,
    power_factor_a_n:         power_factor_a,
    power_factor_b_n:         power_factor_b,
    power_factor_c_n:         power_factor_c,

    # DC / Bus
    total_bus_voltage_n:    total_bus_voltage,
    positive_bus_voltage_n: positive_bus_voltage,
    negative_bus_voltage_n: negative_bus_voltage,
    battery_voltage_n:      battery_voltage,
    battery_current_n:      battery_current,
    dc_power_n:             dc_power,
    total_dc_current_n:     total_dc_current,

    # Status & Temperature
    working_condition_n:     working_condition,
    igbt_temperature_n:      igbt_temperature,
    ambient_temperature_n:   ambient_temperature,
    inductance_temperature_n: inductance_temperature,
    charge_discharge_mode_n: charge_discharge_mode,
    grid_offgrid_state_n:    grid_offgrid_state,

    # Software Versions
    dsp_version_v_n:  dsp_version_v,
    dsp_version_b_n:  dsp_version_b,
    dsp_version_d_n:  dsp_version_d,
    cpld_version_v_n: cpld_version_v,
    cpld_version_b_n: cpld_version_b,
    cpld_version_d_n: cpld_version_d,

    # Energy Counters
    dc_history_charge_n:    dc_history_charge,
    dc_daily_charge_n:      dc_daily_charge,
    dc_history_discharge_n: dc_history_discharge,
    dc_daily_discharge_n:   dc_daily_discharge,
    ac_history_charge_n:    ac_history_charge,
    ac_daily_charge_n:      ac_daily_charge,
    ac_history_discharge_n: ac_history_discharge,
    ac_daily_discharge_n:   ac_daily_discharge,

    # Insulation
    insulation_rx_n: insulation_rx,
    insulation_ry_n: insulation_ry,

    # Module SN
    module_sn_n: module_sn,

    # Fault Words
    hw_fault_word1_n:     hw_fault_word1,
    hw_fault_word2_n:     hw_fault_word2,
    grid_fault_word_n:    grid_fault_word,
    bus_fault_word_n:     bus_fault_word,
    ac_cap_fault_word_n:  ac_cap_fault_word,
    system_fault_word_n:  system_fault_word,
    switch_fault_word_n:  switch_fault_word,
    other_fault_word_n:   other_fault_word,

    # Power Setpoints
    set_active_power_n:           set_active_power,
    set_reactive_power_n:         set_reactive_power,
    set_phase_a_active_power_n:   set_phase_a_active_power,
    set_phase_a_reactive_power_n: set_phase_a_reactive_power,
    set_phase_b_active_power_n:   set_phase_b_active_power,
    set_phase_b_reactive_power_n: set_phase_b_reactive_power,
    set_phase_c_active_power_n:   set_phase_c_active_power,
    set_phase_c_reactive_power_n: set_phase_c_reactive_power,

    # Mode & Configuration
    offgrid_mode_n:                  offgrid_mode,
    operation_mode_n:                operation_mode,
    single_phase_power_control_n:    single_phase_power_control,
    module_host_n:                   module_host,
    current_source_parallel_enable_n: current_source_parallel_enable,
    dehumidification_enable_n:       dehumidification_enable,
    parallel_module_count_n:         parallel_module_count,
    offgrid_voltage_n:               offgrid_voltage,
    offgrid_frequency_n:             offgrid_frequency,
    insulation_detection_enable_n:   insulation_detection_enable,
    max_charge_power_n:              max_charge_power,
    max_discharge_power_n:           max_discharge_power,
    max_charge_current_battery_n:    max_charge_current_battery,
    max_discharge_current_battery_n: max_discharge_current_battery,
    dc_source_bus_voltage_n:         dc_source_bus_voltage,
    bus_voltage_n:                   bus_voltage,

    # Protection Parameters
    grid_overfreq_protection_n:       grid_overfreq_protection,
    grid_underfreq_protection_n:      grid_underfreq_protection,
    island_overfreq_protection_n:     island_overfreq_protection,
    island_underfreq_protection_n:    island_underfreq_protection,
    battery_overvoltage_protection_n: battery_overvoltage_protection,
    battery_undervoltage_protection_n: battery_undervoltage_protection,
    busbar_overvoltage_protection_n:  busbar_overvoltage_protection,
    busbar_undervoltage_protection_n: busbar_undervoltage_protection,
    dc_overcurrent_protection_n:      dc_overcurrent_protection,
    ac_overvoltage_protection_n:      ac_overvoltage_protection,
    ac_undervoltage_protection_n:     ac_undervoltage_protection,
    ac_overcurrent_protection_n:      ac_overcurrent_protection,
    overtemperature_protection_n:     overtemperature_protection,

    # Battery Charging Parameters
    cc_cv_battery_voltage_n: cc_cv_battery_voltage,
    constant_voltage_charging_n: constant_voltage_charging,
    max_cv_time_n:           max_cv_time,
    cv_to_float_current_n:   cv_to_float_current,
    float_charge_voltage_n:  float_charge_voltage,
    float_to_cc_current_n:   float_to_cc_current,

    # Control Commands
    power_on_off_n:   power_on_off,
    fault_reset_n:    fault_reset,
    cure_parameter_n: cure_parameter,
    charge_reset_n:   charge_reset,
    safety_one_key_n: safety_one_key,

    # Communication
    remodbus_address_n:    remodbus_address,
    remodbus_baud_rate_n:  remodbus_baud_rate,
    hmi_modbus_address_n:  hmi_modbus_address,
    hmi_modbus_baud_rate_n: hmi_modbus_baud_rate,
    ems_comm_timeout_n:    ems_comm_timeout,

    # Timing (write-only)
    time_year_n:   time_year,
    time_month_n:  time_month,
    time_day_n:    time_day,
    time_hour_n:   time_hour,
    time_minute_n: time_minute,
    time_second_n: time_second,
}
