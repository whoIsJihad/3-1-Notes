
**Tags:** #os #deadlock #avoidance #bankers-algorithm #safe-state

Deadlock avoidance is a dynamic strategy that requires the OS to know the **maximum possible resource claims** of each process in advance. With this information, the OS can make allocation decisions that guarantee the system will never enter a deadlocked state.

### Safe vs. Unsafe States

The core of this strategy is the concept of a **safe state**.

- **Safe State:** A state is safe if there exists some scheduling order in which every process can run to completion, even if they all request their maximum resources. The system can guarantee that deadlock will not occur.
    
- **Unsafe State:** A state is unsafe if no such completion sequence exists. An unsafe state does **not** guarantee a deadlock will occur (processes might not request their max resources), but it means the OS cannot guarantee that a deadlock _won't_ happen.
    

Deadlock avoidance algorithms ensure the system never enters an unsafe state.

### The Banker's Algorithm (for Multiple Resource Instances)

Proposed by Dijkstra, this is the classic algorithm for deadlock avoidance. It is named after the analogy of a banker who has a fixed amount of capital and must decide whether to grant loans to customers. A loan is only granted if the banker is sure they will have enough capital remaining to satisfy all other customers.

**Data Structures:** Similar to the detection algorithm, it uses vectors and matrices for Existing, Available, Current Allocation, and one more:

- **Max:** An `n x m` matrix where `Max[i][j]` is the maximum number of resources of type `j` that process `i` will ever request.
    
- **Need:** The algorithm calculates a `Need` matrix, where `Need = Max - Current Allocation`.
    

**The Safety Algorithm:** The algorithm checks if the current state is safe. It simulates if there is at least one sequence in which all processes can finish.

1. Initialize a `Work` vector equal to `Available`, and a `Finish` vector (for all processes) to `false`.
    
2. Find a process `Pᵢ` such that `Finish[i]` is `false` and its `Needᵢ` vector is less than or equal to the `Work` vector.
    
3. If no such process exists, go to step 5.
    
4. If found, pretend this process runs to completion. Update `Work = Work + Allocationᵢ` and set `Finish[i]` to `true`. Go back to step 2.
    
5. If `Finish` is `true` for all processes, the state is **safe**. Otherwise, it is **unsafe**.
    

**Resource-Request Algorithm:** When a process `Pᵢ` requests resources `Requestᵢ`:

1. Check if `Requestᵢ ≤ Needᵢ`. If not, it's an error.
    
2. Check if `Requestᵢ ≤ Available`. If not, the process must wait.
    
3. If both checks pass, **pretend** to grant the request:
    
    - `Available = Available - Requestᵢ`
        
    - `Allocationᵢ = Allocationᵢ + Requestᵢ`
        
    - `Needᵢ = Needᵢ - Requestᵢ`
        
4. Run the **Safety Algorithm** on this new, hypothetical state.
    
5. If the new state is **safe**, the allocation is made permanent. If it is **unsafe**, the request is denied, and the state is reverted. The process must wait.