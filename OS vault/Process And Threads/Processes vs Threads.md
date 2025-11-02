# Processes vs Threads

**Tags:** #os #process #threads #comparison

Both processes and threads are fundamental units of execution, but they represent different levels of abstraction and have significant differences in how they are managed by the OS.

|Feature|Process|Thread|
|---|---|---|
|**Weight**|**Heavyweight**. Creation and context switching are slow.|**Lightweight**. Creation and context switching are fast.|
|**Address Space**|Each process has its own separate, private address space.|All threads within a process **share** the same address space.|
|**Resource Sharing**|Processes do not share memory by default. Communication requires explicit Inter-Process Communication (IPC) mechanisms provided by the OS (e.g., pipes, shared memory).|Threads share memory and resources (code, data, files) by default. Communication is simple via shared variables.|
|**Independence**|Processes are independent of each other. A crash in one process does not affect other processes.|Threads are not independent. A crash in one thread can crash the entire process and all of its other threads.|
|**Scheduling**|The OS schedules processes.|The OS schedules threads. Threads are the fundamental unit of scheduling.|
|**Container**|A process is a container for resources and at least one thread.|A thread is a path of execution within a process.|

### When to Use Which?

- **Use Multiple Processes** when you need to run separate, isolated tasks that should not interfere with each other. Security and robustness are key concerns. Web browsers often use separate processes for each tab to prevent a crash in one tab from bringing down the whole browser.
    
- **Use Multiple Threads** when you need to perform multiple related tasks concurrently within a single application that require access to the same data. Performance and efficient communication are the main goals. A word processor might use one thread for user input, another for spell checking, and a third for auto-saving.
    

**Links:** [[Introduction to Threads]], [[Multithreading Model]]