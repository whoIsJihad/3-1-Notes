
_Source: `21. Making complex decisions- nidhi.pdf` (Pages 19-24)_

A "solution" to a [[Markov Decision Processes (MDPs)|Markov Decision Process]] is not a simple plan (like `UP, UP, RIGHT`). Because the world is stochastic, we might end up in any state. A solution must tell us what to do _for every possible state_.

This solution is called a **policy**.

## What is a Policy?

- A policy, denoted $\pi$, is a mapping from states to actions. It's a "strategy" or a "lookup table."
    
- $\pi(s) \rightarrow a$
    
- It answers the question: "When I am in state $s$, what action $a$ should I take?"
    
- An agent "executing" a policy $\pi$ just looks at its current state $s$, finds $\pi(s)$, and performs that action.
    

## What is an _Optimal_ Policy?

- Because the world is stochastic, executing the same policy $\pi$ from the same start state $s$ can result in different state sequences and different total utilities.
    
- We can't judge a policy on one run. We must judge it by its **expected utility**.
    
- The **Optimal Policy,** $\pi^*$, is the policy that yields the **highest expected utility** if you start from any given state $s$.
    
- $U(s)$ (with no $\pi$ superscript) is defined as the utility of the _optimal_ policy, $U^{\pi^*}(s)$. It's the _best possible expected utility_ you can get starting from state $s$.
    

### How Rewards Shape the Policy

The optimal policy $\pi^*$ is _extremely_ sensitive to the [[Utility and Rewards (Discounting)|Reward Model $R(s)$]]. The agent will do _whatever_ it takes to maximize its expected utility.

- **Case 1:** $R(s) = -0.04$ **(Slightly painful life)**
    
    - The agent is penalized for every step. It takes the "safe" route to the +1 reward, even if it's longer.
        
    - It steers _far away_ from the -1 state, because the small step penalty is better than the risk of falling in.
        
    - _See (3,1)_: It moves `LEFT` rather than `UP`, to avoid the risk of slipping into (4,2).
        
- **Case 2:** $R(s) = -1.6284$ **(Very painful life)**
    
    - The step penalty is so high that it's _worse_ than the -1 terminal state.
        
    - The agent's optimal policy is to end the game as fast as possible, even if it means going to the -1 state!
        
    - _See (3,2)_: It moves `RIGHT` to jump into the -1 state and end its suffering.
        
- **Case 3:** $R(s) = -0.001$ **(Boring life)**
    
    - The step penalty is tiny. The agent is happy to wander around, taking big risks, as long as it generally heads toward +1.
        

Finding this $\pi^*$ is the central goal of solving an MDP. We do this using [[Value Iteration]] or [[Policy Iteration]], which are based on [[The Bellman Equation]].

### ❓ Review Questions

1. What is a policy $\pi$? How is it different from a plan (a sequence of actions)?
    
2. What does it mean for a policy to be "optimal"?
    
3. Why does the optimal policy change when the step reward $R(s)$ changes?