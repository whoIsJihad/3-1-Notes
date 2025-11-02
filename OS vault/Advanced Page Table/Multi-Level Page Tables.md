# Multi-Level Page Tables

**Tags:** #os #memory-management #paging #page-directory

The most common solution to the large page table problem is the **multi-level page table**. The core idea is simple but powerful: **if the page table is too big, page the page table itself.**

Instead of a single linear array, the page table is broken into a tree-like structure. In a two-level scheme, the top-level structure is called the **Page Directory**.

- **Page Directory**: An array of **Page Directory Entries (PDEs)**. Each PDE points to a page-sized chunk of the full page table (a **page table page**).
    
- **Page Table Page**: An array of standard **Page Table Entries (PTEs)**. Each PTE points to a physical frame of user data.
    

The OS only allocates a page table page if at least one page within the corresponding virtual address range is in use. Otherwise, the PDE for that range is marked as invalid. This elegantly solves the problem of sparse address spaces.

### Two-Level Address Translation

The virtual address is now split into three parts:

1. **Page Directory Index (PDX)**: The top bits, used as an index into the page directory.
    
2. **Page Table Index (PTX)**: The middle bits, used as an index into the page table page.
    
3. **Offset**: The lowest bits, the offset within the data page.
    

The translation process on a [[The Translation Lookaside Buffer (TLB)|TLB]] miss involves two memory accesses before the final data access:

1. Use the PDX to find the correct PDE in the page directory. The address of the page directory is found via the Page Table Base Register (PTBR).
    
2. The PDE contains the Physical Frame Number (PFN) of the relevant **page table page**.
    
3. Use the PTX to find the correct PTE within that page table page.
    
4. The PTE contains the PFN of the **data page**.
    
5. Combine this PFN with the offset to get the final physical address.
    

```
// Pseudocode for a two-level page table lookup (on TLB miss)

// Get the Page Directory base from the PTBR
PD_Base = PTBR;

// 1. First lookup: Get the Page Directory Entry (PDE)
PDIndex = (VirtualAddress & PD_MASK) >> PD_SHIFT;
PDEAddr = PD_Base + (PDIndex * sizeof(PDE));
PDE = AccessMemory(PDEAddr);

if (PDE.Valid == FALSE) {
    RaiseException(SEGMENTATION_FAULT); // Page table page not allocated
}

// 2. Second lookup: Get the Page Table Entry (PTE)
PT_Base = PDE.PFN << SHIFT; // Base address of the page table page
PTIndex = (VirtualAddress & PT_MASK) >> PT_SHIFT;
PTEAddr = PT_Base + (PTIndex * sizeof(PTE));
PTE = AccessMemory(PTEAddr);

if (PTE.Valid == FALSE) {
    RaiseException(SEGMENTATION_FAULT); // Data page not allocated
}

// ... continue with protection checks, TLB insertion, and retrying the instruction
```

### Time-Space Trade-off

- **Space**: Multi-level tables are highly space-efficient for sparse address spaces, as they only allocate the parts of the page table tree that are actively in use.
    
- **Time**: The cost of this space efficiency is performance. A TLB miss is now more expensive, requiring two memory lookups instead of one. On a three- or four-level page table (common in 64-bit systems), a single TLB miss can require three or four sequential memory lookups, making a high TLB hit rate absolutely critical.