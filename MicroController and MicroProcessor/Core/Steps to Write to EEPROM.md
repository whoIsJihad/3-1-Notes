# Steps to Write to EEPROM

Tags: eeprom, programming, c_code

Writing a byte to the EEPROM involves a specific sequence to prevent accidental data corruption:

1. Wait until the EEWE bit in the [[EEPROM Control Register (EECR)]] becomes zero, indicating any previous write is complete.
    
2. Write the target EEPROM address to the EEAR register.
    
3. Write the data byte to the EEDR register.
    
4. Write a logical one to the EEMWE bit in EECR. This enables writing for the next four clock cycles.
    
5. Within those four cycles, write a logical one to the EEWE bit to start the write operation.
