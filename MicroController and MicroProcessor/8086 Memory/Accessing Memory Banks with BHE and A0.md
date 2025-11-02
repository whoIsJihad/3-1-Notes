

**Tags:** #8086 #hardware #memory_banking #digital_logic

To control its two parallel memory banks, the 8086 uses two special signals. These signals function like "enables" or "chip selects" that you would have used in your Digital Logic Design labs.

1. **`A0` (Address bit 0):** This is the least significant bit of the memory address. By its nature, `A0` is `0` for all even addresses and `1` for all odd addresses. It is used to select the **Low (Even) Bank**.
    
2. **`BHE` (Bus High Enable):** This is a dedicated control signal (Pin 34). It is used to select the **High (Odd) Bank**.
    

Both signals are **active-low**, meaning a signal value of `0` enables the corresponding bank, and a `1` disables it. The processor combines these two signals to perform three types of memory access operations.

### Memory Access Logic Simulation

This table simulates how the 8086 sets these pins to achieve its goal.

|Desired Operation|Address Type|**`BHE`** Pin|**`A0`** Bit|Enabled Bank(s)|Data Bus Lines Used|
|---|---|---|---|---|---|
|Access a **16-bit word** (e.g., at `00002H`)|Even|**0** (Low)|**0** (Low)|Both High and Low|`D15 - D0` (Full)|
|Access an **8-bit byte** (e.g., at `00003H`)|Odd|**0** (Low)|**1** (High)|High Bank only|`D15 - D8` (Upper)|
|Access an **8-bit byte** (e.g., at `00002H`)|Even|**1** (High)|**0** (Low)|Low Bank only|`D7 - D0` (Lower)|
|(Invalid Operation)|N/A|**1** (High)|**1** (High)|None|None|

### The Unaligned Access Problem

There's a critical performance penalty hidden in this design. What happens if a programmer tries to read a 16-bit word starting from an **odd** address (e.g., `00003H`)?

- The first byte (`at 00003H`) is in the High Bank.
    
- The second byte (`at 00004H`) is in the Low Bank.
    

The 8086 hardware **cannot** read from two different "rows" of its banks in a single cycle. To handle this [[The 8086 Unaligned Memory Access Problem]], it must perform two separate 8-bit read cycles back-to-back, which takes twice as long. This is why alignment is a critical concept in performance-oriented low-level programming.

**Links:** [[8086 Physical Memory Introduction]]