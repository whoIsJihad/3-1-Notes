
We've established that [[Informed Search Algorithms - Greedy vs. A*|A* Search]] is complete, optimal, and optimally efficient. So, what's the catch?

**The Catch: Space Complexity.**

A*'s properties are:

- **Time:** $O(b^m)$ (Exponential)
    
- **Space:** $O(b^m)$ (Exponential)
    

A* must store all _generated_ nodes (the "fringe") in a priority queue to find the next-best $f$-cost. This collection of nodes grows exponentially.

In practice, __A_ will almost always run out of RAM before it runs out of time._*

This leads to a class of algorithms that try to get A*'s _optimality_ while using the _linear space_ of a Depth-First Search.

### 1. Recursive Best-First Search (RBFS)

RBFS is a recursive algorithm that tries to mimic A* in linear space.

- **Space Complexity:** $O(bd)$ (Linear, like DFS).
    
- **The Logic:**
    
    1. It explores a path, just like DFS.
        
    2. It keeps track of the $f$-value of the current node.
        
    3. Crucially, it also remembers the **"f-limit"**—the $f$-value of the best _alternative_ path it _didn't_ take (e.g., the second-best child of an ancestor node).
        
    4. It continues going "deeper" as long as $f(\text{current}) \le \text{f-limit}$.
        
    5. If $f(\text{current}) > \text{f-limit}$, it "unwinds" the recursion (backtracks).
        
    6. **Key Trick:** As it unwinds, it _replaces_ the $f$-value of the parent node with the _best_ $f$-value of its children (the one it just explored). This "caches" the value of that subtree, so it can decide whether to re-explore it later.
        
- **Properties:**
    
    - **Optimal?** Yes (if $h(n)$ is admissible).
        
    - **Problem:** It can suffer from "thrashing." It might repeatedly go down a path, backtrack, and then immediately go down the _same path_ again because it has forgotten all the _other_ nodes in that subtree. It's re-generating nodes over and over.
        

### 2. SMA* (Simplified Memory-Bounded A*)

SMA* is a more practical approach: just run A* until you're out of memory, then adapt.

- **The Logic:**
    
    1. Works exactly like A*, expanding the best node (lowest $f$-cost).
        
    2. ...until memory is full.
        
    3. When full, to add a _new_ node, it must first **delete** a node.
        
    4. **Which node?** It deletes the _worst_ node (the one with the _highest_ $f$-value) from the fringe. This is a node it thinks is least promising.
        
    5. **Key Trick (like RBFS):** When it deletes (forgets) a node, it "passes up" the $f$-value of that lost node to its parent. The parent "remembers" the $f$-cost of its best _forgotten_ child.
        
- **Properties:**
    
    - This is a very robust algorithm.
        
    - It finds the **optimal reachable solution** given the memory it has.
        
    - If there's enough memory, it behaves exactly like A*.
        
    - If memory is too tight, it can "thrash" like RBFS.
        

_Back to: [[Informed Search Algorithms - Greedy vs. A_]]* _Back to: [[Heuristic Design & Evaluation]]_