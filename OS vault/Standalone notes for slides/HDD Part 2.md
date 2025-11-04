
- **Part 1 (Last time):** We learned that HDDs are slow, and the `T_seek` (moving the arm) is the _absolute worst_ part of the delay.
    
- **Part 2 (These slides):** Now we're gonna see how the OS is "disk-aware" and _fights_ that slowness.
    

This is a two-act play:

1. **Disk Scheduling:** How to be smart about _one_ disk.
    
2. **RAID:** How to be smart by "ganging up" _multiple_ disks.
    

Let's do this.

---

### A Bro's Guide to Disk Scheduling & RAID

#### Part 1: Disk Scheduling (The "Elevator Bouncer")

The problem is simple. Your OS has a _queue_ of I/O requests for the disk. In your slide's example, the queue is `[98, 183, 37, 122, 14, 124, 65, 67]` and the head is currently at track `53`.

The OS has to decide _which request to do next_. This choice is the **Disk Scheduling Algorithm**. The goal is to **minimize total seek time**.

##### 1. FCFS (First-Come, First-Served)

- **How it works:** The "dumb" way. Just do them in the order they arrived.
    
- **The Path:** `53 -> 98 -> 183 -> 37 -> 122 -> 14 -> 124 -> 65 -> 67`
    
- **Why it sucks:** Look at that path! The head is flying back and forth like a maniac. Your Bengali note is dead on: "head কে বারবার move করানো লাগছে" (the head has to move back and forth a lot).
    
- **Total Movement:** 640 cylinders. Terrible.
    

##### 2. SSTF (Shortest Seek Time First)

- **How it works:** A "greedy" approach. From the head's current spot, _always_ pick the _closest_ request, no matter when it arrived.
    
- **The Path (from 53):**
    
    - Closest is `65` (12 away)
        
    - Next closest is `67` (2 away)
        
    - Next closest is `37` (30 away)
        
    - ...and so on. `53 -> 65 -> 67 -> 37 -> 14 -> 98 -> 122 -> 124 -> 183`
        
- **Why it's good:** Way less movement! Only 236 cylinders.
    
- **Why it sucks (The Fatal Flaw):** **Starvation**. Imagine requests keep arriving for tracks `50`, `55`, `60`... The head will just stay in that "busy" area, and the request for track `183` will _never_ get serviced. It starves.
    

##### 3. SCAN (The "Elevator" Algorithm)

- **How it works:** This is the smart fix. The head moves in _one direction_ (say, `UP`). It services _every_ request in its path. When it hits the _very end_ of the disk (track 199), it reverses and services all requests on the way `DOWN`.
    
- **Why it's good:** It's fair! No starvation. It _will_ eventually get to track 183.
    
- **The Problem:** Your Bengali note nailed it: "মাঝখানের track গুলো বেশি advantage" (middle tracks get more advantage). If your request is at track 0, you _just_ missed the elevator. You have to wait for it to go _all the way_ to 199 and come _all the way back_.
    

##### 4. C-SCAN (Circular-SCAN)

- **How it works:** A simple tweak to SCAN to make it _more_ fair.
    
    - **`UP` Sweep:** Services requests (e.g., `53 -> 65 -> ... -> 183`).
        
    - **At the end (199):** It does _not_ reverse. It _immediately_ "warps" back to track 0 (a single, fast seek).
        
    - **`DOWN` Sweep:** It _services nothing_ on the way back.
        
    - It then starts its `UP` sweep again from 0.
        
- **Why it's better:** "Provides a more uniform wait time." The _worst-case_ wait is now one full `UP` sweep. Nobody has to wait for a full "round trip."
    

##### 5. LOOK & C-LOOK (The "Smartest" Elevator)

- **How it works:** This is the real-world optimization. The C-SCAN algorithm is dumb for going all the way to track 199 if its last request is at `183`.
    
- **C-LOOK:** It's C-SCAN, but it only goes as far as the _last request_ in its direction.
    
    - **The Path (from 53):** `53 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183` (the _last_ request in this direction).
        
    - **Then:** It _warps_ back... not to 0, but to the _first_ request in the other direction (`14`).
        
    - **Then:** `14 -> 37`
        
    - **Then:** Warps back to `65` (or `53` if it just arrived) and continues.
        
- **This is the winner.** It's fair (no starvation) and efficient (no wasted seeks). Your slides are right: SSTF or LOOK are the reasonable default choices.
    

---

#### Part 2: RAID (How to Build a "Super-Disk")

The problem: A single disk is slow and unreliable (if it dies, you cry).

The solution: RAID (Redundant Array of Inexpensive Disks). We "team up" multiple disks.

We judge every RAID level on 3 things: **Capacity** (how much space?), **Reliability** (can it survive a disk failure?), and **Performance** (how fast?).

##### 1. RAID-0: "Striping"

- **How it works:** Chops data into blocks. Block 0 on Disk 0, Block 1 on Disk 1, Block 2 on Disk 2...
    
- **Analogy:** The "Go-Fast" mode.
    
- **Capacity:** `N * B` (N disks, B blocks each). You get _all_ the space.
    
- **Reliability:** **ZERO.** Your Bengali note is perfect: "একটা disk নষ্ট হলেই পুরো data gone." If you lose _one_ disk, you lose _everything_. It's an array of _increased_ risk.
    
- **Performance:** _Insanely fast_. `N * S` (N times sequential speed) and `N * R` (N times random speed).
    

##### 2. RAID-1: "Mirroring"

- **How it works:** Every byte is written _twice_, once on Disk 0 and a _copy_ on Disk 1.
    
- **Analogy:** The "Super Paranoid" mode.
    
- **Capacity:** `(N * B) / 2`. You pay 2x for your storage.
    
- **Reliability:** _Extremely high_. You can lose a disk (or N/2 disks, if you're lucky) and the system doesn't even blink.
    
- **Performance:**
    
    - **Reads:** Fast! (`N*R`). You can read from _all_ disks at once.
        
    - **Writes:** Slow. (`(N/2)R`). Your Bengali note is right: "একই block ২ জায়গায় write করছি, speed কমে যাবে." (I'm writing the same block to 2 places, speed will decrease).
        

##### 3. RAID-4: "Dedicated Parity Disk"

- **How it works:** The "Smart Compromise." You have `N-1` data disks (like RAID-0) and _one_ dedicated "Parity" disk.
    
- **The Magic (Parity):** Parity is just an [XOR operation](https://www.google.com/search?q=https://en.wikipedia.org/wiki/Bitwise_operation%23XOR). `Parity = D0 ^ D1 ^ D2`. If Disk 1 _dies_, you can recreate it: `D1_lost = D0 ^ D2 ^ Parity`.
    
- **Capacity:** `(N-1) * B`. (Pretty good!)
    
- **Reliability:** Can survive 1 disk failure. (Good!)
    
- **Performance:**
    
    - **Reads (Sequential & Random):** Great! `(N-1)` times faster.
        
    - **Writes (Sequential):** Great! You just compute the parity and write it all at once.
        
    - **Writes (Random):** **HORRIBLE.** This is the "Small Write Problem."
        
        - To write _one_ tiny block to `D0`, you _also_ have to update the `Parity` disk.
            
        - This creates a **Parity Disk Bottleneck**. _Every single write_ slams that _one_ parity disk.
            
        - Your slides show this: the random write performance is `R/2`, which is _terrible_ (even worse than a single disk!).
            

##### 4. RAID-5: "Rotated Parity" (The Real-World Winner)

- **How it works:** It's _identical_ to RAID-4, but it _distributes_ the parity block.
    
- **Analogy:** The "Bottleneck-Solver."
    
- Look at the diagram (Slide 27): `P0` is on Disk 4, `P1` is on Disk 3, `P2` is on Disk 2...
    
- **Why?** It _solves_ the bottleneck. Now, a random write to `D0` (which uses `P0` on Disk 4) can happen _at the same time_ as a random write to `D4` (which uses `P1` on Disk 3).
    
- **Capacity:** `(N-1) * B` (Same as RAID-4)
    
- **Reliability:** 1 disk failure (Same as RAID-4)
    
- **Performance:** All-around excellent. It fixes the random-write problem. The performance is `(N*R)/4` (as per slide 28) because _all N disks_ can participate in writes, but each "small write" operation is 4x slower than a read.
    

---

### 5 Levels of Practice Questions

**Level 1: The Definitions (Easy Mode)**

1. What is the _fatal flaw_ of SSTF (Shortest Seek Time First)?
    
2. What's the difference between SCAN and C-SCAN?
    
3. What's the difference between RAID-0 (Striping) and RAID-1 (Mirroring) in terms of their primary _goal_?
    

**Level 2: Compare & Contrast (Gettin' Warmer)**

1. What is the "Parity Disk Bottleneck" in RAID-4, and how does RAID-5 _specifically_ solve it?
    
2. Why is C-LOOK (and LOOK) a better _practical_ choice than C-SCAN (and SCAN)?
    
3. Looking at the final summary slide (29), why is RAID-1 _slower_ for Random Writes (`(N/2)R`) than RAID-0 (`NR`), but _faster_ than RAID-4 (`R/2`)?
    

**Level 3: The Trace (Classic Exam Question)**

- **Queue:** `[100, 50, 180, 70, 120, 10, 140, 20]`
    
- **Head starts at:** `90`
    
- **Disk size:** 0-199
    
- **Initial Direction:** `UP` (towards 199)
    
- **Task:** Write the _exact path_ (the order of tracks serviced) for:
    
    1. SSTF
        
    2. SCAN (the "Elevator")
        
    3. C-LOOK (the "Smart Elevator")
        

**Level 4: The "Why" (Analyze This)**

1. A database server does _lots_ of small, random writes. Why would RAID-5 be a _vastly_ superior choice over RAID-4 for this workload?
    
2. You have two disks. You can _only_ choose between RAID-0 and RAID-1.
    
    - Which one do you use for your _Steam game library_? Why?
        
    - Which one do you use for your _university thesis_? Why?
        
3. Your slide on FCFS shows 640 cylinders of movement. Your slide on SSTF shows 236. _Both_ slides are for the _exact same queue_. How can the _total_ movement be so different?
    

**Level 5: The "Design" (Nightmare Mode)**

1. You have _four_ 1TB disks. You need a storage system that is _both_ fast _and_ can survive _at least one_ disk failure. What two RAID levels from your slides would you choose between, and what is the final **Capacity**, **Reliability** (in disks), and **Performance** (for Random Writes) of each?
    
2. (From Slide 29): The Random Write "Latency" (the last row) for RAID-4 and RAID-5 is `2D` (twice the latency of a single disk). Why? (Hint: Think about the "Small Write Problem" and what `R-M-W` stands for... how many I/Os are needed?)
    

---

Phew! That's a _ton_ of info. Those slides cover two of the most important concepts for disk management.

