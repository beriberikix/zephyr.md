---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/memory_management/shared_multi_heap.html
original_path: kernel/memory_management/shared_multi_heap.html
---

# Shared Multi Heap

The shared multi-heap memory pool manager uses the multi-heap allocator to
manage a set of reserved memory regions with different capabilities /
attributes (cacheable, non-cacheable, etc…).

All the different regions can be added at run-time to the shared multi-heap
pool providing an opaque “attribute” value (an integer or enum value) that can
be used by drivers or applications to request memory with certain capabilities.

This framework is commonly used as follow:

1. At boot time some platform code initialize the shared multi-heap framework
   using [`shared_multi_heap_pool_init()`](../../doxygen/html/group__shared__multi__heap.md#ga5b7f09666e3eac051b4c4942572f9ca3) and add the memory regions to
   the pool with [`shared_multi_heap_add()`](../../doxygen/html/group__shared__multi__heap.md#ga086362a2a8fce827a246039ef8757cc5), possibly gathering the
   needed information for the regions from the DT.
2. Each memory region encoded in a [`shared_multi_heap_region`](../../doxygen/html/structshared__multi__heap__region.md)
   structure. This structure is also carrying an opaque and user-defined
   integer value that is used to define the region capabilities (for example:
   cacheability, cpu affinity, etc…)

```c
// Init the shared multi-heap pool
shared_multi_heap_pool_init()

// Fill the struct with the data for cacheable memory
struct shared_multi_heap_region cacheable_r0 = {
     .addr = addr_r0,
     .size = size_r0,
     .attr = SMH_REG_ATTR_CACHEABLE,
};

// Add the region to the pool
shared_multi_heap_add(&cacheable_r0, NULL);

// Add another cacheable region
struct shared_multi_heap_region cacheable_r1 = {
     .addr = addr_r1,
     .size = size_r1,
     .attr = SMH_REG_ATTR_CACHEABLE,
};

shared_multi_heap_add(&cacheable_r0, NULL);

// Add a non-cacheable region
struct shared_multi_heap_region non_cacheable_r2 = {
     .addr = addr_r2,
     .size = size_r2,
     .attr = SMH_REG_ATTR_NON_CACHEABLE,
};

shared_multi_heap_add(&non_cacheable_r2, NULL);
```

3. When a driver or application needs some dynamic memory with a certain
   capability, it can use [`shared_multi_heap_alloc()`](../../doxygen/html/group__shared__multi__heap.md#ga8cd3d321f5ae516cd55812d304289971) (or the aligned
   version) to request the memory by using the opaque parameter to select the
   correct set of attributes for the needed memory. The framework will take
   care of selecting the correct heap (thus memory region) to carve memory
   from, based on the opaque parameter and the runtime state of the heaps
   (available memory, heap state, etc…)

```c
// Allocate 4K from cacheable memory
shared_multi_heap_alloc(SMH_REG_ATTR_CACHEABLE, 0x1000);

// Allocate 4K from non-cacheable memory
shared_multi_heap_alloc(SMH_REG_ATTR_NON_CACHEABLE, 0x1000);
```

## Adding new attributes

The API does not enforce any attributes, but at least it defines the two most
common ones: [`SMH_REG_ATTR_CACHEABLE`](../../doxygen/html/group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4afb2e0bb04859ff231dee953279b8bf3a) and [`SMH_REG_ATTR_NON_CACHEABLE`](../../doxygen/html/group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a2625b9b8aea429ab748f9e39d55f0dff).

[Shared multi-heap interface](../../doxygen/html/group__shared__multi__heap.md)
