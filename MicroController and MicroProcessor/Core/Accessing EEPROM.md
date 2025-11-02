# Accessing EEPROM

Tags: eeprom, registers, memory_access

To interact with the EEPROM, three sets of registers are used:

1. **EEPROM Address Register (EEARH and EEARL):** A 10-bit register that specifies the address (0-1023) in the EEPROM.
    
2. **EEPROM Data Register (EEDR):** An 8-bit register that contains the data to be written to the EEPROM or the data that has just been read.
    
3. **[[EEPROM Control Register (EECR)]]:** An 8-bit register containing control bits for EEPROM operations.
