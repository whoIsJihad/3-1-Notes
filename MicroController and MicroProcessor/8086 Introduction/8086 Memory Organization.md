# 8086 Memory Organization

**Tags:** #microprocessor #8086 #memory #segmentation #banking

The 8086 has a 16-bit architecture but needs to access a 20-bit (1MB) address space. This created a challenge that Intel solved with a clever but sometimes confusing system called **segmented memory**.

### Memory Segmentation Explained

The problem: How do you create a 20-bit address using only 16-bit registers?

The solution: Combine two 16-bit values. The 1MB memory space is divided into overlapping blocks of 64KB (which is `2^16`, the maximum a single 16-bit register can address). These blocks are called **segments**.

- A **segment register** (like CS or DS) points to the starting address of a 64KB segment.
    
- An **offset register** (like IP or BX) points to a specific memory location _within_ that segment.
    

#### Physical Address Calculation

The BIU calculates the final 20-bit physical address using this formula: `Physical Address = (Segment Register Value * 16) + Offset Register Value`

Multiplying by 16 is the same as shifting the bits of the segment address to the left by 4 places and adding a `0` hex digit at the end.

**Example:** Suppose the Code Segment (CS) register is `A100H` and the Instruction Pointer (IP) is `B234H`.

1. **Take the Segment Address:** `A100H`
    
2. **Shift Left by 4 bits (add a 0):** `A1000H`
    
3. **Add the Offset:**
    
    ```
      A1000H  (Segment Base)
    +  B234H  (Offset)
    ----------
      AC234H  (20-bit Physical Address)
    ```
    

So, the CPU will fetch the next instruction from the physical memory location `AC234H`.

### Memory Banking

To efficiently use its 16-bit data bus with standard 8-bit wide memory chips, the 8086 splits its 1MB memory into two 512KB banks:

- **Even Bank (Low Bank):** Contains all bytes at even addresses (00000H, 00002H, etc.). Connected to data lines D0-D7.
    
- **Odd Bank (High Bank):** Contains all bytes at odd addresses (00001H, 00003H, etc.). Connected to data lines D8-D15.
    

This allows the processor to:

- Read/write a single byte from either bank in one operation.
    
- Read/write a 16-bit word (e.g., the contents of the AX register) in a single operation, as long as the word starts at an even address. It does this by grabbing one byte from the even bank and one from the odd bank simultaneously.
    

**Links:** [[8086 Bus Interface Unit (BIU) Registers]]