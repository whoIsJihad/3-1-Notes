

### 1. The On-Disk Blueprint: How a Filesystem is Organized

Before a single byte of a user's file can be stored, the filesystem must impose a strict, logical structure onto the raw, unstructured disk. The first step is to partition the disk into fixed-size **blocks** (e.g., 4 KB), which become the minimum unit for all read and write operations. These blocks are then organized into distinct regions, each with a specific purpose.

- **The Data Region (D):** This is the largest and most straightforward part of the filesystem. It's a vast pool of data blocks where the actual contents of your files—the bytes that make up your C++ code, your photos, your documents—are stored.
    
- **The Inode Table (I):** A file is more than just its data; it has metadata (owner, permissions, size, creation time, etc.). This metadata is stored in a structure called an **inode** (index node). The inode table is a pre-allocated, contiguous set of blocks on the disk that acts as a fixed-size array for _all_ the inodes in the filesystem.
    
    - **A Critical Limitation:** The size of this table defines the maximum number of files the filesystem can ever hold, regardless of how much free data space there is.
        
    - **Example from the slide:** If an inode is 256 bytes and a block is 4 KB (4096 bytes), then one block can hold `4096 / 256 = 16` inodes. If we reserve 5 blocks for the inode table, the filesystem's absolute maximum file count is `5 * 16 = 80` files.
        
- **Allocation Structures (Bitmaps - i & d):** The filesystem needs to efficiently track which inodes and data blocks are free and which are in use. A **bitmap** is the perfect tool for this. It's a simple, compact structure where each bit corresponds to a block or an inode.
    
    - **inode bitmap (`i`):** A block of bits where the Nth bit is 1 if inode N is in use, and 0 if it's free. To create a new file, the filesystem scans this bitmap for the first 0, flips it to 1, and allocates the corresponding inode.
        
    - **data bitmap (`d`):** Similarly, this block of bits tracks the status of every block in the Data Region. To write new data, the filesystem scans this bitmap for a 0, flips it to 1, and allocates that data block.
        
- **The Super Block (S):** This is the most critical block in the entire filesystem. It is typically the very first block and contains the master information about the filesystem's layout. It stores values such as:
    
    - The total number of blocks in the filesystem.
        
    - The total number of inodes.
        
    - The starting block number of the inode table.
        
    - The starting block numbers for the bitmaps.
        
        When you mount a filesystem (e.g., plug in a USB drive), the operating system's first action is to read the Super Block. If the Super Block is corrupted, the filesystem is unreadable because the OS has no map to interpret the rest of the data.
        

### 2. The Inode: The Heart of a File

The inode is the central data structure that links everything together. It contains all metadata _except_ the filename (which is stored in the directory).

- Finding an Inode: Since the Inode Table is a simple, contiguous array, locating any inode on disk is a fast and deterministic calculation. The OS can find the address of any inode using this formula:
    
    address = table_start_address + (inode_number * sizeof(inode))
    
    This allows the OS to read a file's metadata with a single, direct disk seek, without having to search for it.
    
- **Indexed Allocation: The Key to File Storage:** The most brilliant part of the inode's design is how it uses a small, fixed amount of space to manage files of any size. This mechanism is called **Indexed Allocation**.
    
    - **Direct Pointers:** The inode contains a small array (e.g., 12) of direct block pointers. Each of these pointers stores the address of a block in the Data Region. For small files (e.g., up to 12 * 4KB = 48KB), this is incredibly efficient. To read the entire file, the OS just reads the inode and immediately knows the location of all of its data blocks.
        
    - **Single Indirect Pointer:** When a file grows beyond what the direct pointers can handle, the filesystem uses the _single indirect pointer_. This pointer does **not** point to a data block. Instead, it points to an **index block**. This index block is nothing but a block full of more direct pointers. If a block address takes 4 bytes and a block is 4 KB, this single index block can hold `4096 / 4 = 1024` pointers, allowing the file to grow by an additional `1024 * 4KB = 4MB`.
        
    - **Double and Triple Indirect Pointers:** For truly massive files, the logic extends. A **double indirect pointer** points to a block full of _single indirect pointers_. A **triple indirect pointer** points to a block full of _double indirect pointers_. This multi-level, tree-like structure allows a tiny inode to manage files that can be terabytes in size, providing a scalable solution that remains efficient for the most common case: small files.
        

### 3. Filesystem Operations in Action: I/O Walkthroughs

The on-disk structures dictate the sequence of disk I/O operations required for any task. These detailed walkthroughs reveal why filesystem operations can be expensive.

**Walkthrough: Reading `/foo/bar`**

1. **Read Super Block:** To find the location of the root directory's inode (usually inode #2).
    
2. **Read Root Inode (`/`):** To find the pointers to its data blocks.
    
3. **Read Root Data Block:** To scan the list of directory entries.
    
4. **Scan and Find:** The OS searches this list for the name "foo" and retrieves its inode number.
    
5. **Read `foo`'s Inode:** To find the pointers to _its_ data blocks.
    
6. **Read `foo`'s Data Block:** To scan _its_ list of directory entries.
    
7. **Scan and Find:** The OS searches this list for the name "bar" and retrieves its inode number.
    
8. **Read `bar`'s Inode:** The `open("/foo/bar")` call is now complete. The OS has the file's metadata.
    
9. **Read Data:** Subsequent `read()` calls will use the direct/indirect pointers within `bar`'s inode to finally fetch the file's actual content from the Data Region.
    

Walkthrough: Creating /foo/bar

This is even more I/O intensive because it involves modifications.

1. **Path Traversal (Steps 1-7 above):** First, the OS must read all the way down to the `foo` directory to ensure it exists and to prepare to modify it.
    
2. **Allocate an Inode for `bar`:**
    
    - Read the **inode bitmap** from disk.
        
    - Find the first `0` bit, flip it to `1`.
        
    - Write the modified **inode bitmap** back to disk. (1 read, 1 write)
        
3. **Initialize the Inode:**
    
    - Write a new, initialized inode (with size 0, owner info, etc.) into the corresponding slot in the Inode Table. (1 write)
        
4. **Add to Parent Directory:**
    
    - Add a new entry (`<"bar", new_inode_number>`) into the data block of the `foo` directory.
        
    - Write the modified `foo` **data block** back to disk. (1 write)
        

This simple creation operation can easily require 8-10 separate disk I/Os.

### 4. Performance Optimization: Caching

The sheer number of disk I/Os would make any filesystem unusably slow. The solution is aggressive caching in RAM.

- **The Buffer Cache (Historical Approach):** A fixed region of RAM was dedicated to storing recently accessed disk blocks. If the OS needed to read the root inode, it would first check the buffer cache. If it was there (a "cache hit"), it avoided a slow disk read. This was effective but statically partitioned RAM, which is inefficient.
    
- **The Page Cache (Modern Unified Approach):** Modern operating systems like Linux use a superior, dynamic approach. The **Page Cache** unifies the virtual memory system with the file buffer cache. There is a single pool of page frames in RAM. A frame can be used to store a process's memory (e.g., from the heap) or it can be used to cache a file block. The OS dynamically allocates these frames based on system workload, ensuring that RAM is always used for the most pressing need, whether that's running programs or caching I/O. This is a much more efficient use of system resources.