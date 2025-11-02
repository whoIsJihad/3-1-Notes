Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization of the Minimax Algorithm. It avoids searching parts of the game tree that will not influence the final decision.

The core idea is to "prune" (stop searching) a branch as soon as we know it's worse than a choice we've already found.

## Core Values

It maintains two values during the depth-first search:

- alpha (alpha): The highest-value choice found so far along the path for MAX. This is the best (highest) score MAX can guarantee at this point.
    
- beta (beta): The lowest-value choice found so far along the path for MIN. This is the best (lowest) score MIN can guarantee at this point.
    

## Pruning Condition

- MIN Node Pruning: Prune if a value 'v' is found such that v <= alpha. Why? Because MAX (at a parent node) already has a better choice (alpha) available, and will never let MIN choose this path.
    
- MAX Node Pruning: Prune if a value 'v' is found such that v >= beta. Why? Because MIN (at a parent node) already has a better choice (beta) available and will never let MAX choose this path.
    

In general, the search window is [alpha, beta]. The search is terminated (pruned) when beta <= alpha.

## Effectiveness

- Pruning does not affect the final Minimax result.
    
- Worst Case: No pruning. O(b^m).
    
- Best Case: With perfect move ordering (best moves searched first), the time complexity is reduced to O(b^(m/2)).
    
- This effectively doubles the searchable depth.
    

## Links

- Back to: ([[Adversarial Search Index]])
    
- Based on: ([[Minimax Algorithm]])