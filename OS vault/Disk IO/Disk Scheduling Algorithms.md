**Tags:** #os #storage #hdd #scheduling

# Disk Scheduling Algorithms

Since [[HDD I_O Time Calculation|seek time]] is a dominant factor in random I/O performance, the operating system can significantly improve throughput by intelligently ordering the queue of pending disk requests. This is known as disk scheduling.

Assume a request queue for cylinders: `98, 183, 37, 122, 14, 124, 65, 67` and the head starts at cylinder `53`.

### FCFS (First-Come, First-Served)

Services requests in the order they arrive. This is fair but highly inefficient, as it doesn't try to optimize head movement at all.

- **Path:** `53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67`
    
- **Total Seek:** 640 cylinders.
    

### SSTF (Shortest Seek Time First)

Selects the request that is closest to the current head position. This minimizes seek time but can lead to **starvation** for requests at the edges of the disk if a steady stream of requests arrives in the middle.

- **Path:** `53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183`
    
- **Total Seek:** 236 cylinders.
    

### SCAN (Elevator Algorithm)

The disk arm moves from one end of the disk to the other, servicing all requests in its path. When it reaches the end, it reverses direction. This is better than SSTF at avoiding starvation.

- **Path (moving towards 0 first):** `53 → 37 → 14 → 0 → 65 → 67 → 98 → 122 → 124 → 183`
    
- **Total Seek:** 208 cylinders (assuming travel to end).
    

### C-SCAN (Circular SCAN)

Similar to SCAN, but on the return trip, the head moves all the way back to the beginning without servicing any requests. This provides a more uniform wait time, as requests at the end of the disk don't have to wait for the arm to service requests in both directions.

- **Path (moving towards 199):** `53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37`
    

### LOOK / C-LOOK

These are optimized versions of SCAN and C-SCAN. Instead of traveling to the very end of the disk, the arm reverses direction as soon as it services the last request in its current direction. This is the most common practical implementation.

- **C-LOOK Path:** `53 → 65 → ... → 183 (last req) → 14 (first req) → ... → 37`
    

**Links:** [[Hard Disk Drives MOC]], [[HDD I_O Time Calculation]]