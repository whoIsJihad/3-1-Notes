

**Tags:** #8086 #segmentation #addressing #simulation

The 8086's Bus Interface Unit (BIU) is responsible for converting the 16-bit logical `Segment:Offset` address into a 20-bit physical address that can be sent to the memory controller. The calculation is a simple hardware-level operation.

**The Formula:**

```
Physical Address = (Segment Address * 16) + Offset Address
```

In hexadecimal, multiplying by 16 is equivalent to shifting the number left by one digit (or 4 bits) and appending a `0`.

### Simulation of an Address Calculation

Let's say the program needs to fetch an instruction. The CPU knows the logical address from its registers:

- The Code Segment register `CS` holds `A100H`.
    
- The Instruction Pointer `IP` holds `B234H`.
    
- The logical address is written as `A100:B234`.
    

Here is how the BIU calculates the 20-bit physical address:

**Step 1: Take the 16-bit Segment Address from `CS`**

```
A100H
```

**Step 2: Shift the Segment Address left by 4 bits (Append a `0H`)** This scales the segment value to a 20-bit paragraph boundary address.

```
A1000H
```

**Step 3: Add the 16-bit Offset Address from `IP`**

```
  A1000H  (Shifted Segment Address)
+  B234H  (Offset Address)
----------
  AB234H  (20-bit Physical Address)
```

The final 20-bit physical address `AB234H` is what the BIU places on the external address bus (`A19-A0`) to begin the memory read cycle. This calculation happens for every single memory access.

**Links:** [[8086 Logical Memory and Segmentation]], [[Simulating an 8086 Memory Read Cycle]]