
**Tags:** #os #ipc #concurrency #synchronization #map-of-content

Processes frequently need to cooperate and share information to accomplish tasks. This cooperation, known as Interprocess Communication (IPC), introduces significant complexity. The OS must provide mechanisms to solve three fundamental problems:

1. How to pass information between processes.
    
2. How to ensure two processes do not interfere with each other when accessing shared resources (Mutual Exclusion).
    
3. How to manage dependencies and ensure proper sequencing of actions (Synchronization).
    

This collection of notes provides a deep dive into the classic problems and solutions related to concurrency, from the fundamental nature of race conditions to high-level synchronization primitives like monitors.

### Core Concepts and Problems

- [[The Critical Section Problem]]
    
- [[Early Solutions for Mutual Exclusion]]
    
- [[The Lost Wakeup Problem with Sleep and Wakeup]]
    

### Synchronization Primitives

- [[Semaphores as a Synchronization Tool]]
    
- [[High-Level Synchronization - Monitors and Message Passing]]
    

### Classic Synchronization Case Studies

- [[Solving the Producer-Consumer Problem with Semaphores]]
    
- [[The Dining Philosophers Problem]]
    
- [[The Readers-Writers Problem]]