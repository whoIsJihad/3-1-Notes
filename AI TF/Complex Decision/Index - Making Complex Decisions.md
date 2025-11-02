
This module covers how an agent can make a sequence of optimal decisions in an environment that is uncertain or stochastic. This is the core of **planning** under uncertainty and forms the basis for reinforcement learning.

This topic moves from simple "one-shot" decisions to **Sequential Decision Problems**.

## Core Concepts

- [[Sequential Decision Problems]]: What makes a decision "complex" or "sequential"?
    
- [[Markov Decision Processes (MDPs)]]: The formal framework for defining these problems.
    
- [[Policies (Optimal Policy)]]: What is a "solution" to an MDP?
    
- [[Utility and Rewards (Discounting)]]: How do we calculate the total utility of a sequence of actions, especially if it's infinite?
    
- [[The Bellman Equation]]: The fundamental equation that connects the utility of a state to the utility of its neighbors.
    

## Solution Algorithms

These are the two classic algorithms used to _find_ the optimal policy by solving the Bellman equations.

- [[Value Iteration]]
    
- [[Policy Iteration]]