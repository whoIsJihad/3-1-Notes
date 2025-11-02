# The Bellman Equation

_Source: `21. Making complex decisions- nidhi.pdf` (Pages 32-34, 38)_

The Bellman Equation is the most important equation in [[Markov Decision Processes (MDPs)|MDPs]]. It is a recursive equation that defines the utility of a state in terms of the utilities of its successor states.

It's based on a simple, powerful idea:

> The utility of being in a state $s$ is the **immediate reward** you get $R(s)$, _plus_ the **expected discounted utility** of whatever state $s'$ you land in next (assuming you act optimally).

## The Equation for Optimal Utility $U(s)$

Let $U(s)$ be the utility of state $s$, assuming we are following the optimal policy $\pi^*$.

The optimal policy $\pi^*(s)$ will choose the action $a$ that **maximizes** the expected utility of the next step.

- The "next step" utility is: $\sum_{s'} P(s' | s, a) U(s')$
    
    - This is a weighted average. We sum up the utility of each possible next state $s'$, weighted by the probability of landing in that state $s'$.
        

Combining these, we get the **Bellman Equation**:

> $U(s) = R(s) + \gamma \max_{a \in A(s)} \left[ \sum_{s'} P(s' | s, a) U(s') \right]$

Let's break this down:

- $U(s)$: The utility of our _current_ state (what we want to find).
    
- $R(s)$: The immediate reward for being in this state.
    
- $\gamma$: The [[Utility and Rewards (Discounting)|discount factor]] (e.g., 0.9).
    
- $\max_{a \in A(s)}$: The "optimal" part. We choose the _best_ action $a$ available.
    
- $\sum_{s'} P(s' | s, a) U(s')$: The expected utility of the _next_ state, given we took action $a$.
    

## Bellman Equation for a _Fixed_ Policy

If we aren't acting optimally, but are just following some fixed, pre-defined policy $\pi$, the $\max$ operation disappears. We just do what $\pi$ tells us to do.

> $U^{\pi}(s) = R(s) + \gamma \sum_{s'} P(s' | s, \pi(s)) U^{\pi}(s')$

This is a simpler, _linear_ set of equations (one for each state). This equation is used in the "policy evaluation" step of [[Policy Iteration]].

The Bellman equation for optimal utility $U(s)$ is _non-linear_ (because of the `max` operation). We can't solve it with simple linear algebra. This is why we need iterative algorithms like [[Value Iteration]].

### ❓ Review Questions

1. In your own words, what is the Bellman equation trying to express?
    
2. What is the one and only difference between the Bellman equation for an _optimal_ policy $U(s)$ and the one for a _fixed_ policy $U^{\pi}(s)$?
    
3. Why is the Bellman equation for $U(s)$ "non-linear"?