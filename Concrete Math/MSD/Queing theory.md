# Part 2: Queueing Theory (The Application)

This file covers the _application_ of our theory. Queueing (waiting line) theory is the most common use of Birth-Death processes.

## 1. What is Queueing Theory?

Queueing theory is the mathematical study of waiting lines. It's used in any system where there is a **finite resource** and a **high demand** for it.

- Customers waiting at a checkout.
    
- Data packets waiting in a router.
    
- Cars waiting at a toll booth.
    

## 2. The Four Key Metrics ($L, L_Q, W, W_Q$)

We measure the "performance" of a queue using four key variables:

- $L$: The **Average Length** of the _system_ (total customers, both waiting and being served).
    
- $L_Q$: The **Average Length** of the _queue_ (only customers waiting).
    
- $W$: The **Average Wait** (time) in the _system_ (total time from arrival to departure).
    
- $W_Q$: The **Average Wait** (time) in the _queue_ (only the time spent waiting).
    

## 3. The Master Key: Little's Law

Your notes show a "Basic Cost Identity" that gives us a simple, powerful formula to connect these metrics.

- **Identity:** (Avg. rate the system earns) = (Avg. arrival rate) $\times$ (Avg. amount each customer pays)
    
- **Derivation:**
    
    1. Assume the system earns $1 per second for each customer _in the system_. The avg. earnings are just $L \times \$1 = \mathbf{L}$.
        
    2. The avg. arrival rate is $\mathbf{\lambda}$.
        
    3. A customer pays $1 per second for the _entire time_ they are in the system. Their avg. time is $W$. So their avg. payment is $W \times \$1 = \mathbf{W}$.
        
    4. Plug into the identity: $L = \lambda W$
        

This is **Little's Law**. It's the most important formula in queueing theory. It works for the whole system _and_ just for the queue:

- $L = \lambda W$
    
- $L_Q = \lambda W_Q$
    

## 4. Different Types of Probabilities

Your notes mention three types of "limiting probabilities":

- $P_n$: The **Steady-State Probability**. This is the one we found in Part 1. It's the proportion of _time_ the system has $n$ customers.
    
    - (e.g., $P_0 = 0.3$ means the system is _empty_ 30% of the time).
        
- $a_n$: The **Arrival Probability**. The proportion of _arriving customers_ who find $n$ people already in the system.
    
- $d_n$: The **Departure Probability**. The proportion of _departing customers_ who leave behind $n$ people.
    

A key proposition from your notes is that **for Poisson Arrivals,** $P_n = a_n$. This is a very important property called "Poisson Arrivals See Time Averages" (PASTA). It means the system's long-run average is the same as what an "average" arriving customer sees.