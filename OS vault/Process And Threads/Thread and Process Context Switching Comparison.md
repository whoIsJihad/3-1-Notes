# Thread and Process Context Switching Comparison

**Tags:** #os #threads #process #context-switch #performance

Context switching is the process of saving the state of one execution unit and restoring the state of another. While the general principle is the same for both processes and threads, the work involved and the resulting performance overhead are vastly different.

### Process Context Switch (PCS)

A process context switch is a **heavyweight** operation. It requires the OS to perform a wide range of tasks:

1. **Mode Switch:** Trap from user mode to kernel mode.
    
2. **Save State:** Save the process's CPU registers, program counter, and stack pointer into its [[Process Control Block (PCB)]].
    
3. **Memory Management Flush:** This is the most expensive step. The switch to a new process invalidates the current [[Process Address Space]]. This requires:
    
    - Flushing the CPU's data and instruction caches.
        
    - Flushing the Translation Lookaside Buffer (TLB), which caches virtual-to-physical address translations.
        
4. **Scheduler:** Run the OS scheduler to pick the next process.
    
5. **Restore State:** Load the PCB information and memory management context (e.g., page table pointers) of the new process.
    
6. **Mode Switch:** Return from kernel mode to user mode to begin execution of the new process.
    

The cache and TLB misses that occur after the switch significantly slow down the initial execution of the new process as it must fetch data from much slower main memory.

### Thread Context Switch (TCS)

A thread context switch (between threads of the _same process_) is a **lightweight** operation.

1. **Save State:** Save only the thread-private context: CPU registers, program counter, and stack pointer.
    
2. **Scheduler:** Run the scheduler (either a user-level library or the kernel scheduler) to pick the next thread.
    
3. **Restore State:** Load the private context of the new thread.
    

**Crucially, a thread context switch does not change the process address space.** Therefore, there is **no memory management overhead**. The TLB and CPU caches remain valid, leading to much better performance. If the threads are user-level, a TCS doesn't even require a trap into the kernel, making it as fast as a procedure call.

**Conclusion:** Thread context switching is significantly faster and more efficient than process context switching, making threads the preferred mechanism for concurrent execution within a single application.

**Links:** [[Context Switching]], [[Thread Implementation Models]]