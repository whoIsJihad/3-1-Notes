# The Memory API: Heap Management

**Tags:** #os #memory-management #heap #malloc #system-calls

While the OS provides the virtual address space, user-level programs typically interact with memory through a standardized API, most commonly the C library's heap allocation functions. These functions manage a large, contiguous area of the virtual address space known as the heap.

### Core Heap API Calls

- **`void* malloc(size_t size)`**: The workhorse of dynamic allocation. It allocates a contiguous block of memory of at least `size` bytes on the heap. The memory is **not initialized**; it contains whatever garbage data was there before. It returns a `void*` pointer to the start of the allocated block, or `NULL` on failure.
    
    ```
    // Allocate space for 10 integers
    int *arr = (int *)malloc(10 * sizeof(int));
    if (arr == NULL) {
        // Handle allocation failure
        perror("malloc failed");
        exit(EXIT_FAILURE);
    }
    ```
    
- **`void free(void *ptr)`**: Deallocates a block of memory previously allocated by `malloc`, `calloc`, or `realloc`. The pointer `ptr` must be one that was returned by these functions. Freeing a `NULL` pointer is a safe, no-op. Freeing memory that has already been freed (**double free**) or an invalid pointer leads to undefined behavior.
    
- **`void* calloc(size_t num, size_t size)`**: Allocates memory for an array of `num` elements, each `size` bytes long. The key difference from `malloc` is that the allocated memory is **zero-initialized**.
    
- **`void* realloc(void *ptr, size_t new_size)`**: Resizes a previously allocated memory block pointed to by `ptr`. It may return the same pointer (if the block can be expanded in place) or a new pointer to a different location (if the data had to be moved).
    

### Common Programming Errors with Heap Memory

1. **Memory Leak**: Forgetting to `free()` memory that is no longer needed. The program's memory footprint will grow over time, potentially exhausting available memory.
    
    ```
    void memory_leak_example() {
        while (1) {
            // This memory is allocated in a loop but never freed
            int *data = (int *)malloc(sizeof(int));
        }
    }
    ```
    
2. **Dangling Pointer**: A pointer that references a memory location that has already been freed. Accessing a dangling pointer leads to undefined behavior.
    
    ```
    int *a = (int *)malloc(sizeof(int));
    *a = 10;
    int *b = a; // Both a and b point to the same memory
    free(a);
    // 'b' is now a dangling pointer. The next line is an error.
    // *b = 20;
    ```
    
3. **Double Free**: Calling `free()` twice on the same pointer. This can corrupt the heap's internal data structures.
    
4. **Buffer Overflow**: Writing past the end of an allocated buffer. This can corrupt adjacent data on the heap.
    
    ```
    char *src = "hello"; // 6 bytes with '\0'
    // Allocating too little memory (missing the +1 for the null terminator)
    char *dst = (char *)malloc(strlen(src));
    strcpy(dst, src); // This writes 6 bytes into a 5-byte buffer, an overflow.
    ```
    

### The Underlying System Calls

The C library's `malloc` implementation is a user-level memory manager. When it needs more memory from the OS to satisfy allocation requests, it uses system calls to expand the heap segment.

- **`brk()` and `sbrk()`**: These are the traditional system calls for managing the heap. The `brk` call sets the "program break"—the end of the heap segment—to a new location. `sbrk` increments the program break by a specified amount. `malloc` will call `sbrk` to request large chunks of memory from the kernel, which it then manages and carves up for smaller user requests.
    
- **`mmap()` and `munmap()`**: For very large allocations, modern `malloc` implementations often bypass the heap entirely and use `mmap` to create a new, separate memory region. This is more efficient than extending the heap by a huge amount and can prevent heap fragmentation. `mmap` can create an **anonymous region** (not backed by a file) that serves as private memory for the process.
    

```
#include <sys/mman.h>

// Request a 4KB anonymous memory region
void *region = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

if (region == MAP_FAILED) {
    perror("mmap failed");
}

// Later...
munmap(region, 4096); // Free the region
```