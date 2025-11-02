

---

**Tags:** #memory_banking #8086 #hardware #computer_architecture

We've established the ideal: the data bus width should match the CPU's internal word size. For the 8086, this means a 16-bit data bus for its 16-bit architecture. However, this creates a new problem.

**The Problem:** How does a 16-bit data bus efficiently interface with a memory system that is byte-addressable (where each unique address corresponds to an 8-bit location)?

If the memory was treated as a single, flat 1MB block of bytes, fetching a 16-bit word aligned at an even address (e.g., address `00100H`) would require two sequential memory accesses, defeating the purpose of the 16-bit bus.

### Intel's Solution: Memory Banking

To solve this, the 8086 logically divides its entire 1MB physical address space into two 512KB banks:

1. **Even Bank (Low Bank):**
    
    - Contains all memory locations with even addresses (`...0H`, `...2H`, `...4H`).
        
    - Connected to the lower half of the data bus (`D0-D7`).
        
    - Enabled by a control signal `A0 = 0`.
        
2. **Odd Bank (High Bank):**
    
    - Contains all memory locations with odd addresses (`...1H`, `...3H`, `...5H`).
        
    - Connected to the upper half of the data bus (`D8-D15`).
        
    - Enabled by a control signal `BHE` (Bus High Enable).
        

### How It Works in Practice

This clever arrangement allows the 8086 to perform reads and writes with maximum efficiency in a single machine cycle:

- **To Read/Write a 16-bit Word (at an even address):** The CPU activates **both** banks simultaneously (`A0=0` and `BHE=0`). It grabs the low byte from the even bank on `D0-D7` and the high byte from the odd bank on `D8-D15` at the same time, fully utilizing the 16-bit data bus.
    
- **To Read/Write an 8-bit Byte (at an even address):** The CPU activates only the **even bank** (`A0=0`). Data is transferred on `D0-D7`.
    
- **To Read/Write an 8-bit Byte (at an odd address):** The CPU activates only the **odd bank** (`BHE=0`). Data is transferred on `D8-D15`.
    

This memory banking scheme is the critical hardware design that allows the 16-bit 8086 to work efficiently with an 8-bit, byte-addressable memory world. It is a classic example of architectural problem-solving you'll encounter frequently in CSE.

**Links:** [[8086 Memory Architecture and Bus Interaction]], [[The Mismatch Problem - Bus Width vs Register Size]]