# Informed Search Algorithms: Greedy vs. A*

This is the central lesson of informed search. We'll contrast the "fast but flawed" Greedy search with the "smart and optimal" A* search. Both are types of Informed Search - Best-First Search.

### 1. Greedy Best-First Search

Greedy search is the simple, "short-sighted" approach.

- **Evaluation Function:** $f(n) = h(n)$
    
- **The Logic:** It _only_ considers the estimated cost to the goal ($h(n)$). It completely ignores the cost it took to get to $n$ (the $g(n)$). It's "greedy" because it always expands the node that _appears_ to be closest to the goal, right now.
    

#### Example: Romania (Goal: Bucharest)

1. **At Arad (**$h=366$**):** Fringe has [Sibiu ($h=253$), Timisoara ($h=329$), Zerind ($h=374$)].
    
2. **Expand Sibiu (**$h=253$**):** It has the lowest $h$-value.
    
3. **Fringe now has:** [**Fagaras (**$h=176$**)**, Rimnicu Vilcea ($h=193$), Timisoara ($h=329$), Zerind ($h=374$)].
    
4. **Expand Fagaras (**$h=176$**):** It has the lowest $h$-value.
    
5. **Fringe now has:** [**Bucharest (**$h=0$**)**, Rimnicu Vilcea ($h=193$), ...].
    
6. **Goal Found!**
    

- **Path Found:** Arad $\rightarrow$ Sibiu $\rightarrow$ Fagaras $\rightarrow$ Bucharest
    
- **Total Cost:** 140 + 99 + 211 = **450 km**.
    

This path is **NOT OPTIMAL**. The true optimal path costs 418 km. Greedy was "tricked" by Fagaras's low heuristic ($h=176$), failing to see that the path to get there was already long.

#### Properties of Greedy Search

- **Complete?** No. It can get stuck in loops (just like Depth-First Search).
    
- **Optimal?** No. As the example proves, it's easily misled.
    
- **Time:** $O(b^m)$ (worst case)
    
- **Space:** $O(b^m)$ (worst case, keeps all nodes in memory)
    

### 2. A* (A-Star) Search

A* (pronounced "A-star") is the "gold standard" of pathfinding. It fixes the flaw in Greedy search by being smart.

- **Evaluation Function:** $f(n) = g(n) + h(n)$
    
- **The Logic:** It balances _two_ factors:
    
    1. $g(n)$**:** The _known, actual cost_ of the path from the start to $n$.
        
    2. $h(n)$**:** The _estimated, future cost_ from $n$ to the goal.
        
- Therefore, $f(n)$ is the _total estimated cost_ of the _entire_ solution path going _through_ node $n$. It sees the "whole picture."
    

#### Example: Romania (Goal: Bucharest)

1. **At Arad:** Fringe has [Arad ($f=0+366=366$)].
    
2. **Expand Arad:**
    
    - Sibiu: $f = g(140) + h(253) = 393$
        
    - Timisoara: $f = g(118) + h(329) = 447$
        
    - Zerind: $f = g(75) + h(374) = 449$
        
    - Fringe is: [**Sibiu (**$f=393$**)**, Timisoara ($f=447$), Zerind ($f=449$)].
        
3. **Expand Sibiu (**$f=393$**):**
    
    - Rimnicu Vilcea: $f = g(140+80) + h(193) = 413$
        
    - Fagaras: $f = g(140+99) + h(176) = 415$
        
    - Fringe is: [**Rimnicu Vilcea (**$f=413$**)**, Fagaras ($f=415$), Timisoara ($f=447$), Zerind ($f=449$)].
        
    
    _**This is the key moment!**_ Greedy chose Fagaras (because $h=176$), but A* sees that the _total path_ through Rimnicu Vilcea ($f=413$) is "seemingly" better than the path through Fagaras ($f=415$).
    
4. **Expand Rimnicu Vilcea (**$f=413$**):**
    
    - Pitesti: $f = g(220+97) + h(100) = 417$
        
    - Fringe is: [**Fagaras (**$f=415$**)**, Pitesti ($f=417$), Timisoara ($f=447$), Zerind ($f=449$)].
        
5. **Expand Fagaras (**$f=415$**):** (Now A* explores this, since its $f$-value is lowest).
    
    - Bucharest: $f = g(239+211) + h(0) = 450$
        
    - Fringe is: [**Pitesti (**$f=417$**)**, Bucharest ($f=450$), Timisoara ($f=447$), Zerind ($f=449$)].
        
6. **Expand Pitesti (**$f=417$**):**
    
    - Bucharest: $f = g(317+101) + h(0) = 418$
        
    - Fringe is: [**Bucharest (**$f=418$**)**, Bucharest ($f=450$), ...].
        
7. **Expand Bucharest (**$f=418$**):** This is a goal node. Since A* always expands the lowest $f$-cost node, we are **guaranteed** this is the optimal path.
    
    - **Path Found:** Arad $\rightarrow$ Sibiu $\rightarrow$ Rimnicu Vilcea $\rightarrow$ Pitesti $\rightarrow$ Bucharest
        
    - **Total Cost:** **418 km**.
        

#### Properties of A* Search

- **Complete?** Yes.
    
- **Optimal?** Yes... _if_ your heuristic $h(n)$ follows certain rules. This is a critical "if."
    
- **Optimally Efficient?** Yes. For a given heuristic, no other optimal algorithm is guaranteed to expand fewer nodes.
    
- **Time:** $O(b^m)$ (Exponential in the worst case).
    
- **Space:** $O(b^m)$ (Exponential. It must store all generated nodes in the fringe).
    

**Main Takeaway:** A* is the best, but its optimality depends on our heuristic, and its biggest practical problem is its exponential space complexity.

_Next up: [[Heuristics - The 'Rules' for A-Star Optimality]]_ _Later: [[The Problem with A-Star - Memory]]**_**