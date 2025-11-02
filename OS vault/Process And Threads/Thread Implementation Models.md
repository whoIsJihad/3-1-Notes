# Thread Implementation Models

**Tags:** #os #threads #user-level #kernel-level

Threads can be implemented and managed in two main ways: entirely in user space or with support from the OS kernel.

### User-Level Threads (ULTs)

In this model, the thread management is handled by a runtime library in the user space of a process. The kernel is completely unaware that threads exist; it only sees a single-threaded process.

- **Management:** A user-level thread scheduler in the library decides which thread to run.
    
- **Context Switching:** Switching between threads is extremely fast as it involves just a local procedure call within the process, without any need for a trap into the kernel.
    
- **Main Disadvantage (Blocking):** If one user-level thread makes a blocking system call (e.g., for I/O), the entire process blocks, including all other threads within it, because the kernel cannot schedule another thread.
    

### Kernel-Level Threads (KLTs)

In this model, the kernel itself is aware of and manages the threads. The OS maintains a [[Process Control Block (PCB)]] for the process and smaller thread control blocks for each thread. Threads are scheduled by the kernel's scheduler.

- **Management:** The OS kernel handles thread creation, scheduling, and management.
    
- **Context Switching:** Switching is more expensive than with ULTs because it requires a trap to the kernel, but it's still cheaper than a full process context switch.
    
- **Main Advantage (Non-Blocking):** If one thread makes a blocking system call, the kernel can schedule another thread from the same process (or a different process) to run. This is essential for utilizing multi-core processors effectively.
    

### Hybrid Implementations (Many-to-Many Model)

This model combines the benefits of both approaches. A number of user-level threads are multiplexed onto a smaller or equal number of kernel-level threads.

- The kernel only sees the KLTs.
    
- The user-level scheduler can manage the ULTs rapidly.
    
- If a ULT blocks on a system call, the corresponding KLT blocks, but the kernel can still schedule other KLTs, which can in turn run other ULTs. This model offers flexibility but is more complex to implement.
    

Most modern operating systems (Linux, Windows, macOS) primarily use a **one-to-one model**, where each user-level thread is mapped directly to a single kernel-level thread, giving the best of the KLT approach.

**Links:** [[Multithreading Model]], [[Thread and Process Context Switching Comparison]]