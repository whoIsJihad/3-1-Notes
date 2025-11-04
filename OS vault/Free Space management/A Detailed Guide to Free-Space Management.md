

Welcome! This guide will walk you through the essential concepts of free-space management, explaining everything from your presentation ("17._FreeSpace_Management.pptx") step-by-step. This topic is fundamental to understanding how programs like `malloc` and `free` actually work under the hood in an operating system.

Let's dive in.

### 1. The Big Picture: Managing The Heap (Slide 3)

When your C program runs, its memory is typically divided into several segments:

- **Code (Text):** Your compiled program instructions.
    
- **Data:** Global and static variables.
    
- **Stack:** Used for local variables, function parameters, and return addresses. It grows and shrinks automatically as you call and return from functions.
    
- **Heap:** This is the region of "free" memory available for _dynamic allocation_. When you call `malloc()`, you are requesting a chunk of memory from the heap. When you call `free()`, you are returning it.
    

**Free-Space Management** is the job of the _memory allocator_ (like the one in the C standard library, `libc`) to manage the heap. Its goal is to satisfy `malloc()` requests efficiently while minimizing wasted space.

### 2. The Core Operations: Splitting and Coalescing

The allocator needs two primary operations to manage the free chunks of memory.

#### Splitting (Slides 4-5)

**What it is:** Imagine you have a 30-byte heap with two 10-byte free chunks (at addresses 0 and 20). The rest (address 10-19) is already in use.

```
[ free (10B) ][  used (10B) ][ free (10B) ]
 0           10           20           30
```

Your "free list" (a list of all free chunks) would look like: `(addr:0, len:10) -> (addr:20, len:10)`.

Now, a user requests 1 byte: `malloc(1)`.

The allocator can't just give 1 byte. It finds a free chunk that's big enough (e.g., the one at address 20). It would be incredibly wasteful to mark the _entire_ 10-byte chunk as "used" just for a 1-byte request.

Instead, the allocator **splits** the free chunk:

1. It carves out 1 byte for the user (at address 20).
    
2. It creates a _new_, smaller free chunk with the remainder (9 bytes, starting at address 21).
    

The new memory layout is:

```
[ free (10B) ][  used (10B) ][used(1B)][ free (9B) ]
 0           10           20          21           30
```

The free list is updated to: `(addr:0, len:10) -> (addr:21, len:9)`.

**In short: Splitting finds a free chunk larger than the request and divides it into two: one allocated chunk and one smaller free chunk.**

#### Coalescing (Slide 6)

**What it is:** Coalescing is the _opposite_ of splitting. It's the process of merging adjacent free chunks into a single, larger free chunk.

**Why we need it:** Let's say our heap is back to its original state (two 10B free chunks) and the user frees the 10-byte "used" chunk in the middle.

Without coalescing, our free list would become: `head -> (addr:0, len:10) -> (addr:20, len:10) -> (addr:10, len:10) -> NULL`

Now our heap is _entirely free_, but it's fragmented into three 10-byte chunks. If the user now requests 25 bytes (`malloc(25)`), the request will **fail!** Even though we have 30 bytes of total free memory, we don't have a _contiguous_ 25-byte chunk.

This is where coalescing saves the day. When `free(ptr)` is called, the allocator checks if the chunks immediately _before_ or _after_ the newly freed chunk are _also_ free. If they are, it merges them.

In our example, when the chunk at address 10 is freed, the allocator sees that the chunk at address 0 is free _and_ the chunk at address 20 is free. It coalesces all three, creating a single, 30-byte free chunk.

The free list becomes: `head -> (addr:0, len:30) -> NULL`

Now, a `malloc(25)` request will succeed.

**In short: Coalescing merges adjacent free blocks when one is freed, preventing fragmentation and allowing large requests to be satisfied.**

### 3. Implementation: How `free()` Knows the Size (Slides 7-10)

This is a classic OS puzzle: The `free(void *ptr)` function _only_ takes a pointer. It doesn't take a size. How does it know how many bytes to free?

**The solution is a "Header Block".**

When you call `malloc(20)`, the allocator doesn't just find 20 bytes. It finds, for example, 28 bytes. It uses the first 8 bytes for its own secret bookkeeping in a structure called a "header". It then returns a pointer to you that _starts after the header_.

- **You call:** `ptr = malloc(20);`
    
- **The allocator actually does:**
    
    1. Finds a free chunk of at least `20 + sizeof(header_t)` bytes.
        
    2. Writes data into the header (e.g., at address `hptr`).
        
    3. **Returns `ptr` to you, where `ptr = hptr + sizeof(header_t)`.**
        

As seen on slide 9, this header contains crucial information:

```
typedef struct __header_t { 
    int size;    // The size of the chunk *you* requested (e.g., 20)
    int magic;   // A special number (e.g., 1234567)
} header_t;
```

- `size`: This is the answer! The header stores the size of the allocated region.
    
- `magic`: This is a sanity check. When you call `free()`, the allocator can check this number. If it's not `1234567`, it's a good sign you're freeing something you shouldn't be (e.g., memory on the stack, or memory that's already been freed). This helps catch "double free" bugs.
    

Now, when you call `free(ptr)`, the library performs a little pointer magic (Slide 10):

```
void free(void *ptr) { 
   // 1. Calculate the address of the header
   header_t *hptr = (void *)ptr - sizeof(header_t);

   // 2. Check the magic number for safety
   assert(hptr->magic == 1234567); 
   
   // 3. Now it knows the size!
   int size_to_free = hptr->size; 
   
   // 4. (and the total chunk size is size_to_free + sizeof(header_t))
   // ... now add this chunk back to the free list and coalesce ...
}
```

### 4. Managing the Free List Data Structure (Slides 11-19)

So, how do we keep track of all the free chunks? We use a **linked list**.

But where do we store the nodes of this linked list? We don't want to call `malloc()` to store them—that's what we're trying to write!

**The solution: An "Embedded List".** The free chunks _themselves_ are used to store the linked list nodes. A free chunk doesn't need a magic number; it needs a pointer to the _next_ free chunk.

So, we have two "views" of a piece of memory:

1. **When Allocated:** It has a `(size, magic)` header.
    
2. **When Free:** It has a `(size, next_pointer)` header.
    

```
// A node in the *free* list (Slide 11)
typedef struct __node_t { 
    int size;                // Size of this *free* chunk
    struct __node_t *next;   // Pointer to the next free chunk
} node_t;
```

#### Walkthrough: Allocation & Freeing (Slides 12-17)

1. **Initialization (Slide 12):** The heap starts empty. The allocator asks the OS for a big chunk of memory (e.g., 4096 bytes using `mmap()`). It initializes this as _one big free node_.
    
    - `head = mmap(...)`
        
    - `head->size = 4096 - sizeof(node_t);`
        
    - `head->next = NULL;`
        
    - The free list is just: `head -> (addr:16KB, size:4088) -> NULL`
        
2. **First Allocation (Slide 13):** A user calls `ptr = malloc(100)`.
    
    - The allocator needs `100 + sizeof(header_t)` (the _allocated_ header), which is `100 + 8 = 108` bytes.
        
    - It finds the big 4088-byte free chunk.
        
    - It **splits** this chunk.
        
    - It creates the _allocated chunk_ at the end of the block (this is just one strategy) and returns `ptr` to the user. This chunk gets the `(size: 100, magic: 1234567)` header.
        
    - It updates the original free chunk's size: `head->size = 4088 - 108 = 3980`.
        
    - The free list is now: `head -> (addr:16KB, size:3980) -> NULL`
        
3. **More Allocations (Slide 14):** Three 100-byte chunks are allocated (each 108 bytes total). The free list head node just keeps shrinking.
    
    - Free list is now: `head -> (addr:16KB, size: 3764) -> NULL`
        
4. **Freeing a Chunk (Slide 15):** The user calls `free(sptr)` on the _second_ allocated chunk.
    
    - `free()` finds the header for `sptr` and gets its size.
        
    - It converts this _allocated_ chunk back into a _free node_ (`node_t`).
        
    - It adds this new free node to the _front_ of the free list (a simple and fast way to add it).
        
    - `void* tmp = head;`
        
    - `head = sptr;` (Note: `sptr` is the user pointer, the code really means the `node_t*` version)
        
    - `head->next = tmp;`
        
    - The free list is now: `head -> (new_free_chunk, size:100) -> (original_chunk, size:3764) -> NULL`
        
5. **More Freeing (Slides 16-17):** The other two chunks are freed. Each one is added to the front of the list.
    
    - The free list becomes a fragmented mess: `head -> (chunk3, 100B) -> (chunk1, 100B) -> (chunk2, 100B) -> (original, 3764B) -> NULL`
        
    - **This is precisely why a simple "add to front" `free()` implementation must be paired with a good coalescing strategy!**
        

#### Growing the Heap (Slide 19)

What if the free list is empty or has no chunks big enough? The allocator calls a system call like `sbrk()` to ask the OS to extend the "break"—the end of the heap. This gives the allocator more raw memory from the OS, which it can then add to its free list as a new, large chunk.

### 5. Basic Allocation Strategies (Policies) (Slides 20-22)

When `malloc()` is called, and there are _multiple_ free chunks big enough, which one should it pick? This policy has a huge impact on performance and fragmentation.

- **Best Fit:**
    
    - **How:** Search the _entire_ free list and find the _smallest_ free chunk that is _just big enough_ (or larger) for the request.
        
    - **Pro:** Leaves the smallest possible leftover fragment (e.g., `malloc(10)` in a 12-byte chunk leaves a 2-byte fragment, not a 90-byte fragment from a 100-byte chunk).
        
    - **Con:** Slow. Must search the whole list every time.
        
- **Worst Fit:**
    
    - **How:** Search the _entire_ free list and find the _largest_ free chunk.
        
    - **Pro:** Leaves the largest possible leftover fragment, which might be useful for a future large request.
        
    - **Con:** Slow (must search whole list). Tends to quickly "pollute" the heap by breaking up all the large chunks, making future large requests fail.
        
- **First Fit:**
    
    - **How:** Search the list from the `head` and pick the _first_ chunk you find that is big enough.
        
    - **Pro:** Very fast.
        
    - **Con:** Can lead to a lot of small, fragmented chunks clustering at the beginning of the list, which slows down future searches.
        
- **Next Fit:**
    
    - **How:** Just like First Fit, but you keep a "rover" pointer to where you last left off. The next search starts from there.
        
    - **Pro:** Spreads the allocations more evenly across the list instead of clustering them at the front. Still fast.
        
    - **Con:** Can have surprisingly bad fragmentation behavior in some cases.
        

### 6. Advanced Allocation Algorithms

The simple strategies above have problems. Modern allocators use more sophisticated techniques.

#### Segregated Lists (e.g., McKusick-Karels Allocator) (Slides 23-24)

Instead of _one_ big list, why not have _many_ lists, one for each popular size?

- **Core Idea:** Create an array of free lists, "segregated" by size class.
    
    - `Freelistarr[0]` = list of all 32-byte free chunks
        
    - `Freelistarr[1]` = list of all 64-byte free chunks
        
    - `Freelistarr[2]` = list of all 128-byte free chunks
        
    - ...and so on.
        
- **`malloc(60)`:**
    
    1. Round the request up to the nearest size class (e.g., 64 bytes).
        
    2. Go directly to `Freelistarr[1]` (the 64-byte list).
        
    3. Pop the first chunk off that list and return it.
        
- **This is** _**extremely**_ **fast.** No searching, no splitting.
    
- **What if the list is empty?** The allocator gets a larger chunk of memory (e.g., a 2KB page from the OS), splits it into many 64-byte chunks, and adds them all to the `Freelistarr[1]`.
    
- **Pro:** Very fast allocations and frees for common, small sizes.
    
- **Con:** Can suffer from **internal fragmentation**. A `malloc(33)` request gets a 64-byte chunk, wasting 31 bytes _inside_ the allocated block.
    

#### Buddy System (Slides 25-31)

This is a clever algorithm used by the Linux kernel to manage physical memory pages.

- **Core Idea:** All memory blocks are powers of two (32B, 64B, 128B, ..., 1024B, etc.).
    
- **Allocation (e.g., `Allocate(256)` in a 1024B block):**
    
    1. Start with a 1024B block. It's too big.
        
    2. **Split** it into two 512B "buddies" (A and A'). Add A' to the 512B free list.
        
    3. Take block A (512B). It's too big.
        
    4. **Split** A into two 256B "buddies" (B and B'). Add B' to the 256B free list.
        
    5. Return block B (256B) to the user.
        
- **Freeing (Coalescing):** This is the magic part.
    
    - When a block (e.g., D, 64B) is freed, the allocator _instantly_ knows the address of its buddy (D').
        
    - It checks if D' is _also_ free (e.g., by checking a bitmap, as in slide 27).
        
    - **If buddy is NOT free:** Just add D to the 64B free list.
        
    - **If buddy IS free:** **Coalesce** D and D' into a 128B block (C'). Now, _recursively_ check the buddy of C'. Is C also free? Yes! Coalesce C and C' into a 256B block (B'). Check B''s buddy... and so on, merging all the way up the tree.
        
- **Pro:** Coalescing is _extremely_ fast and efficient. Finding a buddy is a simple bitwise (XOR) address calculation.
    
- **Con:** Suffers from **internal fragmentation** (a 33-byte request gets a 64-byte block).
    

#### Slab Allocator (Slides 32-33)

This is a brilliant optimization, also used heavily in the kernel.

- **Context:** The kernel creates and destroys _thousands_ of identical, complex objects (like `inode` structs, process descriptors, sockets).
    
- **The Problem:** `malloc()` gives you raw, uninitialized memory. When you get a chunk for an `inode`, you then have to _initialize_ it (set default values, acquire locks, etc.). When you `free()` it, you have to _deconstruct_ it. This construction/deconstruction is pure overhead if you're just going to ask for another `inode` 5ms later.
    
- **Slab Solution:**
    
    1. Create a "cache" for each object type (e.g., an `inode_cache`).
        
    2. A cache consists of one or more "slabs".
        
    3. A "slab" is a chunk of memory (one or more pages) that is pre-formatted with _many pre-initialized objects_.
        
- **`Allocate(inode)`:**
    
    1. Go to the `inode_cache`.
        
    2. Find a slab with a free object.
        
    3. Return a pointer to that _already-initialized_ object.
        
- **`Free(inode)`:**
    
    1. Return the object to its slab.
        
    2. **It is NOT deconstructed.** It just sits there, ready to be re-used, in its initialized state.
        
- **Pro:** Eliminates initialization/deconstruction overhead. It's incredibly fast and also completely avoids internal fragmentation (since the objects are packed perfectly).
    

### 7. Summary: Who Uses What? (Slide 33)

You'll find these allocators in different places:

- **User-space `malloc` (`libc`):** Often uses **Segregated Lists** with other optimizations. It's built for general-purpose, fast allocation of various sizes.
    
- **Kernel (managing physical pages):** The Linux kernel uses the **Buddy System** to manage physical memory pages, as pages are naturally power-of-two sized.
    
- **Kernel (managing its own objects):** The kernel builds the **Slab Allocator** _on top of_ the Buddy System. It requests pages from the Buddy System to create slabs for its internal objects.
    

### Sources

- **Primary Source:** Your presentation, "17._FreeSpace_Management.pptx".
    
- **Canonical Textbook:** The concepts and examples (especially the header/magic number and splitting/coalescing) are classic material covered in depth in the textbook **"Operating Systems: Three Easy Pieces"** by Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau. The chapters on "Free-Space Management" are a fantastic resource for this.
    

