
**Tags:** #os #scheduling #dispatcher

The operating system's scheduler doesn't run constantly; it is invoked only when a specific event occurs that requires a decision about which process should run next. These events are the triggers for scheduling.

### Key Scheduling Triggers

1. **When a New Process is Created:** After a process is created (e.g., via `fork()`), both the parent and child are in the `Ready` state. The scheduler must decide whether to continue running the parent or switch to the newly created child process.
    
2. **When a Process Exits:** When the currently running process terminates, its resources are reclaimed. The CPU is now free, and the scheduler must select a new process to run from the ready queue.
    
3. **When a Process Blocks:** If a running process initiates an operation that it must wait for, it enters the `Waiting` (or blocked) state. This commonly happens for I/O requests (e.g., reading a file from a disk) or waiting for a semaphore or lock. The scheduler must then choose another process to run.
    
4. **When an I/O Interrupt Occurs:** When an I/O device finishes its work (e.g., a disk read is complete), it sends an interrupt to the CPU. This interrupt may cause a process that was in the `Waiting` state to move to the `Ready` state. The scheduler may then decide to switch from the currently running process to this newly ready process, especially if the new process has a higher priority.
    
5. **When a Clock Interrupt Occurs:** In preemptive systems, a hardware timer generates an interrupt at regular intervals. At each clock interrupt, the OS gets control. It can then decide if the current process has run for long enough (i.e., its time slice has expired) and, if so, invoke the scheduler to pick the next process.
    

**Links:** [[CPU Scheduling]], [[Preemptive vs Non-preemptive Scheduling]]