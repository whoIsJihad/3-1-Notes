
Hey there! Let's break down the fundamentals of Constraint Satisfaction Problems, or CSPs. This is a core topic in AI, and understanding it well really helps with a whole class of search and planning problems.

This note covers the "what" and "why" of CSPs. For the "how" (the algorithms), see the companion note: [[CSP Solving Algorithms Deep Dive]].

## What is a Constraint Satisfaction Problem?

Think about a standard search problem (like finding a path in a maze). You have a "black box" state, a successor function, and a goal test. You could use BFS, DFS, A*, etc., to find a path from start to goal.

**CSPs are different.** They represent a more specialized, structured kind of problem. Instead of a generic "state," we have a clear, factored representation:

- **Variables (**$X$**):** A set of variables, $\{X_1, X_2, ..., X_n\}$.
    
- **Domains (**$D$**):** A set of domains, $\{D_1, D_2, ..., D_n\}$, where each $D_i$ is the set of possible values for variable $X_i$.
    
- **Constraints (**$C$**):** A set of constraints that specify allowable combinations of values for subsets of variables.
    

The **Goal** is to find a **complete and consistent assignment**—an assignment where every variable has a value from its domain, and no constraints are violated.

This structure is powerful because it allows us to create general-purpose algorithms that are much more efficient than the "black box" search algorithms.

## Core Example: Map Coloring

The classic example you'll always see is **Map Coloring**. Let's use the Australian states from your lecture.

- **Variables (**$X$**):** The states themselves. `X = {WA, NT, SA, Q, NSW, V, T}`.
    
- **Domains (**$D$**):** The set of available colors. `D_i = {red, green, blue}` for all variables.
    
- **Constraints (**$C$**):** No two adjacent regions can have the same color.
    
    - `WA ≠ NT`
        
    - `WA ≠ SA`
        
    - `NT ≠ SA`
        
    - `NT ≠ Q`
        
    - `SA ≠ Q`
        
    - `SA ≠ NSW`
        
    - `SA ≠ V`
        
    - `Q ≠ NSW`
        
    - `NSW ≠ V`
        

A **solution** would be an assignment like: `{WA=red, NT=green, SA=blue, Q=red, NSW=green, V=red, T=green}`.

### Visualizing: The Constraint Graph

We can visualize this as a **Constraint Graph**. It's simple:

- **Nodes:** The variables (e.g., WA, NT, SA).
    
- **Edges (or Arcs):** The binary constraints between them (e.g., an edge between WA and NT).
    

This graph isn't just a pretty picture; it helps us reason about the problem's structure. For instance, `T` (Tasmania) has no constraints with any other state, so it's a disconnected node in the graph.

## More Examples

CSPs pop up everywhere:

- **Cryptarithmetic:** Like the `TWO + TWO = FOUR` puzzle.
    
    - **Variables:** The letters `F, T, U, W, R, O` and the carry-over variables `X1, X2, X3`.
        
    - **Domains:** `{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}` for the letters, `{0, 1}` for the carries.
        
    - **Constraints:**
        
        - `Alldiff(F, T, U, W, R, O)` (all letters are unique).
            
        - The arithmetic rules: `O + O = R + 10*X1`, `X1 + W + W = U + 10*X2`, etc.
            
        - `F ≠ 0`, `T ≠ 0`.
            
- **N-Queens:** Place N queens on an N×N chessboard so no two attack each other.
    
- **Real-world Problems:**
    
    - **Timetabling:** Assigning courses to rooms/times (Variables: courses; Domains: {Room, Time} pairs; Constraints: No two courses in the same room at the same time, professor can't be in two places at once).
        
    - **Scheduling:** Factory jobs, transportation logistics.
        
    - **Sudoku:** A classic CSP!
        

## Varieties of CSPs & Constraints

Just so you know the terminology:

- **By Domain Type:**
    
    - **Discrete Variables:**
        
        - **Finite Domains:** (like Map Coloring, N-Queens). This is what we're focusing on. The number of possible assignments is $O(d^n)$.
            
        - **Infinite Domains:** (e.g., variables are integers). Requires a constraint language (e.g., `StartJob_1 + 5 ≤ StartJob_3`).
            
    - **Continuous Variables:** (e.g., start/end times for Hubble telescope). Often solved with linear programming.
        
- **By Constraint Type:**
    
    - **Unary:** Involves a single variable (e.g., `SA ≠ green`).
        
    - **Binary:** Involves two variables (e.g., `SA ≠ WA`). Most common.
        
    - **Higher-order:** Involves 3+ variables (e.g., the arithmetic in Cryptarithmetic).
        

**Next up:** Now that we know _what_ a CSP is, let's explore _how_ to solve them.

[[CSP Solving Algorithms Deep Dive]]