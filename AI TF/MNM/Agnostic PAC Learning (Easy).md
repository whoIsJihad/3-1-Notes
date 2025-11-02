
### Part 1 — Realizability Assumption (Standard PAC)

The standard PAC model assumes **realizability**, i.e., the true function $f$ is inside the hypothesis space $H$:

$$  
f \in H  
$$

This implies that there exists a hypothesis $h^* \in H$ such that the true error is zero:

$$  
\text{err}_D(h^*) = \Pr_{x \sim D}[h^*(x) \neq f(x)] = 0  
$$

and the empirical error on the training set $S$ is also zero:

$$  
\text{err}_S(h^*) = \frac{1}{|S|} \sum_{x \in S} \mathbf{1}[h^*(x) \neq f(x)] = 0  
$$

**Problem:** In real-world scenarios, this assumption is often unrealistic because:

1. The true function $f$ may **not belong** to the hypothesis space $H$.
    
2. The data may be **noisy**, so even the best hypothesis in $H$ cannot perfectly label all examples.
    

---

### Part 2 — Agnostic PAC Learning

In **Agnostic PAC Learning**, we **drop the realizability assumption**, i.e., we do **not assume** that the true function $f$ is in our hypothesis space $H$:

$$  
f \notin H \quad \text{(possibly)}  
$$

#### New Goal

Since no hypothesis may perfectly classify all examples, the learner now tries to find a hypothesis $h \in H$ that **minimizes empirical error**:

$$  
h_{\text{best}} = \arg\min_{h \in H} \text{err}_S(h)  
$$

where the **empirical error** is defined as:

$$  
\text{err}_S(h) = \frac{1}{m} \sum_{i=1}^{m} \mathbf{1}[h(x_i) \neq y_i]  
$$

- $S = {(x_1, y_1), \dots, (x_m, y_m)}$ is the training set
    
- $\mathbf{1}[\cdot]$ is the indicator function
    

The **true error** (generalization error) is:

$$  
\text{err}_D(h) = \Pr_{x \sim D}[h(x) \neq f(x)]  
$$

#### Key Challenge

We can find $h_{\text{best}}$ on the training set, but we want to **guarantee that its true error is also low**, i.e., we want:

$$  
\text{err}_D(h_{\text{best}}) \approx \min_{h \in H} \text{err}_D(h)  
$$

### Part 3 — Hoeffding Inequality and Agnostic PAC Sample Complexity (Fixed LaTeX)

To bound the difference between **empirical error** and **true error**, we use **Hoeffding's Inequality**. For a single hypothesis $h$:

$$  
\Pr\left(\text{err}_D(h) > \text{err}_S(h) + \epsilon\right) \le e^{-2 m \epsilon^2}  
$$

where $m$ is the number of samples and $\epsilon$ is the allowed deviation.

Since we search over all hypotheses in $H$, we use the **union bound**:

$$  
\Pr\Big( \exists h \in H \text{ such that } \text{err}_D(h) > \text{err}_S(h) + \epsilon \Big) \le |H| e^{-2 m \epsilon^2}  
$$

We want this failure probability to be at most $\delta$, so we set:

$$  
|H| e^{-2 m \epsilon^2} \le \delta  
$$

Solving for $m$ step by step:

$$  
\begin{aligned}  
e^{-2 m \epsilon^2} &\le \frac{\delta}{|H|} \  
-2 m \epsilon^2 &\le \ln\frac{\delta}{|H|} \  
2 m \epsilon^2 &\ge \ln\frac{|H|}{\delta} \  
m &\ge \frac{1}{2 \epsilon^2} \left( \ln|H| + \ln\frac{1}{\delta} \right)  
\end{aligned}  
$$

This is the **sample complexity bound for Agnostic PAC Learning**.

#### Comparison with Realizable PAC Bound

- **Realizable PAC (Occam Bound):**
    

$$  
m \ge \frac{1}{\epsilon} \left( \ln|H| + \ln\frac{1}{\delta} \right)  
$$

- **Agnostic PAC (Hoeffding Bound):**
    

$$  
m \ge \frac{1}{2 \epsilon^2} \left( \ln|H| + \ln\frac{1}{\delta} \right)  
$$

Notice that the Agnostic bound depends on $1/\epsilon^2$ instead of $1/\epsilon$, meaning we require **more samples** to achieve the same error guarantee, which makes sense because the problem is more realistic and harder.