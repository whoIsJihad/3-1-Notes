# Programming the USART

**Tags:** #microcontroller #atmega32 #usart #C-code

Programming the USART involves three main steps: initialization, sending data, and receiving data. This note covers the basic polling method.

### 1. Initializing the USART

This function sets up all the necessary registers for communication.

```
void USART_Init(unsigned int ubrr) {
    // ---- Set Baud Rate ----
    UBRRH = (unsigned char)(ubrr >> 8);
    UBRRL = (unsigned char)ubrr;
    
    // ---- Enable Receiver and Transmitter ----
    // Set the RXEN and TXEN bits in UCSRB
    UCSRB = (1 << RXEN) | (1 << TXEN);
    
    // ---- Set Frame Format: 8 data, 2 stop bit ----
    // To write to UCSRC, the URSEL bit must be set to 1.
    // USBS=1 for 2 stop bits, UCSZ1:0=11 for 8-bit data.
    UCSRC = (1 << URSEL) | (1 << USBS) | (3 << UCSZ0);
}
```

### 2. Sending a Character (Transmit)

To send a character, you wait until the transmit buffer is empty, and then write your data to the `UDR` register.

```
void USART_Transmit(unsigned char data) {
    // ---- Wait for empty transmit buffer ----
    // The UDRE flag in UCSRA is 1 when the buffer is ready.
    while (!(UCSRA & (1 << UDRE))) {
        // Do nothing, just wait
    }
    
    // ---- Put data into buffer, which sends the data ----
    UDR = data;
}
```

### 3. Receiving a Character

To receive a character, you wait until the "Receive Complete" flag is set, and then read the data from the `UDR` register.

```
unsigned char USART_Receive(void) {
    // ---- Wait for data to be received ----
    // The RXC flag in UCSRA is 1 when new data has been received.
    while (!(UCSRA & (1 << RXC))) {
        // Do nothing, just wait
    }
    
    // ---- Get and return received data from buffer ----
    return UDR;
}
```

### Example `main()` function

```
#define F_CPU 16000000UL
#define BAUD 9600
#define MYUBRR F_CPU/16/BAUD-1

int main(void) {
    USART_Init(MYUBRR);
    unsigned char received_char;
    
    while (1) {
        // Echo back any character received
        received_char = USART_Receive();
        USART_Transmit(received_char);
    }
}
```

**Links**: [[USART Communication]], [[USART Control and Status Registers (UCSRA, B, C)]]