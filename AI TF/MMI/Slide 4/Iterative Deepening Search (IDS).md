
**Iterative Deepening Search (IDS)**, or Iterative Deepening Depth-First Search (IDDFS), is a "hybrid" strategy that combines the **linear space complexity of DFS** with the **completeness and optimality (for uniform costs) of BFS**.

It is often the preferred uninformed search strategy when the state space is large and the depth of the solution is unknown.

### Core Mechanism

IDS works by running a series of **Depth-Limited Searches (DLS)** with progressively increasing depth limits.

1. Run DLS with `limit = 0`.
    
2. If no solution, run DLS from the root with `limit = 1`.
    
3. If no solution, run DLS from the root with `limit = 2`.
    
4. ...and so on, until a solution is found at some depth limit $L=d$.
    

### Performance: Is it Wasteful?

It seems incredibly wasteful to re-generate the upper levels of the tree repeatedly. However, the overhead is surprisingly small.

**Analysis:** The total number of nodes generated in an IDS (to depth $d$) is:

$$N(IDS) = (d+1)b^0 + (d)b^1 + (d-1)b^2 + \dots + (1)b^d$$

This sum is dominated by its last term. For large $b$, this is $O(b^d)$.

Compare this to **BFS**:

$$N(BFS) = 1 + b + b^2 + \dots + b^d + (b^{d+1}-b) = O(b^{d+1})$$

**Example (from slides):**

- $b = 10$, $d = 5$
    
- $N(DLS \text{ at } d=5) = 1 + 10 + 100 + 1000 + 10000 + 100000 = 111,111$
    
- $N(IDS \text{ at } d=5) = (6 \cdot 1) + (5 \cdot 10) + (4 \cdot 100) + (3 \cdot 1000) + (2 \cdot 10000) + (1 \cdot 100000) = 123,456$
    
- $N(BFS \text{ at } d=5) \approx 1,111,111$
    

**Conclusion:** IDS performs more work, but the overhead is only a small constant factor. The _asymptotic_ time complexity is $O(b^d)$, which is asymptotically _better_ than BFS's $O(b^{d+1})$.

### Analysis of IDS Properties

|Criterion|Result|Technical Justification|
|---|---|---|
|**Complete?**|**Yes.**|IDS is complete. If a solution exists at depth $d$, IDS will eventually run its DLS with `limit = d` and find it. It cannot get lost in infinite paths.|
|**Optimal?**|**Yes, with a condition.**|Like BFS, IDS is optimal **if all step costs are uniform** ($cost=1$). It finds the shallowest goal first. If costs are not uniform, a "cheaper" goal might exist at a deeper level, which IDS would miss.|
|**Time Complexity**|$O(b^d)$|The work is dominated by the final, successful iteration (DLS at depth $d$), which expands $O(b^d)$ nodes.|
|**Space Complexity**|$O(bd)$|This is the **key advantage**. Because each iteration is just a DLS, the memory usage is that of DFS: **linear** with respect to the current depth limit $d$.|