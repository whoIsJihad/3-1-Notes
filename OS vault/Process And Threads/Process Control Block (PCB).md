# Process Control Block (PCB)

**Tags:** #os #process #pcb #data-structure

To manage all the running processes, the operating system maintains a data structure for each one called the **Process Control Block (PCB)**, sometimes also referred to as a process descriptor or process table entry. The PCB is a critical kernel data structure that stores all the information the OS needs about a particular process.

When the OS performs a [[Context Switching|context switch]], it saves the state of the current process into its PCB and loads the state of the next process from its PCB.

### Key Fields of a PCB
| **Category**           | **Field**                | **Description**                                                                |
| ---------------------- | ------------------------ | ------------------------------------------------------------------------------ |
| **Process Info**       | Process State            | The current state of the process (e.g., `running`, `ready`, `waiting`).        |
|                        | Process ID (PID)         | Unique identifier for the process.                                             |
|                        | Parent Process ID (PPID) | The PID of the process that created this one.                                  |
| **Process Management** | Program Counter (PC)     | Address of the next instruction to execute.                                    |
|                        | CPU Registers            | Current values of CPU general-purpose registers, stack pointer, etc.           |
|                        | Scheduling Information   | Process priority, pointers to scheduling queues, and related data.             |
| **Memory Management**  | Pointers to Segments     | References to text, data, and stack segments in the **Process Address Space**. |
|                        | Root Directory           | The process’s root directory (used for file access isolation).                 |
| **File Management**    | Working Directory        | The process’s current working directory.                                       |
|                        | File Descriptors         | Table of open files associated with this process.                              |
| **Identity**           | User ID (UID)            | Identifier of the user who owns the process.                                   |
|                        | Group ID (GID)           | Identifier of the group that owns the process.                                 |
|                        |                          |                                                                                |
**Links:** [[Process State Model]], [[Context Switching]]