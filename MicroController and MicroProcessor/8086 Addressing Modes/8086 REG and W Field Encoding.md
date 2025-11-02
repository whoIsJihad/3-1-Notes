# 8086 REG and W Field Encoding

**Tags:** #8086 #reference #tables #encoding

This table is a quick reference for determining the 3-bit code for a register operand in the `REG` field of an instruction. The meaning of the code depends on the `W` (Word/Byte) bit.

### REG Field Encoding

|`REG` Code|`W = 0` (Byte)|`W = 1` (Word)|
|---|---|---|
|`000`|`AL`|`AX`|
|`001`|`CL`|`CX`|
|`010`|`DL`|`DX`|
|`011`|`BL`|`BX`|
|`100`|`AH`|`SP`|
|`101`|`CH`|`BP`|
|`110`|`DH`|`SI`|
|`111`|`BH`|`DI`|

**Links:** [[Decoding the MOV Instruction]], [[8086 MOD and R M Field Encoding]]