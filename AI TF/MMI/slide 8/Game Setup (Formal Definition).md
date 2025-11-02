# Game Setup (Formal Definition)

A game can be formally defined as a search problem with the following components:

1. **Players:** Typically two, [[Minimax Algorithm|MAX]] and MIN. MAX moves first.
    
2. **Initial State:** The board configuration at the start of the game.
    
3. **Successor Function:** A list of `(move, state)` pairs specifying all legal moves from a given state.
    
4. **Terminal Test:** A function that determines if the game is over (e.g., checkmate, board full).
    
5. **Utility Function (or Payoff Function):** Gives a numerical value for a terminal state.
    
    - e.g., Win (+1), Lose (-1), Draw (0).
        

The game search tree's size is $O(b^d)$, where:

- `b` = branching factor (legal moves)
    
- `d` = depth (number of moves)
    

For Chess, $b \approx 35$ and $d \approx 100$, making the tree $O(35^{100})$, which is impractically large to search fully.

**Links:**

- Back to: [[Adversarial Search Index]]
    
- Next: [[Minimax Algorithm]]