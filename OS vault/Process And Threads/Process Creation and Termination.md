# Process Creation and Termination

**Tags:** #os #process #lifecycle #fork

Processes are created and destroyed dynamically throughout the uptime of a system. The operating system provides mechanisms to handle these events.

### Process Creation

A new process can be created for several reasons:

1. **System Initialization:** When the OS boots, it creates several system processes (daemons or services) that run in the background to manage the system.
    
2. **System Call by a Running Process:** An existing process can execute a process creation system call. In UNIX-like systems, this is the `fork()` call, which creates a nearly identical copy of the parent process. This is the most common way new processes are created.
    
3. **User Request:** A user can explicitly request to create a new process by typing a command in a shell or double-clicking an icon in a graphical user interface.
    
4. **Initiation of a Batch Job:** In batch processing systems, the OS can create a new process to execute the next job from a queue.
    

### Process Termination

A process terminates when it finishes executing its final statement, but it can also be terminated for other reasons, which fall into two categories:

1. **Voluntary Termination:**
    
    - **Normal Exit:** The process has completed its task successfully and calls an `exit` system call.
        
    - **Error Exit:** The process detects a fatal error (e.g., file not found, invalid input) and voluntarily terminates.
        
2. **Involuntary Termination:**
    
    - **Fatal Error:** The process attempts an illegal operation that the OS detects, such as dividing by zero, accessing unauthorized memory, or executing a privileged instruction. The kernel terminates the process.
        
    - **Killed by Another Process:** A process with the necessary permissions can issue a system call to terminate another process (e.g., using the `kill` command in Linux or ending a task in the Task Manager).
        

When a process is terminated, the OS reclaims all of its resources, including memory, open files, and its [[Process Control Block (PCB)]].

**Links:** [[Process State Model]], [[The fork() System Call]]