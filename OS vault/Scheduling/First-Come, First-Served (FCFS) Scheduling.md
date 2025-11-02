# First-Come, First-Served (FCFS) Scheduling

**Tags:** #os #scheduling #algorithms #fcfs

**First-Come, First-Served (FCFS)** is the simplest CPU scheduling algorithm. As its name implies, the process that requests the CPU first is allocated the CPU first. The implementation is easily managed with a simple FIFO (First-In, First-Out) queue.

- **Type:** [[Preemptive vs Non-preemptive Scheduling|Non-preemptive]]
    
- **Characteristic:** Once a process gets the CPU, it runs to completion or until it blocks.
    

### Example

Consider the following processes arriving at time 0:

|Process|Burst Time|
|---|---|
|P1|24|
|P2|3|
|P3|3|

If they arrive in the order P1, P2, P3, the Gantt chart would be:

```
       P1         P2    P3
|------------------|-----|-----|
0                 24    27    30
```

**Calculation of Waiting Times:**

- P1 waits for 0 ms.
    
- P2 waits for 24 ms.
    
- P3 waits for 27 ms.
    

```
Average Waiting Time = (0 + 24 + 27) / 3 = 17 ms
```

### The Convoy Effect

FCFS suffers from a major problem known as the **convoy effect**. If a long process (like P1) arrives before several short processes, the short processes get stuck waiting for the long one to finish.

What if the processes arrived in the order P2, P3, P1?

Gantt Chart:

```
   P2    P3         P1
|-----|-----|------------------|
0     3     6                 30
```

**Calculation of Waiting Times:**

- P2 waits for 0 ms.
    
- P3 waits for 3 ms.
    
- P1 waits for 6 ms.
    

```
Average Waiting Time = (0 + 3 + 6) / 3 = 3 ms
```

The average waiting time is much better in this case. The performance of FCFS is highly sensitive to the arrival order of processes, making it unsuitable for time-sharing systems.

**Links:** [[CPU Scheduling]], [[Shortest Job First (SJF) Scheduling]]