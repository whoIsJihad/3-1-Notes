# Multithreading Model

**Tags:** #os #threads #multithreading

In a multithreaded process, not all resources are duplicated for each thread. The model is designed for efficiency by sharing as much as possible while keeping the essential execution context separate.

### Shared vs. Private State

#### What Threads Share (Per-Process Items)

All threads within the same process share the following:

- **Address Space:** This is the most important shared resource. It includes the [[Process Address Space|text (code) segment, data segment, and heap]]. This allows threads to read and write to the same variables and data structures.
    
- **Global Variables:** Any global variable is accessible to all threads.
    
- **Open Files:** A list of file descriptors is shared. If one thread opens a file, other threads can also read from or write to it.
    
- **Child Processes:** Any child processes created by the parent process.
    

#### What is Private to Each Thread (Per-Thread Items)

Each thread must have its own private context to execute independently:

- **Program Counter (PC):** Tracks the instruction the thread is currently executing.
    
- **Registers:** The set of CPU register values for the thread.
    
- **Stack:** Each thread has its own stack, which stores local variables, function call parameters, and return addresses. This is crucial because each thread can be in a different stage of execution, calling different functions.
    
- **State:** Each thread has its own execution state (`ready`, `running`, `blocked`, etc.).
    

This model makes thread creation and [[Context Switching|context switching]] much faster than for processes, as the OS does not need to manage or change memory-related information like the address space or page tables.

**Links:** [[Introduction to Threads]], [[Thread Implementation Models]]