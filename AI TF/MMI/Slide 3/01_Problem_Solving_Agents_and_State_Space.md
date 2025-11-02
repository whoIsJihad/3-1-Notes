# 🧠 Problem-Solving Agents and State-Space Model

## Definition of State-Space Model

The **State-Space Model** is the intelligent agent's structured representation of the world, usually defined as a set of **discrete states**. The goal of search is to find a path from the **Initial State** to one of the **Goal States**.

## Key Components

1. **Solution Space (**$S^A$**):** The entire universe of potential solutions. The search aims to find the **optimal solution** ($S^{A*}$) within this space.
    
2. **Initial State:** The starting configuration. For some processes, this can be randomly selected.
    
3. **Goal State(s):** One or more states that satisfy the **Goal Test**. Once reached, the search terminates.
    
    - _Example:_ "Drive to Bucharest" (specific state) or "Drive to a town with a ski-resort" (multiple states).
        
4. **Operators (Actions/Successor Function):** The legal moves or actions that allow the agent to move from one state to another.
    
    - The **Successor Function**, $S(x)$, returns the set of _action-state_ pairs resulting from taking actions from state $x$.