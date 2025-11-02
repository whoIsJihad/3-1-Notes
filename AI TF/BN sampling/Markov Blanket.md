# Markov Blanket

_Source: `20. Uncertainty-5-BN-Sampling.pptx.pdf` (Pages 26-27)_

The **Markov Blanket** is a key concept for making [[Gibbs Sampling]] efficient.

When the Gibbs algorithm asks us to resample $X_i$ from $P(X_i | \text{all other variables})$, it seems like we need to condition on the _entire_ network, which sounds very complicated.

The **Markov Blanket** of a node $X$ is the set of nodes that "shields" it from the rest of the network. Given its Markov Blanket, $X$ is conditionally independent of _everything else_.

## What's in the Blanket?

The Markov Blanket of a node $X$ is composed of three groups of nodes:

1. $X$**'s Parents**
    
2. $X$**'s Children**
    
3. $X$**'s Children's other Parents** (also called "co-parents")
    

## Why it Matters

Because of this property, the scary-looking resampling step in Gibbs... $P(X | \text{all other variables})$

...simplifies to just:$P(X \mid \text{Markov\_Blanket}(X))$


As shown on Page 27, all the other terms in the network that are _not_ in the blanket simply cancel out. The conditional probability of $X$ given its blanket is proportional to: $P(X | \text{Parents}(X)) \times \prod_{Y \in \text{Children}(X)} P(Y | \text{Parents}(Y))$

This is much, _much_ easier to calculate. We only need to look at the CPTs for $X$ and its children.

### ❓ Review Questions

1. What are the three groups of nodes in a node $X$'s Markov Blanket?
    
2. Why is this concept so important for making Gibbs Sampling practical?