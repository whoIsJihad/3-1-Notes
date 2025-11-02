
In many problems, the state space is a **graph**, not a tree. This means it is possible to reach the same state through multiple different paths.

- _Example:_ In a route-finding problem, you can go $S \to A \to B$ and $S \to C \to B$. Node $B$ is a **repeated state**.
    
- This also includes **cycles** (e.g., $A \to B \to A$).
    

Failure to detect repeated states can turn a finite, linear problem into an **infinite, exponential one**. An algorithm could get stuck in a cycle forever (like DFS) or re-explore an entire massive subtree it has already seen (like BFS).

### Solutions to Repeated States

There are two primary methods, which represent a trade-off between optimality and memory efficiency.

#### Method 1: Do Not Create Paths with Cycles (Simple)

This is a simpler check, often used with DFS.

- **Mechanism:** As you traverse a path, keep track of the nodes currently _on that path_ (the ancestors). Before expanding a node, check if its successor is already in the ancestor list. If it is, do not expand it (as this would create a loop).
    
- **Trade-off:**
    
    - **Pro:** Prevents infinite loops in DFS. It's memory-efficient (just stores the current path).
        
    - **Con:** This is **suboptimal**. It does not prevent re-visiting a state reached via a _different_ branch. It only stops $A \to B \to A$. It does _not_ stop $S \to A \to B$ and $S \to C \to B$.
        

#### Method 2: Graph Search (Closed List)

This is the standard, most robust solution.

- **Mechanism:** Maintain a data structure called a **"closed list"** or **"visited set"** which stores _every state that has ever been expanded_.
    
- **Algorithm:**
    
    1. When a node is popped from the fringe for expansion, add its state to the `closed_list`.
        
    2. When generating successor nodes, **do not add any successor to the fringe if its state is already in the `closed_list`**.
        
- **Trade-off:**
    
    - **Pro:** This is **optimal** (assuming the first path found is the best, like in BFS/UCS) and prevents _all_ redundant work.
        
    - **Con:** This is **memory inefficient**. The `closed_list` can grow to store every single reachable state in the problem. For the 8-puzzle, this is $9! = 362,880$ states. For chess, it's astronomical.
        

This is the classic **Graph Search** algorithm, which is essential for most real-world problems.