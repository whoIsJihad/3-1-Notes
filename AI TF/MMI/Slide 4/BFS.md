# 1. Breadth-First Search (BFS)

**Breadth-First Search (BFS)** is an uninformed search strategy that explores the state space "layer by layer." It always expands the **shallowest unexpanded node** first.

This guarantees that if a solution exists, BFS will find the shallowest solution first.

### Core Mechanism & Data Structure

The "fringe" (the set of generated but unexpanded nodes) is managed as a **First-In, First-Out (FIFO) Queue**.

1. Start with the initial state in the queue.
    
2. Loop: a. If the queue is empty, return failure (no solution). b. Dequeue the front node. c. Check if this node is the goal state. * If YES: Return this node (solution found). d. If NO: Expand the node. Take all its successor nodes and **enqueue** them at the **end** of the queue.
    

### Pseudocode for BFS (Graph Search)

```
function BREADTH_FIRST_SEARCH(problem):
    node ← NODE(state=problem.INITIAL_STATE, path_cost=0)
    
    if problem.IS_GOAL(node.state):
        return SOLUTION(node)

    fringe ← FIFO_QUEUE()
    fringe.push(node)
    
    closed_list ← SET() // To handle repeated states/cycles

    while not fringe.is_empty():
        node ← fringe.pop()

        if node.state not in closed_list:
            closed_list.add(node.state)

            for child_node in EXPAND(problem, node):
                if problem.IS_GOAL(child_node.state):
                    return SOLUTION(child_node)
                fringe.push(child_node)
                
    return failure
```

### Analysis of BFS Properties

|Criterion|Result|Technical Justification|
|---|---|---|
|**Complete?**|**Yes.**|BFS is guaranteed to find a solution if one exists, as long as the branching factor $b$ is finite. It explores every reachable node.|
|**Optimal?**|**Yes, with a condition.**|BFS is optimal **if all step costs are uniform** (e.g., $cost=1$). Because it finds the shallowest goal first, and "shallowest" is synonymous with "cheapest" in this case, it finds the optimal solution. It is _not_ optimal for non-uniform step costs.|
|**Time Complexity**|$O(b^{d+1})$|In the worst case, BFS must expand every node up to depth $d$. The number of nodes is a geometric progression: $1 + b + b^2 + \dots + b^d$. This sum is $O(b^d)$. However, the algorithm might not find the goal until it generates some or all nodes at the _next_ level, $d+1$. Thus, the total number of _generated_ nodes is $O(b^{d+1})$.|
|**Space Complexity**|$O(b^{d+1})$|This is the most significant drawback of BFS. The fringe (queue) must store all nodes at a given depth before expanding the next depth. In the worst case, the queue will contain all nodes at depth $d$, and potentially all their successors at depth $d+1$. The size of the fringe grows exponentially: $O(b^{d+1})$.|