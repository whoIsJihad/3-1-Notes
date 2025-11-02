# Shortest Job First (SJF) Scheduling

**Tags:** #os #scheduling #algorithms #sjf #srtf

**Shortest Job First (SJF)** is a scheduling algorithm that selects the process with the smallest next CPU burst time to execute next. If two processes have the same burst time, [[First-Come, First-Served (FCFS) Scheduling|FCFS]] can be used to break the tie.

SJF is provably optimal in that it gives the minimum average waiting time for a given set of processes.

### Types of SJF

1. **Non-preemptive SJF:** Once the CPU is given to a process, it cannot be taken away until the process completes its CPU burst.
    
2. **Preemptive SJF (Shortest Remaining Time First - SRTF):** If a new process arrives with a CPU burst length that is less than the _remaining_ time of the currently executing process, the current process is preempted, and the new, shorter process is scheduled.
    

### Example: Non-preemptive SJF

|Process|Arrival Time|Burst Time|
|---|---|---|
|P1|0|7|
|P2|2|4|
|P3|4|1|
|P4|5|4|

**Gantt Chart:**

- At time 0, only P1 is available. It runs.
    
- P1 finishes at time 7. Now P2, P3, P4 are all in the ready queue.
    
- P3 has the shortest burst time (1), so it runs next.
    
- P3 finishes at time 8. Now P2 and P4 are left. They have the same burst time, so we use FCFS. P2 arrived first.
    
- P2 runs, finishing at time 12.
    
- P4 runs, finishing at time 16.
    

```
   P1      P3   P2      P4
|---------|--|------|------|
0         7  8      12     16
```

**Calculation of Waiting Times:**

- P1: 0 - 0 = 0
    
- P2: 8 - 2 = 6
    
- P3: 7 - 4 = 3
    
- P4: 12 - 5 = 7
    

```
Average Waiting Time = (0 + 6 + 3 + 7) / 4 = 4.0 ms
```

### The Problem with SJF

The major challenge with SJF is knowing the length of the next CPU burst. For batch systems, the user might specify the job length, but for interactive systems, this is impossible to know for sure. The OS can only try to _predict_ the next burst time, typically based on the process's previous burst times (e.g., using an exponential average).

**Links:** [[CPU Scheduling]], [[First-Come, First-Served (FCFS) Scheduling]]