# Process Address Space

**Tags:** #os #process #memory-management #address-space

When the operating system loads a program into memory to create a process, it allocates a dedicated memory region for it known as the **process address space**. This is the set of all virtual memory addresses that the process can "see" and access. From the process's perspective, it has the entire memory to itself, which is an abstraction managed by the OS's memory management unit.

The address space is typically divided into several logical segments:

- **Text (Code) Segment:** This is a read-only segment that holds the compiled machine code of the program being executed.
    
- **Data Segment:** This segment contains global and static variables that are initialized by the programmer. Its size is fixed at compile time.
    
- **Heap:** This is a region of memory used for dynamic memory allocation during runtime. When a program in C uses `malloc()` or `new` in C++, the memory is allocated from the heap. The heap grows upwards from lower memory addresses.
    
- **Stack:** The stack is used for static memory allocation and holds temporary data such as function parameters, return addresses, and local variables. It is a LIFO (Last-In, First-Out) data structure. The stack grows downwards from higher memory addresses.
    

The space between the heap and the stack is free memory that can be allocated by either as the process runs.

**Links:** [[Program vs Process]], [[Process Control Block (PCB)]]