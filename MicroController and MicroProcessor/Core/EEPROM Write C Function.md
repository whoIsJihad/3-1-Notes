# EEPROM Write C Function

Tags: eeprom, c_code, function, programming

Here is an example C function to write data to the ATmega32 EEPROM.

```
void EEPROM_write(unsigned int uiAddress, unsigned char ucData)
{
    /* Wait for completion of previous write */
    while(EECR & (1<<EEWE));

    /* Set up address and data registers */
    EEAR = uiAddress;
    EEDR = ucData;

    /* Write logical one to EEMWE */
    EECR |= (1<<EEMWE);

    /* Start eeprom write by setting EEWE */
    EECR |= (1<<EEWE);
}
```
