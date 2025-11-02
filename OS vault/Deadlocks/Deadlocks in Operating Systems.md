
**Tags:** #os #cse #deadlock #concurrency #map-of-content

A **deadlock** is a state in which a set of two or more processes are blocked forever, each waiting for a resource that is held by another process in the same set. It is one of the most severe problems in concurrent programming, as it can cause a group of processes—or even the entire system—to stop making progress.

This situation arises from the competition for non-preemptable resources. For instance, if Process A holds Resource X and waits for Resource Y, while Process B holds Resource Y and waits for Resource X, neither can proceed.

This collection of notes provides a comprehensive overview of the conditions that lead to deadlocks, the methods for modeling them, and the primary strategies that operating systems employ to deal with this critical issue.

### Core Concepts

- [[The Four Necessary Conditions for Deadlock]]
    
- [[Deadlock Modeling with Resource Allocation Graphs]]
    
- [[Core Strategies for Handling Deadlocks]]
    
- [[Deadlock Detection and Recovery]]
    
- [[Deadlock Avoidance and the Banker's Algorithm]]
    
- [[Deadlock Prevention]]
    
- [[Livelock and Starvation]]