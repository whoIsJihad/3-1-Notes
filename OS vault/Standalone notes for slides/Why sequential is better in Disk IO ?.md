
### The Simple Answer: The "Streaming" Analogy

Think of T_seek and T_rotation as the "find and setup" cost.

Think of T_transfer as the "streaming" cost.

1. **Finding the File (The One-Time Penalty):** To read your 100MB file, the OS first has to find its _starting block_. This requires:
    
    - One **average seek** (`T_seek`) to move the head to the file's _first_ track (e.g., 9ms).
        
    - One **average rotation** (`T_rotation`) to wait for the _first_ block of the file to spin under the head (e.g., 4ms).
        
2. **Streaming the File (The Work):**
    
    - _Once the head is in place and the first sector is under it_, the platter just keeps spinning.
        
    - The head doesn't move. It just sits there and reads all the data _on that track_ in one continuous stream as it flies by.
        
    - It reads Block 0, Block 1, Block 2, Block 3... all in a row. There are **no new seeks** and **no new rotational delays** _as long as you are on the same track_.
        

### The Deeper Answer: "But what about the _next_ track?"

This is the real heart of your question. A 100MB file is _definitely_ not on one track. It spans _hundreds_ of tracks. So, when we finish reading `Track 100` and need to move to `Track 101`, don't we have to pay `T_seek` and `T_rotation` all over again?

**This is the magic:** No, we don't. Or rather, the cost is _so tiny_ it's considered negligible.

This is because two brilliant hardware tricks come into play:

1. **Track-to-Track Seek:** The "average seek" (9ms) is the time it takes to move the head (on average) `1/3` of the way across the _entire disk_. But the seek from one track to the _next adjacent track_ (from Track 100 to Track 101) is a **minimal seek**. This is _incredibly_ fast, often **less than 1 millisecond**.
    
2. **Track Skew (From Your Slides):** The disk engineers _know_ this track-to-track seek will happen. So, they _plan_ for it. As your slide on Track Skew showed, the start of the next track (`Track 101, Sector 0`) is _not_ physically aligned with the start of the previous one (`Track 100, Sector 0`). It's "skewed" (offset) by just the right amount, so that:
    
    - You finish reading the last sector of `Track 100`.
        
    - You perform the tiny `~1ms` track-to-track seek to `Track 101`.
        
    - By the time the head arrives and settles, the _first sector_ of `Track 101` is _just about_ to spin under it.
        

**The result:** The rotational delay for _every subsequent track_ is **almost zero**.

### Back to the Math

This is why the formula for sequential I/O is so different from random I/O:

- **Random I/O:** `T_I/O` ≈ `(T_seek + T_rotation) * N`
    
    - To read `N` random blocks, you pay the _full penalty_ `N` times.
        
    - `Seek ... Wait ... Read ... Seek ... Wait ... Read ...`
        
- **Sequential I/O:** `T_I/O` ≈ `(T_seek + T_rotation) + T_transfer`
    
    - You pay the _full penalty_ only **once**, at the very beginning.
        
    - The `T_transfer` term (e.g., `950ms` in your example) is so _massive_ that it completely "hides" or "amortizes" the cost of those tiny, sub-millisecond track-to-track seeks.
        
    - That `950ms` _is_ the total time spent streaming bits, including the tiny gaps for switching tracks.
        

