# Deadlock Modeling with Resource Allocation Graphs

**Tags:** #os #deadlock #graph-theory #resource-modeling

A Resource Allocation Graph is a directed graph used to visually model the state of resource allocations and requests in a system. It provides a precise way to determine if a deadlock exists.

### Graph Notation

The graph consists of two types of nodes and two types of edges:

- **Process Nodes:** Represented by circles (e.g., A, B, C).
    
- **Resource Nodes:** Represented by squares (e.g., R, S, T). If a resource type has multiple identical instances, dots are placed inside the square.
    
- **Request Edge:** A directed edge from a process to a resource (`A → S`) signifies that Process A is currently requesting Resource S and is waiting for it.
    
- **Assignment Edge:** A directed edge from a resource to a process (`R → A`) signifies that Resource R has been allocated to Process A.
    

### Detecting Deadlock with Graphs

The presence of a **cycle** in the Resource Allocation Graph is the key indicator of a potential or actual deadlock.

- **If the graph contains no cycles:** The system is **not** in a deadlocked state.
    
- **If the graph contains a cycle:**
    
    - If each resource type has only **one instance**, then a cycle **guarantees** a deadlock.
        
    - If resource types have **multiple instances**, a cycle indicates the **possibility** of a deadlock, but it is not a certainty.
        

### Example Walkthrough (from slides)

Consider the following sequence of events:

1. A requests R (`A → R`)
    
2. B requests S (`B → S`)
    
3. C requests T (`C → T`)
    
    - At this point, R is assigned to A, S to B, T to C. The graph has no cycles.
        
    - 4. A requests S (`A → S`)
            
4. B requests T (`B → T`)
    
5. C requests R (`C → R`)
    
    - Now, a cycle has formed: `A → S → B → T → C → R → A`.
        
    - Since each resource has only one instance, the processes A, B, and C are now in a deadlock.
        

This modeling is the basis for [[Deadlock Detection and Recovery|deadlock detection algorithms]], which essentially search for cycles in the system's state graph.