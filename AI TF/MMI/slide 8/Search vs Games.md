# Search vs. Games

A comparison of standard search problems and adversarial game problems.

## Standard Search

- **Adversary:** No adversary.
    
- **Solution:** A (heuristic) method or path for finding a goal.
    
- **Evaluation Function:** Estimates the cost from the start to a goal through a given node.
    
- **Examples:** Path planning, scheduling.
    

## Games

- **Adversary:** Yes, an opponent is present.
    
- **Solution:** A **strategy**, which specifies a move for _every possible_ opponent reply.
    
- **Evaluation Function:** Estimates the "goodness" of a game position.
    
- **Constraints:** Time limits often force an approximate solution.
    
- **Examples:** Chess, Othello, Backgammon.
    

**Links:**

- Back to: [[Adversarial Search Index]]
    
- See also: [[Types of Games]]