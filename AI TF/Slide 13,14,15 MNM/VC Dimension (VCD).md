# VC Dimension (VCD)

_Source: `14. Learning-Theory-8-PAC-VC.pdf` (Pages 67-69, 76)_

The **Vapnik-Chervonenkis (VC) Dimension** is the measure of complexity or "expressiveness" for [[Infinite Hypothesis Spaces|infinite hypothesis spaces]]. It is based entirely on the concept of [[Shattering]].

## Formal Definition

> The VC Dimension of a hypothesis space $H$, written $VC(H)$, is...
> 
> ...the size $d$ of the **largest finite subset of points** $S$ that can be **shattered** by $H$.

If $H$ can shatter _any_ arbitrarily large set of points, its $VC(H) = \infty$.

## How to Find the VC Dimension ($d$)

To prove that $VC(H) = d$, you must show two things:

1. **There exists** _**at least one**_ **set of** $d$ **points that** $H$ _**can**_ **shatter.**
    
    - You just have to find _one_ configuration of $d$ points that works for all $2^d$ labelings.
        
2. **There is** _**no**_ **set of** $d+1$ **points (in any configuration) that** $H$ _**can**_ **shatter.**
    
    - This means for _every_ possible set of $d+1$ points, you can find _at least one_ "impossible" labeling.
        

## Examples of VC Dimension

- $H$ **= Left-bounded intervals `[0, a)`**
    
    - $VC(H) = 1$.
        
    - It _can_ shatter 1 point (you can make it `+` or `-`).
        
    - It _cannot_ shatter 2 points. The labeling `(point 1 = -, point 2 = +)` (assuming $p1 < p2$) is impossible.
        
- $H$ **= Intervals `[a, b]`**
    
    - $VC(H) = 2$.
        
    - It _can_ shatter 2 points (all 4 labelings are possible).
        
    - It _cannot_ shatter 3 points. The labeling `(+ - +)` is impossible for a single interval.
        
- $H$ **= 2D Linear Classifiers (Half-spaces)**
    
    - $VC(H) = 3$.
        
    - It _can_ shatter 3 non-collinear points (all 8 labelings are possible).
        
    - It _cannot_ shatter 4 points (the XOR labeling is impossible).
        
- $H$ **= Linear Classifiers in** $d$**-dimensions**
    
    - $VC(H) = d + 1$.
        

The VC Dimension is the key to creating [[Sample Complexity with VC Dimension|sample complexity bounds]] for these infinite spaces.

### ❓ Review Questions

1. What two conditions must be met to prove that $VC(H) = 3$?
    
2. What is the VC dimension of an axis-aligned rectangle in 2D? (This is a classic one!)
    
3. What is the relationship between the VC dimension of a linear classifier and the number of dimensions ($d$) of the data?