# EEPROM Read C Function

Tags: eeprom, c_code, function, programming

Here is an example C function to read data from the ATmega32 EEPROM.

```
unsigned char EEPROM_read(unsigned int uiAddress)
{
    /* Wait for completion of previous write */
    while(EECR & (1<<EEWE));

    /* Set up address register */
    EEAR = uiAddress;

    /* Start eeprom read by writing EERE */
    EECR |= (1<<EERE);

    /* Return data from data register */
    return EEDR;
}
```
