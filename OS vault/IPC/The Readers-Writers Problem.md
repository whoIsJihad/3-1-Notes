# The Readers-Writers Problem

**Tags:** #os #ipc #synchronization #concurrency-problem #starvation

The **Readers-Writers Problem** is a classic concurrency problem that models access to a shared data resource (e.g., a database). Processes are categorized into two types:

- **Readers:** Processes that only read the data.
    
- **Writers:** Processes that modify the data.
    

The constraints are:

1. Any number of readers can access the resource simultaneously.
    
2. Only one writer can access the resource at any time.
    
3. If a writer is active, no reader may access the resource.
    

This problem highlights the trade-offs between maximizing concurrency (letting all readers in) and avoiding starvation. There are two primary approaches to solving it.

### Case 1: Reader-Priority Solution

This solution prioritizes getting readers into the critical section as quickly as possible. If a stream of readers arrives, they will continuously be let in, even if a writer is waiting.

**Shared Variables:**

```
semaphore mutex = 1; // Controls access to 'rc'
semaphore db = 1;    // Controls access to the database
int rc = 0;          // Number of active readers
```

**Code:**

```
void reader(void) {
    while (TRUE) {
        down(&mutex);
        rc = rc + 1;
        if (rc == 1) {
            down(&db); // First reader locks out writers
        }
        up(&mutex);

        read_data_base();

        down(&mutex);
        rc = rc - 1;
        if (rc == 0) {
            up(&db);   // Last reader lets writers in
        }
        up(&mutex);
    }
}

void writer(void) {
    while (TRUE) {
        down(&db);
        write_data_base();
        up(&db);
    }
}
```

**Analysis:**

- **How it works:** The `db` semaphore acts as the primary lock on the database. The _first_ reader to arrive acquires this lock, and the _last_ reader to leave releases it. All readers in between can bypass this lock, allowing them to read concurrently. The `mutex` simply protects the shared `rc` counter.
    
- **Critical Flaw: Writer Starvation.** As the lecture slides correctly point out, this solution gives "inherent priority to the readers." If new readers are constantly arriving before the last active reader has a chance to leave, `rc` will never become zero. Consequently, `up(&db)` is never called, and any waiting writer will be **starved** indefinitely.
    

### Case 2: Writer-Priority Solution

This solution addresses writer starvation by giving priority to any waiting writer. Once a writer arrives, it should get access to the resource as soon as possible, and any new readers that arrive after the writer will be blocked.

**Shared Variables:**

```
int rc = 0, wc = 0;         // reader count, writer count
semaphore r_mutex = 1, w_mutex = 1; // mutex for rc, wc
semaphore read_try = 1;     // allows readers to try entering
semaphore db = 1;           // exclusive access for writers
```

**Code:**

```
void reader(void) {
    while (TRUE) {
        down(&read_try);       // Can I try to read?
        down(&r_mutex);
        rc = rc + 1;
        if (rc == 1) {
            down(&db);         // First reader locks the db
        }
        up(&r_mutex);
        up(&read_try);         // OK for other readers to try

        read_data_base();

        down(&r_mutex);
        rc = rc - 1;
        if (rc == 0) {
            up(&db);           // Last reader frees the db
        }
        up(&r_mutex);
    }
}

void writer(void) {
    while (TRUE) {
        down(&w_mutex);
        wc = wc + 1;
        if (wc == 1) {
            down(&read_try);   // First writer locks out new readers
        }
        up(&w_mutex);

        down(&db);
        write_data_base();
        up(&db);

        down(&w_mutex);
        wc = wc - 1;
        if (wc == 0) {
            up(&read_try);     // Last writer lets readers try again
        }
        up(&w_mutex);
    }
}
```

**Analysis:**

- **How it works:** The `read_try` semaphore acts as a gate. The _first_ writer to arrive locks this gate (`down(&read_try)`). This immediately blocks any _new_ readers who arrive later from getting past their own `down(&read_try)` call. The writer then waits for the database itself via `down(&db)`. The _last_ writer to leave opens the `read_try` gate again.
    
- **Critical Flaw: Reader Starvation.** This solution fixes writer starvation but introduces the opposite problem. If writers are constantly arriving, one writer will release the `read_try` lock, but another waiting writer will immediately acquire it again. A continuous stream of writers can perpetually lock the `read_try` gate, causing **reader starvation**.
    

Neither solution is perfect; they represent a fundamental trade-off in managing concurrent access. More complex, fair solutions often involve more intricate mechanisms like turnstiles or reader/writer locks with upgrade/downgrade capabilities.