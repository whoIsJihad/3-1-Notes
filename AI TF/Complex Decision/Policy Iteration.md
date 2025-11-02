# Policy Iteration

_Source: `21. Making complex decisions- nidhi.pdf` (Pages 45-50)_

**Policy Iteration** is an alternative algorithm for solving [[Markov Decision Processes (MDPs)|MDPs]]. It often converges much faster than [[Value Iteration]].

Instead of iterating on the _utility values_, Policy Iteration iterates on the _policy itself_.

## The Algorithm

Policy Iteration alternates between two steps: "Policy Evaluation" and "Policy Improvement."

1. **Initialize**:
    
    - Start with a random policy, $\pi_0$.
        
    - Initialize a utility vector $U_0$ (e.g., all zeros).
        
2. **Iterate (Loop until policy is stable):**
    
    - **Step A: Policy Evaluation**
        
        - We have a fixed policy $\pi_i$. We need to find out how good it is.
            
        - Calculate the utility $U_i(s) = U^{\pi_i}(s)$ for _every state_ $s$ under this fixed policy.
            
        - We do this by solving the _simpler, linear_ version of the Bellman equation: $U_i(s) = R(s) + \gamma \sum_{s'} P(s' | s, \pi_i(s)) U_i(s')$
            
        - (This is a set of $n$ linear equations with $n$ unknowns, which can be solved with linear algebra, or more commonly, by running a "modified" value iteration loop until it converges).
            
    - **Step B: Policy Improvement**
        
        - Now that we have the utilities $U_i$ for our old policy, we try to find a _better_ policy, $\pi_{i+1}$.
            
        - For _every_ state $s$, we find the action $a$ that _would be best_, given the utilities $U_i$ we just calculated: $\pi_{i+1}(s) \leftarrow \arg\max_{a \in A(s)} \left[ \sum_{s'} P(s' | s, a) U_i(s') \right]$
            
    - **Step C: Check for Convergence**
        
        - If $\pi_{i+1} = \pi_i$ (the policy didn't change for any state), then we are done. We have found the optimal policy $\pi^*$.
            
        - Otherwise, go back to Step A with the new policy $\pi_{i+1}$.
            

## Value Iteration vs. Policy Iteration

- **Value Iteration**: Performs _one_ Bellman update (which includes the `max`) for all states, then repeats. It "mixes" the utility calculation and the `max` (policy) step.
    
- **Policy Iteration**:
    
    1. **Evaluation**: Fully solves for the utilities of the _current_ policy (a potentially long inner loop).
        
    2. **Improvement**: Finds a _new_ best policy based on those utilities (a single, fast step).
        
    
    - This is often faster because the policy converges in fewer _outer_ iterations than the utility values do.
        

### ❓ Review Questions

1. What are the two alternating steps in Policy Iteration?
    
2. In the "Policy Evaluation" step, why is the Bellman equation _linear_ (no `max` operation)?
    
3. How does the "Policy Improvement" step use the utilities $U_i$ from the evaluation step?