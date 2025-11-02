# 🪟 Abstraction and The State-Space Graph

## Abstraction

**Abstraction** is the critical process of removing irrelevant details to create a simplified, high-level, and approximate model of the world that the computer can manage. A good abstraction must **retain all important details**.

- **Example (Navigation):** The core problem is abstracted to a **map problem**.
    
    - **Nodes** = Cities.
        
    - **Links** = Freeways/Roads.
        
    - Irrelevant details (like traffic, refueling) are ignored initially.
        

## The State-Space Graph

The problem formulation is naturally mapped onto a **Graph**:

- **Nodes:** Represent the **States**.
    
- **Directed Arcs:** Represent the **Operators** or **Actions**.
    
- **Path:** The sequence of states/actions from $S$ (Start) to $G$ (Goal) that constitutes the **Solution**.