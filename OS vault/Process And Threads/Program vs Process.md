# Program vs Process

**Tags:** #os #process #program #definition

While often used interchangeably in casual conversation, a "program" and a "process" are two distinct concepts in operating systems. Understanding the difference is key to understanding how an OS manages execution.

### Program

A **program** is a passive, static entity. It is an executable file stored on a disk (e.g., `/bin/ls` or `firefox.exe`). This file contains a set of machine code instructions and static data required to perform a task. It is simply a collection of bytes with a defined structure.

- **State:** Passive
    
- **Location:** Disk

    

### Process

A **process** is an active, dynamic entity. It is an _instance_ of a program that is currently being executed. When you double-click an icon or run a command in the terminal, the OS loads the program from the disk into memory and creates a process.

- **State:** Active
    
- **Location:** Memory (RAM)
    


You can have a single program (e.g., `firefox.exe`) correspond to multiple, separate processes if you open several instances of the application. Each process has its own independent state.

**Links:** [[Processes and Threads (index)]], [[Process Address Space]]