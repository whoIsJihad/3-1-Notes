# The Critical Section Problem

**Tags:** #os #ipc #concurrency #race-condition

The central challenge in concurrent programming is managing access to shared resources. When multiple processes attempt to read and write to the same shared data, the final result can become unpredictable and incorrect, depending on the exact order in which their instructions are executed.

### Race Conditions

A **race condition** is a situation where the behavior of a system depends on the non-deterministic timing of uncontrollable events. In operating systems, it occurs when multiple processes access and manipulate shared data concurrently, and the outcome depends on the particular order in which the access takes place.

**Example: A Print Spooler** Consider a print spooler directory with a shared variable `in` that points to the next free slot.

- Process A reads `in`, which has a value of 7.
    
- A context switch occurs. Process B runs.
    
- Process B also reads `in`, which is still 7. Process B writes its file to slot 7 and updates `in` to 8.
    
- A context switch occurs. Process A runs again.
    
- Process A, having already read the value 7, now writes its file to slot 7, overwriting Process B's file. It then updates `in` to 8.
    

The system is now in an inconsistent state: one file has been lost, and the `in` pointer is correct, masking the error.

### Critical Sections

To prevent race conditions, we must ensure mutual exclusion. The part of a program where a shared resource is accessed is called a **critical section** or **critical region**.

### Requirements for a Valid Solution

Any robust solution to the critical section problem must satisfy four conditions:

1. **Mutual Exclusion:** No two processes may be simultaneously inside their critical sections.
    
2. **Progress:** If no process is executing in its critical section and some processes wish to enter, then only those processes that are not in their remainder sections can participate in deciding which will enter its critical section next, and this selection cannot be postponed indefinitely.
    
3. **Bounded Waiting:** There must be a bound on the number of times that other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted. This prevents starvation.
    
4. **No Assumptions:** The solution must not make any assumptions about relative process speeds or the number of CPUs.
    

**Links:** [[Early Solutions for Mutual Exclusion]], [[Interprocess Communication and Synchronization]]