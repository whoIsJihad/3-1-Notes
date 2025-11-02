
We know [[Heuristics - The 'Rules' for A-Star Optimality|A* needs good heuristics]], but how do we _invent_ them? And how do we _compare_ two good heuristics?

### 1. How to Invent Admissible Heuristics

#### Technique A: Relaxed Problems

This is the most powerful method.

1. Start with your original problem's rules (e.g., "a tile can move to an adjacent _empty_ square").
    
2. Create a **relaxed problem** by removing restrictions (e.g., "a tile can move to an adjacent square, even if it's occupied").
    
3. The _optimal solution cost_ in the relaxed problem is an admissible heuristic for the _original_ problem.
    

Why? The "true" problem is a subset of the relaxed one. The optimal path in the relaxed problem _must_ be shorter than or equal to the optimal path in the true problem (since you have more "shortcuts" available).

**Case Study: 8-Puzzle Heuristics**

- $h_1$ **(Misplaced Tiles):**
    
    - **Relaxed Problem:** "A tile can move from any square to any _other_ square in one step."
        
    - **Optimal Cost:** The number of tiles not in their goal spot.
        
    - **Is it admissible?** Yes.
        
- $h_2$ **(Manhattan Distance):**
    
    - **Relaxed Problem:** "A tile can move to any _adjacent_ square (up, down, left, right) in one step, ignoring other tiles."
        
    - **Optimal Cost:** The sum of the (x, y) distances for each tile from its goal (the "Manhattan distance").
        
    - **Is it admissible?** Yes.
        

#### Technique B: Pattern Databases

1. Identify a _subproblem_ (e.g., for the 8-puzzle, just the cost of getting tiles 1, 2, 3, 4 into their correct goal squares, ignoring all others).
    
2. **Pre-compute** the _exact, optimal_ solution cost for _every possible configuration_ of that subproblem.
    
3. Store these costs in a giant lookup table (a "pattern database").
    
4. Your heuristic $h(n)$ is just a fast lookup in this table. This is guaranteed to be admissible because the cost to solve the subproblem is always less than or equal to the cost of solving the full problem.
    

### 2. How to Compare Admissible Heuristics

Let's say you have two admissible heuristics, $h_1$ and $h_2$. Which is better?

#### Concept A: Dominance

- **Definition:** $h_2$ **dominates** $h_1$ if, for _every_ node $n$, $h_2(n) \ge h_1(n)$.
    
- **The Logic:** Both are admissible (optimistic), but $h_2$ is "less optimistic" and more accurate. It provides a _tighter_ lower bound on the true cost.
    
- **Impact:** [[Informed Search Algorithms - Greedy vs. A*|A* Search]] using $h_2$ will expand _at most_ as many nodes as A* using $h_1$. It is provably more efficient.
    
- **Example:** For the 8-puzzle, $h_2$ (Manhattan) **dominates** $h_1$ (misplaced). $h_2$ is always the better choice.
    

#### Concept B: Effective Branching Factor ($b^*$)

This is a practical, experimental way to measure a heuristic's quality.

1. Run A* on a set of problems.
    
2. Count the total number of nodes expanded, $N$.
    
3. Find the solution depth, $d$.
    
4. Calculate the **effective branching factor,** $b^*$, which is the branching factor a _uniform, uninformed_ tree would need to have to contain $N+1$ nodes at depth $d$. $N+1 = 1 + b^* + (b^*)^2 + ... + (b^*)^d$
    
5. **A lower** $b^*$ **is better.** A "perfect" heuristic would have $b^*=1$.
    

**Example (8-Puzzle,** $d=24$**):**

- **IDS (uninformed):** $b \approx 2.8$
    
- __A_ with_ $h_1$ _(misplaced):_* $b^* \approx 1.48$
    
- __A_ with_ $h_2$ _(Manhattan):_* $b^* \approx 1.26$
    

This clearly shows $h_2$ is far more efficient, as it makes the search tree "skinnier."

_Back to: [[Heuristics - The 'Rules' for A-Star Optimality]]_ _Next up: [[The Problem with A-Star - Memory]]_