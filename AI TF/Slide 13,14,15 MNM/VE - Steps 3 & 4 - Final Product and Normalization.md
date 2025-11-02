# VE - Steps 3 & 4: Final Product and Normalization

_Source: `15. CSE317...pdf` (Pages 54-55)_

These are the final steps of the [[Variable Elimination Algorithm]] after all hidden variables have been eliminated.

## Step 3: Multiply Remaining Factors

After [[VE - Step 2 - Multiplication and Summing Out|eliminating all hidden variables]] (`E` and `A`), our factor list only contains factors of the query variable, `B`:

- $f_1(B) = P(B)$
    
- $f_9(B)$
    

We multiply all remaining factors together to get our final, unnormalized result, $f_{10}(B)$. $f_{10}(B) = f_1(B) \times f_9(B)$

- $f_{10}(T) = f_1(T) \times f_9(T) = 0.001 \times 0.592243 \approx 0.000592$
    
- $f_{10}(F) = f_1(F) \times f_9(F) = 0.999 \times 0.001493 \approx 0.001492$
    

This gives us the final factor $f_{10}(B)$: | B | Value | |---|---| | T | 0.000592 | | F | 0.001492 |

This $f_{10}(B)$ is $P(B, j, m)$, which is proportional to the $P(B|j,m)$ we want.

## Step 4: Normalize

The final factor $f_{10}(B)$ gives us the correct _ratio_ for $P(B|j,m)$, but the values don't sum to 1. **Normalization** is the process of dividing by the sum to make it a valid probability distribution.

1. **Sum the values**: $0.000592 + 0.001492 = 0.002084$
    
    - This sum is the normalizing constant $\alpha$, which is $P(j,m)$.
        
2. **Divide each entry by the sum**:
    
    - $P(B=T | j, m) = \frac{0.000592}{0.002084} \approx 0.284$
        
    - $P(B=F | j, m) = \frac{0.001492}{0.002084} \approx 0.716$
        

**Final Answer**: $P(B|j,m) = \langle 0.284, 0.716 \rangle$. The probability of a burglary, given both neighbors called, is 28.4%.

This completes the query.

### ❓ Review Questions

1. What does the final, unnormalized factor (like $f_{10}(B)$) represent?
    
2. If an unnormalized factor for a boolean variable `X` was $\langle 10, 30 \rangle$, what is the normalized probability distribution $P(X)$?