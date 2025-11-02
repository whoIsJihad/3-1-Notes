**Tags:** #os #storage #hdd #performance #optimization

# HDD Performance Optimizations

Disk manufacturers and operating systems use several techniques to improve the performance of Hard Disk Drives (HDDs) beyond their basic mechanical limits.

### Track Skew

When reading data sequentially that crosses a track boundary, the head must move from one track to the next. This takes a small amount of time. If the sectors were laid out starting at the same angle on every track, the disk would have already spun past the desired next sector (e.g., sector 0) by the time the head switch was complete.

**Track skew** introduces an offset to the starting position of sectors on each subsequent track. This ensures that by the time the head moves to the next track, the next logical block is just arriving under the head, allowing for seamless sequential reads across tracks.

### Multi-Zoned Recording

Due to geometry, outer tracks are longer and can physically hold more sectors than inner tracks. Early drives used a single number of sectors per track, wasting space on the outer edges.

**Zoned Bit Recording** groups tracks into zones. All tracks within a zone have the same number of sectors. Outer zones have more sectors per track than inner zones. This increases the overall capacity and transfer rate of the drive, as more data can be read per rotation on the outer tracks.

### Caching (Track Buffer)

Modern drives include a small amount of DRAM (e.g., 16-64 MB) on the drive itself, which acts as a cache.

- **Read-ahead:** When a block is requested, the drive might speculatively read subsequent blocks on the same track into the cache, assuming a sequential read is likely.
    
- **Write Caching:**
    
    - **Write-through:** Acknowledges a write only after the data is physically written to the platter. This is safer but slower.
        
    - **Write-back (or write-behind):** Acknowledges a write as soon as the data is placed in the on-drive cache. This is much faster for the OS, but risks data loss if power fails before the data is flushed from the cache to the platter.
        

**Links:** [[Hard Disk Drives MOC]], [[HDD I_O Time Calculation]]