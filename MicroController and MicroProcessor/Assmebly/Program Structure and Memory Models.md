# Program Structure and Memory Models

**Tags:** #assembly #programming #memory_management

An 8086 assembly program is not just a list of instructions; it must be organized into segments that tell the assembler and operating system how to manage its code, data, and stack.

### Memory Models

The first thing you define is the memory model. This is a shorthand that tells the assembler about the size and segmentation of your program. For most simple programs, the `SMALL` model is sufficient.

- **.MODEL Directive**
    
    - **Syntax:** `.MODEL memory_model`
        
    - **`SMALL` Model:** All your code fits into a single 64 KB segment, and all your data fits into a single 64 KB segment.
        

### Program Segments

Every assembly program is built around three main segments:

1. **The Stack Segment**
    
    - **Purpose:** A region of memory used for temporarily storing data, such as function return addresses and local variables.
        
    - **Directive:** `.STACK size_in_bytes`
        
    - **Example:** `.STACK 100h` reserves 256 bytes for the stack. If the size is omitted, a default of 1 KB is used.
        
2. **The Data Segment**
    
    - **Purpose:** This is where you declare all your variables and constants.
        
    - **Directive:** `.DATA`
        
    - **Example:**
        
        ```
        .DATA
        message   DB  'Hello!', '$'
        my_var    DW  ?
        ```
        
3. **The Code Segment**
    
    - **Purpose:** This is where all your executable instructions go.
        
    - **Directive:** `.CODE`
        
    - The main procedure of your program is defined within this segment.
        

### A Complete Program Skeleton

Putting it all together, a basic assembly program for DOS using `emu8086` will have this structure:

```
; 1. Define the memory model
.MODEL SMALL

; 2. Define the stack size
.STACK 100h

; 3. Define all variables in the data segment
.DATA
; (your variable definitions go here)

; 4. Write all instructions in the code segment
.CODE
MAIN PROC  ; Start of the main procedure

    ; --- BOILERPLATE START ---
    ; Initialize the Data Segment (DS) register
    MOV AX, @DATA
    MOV DS, AX
    ; --- BOILERPLATE END ---

    ; Your actual program logic goes here

    ; --- BOILERPLATE START ---
    ; Exit the program and return control to DOS
    MOV AH, 4Ch
    INT 21h
    ; --- BOILERPLATE END ---

MAIN ENDP  ; End of the main procedure
END MAIN   ; End of the entire program, specifies the entry point
```

The **boilerplate** code is essential. The `MOV DS, AX` lines are required because the `DS` register does not automatically point to your data segment; you must initialize it manually. The final two lines are the standard way to exit a program cleanly.

**Links:** [[Introduction to Assembly Language]]