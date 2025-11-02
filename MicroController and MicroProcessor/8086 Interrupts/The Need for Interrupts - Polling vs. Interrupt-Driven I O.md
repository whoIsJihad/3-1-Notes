
**Tags:** #interrupts #polling #io_management #cpu_efficiency

A CPU needs a way to communicate with external I/O devices like keyboards, mice, and network cards. There are two fundamental approaches to managing this communication: Polling and Interrupts.

### Method 1: Polling (Programmed I/O)

In a polling-based system, the CPU is in charge of initiating all communication. It actively and continuously checks the status of each device to see if it needs service.

**Analogy:** Imagine you're expecting a package, but you don't have a doorbell. The only way to know if the delivery person has arrived is to repeatedly open the door and check.

**How it Works in a Computer:** The CPU runs a loop that looks something like this:

1. Ask Device 1: "Do you have any data for me?"
    
2. Ask Device 2: "Do you have any data for me?"
    
3. ...
    
4. Ask Device N: "Do you have any data for me?"
    
5. Repeat.
    

**Disadvantages of Polling:**

- **Extremely Inefficient:** The CPU spends the vast majority of its time asking devices if they are ready. This is wasted processing time that could have been used to run other programs.
    
- **Poor Responsiveness:** The time it takes to notice a device needs service (latency) depends on how many other devices are in the polling loop. A device might have to wait a long time before the CPU gets around to checking on it.
    

Polling is simple to implement but is only suitable for very basic systems with few devices or where timing is not critical.

### Method 2: Interrupt-Driven I/O

In an interrupt-driven system, the roles are reversed. The CPU ignores the I/O devices until a device itself signals that it needs attention.

**Analogy:** You're expecting a package and you have a doorbell. You can go about your day without checking the door. When the delivery person arrives, they ring the bell, "interrupting" you. You then stop what you're doing, answer the door, and resume your day.

**How it Works in a Computer:**

1. The CPU focuses on executing the main program.
    
2. When an I/O device (like a keyboard) has data ready (a key has been pressed), it sends an electrical signal to the CPU's interrupt pin (`INTR` or `NMI`).
    
3. The CPU automatically finishes its current instruction, saves its context, and jumps to a specific piece of code (the Interrupt Service Routine) to handle that device.
    
4. After handling the device, the CPU restores its context and resumes the main program.
    

**Advantages of Interrupts:**

- **Highly Efficient:** The CPU wastes zero time checking on devices that don't need service. It can use 100% of its processing power on the main task until an event occurs.
    
- **Excellent Responsiveness:** The CPU's attention is captured the moment an event happens, leading to very low latency.
    

Interrupts are the cornerstone of modern multitasking operating systems, allowing the CPU to efficiently manage numerous devices and tasks concurrently.

**Links:** [[8086 Interrupts and System Control (Index)]]