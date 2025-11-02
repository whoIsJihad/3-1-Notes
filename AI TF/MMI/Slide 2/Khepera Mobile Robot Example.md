
The Khepera mobile robot is a small, differential-drive robot often used in labs for obstacle avoidance and navigation.

## Objectives

1. Keep safe distance from obstacles.
    
2. Move as straight as possible.
    
3. Cover maximum distance.
    

## Objective Function

These objectives are combined into a single objective function $f$:

$$f = (1-S)(1-\nu)D$$

Where:

- $S$: Normalized sensory value (Higher $S$ means closer to an obstacle). $(1-S)$ encourages obstacle avoidance.
    
- $\nu$: Difference between wheel speeds (Higher $\nu$ means more winding motion). $(1-\nu)$ encourages straight movement.
    
- $D$: Total distance travelled. $D$ encourages covering maximum distance.