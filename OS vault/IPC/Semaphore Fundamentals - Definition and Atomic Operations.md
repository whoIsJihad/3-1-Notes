# Semaphore Fundamentals: Definition and Atomic Operations

**Tags:** #os #ipc #semaphore #concurrency #atomicity

A **semaphore** is a special integer variable used for controlling access to common resources by multiple processes in a concurrent environment. Unlike a regular integer, its value cannot be read or written to directly; it can only be manipulated through two specific, atomic operations. As per the model presented by Dijkstra, the value of a semaphore cannot be negative.

### Types of Semaphores

1. **Counting Semaphore:** The value can range over any non-negative integer domain. This type is used to control access to a resource with a finite number of instances (e.g., a buffer with N slots).
    
2. **Binary Semaphore (Mutex):** The value is restricted to either `0` or `1`. It is used as a lock to provide mutual exclusion for a single resource.
    

### The Atomic Operations

The power of a semaphore comes from its two operations, which the operating system guarantees are **atomic**. This means the entire sequence of checking the value, modifying it, and potentially blocking the process is performed as a single, indivisible unit. No context switch can occur in the middle of a `down` or `up` operation.

1. **`down(s)`** (also called `wait(s)` or `P(s)`):
    
    - Checks the semaphore's value `s`.
        
    - **If the value is greater than 0:** The OS decrements the value, and the process continues execution.
        
    - **If the value is 0:** The process is **blocked** (put to sleep) without changing the semaphore value. The process is placed on a waiting queue associated with that semaphore.
        
2. **`up(s)`** (also called `signal(s)` or `V(s)`):
    
    - Increments the semaphore's value `s`.
        
    - This operation is also atomic. If one or more processes were sleeping on the semaphore (because its value was 0 when they called `down`), the OS selects one process from the waiting queue and allows it to complete its `down` operation (i.e., it is unblocked and moved to the ready queue). A process never blocks whilecks w and the rule against negative values and the rule against negative valueshile performing an `up`.
        

This atomic nature is precisely what solve Wakeup]].m with Sleep and Wakeup|lost wakeup problem]]. An `up` call that happens before a `down` call is "remembered" in the semaphore's count. When the `down` eventually happens, it will decrement the count and proceed without sleeping, correctly consuming the wakeup signal.