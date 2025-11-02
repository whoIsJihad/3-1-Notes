# Utility and Rewards (Discounting)

_Source: `21. Making complex decisions- nidhi.pdf` (Pages 14-15, 26-28)_

In a [[Sequential Decision Problems|sequential decision problem]], the agent's total **utility** is the sum of the rewards it receives over its "life."

However, just summing them up has a major theoretical problem.

## Types of Rewards

1. **Additive Rewards (Finite Horizon)**
    
    - $U_h([s_0, s_1, s_2, ...]) = R(s_0) + R(s_1) + R(s_2) + ...$
        
    - This is what we used in the grid world: $10 \times (-0.04) + 1.0 = 0.6$.
        
    - **Problem**: What if the process is an **infinite horizon**? (i.e., there is no terminal state). If the agent can get even a tiny positive reward $R(s) > 0$ forever, its total utility will be $+\infty$. It's impossible to compare two policies that both give infinite utility.
        
2. **Discounted Rewards (Infinite Horizon)**
    
    - This is the standard solution. We introduce a **discount factor,** $\gamma$ (gamma), where $0 < \gamma \le 1$.
        
    - $U_h([s_0, s_1, s_2, ...]) = R(s_0) + \gamma R(s_1) + \gamma^2 R(s_2) + \gamma^3 R(s_3) + ...$
        
    - This means a reward received _now_ is worth more than a reward received _in the future_.
        

## Why Discounting Works

- **Economic Intuition**: A dollar today is worth more than a dollar tomorrow (because of interest). $\gamma$ is like an interest rate.
    
- **Mathematical Property**: This sum is a geometric series and is **guaranteed to be finite** as long as $\gamma < 1$ and the rewards $R(s)$ are bounded (which they are).
    
    - The maximum possible utility is bounded by: $U_{max} \le \frac{R_{max}}{1 - \gamma}$.
        
    - This allows us to compare policies even in infinite-horizon problems.
        

## Interpreting $\gamma$

- **If** $\gamma$ **is close to 1** (e.g., 0.99): The agent is **"far-sighted."** Future rewards are almost as important as current rewards. It will take a long path to get a slightly better reward.
    
- **If** $\gamma$ **is close to 0** (e.g., 0.1): The agent is **"short-sighted."** It only cares about the immediate next step. It will act "greedily" and may never reach a distant, large reward.
    
- **If** $\gamma = 0$: The agent only cares about $R(s_0)$. It's a "one-step" problem.
    
- **If** $\gamma = 1$: We are back to additive rewards. This only works for _finite_ horizons.
    

We can now define the utility of a state $s$ under a policy $\pi$ as the _expected discounted sum of future rewards_: $U^{\pi}(s) = E[\sum_{t=0}^{\infty} \gamma^t R(S_t) | S_0 = s, \pi]$

This definition leads directly to [[The Bellman Equation]].

### ❓ Review Questions

1. What is the problem with simple additive rewards in an "infinite horizon" problem?
    
2. What is the "discount factor" $\gamma$, and what does it mean if $\gamma$ is 0.9 vs 0.1?
    
3. Why is the discounted utility _guaranteed_ to be finite (bounded)?