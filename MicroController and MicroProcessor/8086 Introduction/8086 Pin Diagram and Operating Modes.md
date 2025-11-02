# 8086 Pin Diagram and Operating Modes

**Tags:** #microprocessor #8086 #pins #hardware

The 8086 microprocessor is a 40-pin chip. Understanding its pins is key to seeing how it interfaces with memory and other peripherals in a computer system.

### Key Pin Groups

- **Address/Data Bus (AD0-AD15):** These 16 pins are **multiplexed**. This means they have two jobs. For a short time at the beginning of a memory cycle, they carry the lower 16 bits of the memory address. For the rest of the cycle, they are used to transfer data.
    
- **Address/Status Bus (A16/S3 - A19/S6):** These 4 pins are also multiplexed. They carry the upper 4 bits of the 20-bit address, and at other times they provide status information about the type of operation currently happening on the bus.
    
- **Power Supply:** Pin 40 is for the +5V power supply (`VCC`), and Pins 1 and 20 are ground (`GND`).
    
- **Clock:** Pin 19 (`CLK`) receives the clock signal from an external oscillator, which synchronizes all internal operations.
    
- **Control Pins:** There are many control pins, like `RD` (Read), which signals a memory read operation, and `INTR` (Interrupt Request), which allows external devices to get the processor's attention.
    

### Modes of Operation

The 8086 is designed to be flexible and can be used in both small, simple systems and large, complex ones. The `MN/MX` pin (Pin 33) is used to select between two operating modes.

- **Minimum Mode (`MN/MX` pin is connected to +5V):**
    
    - This mode is used when the 8086 is the only processor in the system.
        
    - In this configuration, the 8086 generates all the bus control signals (like `RD`, `WR`, `M/IO`) itself. This is ideal for simple, self-contained applications.
        
- **Maximum Mode (`MN/MX` pin is connected to Ground):**
    
    - This mode is designed for systems with more than one processor, such as a main 8086 CPU and an 8087 math coprocessor.
        
    - In this mode, the 8086's control signal pins are redefined to provide status information. An external **bus controller** chip (like the Intel 8288) is required to decode this status and generate the actual bus control signals for the entire system. This allows for complex coordination between multiple processors on the same bus.
        

**Links:** [[8086 Microprocessor Architecture]]