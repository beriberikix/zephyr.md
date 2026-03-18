---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/memory_management/shared_multi_heap.html
original_path: kernel/memory_management/shared_multi_heap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Shared Multi Heap

The shared multi-heap memory pool manager uses the multi-heap allocator to
manage a set of reserved memory regions with different capabilities /
attributes (cacheable, non-cacheable, etc…).

All the different regions can be added at run-time to the shared multi-heap
pool providing an opaque “attribute” value (an integer or enum value) that can
be used by drivers or applications to request memory with certain capabilities.

This framework is commonly used as follow:

1. At boot time some platform code initialize the shared multi-heap framework
   using [`shared_multi_heap_pool_init()`](#c.shared_multi_heap_pool_init) and add the memory regions to
   the pool with [`shared_multi_heap_add()`](#c.shared_multi_heap_add), possibly gathering the
   needed information for the regions from the DT.
2. Each memory region encoded in a [`shared_multi_heap_region`](#c.shared_multi_heap_region)
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
   capability, it can use [`shared_multi_heap_alloc()`](#c.shared_multi_heap_alloc) (or the aligned
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
common ones: [`SMH_REG_ATTR_CACHEABLE`](#c.shared_multi_heap_attr.SMH_REG_ATTR_CACHEABLE) and [`SMH_REG_ATTR_NON_CACHEABLE`](#c.shared_multi_heap_attr.SMH_REG_ATTR_NON_CACHEABLE).

*group* Shared multi-heap interface
:   Shared Multi-Heap (SMH) interface.

    The shared multi-heap manager uses the multi-heap allocator to manage a set of memory regions with different capabilities / attributes (cacheable, non-cacheable, etc…).

    All the different regions can be added at run-time to the shared multi-heap pool providing an opaque “attribute” value (an integer or enum value) that can be used by drivers or applications to request memory with certain capabilities.

    This framework is commonly used as follow:

    - At boot time some platform code initialize the shared multi-heap framework using [shared\_multi\_heap\_pool\_init](#group__shared__multi__heap_1ga5b7f09666e3eac051b4c4942572f9ca3) and add the memory regions to the pool with [shared\_multi\_heap\_add](#group__shared__multi__heap_1ga086362a2a8fce827a246039ef8757cc5), possibly gathering the needed information for the regions from the DT.
    - Each memory region encoded in a [shared\_multi\_heap\_region](#structshared__multi__heap__region) structure. This structure is also carrying an opaque and user-defined integer value that is used to define the region capabilities (for example: cacheability, cpu affinity, etc…)
    - When a driver or application needs some dynamic memory with a certain capability, it can use [shared\_multi\_heap\_alloc](#group__shared__multi__heap_1ga8cd3d321f5ae516cd55812d304289971) (or the aligned version) to request the memory by using the opaque parameter to select the correct set of attributes for the needed memory. The framework will take care of selecting the correct heap (thus memory region) to carve memory from, based on the opaque parameter and the runtime state of the heaps (available memory, heap state, etc…)

    Defines

    MAX\_SHARED\_MULTI\_HEAP\_ATTR
    :   Maximum number of standard attributes.

    Enums

    enum shared\_multi\_heap\_attr
    :   SMH region attributes enumeration type.

        Enumeration type for some common memory region attributes.

        *Values:*

        enumerator SMH\_REG\_ATTR\_CACHEABLE
        :   cacheable

        enumerator SMH\_REG\_ATTR\_NON\_CACHEABLE
        :   non-cacheable

        enumerator SMH\_REG\_ATTR\_NUM
        :   must be the last item

    Functions

    int shared\_multi\_heap\_pool\_init(void)
    :   Init the pool.

        This must be the first function to be called to initialize the shared multi-heap pool. All the individual heaps must be added later with [shared\_multi\_heap\_add](#group__shared__multi__heap_1ga086362a2a8fce827a246039ef8757cc5).

        Note

        As for the generic multi-heap allocator the expectation is that this function will be called at soc- or board-level.

        Return values:
        :   - **0** – on success.
            - **-EALREADY** – when the pool was already inited.
            - **other** – errno codes

    void \*shared\_multi\_heap\_alloc(enum [shared\_multi\_heap\_attr](#c.shared_multi_heap_attr) attr, size\_t bytes)
    :   Allocate memory from the memory shared multi-heap pool.

        Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. The opaque attribute parameter is used by the backend to select the correct heap to allocate memory from.

        Parameters:
        :   - **attr** – capability / attribute requested for the memory block.
            - **bytes** – requested size of the allocation in bytes.

        Return values:
        :   - **ptr** – a valid pointer to heap memory.
            - **err** – NULL if no memory is available.

    void \*shared\_multi\_heap\_aligned\_alloc(enum [shared\_multi\_heap\_attr](#c.shared_multi_heap_attr) attr, size\_t align, size\_t bytes)
    :   Allocate aligned memory from the memory shared multi-heap pool.

        Allocates a block of memory of the specified size in bytes and with a specified capability / attribute. Takes an additional parameter specifying a power of two alignment in bytes.

        Parameters:
        :   - **attr** – capability / attribute requested for the memory block.
            - **align** – power of two alignment for the returned pointer, in bytes.
            - **bytes** – requested size of the allocation in bytes.

        Return values:
        :   - **ptr** – a valid pointer to heap memory.
            - **err** – NULL if no memory is available.

    void shared\_multi\_heap\_free(void \*block)
    :   Free memory from the shared multi-heap pool.

        Used to free the passed block of memory that must be the return value of a previously call to [shared\_multi\_heap\_alloc](#group__shared__multi__heap_1ga8cd3d321f5ae516cd55812d304289971) or [shared\_multi\_heap\_aligned\_alloc](#group__shared__multi__heap_1ga328b199253da06ed724e9b0157167ede).

        Parameters:
        :   - **block** – block to free, must be a pointer to a block allocated by shared\_multi\_heap\_alloc or shared\_multi\_heap\_aligned\_alloc.

    int shared\_multi\_heap\_add(struct [shared\_multi\_heap\_region](#c.shared_multi_heap_region) \*region, void \*user\_data)
    :   Add an heap region to the shared multi-heap pool.

        This adds a shared multi-heap region to the multi-heap pool.

        Parameters:
        :   - **user\_data** – pointer to any data for the heap.
            - **region** – pointer to the memory region to be added.

        Return values:
        :   - **0** – on success.
            - **-EINVAL** – when the region attribute is out-of-bound.
            - **-ENOMEM** – when there are no more heaps available.
            - **other** – errno codes

    struct shared\_multi\_heap\_region
    :   *#include <shared\_multi\_heap.h>*

        SMH region struct.

        This struct is carrying information about the memory region to be added in the multi-heap pool.

        Public Members

        uint32\_t attr
        :   Memory heap attribute.

        uintptr\_t addr
        :   Memory heap starting virtual address.

        size\_t size
        :   Memory heap size in bytes.
