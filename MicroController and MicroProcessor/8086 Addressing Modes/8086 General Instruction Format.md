# 8086 General Instruction Format

**Tags:** #8086 #instruction_set #machine_code

Unlike modern RISC architectures (like MIPS) where every instruction is a fixed size (e.g., 32 bits), the 8086 is a **CISC (Complex Instruction Set Computer)** architecture. Its instructions have a **variable length**, ranging from 1 to 6 bytes. This complexity allows for very dense code but makes the decoding hardware more complicated.

The general structure of a multi-byte instruction can be visualized as a template:

|Byte 1|Byte 2|Bytes 3 & 4|Bytes 5 & 6|
|---|---|---|---|
|**Opcode** & Flags|**MOD, REG, R/M**|**Displacement**|**Immediate Data**|
|(Required)|(Often Required)|(Optional)|(Optional)|

### Breakdown of the Bytes

- **Byte 1: The Opcode Byte**
    
    - **Opcode (Operation Code):** The first 6-7 bits uniquely identify the instruction (e.g., `MOV`, `ADD`, `JMP`).
        
    - **Flags:** This byte often includes 1-2 special flag bits that modify the instruction's behavior, such as:
        
        - `D` (Direction): Specifies if a register is the source or destination.
            
        - `W` (Word): Specifies if the operation is on a byte (8 bits) or a word (16 bits).
            
- **Byte 2: The Addressing Mode Byte**
    
    - This byte is present in most instructions that have operands (like `MOV` or `ADD`). It tells the CPU _where_ to find the data.
        
    - **`MOD` (Mode field, 2 bits):** Specifies whether the operand is a register or a memory location and the size of the displacement.
        
    - **`REG` (Register field, 3 bits):** Identifies one of the register operands.
        
    - **`R/M` (Register/Memory field, 3 bits):** Identifies the other register operand or, in combination with `MOD`, specifies the memory addressing mode.
        
- **Bytes 3 & 4: Displacement**
    
    - These optional bytes are used when the addressing mode requires an offset (a memory address or constant value).
        
    - This can be an 8-bit displacement (stored in Byte 3) or a 16-bit displacement (stored in Bytes 3 and 4, with the low byte first).
        
    - For example, in `MOV AX, [1234H]`, the value `1234H` is the displacement.
        
- **Bytes 5 & 6: Immediate Data**
    
    - These optional bytes are used when an instruction includes a constant value directly.
        
    - For example, in `MOV AX, 1234H`, the value `1234H` is immediate data.
        

The assembler's job is to look at a line of assembly code and fill out this template with the correct binary values, producing the final machine code.

**Links:** [[Decoding the MOV Instruction]], [[8086 Instruction Encoding and Addressing Modes]]