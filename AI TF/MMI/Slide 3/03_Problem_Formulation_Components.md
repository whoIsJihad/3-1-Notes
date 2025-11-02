# 🛠️ Problem Formulation Components

A well-defined search problem must include these four formal components:

1. **Initial State:** The starting point of the search.
    
    - _Example:_ "at Arad".
        
2. **Actions / Successor Function:** The set of legal moves $S(x)$ that transform the current state $x$.
    
    - _Example:_ $S(\text{Arad}) = \{\langle \text{Arad} \to \text{Zerind, Zerind} \rangle, ...\}$.
        
3. **Goal Test (or set of Goal States):** A check to determine if the current state is a solution.
    
    - _Example:_ Is the state $x$ equal to "at Bucharest"?
        
4. **Path Cost (Additive):** A measure of quality for the sequence of actions taken.
    
    - It is **additive**—the total cost is the sum of all individual step costs, $c(x, a, y)$.
        
    - **Step Cost** $c(\dots)$ is assumed to be $\ge 0$.
        
    - _Examples:_ Sum of distances, number of actions executed, or time taken.
        

**Solution:** A **sequence of actions** (or path of states) leading from the Initial State to a state that passes the Goal Test.