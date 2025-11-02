# 🧠 Computational Learning Theory (CLT)

_Source: `13. Learning-Theory-7-PAC-AGN.pdf`, `14. Learning-Theory-8-PAC-VC.pdf`_

**Computational Learning Theory (CLT)**, or "COLT," is the formal, theoretical study of machine learning. It tries to answer fundamental questions:

- **What is learnable?**
    
- **How many training examples do I need** to be confident in my learned model?
    
- How "good" or "complex" is my set of possible functions (hypothesis class)?
    

The framework we use to answer these is called **Probably Approximately Correct (PAC) Learning**.

## Core Concepts

The theory is built on a few key assumptions and models:

1. **The Goal**: We care about **generalization error** ($err_D(h)$), not just training error ($err_S(h)$).
    
2. **Assumption 1 (Stationary)**: Training and test data are drawn from the _same_ fixed, unknown distribution $D$.
    

We study two main "settings" or "models" of learning:

### 1. Realizable Case (Standard PAC)

- **Assumption (Realizability)**: We assume the _true_ target function $f$ is _inside_ our hypothesis space $H$ ($f \in H$).
    
- **Learning Strategy**: The learner can find a _consistent hypothesis_ ($h \in H$) that makes zero errors on the training data ($err_S(h) = 0$).
    
- **The Bound**: This leads to the [[PAC Learning - Realizable Case|Occam's Razor]] bound, which depends on $ln(|H|)$.
    

### 2. Agnostic Case

- **Assumption (Relaxed)**: We _do not_ assume $f \in H$. The true function might be too complex for our model.
    
- **Learning Strategy**: A consistent hypothesis may not exist. The learner's goal is just to find the $h \in H$ with the _lowest possible training error_.
    
- **The Bound**: This is the [[Agnostic Learning]] model. Its sample complexity bound is different and generally requires more samples.
    

### 3. The Problem of Infinity

- Both of the above bounds depend on $ln(|H|)$.
    
- **What if** $|H|$ **is infinite?** (e.g., linear classifiers, neural networks).
    
- We need a different measure of "expressiveness" or "complexity" for [[Infinite Hypothesis Spaces]].
    
- This measure is the **[[VC Dimension (VCD)|Vapnik-Chervonenkis (VC) Dimension]]**, which is based on the concept of **[[Shattering]]**.
    
- This leads to new [[Sample Complexity with VC Dimension|sample complexity bounds]] that replace $ln(|H|)$ with $VC(H)$.