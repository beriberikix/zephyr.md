---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mem-demand-paging.html
original_path: doxygen/html/group__mem-demand-paging.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Demand Paging APIs

[Kernel APIs](group__kernel__apis.md) » [Kernel Memory Management](group__kernel__memory__management.md) » [Demand Paging](group__demand__paging.md)

| Data Structures | |
| --- | --- |
| struct | [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) |
|  | Paging Statistics. [More...](structk__mem__paging__stats__t.md#details) |
| struct | [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) |
|  | Paging Statistics Histograms. [More...](structk__mem__paging__histogram__t.md#details) |

| Functions | |
| --- | --- |
| int | [k\_mem\_page\_out](#ga0b18037209b4d8b5964bd9a1d760f703) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Evict a page-aligned virtual memory region to the backing store. |
| void | [k\_mem\_page\_in](#gab36c36a4e230677d2090514f7a34b408) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Load a virtual data region into memory. |
| void | [k\_mem\_pin](#ga5f2d422edde7d366e81a870ce057589f) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Pin an aligned virtual data region, paging in as necessary. |
| void | [k\_mem\_unpin](#ga3278aae5e24733c722b7d83c4b17dab3) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Un-pin an aligned virtual data region. |
| void | [k\_mem\_paging\_stats\_get](#ga52ad88e0c0eed2aa27331bfd4707b7ec) (struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \*stats) |
|  | Get the paging statistics since system startup. |
| void | [k\_mem\_paging\_thread\_stats\_get](#gafad6b39cb2faf3bb416cd4d3faaa8d8c) (struct [k\_thread](structk__thread.md) \*thread, struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \*stats) |
|  | Get the paging statistics since system startup for a thread. |
| void | [k\_mem\_paging\_histogram\_eviction\_get](#gaec64d019d819b00c7bc3804aac269199) (struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist) |
|  | Get the eviction timing histogram. |
| void | [k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get](#ga1da0a643e8f85f98e29288e441a37dfa) (struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist) |
|  | Get the backing store page-in timing histogram. |
| void | [k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get](#gae4f80d14f88a46ddb9aeb7afba861864) (struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist) |
|  | Get the backing store page-out timing histogram. |

## Detailed Description

## Function Documentation

## [◆ ](#gab36c36a4e230677d2090514f7a34b408)k\_mem\_page\_in()

| void k\_mem\_page\_in | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Load a virtual data region into memory.

After the function completes, all the page frames associated with this function will be paged in. However, they are not guaranteed to stay there. This is useful if the region is known to be used soon.

If CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ is enabled, this function may not be called by ISRs as the backing store may be in-use.

Parameters
:   | addr | Base page-aligned virtual address |
    | --- | --- |
    | size | Page-aligned data region size |

## [◆ ](#ga0b18037209b4d8b5964bd9a1d760f703)k\_mem\_page\_out()

| int k\_mem\_page\_out | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Evict a page-aligned virtual memory region to the backing store.

Useful if it is known that a memory region will not be used for some time. All the data pages within the specified region will be evicted to the backing store if they weren't already, with their associated page frames marked as available for mappings or page-ins.

None of the associated page frames mapped to the provided region should be pinned.

Note that there are no guarantees how long these pages will be evicted, they could take page faults immediately.

If CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ is enabled, this function may not be called by ISRs as the backing store may be in-use.

Parameters
:   | addr | Base page-aligned virtual address |
    | --- | --- |
    | size | Page-aligned data region size |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOMEM | Insufficient space in backing store to satisfy request. The region may be partially paged out. |

## [◆ ](#ga1da0a643e8f85f98e29288e441a37dfa)k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get()

| void k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get | ( | struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \* | *hist* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Get the backing store page-in timing histogram.

This populates the timing histogram struct being passed in as argument.

Parameters
:   | [in,out] | hist | Timing histogram struct to be filled. |
    | --- | --- | --- |

## [◆ ](#gae4f80d14f88a46ddb9aeb7afba861864)k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get()

| void k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get | ( | struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \* | *hist* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Get the backing store page-out timing histogram.

This populates the timing histogram struct being passed in as argument.

Parameters
:   | [in,out] | hist | Timing histogram struct to be filled. |
    | --- | --- | --- |

## [◆ ](#gaec64d019d819b00c7bc3804aac269199)k\_mem\_paging\_histogram\_eviction\_get()

| void k\_mem\_paging\_histogram\_eviction\_get | ( | struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \* | *hist* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Get the eviction timing histogram.

This populates the timing histogram struct being passed in as argument.

Parameters
:   | [in,out] | hist | Timing histogram struct to be filled. |
    | --- | --- | --- |

## [◆ ](#ga52ad88e0c0eed2aa27331bfd4707b7ec)k\_mem\_paging\_stats\_get()

| void k\_mem\_paging\_stats\_get | ( | struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \* | *stats* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Get the paging statistics since system startup.

This populates the paging statistics struct being passed in as argument.

Parameters
:   | [in,out] | stats | Paging statistics struct to be filled. |
    | --- | --- | --- |

## [◆ ](#gafad6b39cb2faf3bb416cd4d3faaa8d8c)k\_mem\_paging\_thread\_stats\_get()

| void k\_mem\_paging\_thread\_stats\_get | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \* | *stats* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Get the paging statistics since system startup for a thread.

This populates the paging statistics struct being passed in as argument for a particular thread.

Parameters
:   | [in] | thread | Thread |
    | --- | --- | --- |
    | [in,out] | stats | Paging statistics struct to be filled. |

## [◆ ](#ga5f2d422edde7d366e81a870ce057589f)k\_mem\_pin()

| void k\_mem\_pin | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Pin an aligned virtual data region, paging in as necessary.

After the function completes, all the page frames associated with this region will be resident in memory and pinned such that they stay that way. This is a stronger version of z\_mem\_page\_in().

If CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ is enabled, this function may not be called by ISRs as the backing store may be in-use.

Parameters
:   | addr | Base page-aligned virtual address |
    | --- | --- |
    | size | Page-aligned data region size |

## [◆ ](#ga3278aae5e24733c722b7d83c4b17dab3)k\_mem\_unpin()

| void k\_mem\_unpin | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Un-pin an aligned virtual data region.

After the function completes, all the page frames associated with this region will be no longer marked as pinned. This does not evict the region, follow this with z\_mem\_page\_out() if you need that.

Parameters
:   | addr | Base page-aligned virtual address |
    | --- | --- |
    | size | Page-aligned data region size |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
