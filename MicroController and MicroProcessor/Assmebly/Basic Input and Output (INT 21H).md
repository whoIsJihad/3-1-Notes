# Basic Input and Output (INT 21H)

**Tags:** #assembly #interrupts #dos #io

In a high-level language, you have simple functions like `printf` or `cin`. In assembly, you don't have these. To communicate with hardware like the keyboard and screen, you must ask the **Operating System** to do it for you. In MS-DOS, this is done using **software interrupts**.

An interrupt temporarily halts the CPU, saves its current state, and jumps to a special OS routine called an **Interrupt Service Routine (ISR)** to handle a specific task. The `INT` instruction triggers a software interrupt.

The most important interrupt for basic I/O is **`INT 21h`**, the main DOS API.

### How to Use `INT 21h`

Using `INT 21h` is a simple two-step process:

1. Load a **function number** into the `AH` register. This number tells DOS what specific service you want (e.g., "read a key," "print a character").
    
2. Call `INT 21h`.
    

DOS will perform the requested action and then return control to your program.

### Key `INT 21h` Functions

**Function 1: Read a Single Character from Keyboard**

- **Setup:** `MOV AH, 1`
    
- **Action:** The program will wait for the user to press a key.
    
- **Result:** The ASCII code of the pressed key is returned in the `AL` register.
    

**Function 2: Display a Single Character**

- **Setup:**
    
    - `MOV AH, 2`
        
    - `MOV DL, character_to_display` (The character must be in `DL`)
        
- **Action:** Prints the character in `DL` to the console.
    
- **Example:** To print the letter 'A':
    
    ```
    MOV AH, 2
    MOV DL, 'A'  ; or MOV DL, 41h
    INT 21h
    ```
    

**Function 9: Display a String**

- **Setup:**
    
    - `MOV AH, 9`
        
    - `LEA DX, string_variable` (The **offset address** of the string must be in `DX`)
        
- **Important Rule:** The string in memory **must** be terminated with a dollar sign character (`$`). This is how DOS knows where the string ends.
    
- **Example:**
    
    ```
    .DATA
    my_message  DB  'Hello World!', '$'
    
    .CODE
    ...
    MOV AH, 9
    LEA DX, my_message  ; Load the address of the message into DX
    INT 21h
    ```
    

**Function 4Ch: Terminate Program**

- **Setup:** `MOV AH, 4Ch`
    
- **Action:** This is the standard way to end your program and return control gracefully to the DOS command prompt.
    

**Links:** [[Introduction to Assembly Language]]