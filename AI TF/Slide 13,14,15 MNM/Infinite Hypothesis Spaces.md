# Infinite Hypothesis Spaces

_Source: `14. Learning-Theory-8-PAC-VC.pdf` (Pages 4-8)_

The sample complexity bounds for both [[PAC Learning - Realizable Case|realizable]] and [[Agnostic Learning|agnostic]] models depend on $ln(|H|)$.

**This creates a problem:** What if our hypothesis space $H$ is **infinite**?

- **Example**: The set of all linear classifiers (lines) in a 2D plane. There are infinitely many possible lines.
    
- **Example**: The set of all axis-aligned rectangles.
    
- **Example**: Neural networks (infinite possible weights).
    

If $|H| = \infty$, then $ln(|H|) = \infty$, which means our bounds would suggest we need an infinite amount of data. This is obviously not right—people successfully train linear classifiers all the time.

This means that $ln(|H|)$ is not the right way to measure the "expressiveness" or "complexity" of an infinite hypothesis space.

## The Solution: VC Dimension

We need a new measure of expressive capacity. This measure is the **[[VC Dimension (VCD)|Vapnik-Chervonenkis (VC) Dimension]]**.

- The VC dimension measures the "richness" or "complexity" of $H$ in a different way.
    
- It is based on the idea of **[[Shattering]]**—the ability of $H$ to perfectly label all possible combinations of a set of points.
    
- For infinite hypothesis spaces, the VC dimension $VC(H)$ will replace $ln(|H|)$ in our sample complexity bounds.
    

### ❓ Review Questions

1. Why is $ln(|H|)$ a problematic measure of complexity for a linear classifier?
    
2. What measure do we use instead of $|H|$ to characterize the complexity of infinite hypothesis spaces?