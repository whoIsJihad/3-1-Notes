# The Translation Lookaside Buffer (TLB)

**Tags:** #os #memory-management #tlb #hardware #cache #mmu

The fundamental performance problem with [[Paging: Solving Fragmentation with Fixed-Size Units|paging]] is that it requires an extra memory access for every virtual address reference to fetch the translation from the page table. This would effectively halve the speed of memory access, which is unacceptable.

To solve this, modern CPUs include a **Translation Lookaside Buffer (TLB)**. The TLB is a small, hardware-based cache that is part of the Memory Management Unit (MMU). It stores recent, frequently used virtual-to-physical address translations.

### TLB Hit and Miss Logic

For every memory access, the hardware first checks the TLB for a valid translation for the given Virtual Page Number (VPN).

1. **TLB Hit**: If the VPN is found in the TLB, the corresponding Physical Frame Number (PFN) is retrieved directly from the TLB entry. The physical address is constructed and the memory access proceeds immediately. This avoids the need to consult the page table in main memory.
    
2. **TLB Miss**: If the VPN is _not_ found in the TLB, a **TLB miss** occurs. The hardware (or OS, depending on the architecture) must now perform the full, slow translation by accessing the page table in memory to find the correct PTE. Once the PFN is found, the translation is loaded into the TLB (potentially evicting another entry), and the instruction is retried. This time, it will result in a TLB hit.
    

```
// Pseudocode for address translation with a TLB
VPN = (VirtualAddress & VPN_MASK) >> SHIFT;
(Success, TlbEntry) = TLB_Lookup(VPN);

if (Success == TRUE) { // TLB Hit
    if (CanAccess(TlbEntry.ProtectBits) == TRUE) {
        Offset = VirtualAddress & OFFSET_MASK;
        PhysAddr = (TlbEntry.PFN << SHIFT) | Offset;
        AccessMemory(PhysAddr);
    } else {
        RaiseException(PROTECTION_FAULT);
    }
} else { // TLB Miss
    // Hardware or OS trap handler performs the page table lookup
    PTEAddr = PTBR + (VPN * sizeof(PTE));
    PTE = AccessMemory(PTEAddr);

    if (PTE.Valid == FALSE) {
        RaiseException(PAGE_FAULT);
    } else {
        // Load the valid translation into the TLB
        TLB_Insert(VPN, PTE.PFN, PTE.ProtectBits);
        RetryInstruction(); // The instruction will now cause a TLB hit
    }
}
```

### Exploiting Locality

The effectiveness of the TLB relies entirely on the principle of **locality of reference**.

- **Temporal Locality**: If a program accesses a memory location, it is likely to access it again soon. Code in a loop is a prime example.
    
- **Spatial Locality**: If a program accesses a memory location, it is likely to access nearby locations soon. Accessing elements of an array sequentially is a classic example.
    

When a program accesses `array[0]`, a TLB miss might occur for that page. However, subsequent accesses to `array[1]`, `array[2]`, etc., will likely be on the same page, resulting in fast TLB hits. Because of locality, a small TLB can achieve a very high hit rate (often >99%), making the overhead of paging negligible most of the time.