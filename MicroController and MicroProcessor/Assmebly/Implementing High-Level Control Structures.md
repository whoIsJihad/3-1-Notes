
**Tags:** #assembly #control_flow #programming_patterns

High-level control structures like `IF-THEN-ELSE` and loops can be constructed in assembly using `CMP` and a combination of conditional and unconditional jumps.

### IF-THEN Structure

**Logic:** If a condition is true, execute a block of code.
**Implementation:** Use a conditional jump that **skips** the code block if the condition is _false_.

**C++ Code:**

```
if (ax >= bx) {
    // then-block
    ax = 0;
}
// code continues here
```

**Assembly Implementation:**

```
    CMP AX, BX          ; Compare AX and BX
    JL  SKIP_IF         ; If AX is Less than BX, jump over the 'then' block

; then-block:
    MOV AX, 0           ; This code only runs if AX >= BX

SKIP_IF:
    ; Code continues here
```

### IF-THEN-ELSE Structure

**Logic:** If a condition is true, execute one block; otherwise, execute a different block. **Implementation:** Use a conditional jump to the `ELSE` block, and an unconditional `JMP` to skip the `ELSE` block after the `THEN` block is done.

**C++ Code:**

```
if (al <= bl) {
    // then-block
} else {
    // else-block
}
```

**Assembly Implementation:**

```
    CMP AL, BL          ; Compare AL and BL
    JNBE ELSE_BLOCK     ; If Not Below or Equal (i.e., AL > BL), jump to ELSE

; then-block:
    ; Code for the 'then' case...
    JMP END_IF          ; Unconditionally jump to the end

ELSE_BLOCK:
    ; Code for the 'else' case...

END_IF:
    ; Code continues here
```

### CASE Structure (Switch-Case)

A multi-way branch can be implemented as a series of `CMP` and `JE` instructions.

**C++ Code:**

```
switch (al) {
    case 1: // ...
        break;
    case 3: // ...
        break;
}
```

**Assembly Implementation:**

```
    CMP AL, 1
    JE  CASE_1

    CMP AL, 3
    JE  CASE_3

    JMP END_CASE        ; Default case (optional)

CASE_1:
    ; Code for case 1...
    JMP END_CASE

CASE_3:
    ; Code for case 3...

END_CASE:
    ; Code continues here
```

This pattern of "test the opposite and jump" is fundamental to translating high-level logic into low-level assembly.

**Links:** [[Advanced Assembly Concepts]]