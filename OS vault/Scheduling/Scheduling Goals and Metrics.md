# Scheduling Goals and Metrics

**Tags:** #os #scheduling #performance #metrics

To compare different CPU scheduling algorithms, we need objective criteria to measure their performance. These metrics reflect how well the scheduler is meeting its goals, which can sometimes be conflicting (e.g., maximizing throughput vs. minimizing response time).

### Key Performance Metrics

- **CPU Utilization:** The percentage of time that the CPU is busy doing useful work (i.e., not idle). The goal is to keep the CPU as busy as possible, typically aiming for 90-100%.
    
- **Throughput:** The number of processes completed per unit of time. Higher throughput means more work is getting done.
    
- **Turnaround Time:** The total time a process spends in the system, from its arrival to its completion. It is the sum of the time spent waiting in the ready queue, executing on the CPU, and doing I/O.
    
    ```
    Turnaround Time = Completion Time - Arrival Time
    ```
    
- **Waiting Time:** The total time a process spends waiting in the ready queue. It does not include the time spent executing or doing I/O. The goal is to minimize the waiting time for all processes.
    
    ```
    Waiting Time = Turnaround Time - Burst Time
    ```
    
- **Response Time:** In an interactive system, this is the time from when a request is submitted until the first response is produced (not the completion of the entire task). A low response time is critical for a good user experience.
    

### Scheduling Goals

The general goals of a scheduling algorithm are:

- **Maximize** CPU utilization.
    
- **Maximize** throughput.
    
- **Minimize** turnaround time.
    
- **Minimize** waiting time.
    
- **Minimize** response time.
    

Often, we analyze the **average** of these times (e.g., average waiting time) across all processes to evaluate an algorithm's overall performance for a given workload.

**Links:** [[CPU Scheduling]]