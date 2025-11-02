# Context Switching

**Tags:** #os #process #context-switch #performance

In a multiprogramming environment, the operating system must switch the CPU between different processes to give the illusion of parallel execution. The mechanism for saving the state of the currently running process and restoring the state of the next one is called a **context switch**.

The "context" of a process is all the information needed to restart it, which is stored in its [[Process Control Block (PCB)]]. This includes the values of the CPU registers, the program counter, the process state, and memory-management information.

### The Context Switch Process

1. **Interrupt/System Call:** An event occurs that requires the OS to intervene. This could be a hardware interrupt, a trap, or a system call.
    
2. **Save Context:** The OS saves the context of the currently running process (Process P0) into its corresponding PCB (PCB0). This involves saving the program counter and all other CPU registers.
    
3. **Scheduler:** The OS scheduler runs to select the next process to execute from the ready queue (e.g., Process P1).
    
4. **Restore Context:** The OS loads the context of the new process (P1) from its PCB (PCB1) into the CPU registers.
    
5. **Resume Execution:** The new process (P1) resumes execution from the point where it was last stopped, as indicated by the restored program counter.
    

### Overhead of Context Switching

Context switching is pure overhead; the system does no useful work for any user process during the switch. The cost of a context switch is significant because:

- It requires saving and loading numerous registers.
    
- It involves executing the OS scheduler code.
    
- It can invalidate the CPU's caches (instruction and data caches) and the Translation Lookaside Buffer (TLB), leading to a performance drop as the new process must repopulate them from slower main memory.
    

This overhead is a major reason for the development of [[Introduction to Threads|threads]], which provide a more lightweight alternative for concurrency.

**Links:** [[Process Control Block (PCB)]], [[Thread and Process Context Switching Comparison]]