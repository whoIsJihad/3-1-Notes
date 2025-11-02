# Early Solutions for Mutual Exclusion: A Deep Dive

**Tags:** #os #ipc #concurrency #busy-waiting #peterson #priority-inversion

Solving the [[The Critical Section Problem]] is non-trivial. Early attempts, while ultimately flawed, are crucial to study because they reveal the subtle but profound difficulties of concurrent programming. These solutions primarily rely on **busy-waiting**, where a process actively consumes CPU cycles while waiting for a condition to be met.

### 1. Disabling Interrupts

**The "How":** This is the simplest and most forceful approach. A process disables all interrupts immediately upon entering its critical section and re-enables them just before leaving.

```
while (TRUE) {
    disable_interrupts();
    // Critical Section
    enable_interrupts();
    // Remainder Section
}
```

**The "Why" it Fails:**

- **Doesn't Work on Multicore Systems:** Disabling interrupts only affects the CPU core the code is running on. Another process on a different core can still access the shared memory concurrently, completely defeating the purpose of mutual exclusion.
    
- **Dangerous User-Level Privilege:** If a user process were given the power to disable interrupts, it could maliciously or accidentally never re-enable them, bringing the entire system to a halt. The OS scheduler, which relies on timer interrupts, would cease to function. For this reason, it's a kernel-level-only technique.
    

### 2. Lock Variables

**The "How":** This approach uses a single shared integer, `lock`, initialized to `0`. A value of `0` means the critical section is free, and `1` means it is occupied.

```
// Process P0
while (lock != 0) { /* do nothing */ }
lock = 1;
// Critical Section
lock = 0;
```

**The "Why" it Fails (A Classic Race Condition):** The check (`while (lock != 0)`) and the set (`lock = 1;`) are two separate instructions. The failure occurs if a process is interrupted between them.

1. **Process P0** executes `while (lock != 0)`. It sees `lock` is `0` and exits the loop.
    
2. **A context switch occurs!** The scheduler preempts P0 and runs P1.
    
3. **Process P1** executes `while (lock != 0)`. It also sees that `lock` is `0` and exits the loop.
    
4. P1 then executes `lock = 1;` and enters its critical section.
    
5. **A context switch occurs!** The scheduler preempts P1 and resumes P0.
    
6. **Process P0** resumes from where it left off. It has _already_ passed the `while` check, so it now executes `lock = 1;` and also enters its critical section.
    

Mutual exclusion is violated. This solution fails because it contains the very race condition it was designed to prevent.

### 3. Strict Alternation

**The "How":** This solution for two processes uses a shared integer `turn`, initialized to `0` or `1`, to strictly alternate which process can enter its critical section.

```
// Process P0
while (TRUE) {
    while (turn != 0) { /* loop */ }
    // Critical Section
    turn = 1;
    // Remainder Section
}

// Process P1
while (TRUE) {
    while (turn != 1) { /* loop */ }
    // Critical Section
    turn = 0;
    // Remainder Section
}
```

**The "Why" it Fails:** This solution enforces mutual exclusion but violates the **Progress** requirement. If P0 needs to enter its critical section multiple times in a row while P1 is busy in its remainder section, P0 cannot. After one entry, it sets `turn = 1` and is now blocked, busy-waiting for P1 to take its turn, even though P1 has no interest in the critical section. This is unacceptably inefficient if the processes run at different speeds.

### 4. Peterson's Solution

**The "How":** This is the first correct software-only solution for two processes. It elegantly combines the ideas of signaling intent (`interested` array) and arbitrating with a `turn` variable.

- `int interested[2];` // Both initialized to FALSE
    
- `int turn;`
    

```
// Code for Process i (where j = 1 - i)
while (TRUE) {
    interested[i] = TRUE;
    turn = j;
    while (interested[j] && turn == j) { /* loop */ }
    // Critical Section
    interested[i] = FALSE;
    // Remainder Section
}
```

**The "Why" it Works:** A process `i` only enters if the other process `j` is _not_ interested, OR if it is `i`'s turn to break the tie. If both processes become interested simultaneously, the `turn` variable acts as the tie-breaker, ensuring only one proceeds while the other waits. This satisfies all four conditions for a good solution.

### The Overarching Problem with Busy-Waiting: Priority Inversion

Beyond wasting CPU cycles, busy-waiting can lead to a catastrophic failure mode called **Priority Inversion**.

1. A **low-priority process (L)** acquires a lock and enters its critical section.
    
2. A **high-priority process (H)** becomes ready to run. The scheduler preempts L and starts running H.
    
3. H attempts to acquire the same lock, finds it busy, and starts busy-waiting in a tight loop.
    
4. Because H has high priority, the scheduler will always choose to run H over L.
    
5. **The Result:** L never gets scheduled, so it can never finish its critical section and release the lock. H, the high-priority process, will busy-wait forever. The high-priority process is effectively blocked by the low-priority process.