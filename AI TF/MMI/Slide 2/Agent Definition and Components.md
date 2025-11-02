# Agent Definition and Components

An **Agent** is anything that can be viewed as perceiving its environment through **sensors** and acting upon that environment through **actuators** (or effectors).

## Key Components

An intelligent agent needs three components:

1. **Perception (via Sensors):** Perceiving information from the environment.
    
    - _Examples (Human):_ Eyes, ears, skin, etc.
        
    - _Examples (Robotic):_ Cameras, infrared range finders.
        
2. **Processing:** Processing the perceived information.
    
3. **Action (via Actuators):** Generating and implementing an action on the environment.
    
    - _Examples (Human):_ Hands, legs, mouth.
        
    - _Examples (Robotic):_ Various motors.
        

> **Agent Architecture:** The physical configuration (wheels, sensors, motors, etc.). **Agent Program:** The function that maps percept histories to actions ($f: P^* \rightarrow A$).
> 
> $$\text{Agent} = \text{Architecture} + \text{Program}$$

## Learning

**Learning** is an **iterative and incremental** method. It gradually improves the agent's performance by avoiding mistakes over time.