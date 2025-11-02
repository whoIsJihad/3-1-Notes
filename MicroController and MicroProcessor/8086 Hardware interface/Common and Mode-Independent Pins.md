# Common and Mode-Independent Pins

**Tags:** #8086 #hardware #pinout

Regardless of whether the 8086 is in Minimum or Maximum mode, a core set of pins retain the same fundamental functions. These pins handle power, clocking, interrupts, and basic system synchronization.

|Pin(s)|Name(s)|I/O|Function & Connection Simulation|
|---|---|---|---|
|40|`VCC`|In|**Power Supply:** Connects to a stable +5V power source. This is the lifeblood of the chip.|
|1, 20|`GND`|In|**Ground:** Provides the 0V reference for all signals. Having two ground pins helps to sink electrical noise and ensure signal integrity.|
|19|`CLK`|In|**Clock Input:** Receives the system clock signal from an external clock generator chip (like the 8284A). Every internal operation is synchronized to the rising edge of this clock pulse.|
|21|`RESET`|In|**Reset:** If held HIGH for at least 4 clock cycles, the CPU terminates its current activity, clears its internal registers (e.g., sets `CS` to `FFFFH`, `IP` to `0000H`), and starts execution from address `FFFF0H`.|
|22|`READY`|In|**Synchronization:** An input from slow memory or I/O devices. If a device pulls `READY` LOW, the 8086 will enter a "wait state," pausing its bus cycle until the device is ready and pulls the pin HIGH again. This is critical for interfacing with devices of varying speeds.|
|23|`TEST`|In|**Wait for Coprocessor:** An input pin tested by the `WAIT` instruction. If `TEST` is HIGH, the CPU will pause execution at the `WAIT` instruction. It is typically connected to the `BUSY` signal of a coprocessor (like the 8087) to ensure the coprocessor has finished its task before the CPU proceeds.|
|18|`INTR`|In|**Maskable Interrupt Request:** An external device can request an interrupt by pulling this pin HIGH. The 8086 will only respond if its internal Interrupt Flag (`IF`) is set. This is a "polite" interrupt request.|
|17|`NMI`|In|**Non-Maskable Interrupt:** A high-priority interrupt that cannot be ignored (it does not check the `IF` flag). This is used for critical events like a power failure warning.|
|2-16, 39|`AD15`-`AD0`|I/O|**Multiplexed Address/Data Bus:** These 16 lines carry the lower 16 bits of the address and the 16-bit data word.|
|35-38|`A19/S6`-`A16/S3`|Out|**Multiplexed Address/Status Bus:** These 4 lines carry the upper 4 bits of the address and also provide status information about the current bus cycle.|
|34|`BHE/S7`|Out|**Bus High Enable / Status:** Used to enable the upper byte of the data bus (`D8-D15`) for 16-bit transfers or byte transfers on odd addresses. It's the key to memory banking.|

## 1. INTR (Maskable Interrupt Request)

The INTR pin handles **normal, external interrupts** from peripherals (like keyboards or disk controllers) that need the CPU's attention.

|Aspect|Description|
|---|---|
|**Hardware Pin**|INTR (Pin 18)|
|**How it's Triggered**|An external device pulls the INTR pin HIGH.|
|**CPU Control**|The 8086 will only respond if the **Interrupt Flag (IF) in the FLAGS register is set** (enabled).|
|**Acknowledgement**|If IF is set, the CPU responds by performing two INTA (Interrupt Acknowledge) cycles. This INTA signal (Pin 24 in Minimum Mode) tells the interrupting device to place an **interrupt vector number** onto the data bus.|
|**Key Purpose**|Allows external devices to "politely" request CPU time, which can be **masked** (ignored) by the programmer using the CLI instruction.|

Export to Sheets

## 2. NMI (Non-Maskable Interrupt)

The NMI pin is reserved for **critical, system-failure events** that absolutely cannot be ignored.

|Aspect|Description|
|---|---|
|**Hardware Pin**|NMI (Pin 17)|
|**How it's Triggered**|An external device, such as a circuit detecting a power failure, pulses the NMI pin HIGH.|
|**CPU Control**|The 8086 **cannot ignore this request**; it does **not** check the Interrupt Flag (IF).|
|**Vector**|NMI is always associated with a **fixed, high-priority interrupt vector** (Type 2, or address 0008H).|
|**Key Purpose**|Used for critical events like power failure warnings or memory parity errors, as the CPU must immediately save its state.|
## The Role of the Interrupt Flag (IF)

The difference hinges on the **Interrupt Flag (IF)**, which is one of the Control Flags in the FLAGS register.

- **Enabling/Disabling:**
    
    - **STI** (Set Interrupt Flag) instruction sets IF=1, **enabling** INTR.
        
    - **CLI** (Clear Interrupt Flag) instruction sets IF=0, **disabling** (masking) INTR.
        
- **NMI bypasses this entirely**, ensuring immediate servicing.
**Links:** [[8086 Hardware Interface and Pinout]], [[Simulating an 8086 Memory Read Cycle]]