
**Tags:** #os #cse #scheduling #algorithms #summary

CPU Scheduling is one of the most fundamental functions of an operating system, dictating the order and duration for which processes get access to the CPU. In any multiprogramming system where multiple processes compete for the CPU, the scheduler's efficiency is paramount. It directly impacts system performance, resource utilization, and the user's perception of responsiveness. This summary integrates the core concepts of scheduling, from when it happens to how different algorithms prioritize and execute processes.

## 1. The Dichotomy of Process Behavior: CPU vs. I/O Bound

To understand scheduling, we must first understand the behavior of the processes being scheduled. Processes are not monolithic; their execution consists of alternating cycles of CPU computation and I/O waiting. The duration of these CPU cycles, or "bursts," leads to a fundamental classification:

- **I/O-Bound Process:** A process that spends most of its time waiting for I/O operations to complete. It is characterized by many **short CPU bursts**. Examples include text editors, web browsers, and database servers, which perform a small amount of processing before waiting for user input or disk access.
    
- **CPU-Bound Process:** A process that spends most of its time performing intensive computations. It is characterized by **long, uninterrupted CPU bursts** and infrequent I/O waits. Examples include scientific simulations, video rendering, and code compilation.
    

A key goal of a scheduler is to manage a mix of these two process types effectively. If a scheduler only runs CPU-bound processes, the I/O devices will sit idle. If it only runs I/O-bound processes, the CPU will be underutilized. The ideal is to overlap the I/O waits of some processes with the CPU execution of others.

## 2. The Core Problem and the Dispatcher

The basic scheduling loop involves moving a process from the `Ready` state to the `Running` state.

- The **Scheduler** is the OS module that selects which process in the ready queue should run next. It is the decision-making policy.
    
- The **Dispatcher** is the module that gives control of the CPU to the process selected by the scheduler. This involves:
    
    - Performing the [[Context Switching|context switch]].
        
    - Switching from kernel mode to user mode.
        
    - Jumping to the proper location in the user program to restart its execution.
        

The time taken by the dispatcher to stop one process and start another is called **dispatch latency**, which is a form of system overhead.

## 3. When Does Scheduling Occur?

A scheduling decision must be made when a process changes state:

1. **Running -> Waiting:** The process blocks on I/O.
    
2. **Running -> Ready:** A timer interrupt occurs (preemption).
    
3. **Waiting -> Ready:** An I/O operation completes.
    
4. **Running -> Terminated:** The process finishes.
    

## 4. Preemptive vs. Non-Preemptive Scheduling

- **Non-Preemptive (Cooperative):** Once a process is given the CPU, it keeps it until it voluntarily releases it. Simple, but a long process can freeze the system.
    
- **Preemptive:** The OS can forcibly take the CPU away from a process. Essential for modern interactive systems.
    

## 5. Scheduling Performance Metrics

- **CPU Utilization:** Percentage of time the CPU is busy.
    
- **Throughput:** Processes completed per unit of time.
    
- **Turnaround Time:** `Completion Time - Arrival Time`.
    
- **Waiting Time:** `Turnaround Time - Burst Time`. Time spent in the ready queue.
    
- **Response Time:** Time from request to first response.
    

## 6. Scheduling Algorithms in Detail

### First-Come, First-Served (FCFS)

The simplest algorithm. Processes are served in the order they arrive.

- **Type:** Non-preemptive.
    
- **Problem: The Convoy Effect.** This is a major drawback of FCFS where the entire system's performance is degraded by one long process. If a long **CPU-bound process** arrives just before several short **I/O-bound processes**, the I/O-bound processes are forced to wait in the ready queue. While the CPU-bound process runs, the I/O devices become idle. When the long process finally finishes, the I/O-bound processes execute their short CPU bursts and move to the I/O queues, leaving the CPU idle. This phenomenon, where short processes get stuck behind a long one, is the convoy effect. It leads to poor utilization of both CPU and I/O devices and a high average waiting time.
    

### Shortest Job First (SJF)

Selects the process with the shortest next CPU burst. Provably optimal for minimizing average waiting time.

- **Non-Preemptive SJF:** When a process starts, it runs until its entire CPU burst is complete.
    
- **Preemptive SJF (Shortest Remaining Time First - SRTF):** If a new process arrives with a burst time shorter than the _remaining_ time of the current process, the current process is preempted.
    
- **Problem: Predicting the Future.** The major challenge is that the OS cannot know the length of the next CPU burst. The common solution is to predict it using an **exponential average** of the process's previous burst times.
    

### Priority Scheduling

Each process has a priority; the highest-priority process runs.

- **Problem: Starvation.** Low-priority processes may never get to run.
    
- **Solution: Aging.** Gradually increase the priority of processes that wait for a long time.
    

### Round Robin (RR)

The quintessential algorithm for time-sharing systems. It is preemptive FCFS.

- **Mechanism:** A fixed time slice, or **quantum**, is defined. Each process gets to run for up to one quantum. If it's still running at the end of the quantum, it is preempted and moved to the back of the ready queue.
    
- **Performance:** The effectiveness of RR is critically dependent on the **quantum size**:
    
    - **Too Large:** The algorithm degenerates into FCFS.
        
    - **Too Small:** Context switch overhead becomes a significant portion of the CPU time, drastically reducing efficiency.
        

**Example Gantt Chart for RR (Quantum = 4ms):** | Process | Burst Time | | :--- | :--- | | P1 | 10 | | P2 | 5 | | P3 | 8 |

```
   P1    P2    P3    P1    P2   P3    P1    P3
|-----|-----|-----|-----|----|-----|-----|-----|
0     4     8     12    16   17    21    23    25
```

This algorithm provides excellent response time and fairness, making it the standard for most interactive desktop and server operating systems.