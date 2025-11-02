
This is our starting point. We're moving from "blind" search to "smart" search.

### 1. The Problem: Why Uninformed Search Fails

First, why do we even need this? Uninformed strategies (like Breadth-First or Depth-First Search) are "blind." They only know the problem definition and have no idea if they're moving _toward_ or _away_ from the goal.

This leads to a "combinatorial explosion."

- **Case Study: The 8-Puzzle**
    
    - The average solution is ~22 steps deep.
        
    - The branching factor ($b$) is about 3.
        
    - An exhaustive search (like BFS) would need to explore $3^{22} \approx 3.1 \times 10^{10}$ states.
        
    - Even Iterative Deepening (IDS) for a simpler $d=12$ puzzle expands 3.6 million states.
        

For any real-world problem, this is computationally infeasible. We'll run out of time and memory.

### 2. The Solution: The Heuristic Function, $h(n)$

The solution is to give our search algorithm "problem-specific knowledge"—a "rule of thumb" to guide it. This is the **heuristic function,** $h(n)$.

- **Definition:** $h(n)$ is an **estimate** of the _optimal_ cost to get from the current node $n$ to the nearest goal state.
    
- **Key Idea:** It's an _educated guess_. It is _not_ the true cost.
    
- **Goal State:** If $n$ is a goal, $h(n) = 0$.
    
- **Example (Romania Map):** If our goal is Bucharest, $h(n)$ for any city $n$ could be the **straight-line-distance** from $n$ to Bucharest. This is a good guess because the _actual road distance_ can never be shorter than the straight line.
    

### 3. The General Strategy: Best-First Search

Best-First Search is the _general algorithm_ that uses a heuristic. It's a template, not a specific algorithm.

- **How it works:** It uses a priority queue (the "fringe") to hold all unexpanded nodes.
    
- **Evaluation Function** $f(n)$**:** It sorts this queue using an "evaluation function" $f(n)$, which measures the "desirability" of a node. The node with the _lowest_ $f(n)$ is expanded next.
    
- **The "Strategy":** The _only_ difference between various informed algorithms is how they define $f(n)$:
    
    - **Uniform Cost Search:** $f(n) = g(n)$ (Just the past cost. It's uninformed!)
        
    - **Greedy Best First Search** :  $f(n) = h(n)$ (Just the estimated future cost)
        
    - **A* Search**  $f(n) = g(n) + h(n)$  (Past cost + Estimated future cost)
        

  ### 4. The Measures of Success

We judge all our search algorithms on these four criteria:

1. **Completeness:** Is it guaranteed to find _a_ solution if one exists?
    
2. **Optimality:** Is it guaranteed to find the _best_ (lowest-cost) solution?
    
3. **Time Complexity:** How many nodes does it expand?
    
4. **Space Complexity:** How much memory does it need? (i.e., how big does the fringe get?)
    

_Next up: [[🧠 Greedy vs A*]]*