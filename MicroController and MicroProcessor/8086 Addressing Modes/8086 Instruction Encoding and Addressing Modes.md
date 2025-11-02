

**Tags:** #8086 #assembly #computer_architecture #instruction_set

At the lowest level, a CPU does not understand human-readable assembly instructions like `MOV AX, BX`. It only understands binary machine code. The process of translating assembly into this binary format is governed by two key concepts: the **Instruction Format** and the **Addressing Modes**.

- **Instruction Format:** This is the template or blueprint that defines how an instruction is structured in binary. For the 8086, this format is variable in length (from 1 to 6 bytes).
    
- **Addressing Modes:** These are the different methods the CPU can use to determine the location of an operand (the data being worked on). The 8086 has a rich set of modes for accessing registers, memory, or immediate values.
    

This set of notes will break down how an assembler uses these rules to convert a line of code into a string of bytes the CPU can execute.

### Core Concepts

- **[[8086 General Instruction Format]]**: A breakdown of the variable-length instruction template, explaining the purpose of each byte.
    
- **[[Decoding the MOV Instruction]]**: A deep dive into the most common instruction, showing how its specific bits (`D`, `W`, `MOD`, `REG`, `R/M`) are determined.
    
- **[[Data Addressing Modes]]**: An explanation and simulation of the various ways to access data in registers and memory.
    
- **[[Program and Stack Addressing Modes]]**: How `JMP`, `CALL`, and stack operations use specialized addressing.
    

**Quick Reference Tables:**

- [[8086 REG and W Field Encoding]]
    
- [[8086 MOD and R M Field Encoding]]