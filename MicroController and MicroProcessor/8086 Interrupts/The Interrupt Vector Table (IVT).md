
---

**Tags:** #interrupts #isr #memory_layout #data_structures

When an interrupt occurs, how does the CPU know _where_ to find the correct Interrupt Service Routine (ISR) to execute? The answer is a critical data structure located at the very beginning of memory: the **Interrupt Vector Table (IVT)**.

### What is the IVT?

The IVT is a simple lookup table, or an array of addresses. It acts as an intermediary, mapping an interrupt's "type number" (from 0 to 255) to the starting address of its corresponding handler code.

**Key Characteristics:**

- **Location:** In the 8086, the IVT is always located in the first 1024 bytes (1 KB) of physical memory, from address `00000H` to `003FFH`.
    
- **Structure:** It is an array of 256 entries.
    
- **Entry Size:** Each entry, called an **interrupt vector**, is 4 bytes long.
    

### Structure of an Interrupt Vector

Each 4-byte vector in the table contains the complete `CS:IP` far address of an ISR.

- **First 2 bytes (Low Word):** The 16-bit **offset** to be loaded into the `IP` register.
    
- **Next 2 bytes (High Word):** The 16-bit **segment** to be loaded into the `CS` register.
    

### How the CPU Uses the IVT

The process is a simple, direct hardware calculation. When an interrupt of **type `n`** occurs:

1. The CPU hardware calculates the starting address of the vector within the IVT.
    
    ```
    VectorAddress = n * 4
    ```
    
2. The CPU reads the 4 bytes starting at `VectorAddress`.
    
    - It reads the 16-bit value at `VectorAddress` and loads it into `IP`.
        
    - It reads the 16-bit value at `VectorAddress + 2` and loads it into `CS`.
        
3. The CPU now begins executing instructions at the new `CS:IP`.
    

#### Simulation: `INT 21H`

Let's trace what happens for the famous DOS system call, `INT 21H`.

1. **Interrupt Type:** The type `n` is `21H` (or 33 in decimal).
    
2. **Calculate Vector Address:**
    
    ```
    VectorAddress = 21H * 4 = 84H
    ```
    
    The physical address is `00084H`.
    
3. **Fetch the Address:**
    
    - The CPU reads the 2 bytes at `00084H` and `00085H` and loads this value into `IP`.
        
    - The CPU reads the 2 bytes at `00086H` and `00087H` and loads this value into `CS`.
        
4. **Jump:** The CPU is now executing the DOS Function Handler, whose address was stored in those four bytes.
    

This table-based dispatch system is extremely efficient and allows the operating system (or even user programs) to define, replace, or chain interrupt handlers simply by changing the 4-byte addresses in the IVT.

**Links:** [[8086 Interrupts and System Control (Index)]]
