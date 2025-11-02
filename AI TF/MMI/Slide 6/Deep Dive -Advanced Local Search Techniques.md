
Tags: #ai #search #optimization #probabilistic #evolutionary

This note explores advanced algorithms designed to solve the primary problem of [[01_Local_Search_and_Hill_Climbing|Hill Climbing]]: getting stuck in local maxima.

These methods introduce clever ways to _escape_ these traps and explore more of the state space.

## 1. Simulated Annealing

This is the most direct solution to the local maximum problem. It's a [[01_Local_Search_and_Hill_Climbing|Hill Climbing]] algorithm that _allows_ "bad" (downhill) moves.

The core idea is borrowed from metallurgy (annealing), where heating and slowly cooling a metal allows its crystal structure to settle into a low-energy, stable state.

**Algorithm:**

1. Start like Hill Climbing, with a `current` state.
    
2. Also start with a high "Temperature" `T`.
    
3. Pick a _random_ neighbor, `next`.
    
4. Calculate `ΔE = VALUE(next) - VALUE(current)`.
    
    - `ΔE` > 0: This is a "good" (uphill) move. **Always accept it.** `current = next`.
        
    - `ΔE` <= 0: This is a "bad" (downhill) move. **Accept it with a probability.**
        
        - `Probability = e^(ΔE / T)`
            

**How `T` (Temperature) Works:**

- **High `T` (Start):** `T` is large. `ΔE / T` is a small negative number. `e^(ΔE / T)` is close to 1. The algorithm is "hot" and frequently accepts bad moves, allowing it to "jump" out of local maxima and explore the landscape freely.
    
- **Low `T` (End):** Over time, `T` is slowly decreased (the "cooling schedule"). `T` approaches 0. `ΔE / T` becomes a large negative number. `e^(ΔE / T)` approaches 0. The algorithm becomes "cold" and greedy, accepting only good moves, allowing it to settle into the _best_ peak it has found.
    

If `T` is cooled slowly enough, Simulated Annealing is theoretically guaranteed to find the _global_ optimum. Its main drawback is that it can be very slow if the cooling schedule is too gradual.

## 2. Genetic Algorithms (GAs)

Genetic Algorithms take a completely different, population-based approach inspired by biological evolution. They are very good at exploration.

Instead of one "hiker," a GA maintains a "population" of `k` states.

**Terminology:**

- **State (or "Individual"):** A single state, often represented as a string (e.g., a binary string, or a string of 8 numbers `[2,4,7,4,8,5,5,2]` for 8-Queens).
    
- **Fitness Function:** The objective function. Higher values = "fitter" individuals.
    
- **Generation:** A single loop of the algorithm.
    

**Algorithm:**

1. **Initial Population:** Start with `k` randomly generated states (individuals).
    
2. **Loop (for each generation):** a. **Selection:** Select two "parent" states from the current population. Fitter individuals have a higher probability of being chosen. b. **Crossover:** Create one or more "child" states by combining the parents. This is the key exploration step. * _Example:_ `Parent 1: [2,4,7,4] | [8,5,5,2]` * `Parent 2: [3,2,7,5] | [2,4,1,1]` * `Child: [2,4,7,4] | [2,4,1,1]` (Takes first half of P1, second half of P2) c. **Mutation:** With a small random probability, apply a small random change to the child (e.g., flip one number: `[2,4,7,4,2,4,1,1]` -> `[2,4,**1**,4,2,4,1,1]`). This maintains diversity and prevents the population from becoming too similar.
    
3. **New Population:** The new children form the next generation's population.
    
4. **Termination:** Stop after a fixed number of generations or when a sufficiently "fit" individual is found.
    

**Pros:** Crossover allows the algorithm to make large, non-local "jumps" in the search space, combining good features from different solutions. **Cons:** Can be complex and has many "tunable parameters" (population size, selection method, crossover rate, mutation rate) that are difficult to get right.

## 3. Gradient Descent (for Continuous Spaces)

This algorithm is a bit different. Simulated Annealing and GAs are typically used for _discrete_ state spaces (like 8-Queens). Gradient Descent is the "hill climbing" equivalent for **continuous** state spaces.

This is the foundational algorithm for training most modern Machine Learning models.

- **Goal:** _Minimize_ a cost function `C(w)` (e.g., the "error" of a model).
    
- **State:** A vector of continuous parameters `w` (the "weights" of the model).
    
- **Problem:** We can't check all "neighbors" because there are infinitely many.
    

**The Calculus Solution:** The **gradient** (`∇C`) is a vector that points in the direction of the _steepest possible ascent_ (uphill).

Therefore, to go _downhill_ (to minimize our error), we must take a small step in the **opposite** direction of the gradient.

**The Update Rule (Algorithm):** You just repeat this one line over and over:

`w_new = w_current - (λ * ∇C(w_current))`

- `w`: The current vector of weights.
    
- `∇C(w)`: The gradient of the cost function (calculated using calculus).
    
- `λ` (lambda): The **learning rate** (or "step size"). A small positive number that determines how big of a step to take.
    

This algorithm is just "valley-finding" in a continuous, high-dimensional landscape. It _also_ suffers from getting stuck in local minima, and much of modern ML research is about finding clever ways (like Momentum or ADAM) to make this simple process work better.

### Related Notes

- **Back to basics:**  [[Deep Dive - Local Search and Hill Climbing]]