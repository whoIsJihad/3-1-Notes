

# 06 - Advanced Conditioning and Bayesian Concepts

## Conditional Expectation and Variance Revisited

Let $S_N = \sum_{i=1}^N X_i$ be a random sum, where $N$ is a random variable and $X_i$ are IID random variables.

### Expected Value of a Random Sum

Using $E[S_N] = E[E[S_N | N]]$:

$$E[S_N] = E[N] E[X]$$

### Variance of a Random Sum

Using the Law of Total Variance:

$$\operatorname{Var}\left(\sum_{i=1}^{N} X_i\right) = E[N] \operatorname{Var}(X) + (E[X])^2 \operatorname{Var}(N)$$

## List Model (Move-to-Front)

In a Move-to-Front list, the probability that element $e_j$ precedes $e_i$ in the long run is given by:

$$P\{ e_j \text{ precedes } e_i \} = \frac{P_j}{P_i + P_j}$$

Where $P_i$ and $P_j$ are the request probabilities for $e_i$ and $e_j$.

The expected position of the element requested is:

$$E[\text{Position Requested}] = 1 + \sum_{i=1}^n \sum_{j \neq i} \frac{P_i P_j}{P_i + P_j}$$

## Bayesian Inference

The core of Bayesian inference is Bayes' Theorem:

$$P(H|D) = \frac{P(D|H) P(H)}{P(D)}$$

Where:

- $P(H|D)$: **Posterior Probability**
    
- $P(D|H)$: **Likelihood**
    
- $P(H)$: **Prior Probability**
    

### Maximum A Posteriori (MAP) Estimation

MAP finds the hypothesis $h$ that maximizes the posterior probability:

$$h_{\text{MAP}} = \operatorname{argmax}_{h_i} [ P(h_i | D) ]$$

This is equivalent to maximizing the product of the Likelihood and the Prior:

$$h_{\text{MAP}} = \operatorname{argmax}_{h_i} [ P(D | h_i) P(h_i) ]$$

MAP incorporates **Occam's Razor** by favoring simpler hypotheses (those with higher priors) while maintaining consistency with the data (high likelihood).