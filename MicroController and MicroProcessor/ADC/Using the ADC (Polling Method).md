# Using the ADC (Polling Method)

**Tags:** #microcontroller #atmega32 #adc #C-code

The polling method is the most straightforward way to use the ADC. The program actively waits in a loop until the conversion is finished. While simple, this method ties up the CPU, preventing it from doing other tasks.

### Steps for Polling

1. **Configure the ADC**:
    
    - Set the reference voltage and input channel in the [[ADMUX Register]].
        
    - Enable the ADC (`ADEN=1`) and set a prescaler in the [[ADCSRA Register]].
        
2. **Start Conversion**:
    
    - Set the `ADSC` (ADC Start Conversion) bit in `ADCSRA` to `1`.
        
3. **Wait for Completion**:
    
    - Continuously check (poll) the `ADSC` bit. The hardware clears this bit to `0` when the conversion is done. A `while` loop is used for this.
        
4. **Read the Result**:
    
    - Read the digital value from the [[ADCH and ADCL Registers]].
        

### C Code Example

This code reads an analog value from ADC0, uses AVCC as a reference, left-adjusts the result for 8-bit precision, and displays it on PORTB.

```
#include <avr/io.h>

int main(void) {
    // Port B as output to display result
    DDRB = 0xFF; 
    
    // Step 1: Configure ADC
    // ADMUX: REFS0=1 (AVCC ref), ADLAR=1 (Left Adjust), MUX selected for ADC0
    ADMUX = (1 << REFS0) | (1 << ADLAR); 
    
    // ADCSRA: ADEN=1 (Enable ADC), Prescaler = 128
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);

    while (1) {
        // Step 2: Start conversion
        ADCSRA |= (1 << ADSC); 
        
        // Step 3: Wait for conversion to complete by polling the ADSC bit
        while (ADCSRA & (1 << ADSC));
        
        // Step 4: Read the 8-bit result and display it
        PORTB = ADCH; 
    }
}
```

**Links**: [[ATmega32 ADC]], [[Using the ADC (Interrupt Method)]]