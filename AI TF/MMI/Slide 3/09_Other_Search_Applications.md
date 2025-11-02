# 🌐 Other Search Applications

Search is a general technique used in many specialized domains:

## Traveling Salesperson Problem (TSP)

- **Problem:** Find the **shortest tour** that visits all cities exactly once and returns to the start.
    
- **State:** Sequence of cities visited so far (e.g., A $\to$ C $\to$ D...).
    
- **Goal:** A complete tour where the sequence ends at the start state.
    

## Robot Assembly

- **Problem:** Positioning and assembling parts (e.g., mobile phone components) using a robotic arm.
    
- **States:** Configuration of the robot (angles, positions) and the object parts being assembled.
    
- **Actions:** Continuous motion of robot joints (e.g., $P$ (prismatic), $R$ (rotational)).
    
- **Goal Test:** Is the object assembled according to specifications?
    

## Learning a Spam Email Classifier (Optimization)

- Many Machine Learning problems are cast as **optimization problems** that use search techniques.
    
- **States:** Settings of the **parameters** (weights) in the ML model.
    
- **Actions:** Moving in the parameter space (adjusting parameters).
    
- **Goal Test:** Achieving **optimal accuracy** on the training data.
    

## VLSI Layout Problem

- **Problem:** Positioning millions of components and connections on a chip to minimize area, delays, and maximize yield.
    
- **Goal:** Placing cells (component groups) without overlap, ensuring room for connecting wires (**Channel Routing**). These are extremely complex search problems.