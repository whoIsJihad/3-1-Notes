# Simple Reflex Agents

Simple reflex agents react immediately to the current percept, without considering history or goals.

## 1. Table-Driven Agents

- **Mechanism:** Uses a massive **lookup table** that maps every possible perceived state to an optimal action.
    
- **Drawbacks:**
    
    - **Too large** to store (e.g., Chess states are $10^{120}$).
        
    - **Not adaptive** to environmental changes.
        
    - **Looping** is possible as they can't condition actions on previous states.
        
    - **Not autonomous** (too dependent on built-in knowledge).
        

## 2. Simple Reflex Agents (Condition-Action Rules)

- **Mechanism:** Uses **condition-action rules** (e.g., `IF [A, Dirty] THEN Suck`).
    
- **Memory/State:** **Stateless**; they do not have memory of past world states.
    
- **Drawbacks:** Still often too big, not easily adaptive, and cannot condition actions on previous states.
    

## Architecture (Shared)

- Only uses the current percept ("What the world is like now") and maps it directly to "What action I should do now" using Condition-Action Rules.
    
- **No internal memory** is utilized in the decision-making loop.