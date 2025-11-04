### An Informal Guide to RAID (and what those formulas _really_ mean)

Hey! Let's break down that RAID presentation. RAID (Redundant Array of Inexpensive Disks) is all about one simple idea: ganging up a bunch of normal, cheap hard drives to make a single disk system that's either **faster**, **safer** (more reliable), or **bigger**.

The slides judge each RAID level on three things:

1. **Capacity:** How much "useful" space do you get?
    
2. **Reliability:** How many disks can fail before you lose all your data?
    
3. **Performance:** How fast can you read and write?
    

To understand the performance formulas, we first have to meet the "cast of characters"—those variables.

### The "Cast of Characters" (What R, S, N, and D Mean)

This is the most important part. `S` and `R` are _not_ the same!

- **`N` = Number of Disks:** The easiest one. This is just the total number of physical disks in your array.
    
- **`B` = Blocks per Disk:** This is the capacity (in blocks) of a _single_ disk. The total raw capacity you _could_ have is `N * B`.
    
- **`S` = Sequential Speed:** Think of `S` as the **max streaming speed** of a _single_ disk. This is your best-case scenario, like reading one huge, continuous video file. The disk heads just fly over the data. In this case, the main bottleneck is the _transfer rate_ (how fast you can get bits off the platter). The slide calculates this as **47.62 MB/s**.
    
- **`R` = Random Speed:** Think of `R` as the **random access speed** of a _single_ disk. This is your worst-case scenario, like reading a bunch of tiny 10KB files scattered all over the disk. For _each_ tiny file, the disk has to do a full "seek" (move the arm) and "rotate" (wait for the platter to spin). This _positioning time_ is the _massive_ bottleneck. That's why the slide calculates `R` as only **0.981 MB/s**.
    
    **Key takeaway:** `S` (streaming) is _waaaay_ faster than `R` (random) because `R` is dominated by physical seek and rotation delays.
    
- **`D` = Latency:** This is just the _time_ or _delay_ for a single, simple disk operation (a read or a write). We use this to talk about how long an operation _takes_, as opposed to its _speed_ (throughput).
    

### The RAID Levels: Why Their Speeds Are What They Are

Let's walk through the main RAID levels from your slides.

#### RAID 0: "The Speed Demon" (Striping)

- **How it works:** It chops your data into "stripes" and spreads it across all disks. Block 0 goes to Disk 0, Block 1 to Disk 1, Block 2 to Disk 2, and so on.
    
- **Capacity:** `N*B`. You get to use all the space.
    
- **Reliability:** `0`. This is the _worst_ part. If even _one_ disk fails, you lose _all_ your data because pieces of every file are scattered everywhere.
    
- **Performance (The "Why"):**
    
    - **Sequential (Read/Write) = `NS`:** You're reading a big file. Since it's striped, you are reading Block 0, 1, 2, and 3 _all at the same time_ from all `N` disks. You get `N` times the streaming speed. This is pure parallelism.
        
    - **Random (Read/Write) = `NR`:** You're reading `N` different small files. You can send one request to each disk, and all `N` disks can seek and read in parallel. You get `N` times the random speed.
        
    - **Latency = `D`:** A simple read/write is just one operation.
        

#### RAID 1: "The Insurance Policy" (Mirroring)

- **How it works:** No striping. It just makes an exact copy of everything. Block 0 goes to _both_ Disk 0 and Disk 1. Block 1 goes to _both_ Disk 2 and Disk 3. You have `N/2` mirrored pairs.
    
- **Capacity:** `(N/2) * B`. You lose exactly half your total space to make copies.
    
- **Reliability:** `1` (or more). It can _definitely_ survive one disk failure. If you're lucky and a disk _and_ its mirror don't _both_ fail, you could lose up to `N/2` disks.
    
- **Performance (The "Why"):**
    
    - **Writes (Seq/Random) = `(N/2)R` or `(N/2)S`:** When you write, you have to write to _both_ disks in a pair. You have `N/2` pairs, so you can do `N/2` writes in parallel.
        
    - **Random Read = `NR`:** This is the clever part! If you have `N` random read requests, you can send them to _any_ of the `N` disks (since every piece of data exists on two disks). All `N` disks can seek and serve data in parallel.
        
    - **Sequential Read = `(N/2)S`:** You're reading one big file, which only exists on one mirrored pair. You're limited to the speed of that pair. (The slide says `(N/2)S`, so we'll stick with that simple model).
        
    - **Latency = `D`:** Still just one operation (the write happens to both disks at the same time).
        

#### RAID 4: "The Smart Idea... with a Huge Flaw" (Dedicated Parity)

- **How it works:** You get `N-1` disks for data (striped just like RAID 0) and _one_ single disk that is dedicated to "parity."
    
- **What is Parity?** It's just an [XOR](https://en.wikipedia.org/wiki/Exclusive_or "null") calculation. For a "stripe" of blocks `D0`, `D1`, `D2`, the parity block `P` is: `P = D0 ^ D1 ^ D2`. If Disk 1 fails, you can rebuild its data (`D1`) by calculating: `D1 = D0 ^ D2 ^ P`.
    
- **Capacity:** `(N-1) * B`. You lose the space of exactly one disk for this parity safety net.
    
- **Reliability:** `1`. You can lose any single disk (a data disk or the parity disk) and rebuild.
    
- **Performance (The "Why"):**
    
    - **Reads (Seq/Random) = `(N-1)S` or `(N-1)R`:** When you read, you just ignore the parity disk and read from the `N-1` data disks in parallel. It's just like RAID 0 but with one fewer disk.
        
    - **Sequential Write = `(N-1)S`:** This is the "Full Stripe Write." If you're writing a huge file, you're writing new `D0, D1, D2` all at once. Your computer can calculate the new `P` in memory and write all `N` blocks (the `N-1` data + 1 parity) at the same time.
        
    - **Random Write = `R/2`:** **This is the "Small Write Problem" and the** _**killer**_ **flaw of RAID 4.** To write _one_ tiny block (say, a new `D1'`), you can't just write it. You also have to update `P`. The _fastest_ way to do this (the "subtractive" update) is:
        
        1. **Read** the _old_ data `D1`.
            
        2. **Read** the _old_ parity `P`.
            
        3. **Write** the _new_ data `D1'`.
            
        4. **Write** the _new_ parity `P'` (calculated as `P' = (D1' ^ D1) ^ P`).
            
    - This is **4 I/Os for a single write!** Even worse, _every single random write_ in the entire array has to read and write that _one, single_ parity disk. It becomes a massive traffic jam. This is the **parity-disk bottleneck**. The performance is terrible, limited by what that one disk can do.
        
    - **Latency = `2D`:** This is a "read-modify-write" operation. You have to read _first_, then write, so it takes twice as long.
        

#### RAID 5: "The Solution" (Rotating Parity)

- **How it works:** It's _exactly_ the same as RAID 4, but it fixes the bottleneck. Instead of putting all parity blocks on _one_ disk, it "rotates" them across all the disks.
    
- **Capacity:** `(N-1) * B`. Same as RAID 4.
    
- **Reliability:** `1`. Same as RAID 4.
    
- **Performance (The "Why"):**
    
    - **Sequential (Read/Write) = `(N-1)S`:** Same as RAID 4.
        
    - **Random Read = `NR`:** This is _better_ than RAID 4. Since data and parity are _both_ scattered, all `N` disks contain data you might want to read. So, you can do `N` random reads in parallel.
        
    - **Random Write = `(N/4)R`:** **This is the big fix.** You _still_ have to do that horrible 4-I/O "read-modify-write" dance for every small write. _However_, the parity block you need to update is now on a _different disk_ for each stripe.
        
        - A write to Stripe 0 hits Disk 0 (data) and Disk 4 (parity).
            
        - A write to Stripe 1 hits Disk 1 (data) and Disk 3 (parity).
            
    - The bottleneck is gone! All `N` disks can be busy at the same time, all working on their own 4-I/O write operations. Since each write costs 4 I/Os, your total power is `N` disks, each giving 1/4 of its performance. Total speed = `(N * R) / 4`. This is _way_ better than RAID 4.
        
    - **Latency = `2D`:** Same as RAID 4. The _delay_ for a single write is still long, but the _total throughput_ is much higher.
        

### Summary Table

Here's that final slide, but with the "whys" we just talked about.

|Level|Capacity|Reliability|Seq. Read|Seq. Write|Random Read|Random Write|Latency (Write)|
|---|---|---|---|---|---|---|---|
|**RAID 0**|`N*B`|0 (None)|`NS` (Parallel)|`NS` (Parallel)|`NR` (Parallel)|`NR` (Parallel)|`D`|
|**RAID 1**|`(N/2)B`|1+ (Mirror)|`(N/2)S`|`(N/2)S`|`NR` (Can read from either copy)|`(N/2)R`|`D`|
|**RAID 4**|`(N-1)B`|1 (Parity)|`(N-1)S`|`(N-1)S` (Full stripe)|`(N-1)R`|`R/2` (Parity Bottleneck!)|`2D` (Read-Modify-Write)|
|**RAID 5**|`(N-1)B`|1 (Parity)|`(N-1)S`|`(N-1)S` (Full stripe)|`NR` (Data on all disks)|`(N/4)R` (Bottleneck fixed!)|`2D` (Read-Modify-Write)|

Hope this informal breakdown makes more sense of that presentation! It's all about trade-offs between speed, safety, and cost.

Let me know if any of those steps or "why" explanations are still a bit fuzzy!