# 80386 Segmentation in Protected Mode

**Tags:** #80386 #protected_mode #segmentation #descriptors

The 80386 takes the segmentation model introduced by the 80286 and enhances it for a 32-bit world. While the core concept of using selectors and descriptors remains the same, the descriptors themselves are updated to support a much larger address space and offer greater control.

### The 80386 Descriptor Format

The 8-byte descriptor is updated to accommodate a 32-bit base address and a 20-bit limit, along with new control flags.

|Byte Offset|High Byte (Bits 15-8)|Low Byte (Bits 7-0)|Purpose|
|---|---|---|---|
|**0 and 1**|`Limit (L15-L8)`|`Limit (L7-L0)`|Lower 16 bits of the Segment Limit.|
|**2 and 3**|`Base (B15-B8)`|`Base (B7-B0)`|Lower 16 bits of the Base Address.|
|**4**|`Base (B23-B16)`|_Unused_|Middle 8 bits of the Base Address.|
|**5**|`Access Rights Byte`|_See below_|Same as 80286 (Present, DPL, etc.).|
|**6**|`G, D, 0, AV` flags|`Limit (L19-L16)`|Upper 4 bits of Limit + new flags.|
|**7**|`Base (B31-B24)`|_Unused_|Upper 8 bits of the Base Address.|

This new structure combines a full **32-bit Base Address** and a **20-bit Limit**.

### New Descriptor Flags in the Access Rights Byte

The 80386 introduces four powerful new flags in the high nibble of the 6th byte of the descriptor:

|Flag|Name|Function|
|---|---|---|
|**`G`**|**Granularity**|This bit fundamentally changes how the `Limit` field is interpreted. **`G=0`**: The limit is measured in units of **1 byte**. The maximum segment size is 1 MB (2^20 bytes). **`G=1`**: The limit is measured in units of **4 KB pages**. The maximum segment size is 4 GB (2^20 * 4 KB). This is how the 80386 achieves huge segment sizes.|
|**`D`**|**Default Operand Size**|This bit tells the CPU whether instructions in this segment should default to 16-bit or 32-bit operations. **`D=0`**: Default is **16-bit**. Operands are `AX`, `SI`, etc. This is for running 80286 code. **`D=1`**: Default is **32-bit**. Operands are `EAX`, `ESI`, etc. This is for native 32-bit code.|
|**`AV`**|**Available**|This bit is not used by the hardware. It is "Available" for the operating system designer to use for any custom purpose.|

#### The 'D' Bit in Action: Code and Stack Segments

- **Code Segment:** If `D=1`, the CPU assumes all instructions and memory offsets are 32-bit unless an instruction prefix overrides it. If `D=0`, it assumes 16-bit operations. This allows the same 80386 processor to run both old 16-bit and new 32-bit programs seamlessly.
    
- **Stack Segment:** If `D=1`, stack operations (`PUSH`, `POP`, `CALL`) are 32-bit by default, and the `ESP` register is used as the stack pointer. If `D=0`, operations are 16-bit, and `SP` is used.
    

This powerful new descriptor format gave the 80386 the flexibility to run legacy code while unlocking the full potential of 32-bit addressing for new operating systems and applications.

**Links:**
[[The Intel 80386 - Dawn of 32-bit Computing]]