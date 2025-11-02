# The Stack - PUSH and POP

**Tags:** #assembly #stack #memory_management

The stack is a special area of memory that operates on a **Last-In, First-Out (LIFO)** principle. It is essential for temporary data storage, saving register states, and managing procedure calls.

In the 8086, the stack resides in the **Stack Segment (`SS`)**. Two registers manage it:

- `SS`: Contains the segment address of the stack.
    
- `SP` (Stack Pointer): Contains the offset of the **top** of the stack.
    

**Key Characteristic:** The 8086 stack grows **downwards** in memory. When you add an item, the `SP` register's value _decreases_.

### `PUSH` Instruction

- **Syntax:** `PUSH source` (source must be a 16-bit register or memory word)
    
- **Action:** Adds a word to the top of the stack. This happens in two steps:
    
    1. The Stack Pointer (`SP`) is decremented by 2.
        
    2. The 16-bit value from the `source` is copied to the memory location `SS:SP`.
        

**Simulation: `PUSH AX`**
  Assume `SP` = `0100h` and `AX` = `1234h`.

1. `SP` becomes `0100h - 2 = 00FEh`.
    
2. The value `1234h` is written to memory at address `SS:00FEh`.
    

### `POP` Instruction

- **Syntax:** `POP destination` (destination must be a 16-bit register or memory word)
    
- **Action:** Removes a word from the top of the stack. This is the reverse of `PUSH`:
    
    1. The 16-bit value at memory location `SS:SP` is copied to the `destination`.
        
    2. The Stack Pointer (`SP`) is incremented by 2.
        

**Simulation: `POP BX`** 
  Assume `SP` = `00FEh` and the value at `SS:00FEh` is `1234h`.

1. The value `1234h` is copied from the stack into the `BX` register.
    
2. `SP` becomes `00FEh + 2 = 0100h`.
    

### `PUSHF` and `POPF`

These instructions are used to save and restore the state of the CPU itself.

- **`PUSHF`**: Pushes the entire 16-bit `FLAGS` register onto the stack.
    
- **`POPF`**: Pops the 16-bit value from the top of the stack into the `FLAGS` register.
    
- **Use Case:** This is critical when calling procedures or handling interrupts. If a procedure is going to perform arithmetic, it should first `PUSHF` to save the main program's flags (Zero, Carry, etc.), and `POPF` just before returning to restore them.
    

**Links:** [[Advanced Assembly Concepts]]