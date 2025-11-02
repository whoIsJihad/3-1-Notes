# Model-Based Reflex Agents

Model-based reflex agents are the first type of agent that incorporates **internal state** (memory) to handle environments that are not fully observable.

## Why Models are Needed

- **Simple Reflex Agents** rely only on the _current_ percept.
    
- In **Partially Observable** environments, the current percept alone is insufficient to determine the current state (e.g., if you only see one side of a room).
    
- The agent must maintain an **internal state** to keep track of the _unseen_ parts of the world.
    

## Key Components (The Internal Model)

A model-based agent updates its internal state using two pieces of embedded knowledge:

1. **How the world evolves:** The agent's knowledge of how the environment changes independent of its actions (e.g., gravity, time passing).
    
2. **What my actions do:** The agent's knowledge of the effects of its own actuators on the world.
    

## Architecture

The architecture connects the **Percepts** (sensors) to the **Internal State** (memory), and then uses the **Internal State** to make a decision using condition-action rules, just like a simple reflex agent—but with context!

$$\text{Action} = f(\text{Current Percept} + \text{Internal State})$$

> _Analogy to OS:_ This is similar to how the operating system (like xv6) maintains the process table or page table as an internal state to accurately manage the system, even when not everything is visible or happening in the immediate moment.