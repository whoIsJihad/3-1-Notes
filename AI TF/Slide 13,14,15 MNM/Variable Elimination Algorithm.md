# Variable Elimination Algorithm

_Source: `15. CSE317...pdf` (Pages 41-44)_

The **Variable Elimination (VE) Algorithm** is the standard method for performing exact [[Inference in Bayesian Networks|inference]].

Its main goal is to efficiently compute the "sum of products" (like $\sum_{a} \sum_{e} P(j|a)...P(e)$) without the exponential blowup of the naive approach.

It solves the problem of repeated sub-expression evaluation (like $P(j|a)P(m|a)$ being computed twice) by using **dynamic programming**. It stores intermediate results (called "factors") and reuses them.

## The VE Algorithm Steps

The algorithm proceeds in a series of steps to compute a query like $P(B | j, m)$.

1. [[VE - Step 1 - Factors and Restriction|Create Factors and Restrict Evidence]]: Convert all CPTs into "factors" and set the evidence variables to their observed values.
    
2. [[VE - Step 2 - Multiplication and Summing Out|Eliminate Hidden Variables]]: For each hidden variable (in some order):
    
    - (2a) **Multiply** all factors that involve this variable.
        
    - (2b) **Sum out** the variable from the resulting factor.
        
3. [[VE - Steps 3 & 4 - Final Product and Normalization|Multiply Remaining Factors]]: After all hidden variables are gone, multiply any factors that are left.
    
4. [[VE - Steps 3 & 4 - Final Product and Normalization|Normalize]]: The result is a factor over the query variable. Normalize it to get the final probability distribution.
    

### Irrelevant Variables

A key optimization is that VE can automatically handle irrelevant variables.

- **Rule**: Any variable that is not an **ancestor** of a query variable or an evidence variable is irrelevant to the query.
    
- **Example**: In $P(J|b)$, the `MaryCalls` node is a leaf node and not evidence or query. The term $\sum_{m}P(m|a)$ will just evaluate to 1 and be eliminated.
    

### ⚠️ Complexity

- Finding the _optimal ordering_ of variables to eliminate is NP-Hard.
    
- The complexity of VE is determined by the size of the largest factor created during the process.
    

### ❓ Review Questions

1. What is the main problem with "naive" inference that Variable Elimination solves?
    
2. What does it mean to say that finding the optimal ordering is "NP-Hard"?