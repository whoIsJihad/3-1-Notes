# Markov Decision Processes (MDPs)

_Source: `21. Making complex decisions- nidhi.pdf` (Pages 16-17)_

A **Markov Decision Process (MDP)** is the formal mathematical framework for a [[Sequential Decision Problems|sequential decision problem]] where the environment is:

1. **Fully Observable**: The agent always knows what state $s$ it is in (e.g., it knows it's at grid cell (1,1)).
    
2. **Stochastic**: The outcomes of actions are probabilistic.
    

## Components of an MDP

An MDP is defined by four (or five) components:

1. **A set of States** $S$: (e.g., all the non-wall grid cells). Includes an initial state $s_0$.
    
2. **A set of Actions** $A(s)$: A set of actions available in each state $s$ (e.g., `UP, DOWN, LEFT, RIGHT`).
    
3. **A Transition Model** $P(s' | s, a)$:
    
    - This is the "physics" of the world. It gives the probability of _landing_ in state $s'$ after taking action $a$ from state $s$.
        
    - _Example_: $P((1,2) | (1,1), \text{UP}) = 0.8$
        
    - _Example_: $P((2,1) | (1,1), \text{UP}) = 0.1$
        
4. **A Reward Model** $R(s)$:
    
    - This gives the reward (or penalty) for _entering_ a state $s$.
        
    - _Example_: $R((4,3)) = +1$, $R((4,2)) = -1$.
        
    - _Example_: $R(s) = -0.04$ for all other states. This is a "cost of living" penalty that encourages the agent to finish quickly.
        

(A fifth component, **Discount Factor** $\gamma$, is also crucial, as seen in [[Utility and Rewards (Discounting)|Utility and Rewards]].)

## The Markov Property

The transition model $P(s' | s, a)$ is **Markovian**. This is a _critical_ assumption.

> **The Markov Property**: The probability of the next state $s'$ depends _only_ on the current state $s$ and the action $a$, and _not_ on any of the history of states and actions that came before.

$P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, ..., s_0) = P(s_{t+1} | s_t, a_t)$

This makes the problem solvable. We don't need to know the whole past to predict the future; we just need to know where we are _now_.

The "solution" to an MDP is called a [[Policies (Optimal Policy)|Policy]].

### ❓ Review Questions

1. What are the four main components of an MDP?
    
2. What is the "Markov Property" in your own words? Why is it important?
    
3. What is the difference between the _Transition Model_ $P(s' | s, a)$ and the _Reward Model_ $R(s)$?