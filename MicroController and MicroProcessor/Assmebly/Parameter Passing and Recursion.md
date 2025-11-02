# Parameter Passing and Recursion

**Tags:** #assembly #functions #stack #recursion

Once you can call a procedure, the next step is to pass data (parameters) to it and get a value back. The stack is the primary mechanism for this.

### Passing Parameters via the Stack

The standard convention is to push parameters onto the stack _before_ making the `CALL`.

```
; Calling code
PUSH  param2        ; Push last parameter first
PUSH  param1
CALL  MY_PROC
```

Inside the procedure, the stack will look like this (from higher to lower memory):

- `param2`
    
- `param1`
    
- Return Address (pushed by `CALL`)
    

To access these parameters, we use the `BP` (Base Pointer) register as a stable reference point, because `SP` might move if we push more data.

**Standard Procedure Entry and Exit ("Prologue and Epilogue"):**

```
MY_PROC  PROC
    ; --- Prologue ---
    PUSH BP             ; 1. Save the old BP value
    MOV  BP, SP         ; 2. Set up our own stack frame pointer (BP now points to old BP)

    ; --- Body ---
    MOV  AX, [BP + 4]   ; Access param1 (BP + 2 is return address)
    MOV  BX, [BP + 6]   ; Access param2

    ; ... do work ...

    ; --- Epilogue ---
    POP  BP             ; 1. Restore the old BP value
    RET                 ; 2. Return to caller
MY_PROC  ENDP
```

- `[BP+2]` always holds the return address.
    
- `[BP+4]` holds the first parameter, `[BP+6]` the second, and so on.
    

### The Stack and Recursion

Recursion (a function calling itself) is possible _only because_ of the stack. Each time a recursive procedure is called, a new **activation record** (or stack frame) is created on the stack.

An activation record contains:

1. The parameters for that specific call.
    
2. The return address for that specific call.
    
3. The saved `BP` value from the previous call.
    
4. Space for any local variables.
    

**Simulation: `Factorial(3)`**

1. `main` calls `Factorial(3)`. An activation record is created for `n=3`.
    
2. Inside `Factorial(3)`, it calls `Factorial(2)`. A _new_ activation record for `n=2` is pushed on top of the first one.
    
3. Inside `Factorial(2)`, it calls `Factorial(1)`. A third activation record for `n=1` is pushed on top.
    
4. `Factorial(1)` hits the base case. It returns `1`. Its activation record is popped off.
    
5. Execution returns to `Factorial(2)`. It multiplies its parameter (`2`) by the return value (`1`) and returns `2`. Its activation record is popped off.
    
6. Execution returns to `Factorial(3)`. It multiplies its parameter (`3`) by the return value (`2`) and returns `6`. Its activation record is popped off.
    
7. Execution returns to `main`.
    

This elegant stacking and unstacking of activation records, managed by the `CALL`, `RET`, `PUSH BP`, and `POP BP` instructions, is the fundamental mechanism that enables complex procedural and recursive logic in almost all modern programming languages.

**Links:** [[Advanced Assembly Concepts]]