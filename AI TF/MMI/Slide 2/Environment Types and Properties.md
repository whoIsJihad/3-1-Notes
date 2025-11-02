# Environment Types and Properties: The Six Dimensions

The task environment defines the world an agent operates in. Understanding these six binary properties helps determine the complexity of the problem and the required sophistication of the agent.

## 1. Observable? (Fully vs. Partially Observable)

This dimension asks: **Can the agent see everything relevant to its decision-making?**

- **Fully Observable (Known State):**
    
    - The agent's sensors give it access to the **complete state** of the environment at all times.
        
    - The agent doesn't need to maintain an internal memory of the world's state, because the current percept is sufficient.
        
    - _Example:_ **Chess** (with no hidden pieces). The agent can see the entire board, all the pieces, and know whose turn it is. The state is fully known.
        
- **Partially Observable (Unknown State):**
    
    - The agent's sensors only give it access to a part of the environment, or the sensors are noisy/inaccurate.
        
    - This is the common scenario in the real world (e.g., your camera can't see behind a building).
        
    - _Example:_ **Driving.** You can't see the interior of other cars, the entire road network, or what a pedestrian will do next. The agent must use its **internal memory (state)** to track what it can't see.
        

## 2. Deterministic? (Deterministic vs. Stochastic)

This dimension asks: **Is the next state entirely predictable from the current state and the action?**

- **Deterministic:**
    
    - The next state of the environment is **completely determined** by the current state and the action executed. There is no randomness involved.
        
    - _Example:_ **Solving a Sudoku puzzle.** If you put the number '5' in a specific square, the resulting board state is guaranteed.
        
- **Stochastic:**
    
    - The next state is **not entirely predictable** due to random factors outside the agent's control.
        
    - _Example:_ **A robotic arm picking a part off a conveyor belt.** Even if the agent executes the same action, the part might slip slightly, or a gust of wind might introduce noise. The result is uncertain.
        
    - **Strategic Environment:** If the uncertainty is _only_ due to the actions of **other agents** (and not environmental randomness), it's called strategic (e.g., Chess, where the opponent's move is the uncertain factor).
        

## 3. Episodic? (Episodic vs. Sequential)

This dimension asks: **Do past actions matter for future decisions?**

- **Episodic:**
    
    - The agent's experience is divided into separate, **atomic episodes**. The action in one episode **does not affect** the actions or decisions in future episodes.
        
    - _Example:_ **An image classification system.** The decision on whether _Image A_ shows a cat is completely independent of the decision on whether _Image B_ shows a dog.
        
- **Sequential:**
    
    - The current action determines the next state, and thus **impacts all future decisions**. Most real-world problems are sequential.
        
    - _Example:_ **Playing a game of Chain Reaction** (like in your AI coursework) or **Driving**. Steering left now affects where you can go for the rest of the trip. The agent must think ahead.
        

## 4. Static? (Static vs. Dynamic)

This dimension asks: **Does the environment change while the agent is deciding what to do?**

- **Static:**
    
    - The environment remains **unchanged** while the agent is deliberating (thinking). This makes planning easier.
        
    - _Example:_ **A Crossword Puzzle.** The grid and the clues won't change while you're thinking about the next word.
        
- **Dynamic:**
    
    - The environment can **change while the agent is deliberating**. The agent must constantly monitor the environment.
        
    - _Example:_ **Autonomous driving.** While the agent is calculating the braking distance, the car in front might brake suddenly, or a pedestrian might step into the road.
        
- **Semi-dynamic:**
    
    - The environment itself does not change, but the agent's performance score does with the passage of time (e.g., Chess with a clock. The board state is static, but running out of time hurts your score).
        

## 5. Discrete? (Discrete vs. Continuous)

This dimension asks: **Are the state and actions clearly defined and finite, or are they continuous?**

- **Discrete:**
    
    - A limited, countable set of distinct, clearly defined percepts and actions.
        
    - _Example (Percepts):_ Clean/Dirty, 10 or 15 or 20 (sensor value ranges).
        
    - _Example (Actions):_ Left, Right, Suck, NoOp (Vacuum Cleaner Agent).
        
- **Continuous:**
    
    - States and actions can take on a range of real-number values.
        
    - _Example (Percepts):_ Temperature, light intensity, exact GPS coordinates.
        
    - _Example (Actions):_ Steering wheel angle ($\theta \in [-\pi, \pi]$), throttle pressure (any value between 0% and 100%).
        

## 6. Agents? (Single Agent vs. Multi-agent)

This dimension asks: **Is the agent acting alone, or are there other intelligent actors?**

- **Single Agent:**
    
    - The agent is operating by itself in the environment. All changes are due to the environment's physics or the agent's own actions.
        
    - _Example:_ **Medical diagnosis system** (The doctor/staff are part of the environment, not opposing agents).
        
- **Multi-agent:**
    
    - There are **other intelligent agents** whose actions affect the overall performance measure.
        
    - _Example:_ **Playing Football.** Your agent must cooperate with teammates and compete against the opposing team.
        
    - This is the most complex domain, as it requires the agent to reason about the _beliefs, goals, and intentions_ of other agents.
        
