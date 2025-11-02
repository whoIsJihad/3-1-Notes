
Tags: #ai #neural_networks #optimization #simulated_annealing #metaheuristic

This note is a deep dive into Simulated Annealing, a powerful metaheuristic algorithm for optimization, based on Chapter 1 of the "Alternative Learning Algorithms" PDF.

## 1. The Core Concept: The Physics Analogy

Simulated Annealing (SA) is directly analogous to the process of **annealing in metallurgy**, where a solid is heated and then cooled slowly to achieve a perfect, stable crystal structure.

1. **Heat:** A solid is heated in a bath until it melts. At high temperatures, the atoms have high energy and move randomly.
    
2. **Slow Cool:** The temperature is decreased _very slowly_. This slow-cooling process gives the atoms "more chances to rearrange" and settle into their "ground state"—a highly regular crystal structure that represents the **minimum energy state** for the system.
    
3. **Quenching:** If the solid is cooled _too quickly_ (quenching), the atoms get locked in place in a "polycrystalline or amorphous state," which has a _higher_ energy. This is a **local minimum**.
    

A greedy algorithm like Hill Climbing is analogous to **quenching**—it finds the _nearest_ minimum-energy state and gets stuck. Simulated Annealing is analogous to **slow cooling**—it explores high-energy states and slowly "cools" to find the _global_ minimum.

## 2. The Metropolis Algorithm (The Core Logic)

In 1953, Metropolis et al. created an algorithm to simulate this physical process. This is the heart of SA.

It defines a probabilistic criterion for accepting new states:

- Let the current state be `i` with energy `Ei`.
    
- Generate a new, randomly perturbed "neighbor" state `j` with energy `Ej`.
    
- Calculate the change in energy: `ΔE = Ej - Ei`.
    

**The Metropolis Criterion:**

- **If `ΔE ≤ 0`:** The new state has lower (or equal) energy. This is a "good" move. **Always accept it.**
    
- **If `ΔE > 0`:** The new state has higher energy. This is a "bad" move. **Accept it with a probability, `P`**:
    
    `P(accept) = exp(-ΔE / T)` _(Note: `T` is the current temperature, and `kB`, the Boltzmann constant, is usually "baked into" `T` in computational models)._
    

This is the key. **"Accepting deterioration... facilitates simulated annealing to escape from local optima."**

## 3. The SA Method for Optimization

We can translate this physics analogy directly to an optimization problem (like training a neural network):

|Physics Term|Optimization Term|
|---|---|
|System State (`i`)|Current Solution (`x`, e.g., the vector of weights)|
|Energy (`E`)|Objective Function (`f(x)`, e.g., the network's error)|
|Ground State|Global Optimum (Global Minimum Error)|
|Temperature (`T`)|Control Parameter (`T`)|
|Perturbation|Generator of random variations (`Δx`)|

The algorithm (from page 15) then becomes:

```
function SimulatedAnnealing(x0, T0, n, m):
  // Initialize
  T = T0                 // Set initial temperature
  x = x0                 // Set initial solution
  x* = x                 // Initialize best solution found so far

  // Outer Loop (Cooling)
  for k = 1 to n:        // n = number of temperature steps
    
    // Inner Loop (Thermal Walk)
    for j = 1 to m:    // m = steps at each temperature
      
      // 1. Generate a neighbor
      x_tilde = Neighbor(x)
      
      // 2. Calculate energy change
      ΔE = E(x_tilde) - E(x)
      
      // 3. Decide to accept or reject
      p = min(exp(-ΔE / T), 1)
      u = Uniform(0, 1)      // Get a random number between 0 and 1
      
      // 4. Accept? (Move if better, or probabilistically if worse)
      if u < p:
        x = x_tilde
        
      // 5. Update Best? (Keep track of the best solution ever found)
      if E(x) < E(x*):
        x* = x
        
    // End Inner Loop
    
    // 6. Decrement Temperature (using a cooling schedule)
    T = T0 / (k + 1)     // Example: Inverse linear schedule
    
  // End Outer Loop
  
  // 7. Return the best solution found
  return x*
```

## 4. The Two Critical Components

For this to work in practice, you need to define two things:

### A) The Generating Function (How to pick `Δx`)

This function generates the random step `Δx`. For continuous parameters (like network weights), this is usually done by sampling from a probability distribution. The PDF discusses two:

- **Gaussian Distribution:**
    
    - Has a central maximum and short tails.
        
    - The variance (`σ²`) is analogous to `T`.
        
    - **High `T`:** Large variance, "long flat tail" -> Generates large `Δx` steps -> **Exploration**.
        
    - **Low `T`:** Small variance, "large central maximum" -> Generates small `Δx` steps -> **Exploitation** (fine-tuning).
        
- **Cauchy Distribution:**
    
    - Also has a central maximum, but with _much longer, flatter tails_ (its variance is infinite).
        
    - This means it is _more likely_ to generate a very large `Δx` (a huge jump) than a Gaussian.
        
    - **Benefit:** This gives it a "higher probability of escaping from a local optimum."
        

### B) The Annealing Schedule (How to cool `T`)

This is the plan for lowering the temperature `T` and is critical to the algorithm's success. It has four parts:

1. **Initial Temperature (`T0`):** Must be high enough to "melt" the system (e.g., accept ~80% of bad moves). This is problem-specific.
    
2. **Temperature Decrement Rule:** The _how_ of cooling.
    
    - **Geometric (Kirkpatrick et al.):** `T(t) = α^t * T0` (e.g., `α = 0.9`). This is very common.
        
    - **Logarithmic (Geman & Geman):** `T(t) = T0 / log(1 + t)`. This is "proven... to lead to the global minimum... in the limit of infinite time," but is "impractical" because it's so slow.
        
    - **Inverse Linear (Szu & Hartley):** `T(t) = T0 / (1 + t)`. This is much faster.
        
3. **Steps at Each Temperature (`m`):** This is the **inner loop**. You must run _many_ steps (`m`) at _each_ temperature to allow the system to "walk" and reach equilibrium before you cool it further.
    
4. **Stopping Criterion:** When to stop. Usually a fixed number of outer loops (`n`), a final (low) temperature, or when the best solution (`x*`) hasn't improved for a long time.