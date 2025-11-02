
**Tags:** #os #ipc #concurrency #deadlock #starvation

The Dining Philosophers problem is a famous synchronization puzzle conceived by Edsger Dijkstra. It serves as a canonical example to illustrate the profound difficulties of avoiding **deadlock** when allocating multiple shared resources among competing processes.

### The Setup

- Five philosophers sit at a circular table.
    
- In the center of the table is a large bowl of spaghetti.
    
- Between each pair of adjacent philosophers is a single chopstick. There are five chopsticks in total.
    
- A philosopher's life alternates between two states: **thinking** and **eating**.
    
- To eat, a philosopher requires **two** chopsticks: the one on their immediate left and the one on their immediate right.
    

The chopsticks are the shared resources. The problem is to design a protocol (an algorithm) for picking up and putting down chopsticks that allows philosophers to eat without the system grinding to a halt.

### The Naive Solution and Guaranteed Deadlock

The most straightforward approach is for each philosopher to pick up their left chopstick, then their right chopstick.

```
// Pseudocode for philosopher i
while (TRUE) {
    think();
    take_chopstick(i);        // Pick up left chopstick
    take_chopstick((i+1) % 5); // Pick up right chopstick
    eat();
    put_down_chopsticks();
}
```

**The Deadlock Scenario:** This seemingly logical approach leads to a classic deadlock if the timing is just right (or wrong):

1. Philosopher 0 picks up their left chopstick (chopstick 0).
    
2. Simultaneously, Philosopher 1 picks up their left chopstick (chopstick 1).
    
3. This continues around the table: Philosopher 2 takes chopstick 2, P3 takes 3, and P4 takes 4.
    
4. Now, every philosopher is holding their left chopstick and is waiting for their right chopstick to become available.
    
5. The right chopstick for each philosopher is the left chopstick of their neighbor, which is already held.
    

A circular wait condition is established. No one can proceed. This is a total deadlock.

### A Deadlock-Free Solution (Tanenbaum's Solution)

A correct solution must break the circular wait condition. One elegant way to do this is to ensure that a philosopher only picks up chopsticks if **both** are available, and this check is performed inside a critical section.

This solution uses a state array (`THINKING`, `HUNGRY`, `EATING`) and an array of semaphores that philosophers block on if they cannot get the chopsticks they need.

```
#define N 5
int state[N];
semaphore mutex = 1;
semaphore s[N]; // One per philosopher, all initialized to 0

void philosopher(int i) {
    while (TRUE) {
        think();
        take_forks(i);
        eat();
        put_forks(i);
    }
}

void take_forks(int i) {
    down(&mutex);             // Enter critical region
    state[i] = HUNGRY;        // Record that I am hungry
    test(i);                  // Try to acquire my two forks
    up(&mutex);               // Exit critical region
    down(&s[i]);              // Block if forks were not acquired
}

void put_forks(int i) {
    down(&mutex);             // Enter critical region
    state[i] = THINKING;
    test((i+4) % N);          // See if my left neighbor can now eat
    test((i+1) % N);          // See if my right neighbor can now eat
    up(&mutex);               // Exit critical region
}

// Check if philosopher i can eat now
void test(int i) {
    if (state[i] == HUNGRY && state[(i+4)%N] != EATING && state[(i+1)%N] != EATING) {
        state[i] = EATING;
        up(&s[i]); // Signal philosopher i that they can proceed to eat
    }
}
```

This solution is more complex but it prevents deadlock. However, it is still possible (though unlikely) for a philosopher to **starve** if their two neighbors conspire to eat in a pattern that always prevents them from acquiring both chopsticks when they are hungry.