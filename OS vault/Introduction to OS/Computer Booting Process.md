# Computer Booting Process

**Tags:** #os #booting #bios #rom #post

**Booting** is the process of starting a computer, which involves loading the core of the Operating System into memory (RAM). Since the OS itself manages loading other programs, it must be started first by a special sequence.

### The Boot Sequence

1. **Power On & BIOS Execution:** When power is supplied, the CPU begins executing a startup program stored in a non-volatile ROM chip on the motherboard. This is the **BIOS** (Basic Input/Output System).
    
2. **POST (Power-On Self-Test):** The BIOS runs initial diagnostics to ensure essential hardware (like RAM and keyboard) is present and functional.
    
3. **Locate Boot Device:** The BIOS checks the **CMOS memory** (a battery-backed chip) for the user-defined boot device order (e.g., Hard Drive, USB, etc.).
    
4. **Load Boot Loader:** The BIOS reads the first sector (the Master Boot Record or MBR) from the selected boot device into memory and transfers execution to it.
    
5. **Load the OS:** The MBR contains a small program called a **boot loader**. This program's job is to find the active partition on the disk and load the main OS from that partition into RAM.
    
6. **OS Initialization:** Once in memory, the OS takes control, initializes its own drivers and subsystems, and starts the necessary background processes before finally loading the user interface.
    

**Links:** [[OS Kernel]], [[Introduction to Operating Systems (index)]], [[A Deep Dive into the Computer Booting ProcessUntitled]]