# Transient State Analysis: The Fundamental Matrix (S)

This section focuses on quantifying the behavior of a Markov Chain within its **Transient States**—the temporary stages a system passes through before reaching stability (Recurrent States).

## 1. Defining the Transient Set (T)

In any Markov Chain with a mix of state types, the first step is to partition the state space.

- **Transient State (**$i$**):** A state from which the process has a non-zero probability of escaping and never returning. In the long run, the process spends zero time here.
    
- **Set** $T$**:** The collection of all transient states, usually ordered as $T = \{1, 2, \dots, t\}$.
    

## 2. The Transient Transition Matrix ($\mathbf{P}_T$)

The matrix $\mathbf{P}_T$ is a sub-matrix of the main transition matrix $\mathbf{P}$, containing only the one-step probabilities _between_ the transient states.

$$\mathbf{P}_T = \begin{pmatrix} P_{11} & P_{12} & \dots & P_{1t} \\ P_{21} & P_{22} & \dots & P_{2t} \\ \vdots & \vdots & \ddots & \vdots \\ P_{t1} & P_{t2} & \dots & P_{tt} \end{pmatrix}$$

**Critical Property:** Since the states are transient, the sum of probabilities in any row $i$ of $\mathbf{P}_T$ **must be** $\le 1$.

$$\sum_{j \in T} P_{ij} \le 1$$

- The remaining probability, $1 - \sum P_{ij}$, is the chance of moving from transient state $i$ to a Recurrent state, thus leaving the transient set permanently.
    

## 3. The Goal: Mean Time in Transient States ($\mathbf{S}$)

We seek the matrix $\mathbf{S}$ (The **Fundamental Matrix** for transient states), where the entry $S_{ij}$ answers the key question:

 $S_{ij} =$  The expected total number of times the process visits state $j$**, given it starts in state** $i$, before the process leaves the entire transient set  $T$ 

This value represents the system's expected total "runtime" or total visits while in its temporary phase.

## 4. Derivation of the Fundamental Matrix $\mathbf{S}$

The derivation relies on the **Law of Total Expectation** by conditioning on the very first step.

### A. The Recurrence Relation

The expected total visits $S_{ij}$ can be broken down into two parts: the visit at Step 0, and all expected future visits (after the first step). We use the Kronecker Delta ($\delta_{ij}$) to handle the starting condition:

$$\delta_{ij} = \begin{cases} 1 & \text{if } i=j \text{ (You are at } j \text{ at time 0)} \\ 0 & \text{if } i \neq j \text{ (You are not at } j \text{ at time 0)} \end{cases}$$

The total expected time $S_{ij}$ is:

$$S_{ij} = \underbrace{\delta_{ij}}_{\substack{\text{Expected time} \\ \text{at Step 0}}} + \underbrace{\sum_{k \in T} P_{ik} S_{kj}}_{\substack{\text{Expected time} \\ \text{after Step 1 (via state } k)}}$$

### B. Matrix Form

In matrix notation, this linear system is written compactly:

$$\mathbf{S} = \mathbf{I} + \mathbf{P}_T \mathbf{S}$$

- $\mathbf{I}$: The Identity matrix, accounting for the immediate $+1$ visit if $i=j$.
    
- $\mathbf{P}_T \mathbf{S}$: The matrix multiplication representing the **total expected future visits** (i.e., the probability of moving $i \to k$, multiplied by the expected time spent in $j$ starting from $k$).
    

### C. The Solution

Solving the linear system for $\mathbf{S}$:

$$\mathbf{S} - \mathbf{P}_T \mathbf{S} = \mathbf{I}$$$$(\mathbf{I} - \mathbf{P}_T) \mathbf{S} = \mathbf{I}$$$$\mathbf{S} = (\mathbf{I} - \mathbf{P}_T)^{-1}$$

**The Fundamental Matrix** $\mathbf{S}$ **is the inverse of the difference between the Identity Matrix and the Transient Transition Matrix.**

## 5. Connecting Expected Time ($\mathbf{S}$) to Probability ($f_{ij}$)

The $\mathbf{S}$ matrix allows us to easily calculate the probability of ever visiting a state, $f_{ij}$.

### Definition of $f_{ij}$

$f_{ij}$ is the probability that, starting in state $i$, the process will **ever** visit state $j$.

### The Relationship

For two distinct transient states $i$ and $j$ ($i \neq j$), the probability of ever visiting $j$ (starting at $i$) is equal to the ratio of the expected total time spent at $j$ (starting at $i$), over the expected total time spent at $j$ (starting at $j$).

$$f_{ij} = \frac{S_{ij}}{S_{jj}}$$

**Insight:** This relationship confirms that the probability of reaching a destination ($f_{ij}$) is directly proportional to the amount of "visitation time" ($S_{ij}$) it guarantees once you've started the process. Since $S_{jj}$ is the expected time starting at $j$, it acts as the normalizing factor (the maximum possible expected time spent in $j$).

## 6. Example Calculation (Recap)

Consider a simple $2 \times 2$ transient set $T=\{1, 2\}$:

$$\mathbf{P}_T = \begin{pmatrix} 0.1 & 0.4 \\ 0 & 0.2 \end{pmatrix}$$

1. **Calculate** $\mathbf{I} - \mathbf{P}_T$:
    
    $$(\mathbf{I} - \mathbf{P}_T) = \begin{pmatrix} 0.9 & -0.4 \\ 0 & 0.8 \end{pmatrix}$$
2. **Calculate** $\mathbf{S}$ **(The Inverse)**:
    
    $$\mathbf{S} = (\mathbf{I} - \mathbf{P}_T)^{-1} \approx \begin{pmatrix} 1.111 & 0.556 \\ 0 & 1.25 \end{pmatrix}$$
3. **Interpretation of** $S_{12}$:
    
    - $S_{12} = 0.556$. If the process starts at State 1, it is expected to spend a total of 0.556 steps in State 2 before exiting the transient phase.
        
4. **Calculate Probability of Visit (**$f_{12}$**)**:
    
    $$f_{12} = \frac{S_{12}}{S_{22}} = \frac{0.556}{1.25} \approx 0.445$$
    - This means there is a **44.5% probability** that the process, starting at 1, will eventually visit State 2.
        

This note solidifies the key concepts, the matrix math, and the relationship between expected visits ($\mathbf{S}$) and ultimate probability ($f_{ij}$) for transient states.