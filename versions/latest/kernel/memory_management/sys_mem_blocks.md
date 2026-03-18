---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/memory_management/sys_mem_blocks.html
original_path: kernel/memory_management/sys_mem_blocks.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Memory Blocks Allocator

The Memory Blocks Allocator allows memory blocks to be dynamically
allocated from a designated memory region, where:

- All memory blocks have a single fixed size.
- Multiple blocks can be allocated or freed at the same time.
- A group of blocks allocated together may not be contiguous.
  This is useful for operations such as scatter-gather DMA transfers.
- Bookkeeping of allocated blocks is done outside of the associated
  buffer (unlike memory slab). This allows the buffer to reside in
  memory regions where these can be powered down to conserve energy.

## [Concepts](#id2)

Any number of Memory Blocks Allocator can be defined (limited only by
available RAM). Each allocator is referenced by its memory address.

A memory blocks allocator has the following key properties:

- The **block size** of each block, measured in bytes.
  It must be at least 4N bytes long, where N is greater than 0.
- The **number of blocks** available for allocation.
  It must be greater than zero.
- A **buffer** that provides the memory for the memory slab’s blocks.
  It must be at least “block size” times “number of blocks” bytes long.
- A **blocks bitmap** to keep track of which block has been allocated.

The buffer must be aligned to an N-byte boundary, where N is a power of 2
larger than 2 (i.e. 4, 8, 16, …). To ensure that all memory blocks in
the buffer are similarly aligned to this boundary, the block size must
also be a multiple of N.

Due to the use of internal bookkeeping structures and their creation,
each memory blocks allocator must be declared and defined at compile time.

### [Internal Operation](#id3)

Each buffer associated with an allocator is an array of fixed-size blocks,
with no wasted space between the blocks.

The memory blocks allocator keeps track of unallocated blocks using
a bitmap.

## [Memory Blocks Allocator](#id4)

Internally, the memory blocks allocator uses a bitmap to keep track of
which blocks have been allocated. Each allocator, utilizing
the `sys_bitarray` interface, gets memory blocks one by one from
the backing buffer up to the requested number of blocks.
All the metadata about an allocator is stored outside of the backing
buffer. This allows the memory region of the backing buffer to be
powered down to conserve energy, as the allocator code never touches
the content of the buffer.

## [Multi Memory Blocks Allocator Group](#id5)

The Multi Memory Blocks Allocator Group utility functions provide
a convenient to manage a group of allocators. A custom allocator
choosing function is used to choose which allocator to use among
this group.

An allocator group should be initialized at runtime via
[`sys_multi_mem_blocks_init()`](#c.sys_multi_mem_blocks_init). Each allocator can then be
added via [`sys_multi_mem_blocks_add_allocator()`](#c.sys_multi_mem_blocks_add_allocator).

To allocate memory blocks from group,
[`sys_multi_mem_blocks_alloc()`](#c.sys_multi_mem_blocks_alloc) is called with an opaque
“configuration” parameter. This parameter is passed directly to
the allocator choosing function so that an appropriate allocator
can be chosen. After an allocator is chosen, memory blocks are
allocated via [`sys_mem_blocks_alloc()`](#c.sys_mem_blocks_alloc).

Allocated memory blocks can be freed via
[`sys_multi_mem_blocks_free()`](#c.sys_multi_mem_blocks_free). The caller does not need to
pass a configuration parameter. The allocator code matches
the passed in memory addresses to find the correct allocator
and then memory blocks are freed via [`sys_mem_blocks_free()`](#c.sys_mem_blocks_free).

## [Usage](#id6)

### [Defining a Memory Blocks Allocator](#id7)

A memory blocks allocator is defined using a variable of type
[`sys_mem_blocks_t`](#c.sys_mem_blocks_t). It needs to be defined and initialized
at compile time by calling [`SYS_MEM_BLOCKS_DEFINE`](#c.SYS_MEM_BLOCKS_DEFINE).

The following code defines and initializes a memory blocks allocator
which has 4 blocks that are 64 bytes long, each of which is aligned
to a 4-byte boundary:

```c
SYS_MEM_BLOCKS_DEFINE(allocator, 64, 4, 4);
```

Similarly, you can define a memory blocks allocator in private scope:

```c
SYS_MEM_BLOCKS_DEFINE_STATIC(static_allocator, 64, 4, 4);
```

A pre-defined buffer can also be provided to the allocator where
the buffer can be placed separately. Note that the alignment of
the buffer needs to be done at its definition.

```c
uint8_t __aligned(4) backing_buffer[64 * 4];
SYS_MEM_BLOCKS_DEFINE_WITH_EXT_BUF(allocator, 64, 4, backing_buffer);
```

### [Allocating Memory Blocks](#id8)

Memory blocks can be allocated by calling [`sys_mem_blocks_alloc()`](#c.sys_mem_blocks_alloc).

```c
int ret;
uintptr_t blocks[2];

ret = sys_mem_blocks_alloc(allocator, 2, blocks);
```

If `ret == 0`, the array `blocks` will contain an array of memory
addresses pointing to the allocated blocks.

### [Releasing a Memory Block](#id9)

Memory blocks are released by calling [`sys_mem_blocks_free()`](#c.sys_mem_blocks_free).

The following code builds on the example above which allocates 2 memory blocks,
then releases them once they are no longer needed.

```c
int ret;
uintptr_t blocks[2];

ret = sys_mem_blocks_alloc(allocator, 2, blocks);
... /* perform some operations on the allocated memory blocks */
ret = sys_mem_blocks_free(allocator, 2, blocks);
```

### [Using Multi Memory Blocks Allocator Group](#id10)

The following code demonstrates how to initialize an allocator group:

```c
sys_mem_blocks_t *choice_fn(struct sys_multi_mem_blocks *group, void *cfg)
{
    ...
}

SYS_MEM_BLOCKS_DEFINE(allocator0, 64, 4, 4);
SYS_MEM_BLOCKS_DEFINE(allocator1, 64, 4, 4);

static sys_multi_mem_blocks_t alloc_group;

sys_multi_mem_blocks_init(&alloc_group, choice_fn);
sys_multi_mem_blocks_add_allocator(&alloc_group, &allocator0);
sys_multi_mem_blocks_add_allocator(&alloc_group, &allocator1);
```

To allocate and free memory blocks from the group:

```c
int ret;
uintptr_t blocks[1];
size_t blk_size;

ret = sys_multi_mem_blocks_alloc(&alloc_group, UINT_TO_POINTER(0),
                                 1, blocks, &blk_size);

ret = sys_multi_mem_blocks_free(&alloc_group, 1, blocks);
```

## [API Reference](#id11)

*group* mem\_blocks\_apis
:   Defines

    SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, buf\_align)
    :   Create a memory block object with a new backing buffer.

        Parameters:
        :   - **name** – Name of the memory block object.
            - **blk\_sz** – Size of each memory block (in bytes).
            - **num\_blks** – Total number of memory blocks.
            - **buf\_align** – Alignment of the memory block buffer (power of 2).

    SYS\_MEM\_BLOCKS\_DEFINE\_STATIC(name, blk\_sz, num\_blks, buf\_align)
    :   Create a static memory block object with a new backing buffer.

        Parameters:
        :   - **name** – Name of the memory block object.
            - **blk\_sz** – Size of each memory block (in bytes).
            - **num\_blks** – Total number of memory blocks.
            - **buf\_align** – Alignment of the memory block buffer (power of 2).

    SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf)
    :   Create a memory block object with a providing backing buffer.

        Parameters:
        :   - **name** – Name of the memory block object.
            - **blk\_sz** – Size of each memory block (in bytes).
            - **num\_blks** – Total number of memory blocks.
            - **buf** – Backing buffer of type uint8\_t.

    SYS\_MEM\_BLOCKS\_DEFINE\_STATIC\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf)
    :   Create a static memory block object with a providing backing buffer.

        Parameters:
        :   - **name** – Name of the memory block object.
            - **blk\_sz** – Size of each memory block (in bytes).
            - **num\_blks** – Total number of memory blocks.
            - **buf** – Backing buffer of type uint8\_t.

    Typedefs

    typedef struct sys\_mem\_blocks sys\_mem\_blocks\_t
    :   Memory Blocks Allocator.

    typedef struct sys\_multi\_mem\_blocks sys\_multi\_mem\_blocks\_t
    :   Multi Memory Blocks Allocator.

    typedef [sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*(\*sys\_multi\_mem\_blocks\_choice\_fn\_t)(struct sys\_multi\_mem\_blocks \*group, void \*cfg)
    :   Multi memory blocks allocator choice function.

        This is a user-provided functions whose responsibility is selecting a specific memory blocks allocator based on the opaque cfg value, which is specified by the user as an argument to [sys\_multi\_mem\_blocks\_alloc()](#group__mem__blocks__apis_1gafa96b1567b57c4466c9640fd1f5408b2). The callback returns a pointer to the chosen allocator where the allocation is performed.

        NULL may be returned, which will cause the allocation to fail and a -EINVAL reported to the calling code.

        Param group:
        :   Multi memory blocks allocator structure.

        Param cfg:
        :   An opaque user-provided value. It may be interpreted in any way by the application.

        Return:
        :   A pointer to the chosen allocator, or NULL if none is chosen.

    Functions

    int sys\_mem\_blocks\_alloc([sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*mem\_block, size\_t count, void \*\*out\_blocks)
    :   Allocate multiple memory blocks.

        Allocate multiple memory blocks, and place their pointers into the output array.

        Parameters:
        :   - **mem\_block** – **[in]** Pointer to memory block object.
            - **count** – **[in]** Number of blocks to allocate.
            - **out\_blocks** – **[out]** Output array to be populated by pointers to the memory blocks. It must have at least `count` elements.

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied.
            - **-ENOMEM** – Not enough blocks for allocation.

    int sys\_mem\_blocks\_alloc\_contiguous([sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*mem\_block, size\_t count, void \*\*out\_block)
    :   Allocate a contiguous set of memory blocks.

        Allocate multiple memory blocks, and place their pointers into the output array.

        Parameters:
        :   - **mem\_block** – **[in]** Pointer to memory block object.
            - **count** – **[in]** Number of blocks to allocate.
            - **out\_block** – **[out]** Output pointer to the start of the allocated block set

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied.
            - **-ENOMEM** – Not enough contiguous blocks for allocation.

    int sys\_mem\_blocks\_get([sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*mem\_block, void \*in\_block, size\_t count)
    :   Force allocation of a specified blocks in a memory block object.

        Allocate a specified blocks in a memory block object. Note: use caution when mixing sys\_mem\_blocks\_get and sys\_mem\_blocks\_alloc, allocation may take any of the free memory space

        Parameters:
        :   - **mem\_block** – **[in]** Pointer to memory block object.
            - **in\_block** – **[in]** Address of the first required block to allocate
            - **count** – **[in]** Number of blocks to allocate.

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied.
            - **-ENOMEM** – Some of blocks are taken and cannot be allocated

    int sys\_mem\_blocks\_is\_region\_free([sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*mem\_block, void \*in\_block, size\_t count)
    :   check if the region is free

        Parameters:
        :   - **mem\_block** – **[in]** Pointer to memory block object.
            - **in\_block** – **[in]** Address of the first block to check
            - **count** – **[in]** Number of blocks to check.

        Return values:
        :   - **1** – All memory blocks are free
            - **0** – At least one of the memory blocks is taken

    int sys\_mem\_blocks\_free([sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*mem\_block, size\_t count, void \*\*in\_blocks)
    :   Free multiple memory blocks.

        Free multiple memory blocks according to the array of memory block pointers.

        Parameters:
        :   - **mem\_block** – **[in]** Pointer to memory block object.
            - **count** – **[in]** Number of blocks to free.
            - **in\_blocks** – **[in]** Input array of pointers to the memory blocks.

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied.
            - **-EFAULT** – Invalid pointers supplied.

    int sys\_mem\_blocks\_free\_contiguous([sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*mem\_block, void \*block, size\_t count)
    :   Free contiguous multiple memory blocks.

        Free contiguous multiple memory blocks

        Parameters:
        :   - **mem\_block** – **[in]** Pointer to memory block object.
            - **block** – **[in]** Pointer to the first memory block
            - **count** – **[in]** Number of blocks to free.

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied.
            - **-EFAULT** – Invalid pointer supplied.

    void sys\_multi\_mem\_blocks\_init([sys\_multi\_mem\_blocks\_t](#c.sys_multi_mem_blocks_t) \*group, [sys\_multi\_mem\_blocks\_choice\_fn\_t](#c.sys_multi_mem_blocks_choice_fn_t) choice\_fn)
    :   Initialize multi memory blocks allocator group.

        Initialize a sys\_multi\_mem\_block struct with the specified choice function. Note that individual allocator must be added later with sys\_multi\_mem\_blocks\_add\_allocator.

        Parameters:
        :   - **group** – Multi memory blocks allocator structure.
            - **choice\_fn** – A [sys\_multi\_mem\_blocks\_choice\_fn\_t](#group__mem__blocks__apis_1ga2e58484681d0d9629af9a8c7c14453d9) callback used to select the allocator to be used at allocation time

    void sys\_multi\_mem\_blocks\_add\_allocator([sys\_multi\_mem\_blocks\_t](#c.sys_multi_mem_blocks_t) \*group, [sys\_mem\_blocks\_t](#c.sys_mem_blocks_t) \*alloc)
    :   Add an allocator to an allocator group.

        This adds a known allocator to an existing multi memory blocks allocator group.

        Parameters:
        :   - **group** – Multi memory blocks allocator structure.
            - **alloc** – Allocator to add

    int sys\_multi\_mem\_blocks\_alloc([sys\_multi\_mem\_blocks\_t](#c.sys_multi_mem_blocks_t) \*group, void \*cfg, size\_t count, void \*\*out\_blocks, size\_t \*blk\_size)
    :   Allocate memory from multi memory blocks allocator group.

        Just as for [sys\_mem\_blocks\_alloc()](#group__mem__blocks__apis_1ga3e53a5c65bb0e88fbf20e66b016c1dff), allocates multiple blocks of memory. Takes an opaque configuration pointer passed to the choice function, which is used by integration code to choose an allocator.

        Parameters:
        :   - **group** – **[in]** Multi memory blocks allocator structure.
            - **cfg** – **[in]** Opaque configuration parameter, as for [sys\_multi\_mem\_blocks\_choice\_fn\_t](#group__mem__blocks__apis_1ga2e58484681d0d9629af9a8c7c14453d9)
            - **count** – **[in]** Number of blocks to allocate
            - **out\_blocks** – **[out]** Output array to be populated by pointers to the memory blocks. It must have at least `count` elements.
            - **blk\_size** – **[out]** If not NULL, output the block size of the chosen allocator.

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied, or no allocator chosen.
            - **-ENOMEM** – Not enough blocks for allocation.

    int sys\_multi\_mem\_blocks\_free([sys\_multi\_mem\_blocks\_t](#c.sys_multi_mem_blocks_t) \*group, size\_t count, void \*\*in\_blocks)
    :   Free memory allocated from multi memory blocks allocator group.

        Free previous allocated memory blocks from [sys\_multi\_mem\_blocks\_alloc()](#group__mem__blocks__apis_1gafa96b1567b57c4466c9640fd1f5408b2).

        Note that all blocks in `in_blocks` must be from the same allocator.

        Parameters:
        :   - **group** – **[in]** Multi memory blocks allocator structure.
            - **count** – **[in]** Number of blocks to free.
            - **in\_blocks** – **[in]** Input array of pointers to the memory blocks.

        Return values:
        :   - **0** – Successful
            - **-EINVAL** – Invalid argument supplied, or no allocator chosen.
            - **-EFAULT** – Invalid pointer(s) supplied.
