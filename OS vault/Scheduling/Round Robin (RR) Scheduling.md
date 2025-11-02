# Round Robin (RR) Scheduling

**Tags:** #os #scheduling #algorithms #round-robin

**Round Robin (RR)** is a preemptive scheduling algorithm designed specifically for time-sharing systems. It is similar to [[First-Come, First-Served (FCFS) Scheduling|FCFS]], but preemption is added to switch between processes.

### How it Works

1. A small unit of time, called a **time quantum** or **time slice** (typically 10-100 milliseconds), is defined.
    
2. The ready queue is treated as a circular queue.
    
3. The CPU scheduler goes around the ready queue, allocating the CPU to each process for a time interval of up to one time quantum.
    
4. If the process finishes its CPU burst within the quantum, it relinquishes the CPU voluntarily.
    
5. If the process's CPU burst is longer than the quantum, the timer goes off, generating an interrupt. The OS performs a context switch, moves the current process to the tail of the ready queue, and dispatches the next process in the queue.
    

### Example

Processes with a time quantum of 20 ms:

|Process|Burst Time|
|---|---|
|P1|53|
|P2|17|
|P3|68|
|P4|24|

**Gantt Chart:**

```
  P1    P2    P3    P4    P1    P3    P4    P1    P3    P3
|-----|-----|-----|-----|-----|-----|----|-----|-----|----|
0    20    37    57    77    97   117   121   134   154  162
```

**Execution Trace:**

- P1 runs for 20 ms (33 left).
    
- P2 runs for 17 ms (finishes).
    
- P3 runs for 20 ms (48 left).
    
- P4 runs for 20 ms (4 left).
    
- P1 runs for 20 ms (13 left).
    
- P3 runs for 20 ms (28 left).
    
- P4 runs for 4 ms (finishes).
    
- P1 runs for 13 ms (finishes).
    
- P3 runs for 20 ms (8 left).
    
- P3 runs for 8 ms (finishes).
    

### Performance of RR

The performance of RR is highly dependent on the size of the time quantum.

- **Large Quantum:** RR behaves like FCFS.
    
- **Small Quantum:** RR provides better response time, but the overhead from frequent context switching becomes very high.
    

The quantum must be large with respect to the context switch time to be efficient.

**Links:** [[CPU Scheduling]], [[Preemptive vs Non-preemptive Scheduling]]