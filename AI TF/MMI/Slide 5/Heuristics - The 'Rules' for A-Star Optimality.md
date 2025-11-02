# ⚖️ Heuristics: The "Rules" for A* Optimality

We just saw that A* Search is optimal, but this comes with a huge asterisk. It's only optimal if the heuristic $h(n)$ is "good." "Good" has a precise mathematical definition.

There are two levels of "good": **Admissible** and **Consistent**.

### 1. Admissible Heuristics (The "Optimistic" Heuristic)

This is the most important rule.

- **Definition:** An admissible heuristic **never overestimates** the true cost.
    
- **Formal:** $h(n) \le h^*(n)$
    
    - $h(n)$ = Your heuristic's _estimate_ from $n$ to the goal.
        
    - $h^*(n)$ = The _true, actual cost_ of the optimal path from $n$ to the goal.
        
- **Analogy:** An admissible heuristic is an "optimist." It always assumes the path ahead is better than or equal to what it truly is.
    
- **Example:** The straight-line distance heuristic is admissible because the shortest _road_ path can _never_ be shorter than the straight line. $h_{SLD}(n) \le h^*_{road}(n)$.
    
- **Why it works (Proof Sketch):**
    
    1. Suppose A* is about to expand a suboptimal goal $G_2$. This means its $f$-cost ($f(G_2) = g(G_2)$) is the lowest in the fringe.
        
    2. But somewhere in that fringe _must_ also be a node $n$ that is on the _true_ optimal path to goal $G$.
        
    3. Because our heuristic is admissible, we know $h(n) \le h^*(n)$.
        
    4. This means $f(n) = g(n) + h(n) \le g(n) + h^*(n)$.
        
    5. $g(n) + h^*(n)$ is the cost of the _true_ optimal path, $g(G)$.
        
    6. So, $f(n) \le g(G)$.
        
    7. Since $G_2$ is suboptimal, $g(G) < g(G_2)$.
        
    8. Chaining this all together: $f(n) \le g(G) < g(G_2) = f(G_2)$.
        
    9. This means $f(n) < f(G_2)$, which is a **contradiction**. A* would have expanded $n$ _before_ $G_2$.
        
- **Theorem:** If $h(n)$ is admissible, __A_ using TREE-SEARCH is optimal._*
    

### 2. Consistent Heuristics (The "Monotonic" Heuristic)

Consistency is a stricter property that is needed for _graph search_ (where we check for and avoid expanding repeated states).

- **Definition:** A heuristic is consistent if, for any node $n$ and its successor $n'$, the cost from $n$ is no greater than taking one step and _then_ using the heuristic.
    
- **Formal (Triangle Inequality):** $h(n) \le c(n, a, n') + h(n')$
    
    - $c(n, a, n')$ is the _step cost_ to get from $n$ to $n'$.
        
- **What this implies:** If a heuristic is consistent, the $f$-values along any path are **non-decreasing**. $f(n') \ge f(n)$.
    
- **Why it matters:** It guarantees that the _first_ time A* expands a node, it has found the optimal path to it. This is crucial for graph search, so we don't have to re-expand nodes.
    
- **Relationship:** If a heuristic is consistent, it is also admissible. (Most admissible heuristics you can think of, like straight-line distance, are also consistent).
    
- **Theorem:** If $h(n)$ is consistent, __A_ using GRAPH-SEARCH is optimal._*
    

