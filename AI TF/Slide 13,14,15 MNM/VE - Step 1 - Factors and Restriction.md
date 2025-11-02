# VE - Step 1: Factors and Restriction

_Source: `15. CSE317...pdf` (Pages 44-47)_

This is the initialization phase of the [[Variable Elimination Algorithm]].

## 1. Create Factors

First, we express our joint probability as a product of initial **factors**. A factor is just a table that maps variable assignments to a number (like a CPT).

For the query $P(B|j,m)$, the joint probability is: $P(B,E,A,J,M) = P(B)P(E)P(A|B,E)P(J|A)P(M|A)$

This gives us five initial factors:

- $f_1(B) = P(B)$
    
- $f_2(E) = P(E)$
    
- $f_3(A,B,E) = P(A|B,E)$
    
- $f_4(J,A) = P(J|A)$
    
- $f_5(M,A) = P(M|A)$
    

## 2. Restrict (Instantiate) Evidence

Next, we "restrict" the factors that include our evidence variables ($J=true$ and $M=true$).

This means we take the original factor and create a new, smaller factor by:

1. Keeping only the rows that match the evidence.
    
2. Removing the evidence variable from the factor's arguments.
    

**Example 1: Restricting** $f_4(J,A)$ **for** $J=true$

- **Original Factor** $f_4(J,A)$: | J | A | Value | |---|---|---| | T | T | 0.90 | | T | F | 0.05 | | F | T | 0.10 | | F | F | 0.95 |
    
- **New Factor** $f_4(A)$ (keeping only $J=T$ rows): | A | Value | |---|---| | T | 0.90 | | F | 0.05 |
    

**Example 2: Restricting** $f_5(M,A)$ **for** $M=true$

- **Original Factor** $f_5(M,A)$: | M | A | Value | |---|---|---| | T | T | 0.70 | | T | F | 0.01 | | F | T | 0.30 | | F | F | 0.99 |
    
- **New Factor** $f_5(A)$ (keeping only $M=T$ rows): | A | Value | |---|---| | T | 0.70 | | F | 0.01 |
    

After this step, our list of factors is: $f_1(B)$, $f_2(E)$, $f_3(A,B,E)$, $f_4(A)$, $f_5(A)$. We are now ready for [[VE - Step 2 - Multiplication and Summing Out|Step 2]].

### ❓ Review Questions

1. What is a "factor"? How is it different from a CPT?
    
2. If we had the evidence $Alarm=false$ (i.e., $A=F$), what would the new factor $f_4(J)$ (derived from $f_4(J,A)$) look like?