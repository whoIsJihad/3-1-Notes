# SPI Registers (SPCR, SPSR, SPDR)

**Tags:** #microcontroller #atmega32 #spi #registers

The SPI peripheral on the ATmega32 is controlled by three registers: `SPCR` for control, `SPSR` for status, and `SPDR` for data.

### `SPCR` – SPI Control Register

This is the main register for configuring the SPI module.

|Bit|Name|Description|
|---|---|---|
|7|`SPIE`|**SPI Interrupt Enable**. Set to `1` to enable the SPI transfer complete interrupt.|
|6|`SPE`|**SPI Enable**. Set to `1` to turn on the SPI peripheral.|
|5|`DORD`|**Data Order**. `0` = MSB first, `1` = LSB first.|
|4|`MSTR`|**Master/Slave Select**. `1` = Master mode, `0` = Slave mode.|
|3|`CPOL`|**Clock Polarity**. `0` = Clock is low when idle, `1` = Clock is high when idle.|
|2|`CPHA`|**Clock Phase**. `0` = Sample on leading edge, `1` = Sample on trailing edge.|
|1, 0|`SPR1:0`|**SPI Clock Rate Select** (Master mode only). Sets the SCK frequency as a division of the system clock (e.g., f_cpu/4, f_cpu/16).|

### `SPSR` – SPI Status Register

This register holds status flags for the SPI communication.

|Bit|Name|Description|
|---|---|---|
|7|`SPIF`|**SPI Interrupt Flag**. Set by hardware to `1` when a serial transfer is complete.|
|6|`WCOL`|**Write Collision Flag**. Set if you write to `SPDR` while a transfer is already in progress.|
|0|`SPI2X`|**Double SPI Speed Bit**. Set to `1` to double the SPI clock speed (halves the prescaler values).|

### `SPDR` – SPI Data Register

This is the read/write register for the data being transferred.

- **Writing to `SPDR`** starts an SPI transmission by loading the data into the shift register.
    
- **Reading from `SPDR`** retrieves the byte that was just received in the shift register.
    

Because SPI is a data exchange, a write to `SPDR` will always result in a byte being received, which can then be read from `SPDR` after the `SPIF` flag is set.

**Links**: [[SPI Communication]]