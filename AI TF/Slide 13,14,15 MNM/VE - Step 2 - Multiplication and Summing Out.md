# VE - Step 2: Multiplication and Summing Out

_Source: `15. CSE317...pdf` (Pages 48-53)_

This is the main loop of the [[Variable Elimination Algorithm]]. We repeat this two-part step for each **hidden variable**. For our query $P(B|j,m)$, the hidden variables are `E` and `A`. Let's pick the elimination order E, then A.

## 1. Eliminate `E`

### (2a) Multiply Factors

First, we find all factors that involve `E`: $f_2(E)$ and $f_3(A,B,E)$. We multiply them to get a new, larger factor, $f_6(A,B,E)$.

**Factor Multiplication** is a **point-wise product**:

- The new factor $f_6(A,B,E) = f_2(E) \times f_3(A,B,E)$ will have variables $A$, $B$, and $E$.
    
- For each row (e.g., $A=T, B=T, E=T$), the new value is the product of the matching values from the original factors.
    
    - $f_6(T,T,T) = f_2(T) \times f_3(T,T,T) = 0.002 \times 0.95 = 0.0019$
        
    - $f_6(T,T,F) = f_2(F) \times f_3(T,T,F) = 0.998 \times 0.94 = 0.93812$
        
- (See page 50 for the full $f_6$ table).
    

### (2b) Sum Out `E`

Now, we eliminate `E` from $f_6(A,B,E)$ by summing it out. This creates a new factor $f_7(A,B)$ that doesn't include `E`.

- For each combination of the remaining variables (e.g., $A=T, B=T$), we sum the values from $f_6$ for all possible values of `E` ( $E=T$ and $E=F$).
    
    - $f_7(T,T) = f_6(T,T,T) + f_6(T,T,F) = 0.0019 + 0.93812 = 0.94002$
        
    - $f_7(T,F) = f_6(T,F,T) + f_6(T,F,F) = 0.00058 + 0.000998 = 0.001578$
        
- (See page 51 for the full $f_7$ table).
    

**Factors list is now:** $f_1(B)$, $f_4(A)$, $f_5(A)$, $f_7(A,B)$.

## 2. Eliminate `A`

### (2a) Multiply Factors

Find all factors with `A`: $f_4(A)$, $f_5(A)$, and $f_7(A,B)$. Multiply them to get $f_8(A,B)$.

- $f_8(A,B) = f_4(A) \times f_5(A) \times f_7(A,B)$
    
- $f_8(T,T) = f_4(T) \times f_5(T) \times f_7(T,T) = 0.90 \times 0.70 \times 0.94002 = 0.592213$
    
- (See page 52 for the full $f_8$ table).
    

### (2b) Sum Out `A`

Sum out `A` from $f_8(A,B)$ to get $f_9(B)$.

- $f_9(T) = f_8(T,T) + f_8(F,T) = 0.592213 + 0.00002999 \approx 0.592243$
    
- $f_9(F) = f_8(T,F) + f_8(F,F) = 0.00099414 + 0.000499211 \approx 0.001493$
    
- (See page 53 for the full $f_9$ table).
    

**Factors list is now:** $f_1(B)$, $f_9(B)$. We are done with elimination.

### ❓ Review Questions

1. What does "point-wise multiplication" of two factors, $f_1(A,B)$ and $f_2(B,C)$, mean? What would the resulting factor's variables be?
    
2. What does it mean to "sum out" a variable? If you have $f(A,B,C)$ and you sum out `B`, what are the variables of the resulting factor?