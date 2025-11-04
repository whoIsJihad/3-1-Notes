# Livelock and Starvation

**Tags:** #os #deadlock #livelock #starvation #concurrency-problems

Livelock and Starvation are concurrency problems related to, but distinct from, deadlock. They also prevent processes from making progress, but for different reasons.

### Livelock

A **livelock** is a situation in which two or more processes are continuously changing their state in response to changes in the other processes, but are not doing any useful work. The processes are not blocked—they are actively running and consuming CPU—but they are stuck in a loop of futile interaction.

- **Human Analogy:** Two people trying to pass each other in a narrow hallway. They both step to their left, then both to their right, then both to their left again, continuously moving but never making progress past each other.
    
- **Technical Example:** A "polite" deadlock avoidance mechanism. Two processes need resources 1 and 2.
    
    1. Process A acquires lock 1. Process B acquires lock 2.
        
    2. Process A tries for lock 2, fails, and releases lock 1 to let B proceed.
        
    3. Process B tries for lock 1, fails, and releases lock 2 to let A proceed.
        
    4. Process A acquires lock 1 again. Process B acquires lock 2 again.
        
    5. The cycle repeats indefinitely. Both processes are busy acquiring and releasing locks but never hold both simultaneously.
        

### Starvation

**Starvation** (or indefinite postponement) is a situation where a process is perpetually denied necessary resources to proceed. The process is never deadlocked, and it could theoretically run, but some other scheduling or resource allocation policy prevents it from ever getting its turn.

- **Cause:** Often caused by simple priority-based scheduling algorithms. If there is a constant stream of high-priority processes arriving, a low-priority process might wait in the ready queue forever and never be scheduled.
    
- **Example from IPC:** The [[The Readers-Writers Problem|Readers-Writers Problem]] where readers have priority. If new readers keep arriving, a writer might be starved and never get a chance to write to the database.
    
- **Solution:** A common solution is **aging**, where the priority of a process is gradually increased the longer it waits for a resource. This eventually raises its priority high enough that it will be scheduled.