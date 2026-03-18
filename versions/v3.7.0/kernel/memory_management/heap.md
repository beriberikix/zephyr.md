---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/memory_management/heap.html
original_path: kernel/memory_management/heap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Memory Heaps

Zephyr provides a collection of utilities that allow threads to
dynamically allocate memory.

## Synchronized Heap Allocator

### Creating a Heap

The simplest way to define a heap is statically, with the
[`K_HEAP_DEFINE`](#c.K_HEAP_DEFINE) macro. This creates a static [`k_heap`](#c.k_heap) variable
with a given name that manages a memory region of the
specified size.

Heaps can also be created to manage arbitrary regions of
application-controlled memory using [`k_heap_init()`](#c.k_heap_init).

### Allocating Memory

Memory can be allocated from a heap using [`k_heap_alloc()`](#c.k_heap_alloc),
passing it the address of the heap object and the number of bytes
desired. This functions similarly to standard C `malloc()`,
returning a NULL pointer on an allocation failure.

The heap supports blocking operation, allowing threads to go to sleep
until memory is available. The final argument is a
[`k_timeout_t`](../services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout value indicating how long the thread may
sleep before returning, or else one of the constant timeout values
[`K_NO_WAIT`](../services/timing/clocks.md#c.K_NO_WAIT "K_NO_WAIT") or [`K_FOREVER`](../services/timing/clocks.md#c.K_FOREVER "K_FOREVER").

### Releasing Memory

Memory allocated with [`k_heap_alloc()`](#c.k_heap_alloc) must be released using
[`k_heap_free()`](#c.k_heap_free). Similar to standard C `free()`, the pointer
provided must be either a `NULL` value or a pointer previously
returned by [`k_heap_alloc()`](#c.k_heap_alloc) for the same heap. Freeing a
`NULL` value is defined to have no effect.

## Low Level Heap Allocator

The underlying implementation of the [`k_heap`](#c.k_heap)
abstraction is provided a data structure named `sys_heap`. This
implements exactly the same allocation semantics, but
provides no kernel synchronization tools. It is available for
applications that want to manage their own blocks of memory in
contexts (for example, userspace) where synchronization is unavailable
or more complicated. Unlike `k_heap`, all calls to any `sys_heap`
functions on a single heap must be serialized by the caller.
Simultaneous use from separate threads is disallowed.

### Implementation

Internally, the `sys_heap` memory block is partitioned into “chunks”
of 8 bytes. All allocations are made out of a contiguous region of
chunks. The first chunk of every allocation or unused block is
prefixed by a chunk header that stores the length of the chunk, the
length of the next lower (“left”) chunk in physical memory, a bit
indicating whether the chunk is in use, and chunk-indexed link
pointers to the previous and next chunk in a “free list” to which
unused chunks are added.

The heap code takes reasonable care to avoid fragmentation. Free
block lists are stored in “buckets” by their size, each bucket storing
blocks within one power of two (i.e. a bucket for blocks of 3-4
chunks, another for 5-8, 9-16, etc…) this allows new allocations to
be made from the smallest/most-fragmented blocks available. Also, as
allocations are freed and added to the heap, they are automatically
combined with adjacent free blocks to prevent fragmentation.

All metadata is stored at the beginning of the contiguous block of
heap memory, including the variable-length list of bucket list heads
(which depend on heap size). The only external memory required is the
`sys_heap` structure itself.

The `sys_heap` functions are unsynchronized. Care must be taken by
any users to prevent concurrent access. Only one context may be
inside one of the API functions at a time.

The heap code takes care to present high performance and reliable
latency. All `sys_heap` API functions are guaranteed to complete
within constant time. On typical architectures, they will all
complete within 1-200 cycles. One complexity is that the search of
the minimum bucket size for an allocation (the set of free blocks that
“might fit”) has a compile-time upper bound of iterations to prevent
unbounded list searches, at the expense of some fragmentation
resistance. This [`CONFIG_SYS_HEAP_ALLOC_LOOPS`](../../kconfig.md#CONFIG_SYS_HEAP_ALLOC_LOOPS "CONFIG_SYS_HEAP_ALLOC_LOOPS") value may be
chosen by the user at build time, and defaults to a value of 3.

## Multi-Heap Wrapper Utility

The `sys_heap` utility requires that all managed memory be in a
single contiguous block. It is common for complicated microcontroller
applications to have more complicated memory setups that they still
want to manage dynamically as a “heap”. For example, the memory might
exist as separate discontiguous regions, different areas may have
different cache, performance or power behavior, peripheral devices may
only be able to perform DMA to certain regions, etc…

For those situations, Zephyr provides a `sys_multi_heap` utility.
Effectively this is a simple wrapper around a set of one or more
`sys_heap` objects. It should be initialized after its child heaps
via [`sys_multi_heap_init()`](#c.sys_multi_heap_init), after which each heap can be added
to the managed set via [`sys_multi_heap_add_heap()`](#c.sys_multi_heap_add_heap). No
destruction utility is provided; just as for `sys_heap`,
applications that want to destroy a multi heap should simply ensure
all allocated blocks are freed (or at least will never be used again)
and repurpose the underlying memory for another usage.

It has a single pair of allocation entry points,
[`sys_multi_heap_alloc()`](#c.sys_multi_heap_alloc) and
[`sys_multi_heap_aligned_alloc()`](#c.sys_multi_heap_aligned_alloc). These behave identically to
the `sys_heap` functions with similar names, except that they also
accept an opaque “configuration” parameter. This pointer is
uninspected by the multi heap code itself; instead it is passed to a
callback function provided at initialization time. This
application-provided callback is responsible for doing the underlying
allocation from one of the managed heaps, and may use the
configuration parameter in any way it likes to make that decision.

When unused, a multi heap may be freed via
[`sys_multi_heap_free()`](#c.sys_multi_heap_free). The application does not need to pass
a configuration parameter. Memory allocated from any of the managed
`sys_heap` objects may be freed with in the same way.

## System Heap

The *system heap* is a predefined memory allocator that allows
threads to dynamically allocate memory from a common memory region in
a `malloc()`-like manner.

Only a single system heap is defined. Unlike other heaps or memory
pools, the system heap cannot be directly referenced using its
memory address.

The size of the system heap is configurable to arbitrary sizes,
subject to space availability.

A thread can dynamically allocate a chunk of heap memory by calling
[`k_malloc()`](#c.k_malloc). The address of the allocated chunk is
guaranteed to be aligned on a multiple of pointer sizes. If a suitable
chunk of heap memory cannot be found `NULL` is returned.

When the thread is finished with a chunk of heap memory it can release
the chunk back to the system heap by calling [`k_free()`](#c.k_free).

### Defining the Heap Memory Pool

The size of the heap memory pool is specified using the
[`CONFIG_HEAP_MEM_POOL_SIZE`](../../kconfig.md#CONFIG_HEAP_MEM_POOL_SIZE "CONFIG_HEAP_MEM_POOL_SIZE") configuration option.

By default, the heap memory pool size is zero bytes. This value instructs
the kernel not to define the heap memory pool object. The maximum size is limited
by the amount of available memory in the system. The project build will fail in
the link stage if the size specified can not be supported.

In addition, each subsystem (board, driver, library, etc) can set a custom
requirement by defining a Kconfig option with the prefix
`HEAP_MEM_POOL_ADD_SIZE_` (this value is in bytes). If multiple subsystems
specify custom values, the sum of these will be used as the minimum requirement.
If the application tries to set a value that’s less than the minimum value, this
will be ignored and the minimum value will be used instead.

To force a smaller than minimum value to be used, the application may enable the
[`CONFIG_HEAP_MEM_POOL_IGNORE_MIN`](../../kconfig.md#CONFIG_HEAP_MEM_POOL_IGNORE_MIN "CONFIG_HEAP_MEM_POOL_IGNORE_MIN") option. This can be useful
when optimizing the heap size and the minimum requirement can be more accurately
determined for a specific application.

### Allocating Memory

A chunk of heap memory is allocated by calling [`k_malloc()`](#c.k_malloc).

The following code allocates a 200 byte chunk of heap memory, then fills it
with zeros. A warning is issued if a suitable chunk is not obtained.

```c
char *mem_ptr;

mem_ptr = k_malloc(200);
if (mem_ptr != NULL)) {
    memset(mem_ptr, 0, 200);
    ...
} else {
    printf("Memory not allocated");
}
```

### Releasing Memory

A chunk of heap memory is released by calling [`k_free()`](#c.k_free).

The following code allocates a 75 byte chunk of memory, then releases it
once it is no longer needed.

```c
char *mem_ptr;

mem_ptr = k_malloc(75);
... /* use memory block */
k_free(mem_ptr);
```

### Suggested Uses

Use the heap memory pool to dynamically allocate memory in a
`malloc()`-like manner.

### Configuration Options

Related configuration options:

- [`CONFIG_HEAP_MEM_POOL_SIZE`](../../kconfig.md#CONFIG_HEAP_MEM_POOL_SIZE "CONFIG_HEAP_MEM_POOL_SIZE")

### API Reference

*group* Heap APIs
:   Defines

    K\_HEAP\_DEFINE(name, bytes)
    :   Define a static [k\_heap](#structk__heap).

        This macro defines and initializes a static memory region and [k\_heap](#structk__heap) of the requested size. After kernel start, &name can be used as if [k\_heap\_init()](#group__heap__apis_1ga9273e06dc8d6a351499f2f5abfdcb39f) had been called.

        Note that this macro enforces a minimum size on the memory region to accommodate metadata requirements. Very small heaps will be padded to fit.

        Parameters:
        :   - **name** – Symbol name for the struct [k\_heap](#structk__heap) object
            - **bytes** – Size of memory region, in bytes

    K\_HEAP\_DEFINE\_NOCACHE(name, bytes)
    :   Define a static [k\_heap](#structk__heap) in uncached memory.

        This macro defines and initializes a static memory region and [k\_heap](#structk__heap) of the requested size in uncached memory. After kernel start, &name can be used as if [k\_heap\_init()](#group__heap__apis_1ga9273e06dc8d6a351499f2f5abfdcb39f) had been called.

        Note that this macro enforces a minimum size on the memory region to accommodate metadata requirements. Very small heaps will be padded to fit.

        Parameters:
        :   - **name** – Symbol name for the struct [k\_heap](#structk__heap) object
            - **bytes** – Size of memory region, in bytes

    Functions

    void k\_heap\_init(struct [k\_heap](#c.k_heap) \*h, void \*mem, size\_t bytes)
    :   Initialize a [k\_heap](#structk__heap).

        This constructs a synchronized [k\_heap](#structk__heap) object over a memory region specified by the user. Note that while any alignment and size can be passed as valid parameters, internal alignment restrictions inside the inner sys\_heap mean that not all bytes may be usable as allocated memory.

        Parameters:
        :   - **h** – Heap struct to initialize
            - **mem** – Pointer to memory.
            - **bytes** – Size of memory region, in bytes

    void \*k\_heap\_aligned\_alloc(struct [k\_heap](#c.k_heap) \*h, size\_t align, size\_t bytes, [k\_timeout\_t](../services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate aligned memory from a [k\_heap](#structk__heap).

        Behaves in all ways like [k\_heap\_alloc()](#group__heap__apis_1ga22b83564e50ae6177388dfe63e32a512), except that the returned memory (if available) will have a starting address in memory which is a multiple of the specified power-of-two alignment value in bytes. The resulting memory can be returned to the heap using [k\_heap\_free()](#group__heap__apis_1ga6cf917a0b3d91a0101192bd4808ada9c).

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Note

        When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

        Parameters:
        :   - **h** – Heap from which to allocate
            - **align** – Alignment in bytes, must be a power of two
            - **bytes** – Number of bytes requested
            - **timeout** – How long to wait, or K\_NO\_WAIT

        Returns:
        :   Pointer to memory the caller can now use

    void \*k\_heap\_alloc(struct [k\_heap](#c.k_heap) \*h, size\_t bytes, [k\_timeout\_t](../services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate memory from a [k\_heap](#structk__heap).

        Allocates and returns a memory buffer from the memory region owned by the heap. If no memory is available immediately, the call will block for the specified timeout (constructed via the standard timeout API, or K\_NO\_WAIT or K\_FOREVER) waiting for memory to be freed. If the allocation cannot be performed by the expiration of the timeout, NULL will be returned. Allocated memory is aligned on a multiple of pointer sizes.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Note

        When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

        Parameters:
        :   - **h** – Heap from which to allocate
            - **bytes** – Desired size of block to allocate
            - **timeout** – How long to wait, or K\_NO\_WAIT

        Returns:
        :   A pointer to valid heap memory, or NULL

    void \*k\_heap\_realloc(struct [k\_heap](#c.k_heap) \*h, void \*ptr, size\_t bytes, [k\_timeout\_t](../services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Reallocate memory from a [k\_heap](#structk__heap).

        Reallocates and returns a memory buffer from the memory region owned by the heap. If no memory is available immediately, the call will block for the specified timeout (constructed via the standard timeout API, or K\_NO\_WAIT or K\_FOREVER) waiting for memory to be freed. If the allocation cannot be performed by the expiration of the timeout, NULL will be returned. Reallocated memory is aligned on a multiple of pointer sizes.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Note

        When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

        Parameters:
        :   - **h** – Heap from which to allocate
            - **ptr** – Original pointer returned from a previous allocation
            - **bytes** – Desired size of block to allocate
            - **timeout** – How long to wait, or K\_NO\_WAIT

        Returns:
        :   Pointer to memory the caller can now use, or NULL

    void k\_heap\_free(struct [k\_heap](#c.k_heap) \*h, void \*mem)
    :   Free memory allocated by [k\_heap\_alloc()](#group__heap__apis_1ga22b83564e50ae6177388dfe63e32a512).

        Returns the specified memory block, which must have been returned from [k\_heap\_alloc()](#group__heap__apis_1ga22b83564e50ae6177388dfe63e32a512), to the heap for use by other callers. Passing a NULL block is legal, and has no effect.

        Parameters:
        :   - **h** – Heap to which to return the memory
            - **mem** – A valid memory block, or NULL

    void \*k\_aligned\_alloc(size\_t align, size\_t size)
    :   Allocate memory from the heap with a specified alignment.

        This routine provides semantics similar to aligned\_alloc(); memory is allocated from the heap with a specified alignment. However, one minor difference is that [k\_aligned\_alloc()](#group__heap__apis_1gae16d486aa250f9c07fa6a57342bcd3b4) accepts any non-zero `size`, whereas aligned\_alloc() only accepts a `size` that is an integral multiple of `align`.

        Above, aligned\_alloc() refers to: C11 standard (ISO/IEC 9899:2011): 7.22.3.1 The aligned\_alloc function (p: 347-348)

        Parameters:
        :   - **align** – Alignment of memory requested (in bytes).
            - **size** – Amount of memory requested (in bytes).

        Returns:
        :   Address of the allocated memory if successful; otherwise NULL.

    void \*k\_malloc(size\_t size)
    :   Allocate memory from the heap.

        This routine provides traditional malloc() semantics. Memory is allocated from the heap memory pool. Allocated memory is aligned on a multiple of pointer sizes.

        Parameters:
        :   - **size** – Amount of memory requested (in bytes).

        Returns:
        :   Address of the allocated memory if successful; otherwise NULL.

    void k\_free(void \*ptr)
    :   Free memory allocated from heap.

        This routine provides traditional free() semantics. The memory being returned must have been allocated from the heap memory pool.

        If *ptr* is NULL, no operation is performed.

        Parameters:
        :   - **ptr** – Pointer to previously allocated memory.

    void \*k\_calloc(size\_t nmemb, size\_t size)
    :   Allocate memory from heap, array style.

        This routine provides traditional calloc() semantics. Memory is allocated from the heap memory pool and zeroed.

        Parameters:
        :   - **nmemb** – Number of elements in the requested array
            - **size** – Size of each array element (in bytes).

        Returns:
        :   Address of the allocated memory if successful; otherwise NULL.

    void \*k\_realloc(void \*ptr, size\_t size)
    :   Expand the size of an existing allocation.

        Returns a pointer to a new memory region with the same contents, but a different allocated size. If the new allocation can be expanded in place, the pointer returned will be identical. Otherwise the data will be copies to a new block and the old one will be freed as per [sys\_heap\_free()](#group__low__level__heap__allocator_1gab654da64adf74e67ae12f263eb420560). If the specified size is smaller than the original, the block will be truncated in place and the remaining memory returned to the heap. If the allocation of a new block fails, then NULL will be returned and the old block will not be freed or modified.

        Parameters:
        :   - **ptr** – Original pointer returned from a previous allocation
            - **size** – Amount of memory requested (in bytes).

        Returns:
        :   Pointer to memory the caller can now use, or NULL.

    struct k\_heap
    :   *#include <kernel.h>*

*group* Low Level Heap Allocator
:   Defines

    sys\_heap\_realloc(heap, ptr, bytes)

    Functions

    void sys\_heap\_init(struct sys\_heap \*heap, void \*mem, size\_t bytes)
    :   Initialize sys\_heap.

        Initializes a sys\_heap struct to manage the specified memory.

        Parameters:
        :   - **heap** – Heap to initialize
            - **mem** – Untyped pointer to unused memory
            - **bytes** – Size of region pointed to by *mem*

    void \*sys\_heap\_alloc(struct sys\_heap \*heap, size\_t bytes)
    :   Allocate memory from a sys\_heap.

        Returns a pointer to a block of unused memory in the heap. This memory will not otherwise be used until it is freed with [sys\_heap\_free()](#group__low__level__heap__allocator_1gab654da64adf74e67ae12f263eb420560). If no memory can be allocated, NULL will be returned. The allocated memory is guaranteed to have a starting address which is a multiple of sizeof(void \*). If a bigger alignment is necessary then [sys\_heap\_aligned\_alloc()](#group__low__level__heap__allocator_1ga92a973158860c6863e1aba8516311076) should be used instead.

        Note

        The sys\_heap implementation is not internally synchronized. No two sys\_heap functions should operate on the same heap at the same time. All locking must be provided by the user.

        Parameters:
        :   - **heap** – Heap from which to allocate
            - **bytes** – Number of bytes requested

        Returns:
        :   Pointer to memory the caller can now use

    void \*sys\_heap\_aligned\_alloc(struct sys\_heap \*heap, size\_t align, size\_t bytes)
    :   Allocate aligned memory from a sys\_heap.

        Behaves in all ways like [sys\_heap\_alloc()](#group__low__level__heap__allocator_1ga6b8bdf02c9be5576fddbe711904a3aad), except that the returned memory (if available) will have a starting address in memory which is a multiple of the specified power-of-two alignment value in bytes. With align=0 this behaves exactly like [sys\_heap\_alloc()](#group__low__level__heap__allocator_1ga6b8bdf02c9be5576fddbe711904a3aad). The resulting memory can be returned to the heap using [sys\_heap\_free()](#group__low__level__heap__allocator_1gab654da64adf74e67ae12f263eb420560).

        Parameters:
        :   - **heap** – Heap from which to allocate
            - **align** – Alignment in bytes, must be a power of two
            - **bytes** – Number of bytes requested

        Returns:
        :   Pointer to memory the caller can now use

    void sys\_heap\_free(struct sys\_heap \*heap, void \*mem)
    :   Free memory into a sys\_heap.

        De-allocates a pointer to memory previously returned from sys\_heap\_alloc such that it can be used for other purposes. The caller must not use the memory region after entry to this function.

        Note

        The sys\_heap implementation is not internally synchronized. No two sys\_heap functions should operate on the same heap at the same time. All locking must be provided by the user.

        Parameters:
        :   - **heap** – Heap to which to return the memory
            - **mem** – A pointer previously returned from [sys\_heap\_alloc()](#group__low__level__heap__allocator_1ga6b8bdf02c9be5576fddbe711904a3aad)

    void \*sys\_heap\_aligned\_realloc(struct sys\_heap \*heap, void \*ptr, size\_t align, size\_t bytes)
    :   Expand the size of an existing allocation.

        Returns a pointer to a new memory region with the same contents, but a different allocated size. If the new allocation can be expanded in place, the pointer returned will be identical. Otherwise the data will be copies to a new block and the old one will be freed as per [sys\_heap\_free()](#group__low__level__heap__allocator_1gab654da64adf74e67ae12f263eb420560). If the specified size is smaller than the original, the block will be truncated in place and the remaining memory returned to the heap. If the allocation of a new block fails, then NULL will be returned and the old block will not be freed or modified.

        Parameters:
        :   - **heap** – Heap from which to allocate
            - **ptr** – Original pointer returned from a previous allocation
            - **align** – Alignment in bytes, must be a power of two
            - **bytes** – Number of bytes requested for the new block

        Returns:
        :   Pointer to memory the caller can now use, or NULL

    size\_t sys\_heap\_usable\_size(struct sys\_heap \*heap, void \*mem)
    :   Return allocated memory size.

        Returns the size, in bytes, of a block returned from a successful [sys\_heap\_alloc()](#group__low__level__heap__allocator_1ga6b8bdf02c9be5576fddbe711904a3aad) or sys\_heap\_alloc\_aligned() call. The value returned is the size of the heap-managed memory, which may be larger than the number of bytes requested due to allocation granularity. The heap code is guaranteed to make no access to this region of memory until a subsequent [sys\_heap\_free()](#group__low__level__heap__allocator_1gab654da64adf74e67ae12f263eb420560) on the same pointer.

        Parameters:
        :   - **heap** – Heap containing the block
            - **mem** – Pointer to memory allocated from this heap

        Returns:
        :   Size in bytes of the memory region

    bool sys\_heap\_validate(struct sys\_heap \*heap)
    :   Validate heap integrity.

        Validates the internal integrity of a sys\_heap. Intended for unit test and validation code, though potentially useful as a user API for applications with complicated runtime reliability requirements. Note: this cannot catch every possible error, but if it returns true then the heap is in a consistent state and can correctly handle any [sys\_heap\_alloc()](#group__low__level__heap__allocator_1ga6b8bdf02c9be5576fddbe711904a3aad) request and free any live pointer returned from a previous allocation.

        Parameters:
        :   - **heap** – Heap to validate

        Returns:
        :   true, if the heap is valid, otherwise false

    void sys\_heap\_stress(void \*(\*alloc\_fn)(void \*arg, size\_t bytes), void (\*free\_fn)(void \*arg, void \*p), void \*arg, size\_t total\_bytes, uint32\_t op\_count, void \*scratch\_mem, size\_t scratch\_bytes, int target\_percent, struct z\_heap\_stress\_result \*result)
    :   sys\_heap stress test rig

        Test rig for heap allocation validation. This will loop for *op\_count* cycles, in each iteration making a random choice to allocate or free a pointer of randomized (power law) size based on heuristics designed to keep the heap in a state where it is near *target\_percent* full. Allocation and free operations are provided by the caller as callbacks (i.e. this can in theory test any heap). Results, including counts of frees and successful/unsuccessful allocations, are returned via the *result* struct.

        Parameters:
        :   - **alloc\_fn** – Callback to perform an allocation. Passes back the *arg* parameter as a context handle.
            - **free\_fn** – Callback to perform a free of a pointer returned from *alloc*. Passes back the *arg* parameter as a context handle.
            - **arg** – Context handle to pass back to the callbacks
            - **total\_bytes** – Size of the byte array the heap was initialized in
            - **op\_count** – How many iterations to test
            - **scratch\_mem** – A pointer to scratch memory to be used by the test. Should be about 1/2 the size of the heap for tests that need to stress fragmentation.
            - **scratch\_bytes** – Size of the memory pointed to by *scratch\_mem*
            - **target\_percent** – Percentage fill value (1-100) to which the random allocation choices will seek. High values will result in significant allocation failures and a very fragmented heap.
            - **result** – Struct into which to store test results.

    void sys\_heap\_print\_info(struct sys\_heap \*heap, bool dump\_chunks)
    :   Print heap internal structure information to the console.

        Print information on the heap structure such as its size, chunk buckets, chunk list and some statistics for debugging purpose.

        Parameters:
        :   - **heap** – Heap to print information about
            - **dump\_chunks** – True to print the entire heap chunk list

*group* Multi-Heap Wrapper
:   Typedefs

    typedef void \*(\*sys\_multi\_heap\_fn\_t)(struct [sys\_multi\_heap](#c.sys_multi_heap) \*mheap, void \*cfg, size\_t align, size\_t size)
    :   Multi-heap choice function.

        This is a user-provided functions whose responsibility is selecting a specific sys\_heap backend based on the opaque cfg value, which is specified by the user as an argument to [sys\_multi\_heap\_alloc()](#group__multi__heap__wrapper_1ga050d7499b982ed62f85d5fc15f79548b), and performing the allocation on behalf of the caller. The callback is free to choose any registered heap backend to perform the allocation, and may choose to pad the user-provided values as needed, and to use an aligned allocation where required by the specified configuration.

        NULL may be returned, which will cause the allocation to fail and a NULL reported to the calling code.

        Param mheap:
        :   Multi-heap structure.

        Param cfg:
        :   An opaque user-provided value. It may be interpreted in any way by the application

        Param align:
        :   Alignment of requested memory (or zero for no alignment)

        Param size:
        :   The user-specified allocation size in bytes

        Return:
        :   A pointer to the allocated memory

    Functions

    void sys\_multi\_heap\_init(struct [sys\_multi\_heap](#c.sys_multi_heap) \*heap, [sys\_multi\_heap\_fn\_t](#c.sys_multi_heap_fn_t) choice\_fn)
    :   Initialize multi-heap.

        Initialize a [sys\_multi\_heap](#structsys__multi__heap) struct with the specified choice function. Note that individual heaps must be added later with sys\_multi\_heap\_add\_heap so that the heap bounds can be tracked by the multi heap code.

        Note

        In general a multiheap is likely to be instantiated semi-statically from system configuration (for example, via linker-provided bounds on available memory in different regions, or from devicetree definitions of hardware-provided addressable memory, etc…). The general expectation is that a soc- or board-level platform device will be initialized at system boot from these upstream configuration sources and not that an application will assemble a multi-heap on its own.

        Parameters:
        :   - **heap** – A [sys\_multi\_heap](#structsys__multi__heap) to initialize
            - **choice\_fn** – A [sys\_multi\_heap\_fn\_t](#group__multi__heap__wrapper_1ga2d8ac07e590ef36ba6f35ae88235564e) callback used to select heaps at allocation time

    void sys\_multi\_heap\_add\_heap(struct [sys\_multi\_heap](#c.sys_multi_heap) \*mheap, struct sys\_heap \*heap, void \*user\_data)
    :   Add sys\_heap to multi heap.

        This adds a known sys\_heap backend to an existing multi heap, allowing the multi heap internals to track the bounds of the heap and determine which heap (if any) from which a freed block was allocated.

        Parameters:
        :   - **mheap** – A [sys\_multi\_heap](#structsys__multi__heap) to which to add a heap
            - **heap** – The heap to add
            - **user\_data** – pointer to any data for the heap

    void \*sys\_multi\_heap\_alloc(struct [sys\_multi\_heap](#c.sys_multi_heap) \*mheap, void \*cfg, size\_t bytes)
    :   Allocate memory from multi heap.

        Just as for [sys\_heap\_alloc()](#group__low__level__heap__allocator_1ga6b8bdf02c9be5576fddbe711904a3aad), allocates a block of memory of the specified size in bytes. Takes an opaque configuration pointer passed to the multi heap choice function, which is used by integration code to choose a heap backend.

        Parameters:
        :   - **mheap** – Multi heap pointer
            - **cfg** – Opaque configuration parameter, as for [sys\_multi\_heap\_fn\_t](#group__multi__heap__wrapper_1ga2d8ac07e590ef36ba6f35ae88235564e)
            - **bytes** – Requested size of the allocation, in bytes

        Returns:
        :   A valid pointer to heap memory, or NULL if no memory is available

    void \*sys\_multi\_heap\_aligned\_alloc(struct [sys\_multi\_heap](#c.sys_multi_heap) \*mheap, void \*cfg, size\_t align, size\_t bytes)
    :   Allocate aligned memory from multi heap.

        Just as for [sys\_multi\_heap\_alloc()](#group__multi__heap__wrapper_1ga050d7499b982ed62f85d5fc15f79548b), allocates a block of memory of the specified size in bytes. Takes an additional parameter specifying a power of two alignment, in bytes.

        Parameters:
        :   - **mheap** – Multi heap pointer
            - **cfg** – Opaque configuration parameter, as for [sys\_multi\_heap\_fn\_t](#group__multi__heap__wrapper_1ga2d8ac07e590ef36ba6f35ae88235564e)
            - **align** – Power of two alignment for the returned pointer, in bytes
            - **bytes** – Requested size of the allocation, in bytes

        Returns:
        :   A valid pointer to heap memory, or NULL if no memory is available

    const struct [sys\_multi\_heap\_rec](#c.sys_multi_heap_rec) \*sys\_multi\_heap\_get\_heap(const struct [sys\_multi\_heap](#c.sys_multi_heap) \*mheap, void \*addr)
    :   Get a specific heap for provided address.

        Finds a single system heap (with user\_data) controlling the provided pointer

        Parameters:
        :   - **mheap** – Multi heap pointer
            - **addr** – address to be found, must be a pointer to a block allocated by sys\_multi\_heap\_alloc

        Returns:
        :   0 multi\_heap\_rec pointer to a structure to be filled with return data or NULL if the heap has not been found

    void sys\_multi\_heap\_free(struct [sys\_multi\_heap](#c.sys_multi_heap) \*mheap, void \*block)
    :   Free memory allocated from multi heap.

        Returns the specified block, which must be the return value of a previously successful [sys\_multi\_heap\_alloc()](#group__multi__heap__wrapper_1ga050d7499b982ed62f85d5fc15f79548b) or [sys\_multi\_heap\_aligned\_alloc()](#group__multi__heap__wrapper_1ga9f958dbfa86e12236b8e356375b8d04c) call, to the heap backend from which it was allocated.

        Accepts NULL as a block parameter, which is specified to have no effect.

        Parameters:
        :   - **mheap** – Multi heap pointer
            - **block** – Block to free, must be a pointer to a block allocated by sys\_multi\_heap\_alloc

    struct sys\_multi\_heap\_rec
    :   *#include <multi\_heap.h>*

    struct sys\_multi\_heap
    :   *#include <multi\_heap.h>*

## Heap listener

*group* Heap Listener APIs
:   Defines

    HEAP\_ID\_FROM\_POINTER(heap\_pointer)
    :   Construct heap identifier from heap pointer.

        Construct a heap identifier from a pointer to the heap object, such as sys\_heap.

        Parameters:
        :   - **heap\_pointer** – Pointer to the heap object

    HEAP\_ID\_LIBC
    :   Libc heap identifier.

        Identifier of the global libc heap.

    HEAP\_LISTENER\_ALLOC\_DEFINE(name, \_heap\_id, \_alloc\_cb)
    :   Define heap event listener node for allocation event.

        Sample usage:

        ```text
        void on_heap_alloc(uintptr_t heap_id, void *mem, size_t bytes)
        {
          LOG_INF("Memory allocated at %p, size %ld", mem, bytes);
        }

        HEAP_LISTENER_ALLOC_DEFINE(my_listener, HEAP_ID_LIBC, on_heap_alloc);
        ```

        Parameters:
        :   - **name** – Name of the heap event listener object
            - **\_heap\_id** – Identifier of the heap to be listened
            - **\_alloc\_cb** – Function to be called for allocation event

    HEAP\_LISTENER\_FREE\_DEFINE(name, \_heap\_id, \_free\_cb)
    :   Define heap event listener node for free event.

        Sample usage:

        ```text
        void on_heap_free(uintptr_t heap_id, void *mem, size_t bytes)
        {
          LOG_INF("Memory freed at %p, size %ld", mem, bytes);
        }

        HEAP_LISTENER_FREE_DEFINE(my_listener, HEAP_ID_LIBC, on_heap_free);
        ```

        Parameters:
        :   - **name** – Name of the heap event listener object
            - **\_heap\_id** – Identifier of the heap to be listened
            - **\_free\_cb** – Function to be called for free event

    HEAP\_LISTENER\_RESIZE\_DEFINE(name, \_heap\_id, \_resize\_cb)
    :   Define heap event listener node for resize event.

        Sample usage:

        ```text
        void on_heap_resized(uintptr_t heap_id, void *old_heap_end, void *new_heap_end)
        {
          LOG_INF("Libc heap end moved from %p to %p", old_heap_end, new_heap_end);
        }

        HEAP_LISTENER_RESIZE_DEFINE(my_listener, HEAP_ID_LIBC, on_heap_resized);
        ```

        Parameters:
        :   - **name** – Name of the heap event listener object
            - **\_heap\_id** – Identifier of the heap to be listened
            - **\_resize\_cb** – Function to be called when the listened heap is resized

    Typedefs

    typedef void (\*heap\_listener\_resize\_cb\_t)(uintptr\_t heap\_id, void \*old\_heap\_end, void \*new\_heap\_end)
    :   Callback used when heap is resized.

        Note

        Minimal C library does not emit this event.

        Param heap\_id:
        :   Identifier of heap being resized

        Param old\_heap\_end:
        :   Pointer to end of heap before resize

        Param new\_heap\_end:
        :   Pointer to end of heap after resize

    typedef void (\*heap\_listener\_alloc\_cb\_t)(uintptr\_t heap\_id, void \*mem, size\_t bytes)
    :   Callback used when there is heap allocation.

        Note

        Heaps managed by libraries outside of code in Zephyr main code repository may not emit this event.

        Note

        The number of bytes allocated may not match exactly to the request to the allocation function. Internal mechanism of the heap may allocate more than requested.

        Param heap\_id:
        :   Heap identifier

        Param mem:
        :   Pointer to the allocated memory

        Param bytes:
        :   Size of allocated memory

    typedef void (\*heap\_listener\_free\_cb\_t)(uintptr\_t heap\_id, void \*mem, size\_t bytes)
    :   Callback used when memory is freed from heap.

        Note

        Heaps managed by libraries outside of code in Zephyr main code repository may not emit this event.

        Note

        The number of bytes freed may not match exactly to the request to the allocation function. Internal mechanism of the heap dictates how memory is allocated or freed.

        Param heap\_id:
        :   Heap identifier

        Param mem:
        :   Pointer to the freed memory

        Param bytes:
        :   Size of freed memory

    Enums

    enum heap\_event\_types
    :   *Values:*

        enumerator HEAP\_EVT\_UNKNOWN = 0

        enumerator HEAP\_RESIZE

        enumerator HEAP\_ALLOC

        enumerator HEAP\_FREE

        enumerator HEAP\_REALLOC

        enumerator HEAP\_MAX\_EVENTS

    Functions

    void heap\_listener\_register(struct [heap\_listener](#c.heap_listener) \*listener)
    :   Register heap event listener.

        Add the listener to the global list of heap listeners that can be notified by different heap implementations upon certain events related to the heap usage.

        Parameters:
        :   - **listener** – Pointer to the [heap\_listener](#structheap__listener) object

    void heap\_listener\_unregister(struct [heap\_listener](#c.heap_listener) \*listener)
    :   Unregister heap event listener.

        Remove the listener from the global list of heap listeners that can be notified by different heap implementations upon certain events related to the heap usage.

        Parameters:
        :   - **listener** – Pointer to the [heap\_listener](#structheap__listener) object

    void heap\_listener\_notify\_alloc(uintptr\_t heap\_id, void \*mem, size\_t bytes)
    :   Notify listeners of heap allocation event.

        Notify registered heap event listeners with matching heap identifier that an allocation has been done on heap

        Parameters:
        :   - **heap\_id** – Heap identifier
            - **mem** – Pointer to the allocated memory
            - **bytes** – Size of allocated memory

    void heap\_listener\_notify\_free(uintptr\_t heap\_id, void \*mem, size\_t bytes)
    :   Notify listeners of heap free event.

        Notify registered heap event listeners with matching heap identifier that memory is freed on heap

        Parameters:
        :   - **heap\_id** – Heap identifier
            - **mem** – Pointer to the freed memory
            - **bytes** – Size of freed memory

    void heap\_listener\_notify\_resize(uintptr\_t heap\_id, void \*old\_heap\_end, void \*new\_heap\_end)
    :   Notify listeners of heap resize event.

        Notify registered heap event listeners with matching heap identifier that the heap has been resized.

        Parameters:
        :   - **heap\_id** – Heap identifier
            - **old\_heap\_end** – Address of the heap end before the change
            - **new\_heap\_end** – Address of the heap end after the change

    struct heap\_listener
    :   *#include <heap\_listener.h>*

        Public Members

        [sys\_snode\_t](../data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Singly linked list node.

        uintptr\_t heap\_id
        :   Identifier of the heap whose events are listened.

            It can be a heap pointer, if the heap is represented as an object, or 0 in the case of the global libc heap.

        enum [heap\_event\_types](#c.heap_event_types) event
        :   The heap event to be notified.
