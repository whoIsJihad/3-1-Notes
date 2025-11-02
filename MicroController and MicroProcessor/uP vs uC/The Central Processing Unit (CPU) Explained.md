# The Central Processing Unit (CPU) Explained

**Tags:** #cpu #alu #control_unit #registers #computer_architecture

The Central Processing Unit (CPU) is not a single monolithic block; it's comprised of several key internal components that each have a specialized role in executing instructions.

### 1. The Arithmetic Logic Unit (ALU)

The ALU is the computational core of the CPU. As its name suggests, it performs two types of operations:

- **Arithmetic Operations:** Addition, subtraction, multiplication, and division. Interestingly, most ALUs are built around a highly optimized adder circuit, and other arithmetic operations are performed using this adder.
    
- **Logic Operations:** `AND`, `OR`, `NOT`, `XOR`, and bit-shifting operations.
    

The ALU also contains a set of **flag bits** (like the Zero Flag, Carry Flag, etc.) which are updated after every operation to reflect the outcome. These flags are stored in the [[8086 Flags Register|Flags Register]] and are crucial for decision-making in programs (e.g., `if-else` statements).

### 2. The Control Unit (CU)

The CU acts as the director or manager of the CPU. It doesn't perform any calculations itself. Instead, its job is to manage the execution process.

- **Instruction Decoding:** It fetches instructions from memory, decodes them to understand what operation is required, and what data is needed.
    
- **Signal Generation:** Based on the decoded instruction, the CU generates the necessary control signals to coordinate the other components. It tells the ALU which operation to perform, directs the registers to send or receive data, and manages the flow of information across the [[The System Bus|system bus]].
    
- **Synchronization:** It uses the system clock to ensure that all events happen in the correct sequence and at the right time.
    
- **Interrupt Handling:** The CU is responsible for responding to external signals called [[Interrupts in Computing|interrupts]].
    

### 3. Registers

Registers are extremely fast, small, temporary storage locations located directly inside the CPU. They are much faster to access than main memory.

- **Purpose:** They are used to hold the data that the ALU is currently working on, store intermediate results, and hold memory addresses.
    
- **Types:**
    
    - **General-Purpose Registers:** Can be used by programmers for a variety of tasks (e.g., `AX`, `BX` in the 8086).
        
    - **Dedicated/Special-Purpose Registers:** Have a specific function, like the Program Counter (or Instruction Pointer) which always points to the next instruction to be executed, or the Accumulator, which is a preferred register for ALU operations.
        

The number and type of registers vary significantly between different processor architectures. The size of the registers that the ALU can operate on defines the "bit-ness" of a processor (e.g., a 64-bit CPU has an ALU and registers that can handle 64-bit data in one go).

**Links:** [[Core Components of a Computer System]]