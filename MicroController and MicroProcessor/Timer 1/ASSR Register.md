# ASSR Register (Asynchronous Status Register)

**Tags:** #microcontroller #avr #timers #registers #timer2 #rtc

The Asynchronous Status Register (ASSR) is a special register used exclusively for controlling the asynchronous operation of [[AVR Timer2]].

### Bit Configuration

| Bit            | 7   | 6   | 5   | 4   | 3   | 2      | 1      | 0      |
| -------------- | --- | --- | --- | --- | --- | ------ | ------ | ------ |
| **Name**       | -   | -   | -   | -   | AS2 | TCN2UB | OCR2UB | TCR2UB |
| **Read/Write** | R   | R   | R   | R   | R/W | R      | R      | R      |
| **Initial**    | 0   | 0   | 0   | 0   | 0   | 0      | 0      | 0      |

### Bit Descriptions

|Bit|Name|Description|
|---|---|---|
|3|**AS2**|**Asynchronous Timer/Counter2:** When this bit is set to 1, Timer2 is clocked from the external crystal oscillator connected to the TOSC1/TOSC2 pins. When cleared to 0, it is clocked from the main I/O clock.|
|2|**TCN2UB**|**Timer/Counter2 Update Busy:** When running asynchronously, writing to TCNT2, OCR2, or TCCR2 takes time. This bit is set by hardware while the register is being updated and cleared when the update is complete. You must wait for this bit to be 0 before writing to TCNT2.|
|1|**OCR2UB**|**Output Compare Register2 Update Busy:** Similar to TCN2UB, but for the OCR2 register. Wait for this bit to be 0 before writing to OCR2.|
|0|**TCR2UB**|**Timer/Counter Control Register2 Update Busy:** Similar to TCN2UB, but for the TCCR2 register. Wait for this bit to be 0 before writing to TCCR2.|

Before enabling asynchronous mode (setting `AS2`), you should first configure `TCNT2`, `OCR2`, and `TCCR2`. After setting `AS2`, you must wait for the Update Busy flags to clear before the timer is ready to use.

**Links:** [[AVR Timer2]]