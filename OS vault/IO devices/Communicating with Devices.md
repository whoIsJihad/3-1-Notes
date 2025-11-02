**Tags:** #os #io #hardware #architecture

# Communicating with Devices

The OS needs a way to actually read and write the status, command, and data registers of a [[The Canonical I_O Device|canonical device]]. There are two primary methods for this.

### 1. I/O Instructions

Some architectures provide special CPU instructions to communicate with devices.

- **Example (x86):** The `in` and `out` instructions.
    
- These instructions take a port number (representing the device address) and a value.
    
- The device registers live in a separate I/O address space, distinct from the main memory address space.
    
- This is the approach used in the [[xv6 IDE Driver Implementation]].
    

### 2. Memory-Mapped I/O

This is the more common and modern approach. The device registers are mapped into the system's main memory address space.

- To the CPU, the device registers look just like regular memory locations.
    
- There are no special instructions needed. The OS uses standard `load` and `store` instructions to read from and write to the device registers.
    
- The hardware ensures that these specific memory addresses are routed to the device instead of to RAM.
    

**Links:** [[I_O Devices MOC]], [[The Canonical I_O Device]], [[xv6 IDE Driver Implementation]]