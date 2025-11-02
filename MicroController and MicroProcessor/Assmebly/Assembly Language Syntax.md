# Assembly Language Syntax

**Tags:** #assembly #syntax #programming

An assembly language program is a sequence of statements, with one statement per line. Each statement follows a basic syntax, though not all parts are required for every statement. Assembly language is generally **not case-sensitive**, but by convention, we use uppercase for instructions and registers and lowercase for variable and label names.

**General Syntax:**

```
Label:   Operation   Operand(s)   ; Comment
```

- Fields must be separated by at least one space or tab.
    

### 1. Label (or Name)

- **Purpose:** An optional identifier that marks a specific line in the code. The assembler translates the label into a memory address. This is essential for `JMP` (jump) and `CALL` instructions.
    
- **Rules:** Can be up to 31 characters long. Must not start with a digit.
    

### 2. Operation

- **Purpose:** This is the main part of the statement and is required. It can be one of two things:
    
    - **Instruction Opcode:** A symbolic name for a machine instruction (e.g., `MOV`, `ADD`, `SUB`). The assembler translates this into binary machine code.
        
    - **Assembler Directive (Pseudo-op):** An instruction _to the assembler_ itself (e.g., `PROC`, `DB`, `.MODEL`). These do not translate to machine code but control how the assembler builds the program.
        

### 3. Operand(s)

- **Purpose:** Specifies the data that the operation will work on. An instruction can have zero, one, or two operands.
    
- **Syntax (for two operands):** `Operation destination, source`
    
    - The **destination** operand is always first. This is where the result of the operation is stored.
        
    - The **source** operand provides one of the values for the operation.
        

### 4. Comment

- **Purpose:** An optional explanation of what the line of code does.
    
- **Syntax:** Anything following a semicolon (`;`) on a line is ignored by the assembler.
    
- **Importance:** Good commenting is **critical** in assembly language because the logic is often not immediately obvious from the instructions alone.
    

**Example Breakdown:**

```
START_LOOP:   MOV CX, 10      ; Initialize loop counter to 10
```

- `START_LOOP:` is the **Label**.
    
- `MOV` is the **Operation** (an instruction).
    
- `CX, 10` are the **Operands** (`CX` is the destination, `10` is the source).
    
- `; Initialize loop counter to 10` is the **Comment**.
    

**Links:** [[Introduction to Assembly Language]]