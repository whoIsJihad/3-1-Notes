
This table compares the performance of the five key uninformed search strategies.

### Variable Definitions

- $b$: **branching factor** (max successors of a node)
    
- $d$: **depth** of the shallowest (and/or cheapest) goal
    
- $m$: **maximum depth** of the state space (can be $\infty$)
    
- $l$: the **depth limit** used in DLS
    
- $C^*$: cost of the optimal solution
    
- $\epsilon$: the minimum positive step cost (must be $> 0$)
    

### Comparison Table

|Criterion|Breadth-First (BFS)|Uniform-Cost (UCS)|Depth-First (DFS)|Depth-Limited (DLS)|Iterative Deepening (IDS)|
|---|---|---|---|---|---|
|**Complete?**|**Yes**|**Yes** (if $\epsilon > 0$)|**No**|**No** (if $d > l$)|**Yes**|
|**Optimal?**|**Yes** (if cost=1)|**Yes** (any cost)|**No**|**No**|**Yes** (if cost=1)|
|**Time**|$O(b^{d+1})$|$O(b^{\lceil C^{*}/\epsilon \rceil})$|$O(b^m)$|$O(b^l)$|$O(b^d)$|
|**Space**|$O(b^{d+1})$|$O(b^{\lceil C^{*}/\epsilon \rceil})$|$O(bm)$|$O(bl)$|$O(bd)$|
|**Primary Drawback**|Exponential Space|Exponential Space/Time|Non-Optimal, Incomplete|Incomplete|Not optimal for var costs|
|**Primary Advantage**|Optimal (uniform cost)|Optimal (any cost)|**Linear Space**|**Linear Space**|**Linear Space** + Optimal|

### Key Takeaways

- **BFS** is simple and optimal for $cost=1$ problems, but fails on memory.
    
- **UCS** is the go-to for finding the _cheapest_ path, but also fails on memory.
    
- **DFS** is memory-efficient (linear space!) but is generally a poor choice as it's incomplete and non-optimal.
    
- **IDS** is generally the **best all-around uninformed search strategy**, giving the best of both worlds: the completeness and optimality of BFS with the linear space-efficiency of DFS.