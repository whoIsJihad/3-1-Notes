**Tags:** #assembly #bitwise #instruction_set

Bitwise instructions operate on individual bits of data. They are fundamental for tasks like setting or clearing specific flags, masking, and performing fast arithmetic.

### Logical Instructions (`AND`, `OR`, `XOR`, `NOT`, `TEST`)

These instructions perform bit-by-bit logical operations.

- **`AND destination, source`**: The result is `1` only if the corresponding bits in both operands are `1`.
    
    - **Common Use:** Masking or clearing bits. `AND AL, 0Fh` clears the upper 4 bits of `AL`, keeping the lower 4.
        
- **`OR destination, source`**: The result is `1` if the corresponding bit in _either_ operand is `1`.
    
    - **Common Use:** Setting bits. `OR AL, 80h` sets the most significant bit of `AL` to 1, leaving other bits unchanged.
        
- **`XOR destination, source`**: The result is `1` if the corresponding bits are different.
    
    - **Common Use:** Clearing a register. `XOR AX, AX` is a fast and efficient way to set `AX` to zero.
        
- **`NOT destination`**: Flips all the bits in the operand (one's complement).
    
- **`TEST destination, source`**: Performs a "phantom" `AND` operation. The result is not stored, but the CPU flags (like the Zero Flag) are updated.
    
    - **Common Use:** Checking if a bit is set without altering the register. `TEST AL, 1` will set the Zero Flag if `AL` is even (LSB is 0) and clear it if `AL` is odd (LSB is 1).
        

### Shift and Rotate Instructions

These instructions move bits within an operand. The number of shifts is either `1` or the value in the `CL` register.

- **`SHL` / `SAL` (Shift Logical/Arithmetic Left)**
    
    - **Action:** Shifts all bits to the left. The Most Significant Bit (MSB) moves into the Carry Flag (CF), and a `0` is shifted into the Least Significant Bit (LSB). `SHL` and `SAL` are identical.
        
    - **Use Case:** Fast multiplication by 2. `SHL AX, 1` is equivalent to `AX * 2`.
        
- **`SHR` (Shift Logical Right)**
    
    - **Action:** Shifts all bits to the right. The LSB moves into the Carry Flag, and a `0` is shifted into the MSB.
        
    - **Use Case:** Fast unsigned division by 2.
        
- **`SAR` (Shift Arithmetic Right)**
    
    - **Action:** Shifts all bits to the right. The LSB moves into the Carry Flag, but the original MSB is **copied** back into the MSB position.
        
    - **Use Case:** Fast signed division by 2. This instruction preserves the number's sign.
        

**Links:** [[Advanced Assembly Concepts]]