# Process Control Block (PCB)

**Tags:** #os #process #pcb #data-structure

To manage all the running processes, the operating system maintains a data structure for each one called the **Process Control Block (PCB)**, sometimes also referred to as a process descriptor or process table entry. The PCB is a critical kernel data structure that stores all the information the OS needs about a particular process.

When the OS performs a [[Context Switching|context switch]], it saves the state of the current process into its PCB and loads the state of the next process from its PCB.

### Key Fields of a PCB

| Category                                                              | Field                  | Description                                                                      |
| --------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------- |
|                                                                       | Process State          | The current state of the process (e.g., `running`, `ready`, `waiting`).          |
|                                                                       | Process ID (PID)       | A unique identifier for the process.                                             |
|                                                                       | Parent Process ID      | The PID of the process that created this one.                                    |
| **Process Management**                                                | Program Counter (PC)   | The address of the next instruction to be executed.                              |
|                                                                       | CPU Registers          | The current values of the CPU's general-purpose registers, stack pointer, etc.   |
|                                                                       | Scheduling Information | Process priority, pointers to scheduling queues.                                 |
|                                                                       |                        |                                                                                  |
| **Memory Management**                                                 | Pointers to Segments   | Pointers to the text, data, and stack segments in the [[Process Address Space]]. |
|                                                                       |                        |                                                                                  |
|                                                                       | Root Directory         | The process's root directory.                                                    |
| **File Management**                                                   | Working Directory      | The process's current working directory.                                         |
|                                                                       | File Descriptors       | A table of open files for this process.                                          |
|                                                                       |                        |                                                                                  |
| **Identity**                                                          | User ID (UID)          | The user who owns the process.                                                   |
|                                                                       | Group ID (GID)         | The group that owns the process.                                                 |

**Links:** [[Process State Model]], [[Context Switching]]