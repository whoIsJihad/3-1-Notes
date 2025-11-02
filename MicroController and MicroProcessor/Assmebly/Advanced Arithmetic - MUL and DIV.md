# Advanced Arithmetic - MUL and DIV

**Tags:** #assembly #arithmetic #instruction_set

Multiplication and division in the 8086 are more complex than simple addition because the result can be twice the size of the operands. These instructions have implicit rules about which registers to use.

### Multiplication (`MUL`, `IMUL`)

- **`MUL source`**: Unsigned multiplication.
    
- **`IMUL source`**: Signed multiplication.
    

The `source` can be an 8-bit or 16-bit register or memory location. The other operand is **implicitly** `AL` or `AX`.

- **Byte Multiplication (8-bit source):**
    
    - **Operation:** `AX = AL * source`
        
    - The 8-bit value in `AL` is multiplied by the 8-bit `source`.
        
    - The full 16-bit result is stored in `AX`.
        
- **Word Multiplication (16-bit source):**
    
    - **Operation:** `DX:AX = AX * source`
        
    - The 16-bit value in `AX` is multiplied by the 16-bit `source`.
        
    - The 32-bit result is stored across two registers: the upper 16 bits go into `DX` and the lower 16 bits go into `AX`.
        

### Division (`DIV`, `IDIV`)

- **`DIV source`**: Unsigned division.
    
- **`IDIV source`**: Signed division.
    

The dividend is **implicitly** `AX` or `DX:AX`.

- **Byte Division (8-bit divisor):**
    
    - **Operation:** The 16-bit dividend in `AX` is divided by the 8-bit `source`.
        
    - **Result:**
        
        - The 8-bit quotient is stored in `AL`.
            
        - The 8-bit remainder is stored in `AH`.
            
- **Word Division (16-bit divisor):**
    
    - **Operation:** The 32-bit dividend in `DX:AX` is divided by the 16-bit `source`.
        
    - **Result:**
        
        - The 16-bit quotient is stored in `AX`.
            
        - The 16-bit remainder is stored in `DX`.
            

### Important Considerations for Division

- **Divide Overflow:** If the quotient is too large to fit in the destination (`AL` or `AX`), the CPU triggers a "Divide Overflow" interrupt, which usually crashes the program. This happens if you divide by a small number or forget to prepare the dividend.
    
- **Preparing the Dividend:**
    
    - For **unsigned** division (`DIV`), you must clear the upper part of the dividend. For word division, this means setting `DX` to zero (`XOR DX, DX`).
        
    - For **signed** division (`IDIV`), you must **sign-extend** the dividend.
        
        - `CBW` (Convert Byte to Word): Extends the sign bit of `AL` into all bits of `AH`.
            
        - `CWD` (Convert Word to Double Word): Extends the sign bit of `AX` into all bits of `DX`.
            

**Example: Signed Word Division of -1250 by 7**

```
MOV AX, -1250   ; Load dividend into AX
CWD             ; Sign-extend AX into DX. DX is now FFFFh.
MOV BX, 7       ; Load divisor into BX
IDIV BX         ; AX = quotient, DX = remainder
```

**Links:** [[Advanced Assembly Concepts]]