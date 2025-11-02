# EEPROM Control Register (EECR)

Tags: eeprom, registers, control_register

The EECR contains the control bits for managing EEPROM read and write operations. Key bits include:

- **EERE (EEPROM Read Enable):** Writing a one to this bit triggers a read from the address specified in EEAR.
    
- **EEWE (EEPROM Write Enable):** Writing a one to this bit triggers a write of the data in EEDR to the address in EEAR.
    
- **EEMWE (EEPROM Master Write Enable):** This bit must be set before EEWE can be set. It acts as a safety mechanism to prevent accidental writes. It is automatically cleared by hardware after four clock cycles.
    
- **EERIE (EEPROM Ready Interrupt Enable):** Enables an interrupt that fires when an EEPROM write is complete.
