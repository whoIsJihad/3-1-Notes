# The 8086 Programmer's Model

**Tags:** #8086 #registers #cpu_architecture

The "Programmer's Model" refers to the set of CPU registers that an assembly language programmer can directly access and manipulate. The 8086 has fourteen 16-bit registers, each with a specific name and purpose.

### 1. Data Registers (General Purpose)

These four 16-bit registers can be used for general data storage and arithmetic. They are unique because they can also be accessed as two separate 8-bit registers (a High byte and a Low byte).

- **AX (Accumulator):** The primary register for arithmetic operations. It's often the most efficient register to use for calculations. (`AH` and `AL`)
    
- **BX (Base):** Can be used as a pointer to the base address of a data structure in memory. (`BH` and `BL`)
    
- **CX (Count):** Used as a counter for loop instructions (`LOOP`) and string operations. (`CH` and `CL`)
    
- **DX (Data):** Used in multiplication and division operations, and for specifying port addresses in I/O operations. (`DH` and `DL`)
    

### 2. Address Registers

These registers are used to hold memory addresses and are central to the 8086's segmented memory scheme.

**Pointer Registers:**

- **SP (Stack Pointer):** Points to the top of the current stack. Used implicitly by `PUSH` and `POP`.
    
- **BP (Base Pointer):** Points to a base location within the stack, typically used to access function parameters and local variables.
    
- **IP (Instruction Pointer):** Always contains the offset address of the _next_ instruction to be executed. You cannot modify this register directly.
    

**Index Registers:**

- **SI (Source Index):** Used as a source pointer for string operations.
    
- **DI (Destination Index):** Used as a destination pointer for string operations.
    

### 3. Segment Registers

These registers hold the starting address of the four currently active memory segments.

- **CS (Code Segment):** Points to the segment containing the program's executable instructions. Paired with `IP`.
    
- **DS (Data Segment):** Points to the segment containing the program's global and static variables.
    
- **SS (Stack Segment):** Points to the segment used for the stack. Paired with `SP` and `BP`.
    
- **ES (Extra Segment):** An extra data segment, primarily used as the destination for string operations.
    

### 4. Status Register

- **FLAGS:** A 16-bit register where each bit is a "flag" that indicates the result of the last arithmetic/logic operation (e.g., Zero Flag, Carry Flag, Sign Flag) or controls the CPU's state (e.g., Interrupt Flag).
    

**Links:** [[Introduction to Assembly Language]]