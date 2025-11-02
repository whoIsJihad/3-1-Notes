# TIFR Register (Timer/Counter Interrupt Flag Register)

**Tags:** #microcontroller #avr #timers #registers #interrupts

The TIFR register holds the status flags for timer events. A flag is automatically set to 1 by the hardware when the corresponding event occurs (e.g., an overflow or a compare match).

### Bit Configuration

| Bit               | 7    | 6    | 5    | 4     | 3     | 2    | 1    | 0    |     |
| ----------------- | ---- | ---- | ---- | ----- | ----- | ---- | ---- | ---- | --- |
| **Name**          | OCF2 | TOV2 | ICF1 | OCF1A | OCF1B | TOV1 | OCF0 | TOV0 |     |
| **Read/Write**    | R/W  | R/W  | R/W  | R/W   | R/W   | R/W  | R/W  | R/W  |     |
| **Initial Value** | 0    | 0    | 0    | 0     | 0     | 0    | 0    | 0    |     |

### Bit Descriptions

|Bit|Name|Description|
|---|---|---|
|7|**OCF2**|Output Compare Flag 2. Set when TCNT2 matches OCR2.|
|6|**TOV2**|Timer/Counter2 Overflow Flag. Set on Timer2 [[Timer Overflow]].|
|5|**ICF1**|Input Capture Flag 1. Set when an event occurs on the ICP1 pin.|
|4|**OCF1A**|Output Compare A Flag 1. Set when TCNT1 matches OCR1A.|
|3|**OCF1B**|Output Compare B Flag 1. Set when TCNT1 matches OCR1B.|
|2|**TOV1**|Timer/Counter1 Overflow Flag. Set on Timer1 [[Timer Overflow]].|
|1|**OCF0**|Output Compare Flag 0. Set when TCNT0 matches OCR0.|
|0|**TOV0**|Timer/Counter0 Overflow Flag. Set on Timer0 [[Timer Overflow]].|

A flag is cleared in one of two ways:

1. **Automatically:** When the corresponding interrupt service routine is executed.
    
2. **Manually:** By writing a logic 1 to the bit position. (Note: you write a 1 to clear it, not a 0).
    

**Links:** [[Timer Interrupts]], [[TIMSK Register]]