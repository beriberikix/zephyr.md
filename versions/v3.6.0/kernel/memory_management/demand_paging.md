---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/memory_management/demand_paging.html
original_path: kernel/memory_management/demand_paging.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Demand Paging

Demand paging provides a mechanism where data is only brought into physical
memory as required by current execution context. The physical memory is
conceptually divided in page-sized page frames as regions to hold data.

- When the processor tries to access data and the data page exists in
  one of the page frames, the execution continues without any interruptions.
- When the processor tries to access the data page that does not exist
  in any page frames, a page fault occurs. The paging code then brings in
  the corresponding data page from backing store into physical memory if
  there is a free page frame. If there is no more free page frames,
  the eviction algorithm is invoked to select a data page to be paged out,
  thus freeing up a page frame for new data to be paged in. If this data
  page has been modified after it is first paged in, the data will be
  written back into the backing store. If no modifications is done or
  after written back into backing store, the data page is now considered
  paged out and the corresponding page frame is now free. The paging code
  then invokes the backing store to page in the data page corresponding to
  the location of the requested data. The backing store copies that data
  page into the free page frame. Now the data page is in physical memory
  and execution can continue.

There are functions where paging in and out can be invoked manually
using [`k_mem_page_in()`](#c.k_mem_page_in) and [`k_mem_page_out()`](#c.k_mem_page_out).
[`k_mem_page_in()`](#c.k_mem_page_in) can be used to page in data pages
in anticipation that they are required in the near future. This is used to
minimize number of page faults as these data pages are already in physical
memory, and thus minimizing latency. [`k_mem_page_out()`](#c.k_mem_page_out) can be
used to page out data pages where they are not going to be accessed for
a considerable amount of time. This frees up page frames so that the next
page in can be executed faster as the paging code does not need to invoke
the eviction algorithm.

## Terminology

Data Page
:   A data page is a page-sized region of data. It may exist in a page frame,
    or be paged out to some backing store. Its location can always be looked
    up in the CPU’s page tables (or equivalent) by virtual address.
    The data type will always be `void *` or in some cases `uint8_t *`
    when doing pointer arithmetic.

Page Frame
:   A page frame is a page-sized physical memory region in RAM. It is a
    container where a data page may be placed. It is always referred to by
    physical address. Zephyr has a convention of using `uintptr_t` for physical
    addresses. For every page frame, a `struct z_page_frame` is instantiated to
    store metadata. Flags for each page frame:

    - `Z_PAGE_FRAME_PINNED` indicates a page frame is pinned in memory
      and should never be paged out.
    - `Z_PAGE_FRAME_RESERVED` indicates a physical page reserved by hardware
      and should not be used at all.
    - `Z_PAGE_FRAME_MAPPED` is set when a physical page is mapped to
      virtual memory address.
    - `Z_PAGE_FRAME_BUSY` indicates a page frame is currently involved in
      a page-in/out operation.
    - `Z_PAGE_FRAME_BACKED` indicates a page frame has a clean copy
      in the backing store.

Z\_SCRATCH\_PAGE
:   The virtual address of a special page provided to the backing store to:
    \* Copy a data page from `Z_SCRATCH_PAGE` to the specified location; or,
    \* Copy a data page from the provided location to `Z_SCRATCH_PAGE`.
    This is used as an intermediate page for page in/out operations. This
    scratch needs to be mapped read/write for backing store code to access.
    However the data page itself may only be mapped as read-only in virtual
    address space. If this page is provided as-is to backing store,
    the data page must be re-mapped as read/write which has security
    implications as the data page is no longer read-only to other parts of
    the application.

## Paging Statistics

Paging statistics can be obtained via various function calls when
[`CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS`](../../kconfig.md#CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS "CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS") is enabled:

- Overall statistics via [`k_mem_paging_stats_get()`](#c.k_mem_paging_stats_get)
- Per-thread statistics via [`k_mem_paging_thread_stats_get()`](#c.k_mem_paging_thread_stats_get)
  if [`CONFIG_DEMAND_PAGING_THREAD_STATS`](../../kconfig.md#CONFIG_DEMAND_PAGING_THREAD_STATS "CONFIG_DEMAND_PAGING_THREAD_STATS") is enabled
- Execution time histogram can be obtained when
  [`CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM`](../../kconfig.md#CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM "CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM") is enabled, and
  [`CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS`](../../kconfig.md#CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS "CONFIG_DEMAND_PAGING_TIMING_HISTOGRAM_NUM_BINS") is defined.
  Note that the timing is highly dependent on the architecture,
  SoC or board. It is highly recommended that
  `k_mem_paging_eviction_histogram_bounds[]` and
  `k_mem_paging_backing_store_histogram_bounds[]`
  be defined for a particular application.

  - Execution time histogram of eviction algorithm via
    [`k_mem_paging_histogram_eviction_get()`](#c.k_mem_paging_histogram_eviction_get)
  - Execution time histogram of backing store doing page-in via
    [`k_mem_paging_histogram_backing_store_page_in_get()`](#c.k_mem_paging_histogram_backing_store_page_in_get)
  - Execution time histogram of backing store doing page-out via
    [`k_mem_paging_histogram_backing_store_page_out_get()`](#c.k_mem_paging_histogram_backing_store_page_out_get)

## Eviction Algorithm

The eviction algorithm is used to determine which data page and its
corresponding page frame can be paged out to free up a page frame
for the next page in operation. There are two functions which are
called from the kernel paging code:

- [`k_mem_paging_eviction_init()`](#c.k_mem_paging_eviction_init) is called to initialize
  the eviction algorithm. This is called at `POST_KERNEL`.
- [`k_mem_paging_eviction_select()`](#c.k_mem_paging_eviction_select) is called to select
  a data page to evict. A function argument `dirty` is written to
  signal the caller whether the selected data page has been modified
  since it is first paged in. If the `dirty` bit is returned
  as set, the paging code signals to the backing store to write
  the data page back into storage (thus updating its content).
  The function returns a pointer to the page frame corresponding to
  the selected data page.

Currently, a NRU (Not-Recently-Used) eviction algorithm has been
implemented as a sample. This is a very simple algorithm which
ranks each data page on whether they have been accessed and modified.
The selection is based on this ranking.

To implement a new eviction algorithm, the two functions mentioned
above must be implemented.

## Backing Store

Backing store is responsible for paging in/out data page between
their corresponding page frames and storage. These are the functions
which must be implemented:

- [`k_mem_paging_backing_store_init()`](#c.k_mem_paging_backing_store_init) is called to
  initialized the backing store at `POST_KERNEL`.
- [`k_mem_paging_backing_store_location_get()`](#c.k_mem_paging_backing_store_location_get) is called to
  reserve a backing store location so a data page can be paged out.
  This `location` token is passed to
  [`k_mem_paging_backing_store_page_out()`](#c.k_mem_paging_backing_store_page_out) to perform actual
  page out operation.
- [`k_mem_paging_backing_store_location_free()`](#c.k_mem_paging_backing_store_location_free) is called to
  free a backing store location (the `location` token) which can
  then be used for subsequent page out operation.
- [`k_mem_paging_backing_store_page_in()`](#c.k_mem_paging_backing_store_page_in) copies a data page
  from the backing store location associated with the provided
  `location` token to the page pointed by `Z_SCRATCH_PAGE`.
- [`k_mem_paging_backing_store_page_out()`](#c.k_mem_paging_backing_store_page_out) copies a data page
  from `Z_SCRATCH_PAGE` to the backing store location associated
  with the provided `location` token.
- [`k_mem_paging_backing_store_page_finalize()`](#c.k_mem_paging_backing_store_page_finalize) is invoked after
  [`k_mem_paging_backing_store_page_in()`](#c.k_mem_paging_backing_store_page_in) so that the page frame
  struct may be updated for internal accounting. This can be
  a no-op.

To implement a new backing store, the functions mentioned above
must be implemented.
[`k_mem_paging_backing_store_page_finalize()`](#c.k_mem_paging_backing_store_page_finalize) can be an empty
function if so desired.

## API Reference

*group* mem-demand-paging
:   Functions

    int k\_mem\_page\_out(void \*addr, size\_t size)
    :   Evict a page-aligned virtual memory region to the backing store.

        Useful if it is known that a memory region will not be used for some time. All the data pages within the specified region will be evicted to the backing store if they weren’t already, with their associated page frames marked as available for mappings or page-ins.

        None of the associated page frames mapped to the provided region should be pinned.

        Note that there are no guarantees how long these pages will be evicted, they could take page faults immediately.

        If CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ is enabled, this function may not be called by ISRs as the backing store may be in-use.

        Parameters:
        :   - **addr** – Base page-aligned virtual address
            - **size** – Page-aligned data region size

        Return values:
        :   - **0** – Success
            - **-ENOMEM** – Insufficient space in backing store to satisfy request. The region may be partially paged out.

    void k\_mem\_page\_in(void \*addr, size\_t size)
    :   Load a virtual data region into memory.

        After the function completes, all the page frames associated with this function will be paged in. However, they are not guaranteed to stay there. This is useful if the region is known to be used soon.

        If CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ is enabled, this function may not be called by ISRs as the backing store may be in-use.

        Parameters:
        :   - **addr** – Base page-aligned virtual address
            - **size** – Page-aligned data region size

    void k\_mem\_pin(void \*addr, size\_t size)
    :   Pin an aligned virtual data region, paging in as necessary.

        After the function completes, all the page frames associated with this region will be resident in memory and pinned such that they stay that way. This is a stronger version of z\_mem\_page\_in().

        If CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ is enabled, this function may not be called by ISRs as the backing store may be in-use.

        Parameters:
        :   - **addr** – Base page-aligned virtual address
            - **size** – Page-aligned data region size

    void k\_mem\_unpin(void \*addr, size\_t size)
    :   Un-pin an aligned virtual data region.

        After the function completes, all the page frames associated with this region will be no longer marked as pinned. This does not evict the region, follow this with z\_mem\_page\_out() if you need that.

        Parameters:
        :   - **addr** – Base page-aligned virtual address
            - **size** – Page-aligned data region size

    void k\_mem\_paging\_stats\_get(struct [k\_mem\_paging\_stats\_t](#c.k_mem_paging_stats_t) \*stats)
    :   Get the paging statistics since system startup.

        This populates the paging statistics struct being passed in as argument.

        Parameters:
        :   - **stats** – **[inout]** Paging statistics struct to be filled.

    void k\_mem\_paging\_thread\_stats\_get(struct [k\_thread](../services/threads/index.md#c.k_thread "k_thread") \*thread, struct [k\_mem\_paging\_stats\_t](#c.k_mem_paging_stats_t) \*stats)
    :   Get the paging statistics since system startup for a thread.

        This populates the paging statistics struct being passed in as argument for a particular thread.

        Parameters:
        :   - **thread** – **[in]** Thread
            - **stats** – **[inout]** Paging statistics struct to be filled.

    void k\_mem\_paging\_histogram\_eviction\_get(struct [k\_mem\_paging\_histogram\_t](#c.k_mem_paging_histogram_t) \*hist)
    :   Get the eviction timing histogram.

        This populates the timing histogram struct being passed in as argument.

        Parameters:
        :   - **hist** – **[inout]** Timing histogram struct to be filled.

    void k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get(struct [k\_mem\_paging\_histogram\_t](#c.k_mem_paging_histogram_t) \*hist)
    :   Get the backing store page-in timing histogram.

        This populates the timing histogram struct being passed in as argument.

        Parameters:
        :   - **hist** – **[inout]** Timing histogram struct to be filled.

    void k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get(struct [k\_mem\_paging\_histogram\_t](#c.k_mem_paging_histogram_t) \*hist)
    :   Get the backing store page-out timing histogram.

        This populates the timing histogram struct being passed in as argument.

        Parameters:
        :   - **hist** – **[inout]** Timing histogram struct to be filled.

    struct k\_mem\_paging\_stats\_t
    :   *#include <demand\_paging.h>*

        Paging Statistics.

        Public Members

        unsigned long cnt
        :   Number of page faults.

        unsigned long irq\_locked
        :   Number of page faults with IRQ locked.

        unsigned long irq\_unlocked
        :   Number of page faults with IRQ unlocked.

        unsigned long in\_isr
        :   Number of page faults while in ISR.

        unsigned long clean
        :   Number of clean pages selected for eviction.

        unsigned long dirty
        :   Number of dirty pages selected for eviction.

    struct k\_mem\_paging\_histogram\_t
    :   *#include <demand\_paging.h>*

        Paging Statistics Histograms.

### Eviction Algorithm APIs

*group* mem-demand-paging-eviction
:   Eviction algorithm APIs.

    Functions

    struct z\_page\_frame \*k\_mem\_paging\_eviction\_select(bool \*dirty)
    :   Select a page frame for eviction.

        The kernel will invoke this to choose a page frame to evict if there are no free page frames.

        This function will never be called before the initial [k\_mem\_paging\_eviction\_init()](#group__mem-demand-paging-eviction_1ga68dcfc0e5374de2c8ad7b9fe4e65c4f4).

        This function is invoked with interrupts locked.

        Parameters:
        :   - **dirty** – **[out]** Whether the page to evict is dirty

        Returns:
        :   The page frame to evict

    void k\_mem\_paging\_eviction\_init(void)
    :   Initialization function.

        Called at POST\_KERNEL to perform any necessary initialization tasks for the eviction algorithm. [k\_mem\_paging\_eviction\_select()](#group__mem-demand-paging-eviction_1ga12641d53942529c7d7364c08473a6eca) is guaranteed to never be called until this has returned, and this will only be called once.

### Backing Store APIs

*group* mem-demand-paging-backing-store
:   Backing store APIs.

    Functions

    int k\_mem\_paging\_backing\_store\_location\_get(struct z\_page\_frame \*pf, uintptr\_t \*location, bool page\_fault)
    :   Reserve or fetch a storage location for a data page loaded into a page frame.

        The returned location token must be unique to the mapped virtual address. This location will be used in the backing store to page out data page contents for later retrieval. The location value must be page-aligned.

        This function may be called multiple times on the same data page. If its page frame has its Z\_PAGE\_FRAME\_BACKED bit set, it is expected to return the previous backing store location for the data page containing a cached clean copy. This clean copy may be updated on page-out, or used to discard clean pages without needing to write out their contents.

        If the backing store is full, some other backing store location which caches a loaded data page may be selected, in which case its associated page frame will have the Z\_PAGE\_FRAME\_BACKED bit cleared (as it is no longer cached).

        pf->addr will indicate the virtual address the page is currently mapped to. Large, sparse backing stores which can contain the entire address space may simply generate location tokens purely as a function of pf->addr with no other management necessary.

        This function distinguishes whether it was called on behalf of a page fault. A free backing store location must always be reserved in order for page faults to succeed. If the page\_fault parameter is not set, this function should return -ENOMEM even if one location is available.

        This function is invoked with interrupts locked.

        Parameters:
        :   - **pf** – Virtual address to obtain a storage location
            - **location** – **[out]** storage location token
            - **page\_fault** – Whether this request was for a page fault

        Returns:
        :   0 Success

        Returns:
        :   -ENOMEM Backing store is full

    void k\_mem\_paging\_backing\_store\_location\_free(uintptr\_t location)
    :   Free a backing store location.

        Any stored data may be discarded, and the location token associated with this address may be re-used for some other data page.

        This function is invoked with interrupts locked.

        Parameters:
        :   - **location** – Location token to free

    void k\_mem\_paging\_backing\_store\_page\_out(uintptr\_t location)
    :   Copy a data page from Z\_SCRATCH\_PAGE to the specified location.

        Immediately before this is called, Z\_SCRATCH\_PAGE will be mapped read-write to the intended source page frame for the calling context.

        Calls to this and [k\_mem\_paging\_backing\_store\_page\_in()](#group__mem-demand-paging-backing-store_1ga9becb4908cc7840ece93a2360692962d) will always be serialized, but interrupts may be enabled.

        Parameters:
        :   - **location** – Location token for the data page, for later retrieval

    void k\_mem\_paging\_backing\_store\_page\_in(uintptr\_t location)
    :   Copy a data page from the provided location to Z\_SCRATCH\_PAGE.

        Immediately before this is called, Z\_SCRATCH\_PAGE will be mapped read-write to the intended destination page frame for the calling context.

        Calls to this and [k\_mem\_paging\_backing\_store\_page\_out()](#group__mem-demand-paging-backing-store_1ga51f663e0a8c31367082e78097359af6d) will always be serialized, but interrupts may be enabled.

        Parameters:
        :   - **location** – Location token for the data page

    void k\_mem\_paging\_backing\_store\_page\_finalize(struct z\_page\_frame \*pf, uintptr\_t location)
    :   Update internal accounting after a page-in.

        This is invoked after [k\_mem\_paging\_backing\_store\_page\_in()](#group__mem-demand-paging-backing-store_1ga9becb4908cc7840ece93a2360692962d) and interrupts have been\* re-locked, making it safe to access the z\_page\_frame data. The location value will be the same passed to [k\_mem\_paging\_backing\_store\_page\_in()](#group__mem-demand-paging-backing-store_1ga9becb4908cc7840ece93a2360692962d).

        The primary use-case for this is to update custom fields for the backing store in the page frame, to reflect where the data should be evicted to if it is paged out again. This may be a no-op in some implementations.

        If the backing store caches paged-in data pages, this is the appropriate time to set the Z\_PAGE\_FRAME\_BACKED bit. The kernel only skips paging out clean data pages if they are noted as clean in the page tables and the Z\_PAGE\_FRAME\_BACKED bit is set in their associated page frame.

        Parameters:
        :   - **pf** – Page frame that was loaded in
            - **location** – Location of where the loaded data page was retrieved

    void k\_mem\_paging\_backing\_store\_init(void)
    :   Backing store initialization function.

        The implementation may expect to receive page in/out calls as soon as this returns, but not before that. Called at POST\_KERNEL.

        This function is expected to do two things:

        - Initialize any internal data structures and accounting for the backing store.
        - If the backing store already contains all or some loaded kernel data pages at boot time, Z\_PAGE\_FRAME\_BACKED should be appropriately set for their associated page frames, and any internal accounting set up appropriately.
