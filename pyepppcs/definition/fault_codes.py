from pyepppcs.definition.register_names import *

# Bit meanings per PCS Communication Protocol V1.22, section 5.1.
# 1 = fault, 0 = normal; bits not listed are reserved.

hw_fault_word1_bits = {
    0: "EPO fault",
    1: "IGBT OCP fault",
    2: "Bus hardware overvoltage fault",
    4: "Power module wave-by-wave current limiting fault",
    5: "Balance module wave-by-wave current limiting fault",
}

hw_fault_word2_bits = {
    0: "24V power fault",
    1: "Fan fault",
    2: "Connection fault",
    6: "External input dry contact 3 fault",
    7: "Inductance overtemperature fault",
    8: "Power module overtemperature fault",
    9: "Balance module overtemperature fault",
    10: "15V power fault",
    11: "System fire alarm fault",
    12: "External input dry contact 1 fault",
    13: "External input dry contact 2 fault",
    14: "Ambient temperature overtemperature fault",
    15: "Dry contact overtemperature fault",
}

grid_fault_word_bits = {
    0: "Grid phase A overvoltage fault",
    1: "Grid phase B overvoltage fault",
    2: "Grid phase C overvoltage fault",
    3: "Grid phase A undervoltage fault",
    4: "Grid phase B undervoltage fault",
    5: "Grid phase C undervoltage fault",
    6: "Grid overfrequency fault",
    7: "Grid underfrequency fault",
    8: "Grid phase sequence error fault",
    9: "Phase A software overcurrent fault",
    10: "Phase B software overcurrent fault",
    11: "Phase C software overcurrent fault",
    12: "Grid voltage unbalance fault",
    13: "Grid current unbalance fault",
    14: "Grid phase loss fault",
    15: "N-line overcurrent fault",
}

bus_fault_word_bits = {
    0: "Precharge bus overvoltage fault",
    1: "Precharge bus undervoltage fault",
    4: "Running bus overvoltage fault",
    5: "Running bus undervoltage fault",
    6: "Positive/negative bus unbalance fault",
    7: "Battery undervoltage fault",
    9: "Battery overvoltage fault",
    10: "DC precharge overcurrent fault",
    11: "DC overcurrent fault",
    12: "Balance module software overcurrent fault",
    15: "Battery reverse connection fault",
}

ac_cap_fault_word_bits = {
    0: "Precharge timeout fault",
    1: "Precharge phase A overcurrent fault",
    2: "Precharge phase B overcurrent fault",
    3: "Precharge phase C overcurrent fault",
    6: "Leakage overcurrent fault",
}

system_fault_word_bits = {
    0: "Control board RAM fault",
    1: "Control board EEPROM fault",
    2: "AD zero drift fault",
    3: "Back-end communication protocol fault",
    4: "CAN communication protocol fault",
    5: "CPLD communication protocol fault",
    6: "DataLog data fault",
    8: "Insulation detection fault",
    9: "Software/firmware mismatch fault",
    11: "BMS battery status fault",
    12: "STS communication fault",
    13: "BMS communication fault",
    14: "Parallel system CAN communication fault",
    15: "EMS communication fault",
}

# Bits 8-10: contact the manufacturer; if powered off, do not power on again.
switch_fault_word_bits = {
    0: "Precharge relay close fault",
    1: "Precharge relay open fault",
    2: "Precharge relay closed-state fault",
    3: "Precharge relay open-state fault",
    4: "Main relay close fault",
    5: "Main relay open fault",
    6: "Main relay closed-state fault",
    7: "Main relay open-state fault",
    8: "AC main relay adhesion fault",
    9: "DC relay open circuit fault",
    10: "AC main relay open circuit fault",
}

other_fault_word_bits = {
    0: "Inverter phase A overvoltage fault",
    1: "Inverter phase B overvoltage fault",
    2: "Inverter phase C overvoltage fault",
    3: "Grid island fault",
    5: "System resonance fault",
    6: "Software overvoltage/overcurrent fault",
    8: "High voltage ride-through timeout fault",
    9: "Inverter phase A undervoltage fault",
    10: "Inverter phase B undervoltage fault",
    11: "Inverter phase C undervoltage fault",
    12: "Off-grid no synchronization signal fault",
    14: "Off-grid output short circuit fault",
    15: "Low voltage ride-through timeout fault",
}

fault_bits_map = {
    hw_fault_word1_n:    hw_fault_word1_bits,
    hw_fault_word2_n:    hw_fault_word2_bits,
    grid_fault_word_n:   grid_fault_word_bits,
    bus_fault_word_n:    bus_fault_word_bits,
    ac_cap_fault_word_n: ac_cap_fault_word_bits,
    system_fault_word_n: system_fault_word_bits,
    switch_fault_word_n: switch_fault_word_bits,
    other_fault_word_n:  other_fault_word_bits,
}


def decode_fault_word(register_name: str, raw: int) -> list:
    """Return descriptions of the set bits in a fault word (unknown bits are reported as reserved)."""
    bits = fault_bits_map[register_name]
    return [
        bits.get(bit, f"Reserved bit {bit}")
        for bit in range(16)
        if raw & (1 << bit)
    ]
