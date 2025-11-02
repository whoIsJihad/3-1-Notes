# Process State Model

**Tags:** #os #process #state-model #lifecycle

As a process executes, its state changes. The operating system tracks the state of each process, which is a fundamental part of scheduling and resource management. The five-state model is a common representation of a process's lifecycle.

### The Five States

1. **New:** The process is in the process of being created. The OS has allocated a [[Process Control Block (PCB)]] but has not yet loaded the program into memory or fully initialized its resources.
    
2. **Ready:** The process is loaded into memory and is waiting for its turn to be executed by the CPU. It has everything it needs to run, but the OS scheduler has not yet selected it. There is often a queue of ready processes.
    
3. **Running:** The process's instructions are actively being executed by the CPU. A process in this state holds the CPU. On a single-core system, only one process can be in the `running` state at any given moment.
    
4. **Waiting (or Blocked):** The process is unable to continue execution because it is waiting for some event to occur. Common events include waiting for an I/O operation to complete (e.g., reading from a disk), waiting for a network packet, or waiting for a lock to be released.
    
5. **Terminated:** The process has finished its execution, either normally or due to an error. The OS is in the process of cleaning up its resources and deallocating its memory and PCB.
    

### State Transitions

- **New -> Ready:** The OS has finished setting up the process and admits it to the pool of runnable processes.
    
- **Ready -> Running:** The OS scheduler dispatches the process, giving it control of the CPU.
    
- **Running -> Ready:** The process's time slice expires in a preemptive multitasking system, or it is interrupted.
    
- **Running -> Waiting:** The process initiates an I/O request or waits for an event and must block until it completes.
    
- **Waiting -> Ready:** The event the process was waiting for has occurred (e.g., the I/O operation is complete). The process can now compete for CPU time again.
    
- **Running -> Terminated:** The process completes its execution or is killed by the OS.
    

**Links:** [[Process Control Block (PCB)]], [[Process Creation and Termination]]