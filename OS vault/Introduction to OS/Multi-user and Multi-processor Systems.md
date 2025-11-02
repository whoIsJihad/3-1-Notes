# Multi-user and Multi-processor Systems

**Tags:** #os #multi-user #multi-processor #concurrency

Modern operating systems are designed to manage complex hardware and serve multiple roles simultaneously.

### Multi-user OS

A **multi-user operating system** allows multiple distinct users to access and use a computer's resources concurrently. The OS is responsible for keeping each user's data and applications separate and secure from other users.

- **Concurrent Access:** Multiple users can be logged in and running programs at the same time.
    
- **Resource Management:** The OS manages and allocates resources like CPU time, memory, and disk space among the users.
    
- **Remote Access:** This is a key feature, allowing users to log in and work from remote terminals (e.g., via SSH).
    
- **Examples:** All modern server OSes like Linux, UNIX, and Windows Server are multi-user systems.
    

### Multi-processor OS

A **multi-processor operating system** (also called a parallel or tightly-coupled system) is capable of managing and utilizing a computer with more than one CPU.

- **Increased Throughput:** The primary goal is to increase performance by running tasks in parallel across multiple processors.
    
- **Shared Resources:** The processors typically share the same physical memory, computer bus, and I/O devices.
    
- **Complex Scheduling:** The OS scheduler must be sophisticated enough to distribute tasks efficiently across all available processors to maximize utilization and avoid bottlenecks.
    
- **Examples:** Modern versions of Linux, Windows, macOS, and Solaris all support multi-processor hardware.
    

**Links:** [[Introduction to Operating Systems (index)]]