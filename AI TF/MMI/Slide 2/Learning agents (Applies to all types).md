# Learning Agents

**Learning** is the component that allows an agent to become **autonomous** by improving its behavior over time through its own experience, rather than depending solely on the designer's built-in knowledge.

## Core Concept: Iterative Improvement

- Learning is always an **iterative and incremental method**.
    
- It gradually improves the agent's performance measure by avoiding past mistakes.
    

## The Learning Process

A conceptual Learning Agent design typically includes four components:

1. **Learning Element:** Responsible for making improvements to the agent's knowledge base or program.
    
2. **Performance Element:** The current _agent program_ that selects the external actions (this is the component being improved).
    
3. **Critic:** Provides feedback to the Learning Element based on the **Performance Measure** (e.g., "That action cost too much," or "That achieved the goal quickly").
    
4. **Problem Generator:** Suggests new, exploratory actions that might lead to new and informative experiences, enabling the agent to better understand its environment (exploration).