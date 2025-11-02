# Default Segment and Offset Mappings

**Tags:** #8086 #registers #assembly #addressing

While any segment can theoretically be used for any purpose, the 8086 architecture has strong conventions and default pairings for specific operations. When an instruction implies a memory access without explicitly stating which segment to use, the BIU automatically defaults to a specific segment register. This simplifies assembly programming immensely.

### The Default Pairings

This table outlines the primary default mappings for different types of memory access.

|Memory Access Purpose|Default Segment Register|Common Offset Register(s)|Logical Address Example|
|---|---|---|---|
|**Instruction Fetch**|`CS` (Code Segment)|`IP` (Instruction Pointer)|`CS:IP`|
|**General Data Access**|`DS` (Data Segment)|`BX`, `SI`, `DI`, or a direct 16-bit address|`DS:BX`|
|**Stack Operations (PUSH, POP)**|`SS` (Stack Segment)|`SP` (Stack Pointer)|`SS:SP`|
|**Stack Data Access (non-PUSH/POP)**|`SS` (Stack Segment)|`BP` (Base Pointer)|`SS:BP`|
|**String Operation Destination**|`ES` (Extra Segment)|`DI` (Destination Index)|`ES:DI`|
|**String Operation Source**|`DS` (Data Segment)|`SI` (Source Index)|`DS:SI`|

### Segment Override Prefix

Assembly language provides a way to override these defaults. A programmer can use a **segment override prefix** before an instruction to tell the CPU to use a different segment register for that one operation.

For example, the instruction `MOV AX, [BX]` would normally use `DS` by default (`DS:BX`). However, `MOV AX, ES:[BX]` tells the CPU to use the `ES` register instead, calculating the address from `ES:BX`.

**Links:** [[8086 Logical Memory and Segmentation]]