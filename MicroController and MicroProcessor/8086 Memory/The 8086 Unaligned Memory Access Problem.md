

**Tags:** #8086 #computer_architecture #performance #memory_alignment

In computer architecture, **memory alignment** refers to the practice of storing data at a memory address that is a multiple of its size. For the 16-bit (2-byte) 8086, a data word is considered **aligned** if it begins at an even memory address (`0H, 2H, 4H, ...`) and **unaligned** if it begins at an odd address (`1H, 3H, 5H, ...`).

While the 8086 _can_ handle unaligned data, doing so incurs a significant performance penalty. This isn't an arbitrary software rule; it's a direct consequence of the processor's physical hardware design—specifically, its dual memory banks.

### The Ideal Scenario: Aligned Word Access

Let's first simulate the efficient, aligned case. The CPU needs to read a 16-bit word from the **even** address `00002H`.

- **Goal:** Read the two bytes at `00002H` and `00003H`.
    
- **Hardware Mapping:**
    
    - Byte at `00002H` is in the **Low (Even) Bank**.
        
    - Byte at `00003H` is in the **High (Odd) Bank**.
        
- **The Hardware's Advantage:** Both of these memory locations can be accessed with the same "row" address sent on lines `A1-A19`. The CPU can enable both banks at the same time.
    

**The Single-Cycle Operation:**

1. The 8086 places the address `00002H` on the bus.
    
2. It sets its control signals:
    
    - `A0` is `0` (because the address is even), which selects the **Low Bank**.
        
    - `BHE` is `0` (active-low), which selects the **High Bank**.
        
3. Because both banks are selected simultaneously, the Low Bank places its byte (`at 00002H`) on `D0-D7` and the High Bank places its byte (`at 00003H`) on `D8-D15`.
    
4. The CPU reads the full 16 bits from its data bus.
    

**Result:** The entire word is fetched in **one** memory bus cycle. This is fast and efficient.

### The Problem Scenario: Unaligned Word Access

Now, let's simulate the inefficient, unaligned case. The CPU is instructed to read a 16-bit word starting from the **odd** address `00003H`.

- **Goal:** Read the two bytes at `00003H` and `00004H`.
    
- **Hardware Mapping:**
    
    - Byte at `00003H` is in the **High (Odd) Bank**.
        
    - Byte at `00004H` is in the **Low (Even) Bank**.
        
- **The Hardware's Limitation:** These two memory locations are in different physical "rows" within the memory chips. The byte at `00003H` shares a row with `00002H`, while the byte at `00004H` shares a row with `00005H`. The 8086 **cannot** send two different row addresses (`A1-A19`) to the memory banks in the same cycle.
    

**The Two-Cycle Penalty:**

The BIU must break the single request into two separate, sequential memory cycles.

**Cycle 1: Read the first byte (from the odd address)**

1. The CPU first requests the byte at `00003H`.
    
2. It sets its control signals for an 8-bit odd read:
    
    - `A0` is `1` (because the address is odd).
        
    - `BHE` is `0` (selecting the **High Bank**).
        
3. The byte from `00003H` is fetched on data lines `D8-D15`. The CPU temporarily stores this byte.
    

**Cycle 2: Read the second byte (from the next even address)**

1. The CPU now requests the byte at `00004H`.
    
2. It changes its control signals for an 8-bit even read:
    
    - `A0` is `0` (selecting the **Low Bank**).
        
    - `BHE` is `1` (disabling the High Bank).
        
3. The byte from `00004H` is fetched on data lines `D0-D7`.
    
4. The CPU combines the byte from Cycle 1 with the byte from Cycle 2 to assemble the full 16-bit word.
    

**Result:** The word is fetched, but it required **two** full memory bus cycles. The operation took twice as long as the aligned access.

### Why This Matters

This hardware limitation is why modern compilers and high-level languages are obsessed with data alignment.

- **Struct Padding:** When you define a `struct` in C++, the compiler often inserts invisible "padding" bytes between members. It does this to ensure that multi-byte members (like an `int` or `double`) start on an aligned address (a multiple of 4 or 8 on modern systems), even if it wastes a little space. The small space cost is a worthwhile trade-off for avoiding slow, unaligned access penalties.
    
- **Performance Tuning:** In high-performance computing, programmers manually align their data structures to ensure the CPU can always perform single-cycle memory accesses, maximizing throughput.
    

