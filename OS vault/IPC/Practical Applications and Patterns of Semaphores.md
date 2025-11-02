# Practical Applications and Patterns of Semaphores

**Tags:** #os #ipc #semaphore #mutex #synchronization

Semaphores are a versatile tool that can be used to solve different kinds of concurrency problems. As shown in the lecture, their usage can be categorized into three main patterns based on how they are initialized and used.

### 1. Mutual Exclusion

This is the most common use case, where a semaphore acts as a lock to protect a critical section.

- **Pattern:** A single **binary semaphore (mutex)** is initialized to `1`.
    
- **Implementation:**
    
    ```
    semaphore mutex = 1;
    
    do {
        down(&mutex);
            // Critical Section
        up(&mutex);
            // Remainder Section
    } while (TRUE);
    ```
    
- **Logic:** The first process to call `down(&mutex)` will find the value is `1`, decrement it to `0`, and enter the critical section. Any other process that subsequently calls `down(&mutex)` will find the value is `0` and will block. The process remains blocked until the first process calls `up(&mutex)`, which increments the value back to `1` and unblocks a waiting process.
    

### 2. Controlling Access to a Limited Resource Pool

This pattern is used when you have a pool of `m` identical resources (e.g., database connections, printer buffers) and you want to allow up to `m` processes to use them concurrently.

- **Pattern:** A **counting semaphore** is initialized to `m`, the number of available resources.
    
- **Implementation:**
    
    ```
    #define M 5 // e.g., 5 available resources
    semaphore resource_pool = M;
    
    // A process wanting to use a resource
    down(&resource_pool);
        // Use one of the resources
    up(&resource_pool); // Release the resource back to the pool
    ```
    
- **Logic:** The first `m` processes to call `down(&resource_pool)` will succeed, decrementing the value each time (from `m` down to `0`). The `(m+1)`-th process will find the value is `0` and will block. It will only be unblocked when one of the other processes finishes and calls `up(&resource_pool)`, incrementing the value from `0` to `1`.
    

### 3. Synchronization (Enforcing Order)

This powerful pattern is used to guarantee that a specific event in one process happens only after another specific event in a different process has occurred.

- **Pattern:** A single **binary semaphore** is initialized to `0`.
    
- **Implementation:** Suppose we require statement `S2` in Process P2 to execute only _after_ statement `S1` in Process P1 has completed.
    
    ```
    semaphore synch = 0;
    
    // Process P1
    S1;
    up(&synch); // Signal that S1 is done.
    
    // Process P2
    down(&synch); // Wait for the signal from P1.
    S2;
    ```
    
- **Logic:** If P2 runs first, it will immediately call `down(&synch)`. Since the value is `0`, P2 will block. It will remain blocked until P1 runs, completes `S1`, and calls `up(&synch)`. This increments `synch` from `0` to `1` and wakes up P2. P2 can then complete its `down` operation (decrementing `synch` back to `0`) and proceed to execute `S2`. This enforces the desired order regardless of how the scheduler runs the processes.