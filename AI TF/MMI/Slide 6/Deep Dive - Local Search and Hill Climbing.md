
Tags: #ai #search #optimization #greedy

This note covers the fundamental concept of local search and provides a detailed look at its simplest implementation, Hill Climbing, along with its common pitfalls and variations.

## 1. What is Local Search?

In many problems (like 8-Queens or optimization tasks), we don't care _how_ we get to a solution; we only care about the final state itself. This is different from path-finding algorithms (like A* or Dijkstra) where the _path_ is the solution.

Local search algorithms embrace this idea. They operate using a simple loop:

1. Start with a single `current state` (e.g., a random 8-Queens board).
    
2. Move to one of its "neighboring states" (e.g., a board where one queen has moved).
    
3. Repeat until a solution is found or we get stuck.
    

**Key Characteristics:**

- **Low Memory:** They only keep track of the `current state`, not a massive frontier or path history. This is their biggest advantage.
    
- **Scalability:** Because they use so little memory, they can find _reasonable_ (though not always optimal) solutions in massive or even infinite (continuous) state spaces where systematic searches would instantly fail.
    
- **Suitability:** They are ideal for **pure optimization problems**, where the goal is to find a state that maximizes (or minimizes) an **objective function** (also called a "cost function" or "heuristic").
    

### The State-Space Landscape Metaphor

This is the most important concept for understanding all local search algorithms. Imagine the state space as a 3D landscape:

- **State:** A position (x, y) on the landscape.
    
- **Objective Function:** The altitude (z) at that position.
    
- **Goal (for maximization):** Find the highest mountain peak on the entire map.
    
- **Goal (for minimization):** Find the lowest valley on the entire map.
    

A local search algorithm is like a person hiking in this landscape in a thick fog. They can only feel the ground right where they are and at their immediate neighboring steps.

## 2. Hill-Climbing: The "Greedy" Hiker

Hill-Climbing is the most basic, "greed-is-good" local search algorithm. It's the hiker that _always_ takes the steepest possible step uphill.

It continuously moves in the direction of increasing value until it reaches a "peak" where no neighbor has a higher value.

### Pseudocode (Maximization)

```
function HILL-CLIMBING(problem):
  // Start at a random "location"
  current = MAKE-NODE(INITIAL-STATE)

  loop do:
    // Check all immediate neighbors
    neighbor = The highest-valued successor of current

    // If no neighbor is higher, we're at a peak. We're done.
    if VALUE(neighbor) <= VALUE(current):
      return STATE(current)
    
    // Otherwise, take that one best step.
    current = neighbor
```

### Example: 8-Queens as a Minimization Problem

We can frame 8-Queens as a local search (minimization) problem:

- **State:** A complete state with all 8 queens on the board (one per column).
    
- **Neighboring State:** A state reachable by moving a _single_ queen to another square _in the same column_.
    
- **Objective Function:** We want to _minimize_ a heuristic `h(n)`, defined as "the number of pairs of queens that are attacking each other." A perfect solution has `h(n) = 0`.
    
- **Hill-Climbing (Minimization):** In this case, it's "valley-finding." In each step, the algorithm finds the queen-move that results in the _lowest_ `h` value (the fewest attacks) and takes it.
    

## 3. The Problems: Why Hill Climbing Gets Stuck

The "thick fog" and "greedy" strategy is fast, but it often fails. Our hiker gets stuck on "false peaks."

- **Local Maximum:** This is a "foothill" that is higher than all its neighbors but is _not_ the true, global maximum (the highest peak on the map). Hill Climbing will stop here, satisfied with its suboptimal solution.
    
- **Plateau (or "Shoulder"):** An area of the state space where the evaluation function is flat. The hiker reaches a flat area and, seeing no "uphill" step, stops, even though a path across the plateau might lead to another upward slope.
    
- **Ridge:** A narrow crest in the landscape that is hard to navigate. A greedy algorithm might get stuck oscillating back and forth on the ridge, as any single move might lead "downhill."
    

For the 8-Queens problem, basic Hill Climbing fails ~86% of the time by getting stuck in a local minimum (e.g., a board with `h=1` that it can't improve).

## 4. Mitigations and Variations of Hill Climbing

We can make our hiker "smarter" to deal with these problems.

- **Sideways Moves:**
    
    - **Idea:** Allow the algorithm to move to a state with the _same_ value (i.e., walk across a plateau) for a limited number of steps, hoping to find an "uphill" move on the other side.
        
    - **Result (8-Queens):** Allowing 100 sideways moves increases the success rate from 14% to 94%.
        
- **Stochastic Hill Climbing:**
    
    - **Idea:** Don't _always_ pick the _best_ uphill move. Instead, randomly select from _all_ available uphill moves.
        
    - **Why?** A less-steep step might lead to a more promising region of the state space than the steepest-looking one.
        
- **First-Choice Hill Climbing:**
    
    - **Idea:** For state spaces with _millions_ of neighbors, checking them all is too slow. Instead, generate successors one by one at random until one is found that is better than the current state. Then, take that step immediately.
        
- **Random-Restart Hill Climbing:**
    
    - **Idea:** The simplest and often most effective solution. Just accept that Hill Climbing will get stuck.
        
    - **Algorithm:** Run Hill Climbing to completion. If the solution isn't good enough (or isn't the goal), _save the result_ and then _restart the entire process_ from a new, randomly generated initial state.
        
    - **Logic:** If the algorithm has a 14% chance of success, running it `k` times gives a much higher probability of finding the global optimum.
        
- **Local Beam Search:**
    
    - **Idea:** This is a more complex variant. Instead of one hiker, start with _k_ hikers (states) at random locations.
        
    - **Algorithm:**
        
        1. Start with `k` randomly generated states.
            
        2. In each step, generate _all_ successors for _all k_ states.
            
        3. If any is a goal, stop.
            
        4. Otherwise, select the _k best_ successors from the _entire list_ to be the _new_ population of `k` states.
            
    - **Key Difference:** This is _not_ just running `k` independent random-restarts. The `k` search "threads" share information. A successor from a "promising" state can out-compete and replace a "stuck" state, focusing the search on good areas.
        

### Next Steps

Hill Climbing's variations help, but they still struggle. The next logical step is to use algorithms that _systematically_ allow "bad" moves to escape local maxima.

- **See:** [[Deep Dive -Advanced Local Search Techniques]]