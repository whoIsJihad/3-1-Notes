# 2. Uniform-Cost Search (UCS)

**Uniform-Cost Search (UCS)** is an uninformed search strategy that addresses the optimality limitation of BFS. While BFS is optimal for uniform step costs, UCS is designed to be **optimal for any non-negative step costs**.

UCS always expands the unexpanded node $n$ that has the **lowest path cost**, denoted as $g(n)$.

- **Path Cost** $g(n)$**:** The sum of all step costs from the initial state to node $n$.
    

### Core Mechanism & Data Structure

The "fringe" is managed as a **Priority Queue**, ordered by $g(n)$.

1. Start with the initial state node in the priority queue (with $g(n)=0$).
    
2. Loop: a. If the fringe is empty, return failure. b. Pop the node with the _lowest_ $g(n)$ from the priority queue. c. Check if this node is the goal state. * If YES: Return this node (solution found). This is guaranteed to be the optimal path. d. If NO: Expand the node. For each successor node: * Calculate its new path cost: $g(\text{successor}) = g(\text{node}) + \text{step\_cost}(\text{node}, \text{successor})$. * Add the successor to the priority queue.
    

**Note:** If all step costs are equal (e.g., $cost=1$), $g(n)$ is just the depth of the node. In this case, UCS behaves identically to BFS.

### Pseudocode for UCS (Graph Search)

```
function UNIFORM_COST_SEARCH(problem):
    node ← NODE(state=problem.INITIAL_STATE, path_cost=0)
    
    fringe ← PRIORITY_QUEUE(order_by=g) // g is path_cost
    fringe.push(node)
    
    closed_list ← MAP() // Stores state -> best_path_cost

    while not fringe.is_empty():
        node ← fringe.pop()

        if problem.IS_GOAL(node.state):
            return SOLUTION(node)

        // If we've seen this state before via a better path, skip
        if node.state in closed_list and closed_list[node.state] < node.path_cost:
            continue

        closed_list[node.state] = node.path_cost // Mark as visited with this cost

        for child_node in EXPAND(problem, node):
            if child_node.state not in closed_list:
                fringe.push(child_node)
            // Found a cheaper path to a node already in the fringe?
            else if child_node.state in fringe and fringe.get_cost(child_node.state) > child_node.path_cost:
                fringe.decrease_key(child_node) // Update its cost/priority
                
    return failure
```

### Analysis of UCS Properties

|Criterion|Result|Technical Justification|
|---|---|---|
|**Complete?**|**Yes, with a condition.**|UCS is complete _if_ all step costs are non-negative and $\ge \epsilon$ (some small positive value). If zero-cost steps are allowed, UCS can get stuck in an infinite loop of zero-cost actions (e.g., A $\to$ B $\to$ A) without making progress.|
|**Optimal?**|**Yes.**|UCS is optimally complete. Because it always expands the node with the lowest path cost $g(n)$, it explores the state space in contours of increasing cost. The first time it reaches the goal, it _must_ be via the cheapest path.|
|**Time Complexity**|$O(b^{\lceil C^{*}/\epsilon \rceil})$|Let $C^*$ be the cost of the optimal solution and $\epsilon$ be the minimum step cost. The algorithm explores all nodes with $g(n) \le C^*$. The "depth" of the search is roughly $C^*/\epsilon$. Thus, the complexity is $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$ or $O(b^{\lceil C^{*}/\epsilon \rceil})$.|
|**Space Complexity**|$O(b^{\lceil C^{*}/\epsilon \rceil})$|The space complexity is identical to the time complexity. The priority queue must store the fringe, which contains all nodes with $g(n) \le C^*$. This set can grow exponentially.|