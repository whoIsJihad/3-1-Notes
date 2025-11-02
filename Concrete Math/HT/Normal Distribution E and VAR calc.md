# Derivation of $\mathbf{E[X]}$ and $\mathbf{Var[X]}$ for the Normal Distribution using the Gamma Function

We derive the Expected Value $(E[X])$ and Variance $(\operatorname{Var}(X))$ for a normally distributed random variable $X$:

$$X\sim \mathcal N(\mu,\sigma^2),\qquad f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big).$$

## Useful Gamma-Integral Identity

For $a>0$ and $k>-1$:

$$\int_0^\infty x^{k} e^{-a x^{2}}\,dx=\tfrac{1}{2}a^{-(k+1)/2}\,\Gamma\Big(\frac{k+1}{2}\Big).$$

**Special values:** $\Gamma(\tfrac12)=\sqrt{\pi}$ and $\Gamma(\tfrac32)=\tfrac12\sqrt{\pi}$.

## 1) Expected Value $\mathbf{E[X]}$

The expectation is computed as:

$$E[X]=\int_{-\infty}^{\infty} x f(x)\,dx.$$

We use the shift $t=x-\mu$, which implies $x=t+\mu$ and $dx=dt$:

$$E[X]=\int_{-\infty}^{\infty} (t+\mu)\,\frac{1}{\sqrt{2\pi}\sigma}e^{-t^{2}/(2\sigma^{2})}\,dt.$$

Splitting the integral into two terms:

$$E[X]=\underbrace{\frac{1}{\sqrt{2\pi}\sigma}\int_{-\infty}^{\infty} t\,e^{-t^{2}/(2\sigma^{2})}\,dt}_{\text{Term 1}} + \mu\underbrace{\frac{1}{\sqrt{2\pi}\sigma}\int_{-\infty}^{\infty} e^{-t^{2}/(2\sigma^{2})}\,dt}_{\text{Term 2}}.$$

1. **Term 1:** The function $g(t) = t\,e^{-t^{2}/(2\sigma^{2})}$ is an **odd function**. Since the integration bounds are symmetric $(-\infty, \infty)$, this integral vanishes:
    
    $$\frac{1}{\sqrt{2\pi}\sigma}\int_{-\infty}^{\infty} t\,e^{-t^{2}/(2\sigma^{2})}\,dt = 0.$$
2. **Term 2:** The integral part is the total area under the standardized Normal PDF (since it integrates to 1):
    
    $$\frac{1}{\sqrt{2\pi}\sigma}\int_{-\infty}^{\infty} e^{-t^{2}/(2\sigma^{2})}\,dt = 1.$$

Therefore, we have:

$$E[X] = 0 + \mu(1)$$$$\boxed{E[X]=\mu.}$$

## 2) Variance $\mathbf{\operatorname{Var}(X)}$

The variance is defined as:

$$\operatorname{Var}(X)=E\big[(X-\mu)^2\big]=\int_{-\infty}^{\infty}(x-\mu)^2 f(x)\,dx.$$

We use the substitution $u=(x-\mu)/\sigma$, which gives $x-\mu=\sigma u$ and $dx=\sigma du$:

$$\operatorname{Var}(X)=\int_{-\infty}^{\infty} (\sigma u)^2\frac{1}{\sqrt{2\pi}\sigma}e^{-u^{2}/2}\sigma\,du$$$$\operatorname{Var}(X)=\sigma^{2}\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} u^{2} e^{-u^{2}/2}\,du.$$

We focus on the integral $I$:

$$I=\int_{-\infty}^{\infty} u^{2} e^{-u^{2}/2}\,du = 2\int_{0}^{\infty} u^{2} e^{-u^{2}/2}\,du \quad \text{(due to even symmetry)}.$$

We apply the Gamma identity with the parameters $k=2$ and $a=\tfrac12$:

$$\int_{0}^{\infty} u^{2} e^{-(1/2)u^{2}}\,du = \tfrac{1}{2}\Big(\tfrac{1}{2}\Big)^{-(2+1)/2}\Gamma\Big(\frac{2+1}{2}\Big)$$$$= \tfrac{1}{2}\Big(\tfrac{1}{2}\Big)^{-3/2}\Gamma\Big(\tfrac{3}{2}\Big)$$$$= \tfrac{1}{2}\cdot 2^{3/2}\cdot\frac{1}{2}\sqrt{\pi}$$$$= \frac{1}{4} \cdot (2\sqrt{2}) \cdot \sqrt{\pi}$$$$= \frac{\sqrt{2\pi}}{2}.$$

Plugging this back into the equation for $I$:

$$I=2\int_{0}^{\infty} u^{2} e^{-u^{2}/2}\,du = 2\cdot\frac{\sqrt{2\pi}}{2}=\sqrt{2\pi}.$$

Finally, substituting $I$ back into the variance formula:

$$\operatorname{Var}(X)=\sigma^{2}\frac{1}{\sqrt{2\pi}}\cdot I = \sigma^{2}\frac{1}{\sqrt{2\pi}}\cdot\sqrt{2\pi}=\sigma^{2}.$$$$\boxed{\operatorname{Var}(X)=\sigma^{2}.}$$

## Summary

Using the Gamma function identity for Gaussian-type integrals, we successfully derive the familiar results:

$$\boxed{E[X]=\mu,\qquad \operatorname{Var}(X)=\sigma^{2}.}$$