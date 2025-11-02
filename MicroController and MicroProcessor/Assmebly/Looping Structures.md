

**Tags:** #assembly #control_flow #loops

Loops are fundamental control structures for repeating a block of code. Assembly provides both a specialized instruction for simple loops (`LOOP`) and the building blocks (`CMP`, `JMP`) to create more complex loops like `WHILE` and `REPEAT-UNTIL`.

### The `LOOP` Instruction (FOR Loop)

The `LOOP` instruction is designed for creating simple, count-down loops. It uses the `CX` register as its built-in counter.

- **Syntax:** `LOOP destination_label`
    
- **Action:** `LOOP` performs two actions in one instruction:
    
    1. It automatically decrements the `CX` register by 1.
        
    2. If `CX` is **not zero** after the decrement, it jumps to the `destination_label`.
        

**C++ Equivalent (FOR Loop):**

```
for (int cx = 80; cx > 0; cx--) {
    // loop body
}
```

**Assembly Implementation:**

```
    MOV CX, 80      ; Initialize the counter

TOP_OF_LOOP:
    ; ... body of the loop ...
    LOOP TOP_OF_LOOP
```

**Caution:** The `LOOP` instruction is a "bottom-tested" loop. It decrements and checks _after_ the body runs. This means if you start with `CX = 0`, the loop will execute 65,536 times! To prevent this, you can check `CX` before entering the loop: `JCXZ SKIP_LOOP` (Jump if CX is Zero).

### WHILE Loop

A `WHILE` loop is a "top-tested" loop: the condition is checked before the body is executed. **Implementation:**

1. Check the condition.
    
2. If the condition is false, jump to the end of the loop.
    
3. Execute the loop body.
    
4. Jump unconditionally back to the start to re-check the condition.
    

**C++ Equivalent:**

```
while (al != '\r') {
    // loop body
}
```

**Assembly Implementation:**

```
WHILE_START:
    CMP AL, 0Dh         ; Is AL equal to carriage return?
    JE  END_WHILE       ; If equal, exit the loop

    ; ... loop body ...

    JMP WHILE_START     ; Go back to the top to check again

END_WHILE:
```

### REPEAT-UNTIL Loop

A `REPEAT-UNTIL` loop is a "bottom-tested" loop: the body always executes at least once, and the condition is checked at the end. **Implementation:**

1. Execute the loop body.
    
2. Check the condition.
    
3. If the condition is false, jump back to the start of the loop body.
    

**Pascal/Delphi Equivalent:**

```
repeat
  // loop body
until al = ' ';
```

**Assembly Implementation:**

```
REPEAT_START:
    ; ... loop body ...

    CMP AL, ' '         ; Is AL equal to a space?
    JNE REPEAT_START    ; If Not Equal, loop again
```

**Links:** [[Advanced Assembly Concepts]]