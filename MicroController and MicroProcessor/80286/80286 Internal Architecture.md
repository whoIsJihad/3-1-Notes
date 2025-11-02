# 80286 Internal Architecture

**Tags:** #80286 #cpu_architecture #pipeline

The 80286 evolved the 8086's simple two-unit (BIU/EU) design into a more sophisticated four-unit pipeline. This deeper level of parallelism allowed different stages of instruction processing to occur simultaneously, significantly boosting performance.

### The Four Functional Units

1. **Bus Interface Unit (BIU):**
    
    - **Role:** Manages all communication with the external world (memory and I/O).
        
    - **Responsibilities:**
        
        - Controls the 24-bit address bus and 16-bit data bus.
            
        - Contains a **6-byte prefetch queue**, just like the 8086, to fetch instructions before they are needed.
            
        - Communicates with coprocessors (like the 80287 math coprocessor).
            
2. **Instruction Unit (IU):**
    
    - **Role:** Decodes instructions fetched by the BIU.
        
    - **Responsibilities:**
        
        - Pulls raw instruction bytes from the BIU's prefetch queue.
            
        - Decodes up to **three instructions** in advance and places them into a **decoded instruction queue**.
            
    - **Advantage:** By decoding instructions _before_ the Execution Unit is ready for them, the CPU hides the time it takes to decode complex instructions, reducing stalls.
        
3. **Execution Unit (EU):**
    
    - **Role:** Executes the decoded instructions.
        
    - **Responsibilities:**
        
        - Takes fully decoded instructions from the IU's queue.
            
        - Contains the main register set (AX, BX, etc.) and the ALU (Arithmetic Logic Unit).
            
        - Performs all calculations and data manipulations.
            
        - Sends results back to the registers or, via the BIU, to memory.
            
4. **Address Unit (AU):**
    
    - **Role:** Calculates the final physical memory addresses. This is the **hardware Memory Management Unit (MMU)**.
        
    - **Responsibilities:**
        
        - **In Real Mode:** Performs the simple `(Segment * 16) + Offset` calculation.
            
        - **In Protected Mode:** Performs the complex task of fetching descriptors from memory, checking access rights and limits, and calculating the 24-bit physical address.
            
    - **Advantage:** By offloading address calculation to a dedicated unit, the EU can focus solely on executing instructions, further enhancing parallelism.
        

This four-stage pipeline (`Fetch -> Decode -> Execute -> Address Calculation`) was a major architectural leap, allowing the 80286 to achieve a much higher Instructions Per Clock (IPC) rate than its predecessor.

**Links:** [[The Intel 80286(index)]]