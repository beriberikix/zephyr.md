---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/memory_management/slabs.html
original_path: kernel/memory_management/slabs.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
It must then be initialized by calling [`k_mem_slab_init()`](#c.k_mem_slab_init).

The following code defines and initializes a memory slab that has 6 blocks
that are 400 bytes long, each of which is aligned to a 4-byte boundary.

```c
struct k_mem_slab my_slab;
char __aligned(4) my_slab_buffer[6 * 400];

k_mem_slab_init(&my_slab, my_slab_buffer, 400, 6);
```

Alternatively, a memory slab can be defined and initialized at compile time
by calling [`K_MEM_SLAB_DEFINE`](#c.K_MEM_SLAB_DEFINE).

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

A memory block is allocated by calling [`k_mem_slab_alloc()`](#c.k_mem_slab_alloc).

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

A memory block is released by calling [`k_mem_slab_free()`](#c.k_mem_slab_free).

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

*group* mem\_slab\_apis
:   Defines

    K\_MEM\_SLAB\_DEFINE(name, slab\_block\_size, slab\_num\_blocks, slab\_align)
    :   Statically define and initialize a memory slab in a public (non-static) scope.

        The memory slab’s buffer contains *slab\_num\_blocks* memory blocks that are *slab\_block\_size* bytes long. The buffer is aligned to a *slab\_align* -byte boundary. To ensure that each memory block is similarly aligned to this boundary, *slab\_block\_size* must also be a multiple of *slab\_align*.

        The memory slab can be accessed outside the module where it is defined using:

        ```text
        extern struct k_mem_slab <name>;
        ```

        Note

        This macro cannot be used together with a static keyword. If such a use-case is desired, use [K\_MEM\_SLAB\_DEFINE\_STATIC](#group__mem__slab__apis_1ga90bdbb15f410991f54ba16025c24bc3c) instead.

        Parameters:
        :   - **name** – Name of the memory slab.
            - **slab\_block\_size** – Size of each memory block (in bytes).
            - **slab\_num\_blocks** – Number memory blocks.
            - **slab\_align** – Alignment of the memory slab’s buffer (power of 2).

    K\_MEM\_SLAB\_DEFINE\_STATIC(name, slab\_block\_size, slab\_num\_blocks, slab\_align)
    :   Statically define and initialize a memory slab in a private (static) scope.

        The memory slab’s buffer contains *slab\_num\_blocks* memory blocks that are *slab\_block\_size* bytes long. The buffer is aligned to a *slab\_align* -byte boundary. To ensure that each memory block is similarly aligned to this boundary, *slab\_block\_size* must also be a multiple of *slab\_align*.

        Parameters:
        :   - **name** – Name of the memory slab.
            - **slab\_block\_size** – Size of each memory block (in bytes).
            - **slab\_num\_blocks** – Number memory blocks.
            - **slab\_align** – Alignment of the memory slab’s buffer (power of 2).

    Functions

    int k\_mem\_slab\_init(struct k\_mem\_slab \*slab, void \*buffer, size\_t block\_size, uint32\_t num\_blocks)
    :   Initialize a memory slab.

        Initializes a memory slab, prior to its first use.

        The memory slab’s buffer contains *slab\_num\_blocks* memory blocks that are *slab\_block\_size* bytes long. The buffer must be aligned to an N-byte boundary matching a word boundary, where N is a power of 2 (i.e. 4 on 32-bit systems, 8, 16, …). To ensure that each memory block is similarly aligned to this boundary, *slab\_block\_size* must also be a multiple of N.

        Parameters:
        :   - **slab** – Address of the memory slab.
            - **buffer** – Pointer to buffer used for the memory blocks.
            - **block\_size** – Size of each memory block (in bytes).
            - **num\_blocks** – Number of memory blocks.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – invalid data supplied

    int k\_mem\_slab\_alloc(struct k\_mem\_slab \*slab, void \*\*mem, [k\_timeout\_t](../services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate memory from a memory slab.

        This routine allocates a memory block from a memory slab.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Note

        When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

        Parameters:
        :   - **slab** – Address of the memory slab.
            - **mem** – Pointer to block address area.
            - **timeout** – Non-negative waiting period to wait for operation to complete. Use K\_NO\_WAIT to return without waiting, or K\_FOREVER to wait as long as necessary.

        Return values:
        :   - **0** – Memory allocated. The block address area pointed at by *mem* is set to the starting address of the memory block.
            - **-ENOMEM** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.
            - **-EINVAL** – Invalid data supplied

    void k\_mem\_slab\_free(struct k\_mem\_slab \*slab, void \*mem)
    :   Free memory allocated from a memory slab.

        This routine releases a previously allocated memory block back to its associated memory slab.

        Parameters:
        :   - **slab** – Address of the memory slab.
            - **mem** – Pointer to the memory block (as returned by [k\_mem\_slab\_alloc()](#group__mem__slab__apis_1gab16a46d8394aca18de740ad044a8734a)).

    static inline uint32\_t k\_mem\_slab\_num\_used\_get(struct k\_mem\_slab \*slab)
    :   Get the number of used blocks in a memory slab.

        This routine gets the number of memory blocks that are currently allocated in *slab*.

        Parameters:
        :   - **slab** – Address of the memory slab.

        Returns:
        :   Number of allocated memory blocks.

    static inline uint32\_t k\_mem\_slab\_max\_used\_get(struct k\_mem\_slab \*slab)
    :   Get the number of maximum used blocks so far in a memory slab.

        This routine gets the maximum number of memory blocks that were allocated in *slab*.

        Parameters:
        :   - **slab** – Address of the memory slab.

        Returns:
        :   Maximum number of allocated memory blocks.

    static inline uint32\_t k\_mem\_slab\_num\_free\_get(struct k\_mem\_slab \*slab)
    :   Get the number of unused blocks in a memory slab.

        This routine gets the number of memory blocks that are currently unallocated in *slab*.

        Parameters:
        :   - **slab** – Address of the memory slab.

        Returns:
        :   Number of unallocated memory blocks.

    int k\_mem\_slab\_runtime\_stats\_get(struct k\_mem\_slab \*slab, struct sys\_memory\_stats \*stats)
    :   Get the memory stats for a memory slab.

        This routine gets the runtime memory usage stats for the slab *slab*.

        Parameters:
        :   - **slab** – Address of the memory slab
            - **stats** – Pointer to memory into which to copy memory usage statistics

        Return values:
        :   - **0** – Success
            - **-EINVAL** – Any parameter points to NULL

    int k\_mem\_slab\_runtime\_stats\_reset\_max(struct k\_mem\_slab \*slab)
    :   Reset the maximum memory usage for a slab.

        This routine resets the maximum memory usage for the slab *slab* to its current usage.

        Parameters:
        :   - **slab** – Address of the memory slab

        Return values:
        :   - **0** – Success
            - **-EINVAL** – Memory slab is NULL
