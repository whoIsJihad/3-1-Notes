
---

### A Bro's Guide to Hard Disk Drives (And Why They're So Slow)

#### Part 1: The Anatomy - What is this thing?

First off, RAM is "volatile" (it forgets when the power's off). A Hard Disk Drive (HDD) is "permanent" storage.

Your Bengali note is perfect: RAM is volatile, disk/SSD is for permanent storage.

At its simplest, an HDD is just a stack of magnetic "CDs" (called **Platters**) that spin around a central axle (the **Spindle**). A tiny "hand," called the **Disk Arm**, holds a **Disk Head** (the read/write part) that floats _nanometers_ above the platter surface.

Your notes also got the storage hierarchy right:

- A platter **Surface** (top and bottom) is covered in magnetic bits.
    
- The surface is divided into thousands of concentric circles, like lanes on a running track. These are **Tracks**.
    
- Each track is chopped up into little 512-byte or 4KB segments. These are **Sectors**. A sector is the _smallest_ unit you can read or write.
    

So, an "address" for a piece of data is basically: "Platter 3, Surface 1, Track 2048, Sector 15."

#### Part 2: The Three Delays (The "Why is it SO SLOW?")

When your OS says "read this 4KB block of data," the total time it takes is dominated by physics. This is the _most important equation_ in this whole chapter:

**`T_I/O = T_seek + T_rotation + T_transfer`**

This is the total time for _one_ I/O operation. Let's break down each part.

##### 1. Seek Time (`T_seek`)

- **What it is:** The time it takes for the **Disk Arm** to physically move the **Disk Head** from its current track to the track you want to read.
    
- **Analogy:** This is _exactly_ like picking up the needle on a vinyl record player and moving it to a different song.
    
- **What this involves (from your slides):** The arm has to `Accelerate`, maybe `Coast` at top speed, `Decelerate`, and then `Settle` (it wiggles a bit) before it's perfectly aligned.
    
- **Time:** This is the _slowest_ part. A "fast" drive (like the Cheetah 15K.5 in your slides) still takes an _average_ of **4 milliseconds (ms)**. A slow one takes 9ms.
    

##### 2. Rotational Delay (`T_rotation`)

- **What it is:** The platter is _always spinning_ (e.g., at 7200 RPM). Once the head _arrives_ at the correct track (after the seek), it has to _wait_ for the platter to spin around so the sector you _want_ is physically underneath the head.
    
- **Your Slide Example:** "30 read korchilam ekhon 24 read korte chai... wait kora lagbe." (I was reading 30, now I want to read 24... I have to wait). This is it! If sector 24 _just_ spun past, you have to wait for an _entire rotation_ for it to come back.
    
- **The Math:**
    
    - 7200 Rotations Per Minute (RPM) = 120 Rotations Per Second (RPS).
        
    - 1 rotation takes: `1 / 120s` = `8.33 milliseconds (ms)`.
        
    - **The Key:** We don't know _where_ the platter will be. On _average_, we'll have to wait for **half a rotation**.
        
    - **Average `T_rotation` = (1/2) * 8.33ms = ~4.17ms.** (Your slides use 4ms, which is a great estimate).
        

##### 3. Transfer Time (`T_transfer`)

- **What it is:** The _actual_ time it takes to read the data off the platter, _once the head is in the right place and the sector is spinning underneath it_.
    
- **What this depends on:** How fast the disk spins and how densely the bits are packed. This is given as the "Max Transfer Rate" (e.g., 105 MB/s).
    
- **The Math:** `T_transfer = Size_To_Read / Transfer_Rate`
    
- **Time:** This part is _fast_. To read 4KB: `4KB / 105 MB/s = 0.000038 seconds = 0.038ms`.
    

---

#### Part 3: The Big "Ah-Ha!" Moment: Random vs. Sequential

This is where it all comes together. This is why your OS _hates_ HDDs.

##### Case 1: Random 4KB Read (The "Worst Case")

Let's use the Barracuda drive from your slides (9ms seek, 7200 RPM, 105MB/s). Your program wants to read a _single_ 4KB block.

T_I/O = T_seek + T_rotation + T_transfer

T_I/O = 9.0ms + 4.17ms + 0.038ms

T_I/O ≈ 13.2ms

Think about this. It took **13.2 milliseconds** to do the read. But the _actual work_ (`T_transfer`) took only **0.038ms**.

**This means 99.7% of the time was spent _waiting_ (seeking and rotating).**

This is _abysmally_ bad. The effective speed isn't 105 MB/s, it's `4KB / 13.2ms = 0.3 MB/s`. You get _less than 1%_ of the "max" speed.

##### Case 2: Sequential 100MB Read (The "Best Case")

Now your program wants to read a _single, huge_ 100MB file.

T_I/O = T_seek + T_rotation + T_transfer

T_I/O = 9.0ms + 4.17ms + (100MB / 105MB/s)

T_I/O = 9.0ms + 4.17ms + 952ms

T_I/O ≈ 965ms

Now look. The _total_ time was ~965ms. The _work_ (`T_transfer`) took 952ms.

**This means 98.6% of the time was spent _doing useful work_.**
Why do we add the T_seek and T_rotation only once? Read [[ Why sequential is better in Disk IO ?]]

The seek/rotation overhead was _nothing_ compared to the massive transfer. The effective speed is `100MB / 965ms = 103.6 MB/s`. That's almost the max!

THE GRAND CONCLUSION:

HDDs are AMAZING at sequential I/O (reading one big file).

HDDs are HORRIBLE at random I/O (jumping around).

This is why:

- File "defragmentation" was a thing (it turns random files into sequential ones).
    
- Databases will do _anything_ to avoid random reads.
    
- Your OS File System uses a "buffer cache" to absorb random _writes_ and write them out sequentially later.
    

---

#### Part 4: The Built-in Hacks (How Drives Cheat)

Your slides cover some brilliant tricks hardware engineers use to fight physics.

##### Hack 1: ZBR (Zoned Bit Recording)

- **Problem:** A track on the _outer_ edge of the platter is way longer than a track on the _inner_ edge. If you put the same number of sectors on each, you're wasting tons of space on the outside.
    
- **Solution:** **Multi-Zoned** recording. Group tracks into "zones." Outer-edge zones get _more sectors per track_ than inner zones.
    
- **Bonus:** This also means the **transfer rate is _higher_ on the outer tracks** (more bits fly under the head per second).
    

##### Hack 2: Track Skew

- **Problem:** You're reading a huge file. You finish `Track 10, Sector 79` (the last sector). The next block is `Track 11, Sector 0`.
    
- You _have to_ seek (move the arm) from Track 10 to Track 11. This takes time (e.g., 1ms).
    
- _While you're seeking, the platter is still spinning!_
    
- By the time the head _arrives_ at Track 11, `Sector 0` has _already spun past_. You've missed it.
    
- **Result:** You have to wait for an _entire new rotation_ (8.33ms!) just to catch `Sector 0`.
    
- **Solution:** **Track Skew.** The hardware _intentionally_ offsets the starting sector of each track. `Sector 0` on `Track 11` isn't aligned with `Sector 0` on `Track 10`. It's "skewed" by a few sectors, giving the head _just enough time_ to seek and "catch" the new sector perfectly.
    
- **Your Note:** "24 same jaygay shuru kora hoyna, jeno track change korar por 24 head-er niche ashe." (24 isn't started at the same place, so that after the track change, 24 arrives under the head.) **This is 100% correct.**
    

##### Hack 3: The On-Board Cache (Track Buffer)

- **Problem:** The OS is "chatty." It asks for 4KB. Then another 4KB. Then another.
    
- **Solution:** Put a chunk of RAM (e.g., 16-256 MB) _on the disk's controller board_.
    
- **Read-Ahead:** When the OS asks for Sector 30, the drive is smart. It reads Sector 30 _and the rest of the entire track_ (31, 32, etc.) into its super-fast cache. When the OS inevitably asks for Sector 31, the drive gives it _instantly_ from its cache (0ms seek, 0ms rotation).
    
- **Write Caching:**
    
    - **Write-Through:** OS says "save this." Drive writes to cache _and_ to the platter. _Only after_ the platter-write is done, it tells the OS "OK." (Safe, but slow).
        
    - **Write-Back:** OS says "save this." Drive writes to its cache _and immediately_ tells the OS "OK, I'm done!" (Super-fast). The drive _promises_ to write it to the platter later.
        
- **The Danger (from your slides):** What if the drive uses Write-Back, lies to the OS, and then the power cuts out? The data in the cache is _gone_. The OS _thinks_ it was saved, but it's lost. This is **data corruption**.
    
- **The OS-Level Fix (Journaling):** The OS _knows_ the drive lies. So, modern file systems (ext4, NTFS) use **journaling**. Before writing the _real_ data, it first writes a tiny _log_ (a "journal") that says "I am _about to_ write data X to location Y." If the power dies, on reboot, the OS reads the log, sees the _intention_, and re-does the operation.
    

---

### 5 Levels of Practice Questions

**Level 1: The Definitions (Easy Mode)**

1. What's the difference between a Track and a Sector?
    
2. What are the _three_ physical components of `T_I/O`?
    
3. What is "Rotational Delay"?
    

**Level 2: Compare & Contrast (Gettin' Warmer)**

1. Explain the danger of "Write-Back" caching.
    
2. What problem does "Track Skew" solve?
    
3. Why is "Zoned Bit Recording" (ZBR) a good idea?
    

**Level 3: The Math (Classic Exam Question)**

- You have a new drive with these specs:
    
    - **RPM:** 10,000 RPM
        
    - **Avg. Seek:** 6 ms
        
    - **Max Transfer:** 200 MB/s
        

1. What is the average `T_rotation` in milliseconds?
    
2. What is the total `T_I/O` for a **single 4KB random read**?
    
3. What is the _effective transfer rate_ for that random read (in MB/s)?
    

**Level 4: The "Why" (Analyze This)**

1. Why is the _effective_ I/O rate for random reads so much _worse_ than the drive's "Max Transfer Rate"?
    
2. What did a "disk defragmenter" utility _do_, and _why_ did it make a computer feel faster? (Hint: Think Sequential vs. Random).
    
3. If you have a 7200 RPM drive and a 5400 RPM drive (which is slower), which _part_ of the `T_I/O` equation gets worse?
    

**Level 5: The "Design" (Nightmare Mode)**

1. You are designing a database file format. You need to store 10 million user records, each 1KB. To get the _fastest possible_ read-time for _all_ records (a "full table scan"), how would you _physically_ lay them out on an HDD?
    
2. Why is an SSD (Solid State Drive) _so much faster_ at "random I/O" than an HDD? (Hint: Which of the three `T_I/O` components does an SSD have?)