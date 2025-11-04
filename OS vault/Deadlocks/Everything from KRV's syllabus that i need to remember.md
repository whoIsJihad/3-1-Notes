# Quick Reference: Process Life Cycle & Kernel Split

## 1. The Journey to a Process (From File to Memory)

- **Source Code** $\rightarrow$ **Object File:** The compiler turns your `hello.c` into raw machine code (`hello.o`)—just a blob of hex instructions and data, not runnable yet.
    
- **Linking is Key:** The **Linker** takes your object file and glues it together with necessary **Libraries** (like `libc.a`) to create the final executable file (`a.out`). This is the binary file that gets saved to the Disk.
    
- **The Magic ID:** When the OS wants to run a binary, it doesn't look at the extension (`.exe`). It looks at the first few bytes (often 4) of the file. This **Magic Number** (e.g., `0x45 4c 46` for ELF) confirms it’s a valid executable file format.
    
- **The `exec` Call:** This is the OS command that actually loads the file. It assigns the **Virtual Address (VA)** space, copies the **TEXT** and **DATA** segments from the file into that new VA, initializes the **STACK** and **HEAP** boundaries, and sets the **EIP** (Program Counter) to start execution.
    

## 2. The User/Kernel Address Split

- **Virtual Space is Partitioned:** Every process's 4GB Virtual Address space is logically divided into two distinct zones.
    
    - **User Space (Low Addresses, e.g., 0x0000...):** This is where your application code (TEXT, DATA, STACK, HEAP) lives. Execution runs in **User Mode** here (restricted privileges).
        
    - **Kernel Space (High Addresses, e.g., 0x8000... to 0xFFFF...):** This is where the OS code (kernel functions, schedulers, device drivers) lives. Execution runs in **Kernel Mode** here (full privileges).
        
- **The Isolation Boundary:** The switch between these two is the **Execution Mode** flip. The OS controls access to the high addresses.
    
- **Physical Memory Sharing (The Non-Wasteful Part):** While the **Kernel Space** _appears_ in the virtual map of every single process, it points to the **same single physical location** in RAM via the Page Table. This is done for **speed**, avoiding slow Page Table swaps during system calls.
    

## 3. The Process Definition

- **Unit of Isolation:** The process is the fundamental container. It isolates resources:
    
    - **Address Space:** Nobody touches my data.
        
    - **Execution Mode:** Restricting what the User code can do.
        
    - **Time Slice:** Making sure everyone gets a turn on the CPU.****