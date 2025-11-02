

**Tags:** #os #kernel #core-concept

The **Kernel** is the central component, or the heart, of an Operating System. It is the first part of the OS to be loaded into memory and remains resident for as long as the computer is running.

### Key Characteristics

- **Core Component:** The kernel has complete control over everything in the system. It manages memory, CPU scheduling, disk access, and other hardware.
    
- **Always in Memory:** It contains the most critical OS functions that must be available at all times.
    
- **Bridge to Hardware:** It acts as the fundamental bridge between application software and the physical hardware.
    
- **Privileged Execution:** The kernel runs in a privileged mode ([[Dual-Mode Operation]]) to access hardware and manage system resources securely.
    

In many systems, especially older UNIX versions, the term "kernel" was often used synonymously with "Operating System" itself.

**Links:** [[OS Architectures]], [[Dual-Mode Operation]]