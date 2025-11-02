# The `volatile` Keyword

**Tags:** #C-language #programming #interrupts #compiler

The `volatile` keyword is a type qualifier in C that tells the compiler that a variable's value can change at any time, without any action being taken by the code the compiler can see.

This is **absolutely essential** when sharing data between an Interrupt Service Routine (ISR) and the main program.

### Why is `volatile` Necessary?

Modern compilers are very aggressive with optimizations. If the compiler analyzes a section of code and sees that a variable is never changed within that code, it might make assumptions to generate faster or smaller machine code.

For example, consider this code:

```
// (Without volatile)
unsigned int counter = 0;

ISR(TIMER0_OVF_vect) {
    counter++; // This change is "invisible" to main()
}

int main(void) {
    // ... setup code ...
    while (counter < 100) {
        // Wait here
    }
    // Do something else
}
```

The compiler might look at the `while (counter < 100)` loop and notice that nothing _inside the loop_ changes `counter`. It might "optimize" this by assuming `counter` will always be 0, creating an infinite loop (`while (0 < 100)`), even though the ISR is changing the value in the background.

### How `volatile` Solves the Problem

By declaring the variable as `volatile`, you are giving a direct order to the compiler: "**Do not optimize this variable.** Every time my code reads this variable, you must fetch its value directly from memory. Every time my code writes to it, you must store the value directly to memory."

The corrected declaration looks like this:

```
volatile unsigned int counter = 0;
```

This guarantees that the `while` loop in `main()` will always read the most up-to-date value of `counter` from RAM—the same value that is being modified by the ISR—and the program will work as expected.

**Rule of Thumb**: Any global variable that is modified within an ISR and read outside of it **must** be declared `volatile`.

**Links**: [[Programming Interrupts in C]]