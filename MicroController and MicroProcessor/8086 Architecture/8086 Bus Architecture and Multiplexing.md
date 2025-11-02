# 8086 Bus Architecture and Multiplexing

**Tags:** #8086 #bus_architecture #multiplexing #hardware

The 8086's performance and capabilities are directly tied to the physical buses that connect it to the rest of the computer system. It features three main buses, with the data and address buses being the most prominent.

- **16-bit Data Bus:** This means the 8086 can transfer 16 bits (2 bytes) of data to or from memory in a single machine cycle. This was a major advantage over its 8-bit predecessors, effectively doubling the data throughput.
    
- **20-bit Address Bus:** This allows the processor to generate `2^20` unique memory addresses, giving it the ability to access up to 1 Megabyte (1MB) of physical memory.
    
- **21-bit Control Bus:** This bus carries the various timing and control signals necessary to orchestrate the complex interactions between the CPU and external components.
    

### The Need for Multiplexing

A significant challenge in chip design is the limited number of physical pins available on the package (the 8086 has 40 pins). Providing separate pins for a 20-bit address bus and a 16-bit data bus would require 36 pins alone, leaving almost no room for power, ground, and the 21 essential control signals.

To solve this, Intel used **multiplexing**.

- **Definition:** Multiplexing is a technique where a single set of pins is used for multiple purposes at different times.
    
- **Implementation in 8086:** The 8086 uses the same set of pins for both the address and data lines (`AD0-AD15`).
    
    1. **During the T1 state** of a machine cycle, these pins carry the lower 16 bits of the memory address.
        
    2. **During the T2, T3, and T4 states**, these same pins are used as the 16-bit data bus to transfer data.
        

An external latch (like the 8282 chip) is required to "catch" and hold the address from the bus during T1, so that the memory system knows which location to access while the bus is later used for data. This is a classic engineering trade-off: it adds a little complexity to the external circuit but saves a significant number of pins on the microprocessor itself.

**Links:**  [[Determining Physical Memory Size]]