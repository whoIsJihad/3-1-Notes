# Arrays and Advanced Addressing

**Tags:** #assembly #arrays #addressing_modes

Arrays in assembly are simply contiguous blocks of memory. Accessing them efficiently requires moving beyond direct addressing and using the 8086's more powerful memory addressing modes.

### Defining Arrays

You can define an array using data definition directives (`DB`, `DW`) with multiple initial values or the `DUP` operator.

- **`DUP` (Duplicate) Operator:** A convenient way to initialize large arrays.
    
    - **Syntax:** `count DUP (value)`
        
    - **Example 1:** `word_array DW 100 DUP(0)` creates an array of 100 words, all initialized to zero.
        
    - **Example 2:** `uninit_bytes DB 256 DUP(?)` reserves 256 bytes of uninitialized memory.
        

### Advanced Addressing Modes for Arrays

These modes are the key to working with arrays inside loops.

1. **Register Indirect Mode:** The offset of the array element is in a register (`BX`, `BP`, `SI`, or `DI`).
    
    - **Example:** `MOV AX, [SI]`
        
    - **Use Case:** Perfect for iterating through an array. You can load the starting address of the array into `SI` and then increment `SI` in a loop to access each element sequentially.
        
2. **Based Mode:** An effective address is calculated by `[base_reg + displacement]`.
    
    - **Example:** `MOV AX, [BX + W]` where W is the array's base address.
        
    - **Use Case:** Accessing an array element using an index stored in `BX`. If `W` is a word array, and you want the element at index `i`, you would first calculate `offset = i * 2`, load it into `BX`, and then use `MOV AX, [BX + W]`.
        
3. **Indexed Mode:** Similar to Based Mode, but uses an index register (`SI` or `DI`).
    
    - **Example:** `MOV AX, [SI + W]`
        
    - **Functionally equivalent** to Based Mode for 1D arrays, just using a different register.
        

### The `PTR` Operator

The assembler can sometimes get confused about whether an operation should be a byte or a word. This happens when you access memory indirectly without a register operand to provide a size clue.

- **Problem:** In `MOV [BX], 5`, should the assembler move the 8-bit value `5` or the 16-bit value `0005h`? The instruction is ambiguous.
    
- **Solution:** The `PTR` operator explicitly tells the assembler the size of the memory operand.
    
    - `MOV BYTE PTR [BX], 5` ; Moves 8 bits.
        
    - `MOV WORD PTR [BX], 5` ; Moves 16 bits.
        

**Example: Summing an Array**

```
.DATA
W DW 10, 20, 30, 40, 50

.CODE
...
    XOR AX, AX            ; AX = sum = 0
    MOV CX, 5             ; CX = loop counter
    LEA SI, W             ; SI points to the start of the array

ADD_LOOP:
    ADD AX, [SI]          ; Add the current word element to sum
    ADD SI, 2             ; Move pointer to the next word (2 bytes)
    LOOP ADD_LOOP         ; Decrement CX and jump if not zero
```

**Links:** [[Advanced Assembly Concepts]]