# Dual-Mode Operation

**Tags:** #os #cpu-modes #kernel-mode #user-mode #security

To protect the [[OS Kernel]] and system resources from user programs, modern CPUs provide **Dual-Mode Operation**. A hardware **mode bit** is used to distinguish between two modes of execution.

1. **Kernel Mode (Mode Bit = 0)**:
    
    - The CPU can execute the full instruction set and access all hardware.
        
    - The OS kernel runs in this highly privileged mode.
        
    - Also known as: master mode, system mode, privileged mode.
        
    - A crash in kernel mode is catastrophic and will halt the entire system.
        
2. **User Mode (Mode Bit = 1)**:
    
    - The CPU has restricted access and can only execute a subset of instructions.
        
    - User applications (e.g., web browser, text editor) run in this mode.
        
    - Also known as: slave mode, restricted mode, unprivileged mode.
        
    - A crash in user mode only affects that specific application; the OS can typically recover.
        

The transition from user mode to kernel mode occurs when an application needs an OS service, which is requested via a [[System Calls|system call]].

### Comparison Table

|Feature|Kernel Mode|User Mode|
|---|---|---|
|**Privilege**|Full access to hardware and memory.|Restricted access; cannot access hardware directly.|
|**Execution**|The [[OS Kernel]] runs here.|User applications run here.|
|**Mode Bit**|`0`|`1`|
|**Impact of Crash**|Halts the entire computer system.|Terminates the single application; OS remains stable.|
|**Resource Management**|Directly manages system resources.|Must request resources from the OS via system calls.|

**Links:** [[System Calls]], [[OS Kernel]]