# Determining Physical Memory Size

**Tags:** #memory #address_bus #computer_architecture

The maximum amount of primary memory a microprocessor can access is not an arbitrary number; it is a direct function of the width of its **address bus**.

### The Calculation

The address bus is used to uniquely identify each location in memory. If a processor has an address bus with **N** bits (or N parallel lines), it can generate `2^N` unique binary combinations. Each of these combinations can point to a distinct memory location.

For the Intel 8086:

- Address Bus Width (N) = 20 bits
    
- Total Addressable Locations = `2^20` = 1,048,576 locations
    

### From Locations to Bytes

The total memory size also depends on how much data is stored at each unique location. In the memory architecture used by the 8086 (and most modern computers), each addressable location holds **one byte (8 bits)** of data.

Therefore, the total physical memory size is:

```
Total Memory = (Number of Locations) * (Data per Location)
Total Memory = 2^20 locations * 1 byte/location
Total Memory = 1,048,576 bytes = 1 Megabyte (MB)
```

It's important to separate these two concepts:

1. **Number of Locations:** Determined solely by the **address bus width**.
    
2. **Data Transfer Rate:** Determined by the **data bus width**. The 8086 can access two 8-bit locations simultaneously to fill its 16-bit data bus.
    

If each memory location were capable of holding 2 bytes, a 20-bit address bus would be able to access 2MB of memory. However, the byte-addressable standard is fundamental to modern computer architecture.

**Links:** [[The Mismatch Problem - Bus Width vs Register Size]]