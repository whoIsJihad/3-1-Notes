# Semaphore Fundamentals: Definition and Atomic Operations


---

# Semaphore Fundamentals: Definition and Atomic Operations

**Tags:** #os #ipc #semaphore #concurrency #atomicity

A **semaphore** is a special integer variable used to control access to shared resources by multiple processes in a concurrent environment. Unlike a regular integer, its value cannot be read or modified directly; it can only be changed using two **atomic operations** provided by the operating system.

As defined by **Dijkstra**, a semaphore’s value is never negative.

---

### Types of Semaphores

1. **Counting Semaphore:**
    
    - Can take any non-negative integer value.
        
    - Used to manage access to a resource that has multiple instances (e.g., a buffer with _N_ slots).
        
2. **Binary Semaphore (Mutex):**
    
    - Can only take the values `0` or `1`.
        
    - Used to enforce **mutual exclusion** — ensuring that only one process can access a critical section at a time.
        

---

### The Atomic Operations

The strength of a semaphore lies in its two **atomic** operations.  
_Atomicity_ means the operation executes as one indivisible unit — no context switch or interleaving by another process can occur midway.

---

#### 1. `down(s)` — also known as `wait(s)` or `P(s)`

- Checks the semaphore’s value `s`.
    
- **If `s > 0`:**  
    The value is decremented (`s = s - 1`), and the process continues execution.
    
- **If `s == 0`:**  
    The process is **blocked** (put to sleep) without changing `s`.  
    It is placed on a waiting queue associated with the semaphore.
    

---

#### 2. `up(s)` — also known as `signal(s)` or `V(s)`

- Increments the semaphore’s value (`s = s + 1`).
    
- If one or more processes are sleeping on the semaphore, **one** of them is removed from the waiting queue and **unblocked**, allowing it to complete its `down` operation.
    
- A process **never blocks** while performing an `up`.
    

---

### Why Atomicity Matters: The Lost Wakeup Problem

Without atomicity, a timing issue known as the **lost wakeup problem** could occur — where a process signals another (`up`) before it has started waiting (`down`), causing the wakeup to be lost.

Semaphores prevent this by **remembering** the signal:  
If an `up` occurs before a `down`, the semaphore’s count increases, and the subsequent `down` will simply decrement it and continue without blocking.

---

