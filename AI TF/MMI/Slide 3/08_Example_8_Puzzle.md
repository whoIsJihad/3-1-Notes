# 🧩 Example: 8-Puzzle

**Problem:** Slide tiles in a $3 \times 3$ grid from a **Start State** to a fixed **Goal State**.

## Problem Formulation

- **States:** The specific locations of the 8 numbered tiles and the one blank space.
    
- **Initial State:** The given starting arrangement.
    
- **Actions/Operators:** Move the blank space: **Left, Right, Up, or Down**.
    
    - _Note:_ The blank space can only move if a neighboring tile exists to swap with.
        
- **Goal Test:** Does the current state match the desired Goal State configuration?
    
- **Path Cost:** 1 per move (each tile slide counts as a single step).