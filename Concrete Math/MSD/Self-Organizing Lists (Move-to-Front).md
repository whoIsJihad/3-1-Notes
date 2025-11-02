
## This is an Easier Note written by gpt [[ Move to Front -GPT]]
This note analyzes the **Move-to-Front (MTF)** list model. This is a self-organizing list algorithm where, upon an element being requested, it is moved to the front of the list.

**Goal:** Find the expected position of the _next_ element requested, assuming the process has been running for a long time (i.e., it is in a steady state).

## Model Assumptions

1. We have a list of $n$ elements, $e_1, \dots, e_n$.
    
2. At each step, element $e_i$ is requested with probability $P_i$, where $\sum_{i=1}^{n} P_i = 1$.
    
3. The event of _which_ element is selected is independent of the _current_ list configuration (position).
    

## Derivation of Expected Position

Let $E[Pos_{req}]$ be the expected position of the element that is requested.

$$E[Pos_{req}] = \sum_{i=1}^{n} E[\text{Position of } e_i | e_i \text{ is requested}] \cdot P(e_i \text{ is requested})$$

Using the independence assumption (3):

$$E[Pos_{req}] = \sum_{i=1}^{n} E[\text{Position of } e_i] \cdot P_i$$

Now, let's find $E[\text{Position of } e_i]$. We can define the position of $e_i$ using indicator variables. Let $I_j$ be an indicator variable for $j \neq i$: $I_j = 1$ if $e_j$ precedes $e_i$, and $0$ otherwise.

The position of $e_i$ is 1 (for itself) plus the count of all elements preceding it:

$$\text{Position of } e_i = 1 + \sum_{j \neq i} I_j$$

By linearity of expectation:

$$E[\text{Position of } e_i] = E\left[1 + \sum_{j \neq i} I_j\right] = 1 + \sum_{j \neq i} E[I_j]$$

The expectation of an indicator variable is just the probability of the event it indicates:

$$E[I_j] = P(e_j \text{ precedes } e_i)$$

**Key Insight (Steady State) [cite: PDF Page 3]:** In the steady state of the MTF algorithm, $e_j$ will precede $e_i$ if and only if the **most recent request for either** $e_i$ **or** $e_j$ was for $e_j$.

Therefore:

$$P(e_j \text{ precedes } e_i) = P(\text{request } e_j \mid \text{request was } e_i \text{ or } e_j)$$

Using the definition of conditional probability, $P(A|B) = P(A \cap B) / P(B)$:

$$P(e_j \text{ precedes } e_i) = \frac{P(e_j \text{ is requested})}{P(e_i \text{ is requested}) + P(e_j \text{ is requested})} = \frac{P_j}{P_i + P_j}$$

**Final Formula [cite: PDF Page 4]:** Substitute this back into the formula for $E[\text{Position of } e_i]$:

$$E[\text{Position of } e_i] = 1 + \sum_{j \neq i} \frac{P_j}{P_i + P_j}$$

And substitute _this_ into the main formula for $E[Pos_{req}]$:

$$E[Pos_{req}] = \sum_{i=1}^{n} P_i \left( 1 + \sum_{j \neq i} \frac{P_j}{P_i + P_j} \right)$$

This can be simplified:

$$E[Pos_{req}] = \sum_{i=1}^{n} P_i + \sum_{i=1}^{n} P_i \sum_{j \neq i} \frac{P_j}{P_i + P_j}$$

Since $\sum P_i = 1$:

$$E[Pos_{req}] = 1 + \sum_{i=1}^{n} \sum_{j \neq i} \frac{P_i P_j}{P_i + P_j}$$

## Additional Solved Problem (External)

- **Problem:** Consider a list of 3 elements $(A, B, C)$. The request probabilities are: $P_A = 0.6$, $P_B = 0.3$, and $P_C = 0.1$. Using the Move-to-Front algorithm, what is the expected position of the next requested element in the steady state?
    
- **Solution:**
    
    1. **Use the final formula:** $E[Pos_{req}] = 1 + \sum_{i=1}^{n} \sum_{j \neq i} \frac{P_i P_j}{P_i + P_j}$.
        
    2. **Note:** The sum $\sum_{i=1}^{n} \sum_{j \neq i}$ counts every pair twice (e.g., (A,B) and (B,A)). We can rewrite this as $2 \sum_{i < j}$.
        
        $$E[Pos_{req}] = 1 + 2 \sum_{i < j} \frac{P_i P_j}{P_i + P_j}$$
    3. **Identify the pairs** $(i, j)$ **where** $i < j$**:** (A,B), (A,C), (B,C).
        
    4. **Calculate the term** $\frac{P_i P_j}{P_i + P_j}$ **for each pair:**
        
        - (A, B): $\frac{P_A P_B}{P_A + P_B} = \frac{0.6 \times 0.3}{0.6 + 0.3} = \frac{0.18}{0.9} = 0.20$
            
        - (A, C): $\frac{P_A P_C}{P_A + P_C} = \frac{0.6 \times 0.1}{0.6 + 0.1} = \frac{0.06}{0.7} \approx 0.0857$
            
        - (B, C): $\frac{P_B P_C}{P_B + P_C} = \frac{0.3 \times 0.1}{0.3 + 0.1} = \frac{0.03}{0.4} = 0.0750$
            
    5. **Sum these terms and multiply by 2:**
        
        - $\text{Sum} = 2 \times (0.20 + 0.0857 + 0.0750) = 2 \times (0.3607) \approx 0.7214$
            
    6. **Add 1:**
        
        - $E[Pos_{req}] = 1 + 0.7214 = 1.7214$.
            
    
    - **Answer:** The expected position of the next requested item is approximately 1.72. This makes sense, as the most likely item (A, at 60%) will be at position 1 most of the time.
    