# Introduction to Adversarial Search

**Adversarial Search** is a search technique used in game playing where two or more agents with conflicting goals make decisions.

- **Core Condition:** Minimum of 2 agents.
    
- Agents are adversaries (e.g., between two teams) not cooperative (e.g., within a team).
    
- Example: Chess is purely adversarial.
    

## Typical Assumptions

- **Two agents** whose actions alternate (e.g., MAX and MIN).
    
- **Fully observable environments**: Both players can see the complete state of the game.
    
- **Zero-Sum Game**: The utility values for each agent are the opposite of the other.
    
    - If one player wins (+1), the other loses (-1).
        
    - The sum of utilities is always zero.
        
- **Deterministic**: Given a state and an action, the resulting state is known.
    
- **Turn-taking**.
    

These assumptions define a "deterministic, turn-taking, zero-sum game of perfect information."

**Links:**

    
- Next: [[Search vs Games]]