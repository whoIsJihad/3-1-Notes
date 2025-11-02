# The System Bus

**Tags:** #bus #address_bus #data_bus #control_bus #computer_architecture

The system bus is the shared communication highway that connects the major components of a computer (CPU, memory, I/O devices). It's not a single bus, but a collection of three separate buses, each with a specific purpose.

### 1. Address Bus

- **Purpose:** The address bus is used by the CPU to specify a memory location or an I/O port that it wants to interact with.
    
- **Direction:** It is **unidirectional** (one-way). The address always travels _from_ the CPU _to_ the memory or I/O controllers.
    
- **Width:** The width (number of parallel wires) of the address bus determines the maximum amount of memory the CPU can address. An n-bit address bus can address `2^n` unique memory locations.
    
    ```
    // Example: A 20-bit address bus can address 2^20 locations (1 MB).
    // A 32-bit address bus can address 2^32 locations (4 GB).
    // A 64-bit address bus can address 2^64 locations (16 Exabytes).
    ```
    

### 2. Data Bus

- **Purpose:** The data bus is used to transfer the actual data between the CPU, memory, and I/O devices.
    
- **Direction:** It is **bidirectional** (two-way). Data can flow from the CPU to memory (a write operation) or from memory to the CPU (a read operation).
    
- **Width:** The width of the data bus determines how much data can be transferred in a single cycle. A 16-bit data bus can transfer 2 bytes at once, while a 64-bit data bus can transfer 8 bytes at once. A wider data bus generally leads to better system performance.
    

### 3. Control Bus

- **Purpose:** The control bus carries command and timing signals from the Control Unit to all other components. It synchronizes the activities on the other two buses.
    
- **Direction:** It is a mix of unidirectional and bidirectional signals.
    
- **Example Signals:**
    
    - **Memory Read/Write:** A signal that tells the memory whether the CPU wants to read from it or write to it.
        
    - **I/O Read/Write:** A signal that specifies an I/O operation instead of a memory operation.
        
    - **Clock Signals:** Used to synchronize data transfers.
        
    - **Interrupt Requests:** Signals from I/O devices to the CPU.
        
    - **Ready:** A signal from a slow device (like memory) to tell the CPU that it has completed its task.
        

Together, these three buses form the backbone of the Von Neumann architecture used in most modern computers.

**Links:** [[Core Components of a Computer System]]