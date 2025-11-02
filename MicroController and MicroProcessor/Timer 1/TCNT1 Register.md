# TCNT1 Register

**Tags:** #microcontroller #avr #timers #registers #timer1

The **Timer/Counter1 Register (TCNT1)** is the 16-bit counter for [[AVR Timer1]].

### Functionality

Being a 16-bit register, it is composed of two 8-bit registers:

- **TCNT1H** (High byte)
    
- **TCNT1L** (Low byte)
    

The AVR hardware handles the 16-bit arithmetic automatically. When the CPU reads or writes to the 16-bit register, it uses a temporary high byte register (`TEMP`) to ensure the operation is atomic (cannot be interrupted halfway through).

- **When writing to TCNT1:** The high byte must be written first to `TCNT1H`. When the low byte is written to `TCNT1L`, both bytes are updated simultaneously.
    
- **When reading from TCNT1:** The low byte must be read first from `TCNT1L`. This causes the high byte's value to be copied into the temporary register. When the high byte is read from `TCNT1H`, the value is fetched from this temporary register.
    

This ensures that the 16-bit value read is consistent, even if a timer tick occurs between the reading of the low and high bytes. Most C compilers for AVR (like `avr-gcc`) handle this automatically when you access `TCNT1` as a 16-bit variable.

The counter increments from 0 up to 65535 (0xFFFF) before a [[Timer Overflow]] occurs.

**Links:** [[AVR Timer1]]