# Data Addressing Modes

**Tags:** #8086 #addressing_modes #assembly

Addressing modes are the rules the CPU uses to calculate the **Effective Address (EA)** of an operand. The 8086 provides a rich set of modes for accessing data, which makes its assembly language powerful and flexible.

### 1. Immediate Addressing

The operand is a constant value encoded directly into the instruction itself.

- **Example:** `MOV AX, 1234H`
    
- **How it works:** The value `1234H` is stored in the last two bytes of the machine code. The CPU fetches these bytes and loads them directly into `AX`. No memory access is needed for the operand.
    

### 2. Register Addressing

The operand is located in one of the CPU's general-purpose registers.

- **Example:** `MOV AX, BX`
    
- **How it works:** The CPU moves the data directly from the internal `BX` register to the `AX` register. This is the fastest type of data access.
    

### 3. Direct Addressing

The operand is in memory at a specific address. The 16-bit offset of this address is encoded directly in the instruction.

- **Example:** `MOV AL, [2000H]`
    
- **How it works:** The value `2000H` is the displacement. The CPU calculates the physical address as `DS:2000H` and fetches the byte from that memory location into `AL`.
    

### 4. Register Indirect Addressing

The operand is in memory, and the register specified in the instruction holds the operand's 16-bit offset.

- **Example:** `MOV AX, [BX]`
    
- **How it works:** The CPU reads the value from `BX`. Let's say `BX` contains `3000H`. The CPU then calculates the physical address as `DS:3000H` and fetches the word from that memory location into `AX`. This is powerful for iterating through data arrays.
    

### 5. Register Relative Addressing

The operand is in memory at an address calculated by adding a register and a displacement.

- **Example:** `MOV AX, [BX + 100H]` or `MOV AX, ARRAY[BX]`
    
- **How it works:** This is ideal for accessing elements in a struct or array. `BX` holds the base address of the data structure, and the displacement (`100H`) is the fixed offset to a specific field or element. The physical address is calculated from `DS:(BX + 100H)`.
    

### 6. Base-Plus-Index Addressing

The operand is in memory at an address calculated by adding a base register (`BX` or `BP`) and an index register (`SI` or `DI`).

- **Example:** `MOV AX, [BX + SI]`
    
- **How it works:** This mode is perfect for accessing elements in a 2D array or an array of structs. `BX` can hold the base address of the array, and `SI` can hold the index of the desired element. The physical address is calculated from `DS:(BX + SI)`.
    

### 7. Base-Relative-Plus-Index Addressing

This is the most complex mode, combining a base register, an index register, and a displacement.

- **Example:** `MOV AX, [BX + SI + 10H]`
    
- **How it works:** This is used for complex data structures. For example, `BX` could point to the start of a struct, `SI` could be an index into an array within that struct, and `10H` could be the offset to a specific field within an element of that array. The physical address is calculated from `DS:(BX + SI + 10H)`.
    

**Links:** [[8086 Instruction Encoding and Addressing Modes]]