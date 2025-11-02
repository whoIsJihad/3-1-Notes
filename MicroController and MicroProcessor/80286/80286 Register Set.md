# 80286 Register Set

**Tags:** #80286 #registers #protected_mode

The 80286 register set is an extension of the 8086's. It includes all the familiar 8086 registers for backward compatibility but adds new registers and flags to manage the new Protected Mode capabilities.

### Base Register Set (Identical to 8086)

- **General Purpose Registers:** `AX`, `BX`, `CX`, `DX`
    
- **Pointer Registers:** `SP`, `BP`
    
- **Index Registers:** `SI`, `DI`
    
- **Segment Registers:** `CS`, `DS`, `SS`, `ES` (These have a new function in Protected Mode)
    
- **Instruction Pointer:** `IP`
    

### New and Modified Registers

#### 1. FLAGS Register

The 80286 `FLAGS` register adds two new fields critical for protected mode.

- **`IOPL` (I/O Privilege Level - bits 12-13):**
    
    - **Purpose:** Defines the minimum privilege level required to execute I/O instructions (like `IN` and `OUT`). This prevents user-level applications from directly accessing hardware, a key OS protection feature.
        
    - **Levels:** `00` is the highest privilege (kernel level), `11` is the lowest (user level). If a program's current privilege level is less privileged than the `IOPL`, an attempt to perform I/O will trigger a protection fault.
        
- **`NT` (Nested Task - bit 14):**
    
    - **Purpose:** Used by the OS to manage chained or "nested" task calls. It indicates that the current task was initiated by a `CALL` instruction from another task, rather than a `JMP`. This helps the OS correctly return control when tasks complete.
        

#### 2. Machine Status Word (MSW) Register

The MSW is a new 16-bit register that controls the fundamental state of the CPU, particularly the switch into protected mode.

- **`PE` (Protection Enable - bit 0):**
    
    - **The Big Switch:** Setting this bit switches the processor from Real Mode to **Protected Mode**.
        
    - **One-Way Trip:** This bit can only be cleared by resetting the entire CPU. This was a significant design flaw, as switching back to Real Mode required a full hardware reset.
        
- **`TS` (Task Switched - bit 3):**
    
    - **Purpose:** The CPU sets this bit automatically every time it performs a task switch. It's used to manage the state of a math coprocessor (like the 80287), preventing a new task from accidentally using results left over from the previous task.
        

The other bits (`MP`, `EM`) are also related to managing the math coprocessor. New instructions, `LMSW` (Load MSW) and `SMSW` (Store MSW), were added to manipulate this register.

**Links:** [[The Intel 80286(index)]]