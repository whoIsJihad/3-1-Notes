**Tags:** #os #storage #hdd #performance

# HDD I/O Time Calculation

The total time to service a disk I/O request is the sum of three main components: seek time, rotational delay, and transfer time. Random I/O is dominated by seek and rotation, while sequential I/O is dominated by transfer time.

### The I/O Time Formula

The total time for a single I/O request can be calculated as follows:

```
T_I/O = T_seek + T_rotation + T_transfer
```

- **`T_seek` (Seek Time):** The time it takes for the disk arm to move the head to the correct track (cylinder). This involves acceleration, coasting, deceleration, and a settling period. Average seek times are typically in the 4-10 ms range.
    
- **`T_rotation` (Rotational Delay):** The time it takes for the desired sector to rotate under the disk head. On average, this is half the time of a full rotation.
    
- **`T_transfer` (Transfer Time):** The time it takes to read or write the data from the sector(s) once the head is in position. This depends on the rotation speed and the number of bytes being transferred.
    

### Example: Random vs. Sequential I/O

Let's compare the performance of two drives from the lecture.

|Specification|Cheetah 15K.5|Barracuda|
|---|---|---|
|RPM|15,000|7,200|
|Avg. Seek|4 ms|9 ms|
|Max Transfer|125 MB/s|105 MB/s|

**Random 4KB Read/Write:**

For a random I/O, the disk must perform a seek and wait for rotation for every small block.

- **Cheetah:** `4ms (seek) + 2ms (avg rotation) + 0.03ms (transfer) ≈ 6ms`. Rate: `4KB / 6ms ≈ 0.66 MB/s`.
    
- **Barracuda:** `9ms (seek) + 4ms (avg rotation) + 0.038ms (transfer) ≈ 13ms`. Rate: `4KB / 13ms ≈ 0.31 MB/s`.
    

**Sequential 100MB Read/Write:**

For a sequential I/O, the disk performs one seek and then transfers a large amount of data continuously.

- **Cheetah:** The transfer time dominates. Rate is close to the max transfer rate: `100MB / 800ms ≈ 125 MB/s`.
    
- **Barracuda:** The transfer time also dominates. Rate is close to the max transfer rate: `100MB / 950ms ≈ 105 MB/s`.
    

This shows that **random I/O is orders of magnitude slower than sequential I/O** on mechanical disks.

**Links:** [[Hard Disk Drives MOC]], [[Disk Scheduling Algorithms]]