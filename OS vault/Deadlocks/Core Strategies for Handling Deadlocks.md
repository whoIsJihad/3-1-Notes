# Core Strategies for Handling Deadlocks

**Tags:** #os #deadlock #strategies #ostrich-algorithm

Operating systems can adopt one of four primary strategies when it comes to dealing with deadlocks. The choice of strategy depends on the severity and frequency of the problem, and the overhead of the solution.

### 1. The Ostrich Algorithm (Ignoring the Problem)

This is the most common strategy, employed by operating systems like UNIX and Windows. The approach is to stick your head in the sand and pretend the problem doesn't exist.

- **Rationale:** Deadlocks are considered to be very rare events in a well-designed system. The performance overhead of constantly checking for them (detection), carefully allocating resources (avoidance), or imposing strict rules (prevention) is considered a higher cost than the rare inconvenience of a system freeze.
    
- **Implementation:** The OS provides no mechanisms to handle deadlocks. If the system freezes, the user is expected to reboot it.
    
- **Analogy:** It's like deciding not to buy theft insurance for a bicycle because the cost of the insurance over time is more than the cost of the bike, and the chance of theft is low.
    

### 2. Deadlock Detection and Recovery

This strategy allows deadlocks to occur, but the system periodically runs an algorithm to check for their existence. If a deadlock is detected, the system takes steps to break it.

- **When to check?** The detection algorithm can be run every time a resource is requested (expensive), on a timer (e.g., every 10 minutes), or when CPU utilization drops below a certain threshold.
    
- **See:** [[Deadlock Detection and Recovery]]
    

### 3. Deadlock Avoidance

This strategy uses a priori information about the maximum resources a process _might_ need to make careful allocation decisions. The OS will only grant a resource request if it can be sure that the resulting system state will not lead to a future deadlock.

- **Core Idea:** Never allocate a resource if doing so would put the system in an "unsafe state."
    
- **See:** [[Deadlock Avoidance and the Banker's Algorithm]]
    

### 4. Deadlock Prevention

This strategy involves designing the system in a way that structurally negates one of the [[The Four Necessary Conditions for Deadlock|four necessary conditions for deadlock]]. By making one of the conditions impossible, deadlock itself becomes impossible.

- **Approach:** This is a static approach that imposes strict rules on how resources are requested.
    
- **See:** [[Deadlock Prevention]]