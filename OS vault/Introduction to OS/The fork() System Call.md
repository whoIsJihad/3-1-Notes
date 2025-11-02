# The fork() System Call

**Tags:** #os #system-calls #process-management #fork

The `fork()` system call is a core function in UNIX-like operating systems used to create a new process.

### How `fork()` Works

1. When a running process (the **parent**) calls `fork()`, the kernel creates a new process (the **child**) which is nearly an exact duplicate of the parent.
    
2. The child process gets its own separate memory space, but it inherits copies of the parent's open file descriptors, registers, and other context.
    
3. Both the parent and the child process continue execution at the instruction immediately following the `fork()` call.
    
4. The only way to differentiate them in the code is by checking the return value of `fork()`:
    
    - In the **parent process**, `fork()` returns the unique Process ID (PID) of the newly created child.
        
    - In the **child process**, `fork()` returns `0`.
        
    - If the fork fails, it returns `-1` in the parent.
        

### Example: How `fork()` creates processes

The following code demonstrates that `fork()` doubles the number of processes. Three calls result in $2^3 = 8$ processes.

```
#include <stdio.h>
#include <unistd.h>

int main() {
    fork(); // 1 process becomes 2
    fork(); // 2 processes become 4
    fork(); // 4 processes become 8
    printf("Hello from a process!\n");
    return 0;
}
```

**Output:** The line "Hello from a process!" will be printed 8 times, as each of the 8 processes will execute the `printf` statement.

**Links:** [[System Calls]], [[Introduction to Operating Systems (index)]]