# Variables and Data Definition

**Tags:** #assembly #variables #memory_management

In assembly, a "variable" is simply a named location in memory. You declare variables in the `.DATA` segment of your program using **data definition directives**. These directives tell the assembler to allocate a certain amount of memory and optionally give it an initial value.

### Data Definition Directives

These are the primary pseudo-ops for defining data:

|Directive|Description|Size Allocated|
|---|---|---|
|`DB`|Define Byte|1 Byte|
|`DW`|Define Word|2 Bytes|
|`DD`|Define Double Word|4 Bytes|

### Syntax

The general syntax for defining a variable is:

```
variable_name   directive   initial_value(s)
```

- **`variable_name`:** An optional label for the memory location.
    
- **`directive`:** `DB`, `DW`, etc.
    
- **`initial_value(s)`:** The value(s) to store in memory.
    
    - You can list multiple values separated by commas to create an array.
        
    - Use a question mark (`?`) to leave the memory uninitialized.
        

### Examples

**Defining Single Variables:**

```
; Define a byte named 'my_byte' with an initial value of 10
my_byte     DB    10

; Define a word named 'my_word' with the hex value 1234h
my_word     DW    1234h

; Define a word named 'user_age' but leave its value uninitialized
user_age    DW    ?

; Define a character variable
letter_a    DB    'A'
```

**Defining Arrays:**

```
; Define an array of bytes
byte_array  DB    10, 20, 30, 40

; Define an array of words
word_array  DW    1000h, 2000h, 3000h

; Define a string (which is an array of characters)
; The '$' character is often used to mark the end of a string for printing
message     DB    'Hello, World!', '$'
```

### Named Constants with `EQU`

Sometimes you want to give a symbolic name to a constant value, not a memory location. The `EQU` (equate) directive does this. The assembler will replace every occurrence of the name with its value during assembly.

- **This does not allocate any memory.**
    

**Syntax:**

```
constant_name   EQU   value
```

**Example:**

```
LINE_FEED   EQU   0Ah      ; Give the name LINE_FEED to the ASCII line feed character
MOV   DL, LINE_FEED      ; The assembler treats this as MOV DL, 0Ah
```

**Links:** [[Introduction to Assembly Language]]