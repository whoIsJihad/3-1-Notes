
**Tags:** #os #deadlock #concurrency #coffman-conditions

A deadlock situation can arise if and only if four specific conditions hold simultaneously in a system. These are often referred to as the Coffman conditions. The absence of even one of these conditions is sufficient to make deadlock impossible.

### 1. Mutual Exclusion Condition

At least one resource must be held in a **non-shareable** mode. This means that only one process at a time can use the resource. If another process requests that resource, the requesting process must be delayed until the resource has been released.

- **Example:** A printer cannot be used by two processes simultaneously. It must be exclusively controlled.
    

### 2. Hold and Wait Condition

A process must be holding at least one resource and be waiting to acquire additional resources that are currently being held by other processes.

- **Example:** A process holds a scanner and is waiting for a printer, which is held by another process.
    

### 3. No Preemption Condition

Resources cannot be preempted. This means a resource can only be released **voluntarily** by the process holding it, after that process has completed its task. It cannot be forcibly taken away.

- **Example:** A process has opened a file for writing. The OS cannot force the process to give up control of the file until it voluntarily closes it.
    

### 4. Circular Wait Condition

There must exist a set of waiting processes `{P₀, P₁, ..., Pₙ}` such that P₀ is waiting for a resource held by P₁, P₁ is waiting for a resource held by P₂, ..., Pₙ₋₁ is waiting for a resource held by Pₙ, and Pₙ is waiting for a resource held by P₀.

- **Example:** Process A waits for Process B's resource, and Process B waits for Process A's resource. This forms a circular chain of length two.
    

Understanding these four conditions is the key to all deadlock handling strategies. [[Deadlock Prevention]] works by ensuring at least one of these conditions can never occur, while [[Deadlock Detection and Recovery|deadlock detection]] involves identifying when a circular wait has formed.