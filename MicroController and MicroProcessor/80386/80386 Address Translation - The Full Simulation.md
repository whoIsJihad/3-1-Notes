# 80386 Address Translation: The Full Simulation

**Tags:** #80386 #mmu #segmentation #paging #simulation

The ultimate task of the 80386's Memory Management Unit (MMU) is to convert a logical address (`Selector:Offset`) into a final physical address. When paging is enabled, this is a two-phase process: **Segmentation** followed by **Paging**. This simulation will walk through the entire journey.

**Scenario:**

- The CPU needs to access data using the logical address `CS:EIP`.
    
- `CS` contains the selector `0018h`. `EIP` contains the offset `10A2BC23h`.
    
- The `GDTR` points to the GDT at physical address `00002000h`.
    
- The `CR3` register points to the Page Directory at physical address `00001000h`.
    
- Paging is **enabled** (`PG` bit in `CR0` is 1).
    

### Phase 1: Segmentation (Logical Address -> Linear Address)

**Goal:** Convert `Selector:Offset` into a 32-bit linear address.

**Step 1: Decode the Selector** The CPU looks at the `CS` register (`0018h` or `0001 1000` binary).

- **Index:** `0000 0000 0001 1` -> **Entry #3**.
    
- **TI:** `0` -> Use **GDT**.
    
- **RPL:** `00` -> Requesting Ring 0.
    

**Step 2: Locate the Descriptor** The CPU calculates the physical address of the descriptor in the GDT.

- `Descriptor Address = GDTR_Base + (Index * 8)`
    
- `Descriptor Address = 00002000h + (3 * 8) = 00002000h + 18h = 00002018h`
    

**Step 3: Fetch the Descriptor and Calculate Linear Address** The CPU reads the 8-byte descriptor from `00002018h`. Let's assume it finds:

- **Base Address:** `3823A216h`
    
- **Limit:** `4320B` with `G` bit = `1` (Granularity is 4KB pages).
    
- **Security checks pass.**
    

The Segmentation Unit now calculates the 32-bit linear address.

- `Linear Address = Descriptor_Base + Offset`
    
- `Linear Address = 3823A216h + 10A2BC23h = 48C65E39h`
    

**End of Phase 1:** The logical address `0018:10A2BC23` has been translated to the linear address `48C65E39h`. If paging were disabled, this would be the final physical address. But it's enabled, so we proceed.

### Phase 2: Paging (Linear Address -> Physical Address)

**Goal:** Translate the 32-bit linear address `48C65E39h` into a final physical address using the two-level page tables.

**Step 4: Split the Linear Address** The Paging Unit hardware splits the 32-bit linear address into three distinct parts:

**Linear Address:** `48C65E39h` **In Binary:** `0100 1000 1100 0110 0101 1110 0011 1001`

|Bits 31-22 (10 bits)|Bits 21-12 (10 bits)|Bits 11-0 (12 bits)|
|---|---|---|
|**Directory Index**|**Page Table Index**|**Page Offset**|
|`0100 1000 11`|`00 0110 0101`|`1110 0011 1001`|
|`123h` (or `291` decimal)|`065h` (or `101` decimal)|`E39h`|

**Step 5: Find the Page Table Entry (First Memory Access)**

1. **Find Directory Entry:** The CPU starts with the Page Directory Base Address from `CR3` (`00001000h`) and uses the Directory Index (`123h`) to find the correct entry. Each entry is 4 bytes.
    
    - `PDE Address = CR3_Base + (Directory_Index * 4)`
        
    - `PDE Address = 00001000h + (123h * 4) = 00001000h + 48Ch = 0000148Ch`
        
2. **Read Directory Entry:** The CPU reads the 4-byte Page Directory Entry (PDE) at `0000148Ch`. This entry contains the physical base address of the _next_ level table. Let's assume it reads `00020000h`.
    

**Step 6: Find the Page Frame Address (Second Memory Access)**

1. **Find Table Entry:** The CPU now uses the base address from the PDE (`00020000h`) and the Page Table Index (`065h`) to find the final entry.
    
    - `PTE Address = PDE_Value + (Page_Table_Index * 4)`
        
    - `PTE Address = 00020000h + (065h * 4) = 00020000h + 194h = 00020194h`
        
2. **Read Table Entry:** The CPU reads the 4-byte Page Table Entry (PTE) at `00020194h`. This entry contains the physical base address of the actual **4 KB page frame**. Let's assume it reads `00300000h`.
    

**Step 7: Calculate the Final Physical Address** The hardware now combines the base address of the page frame with the final part of the linear address.

1. **Page Frame Base Address:** `00300000h` (from the PTE)
    
2. **Page Offset:** `E39h` (from the original linear address)
    

- `Physical Address = Page_Frame_Base + Page_Offset`
    
- `Physical Address = 00300000h + E39h = 00300E39h`
    

**Final Result:** The logical address `CS:EIP` resolves to the physical RAM location **`00300E39h`**. The CPU can now perform its read/write operation on this address. The entire, complex process is handled transparently by the hardware, accelerated by the on-chip Translation Lookaside Buffer (TLB) to avoid the two extra memory accesses for recently used pages.