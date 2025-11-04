
**Tags:** #os #deadlock #prevention #strategies

Deadlock prevention is a static approach that designs the system to make deadlocks structurally impossible. It works by ensuring that at least one of the [[The Four Necessary Conditions for Deadlock]] can never be met.

### Attacking the Mutual Exclusion Condition

- **Approach:** Avoid assigning a resource exclusively to one process.
    
- **Method:** Spooling is a classic example. A printer is a non-shareable resource. However, processes can direct their output to a spooler daemon, which manages a queue of files on disk. The only process that directly requests the printer is the daemon. This eliminates the mutual exclusion for processes wanting to "print," but it can create a new deadlock for finite spooling disk space.
    
- **Feasibility:** This is not always possible. Some resources, like a CPU register, are inherently exclusive.
    

### Attacking the Hold and Wait Condition

- **Approach:** A process cannot hold resources while waiting for another.
    
- **Method 1:** Require a process to request **all** its required resources at the very beginning. The OS either grants all of them or none of them.
    
- **Method 2:** A process must temporarily release all resources it currently holds before requesting a new one.
    
- **Problems:**
    
    - Processes often don't know their maximum resource needs in advance.
        
    - This is highly inefficient. A process might hold resources for hours when it only needs them for a few seconds at the end, leading to low resource utilization.
        

### Attacking the No Preemption Condition

- **Approach:** If a process holding resources requests another resource that cannot be immediately allocated, it must release all resources it is currently holding.
    
- **Method:** Virtualize resources. Spooling is again an example.
    
- **Feasibility:** This is difficult to implement and only works for resources whose state can be easily saved and restored, like memory or CPU registers. It doesn't work for a printer that is halfway through a job.
    

### Attacking the Circular Wait Condition

- **Approach:** Impose a total ordering of all resource types and require that each process requests resources in an increasing order of enumeration.
    
- **Method:** Assign a unique number to each resource (e.g., 1=Scanner, 2=Disk Drive, 3=Printer). A process can request a Scanner and then a Printer (1 -> 3), but it cannot request a Printer and then a Scanner (3 -> 1).
    
- **Logic:** This makes a circular wait impossible. A process holding resource `i` can only request resources `j` where `j > i`. This linear ordering prevents a cycle from ever forming in the resource allocation graph.
    
- **Feasibility:** This is one of the most practical prevention techniques, but it can be restrictive for programmers and may not correspond to the natural order of resource use.
    

|Condition Attacked|Prevention Approach|
|---|---|
|**Mutual Exclusion**|Spooling resources|
|**Hold and Wait**|Request all resources at once|
|**No Preemption**|Forcibly take resources away (virtualize)|
|**Circular Wait**|Order resources numerically|