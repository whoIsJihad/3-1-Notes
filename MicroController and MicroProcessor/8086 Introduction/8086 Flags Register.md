# 8086 Flags Register

**Tags:** #microprocessor #8086 #registers #flags

The FLAGS register is a special 16-bit register inside the EU. It doesn't hold data but instead holds a collection of individual bits called "flags." Each flag reports on the status of the last operation or controls the behavior of the CPU.

### Layout of the Flags Register

|Bit|15|14|13|12|11|10|9|8|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Flag**|X|X|X|X|**OF**|**DF**|**IF**|**TF**|**SF**|**ZF**|X|**AF**|X|**PF**|X|**CF**|

### Status Flags (Updated automatically after arithmetic/logic operations)

- **`CF` (Carry Flag):** Set to 1 if an operation resulted in a carry out (for addition) or a borrow (for subtraction) from the most significant bit. Used for multi-word arithmetic.
    
- **`PF` (Parity Flag):** Set to 1 if the lower 8 bits of the result contain an even number of '1' bits. Used for simple error checking.
    
- **`AF` (Auxiliary Carry Flag):** Set to 1 if there was a carry/borrow between bit 3 and bit 4. This is specifically for BCD (Binary Coded Decimal) arithmetic.
    
- **`ZF` (Zero Flag):** Set to 1 if the result of an operation is zero. Very important for loops and comparisons (`JE`/`JNE` - Jump if Equal/Not Equal).
    
- **`SF` (Sign Flag):** A copy of the most significant bit (MSB) of the result. For signed numbers, an MSB of 1 means the result is negative.
    
- **`OF` (Overflow Flag):** Set to 1 if a signed arithmetic operation produced a result that is too large or too small to fit in the destination. For example, adding two large positive numbers and getting a negative result. This indicates the signed result is invalid.
    

### Control Flags (Set or cleared by the programmer to control the CPU)

- **`DF` (Direction Flag):** Controls the direction of string operations.
    
    - If `DF=0` (using `CLD` instruction), `SI` and `DI` are automatically incremented.
        
    - If `DF=1` (using `STD` instruction), `SI` and `DI` are automatically decremented.
        
- **`IF` (Interrupt Flag):** Controls whether the CPU will respond to maskable interrupts from external devices.
    
    - If `IF=1` (using `STI` instruction), interrupts are enabled.
        
    - If `IF=0` (using `CLI` instruction), interrupts are ignored.
        
- **`TF` (Trap Flag):** If set to 1, the CPU enters single-step mode. It executes one instruction and then triggers a special internal interrupt. This is the mechanism used by debuggers.
    

**Links:** [[8086 Execution Unit (EU) Registers]]