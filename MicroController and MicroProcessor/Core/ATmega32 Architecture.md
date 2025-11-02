# ATmega32 Architecture

Tags: atmega32, architecture, harvard, pipelining

The ATmega32 CPU Core uses the AVR enhanced [[RISC vs CISC Architecture|RISC architecture]] and features:

- **[[von Neumann and Harvard Architectures|Harvard Architecture]]**: Separate memories and buses for program and data.
    
- **[[Single Level Pipelining]]**: The next instruction is fetched while the current one is executing, improving throughput.
    
- **[[General Purpose Register File]]**: 32 general-purpose 8-bit registers directly connected to the Arithmetic Logic Unit (ALU).
    
- **[[In-System Reprogrammable Flash Memory]]**: For storing program code.
    
- **[[Data SRAM]]**: For data storage.
    
- **[[EEPROM Data Memory]]**: For non-volatile data storage.
    
- Various peripherals like Timers, SPI, and an Analog Comparator.
