
**Tags:** #os #memory-management #virtual-memory #swapping #page-fault #map-of-content

This note covers the mechanism that allows an operating system to provide an address space for a process that is larger than the available physical memory. By treating the physical memory as a cache for a much larger storage space on disk (the **swap space**), the OS can move less-used pages out to disk and bring them back into memory on demand.

This entire process is driven by a hardware-software interaction known as a **page fault**. We will explore the role of the "present bit" in the page table entry, the hardware's actions when a non-present page is accessed, and the detailed sequence of steps the OS's page fault handler takes to resolve the fault.

### Core Topics

- [[The Page Fault- Mechanism and Handling]]