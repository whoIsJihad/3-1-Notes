# Goal-Based Agents

Goal-based agents are **deliberative** (not just reactive) and choose actions to achieve a specific, desirable state.

## Mechanism

- **Goal:** A description of a desirable situation.
    
- The agent must consider a sequence of possible actions to see if the goal is achieved ("What will happen if I do...").
    

## Architecture

This type adds **internal state (memory)** and a model of the world to predict the future:

1. **State:** Tracks the current state of the world.
    
2. **How the world evolves:** Internal model of environmental dynamics.
    
3. **What my actions do:** Internal model of action outcomes.
    
4. **Goals:** The target situation to be achieved.
    

## Limitation

They focus only on achieving the goal (happy state) and **do not consider the cost** or the "degree of happiness" across multiple goal-achieving paths. This is where [[Utility-Based Agents]] are required.