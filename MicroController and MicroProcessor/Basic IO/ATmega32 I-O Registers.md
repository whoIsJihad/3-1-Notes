# ATmega32 I/O Registers

**Tags:** #microcontroller #atmega32 #registers #IO

For each I/O port, there are three 8-bit registers that control its behavior.

### 1. `DDRx` - Data Direction Register
* **Purpose**: Sets the direction (input or output) of each pin.
* **Configuration**:
    * `0` = **input**
    * `1` = **output**

### 2. `PORTx` – Pin Output Register
* **Purpose**: Has a dual role.
* **For Output Pins**: Writing a `1` or `0` drives the pin HIGH or LOW.
* **For Input Pins**: Writing a `1` **activates the internal pull-up resistor**.

### 3. `PINx` - Pin Input Register
* **Purpose**: Used to read the logical state (voltage level) of the pins.
* **Usage**: You read from this register to get input values.

**Links**: [[Configuring and Using GPIO Pins]], [[ATmega32 Basic I-O]]