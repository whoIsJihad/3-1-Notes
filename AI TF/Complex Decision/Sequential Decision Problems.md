# Sequential Decision Problems

_Source: `21. Making complex decisions- nidhi.pdf` (Pages 8-13)_

## Simple vs. Sequential Decisions

- **Simple Decision**: A "one-shot" choice. You calculate the expected utility of each option and pick the best one. The problem is then over.
    
    - _Example_: Choosing which breakfast to have.
        
- **Sequential Decision**: You must make a _sequence_ of actions. The utility of an action now depends on the actions you plan to take in the future. The future, in turn, depends on what you do now.
    
    - _Example_: Navigating a grid world to find a prize.
        

## The Grid World Example

This is the classic problem used to explain sequential decisions.

- **Environment**: A $4 \times 3$ grid.
    
- **Start State**: (1, 1)
    
- **Terminal States**: (4, 3) with a reward of +1 (win) and (4, 2) with a reward of -1 (lose).
    
- **The Problem**: The agent's actions are **stochastic** (not deterministic).
    

### Stochastic Actions

- If this were a simple search problem (deterministic actions), the solution would be a fixed plan, like `UP, UP, RIGHT, RIGHT, RIGHT`.
    
- But here, actions are uncertain. If the agent chooses `UP`:
    
    - **0.8 probability** it moves `UP`.
        
    - **0.1 probability** it moves `LEFT` (at a right angle).
        
    - **0.1 probability** it moves `RIGHT` (at a right angle).
        
- If it hits a wall, it stays in the same place.
    

**Why Search Fails:** A simple action sequence (a "plan") is not a solution, because it's not guaranteed to work. The agent might try to go `UP` and accidentally move `LEFT`.

- The probability of the "perfect" 5-step sequence `UP, UP, RIGHT, RIGHT, RIGHT` actually working is $0.8^5 = 0.32768$.
    
- We don't need a _plan_; we need a **strategy** that tells us what to do for _any state we might end up in_. This strategy is called a [[Policies (Optimal Policy)|Policy]].
    

This problem setup is formally known as a [[Markov Decision Processes (MDPs)|Markov Decision Process (MDP)]].

### ❓ Review Questions

1. What is the key difference between a simple decision problem and a sequential one?
    
2. Why can't we use a simple search algorithm (like BFS or A*) to find a "solution" for this grid world?
    
3. What is a "stochastic" action?