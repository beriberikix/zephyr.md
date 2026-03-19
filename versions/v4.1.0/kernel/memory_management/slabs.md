---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/memory_management/slabs.html
original_path: kernel/memory_management/slabs.html
---

# Memory Slabs

A *memory slab* is a kernel object that allows memory blocks
to be dynamically allocated from a designated memory region.
All memory blocks in a memory slab have a single fixed size,
allowing them to be allocated and released efficiently
and avoiding memory fragmentation concerns.

## [Concepts](#id1)

Any number of memory slabs can be defined (limited only by available RAM). Each
memory slab is referenced by its memory address.

A memory slab has the following key properties:

- The **block size** of each block, measured in bytes.
  It must be at least 4N bytes long, where N is greater than 0.
- The **number of blocks** available for allocation.
  It must be greater than zero.
- A **buffer** that provides the memory for the memory slab’s blocks.
  It must be at least “block size” times “number of blocks” bytes long.

The memory slab’s buffer must be aligned to an N-byte boundary, where
N is a power of 2 larger than 2 (i.e. 4, 8, 16, …). To ensure that
all memory blocks in the buffer are similarly aligned to this boundary,
the block size must also be a multiple of N.

A memory slab must be initialized before it can be used. This marks all of
its blocks as unused.

A thread that needs to use a memory block simply allocates it from a memory
slab. When the thread finishes with a memory block,
it must release the block back to the memory slab so the block can be reused.

If all the blocks are currently in use, a thread can optionally wait
for one to become available.
Any number of threads may wait on an empty memory slab simultaneously;
when a memory block becomes available, it is given to the highest-priority
thread that has waited the longest.

Unlike a heap, more than one memory slab can be defined, if needed. This
allows for a memory slab with smaller blocks and others with larger-sized
blocks. Alternatively, a memory pool object may be used.

### [Internal Operation](#id2)

A memory slab’s buffer is an array of fixed-size blocks,
with no wasted space between the blocks.

The memory slab keeps track of unallocated blocks using a linked list;
the first 4 bytes of each unused block provide the necessary linkage.

## [Implementation](#id3)

### [Defining a Memory Slab](#id4)

A memory slab is defined using a variable of type `k_mem_slab`.
It must then be initialized by calling [`k_mem_slab_init()`](../../doxygen/html/group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1).

The following code defines and initializes a memory slab that has 6 blocks
that are 400 bytes long, each of which is aligned to a 4-byte boundary.

```c
struct k_mem_slab my_slab;
char __aligned(4) my_slab_buffer[6 * 400];

k_mem_slab_init(&my_slab, my_slab_buffer, 400, 6);
```

Alternatively, a memory slab can be defined and initialized at compile time
by calling [`K_MEM_SLAB_DEFINE`](../../doxygen/html/group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e).

The following code has the same effect as the code segment above. Observe
that the macro defines both the memory slab and its buffer.

```c
K_MEM_SLAB_DEFINE(my_slab, 400, 6, 4);
```

Similarly, you can define a memory slab in private scope:

```c
K_MEM_SLAB_DEFINE_STATIC(my_slab, 400, 6, 4);
```

### [Allocating a Memory Block](#id5)

A memory block is allocated by calling [`k_mem_slab_alloc()`](../../doxygen/html/group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a).

The following code builds on the example above, and waits up to 100 milliseconds
for a memory block to become available, then fills it with zeroes.
A warning is printed if a suitable block is not obtained.

```c
char *block_ptr;

if (k_mem_slab_alloc(&my_slab, (void **)&block_ptr, K_MSEC(100)) == 0) {
    memset(block_ptr, 0, 400);
    ...
} else {
    printf("Memory allocation time-out");
}
```

### [Releasing a Memory Block](#id6)

A memory block is released by calling [`k_mem_slab_free()`](../../doxygen/html/group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1).

The following code builds on the example above, and allocates a memory block,
then releases it once it is no longer needed.

```c
char *block_ptr;

k_mem_slab_alloc(&my_slab, (void **)&block_ptr, K_FOREVER);
... /* use memory block pointed at by block_ptr */
k_mem_slab_free(&my_slab, (void *)block_ptr);
```

## [Suggested Uses](#id7)

Use a memory slab to allocate and free memory in fixed-size blocks.

Use memory slab blocks when sending large amounts of data from one thread
to another, to avoid unnecessary copying of the data.

## [Configuration Options](#id8)

Related configuration options:

- [`CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION`](../../kconfig.md#CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION "CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION")

## [API Reference](#id9)

[Memory Slab APIs](../../doxygen/html/group__mem__slab__apis.md)
