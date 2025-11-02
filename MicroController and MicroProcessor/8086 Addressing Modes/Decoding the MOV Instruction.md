# Decoding the MOV Instruction

**Tags:** #8086 #assembly #instruction_set #simulation

The `MOV` instruction is the most common in 8086 assembly, and its encoding is a perfect case study for understanding the instruction format. The opcode for `MOV` between a register and another register/memory location is `100010`. The rest of the first two bytes are filled in based on the operands.

**Template for `MOV`:**

|Bit 7-2|Bit 1 (D)|Bit 0 (W)|Byte 2 (MOD, REG, R/M)|
|---|---|---|---|
|`100010`|Direction|Word/Byte|Addressing Mode|

### Simulating the Encoding of `MOV BL, AL`

Let's translate this simple register-to-register move into its final machine code.

1. **Opcode:** `100010` (for `MOV`).
    
2. **`W` (Word/Byte) Bit:** The operation involves `BL` and `AL`, which are 8-bit registers. Therefore, this is a byte operation.
    
    - **`W` = 0**
        
3. **`D` (Direction) Bit:** This bit answers the question: "Is the register in the `REG` field the destination?"
    
    - If `D` = 1, the `REG` field specifies the **destination** register.
        
    - If `D` = 0, the `REG` field specifies the **source** register.
        
    - In our case, the destination is `BL` and the source is `AL`. Let's decide to encode `AL` in the `REG` field. Since `AL` is the source, we set `D` to 0.
        
    - **`D` = 0**
        
4. **`MOD`, `REG`, `R/M` Fields:**
    
    - **`MOD`:** Since both operands are registers (not a memory location), this is "Register Mode".
        
        - **`MOD` = 11**
            
    - **`REG`:** We decided to encode the source, `AL`, in this field. Looking at the encoding table, the code for `AL` is `000`.
        
        - **`REG` = 000**
            
    - **`R/M`:** This field must encode the other register, the destination `BL`. The code for `BL` is `011`.
        
        - **`R/M` = 011**
            

**Assembling the Final Machine Code:**

- **Byte 1:** `100010` (Opcode) + `0` (D) + `0` (W) = `10001000` = **`88H`**
    
- **Byte 2:** `11` (MOD) + `000` (REG) + `011` (R/M) = `11000011` = **`C3H`**
    

Thus, the assembly instruction `MOV BL, AL` translates to the two-byte machine code **`88C3H`**.

### Simulating the Encoding of `MOV CX, [437AH]`

This instruction moves a word from a direct memory address into the `CX` register.

1. **Opcode:** `100010`
    
2. **`W` Bit:** `CX` is a 16-bit register. **`W` = 1**
    
3. **`D` Bit:** `CX` is the destination. We will encode `CX` in the `REG` field. **`D` = 1**
    
4. **`MOD`, `REG`, `R/M` Fields:**
    
    - **`MOD`:** This is a direct memory access with no register component. From the encoding table, this special case uses `MOD` = 00 and `R/M` = 110. **`MOD` = 00**
        
    - **`R/M`:** **`R/M` = 110**
        
    - **`REG`:** We are encoding the destination `CX`. The code for `CX` is `001`. **`REG` = 001**
        
5. **Displacement Bytes (3 & 4):** The direct address is `437AH`. This is a 16-bit displacement, stored with the low byte first.
    
    - **Byte 3 (Low):** `7AH`
        
    - **Byte 4 (High):** `43H`
        

**Assembling the Final Machine Code:**

- **Byte 1:** `100010` (Opcode) + `1` (D) + `1` (W) = `10001011` = **`8BH`**
    
- **Byte 2:** `00` (MOD) + `001` (REG) + `110` (R/M) = `00001110` = **`0EH`**
    
- **Bytes 3 & 4:** `7A43H`
    

The instruction `MOV CX, [437AH]` translates to the four-byte machine code **`8B 0E 7A 43`**.

**Links:** [[8086 General Instruction Format]], [[8086 REG and W Field Encoding]], [[8086 MOD and R M Field Encoding]]