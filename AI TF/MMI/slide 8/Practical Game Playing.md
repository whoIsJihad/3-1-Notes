# Practical Game Playing

Because game trees are too large to search fully, we must apply practical limits.

## 1. Cutoff Test

Instead of searching to terminal nodes, we stop at a certain depth (e.g., depth limit `d`). This is often implemented with **Iterative Deepening Search (IDS)**, which runs DFS with increasing depth limits (d=1, d=2, ...) until the time limit runs out.

When the search is cut off, we must estimate the node's utility. This is done by an evaluation function.

## 2. Static (Heuristic) Evaluation Function

An evaluation function, `Eval(s)`, estimates the "goodness" of a game state `s` for a player.

- It's used when a search is cut off before a terminal node.
    
- For zero-sum games, `Eval_MAX(s) = -Eval_MIN(s)`.
    
- Typically a **linear weighted sum of features**: `Eval(s) = w1*f1(s) + w2*f2(s) + ... + wn*fn(s)`
    
- **Example (Chess):**
    
    - `f1(s)` = (num white queens) - (num black queens)
        
    - `w1` = 9 (value of a queen)
        
    - `f2(s)` = (num white rooks) - (num black rooks)
        
    - `w2` = 5 (value of a rook)
        

## 3. The Horizon Effect

A problem where the search cuts off just before a major event (like a piece capture). The program has a "limited horizon" and can't see the impending doom or opportunity.

- **Solution (Quiescence Search):** If a state is "unstable" (e.g., in the middle of a capture), search deeper along that specific branch until the position becomes "quiet" or stable.
    

**Links:**

- Back to: [[Adversarial Search Index]]
    
- See also: [[Chance Games]]