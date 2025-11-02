

**Tags:** #8086 #hardware #memory_banking

While the 8086 can address a continuous 1MB of memory (from `00000H` to `FFFFFH`), the physical implementation is not a single, simple block. To efficiently interface its 16-bit data bus with standard 8-bit memory chips, the 8086 organizes its memory into two parallel **banks**.

- **Low Bank (Even Bank):**
    
    - Contains all memory locations with an **even** address (`00000H`, `00002H`, etc.).
        
    - Connected to the lower half of the data bus (`D0-D7`).
        
    - This bank holds 512 KB of data.
        
- **High Bank (Odd Bank):**
    
    - Contains all memory locations with an **odd** address (`00001H`, `00003H`, etc.).
        
    - Connected to the upper half of the data bus (`D8-D15`).
        
    - This bank also holds 512 KB of data.
        

### Why Banking is Necessary

This parallel structure is a clever solution to a hardware mismatch. The 8086 wants to read/write 16 bits (2 bytes) at a time to be efficient. Memory chips of that era stored 8 bits (1 byte) per location.

By arranging the memory this way, the 8086 can:

1. **Read/Write a 16-bit Word in a Single Cycle:** If the word starts at an even address (e.g., `00002H`), the 8086 can grab the low byte from the Low Bank and the high byte from the High Bank simultaneously, filling its entire 16-bit data bus in one operation.
    
2. **Read/Write an 8-bit Byte Efficiently:** It can also access just one bank to read or write a single byte from either an even or odd address.
    

This design is controlled by two specific hardware signals, `A0` and `BHE`, which act as the chip selects for these banks.

**Links:** [[Accessing Memory Banks with BHE and A0]], [[8086 Memory Organization (index)]]