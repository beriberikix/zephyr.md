---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/memory_management/demand_paging.html
original_path: kernel/memory_management/demand_paging.html
---

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
using [`k_mem_page_in()`](../../doxygen/html/group__mem-demand-paging.md#gab36c36a4e230677d2090514f7a34b408) and [`k_mem_page_out()`](../../doxygen/html/group__mem-demand-paging.md#ga0b18037209b4d8b5964bd9a1d760f703).
[`k_mem_page_in()`](../../doxygen/html/group__mem-demand-paging.md#gab36c36a4e230677d2090514f7a34b408) can be used to page in data pages
in anticipation that they are required in the near future. This is used to
minimize number of page faults as these data pages are already in physical
memory, and thus minimizing latency. [`k_mem_page_out()`](../../doxygen/html/group__mem-demand-paging.md#ga0b18037209b4d8b5964bd9a1d760f703) can be
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
    addresses. For every page frame, a `struct k_mem_page_frame` is instantiated to
    store metadata. Flags for each page frame:

    - `K_MEM_PAGE_FRAME_FREE` indicates a page frame is unused and on the list of
      free page frames. When this flag is set, none of the other flags are
      meaningful and they must not be modified.
    - `K_MEM_PAGE_FRAME_PINNED` indicates a page frame is pinned in memory
      and should never be paged out.
    - `K_MEM_PAGE_FRAME_RESERVED` indicates a physical page reserved by hardware
      and should not be used at all.
    - `K_MEM_PAGE_FRAME_MAPPED` is set when a physical page is mapped to
      virtual memory address.
    - `K_MEM_PAGE_FRAME_BUSY` indicates a page frame is currently involved in
      a page-in/out operation.
    - `K_MEM_PAGE_FRAME_BACKED` indicates a page frame has a clean copy
      in the backing store.

K\_MEM\_SCRATCH\_PAGE
:   The virtual address of a special page provided to the backing store to:
    \* Copy a data page from `k_MEM_SCRATCH_PAGE` to the specified location; or,
    \* Copy a data page from the provided location to `K_MEM_SCRATCH_PAGE`.
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

- Overall statistics via [`k_mem_paging_stats_get()`](../../doxygen/html/group__mem-demand-paging.md#ga52ad88e0c0eed2aa27331bfd4707b7ec)
- Per-thread statistics via [`k_mem_paging_thread_stats_get()`](../../doxygen/html/group__mem-demand-paging.md#gafad6b39cb2faf3bb416cd4d3faaa8d8c)
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
    [`k_mem_paging_histogram_eviction_get()`](../../doxygen/html/group__mem-demand-paging.md#gaec64d019d819b00c7bc3804aac269199)
  - Execution time histogram of backing store doing page-in via
    [`k_mem_paging_histogram_backing_store_page_in_get()`](../../doxygen/html/group__mem-demand-paging.md#ga1da0a643e8f85f98e29288e441a37dfa)
  - Execution time histogram of backing store doing page-out via
    [`k_mem_paging_histogram_backing_store_page_out_get()`](../../doxygen/html/group__mem-demand-paging.md#gae4f80d14f88a46ddb9aeb7afba861864)

## Eviction Algorithm

The eviction algorithm is used to determine which data page and its
corresponding page frame can be paged out to free up a page frame
for the next page in operation. There are four functions which are
called from the kernel paging code:

- [`k_mem_paging_eviction_init()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4) is called to initialize
  the eviction algorithm. This is called at `POST_KERNEL`.
- [`k_mem_paging_eviction_add()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga6bb19be3098cc839ae3f6e9528598867) is called each time a data page becomes
  eligible for future eviction.
- [`k_mem_paging_eviction_remove()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga16a4df904cc7a9641d06741ed589949d) is called when a data page is no
  longer eligible for eviction. This may happen if the given data page becomes
  pinned, gets unmapped or is about to be evicted.
- [`k_mem_paging_eviction_select()`](../../doxygen/html/group__mem-demand-paging-eviction.md#gaadbb4eb56c239f800daf995e6673ae1d) is called to select
  a data page to evict. A function argument `dirty` is written to
  signal the caller whether the selected data page has been modified
  since it is first paged in. If the `dirty` bit is returned
  as set, the paging code signals to the backing store to write
  the data page back into storage (thus updating its content).
  The function returns a pointer to the page frame corresponding to
  the selected data page.

There is one additional function which is called by the architecture’s memory
management code to flag data pages when they trigger an access fault:
[`k_mem_paging_eviction_accessed()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga228747c10bfd8816aec59fddf0e3a224). This is used by the LRU algorithm
to requeue “used” pages.

Two eviction algorithms are currently available:

- An NRU (Not-Recently-Used) eviction algorithm has been implemented as a
  sample. This is a very simple algorithm which ranks data pages on whether
  they have been accessed and modified. The selection is based on this ranking.
- An LRU (Least-Recently-Used) eviction algorithm is also available. It is
  based on a sorted queue of data pages. The LRU code is more complex compared
  to the NRU code but also considerably more efficient. This is recommended for
  production use.

To implement a new eviction algorithm, [`k_mem_paging_eviction_init()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)
and [`k_mem_paging_eviction_select()`](../../doxygen/html/group__mem-demand-paging-eviction.md#gaadbb4eb56c239f800daf995e6673ae1d) must be implemented.
If [`CONFIG_EVICTION_TRACKING`](../../kconfig.md#CONFIG_EVICTION_TRACKING "CONFIG_EVICTION_TRACKING") is enabled for an algorithm,
these additional functions must also be implemented,
[`k_mem_paging_eviction_add()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga6bb19be3098cc839ae3f6e9528598867), [`k_mem_paging_eviction_remove()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga16a4df904cc7a9641d06741ed589949d),
[`k_mem_paging_eviction_accessed()`](../../doxygen/html/group__mem-demand-paging-eviction.md#ga228747c10bfd8816aec59fddf0e3a224).

## Backing Store

Backing store is responsible for paging in/out data page between
their corresponding page frames and storage. These are the functions
which must be implemented:

- [`k_mem_paging_backing_store_init()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga7ff441f23619b2678bfb72559d5bd592) is called to
  initialized the backing store at `POST_KERNEL`.
- [`k_mem_paging_backing_store_location_get()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga1192487fdc8d63c025de42162fb204cd) is called to
  reserve a backing store location so a data page can be paged out.
  This `location` token is passed to
  [`k_mem_paging_backing_store_page_out()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga51f663e0a8c31367082e78097359af6d) to perform actual
  page out operation.
- [`k_mem_paging_backing_store_location_free()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga6ad421ad5671d9df3d96e03361f672e8) is called to
  free a backing store location (the `location` token) which can
  then be used for subsequent page out operation.
- [`k_mem_paging_backing_store_location_query()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga25debe925b369765ecd5bd7777ce32d0) is called to obtain
  the `location` token corresponding to storage content to be virtually
  mapped and paged-in on demand. Most useful with
  [`CONFIG_DEMAND_MAPPING`](../../kconfig.md#CONFIG_DEMAND_MAPPING "CONFIG_DEMAND_MAPPING").
- [`k_mem_paging_backing_store_page_in()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga9becb4908cc7840ece93a2360692962d) copies a data page
  from the backing store location associated with the provided
  `location` token to the page pointed by `K_MEM_SCRATCH_PAGE`.
- [`k_mem_paging_backing_store_page_out()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga51f663e0a8c31367082e78097359af6d) copies a data page
  from `K_MEM_SCRATCH_PAGE` to the backing store location associated
  with the provided `location` token.
- [`k_mem_paging_backing_store_page_finalize()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga8d4bd3ea311fd873413d0477e8deb464) is invoked after
  [`k_mem_paging_backing_store_page_in()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga9becb4908cc7840ece93a2360692962d) so that the page frame
  struct may be updated for internal accounting. This can be
  a no-op.

To implement a new backing store, the functions mentioned above
must be implemented.
[`k_mem_paging_backing_store_page_finalize()`](../../doxygen/html/group__mem-demand-paging-backing-store.md#ga8d4bd3ea311fd873413d0477e8deb464) can be an empty
function if so desired.

## API Reference

[Demand Paging APIs](../../doxygen/html/group__mem-demand-paging.md)

Related code samples

- [Demand paging](../../samples/subsys/demand_paging/README.md#demand-paging "Leverage demand paging to deal with code bigger than available RAM.")Leverage demand paging to deal with code bigger than available RAM.

### Eviction Algorithm APIs

[Eviction Algorithm APIs](../../doxygen/html/group__mem-demand-paging-eviction.md)

### Backing Store APIs

[Backing Store APIs](../../doxygen/html/group__mem-demand-paging-backing-store.md)
