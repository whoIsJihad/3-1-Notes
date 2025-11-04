
---

# 🧬 Genetic Algorithm (GA) — Complete Notes

---

## 1️⃣ What is a Genetic Algorithm?

A **Genetic Algorithm (GA)** is a type of **evolutionary algorithm** inspired by **Charles Darwin’s theory of natural selection**.

It mimics biological evolution to **search for optimal or near-optimal solutions** to a problem.

In short:

> Genetic Algorithms evolve a population of candidate solutions through selection, crossover, and mutation — improving fitness over generations.

---

## 2️⃣ Real-Life Analogy

Think of evolution in nature:

- Individuals (organisms) have **genes**.
    
- Some are **fitter** — better adapted to the environment.
    
- The **fittest survive** and **reproduce**.
    
- Over generations, the population **evolves** towards better traits.
    

In GA:

- Each **individual** = a possible **solution**.
    
- **Genes** = parts (variables) of the solution.
    
- **Fitness** = how good the solution is.
    
- Over many generations, solutions evolve to better ones.
    

---

## 3️⃣ General GA Structure

Every GA has these key steps:

|Step|Description|
|---|---|
|1. **Initialization**|Start with a random population of candidate solutions.|
|2. **Evaluation**|Compute fitness (how good each solution is).|
|3. **Selection**|Choose better individuals for reproduction.|
|4. **Crossover (Recombination)**|Combine pairs of individuals to produce offspring.|
|5. **Mutation**|Randomly change small parts of offspring for diversity.|
|6. **Replacement**|Form the next generation from offspring (and sometimes best old ones).|
|7. **Termination**|Stop when a criterion is met (max generations or good enough fitness).|

---

## 4️⃣ Representation (Chromosome Encoding)

A **chromosome** represents one possible solution.  
Each chromosome consists of **genes**, representing **decision variables**.

### Common encodings:

|Problem type|Representation example|
|---|---|
|Binary optimization|1011010110|
|Real-valued optimization|[2.5, 0.3, -1.2, 5.0]|
|Travelling Salesman Problem|[City3, City1, City4, City2, City5] (a permutation)|

---

## 5️⃣ Fitness Function

The **fitness function** measures how good a solution is.

- It maps a chromosome → a single **score** (higher = better).
    
- It depends entirely on the problem.
    

Examples:

- Maximize profit → fitness = profit
    
- Minimize distance → fitness = 1 / distance
    
- Minimize error → fitness = 1 / (1 + error)
    

The GA uses this fitness to guide evolution.

---

## 6️⃣ Selection

**Goal:** Prefer better solutions while still keeping diversity.

### Common methods:

1. **Roulette Wheel Selection (Fitness Proportionate):**
    
    - Each chromosome gets a slice of a wheel proportional to fitness.
        
    - Spin the wheel to pick.
        
    - Problem: Can get stuck if one is too dominant.
        
2. **Tournament Selection:**
    
    - Randomly pick _k_ individuals.
        
    - The fittest among them wins.
        
3. **Rank Selection:**
    
    - Sort population by fitness.
        
    - Assign selection probability based on rank (not raw fitness).
        

---

## 7️⃣ Crossover (Recombination)

**Goal:** Create offspring by mixing genes from two parents.

Types vary by encoding:

### 🧩 Binary or Real-Valued GA:

- **Single-Point Crossover:** Split at one point and swap tails.
    
    ```
    Parent1: 101|101
    Parent2: 010|010
    Child:   101010
    ```
    
- **Two-Point Crossover:** Swap middle section.
    
- **Arithmetic Crossover:** Child = α * Parent1 + (1-α) * Parent2.
    

### 🚗 Permutation-based (like TSP):

- **Order Crossover (OX)**
    
- **Partially Mapped Crossover (PMX)**
    
- **Cycle Crossover (CX)**
    

These preserve city order and avoid duplicates.

---

## 8️⃣ Mutation

**Goal:** Introduce small random changes to maintain genetic diversity.  
Without mutation, GA might get stuck in a local optimum.

### Common types:

|Encoding|Mutation|
|---|---|
|Binary|Flip one bit (0→1 or 1→0)|
|Real|Add small random noise|
|Permutation|Swap two positions or reverse a segment|

Mutation rate is usually low (like 1–5%).

---

## 9️⃣ Replacement / Survivor Selection

Once offspring are created, the next generation must be formed.

Two common strategies:

- **Generational Replacement:** Replace the entire population with offspring.
    
- **Elitism:** Keep a few best individuals unchanged (to not lose best solutions).
    

---

## 🔟 Termination Criteria

GA runs until one of these:

- Reached max generations
    
- Found a solution with acceptable fitness
    
- No improvement for many generations
    

---

## 1️⃣1️⃣ Pseudo-Code of a Genetic Algorithm

```text
1. Initialize population P randomly
2. Evaluate fitness of each individual in P
3. Repeat until termination condition:
       a. Select parents from P
       b. Apply crossover to produce offspring
       c. Apply mutation to offspring
       d. Evaluate fitness of offspring
       e. Form new population from offspring (and possibly best old individuals)
4. Return the best individual found
```

---

## 1️⃣2️⃣ Example: Using GA for TSP

|Step|Description|
|---|---|
|Chromosome|Sequence of cities|
|Fitness|1 / total_distance|
|Crossover|Order crossover (OX)|
|Mutation|Swap two cities|
|Goal|Minimize total travel distance|

GA gradually improves the tour order each generation.

---

## 1️⃣3️⃣ Advantages of GAs

✅ Works for **complex**, **nonlinear**, or **black-box** problems.  
✅ Doesn’t require gradient or differentiability.  
✅ Can handle multiple objectives.  
✅ Often finds global or near-global optima.

---

## 1️⃣4️⃣ Disadvantages

❌ No guarantee of optimal solution.  
❌ Slower than specialized algorithms.  
❌ Parameter tuning (population size, mutation rate, etc.) can be tricky.  
❌ Fitness function design is problem-dependent.

---

## 1️⃣5️⃣ Common GA Parameters

|Parameter|Typical Range|
|---|---|
|Population size|20–200|
|Crossover rate|0.6 – 0.9|
|Mutation rate|0.01 – 0.1|
|Generations|100–1000 (depends on problem)|

---

## 1️⃣6️⃣ GA Variants

- **Steady-State GA:** Only a few offspring per generation.
    
- **Elitist GA:** Always retain the best individual.
    
- **Hybrid GA (Memetic Algorithm):** GA + local search (like hill climbing).
    
- **Parallel GA:** Multiple populations evolving simultaneously.
    

---

## 1️⃣7️⃣ Applications of Genetic Algorithms

🧠 **AI & ML:** Feature selection, neural network weights  
🏙️ **Optimization:** Scheduling, route planning (TSP), resource allocation  
🧱 **Engineering:** Circuit design, control parameters  
💹 **Finance:** Portfolio optimization, strategy tuning  
🎮 **Games:** Strategy evolution, pathfinding

---

## 🧾 Summary

|Concept|Analogy|Purpose|
|---|---|---|
|Chromosome|DNA|Represents a solution|
|Fitness|Survival ability|Evaluates quality|
|Selection|Natural selection|Choose good parents|
|Crossover|Mating|Create offspring|
|Mutation|Genetic variation|Maintain diversity|
|Evolution|Generational change|Improve population|

---

