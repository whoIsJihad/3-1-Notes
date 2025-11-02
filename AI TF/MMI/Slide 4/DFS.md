# 3. Depth-First Search (DFS)

**Depth-First Search (DFS)** is an uninformed search strategy that explores the state space by always expanding the **deepest unexpanded node** first.

It dives down a single path as far as it can go. When it hits a dead end (or a previously visited node in a graph search), it **backtracks** to the last decision point and tries the next available option.

### Core Mechanism & Data Structure

The "fringe" is managed as a **Last-In, First-Out (LIFO) Stack**.

1. Start with the initial state in the stack.
    
2. Loop: a. If the stack is empty, return failure. b. Pop the top node from the stack. c. Check if this node is the goal state. * If YES: Return this node (solution found). d. If NO: Expand the node. Take all its successor nodes and **push** them onto the **top** of the stack.
    

This LIFO behavior means the most recently generated successor (which is one level deeper) is the _very next_ node to be expanded.

### Pseudocode for DFS (Recursive Tree-Search Version)

```
function RECURSIVE_DLS(node, problem, limit):
    if problem.IS_GOAL(node.state):
        return SOLUTION(node)
    
    else if limit == 0:
        return "cutoff" // Reached depth limit
        
    else:
        cutoff_occurred ← false
        for child_node in EXPAND(problem, node):
            result ← RECURSIVE_DLS(child_node, problem, limit - 1)
            
            if result == "cutoff":
                cutoff_occurred ← true
            else if result != failure:
                return result
                
        if cutoff_occurred:
            return "cutoff"
        else:
            return failure
```

_(Note: A full DFS would call this with `limit = ∞`. The iterative stack-based approach is more common.)_

### Analysis of DFS Properties

|Criterion|Result|Technical Justification|
|---|---|---|
|**Complete?**|**No.**|DFS is **not complete** in general. If the state space contains **infinite-depth paths** (e.g., a tree that goes on forever) or **cycles** (in a graph search without a `closed_list`), DFS can get stuck following one of these paths forever and never find a solution, even if one exists on another branch.|
|**Optimal?**|**No.**|DFS is **not optimal**. It has a "dive-first" mentality. It may find a very deep, high-cost solution on the first path it explores, while a much better, shallower solution exists on a branch it hasn't explored yet.|
|**Time Complexity**|$O(b^m)$|$m$ is the **maximum depth** of the state space. In the worst case, DFS may explore every node in the tree down to this maximum depth. If $m$ is much larger than the actual solution depth $d$, this is terrible. However, if solutions are dense, DFS might get "lucky" and find one very quickly, potentially much faster than BFS.|
|**Space Complexity**|$O(bm)$|**This is the primary advantage of DFS.** Because it only needs to store the _current path_ it is exploring (and the unexpanded siblings on that path), its memory usage is **linear** with respect to the maximum depth $m$. It does not need to store all nodes at a given level, unlike BFS.|

### Depth-Limited Search (DLS)

To solve the "infinite path" problem of DFS, **Depth-Limited Search (DLS)** is used. It is simply a DFS that enforces a maximum depth limit, $L$. It will not expand nodes at depth $L$.

- **Completeness:** Still **not complete**. If the shallowest solution is deeper than the limit $L$ (i.e., $d > L$), DLS will fail to find it.
    
- **Time:** $O(b^L)$
    
- **Space:** $O(bL)$