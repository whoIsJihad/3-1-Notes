# Deadlock Detection and Recovery

**Tags:** #os #deadlock #detection #recovery #graph-theory

This strategy assumes deadlocks can happen and focuses on finding them and fixing them. It involves two phases: running a detection algorithm and then applying a recovery method.

### 1. Detection

The goal of a detection algorithm is to find a circular wait. The method depends on the number of resource instances.

#### For a Single Instance of Each Resource Type

The OS can maintain a [[Deadlock Modeling with Resource Allocation Graphs|Resource Allocation Graph]] and periodically run a depth-first search or similar algorithm to check for cycles. If a cycle is found, a deadlock exists.

#### For Multiple Instances of Each Resource Type

A graph-based approach is too complex. Instead, a matrix-based algorithm (similar to the Banker's Algorithm) is used. The core data structures are:

- **E (Existing):** A vector of total existing resources of each type. `E = (6, 3, 4, 2)`
    
- **A (Available):** A vector of currently available resources. `A = (1, 0, 2, 0)`
    
- **C (Current Allocation):** An `n x m` matrix where `C[i][j]` is the number of resources of type `j` held by process `i`.
    
- **R (Request):** An `n x m` matrix where `R[i][j]` is the number of resources of type `j` requested by process `i`.
    

**The Algorithm:** The algorithm searches for a process whose request vector `R[i]` is less than or equal to the `Available` vector `A`.

1. Find an unmarked process `Pᵢ` such that `Rᵢ ≤ A`.
    
2. If no such process exists, the algorithm terminates. Any processes still marked as "in progress" are part of a deadlock.
    
3. If such a process is found, assume it gets its resources, runs to completion, and releases all resources it was holding (its row in the `C` matrix). Add these released resources back to the `A` vector. Mark the process as "terminated" and go back to step 1.
    

### 2. Recovery

Once a deadlock has been detected, the system must break it. This is always a disruptive process.

1. **Recovery through Preemption:** Forcibly take a resource from one of the deadlocked processes and give it to another. This is difficult to do cleanly and may require the victim process to be rolled back.
    
2. **Recovery through Rollback:** Periodically checkpoint the state of processes. To break a deadlock, restore one of the processes to a prior checkpoint before it acquired the resource, forcing it to release the resource.
    
3. **Recovery through Killing Processes:** This is the simplest and crudest method.
    
    - Kill a process in the deadlock cycle. The resources it holds will be released, hopefully allowing other processes to proceed.
        
    - If that doesn't work, kill another process in the cycle until the deadlock is broken. The choice of which process to kill can be based on priority, how long it has been running, etc.