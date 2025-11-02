# 8086 Execution Unit (EU) Registers

**Tags:** #microprocessor #8086 #registers #EU

The Execution Unit (EU) houses the registers that programmers use most frequently for data manipulation. These are all 16-bit registers, but the first four are special because they can also be treated as two separate 8-bit registers.

### General Purpose Registers

These are often called the "data registers."

|Register|16-bit Name|8-bit High|8-bit Low|Common Usage and Special Functions|
|---|---|---|---|---|
|**Accumulator**|`AX`|`AH`|`AL`|The primary register for arithmetic. It's used implicitly by multiplication (`MUL`) and division (`DIV`) instructions, and for input/output (`IN`/`OUT`) operations. Many instructions run faster when using AX.|
|**Base**|`BX`|`BH`|`BL`|Can be used to hold the offset address of a memory location. It's the only data register that can be used as a pointer in certain addressing modes.|
|**Count**|`CX`|`CH`|`CL`|Used as an automatic counter for string instructions (`REP`) and loops (`LOOP`). Shift and rotate instructions use the value in `CL` to determine how many bits to shift.|
|**Data**|`DX`|`DH`|`DL`|A general-purpose register, but it also has special roles. It holds the upper 16 bits of the result in a 32-bit multiplication, and it's used to hold the port address for `IN`/`OUT` instructions.|

### Pointer Registers

These registers generally hold offsets within the stack segment and are used for managing the stack.

- **`SP` (Stack Pointer):** Always points to the top of the stack. `PUSH` and `POP` instructions automatically update this register.
    
- **`BP` (Base Pointer):** Used to access data within the stack segment. It's often used to access function parameters and local variables on the stack without modifying `SP`.
    

### Index Registers

These registers are used to hold offsets for accessing data in memory, especially useful for arrays and strings.

- **`SI` (Source Index):** Used as the source pointer for string instructions. It holds the offset of the source data in the Data Segment.
    
- **`DI` (Destination Index):** Used as the destination pointer for string instructions. It holds the offset of the destination in the Extra Segment.
    

**Links:** [[8086 Microprocessor Architecture]], [[8086 Flags Register]]