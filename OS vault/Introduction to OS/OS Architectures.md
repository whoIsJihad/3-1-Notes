# OS Architectures

**Tags:** #os #architecture #monolithic #microkernel #hybrid

The internal structure of an [[OS Kernel]] can be broadly categorized into three main designs: Monolithic, Microkernel, and Hybrid.

### Monolithic Kernel

In a monolithic architecture, the entire operating system—including the file system, memory management, CPU scheduling, and device drivers—is packaged into a single, large executable that runs in a single address space in kernel mode.

- **Key Characteristic:** High-performance due to direct function calls between components, but low reliability as a single faulty driver can crash the entire system.
    
- **Examples:** Traditional UNIX, Linux.
    

### Microkernel

A microkernel architecture moves as much functionality as possible out of the kernel and into user-space programs called **servers**. The kernel itself is kept minimal, responsible only for the most fundamental services like inter-process communication (IPC) and basic scheduling.

- **Key Characteristic:** High reliability and security, as a crash in a user-space server (like a device driver) does not bring down the OS. This comes at the cost of performance due to the overhead of message passing.
    
- **Examples:** QNX, Mach.
    

### Hybrid Kernel

A hybrid kernel is a pragmatic compromise, attempting to combine the performance of a monolithic kernel with the stability and modularity of a microkernel. Core services run in the kernel for speed, while others can run as servers in user-space.

- **Key Characteristic:** A mixed approach. In practice, many hybrid kernels end up moving critical performance-sensitive components (like graphics drivers) into the kernel, making them behave very much like monolithic kernels.
    
- **Example: Windows (NT Kernel)**
    
    - Windows was designed as a hybrid kernel with a layered architecture.
        
    - However, for performance reasons, critical components like the Graphics Device Interface (GDI) and Window Manager were moved from user-space into a kernel-mode module (`win32k.sys`).
        
    - Because of this, a faulty graphics driver can cause a system-wide crash (the Blue Screen of Death), a behavior characteristic of monolithic systems.
        

**Links:** [[OS Kernel]], [[Introduction to Operating Systems (index)]]