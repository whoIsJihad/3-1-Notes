# Preemptive vs Non-preemptive Scheduling

**Tags:** #os #scheduling #preemption

Scheduling algorithms can be broadly divided into two categories based on how they handle a process that is currently allocated the CPU.

### Non-preemptive Scheduling

In non-preemptive scheduling (also called **cooperative** scheduling), once a process is given the CPU, it keeps the CPU until it voluntarily relinquishes it. A process gives up the CPU in only two situations:

1. When the process terminates.
    
2. When the process switches to the `Waiting` state (e.g., for an I/O request).
    

The scheduler has no power to forcibly stop a process that is running. This model is simple to implement but has a major drawback: a long-running or uncooperative process can monopolize the CPU, making the entire system unresponsive.

- **Examples:** [[First-Come, First-Served (FCFS) Scheduling]], non-preemptive [[Shortest Job First (SJF) Scheduling]].
    

### Preemptive Scheduling

In preemptive scheduling, the operating system has the power to interrupt a running process and forcibly take the CPU away from it, moving the process to the `Ready` state. This is typically done when a process has used up its allocated time slice (quantum) or when a higher-priority process becomes ready to run.

This model is more complex as it requires careful handling of shared data, but it is essential for modern time-sharing and interactive operating systems. It ensures that no single process can dominate the CPU, leading to better system responsiveness and fairness.

- **Examples:** [[Round Robin (RR) Scheduling]], preemptive [[Shortest Job First (SJF) Scheduling]] (SRTF).
    

**Links:** [[CPU Scheduling]], [[When to Schedule]]