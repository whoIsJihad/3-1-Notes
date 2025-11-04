# The Problem

> (b) Consider a variation of the classical producer consumer problem. In this variation, there is only one consumer and $M$ producers $P_1, P_2, \dots, P_M$ and all producers belong to the same priority class. Producers produce item in a cyclic order. For example, producer $P_1$ produces first, then producer $P_2$, and so on. After producer $P_M$ produces an item, it enables producer $P_1$ to produce an item. Note that, the order of producing items and the order of insertion in the buffer may not always be the same.
> 
> A solution to the classical Producer-Consumer problem is presented in Figure 2(b). Modify this solution with minimal changes to obtain a solution for the above mentioned problem. [You do not need to write down the consumer code.]

# Solution

This solution uses one new semaphore array, `turn`, to enforce the cyclic production order. The classical semaphores (`mutex`, `empty`, `full`) are assumed to be part of the solution we are modifying.

```
// --- 1. Shared Data and Semaphores ---

// Assumed buffer size (e.g., N)
int N; 

// Classical semaphores from the original solution
sem mutex = 1;   // For mutual exclusion of the buffer
sem empty = N;   // Counts empty buffer slots
sem full = 0;    // Counts full buffer slots

// --- MINIMAL CHANGE: New semaphore array for cyclic order ---
// (Assuming M producers, P1 to PM)
sem turn[M+1]; // Using 1-based indexing to match P1...PM


// --- 2. Semaphore Initialization ---
void initialize_semaphores() {
    // Classical initialization (already done)
    mutex = 1;
    empty = N;
    full = 0;
    
    // --- MINIMAL CHANGE: Initialize turn semaphores ---
    // P1 starts first
    turn[1] = 1; 

    // All other producers (P2 to PM) must wait
    for (int i = 2; i <= M; i++) {
        turn[i] = 0;
    }
}


// --- 3. Modified Producer Code (for Producer P_i) ---

// This code runs for each producer P_i (where i is from 1 to M)
void producer(int i) {
    
    // Calculate the *next* producer in the cycle
    // (i % M) + 1 handles the wrap-around from M back to 1
    int next_producer_id = (i % M) + 1;

    while (true) {
        
        // --- MINIMAL CHANGE: Wait for this producer's turn ---
        wait(turn[i]);

        // --- Start of Classical Producer Logic ---
        
        // Wait for an empty slot in the buffer
        wait(empty);
        
        // Acquire lock for the buffer
        wait(mutex);

        // --- Critical Section ---
        // ...
        // produce_item();
        // add_item_to_buffer();
        // ...
        // --- End Critical Section ---

        // Release lock
        signal(mutex);
        
        // Signal that a slot is now full (for the consumer)
        signal(full);

        // --- End of Classical Producer Logic ---

        // --- MINIMAL CHANGE: Pass the turn to the next producer ---
        signal(turn[next_producer_id]);
    }
}
```