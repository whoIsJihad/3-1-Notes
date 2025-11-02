# ⚙️ Initial Simplifying Assumptions

To simplify a complex real-world problem into a tractable search problem, we typically make the following four assumptions about the environment:

1. **Environment is Static:** No external changes occur while the agent is solving the problem. The world holds still.
    
2. **Environment is Observable:** The agent has full visibility into the current state of the environment.
    
3. **Environment and Actions are Discrete:** Both the states (situations) and the actions (operators) are distinct, countable steps. (This is typically assumed, though continuous exceptions exist).
    
4. **Environment is Deterministic:** Every action executed leads to a **single, predictable next state** (no uncertainty).