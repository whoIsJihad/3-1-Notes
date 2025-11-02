# Value Iteration

_Source: `21. Making complex decisions- nidhi.pdf` (Pages 37, 40-44)_

**Value Iteration** is the "classic" algorithm for solving a [[Markov Decision Processes (MDPs)|Markov Decision Process]]. Its goal is to find the optimal utility $U(s)$ for every state $s$.

It works by turning [[The Bellman Equation]] into an iterative update rule.

## The Problem

[[The Bellman Equation]] gives us a set of $n$ (number of states) non-linear equations with $n$ unknowns (the $U(s)$ for each state). $U(s) = R(s) + \gamma \max_{a} \sum_{s'} P(s' | s, a) U(s')$

We can't solve this directly.

## The Algorithm

Value Iteration solves this by starting with a "guess" for the utilities and then repeatedly applying the Bellman equation as an update rule until the values stop changing (i.e., they converge).

1. **Initialize**: Create a utility vector $U_0$ and set $U_0(s) = 0$ for all states $s$. Set iteration $i=0$.
    
2. **Iterate**: Start a loop.
    
    - $i = i + 1$.
        
    - Create a _new_ utility vector $U_{i+1}$.
        
    - For _every_ state $s$:
        
        - Calculate the new utility $U_{i+1}(s)$ using the values from the _previous_ iteration $U_i$.
            
        - This is the **Bellman Update**: $U_{i+1}(s) \leftarrow R(s) + \gamma \max_{a \in A(s)} \left[ \sum_{s'} P(s' | s, a) U_i(s') \right]$
            
3. **Check for Convergence**:
    
    - Calculate the maximum change: $\delta = \max_{s} |U_{i+1}(s) - U_i(s)|$.
        
    - If $\delta$ is very small (e.g., $<\epsilon$), stop. The utilities have converged.
        
    - Otherwise, go back to Step 2.
        
4. **Return**: The final utility vector $U(s)$ is the optimal utility function $U^*(s)$.
    

Once you have the final $U(s)$ values, you can extract the optimal policy $\pi^*(s)$ by (for each state $s$) choosing the action $a$ that maximizes the `max` part of the equation: $\pi^*(s) = \arg\max_{a \in A(s)} \left[ \sum_{s'} P(s' | s, a) U(s') \right]$

### ❓ Review Questions

1. What is the "Bellman Update"? What values are on the left side of the arrow, and what values are on the right?
    
2. How does Value Iteration start (i.e., what is the initial guess for all utilities)?
    
3. When does the algorithm stop?