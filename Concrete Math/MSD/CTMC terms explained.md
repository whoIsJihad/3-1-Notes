

---

## The CTMC TLDR: Speed, Amount, and Balance

### 1. What a State Probability $P_i(t)$ Means

Forget the phrase "percentage of time." Think of the **Probability $P_i(t)$** as the **"Amount"** of the system that is currently in state $i$ at the specific moment $t$.

- **Physical System:** A huge cluster of $10,000$ identical servers.
    
- **$P_{\text{Idle}}(t) = 0.6$:** At time $t$, **$60\%$** of all servers are Idle.
    

This probability is the **volume** we are tracking.

### 2. What a Rate $q_{ij}$ (Speed) Means

The **Rate $q_{ij}$** (e.g., $q_{12}=10$) is the **Speed Limit** or **Capacity** of the transition pipe between State $i$ and State $j$.

- $q_{12}=10$ is an event (like a packet arrival) that happens at a speed of 10 times per unit time.
    
- It is a **fixed parameter** of the system, like a constant in a differential equation.
    

### 3. What "Flow" (Flux) Means

**Flow** is the calculation that combines the **Amount** and the **Speed**.

$$\text{Flow/Flux from } i \to j = \text{Amount in } i \times \text{Speed } q_{ij}$$

$$\text{Flow} = P_i(t) \cdot q_{ij}$$

**Example:**

- $P_{\text{Idle}}(t) = 0.6$ (Amount)
    
- $q_{\text{Idle} \to \text{Busy}} = 10$ (Speed)
    
- **Flow $\mathbf{= 6.0}$:** This is the rate at which the _percentage_ is transferring out of Idle and into Busy.
    

This Flow term is the actual **transfer rate of the probability volume** through the pipe.

---

## The Kolmogorov Forward Equation (Balance)

The Forward Equation is just a fancy name for the principle of **Conservation of Percentage** (or probability volume). It tells us how fast the **Amount** ($P_j(t)$) in any state is changing.

The equation for State $j$ is:

$$\frac{d}{dt} P_j(t) = (\text{Total Flow IN}) - (\text{Total Flow OUT})$$

- **Flow IN:** All the percentages coming from other states ($k$) into state $j$ (e.g., $P_k(t) \cdot q_{kj}$). This is the **gain**.
    
- **Flow OUT:** The percentage already in state $j$ leaving for any other state (e.g., $P_j(t) \cdot \nu_j$). This is the **loss**.
    

**The Conclusion:** The system is always trying to reach a balance where the **Flow IN = Flow OUT** for every state. When this happens, $\frac{d}{dt} P_j(t) = 0$, and you have reached the **Steady-State Distribution** where the percentages (probabilities) stop changing.

That's the entire mechanism in one picture: The fixed **speeds ($Q$)** dictate how the **amount ($P(t)$)** moves, and the **Forward Equation** tracks the resulting balance.