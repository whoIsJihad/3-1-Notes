# EEPROM Data Memory

Tags: eeprom, memory, non_volatile

EEPROM (Electrically Erasable Programmable Read-Only Memory) is a type of non-volatile memory used to store small amounts of data that must be saved when power is removed.

- The [[ATmega32 Architecture|ATmega32]] has 1024 bytes (1 KB) of data EEPROM.
    
- It is organized as a separate data space.
    
- Single bytes can be read and written.
    
- Reading from EEPROM halts the CPU for four clock cycles.
    
- Writing to EEPROM halts the CPU for two clock cycles.
    
- It has an endurance of at least 100,000 write/erase cycles.
