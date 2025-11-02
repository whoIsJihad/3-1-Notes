# Timer Interrupts

**Tags:** #microcontroller #avr #timers #interrupts

Timer interrupts allow the microcontroller to execute a specific piece of code (an Interrupt Service Routine, or ISR) automatically when a certain timer event occurs. This is extremely efficient as it allows the CPU to perform other tasks while waiting for a time-based event, rather than being stuck in a delay loop.

The main timer-related interrupt sources are:

1. **Timer Overflow:** Triggers when the timer counts past its maximum value. See [[Timer Overflow]].
    
2. **Output Compare Match:** Triggers when the timer's count value ([[TCNT0]] or [[TCNT1]]) matches the value stored in an Output Compare Register ([[OCR1A and OCR1B Registers]]). This is the core of [[Timer0 CTC Mode]].
    
3. **Input Capture:** Triggers on an external event (a signal change on a specific pin) and captures the current timer value. See [[Input Capture Mode]].
    

To use a timer interrupt, you must:

1. Enable interrupts globally by calling `sei();`.
    
2. Enable the specific timer interrupt (e.g., Timer Overflow, Output Compare) by setting the corresponding bit in the [[TIMSK Register]].
    
3. Write an ISR for the specific interrupt vector (e.g., `TIMER0_OVF_vect` for Timer0 overflow).
    

The interrupt flag for the event is set in the [[TIFR Register]]. This flag is usually cleared automatically when the ISR is executed.

**Links:** [[Timer 1/AVR Timers and Counters]], [[TIMSK Register]], [[TIFR Register]]