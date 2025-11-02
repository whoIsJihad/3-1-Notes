# Stochastic Processes and Markov Chains (Based on Sheldon L. Ross)

## 1. Stochastic Process

A **Stochastic Process** is defined as a collection of random variables $X_t$, indexed by time $t$, where $t \in T$.

- $X_t$: Represents the **state of the process** at time $t$.
    
- **Indexing Set (**$T$**)**: The set of possible time values. In the context of Markov Chains, $T$ is typically discrete (e.g., $T = \{0, 1, 2, \dots\}$).
    

## 2. Markov Chain

A **Markov Chain** is a specific type of stochastic process that satisfies the **Markov Property**.

### First-Order Markov Chain Definition

A stochastic process is a **First-Order Markov Chain** if the future state depends only on the current state, and not on the sequence of events that preceded it.

Mathematically, this is expressed as a fixed probability $P_{ij}$ that the process will next be in state $j$, given it is currently in state $i$:

$$P\{X_{n+1}=j | X_{n}=i, X_{n-1}=i_{n-1}, \dots, X_{1}=i_{1}, X_{0}=i_{0}\} = P_{ij}$$

The key takeaway is: **Only the information from the last step (**$X_n=i$**) is required.**

### Order of Markov Chain

The notes mention:

- **First Order:** Only the last state is needed.
    
- **Second Order:** The last **two** states are needed to determine the next state's probability.
    

### Transition Matrix (P)

The transition probabilities $P_{ij}$ are arranged in a **square matrix** $\mathbf{P}$, called the **One-Step Transition Probability Matrix**.

$$\mathbf{P} = \begin{pmatrix} P_{00} & P_{01} & P_{02} & \dots \\ P_{10} & P_{11} & P_{12} & \dots \\ P_{20} & P_{21} & P_{22} & \dots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

### Two Properties of Transition Probabilities

1. **Non-negativity:** All transition probabilities must be non-negative.
    
    $$P_{ij} \ge 0$$
2. **Row Sum to One (Conservation of Probability):** For any state $i$, the sum of probabilities of transitioning to all possible states $j$ must equal 1. This means that from state $i$, the process must move _somewhere_.
    
    $$\sum_{j} P_{ij} = 1, \quad \text{for all } i$$

## 3. Chapman-Kolmogorov Equation

The Chapman-Kolmogorov equation allows us to compute the $n$**-step transition probability**, $P_{ij}^{(n)}$, which is the probability of moving from state $i$ to state $j$ in exactly $n$ steps.

### Definition of $n$-step Transition Probability

$$P_{ij}^{(n)} = P\{X_{k+n}=j | X_{k}=i\}, \quad n \ge 0, i, j \ge 0$$

### The Equation

The $n+m$ step transition probability from $i$ to $j$ is calculated by summing over all possible intermediate states $k$ at step $n$:

$$P_{ij}^{(n+m)} = \sum_{k=0}^{\infty} P_{ik}^{(n)} \cdot P_{kj}^{(m)}$$

The intermediate state $k$ is any **possible value** that the process can take at time $n$.

### Matrix Form of the Equation

The power of this equation is seen in the matrix form: the $(n+m)$-step transition matrix is simply the product of the $n$-step and $m$-step transition matrices.

$$\mathbf{P}^{(n+m)} = \mathbf{P}^{(n)} \cdot \mathbf{P}^{(m)}$$

A key result is that the $n$-step transition matrix, $\mathbf{P}^{(n)}$, is equal to the transition matrix $\mathbf{P}$ raised to the power of $n$:

$$\mathbf{P}^{(n)} = \mathbf{P}^{n}$$

### Example Calculation

Given a weather example with states R (Rainy) and S (Sunny):

$$\mathbf{P} = \begin{pmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{pmatrix}$$

- $P_{RR} = 0.7$ (Rain today $\rightarrow$ Rain tomorrow)
    
- $P_{RS} = 0.3$ (Rain today $\rightarrow$ Sunny tomorrow)
    

The 2-step transition matrix $\mathbf{P}^{(2)}$ is:

$$\mathbf{P}^{(2)} = \mathbf{P} \cdot \mathbf{P} = \begin{pmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{pmatrix} \begin{pmatrix} 0.7 & 0.3 \\ 0.4 & 0.6 \end{pmatrix} = \begin{pmatrix} 0.61 & 0.39 \\ 0.52 & 0.48 \end{pmatrix}$$

If it is raining today, the probability that it will rain 2 days from today is $P_{RR}^{(2)} = 0.61$.

The 4-step transition matrix $\mathbf{P}^{(4)}$ can be found as $\mathbf{P}^{(4)} = \mathbf{P}^{(2)} \cdot \mathbf{P}^{(2)}$.

## 4. Classification of States

States in a Markov chain can be classified based on their accessibility and communication properties.

### Accessibility

**State** $j$ **is said to be accessible from state** $i$ if there exists some number of steps $n \ge 0$ such that the $n$-step transition probability is greater than zero.

$$i \to j \quad \text{if} \quad P_{ij}^{(n)} > 0 \quad \text{for some } n$$

### Communication

**Two states** $i$ **and** $j$ **are said to communicate** if they are accessible to each other (bidirectional accessibility).

$$i \leftrightarrow j \quad \text{if} \quad i \to j \quad \text{and} \quad j \to i$$

### Classes

- Two states that communicate are said to be in the **same class**.
    
- Communication is an equivalence relation (reflexive, symmetric, transitive), which partitions the state space into disjoint classes.
    

### Irreducible Markov Chain

A Markov Chain is **irreducible** if there is only one class; that is, **all states communicate with each other.**

### State Types (Example Classification)

Consider the transition matrix example:

$$\mathbf{P} = \begin{pmatrix} 0.5 & 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 & 0 \\ 0.25 & 0.25 & 0.25 & 0.25 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

The classes identified are:

1. $\{0, 1\}$: These states communicate with each other, but they do not transition to state 2 or 3. They are **Recurrent** states (if you enter this class, you cannot leave it).
    
2. $\{2\}$: This state can transition out to $\{0, 1\}$ and $\{3\}$. It is a **Transient** state (won't be stuck in the long run).
    
3. $\{3\}$: Once the process enters state 3 ($P_{33}=1$), it remains there. This is an **Absorbing** state (a special type of recurrent state).
    

## 5. Limiting Probabilities and Long-Run Proportions

For many Markov chains, as the number of transitions $n$ becomes very large, the $n$-step transition probabilities $P_{ij}^{(n)}$ converge to a steady-state value $\pi_j$, which is independent of the initial state $i$.

### Limiting Probability $\pi_j$

If the limit exists and is independent of $i$:

$$\pi_{j} = \lim_{n \rightarrow \infty} P_{ij}^{(n)}, \quad j \ge 0$$

$\pi_j$ is interpreted as the **long-run proportion of time** the process spends in state $j$, or the **limiting probability** that the process will be in state $j$ after a large number of transitions.

### System of Equations for $\pi_j$

The vector of limiting probabilities $\boldsymbol{\pi} = (\pi_0, \pi_1, \dots)$ is the unique non-negative solution to the following system of equations:

1. **Steady-State Equation (Balance Equation):** The probability of being in state $j$ in the long run is the sum of the probabilities of being in any state $i$ and transitioning to $j$.
    
    $$\pi_{j} = \sum_{i=0}^{\infty} \pi_{i} P_{ij}, \quad j \ge 0$$
    
    In matrix notation, this is $\boldsymbol{\pi} = \boldsymbol{\pi} \mathbf{P}$.
    
2. **Normalization Condition:** The sum of all limiting probabilities must be 1.
    
    $$\sum_{j=0}^{\infty} \pi_{j} = 1$$

### Example Calculation (Weather)

Using the weather example states R (state 0) and S (state 1) with the matrix:

$$\mathbf{P} = \begin{pmatrix} \alpha & 1-\alpha \\ \beta & 1-\beta \end{pmatrix} = \begin{pmatrix} P_{RR} & P_{RS} \\ P_{SR} & P_{SS} \end{pmatrix}$$

Let $\pi_0 = \pi_R$ and $\pi_1 = \pi_S$. The system of equations is:

1. $\pi_0 = \pi_0 P_{RR} + \pi_1 P_{SR} \quad \Rightarrow \quad \pi_0 = \alpha \pi_0 + \beta \pi_1$
    
2. $\pi_0 + \pi_1 = 1$
    

Substituting $\pi_1 = 1 - \pi_0$ into (1):

$$\pi_0 = \alpha \pi_0 + \beta (1 - \pi_0)$$$$\pi_0 (1 - \alpha + \beta) = \beta$$

The **Long Run Proportions** are:

$$\pi_{0} = \frac{\beta}{1 - \alpha + \beta} \quad \text{and} \quad \pi_{1} = \frac{1 - \alpha}{1 - \alpha + \beta}$$

## 6. Hardy-Weinberg Law (Application of Probability)

The notes conclude with an application of probability theory to genetics, specifically the Hardy-Weinberg Law.

### Setup

- **Gene Types:** Two types, $\mathbf{A}$ and $\mathbf{a}$.
    
- **Gene Pairs (Genotypes):** Each individual possesses one of three pairs (genotypes): $\mathbf{AA}$, $\mathbf{aa}$, or $\mathbf{Aa}$.
    
- **Initial Proportions (Generation 0):**
    
    - $P\{\mathbf{AA}\} = p_0$
        
    - $P\{\mathbf{aa}\} = q_0$
        
    - $P\{\mathbf{Aa}\} = r_0$
        
    - **Constraint:** $p_0 + q_0 + r_0 = 1$ (This covers the entire population).
        

### Calculation of Gene Frequencies

Assuming random mating, we calculate the probability that a gene contributed by a parent is $\mathbf{A}$ or $\mathbf{a}$.

1. **Probability of contributing gene** $\mathbf{A}$ **(First Generation):**
    
    - A parent with $\mathbf{AA}$ contributes $\mathbf{A}$ with $P\{\mathbf{A}|\mathbf{AA}\} = 1$.
        
    - A parent with $\mathbf{aa}$ contributes $\mathbf{A}$ with $P\{\mathbf{A}|\mathbf{aa}\} = 0$.
        
    - A parent with $\mathbf{Aa}$ contributes $\mathbf{A}$ with $P\{\mathbf{A}|\mathbf{Aa}\} = 1/2$.
        
    
    Using the Law of Total Probability:
    
    $$P\{\mathbf{A}\} = P\{\mathbf{A}|\mathbf{AA}\}p_0 + P\{\mathbf{A}|\mathbf{aa}\}q_0 + P\{\mathbf{A}|\mathbf{Aa}\}r_0$$$$P\{\mathbf{A}\} = 1 \cdot p_0 + 0 \cdot q_0 + \frac{1}{2} r_0 = p_0 + \frac{r_0}{2}$$
2. **Probability of contributing gene** $\mathbf{a}$ **(First Generation):**
    
    $$P\{\mathbf{a}\} = P\{\mathbf{a}|\mathbf{AA}\}p_0 + P\{\mathbf{a}|\mathbf{aa}\}q_0 + P\{\mathbf{a}|\mathbf{Aa}\}r_0$$$$P\{\mathbf{a}\} = 0 \cdot p_0 + 1 \cdot q_0 + \frac{1}{2} r_0 = q_0 + \frac{r_0}{2}$$

### Calculation of Genotype Proportions (Next Generation)

Assuming independent selection of genes from two parents (random mating):

- $P\{\mathbf{AA}\} = P\{\mathbf{A}\} \cdot P\{\mathbf{A}\} = \left(p_0 + \frac{r_0}{2}\right)^2 = p$
    
- $P\{\mathbf{aa}\} = P\{\mathbf{a}\} \cdot P\{\mathbf{a}\} = \left(q_0 + \frac{r_0}{2}\right)^2 = q$
    
- $P\{\mathbf{Aa}\} = P\{\mathbf{A}\} \cdot P\{\mathbf{a}\} + P\{\mathbf{a}\} \cdot P\{\mathbf{A}\} = 2 \left(p_0 + \frac{r_0}{2}\right) \left(q_0 + \frac{r_0}{2}\right) = r$
    

### Conclusion: Hardy-Weinberg Law

The notes confirm a critical result: The fraction of genes that are $\mathbf{A}$ in the next generation, $P\{\mathbf{A}\}$, remains **unchanged** from the previous generation.

$$P\{\mathbf{A}\}_{\text{new}} = p + \frac{r}{2} = \left(p_0 + \frac{r_0}{2}\right)$$

**The Law:** Under random mating, in successive generations _after the initial one_, the percentage of the population having gene pairs $\mathbf{AA}$, $\mathbf{Aa}$, or $\mathbf{aa}$ will remain the values $p$, $q$, and $r$. In other words, the genetic makeup of a population remains constant from generation to generation in the absence of other evolutionary influences.