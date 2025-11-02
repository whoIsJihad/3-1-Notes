[[Easier Notes on Markov Chain - Initial two lectures  on MSD]]
[[ Expected time in Transient States ]]
## First-Order Markov Chains

A stochastic process $\{X_t\}$ is a **First-Order Markov Chain** if the future state depends only on the current state.

$$P\{ X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, \dots \} = P\{ X_{n+1} = j | X_n = i \} = P_{ij}$$

Where $P_{ij}$ is the probability of transitioning from state $i$ to state $j$.

### Transition Matrix ($\mathbf{P}$)

The transition probabilities are stored in a square matrix $\mathbf{P}$. The sum of probabilities in any row must equal 1: $\sum_{j} P_{ij} = 1$.

## Chapman-Kolmogorov Equation

This equation calculates the **n-step transition probability**, $P_{ij}^{(n)}$. In matrix notation, the $n$-step transition matrix is $\mathbf{P}^{(n)} = \mathbf{P} \cdot \mathbf{P} \cdot \dots \cdot \mathbf{P}$ ($n$ times).

The equation for $n+m$ steps:

$$P_{ij}^{(n+m)} = \sum_{k=0}^{\infty} P_{ik}^{(n)} P_{kj}^{(m)}$$

## Classification of States

1. **Accessible (**$i \to j$**):** State $j$ is accessible from $i$ if $P_{ij}^{(n)} > 0$ for some $n \ge 0$.
    
2. **Communicate (**$i \leftrightarrow j$**):** $i$ is accessible from $j$ AND $j$ is accessible from $i$.
    
3. **Recurrent (Persistent):** State $i$ is recurrent if the probability of eventually re-entering state $i$, $f_{ii}$, is 1.
    
    - **Test for Recurrence:**
        
        $$\sum_{n=1}^{\infty} P_{ii}^{(n)} = \infty$$
4. **Transient:** State $i$ is transient if $f_{ii} < 1$.
    

## Limiting Probabilities and Stationary Distribution

The limiting probability vector $\pi = [\pi_0, \pi_1, \dots]$ is the unique non-negative solution to the equations:

1. **Stationary Equation (Balance Equation):**
    
    $$\pi_j = \sum_{i=0}^{m} \pi_i P_{ij}$$
2. **Normalization:**
    
    $$\sum_{j=0}^{m} \pi_j = 1$$

## Custom Example: Three-State Machine Status (Transient States)

To find the mean time spent in the set of transient states $T$, we calculate the matrix $\mathbf{S}$:

$$\mathbf{S} = (\mathbf{I} - \mathbf{P}_T)^{-1}$$

Where $\mathbf{P}_T$ contains only the transition probabilities between transient states. The elements $S_{ij}$ give the expected number of times the process is in state $j$, starting from state $i$, before being absorbed by a recurrent state.