# The Descriptor Cache (Program-Invisible Registers)

**Tags:** #80286 #protected_mode #cpu_cache #performance

A major potential drawback of Protected Mode is the performance overhead. Every time a memory access occurs, the CPU has to read the descriptor table from main memory before it can even begin to access the target data. This would effectively double the time for every memory operation, crippling performance.

`Memory Access = Read Descriptor from RAM + Read Data from RAM`

To solve this problem, the 80286 architects introduced **program-invisible registers**, also known as the **descriptor cache**.

### The Caching Mechanism

Each of the segment registers (`CS`, `DS`, `SS`, `ES`) has a hidden, 6-byte "cache" portion attached to it. This cache is "program-invisible" because you cannot access it directly with any instruction; the CPU manages it automatically.

**How it Works:**

1. **Loading a Selector:** When you execute an instruction like `MOV DS, AX`, you are loading a new **selector** into the visible part of the `DS` register.
    
2. **Automatic Cache Fill:** The moment the selector is loaded, the CPU's hardware triggers a memory read cycle. It uses the new selector to find the corresponding 8-byte descriptor in the GDT or LDT. It then automatically copies the key information—the 24-bit Base Address, the 16-bit Limit, and the 8-bit Access Rights—into the 6-byte invisible cache portion of the `DS` register.
    
3. **Subsequent Accesses:** Now, for every subsequent instruction that uses `DS` for a memory access (e.g., `MOV BX, [SI]`), the CPU **does not need to go back to the descriptor table in RAM**. It already has all the necessary information (Base, Limit, Access Rights) stored right next to the segment register in its high-speed internal cache.
    

### Performance Impact

This caching mechanism is a critical optimization. It means the performance penalty of reading a descriptor is paid **only once**—when the segment register is initially loaded. All subsequent accesses to that segment run at full speed, as the MMU can get the base address and perform limit checks using the internal cache registers.

The process remains "protected" because the limit and access rights are also cached, so every access is still fully validated by the hardware.

This design principle—caching frequently accessed data to avoid slow memory lookups—is the same concept behind modern L1/L2/L3 CPU caches, but applied here specifically to the memory management unit.

**Links:** [[The Intel 80286 - Bridge to Modern Computing]]