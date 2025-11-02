
Welcome to the deep dive on _solving_ CSPs! In [[CSP Concepts and Motivation]], we defined what CSPs are (Variables, Domains, Constraints). Now, let's figure out how to find a solution.

The most fundamental and important algorithm to understand is **Backtracking Search**.

## 1. Backtracking Search (The Foundation)

A naive approach might be to just generate _all_ possible complete assignments and then check if they're valid. But with $n$ variables and domain size $d$, that's $O(d^n)$ assignments, which is way too slow.

A smarter approach is **Backtracking Search**.

**The Idea:** It's basically a depth-first search (DFS) where we build a solution one variable at a time.

1. Pick an unassigned variable.
    
2. Try to assign it a value from its domain.
    
3. Check if this assignment conflicts with any _already assigned_ variables.
    
    - **If NO conflict:** Move on and recursively assign the next variable.
        
    - **If YES conflict:** This value won't work. Try the next value in the domain.
        
4. If you run out of values for a variable, you've hit a dead end. **Backtrack** to the _previous_ variable and try a different value for _it_.
    
5. If you successfully assign all variables, you've found a solution!
    

### Backtracking Pseudocode

This is the algorithm from your lecture, explained.

```
function BACKTRACKING-SEARCH(csp) returns a solution or failure
    return RECURSIVE-BACKTRACKING({}, csp)

function RECURSIVE-BACKTRACKING(assignment, csp) returns a solution or failure
    // Check if we're done
    if assignment is complete then return assignment
    
    // Get the next variable to try
    var = SELECT-UNASSIGNED-VARIABLE(csp)
    
    // Try each value for that variable
    for each value in ORDER-DOMAIN-VALUES(var, assignment, csp) do
        // Check if this value is consistent with what we've already assigned
        if value is consistent with assignment then
            // 1. CHOOSE
            add {var = value} to assignment
            
            // 2. EXPLORE
            result = RECURSIVE-BACKTRACKING(assignment, csp)
            
            // If the recursive call found a solution, pass it up!
            if result ≠ failure then return result
            
            // 3. UN-CHOOSE (This is the "backtrack" step)
            // The recursive call failed, so this value was a dead end.
            // Remove it and try the next value in the loop.
            remove {var = value} from assignment
            
    // If we've tried all values and none worked, we failed.
    return failure
```

## 2. Improving Backtracking (Making It Fast)

Standard backtracking is still too slow. The algorithm above has two "magic" functions: `SELECT-UNASSIGNED-VARIABLE` and `ORDER-DOMAIN-VALUES`.

We can be _much_ smarter about these choices. This leads to **heuristics**.

### Strategy 1: Smart Heuristics (Better Ordering)

#### Which **Variable** to Assign Next?

**Heuristic 1: Most Constrained Variable (MRV)**

- **Also known as:** "Minimum Remaining Values"
    
- **The Idea:** Choose the variable that has the **fewest legal values** left in its domain.
    
- **Why?** This is a "fail-fast" strategy. If a variable has only one value left, you _must_ assign it. If it has zero values left, you know you need to backtrack _now_, saving you from going down a long, doomed path.
    

**Heuristic 2: Most Constraining Variable (Degree Heuristic)**

- **The Idea:** If there's a tie for MRV, pick the variable that is involved in the **most constraints** with _other unassigned_ variables.
    
- **Why?** This variable "constrains" its neighbors the most. Getting it assigned and "locked down" first helps prune the search tree by affecting the domains of its neighbors earlier.
    

#### Which **Value** to Assign First?

**Heuristic 3: Least Constraining Value**

- **The Idea:** Once you've picked a variable, try the value that **rules out the fewest values** in the domains of its neighboring _unassigned_ variables.
    
- **Why?** This is the opposite of the variable heuristics. For values, you want to be "optimistic." You want to pick the value that leaves the most flexibility for your future choices, maximizing the chance of finding a solution.
    

### Strategy 2: Inference (Early Failure Detection)

Heuristics are good, but we can also detect failure even earlier by **propagating** the implications of our choices.

#### Inference 1: Forward Checking

This is the simplest form of inference.

- **The Idea:** When you assign a value to a variable (e.g., `WA = red`), don't just sit there. **Look ahead!**
    
- Go to all _unassigned_ neighboring variables (like `NT` and `SA`) and remove the conflicting value (`red`) from _their_ domains.
    
- **The Payoff:** If, during this process, any neighbor's domain becomes **empty**, you know _immediately_ that your assignment (`WA = red`) was a mistake. You can backtrack right away, without even trying to assign `NT` or `SA`.
    

Forward checking is better than plain backtracking, but it's not perfect. It doesn't detect _all_ future failures.

#### Inference 2: Arc Consistency (AC-3)

This is the more powerful, "deep dive" version of inference.

- **Core Idea:** An **arc** $(X_i, X_j)$ is **consistent** if for **every** value $x$ in $X_i$'s domain, there is **some** value $y$ in $X_j$'s domain that satisfies the constraint between them.
    
- If an arc is _not_ consistent, we can remove the "bad" value(s) from $X_i$'s domain, because we know they can't possibly be part of a solution.
    
- **The Algorithm (AC-3):**
    
    1. Start with a queue of _all_ arcs (binary constraints) in the CSP.
        
    2. While the queue is not empty, pop an arc $(X_i, X_j)$.
        
    3. Check if it's consistent.
        
    4. For every value $x$ in $D_i$:
        
        - If there's no allowed $y$ in $D_j$, then $x$ is bad. **Remove** $x$ **from** $D_i$.
            
    5. **Crucial Step:** If you _did_ remove any values from $D_i$, then _all other arcs pointing to_ $X_i$ (like $(X_k, X_i)$) might now be inconsistent. **Add all those arcs** $(X_k, X_i)$ **back into the queue** to be re-checked.
        
    6. Repeat until the queue is empty.
        

You can run AC-3 _before_ you start backtracking, or even _during_ backtracking (after each assignment) to prune the domains as you go.

##### AC-3 Pseudocode

```
function AC-3(csp) returns the CSP (with potentially reduced domains)
    // 1. Initialize queue with all arcs
    queue = all arcs in csp
    
    while queue is not empty do
        (Xi, Xj) = REMOVE-FIRST(queue)
        
        // Check if we can prune Xi's domain using Xj
        if RM-INCONSISTENT-VALUES(Xi, Xj) then
            // If we pruned Xi, we must re-check all its neighbors
            for each Xk in NEIGHBORS[Xi] (excluding Xj) do
                add (Xk, Xi) to queue
                
function RM-INCONSISTENT-VALUES(Xi, Xj) returns true iff a value was removed
    removed = false
    for each x in DOMAIN[Xi] do
        // Check if there is ANY value y in Xj's domain that works with x
        if no value y in DOMAIN[Xj] allows (x,y) to be consistent then
            // If not, x can never be part of a solution
            delete x from DOMAIN[Xi]
            removed = true
    return removed
```

## 3. Alternative: Local Search (Min-Conflicts)

Backtracking is a _systematic_ search. It's guaranteed to find a solution if one exists (it's "complete").

An alternative is **Local Search**.

- **The Idea:**
    
    1. Start with a _complete_ assignment, even if it's full of conflicts (e.g., just assign a random color to every state).
        
    2. Iteratively _fix_ the conflicts.
        
- **The Min-Conflicts Heuristic:**
    
    1. Randomly pick a variable that is currently in conflict (e.g., `SA` is red, and its neighbor `WA` is also red).
        
    2. Re-assign that variable a _new_ value—specifically, the value that causes the **minimum number of conflicts** with its neighbors. (e.g., if `NT` is green and `Q` is green, changing `SA` to blue causes 0 conflicts, while changing it to green would cause 2).
        
    3. Repeat until no conflicts remain.
        

This approach is surprisingly fast and effective, especially for large problems like N-Queens (it can solve $n=1,000,000$ queens!). It's not "complete" (it can get stuck in local minima), but in practice, it's very powerful.