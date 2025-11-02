# Utility-Based Agents

Utility-based agents are used when there are multiple possible alternatives or when the distinction between success/failure is complex. They always factor in the **cost** of an action.

## Mechanism

- A goal provides only a crude distinction (happy vs. unhappy). Utility-based agents use a more general performance measure: the **Utility function**.
    
- **Utility function** $U$**:** A function that maps a State to a real number, indicating the measure of success or "degree of happiness" in that state.
    
    $$U: \text{State} \rightarrow \text{Reals}$$
- The agent selects the action that maximizes its **expected utility**.
    

## Architecture

The utility-based architecture builds upon the goal-based one by replacing the simple _Goals_ with a precise _Utility_ calculation:

- It determines "How happy I will be in such a state" (utility) before choosing the action.