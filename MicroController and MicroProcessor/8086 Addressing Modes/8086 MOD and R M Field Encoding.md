# 8086 MOD and R/M Field Encoding

**Tags:** #8086 #reference #tables #encoding

This table is a comprehensive reference for the `MOD` and `R/M` fields. These 5 bits work together to specify the second operand and its addressing mode.

- **When `MOD` = `11`**, the `R/M` field specifies a register operand.
    
- **When `MOD` is `00`, `01`, or `10`**, the `R/M` field specifies a memory addressing mode. The `MOD` field determines the size of the displacement (none, 8-bit, or 16-bit).
    

### MOD and R/M Field Encoding Table

|`R/M` Code|`MOD = 00` (No Displacement)|`MOD = 01` (+8-bit Disp.)|`MOD = 10` (+16-bit Disp.)|`MOD = 11` (Register Mode)|
|---|---|---|---|---|
|||||**`W=0` / `W=1`**|
|**`000`**|`[BX + SI]`|`[BX + SI] + d8`|`[BX + SI] + d16`|`AL` / `AX`|
|**`001`**|`[BX + DI]`|`[BX + DI] + d8`|`[BX + DI] + d16`|`CL` / `CX`|
|**`010`**|`[BP + SI]`|`[BP + SI] + d8`|`[BP + SI] + d16`|`DL` / `DX`|
|**`011`**|`[BP + DI]`|`[BP + DI] + d8`|`[BP + DI] + d16`|`BL` / `BX`|
|**`100`**|`[SI]`|`[SI] + d8`|`[SI] + d16`|`AH` / `SP`|
|**`101`**|`[DI]`|`[DI] + d8`|`[DI] + d16`|`CH` / `BP`|
|**`110`**|**`d16` (Direct Address)**|`[BP] + d8`|`[BP] + d16`|`DH` / `SI`|
|**`111`**|`[BX]`|`[BX] + d8`|`[BX] + d16`|`BH` / `DI`|

**Note:** The combination `MOD=00` and `R/M=110` is a special case used for Direct Addressing, where a 16-bit displacement (`d16`) is the only component of the address.

**Links:** [[Decoding the MOV Instruction]], [[8086 REG and W Field Encoding]]