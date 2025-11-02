# USART Control and Status Registers (UCSRA, B, C)

**Tags:** #microcontroller #atmega32 #usart #registers

The USART is primarily configured using three registers: `UCSRA`, `UCSRB`, and `UCSRC`.

### [[UCSRA]] – USART Control and Status Register A

This register mainly holds status flags for the communication.

| Bit | Name   | Description                                                                                                      |
| --- | ------ | ---------------------------------------------------------------------------------------------------------------- |
| 7   | `RXC`  | **Receive Complete Flag**. Set to `1` when a new, unread character is in the receive buffer.                     |
| 6   | `TXC`  | **Transmit Complete Flag**. Set to `1` when the entire frame in the transmit shift register has been sent.       |
| 5   | `UDRE` | **USART Data Register Empty Flag**. Set to `1` when the transmit buffer (`UDR`) is empty and ready for new data. |
| 4   | `FE`   | **Frame Error Flag**. Set if the receiver detects an invalid stop bit.                                           |
| 3   | `DOR`  | **Data OverRun Flag**. Set if a new character is received before the previous one was read from the buffer.      |
| 2   | `PE`   | **Parity Error Flag**. Set if a parity mismatch is detected.                                                     |
| 1   | `U2X`  | **Double Transmission Speed**. Set to `1` to double the baud rate for the same UBRR setting.                     |
| 0   | `MPCM` | **Multi-processor Communication Mode**.                                                                          |
|     |        |                                                                                                                  |

### [[UCSRB]] – USART Control and Status Register B

This register is used for enabling the transmitter/receiver and their interrupts.

| Bit | Name    | Description                                                         |
| --- | ------- | ------------------------------------------------------------------- |
| 7   | `RXCIE` | **RX Complete Interrupt Enable**.                                   |
| 6   | `TXCIE` | **TX Complete Interrupt Enable**.                                   |
| 5   | `UDRIE` | **UDR Empty Interrupt Enable**.                                     |
| 4   | `RXEN`  | **Receiver Enable**. Set to `1` to enable the USART receiver.       |
| 3   | `TXEN`  | **Transmitter Enable**. Set to `1` to enable the USART transmitter. |
| 2   | `UCSZ2` | Part of the character size selection (used with `UCSRC`).           |
| 1   | `RXB8`  | The 9th received data bit (if using 9-bit mode).                    |
| 0   | `TXB8`  | The 9th transmitted data bit (if using 9-bit mode).                 |

### [[UCSRC]] – USART Control and Status Register C

This register is used to set the communication mode, parity, stop bits, and character size. **Note:** This register shares the same memory address as `UBRRH`, so the `URSEL` bit must be set to `1` to write to `UCSRC`.

|Bit|Name|Description|
|---|---|---|
|7|`URSEL`|**Register Select**. Must be `1` to write to `UCSRC`.|
|6|`UMSEL`|**USART Mode Select**. `0` = Asynchronous, `1` = Synchronous.|
|5, 4|`UPM1:0`|**Parity Mode**. `00` = Disabled, `10` = Even Parity, `11` = Odd Parity.|
|3|`USBS`|**Stop Bit Select**. `0` = 1 stop bit, `1` = 2 stop bits.|
|2, 1|`UCSZ1:0`|**Character Size** (with `UCSZ2` in `UCSRB`). `011` for 8-bit.|
|0|`UCPOL`|**Clock Polarity** (used in synchronous mode only).|

**Links**: [[USART Communication]], [[Programming the USART]]