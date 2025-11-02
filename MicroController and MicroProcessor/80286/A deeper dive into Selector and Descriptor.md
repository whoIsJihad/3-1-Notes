# Selectors and Descriptor Tables: A Deep Dive

**Tags:** #80286 #protected_mode #memory_management #simulation

In Protected Mode, the CPU stops thinking about memory in terms of the simple `Segment:Offset` addresses used by the 8086. It adopts a more powerful, indirect system to support memory protection and multitasking. The new logical address format is **`Selector:Offset`**. Understanding how the CPU translates this into a physical memory location is the key to understanding all modern operating systems.

The segment registers (`CS`, `DS`, `SS`, `ES`) no longer hold a physical base address. Instead, they hold a 16-bit value called a **Selector**.

### What is a Selector? The "Table of Contents" Entry

A Selector is not an address; it's an **index** or a "pointer" to an entry in a special "table of contents" for memory. This table of contents is called a **Descriptor Table**. The selector tells the CPU exactly where to look in this table to find the _real_ information about a memory segment.

Let's dissect a 16-bit selector:

|Bits 15-3 (13 bits)|Bit 2 (1 bit)|Bits 1-0 (2 bits)|
|---|---|---|
|**Index**|**TI (Table Indicator)**|**RPL (Requested Privilege Level)**|
|Specifies which entry to use (0-8191).|`0` = Global Table (GDT) `1` = Local Table (LDT)|The privilege level the code is _requesting_ for this access (`00`=highest, `11`=lowest).|

### What are Descriptor Tables? The "Map of Memory"

A Descriptor Table is a data structure created and managed by the operating system, but read and enforced by the CPU hardware. It's the master map that defines every segment of memory the system can use. Each entry in this table is an 8-byte structure called a **Descriptor**.

There are two types of tables:

1. **Global Descriptor Table (GDT):** There is only **one** GDT for the whole system. It defines "global" segments that any program might need access to, like the OS kernel's code and data, or video memory. The CPU knows where to find the GDT because its physical base address and size are loaded into a special register, the **`GDTR`**, during boot-up.
    
2. **Local Descriptor Table (LDT):** Each program (or "task") can have its own **private** LDT. This table defines segments that are exclusive to that program—its own code, data, and stack. This is how the OS isolates programs from each other. The CPU knows where to find the _current task's_ LDT because it's pointed to by another special register, the **`LDTR`**.
    

### Simulation: From `MOV AX, [SI]` to Physical Address

Let's simulate the entire address translation process. This is what the CPU's Address Unit (MMU) does automatically in hardware.

**Scenario:**

- Our program needs to execute the instruction `MOV AX, [SI]`.
    
- The `DS` register holds the selector `0008h`.
    
- The `SI` register holds the offset `1000h`.
    
- The `GDTR` points to the GDT, which is located at physical address `000100h`.
    

#### Step 1: Decode the Selector

The CPU first looks at the `DS` register, which contains the selector `0008h`. It breaks this 16-bit value down according to the format.

**Selector `0008h` in Binary:** `0000 0000 0000 1000`

|Binary Value|Field|Interpretation|
|---|---|---|
|`0000 0000 0000 1`|**Index** (13 bits)|The CPU needs to look at **entry #1** in the table. (The last 3 bits are masked off, so `1000` becomes `001`).|
|`0`|**TI (Table Indicator)**|The `TI` bit is `0`, so the CPU will use the **Global Descriptor Table (GDT)**.|
|`00`|**RPL (Requested Privilege)**|The code is requesting access at privilege level `00` (the highest level).|

**Conclusion of Step 1:** The CPU now knows it must find **entry #1** in the **GDT**.

#### Step 2: Locate the Descriptor in Memory

The CPU needs to find where this descriptor is physically located in RAM.

|Register/Value|Description|Calculation|
|---|---|---|
|`GDTR`|Contains GDT Base Address|`000100h`|
|Selector Index|From Step 1|`1`|
|Size of a Descriptor|Fixed hardware value|`8` bytes|

**Calculation:**

```
Descriptor_Address = GDT_Base_Address + (Index * 8)
Descriptor_Address = 000100h + (1 * 8)
Descriptor_Address = 000108h
```

**Conclusion of Step 2:** The CPU now knows that the 8-byte descriptor it needs to read starts at physical memory address `000108h`.

#### Step 3: Fetch and Parse the Descriptor

The CPU performs a memory read from `000108h` to fetch the 8-byte descriptor. Let's assume the descriptor contains the following data (this is set up by the OS):

- **Base Address:** `00400000h`
    
- **Limit:** `FFFFh` (a full 64 KB segment)
    
- **Access Rights:** Allows read/write access at privilege level `00`.
    

The CPU extracts this information and stores it in the invisible cache of the `DS` register.

#### Step 4: Security and Bounds Checking

Before proceeding, the hardware performs critical checks:

1. **Privilege Check:** Is the program's Current Privilege Level (CPL) allowed to access this segment based on the Descriptor Privilege Level (DPL)? (Let's assume yes).
    
2. **Limit Check:** Is the requested offset within the segment's bounds?
    
    - Offset (`SI`) = `1000h`
        
    - Segment Limit = `FFFFh`
        
    - Is `1000h <= FFFFh`? **Yes**. The access is valid. If `SI` had been `10000h`, the CPU would trigger a protection fault right here.
        

#### Step 5: Calculate the Final Physical Address

Now that all checks have passed, the CPU can finally calculate the target physical address.

**Calculation:**

```
Physical_Address = Base_Address_from_Descriptor + Offset
Physical_Address = 00400000h + 1000h
Physical_Address = 00401000h
```