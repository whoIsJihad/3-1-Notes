# 💧 Example: Water Jug Problem (3- and 4-Gallon)

**Problem:** Using a 4-gallon jug and a 3-gallon jug (with unlimited water supply), measure **exactly 2 gallons** in the 4-gallon jug.

## Problem Formulation

- **State Representation:** A pair $(x, y)$.
    
    - $x$: Gallons in the 4-gallon jug ($0 \le x \le 4$).
        
    - $y$: Gallons in the 3-gallon jug ($0 \le y \le 3$).
        
- **Start State:** $(0, 0)$.
    
- **Goal State:** $(2, n)$ (2 gallons in the 4-gallon jug, $n$ is any amount in the 3-gallon jug).
    
- **Operators (Actions):** Defined by 10 **Production Rules** (e.g., fill jug, empty jug, pour between jugs).
    

## Key Production Rules

|Rule|Action|Condition|State Transition Example|
|---|---|---|---|
|**R1**|Fill 4-gallon jug.|if $x<4$|$(x, y) \to (4, y)$|
|**R6**|Empty 3-gallon jug.|if $y>0$|$(x, y) \to (x, 0)$|
|**R9**|Pour all 3-gal to 4-gal.|if $x+y \le 4$ and $y>0$|$(x, y) \to (x+y, 0)$|
|**R7**|Pour 3-gal to 4-gal until 4-gal is full.|if $x+y \ge 4$ and $y>0$|$(x, y) \to (4, y-(4-x))$|

**A Solution Path (Example):** $(0, 0) \xrightarrow{R2} (0, 3) \xrightarrow{R9} (3, 0) \xrightarrow{R2} (3, 3) \xrightarrow{R7} (4, 2) \xrightarrow{R5} (0, 2) \xrightarrow{R9} (2, 0) \to \text{GOAL!}$