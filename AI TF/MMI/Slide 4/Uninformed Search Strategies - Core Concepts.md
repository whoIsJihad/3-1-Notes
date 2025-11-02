

## 1. Introduction to Uninformed Search

**Uninformed Search**, also known as **Blind Search**, is a class of search algorithms that operates with no additional information about the problem domain beyond the problem's definition.

When an uninformed search algorithm is deciding which node to expand next from the **fringe** (the set of generated but unexpanded nodes), it has no clue whether one non-goal state is any closer to the goal than another.

The search is "blind" because it can't see "which way" the goal is. It can only systematically explore the state space based on its structure.

This contrasts with **Informed (Heuristic) Search**, which uses a heuristic function ($h(n)$) to estimate the cost from a node to the goal, allowing it to make more intelligent "guesses."

## 2. Measuring Problem-Solving Performance

To compare the effectiveness of different search algorithms, we use four key metrics:

1. **Completeness:**
    
    - **Question:** Is the algorithm guaranteed to find a solution, assuming one exists?
        
    - An incomplete algorithm might search forever or terminate without finding an existing solution.
        
2. **Optimality:**
    
    - **Question:** Does the algorithm find the _optimal_ solution?
        
    - **Optimality** is defined by the problem. It usually means finding the solution with the lowest **path cost** (e.g., the shortest path, the cheapest route). An algorithm that finds _a_ solution but not the _best_ one is non-optimal.
        
3. **Time Complexity:**
    
    - **Question:** How long does the algorithm take to find a solution?
        
    - This is typically measured by the number of **nodes generated or expanded** during the search.
        
    - We often express this using Big-O notation in terms of:
        
        - $b$: **branching factor** (the maximum number of successors of any node).
            
        - $d$: **depth** of the shallowest goal node.
            
        - $m$: **maximum depth** of the state space (can be $\infty$).
            
4. **Space Complexity:**
    
    - **Question:** How much memory does the algorithm need to perform the search?
        
    - This is measured by the maximum number of nodes stored in memory at any one time.
        
    - This includes the nodes in the **fringe** and, for some algorithms, the **closed list** (set of already-expanded nodes).
        
    - In many practical AI problems, space complexity is a more significant limiting factor than time complexity.