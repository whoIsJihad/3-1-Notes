# The Optimal (OPT) Replacement Policy

**Tags:** #os #memory-management #page-replacement #algorithms

The **Optimal Replacement Policy**, sometimes called OPT or MIN, provides the theoretical best-case performance for page replacement.

**The Policy:** When a page must be evicted, replace the page that will be accessed **furthest in the future**.

### How It Works

This algorithm requires the OS to have perfect knowledge of the future—it must know the entire sequence of upcoming memory references for a process. When an eviction is needed, it examines all pages currently in the cache and chooses the one whose next access is the most distant in the future.

#### Example Trace

Consider a cache with 3 slots and the following reference string: `0, 1, 2, 0, 1, 3, 0, 3, 1, 2, 1`

|Access|Hit/Miss|Evict|Cache State|Comment|
|---|---|---|---|---|
|**0**|Miss||`0`||
|**1**|Miss||`0, 1`||
|**2**|Miss||`0, 1, 2`|Cache is full.|
|**0**|Hit||`0, 1, 2`||
|**1**|Hit||`0, 1, 2`||
|**3**|Miss|`2`|`0, 1, 3`|To bring in `3`, we look at `0, 1, 2`. The next `0` is soon. The next `1` is soon. The next `2` is furthest away. Evict `2`.|
|**0**|Hit||`0, 1, 3`||
|**3**|Hit||`0, 1, 3`||
|**1**|Hit||`0, 1, 3`||
|**2**|Miss|`3`|`0, 1, 2`|To bring in `2`, we look at `0, 1, 3`. The next `1` is soon. The next access to `0` and `3` is not in our string. Let's evict `3`.|
|**1**|Hit||`0, 1, 2`||

**Result:** 7 hits, 4 misses.

### Impracticality

The OPT policy is **unrealizable in practice** because an OS cannot predict the future access pattern of a program. Its primary value is as a theoretical benchmark. It allows OS developers to run simulations of other, practical algorithms against OPT to measure how close they come to perfection.