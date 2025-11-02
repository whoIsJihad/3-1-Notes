# The Page Fault: Mechanism and Handling

**Tags:** #os #memory-management #virtual-memory #swapping #page-fault #hardware #trap

A **page fault** is not necessarily an error; it is a trap to the operating system, triggered by the hardware, when a process tries to access a page that is not currently present in physical memory. It is the fundamental mechanism that enables demand paging and swapping.

### The Present Bit

To support swapping, a new piece of metadata is used in the Page Table Entry (PTE): the **present bit**.

- **Present = 1**: The page is in a physical frame, and the Physical Frame Number (PFN) in the PTE is valid. The translation can proceed as normal.
    
- **Present = 0**: The page is _not_ in physical memory. It is currently located on disk in the swap space. The rest of the PTE can be repurposed by the OS to store the disk address of the page.
    

### The Hardware's Role: Detecting the Fault

The address translation process, including the [[The Translation Lookaside Buffer (TLB)|TLB lookup]], is modified to check this bit.

1. A memory access begins (e.g., `movl 0x1234, %eax`).
    
2. The hardware checks the TLB for a valid translation.
    
    - **TLB Hit**: If a hit occurs, the present bit must have been 1, so the translation completes instantly.
        
    - **TLB Miss**: The hardware proceeds to walk the page table.
        
3. The hardware fetches the correct PTE from memory.
    
4. It now checks the control bits in the PTE. If the **present bit is 0**, the hardware stops the translation process, saves the faulting virtual address and the type of fault in special registers, and raises a **page fault**, trapping into the OS kernel.
    

```
// Pseudocode showing the final step of a TLB miss with the Present Bit check

// ... after fetching the PTE from the page table ...
PTE = AccessMemory(PTEAddr);

if (PTE.Valid == False) {
    RaiseException(SEGMENTATION_FAULT);
} else if (CanAccess(PTE.ProtectBits) == False) {
    RaiseException(PROTECTION_FAULT);
} else if (PTE.Present == True) {
    // Page is valid and in memory.
    // Load translation into TLB and retry the instruction.
    TLB_Insert(VPN, PTE.PFN, PTE.ProtectBits);
    RetryInstruction();
} else if (PTE.Present == False) {
    // Page is valid but NOT in memory.
    // This is the page fault.
    RaiseException(PAGE_FAULT);
}
```

### The OS's Role: The Page Fault Handler

When the OS gets control via the page fault trap, it executes a special routine called the **page fault handler**. Its job is to resolve the fault and make it seem as if the memory was there all along.

The sequence of events is as follows:

1. **Find Page on Disk**: The OS uses the faulting virtual address to locate the corresponding PTE and finds the disk address of the required page from the PTE's repurposed bits.
    
2. **Find a Free Physical Frame**: The OS checks its free list for an available page frame.
    
    - **If a frame is free**: It proceeds to the next step.
        
    - **If no frame is free**: This triggers a **page replacement** decision. The OS must run a page replacement algorithm (e.g., LRU) to select a "victim" page to evict.
        
3. **Swap Out Victim (if necessary)**: If a victim page was chosen, the OS checks its "dirty bit."
    
    - If the victim is dirty (was modified), it must be **written back** to its location in the swap space. This is a slow disk I/O operation.
        
    - If the victim is clean, it can simply be overwritten.
        
4. **Swap In Required Page**: The OS issues a disk I/O request to **read the required page** from its location in the swap space into the newly freed physical frame. This is another slow disk I/O operation. The process is put into the blocked state while this occurs.
    
5. **Update Page Table**: Once the page is loaded into memory, the OS updates the faulting process's page table. It sets the PTE for the new page with the correct PFN, sets the protection bits, and sets the **present bit to 1**.
    
6. **Retry Instruction**: The OS returns from the trap, which causes the original instruction that caused the fault to be restarted. This time, the hardware will find that the page is present, the translation will succeed (likely after a TLB miss that now populates the TLB), and the program continues its execution, completely unaware that a fault ever occurred.