# Approximating LRU: The Clock Algorithm

**Tags:** #os #memory-management #page-replacement #algorithms #lru #clock-algorithm

Perfect [[Using History: The LRU Policy|LRU]] is too slow to implement in software because it requires action on every memory access. To solve this, operating systems use hardware support to get an approximation of LRU. The most common approach is the **Clock Algorithm**.

### Hardware Support: The Use Bit

The Clock algorithm requires a single bit of hardware support for each page: the **use bit** (or accessed bit).

- This bit is associated with each Page Table Entry (PTE).
    
- **Whenever a page is referenced** (read from or written to), the **hardware automatically sets the use bit to 1**.
    
- The hardware _never_ clears this bit. That is the OS's job.
    

This bit gives the OS a simple piece of information: has this page been used _recently_? "Recently" in this context means "since the last time the OS cleared its use bit."

### The Clock Algorithm

The algorithm visualizes all physical pages arranged in a circular list, like the face of a clock. A "clock hand" points to one of the pages.

**The Policy:** When a page fault occurs, the OS searches for a page to evict by sweeping the clock hand. It looks for a page whose use bit is `0`.

**The Algorithm:**

1. When a replacement is needed, the OS looks at the page the clock hand is currently pointing to.
    
2. It checks that page's use bit.
    
    - **If the use bit is 1**: This means the page has been recently used. The OS doesn't want to evict it. Instead, it **clears the use bit to 0** and **advances the clock hand** to the next page. This gives the page a "second chance."
        
    - **If the use bit is 0**: This means the page has _not_ been used since the last time the clock hand swept over it. It is a good candidate for eviction. The OS selects this page as the victim, replaces it, and then advances the clock hand.
        

This algorithm is a good approximation of LRU because pages that are frequently used will have their use bit constantly set back to 1, and the clock hand will likely skip over them multiple times. Pages that are truly idle will have their use bit cleared to 0 on one sweep and will then be found as a `0` on the next sweep, making them candidates for eviction.