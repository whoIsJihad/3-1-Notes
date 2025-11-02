# Essential 8086 Instructions

**Tags:** #assembly #instruction_set

This note covers the fundamental instructions needed to write basic assembly programs.

### Data Transfer Instructions

- **`MOV destination, source`**
    
    - **Action:** Copies the value of the `source` operand into the `destination` operand. The source is unchanged.
        
    - **Rules:** You **cannot** `MOV` from one memory location directly to another. One of the operands must be a register.
        
    - **Example:** `MOV AX, my_word` (Copy the value from the variable `my_word` into the `AX` register).
        
- **`XCHG destination, source`**
    
    - **Action:** Swaps the contents of the `source` and `destination` operands.
        
    - **Example:** `XCHG AX, BX` (The value of AX goes to BX, and the value of BX goes to AX).
        
- **`LEA destination, source`** (Load Effective Address)
    
    - **Action:** This is a crucial and often misunderstood instruction. It does **not** load the _data_ from the source; it loads the _offset address_ of the source into the destination register.
        
    - **Example:** `LEA DX, message`
        
    - **Result:** `DX` will contain the 16-bit memory offset of the `message` variable, not the characters 'H', 'e', 'l', 'l', 'o'. This is essential for passing pointers to functions, like the DOS print string function.
        

### Arithmetic Instructions

- **`ADD destination, source`**
    
    - **Action:** `destination = destination + source`
        
- **`SUB destination, source`**
    
    - **Action:** `destination = destination - source`
        
- **`INC destination`** (Increment)
    
    - **Action:** Adds 1 to the destination. `destination = destination + 1`. This is smaller and faster than `ADD destination, 1`.
        
- **`DEC destination`** (Decrement)
    
    - **Action:** Subtracts 1 from the destination. `destination = destination - 1`.
        
- **`NEG destination`** (Negate)
    
    - **Action:** Replaces the destination's value with its two's complement.
        
    - **Example:** If `BX` contains `0002h`, `NEG BX` will change `BX` to `FFFEh` (-2).
        

### Operand Rules for Arithmetic Instructions

For `ADD` and `SUB`, the same rule as `MOV` applies: you **cannot** have two memory operands in the same instruction. At least one must be a register.

**Example Translation:** Translate the high-level statement `A = B - 2 * A` into assembly, where A and B are word variables.

```
MOV AX, A       ; AX = A
ADD AX, AX      ; AX = 2 * A (Faster than multiplying)
MOV BX, B       ; BX = B
SUB BX, AX      ; BX = B - (2 * A)
MOV A, BX       ; Store the final result back into A
```

**Links:** [[Introduction to Assembly Language]]