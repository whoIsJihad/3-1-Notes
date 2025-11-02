# Introduction to Threads

**Tags:** #os #threads #concurrency #lightweight-process

Creating a new process is expensive because it requires the OS to set up a new [[Process Address Space]] and a new [[Process Control Block (PCB)]]. [[Context Switching]] between processes is also costly. To provide a more efficient way to achieve concurrency, modern operating systems support **threads**.

A thread is the smallest unit of execution that an OS can schedule. It can be thought of as a **lightweight process**.

- A traditional process has a single thread of execution.
    
- A multi-threaded process can have multiple threads of execution running concurrently.
    

Threads are the unit of scheduling, while processes are the containers in which threads execute. All threads within a single process share the same address space and resources, but each thread has its own private execution context.

### Key Characteristics

- **Shared Resources:** Threads within the same process share the code segment, data segment, and open files. This allows for easy and efficient communication between them.
    
- **Private State:** Each thread has its own program counter (PC), register set, and execution stack. This allows each thread to execute independently.
    

Because threads share so much state, creating a new thread and context switching between threads is much faster than doing so for processes. This makes them ideal for tasks that can be broken down into parallel sub-tasks within a single application, such as a web server handling multiple client requests simultaneously.

**Links:** [[Processes vs Threads]], [[Multithreading Model]]