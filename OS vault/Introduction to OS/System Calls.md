# System Calls

**Tags:** #os #system-calls #api #trap

**System Calls** are the programming interface that allows user-level processes to request services from the [[OS Kernel]]. Since user applications run in a restricted mode, they cannot perform privileged operations like accessing hardware directly. System calls are the mandatory gateway for these services.

### The System Call Mechanism

1. **User Program Invokes Call:** A user program calls a standard library function (e.g., `printf()`, `read()`).
    
2. **Library Sets Up and Traps:** The library function sets up the necessary parameters and executes a special `TRAP` instruction.
    
3. **Mode Switch:** The `TRAP` instruction causes a hardware interrupt, which switches the CPU from **User Mode** to **Kernel Mode**. Control is transferred to a specific location in an OS interrupt handler table.
    
4. **Kernel Executes Service:** The OS identifies which system call was requested and executes the corresponding service routine (e.g., writing to the screen buffer, reading from a disk controller).
    
5. **Return and Mode Switch:** After the service is complete, the OS switches the CPU back to **User Mode** and returns control to the user program, which continues its execution right after the library call.
    

### Common System Call Categories

- **Process Control:** `fork()`, `exit()`, `wait()`
    
- **File Management:** `open()`, `read()`, `write()`, `close()`
    
- **Device Management:** `ioctl()`, `read()`, `write()`
    
- **Information Maintenance:** `getpid()`, `alarm()`, `sleep()`
    
- **Communication:** `pipe()`, `shmget()`, `socket()`
    
---

**Links:** [[The fork() System Call]], [[Dual-Mode Operation]] 