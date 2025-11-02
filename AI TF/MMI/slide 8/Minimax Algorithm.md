# Minimax Algorithm

The **Minimax** strategy finds the optimal move for a player (MAX) by assuming the opponent (MIN) also plays optimally. It maximizes the utility for the worst-case outcome for MAX.

It works by propagating utility values up from terminal nodes.

## Minimax Value

The value of a node `n` is computed as:

`MINIMAX-VALUE(n)` =

- `UTILITY(n)` if `n` is a terminal node
    
- `max(MINIMAX-VALUE(s))` for all successors `s` if `n` is a MAX node
    
- `min(MINIMAX-VALUE(s))` for all successors `s` if `n` is a MIN node
    

## Pseudocode

```
function MINIMAX-DECISION(state) returns an action
  v = MAX-VALUE(state)
  return the action in SUCCESSORS(state) with value v

function MAX-VALUE(state) returns a utility value
  if TERMINAL-TEST(state) then return UTILITY(state)
  v = -infinity
  for a, s in SUCCESSORS(state) do
    v = MAX(v, MIN-VALUE(s))
  return v

function MIN-VALUE(state) returns a utility value
  if TERMINAL-TEST(state) then return UTILITY(state)
  v = +infinity
  for a, s in SUCCESSORS(state) do
    v = MIN(v, MAX-VALUE(s))
  return v
```

## Properties

- **Completeness:** Yes (if the tree is finite).
    
- **Optimality:** Yes (if MIN plays optimally).
    
- **Time Complexity:** $O(b^m)$ (where `b` is branching factor, `m` is max depth)
    
- **Space Complexity:** $O(bm)$ (for depth-first search)
    

The exponential time complexity is the algorithm's main problem, leading to the need for [[Alpha-Beta Pruning]].

**Links:**

- Back to: [[Adversarial Search Index]]
    
- Optimization: [[Alpha-Beta Pruning]]