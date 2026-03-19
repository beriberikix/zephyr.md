---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mem-demand-paging-eviction.html
original_path: doxygen/html/group__mem-demand-paging-eviction.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Eviction Algorithm APIs

[Kernel APIs](group__kernel__apis.md) » [Kernel Memory Management](group__kernel__memory__management.md) » [Demand Paging](group__demand__paging.md)

Eviction algorithm APIs.
[More...](#details)

| Functions | |
| --- | --- |
| void | [k\_mem\_paging\_eviction\_add](#ga6bb19be3098cc839ae3f6e9528598867) (struct k\_mem\_page\_frame \*pf) |
|  | Submit a page frame for eviction candidate tracking. |
| void | [k\_mem\_paging\_eviction\_remove](#ga16a4df904cc7a9641d06741ed589949d) (struct k\_mem\_page\_frame \*pf) |
|  | Remove a page frame from potential eviction candidates. |
| void | [k\_mem\_paging\_eviction\_accessed](#ga228747c10bfd8816aec59fddf0e3a224) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Process a page frame as being newly accessed. |
| struct k\_mem\_page\_frame \* | [k\_mem\_paging\_eviction\_select](#gaadbb4eb56c239f800daf995e6673ae1d) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*dirty) |
|  | Select a page frame for eviction. |
| void | [k\_mem\_paging\_eviction\_init](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4) (void) |
|  | Initialization function. |

## Detailed Description

Eviction algorithm APIs.

## Function Documentation

## [◆ ](#ga228747c10bfd8816aec59fddf0e3a224)k\_mem\_paging\_eviction\_accessed()

| void k\_mem\_paging\_eviction\_accessed | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Process a page frame as being newly accessed.

The architecture-specific memory fault handler will invoke this to tell the eviction algorithm the provided physical address belongs to a page frame being accessed and such page frame should become unlikely to be considered as the next eviction candidate.

This function is invoked with interrupts locked.

Parameters
:   | [in] | phys | The physical address being accessed |
    | --- | --- | --- |

## [◆ ](#ga6bb19be3098cc839ae3f6e9528598867)k\_mem\_paging\_eviction\_add()

| void k\_mem\_paging\_eviction\_add | ( | struct k\_mem\_page\_frame \* | *pf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Submit a page frame for eviction candidate tracking.

The kernel will invoke this to tell the eviction algorithm the provided page frame may be considered as a potential eviction candidate.

This function will never be called before the initial [k\_mem\_paging\_eviction\_init()](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4).

This function is invoked with interrupts locked.

Parameters
:   | [in] | pf | The page frame to add |
    | --- | --- | --- |

## [◆ ](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)k\_mem\_paging\_eviction\_init()

| void k\_mem\_paging\_eviction\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Initialization function.

Called at POST\_KERNEL to perform any necessary initialization tasks for the eviction algorithm. [k\_mem\_paging\_eviction\_select()](#gaadbb4eb56c239f800daf995e6673ae1d) is guaranteed to never be called until this has returned, and this will only be called once.

## [◆ ](#ga16a4df904cc7a9641d06741ed589949d)k\_mem\_paging\_eviction\_remove()

| void k\_mem\_paging\_eviction\_remove | ( | struct k\_mem\_page\_frame \* | *pf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Remove a page frame from potential eviction candidates.

The kernel will invoke this to tell the eviction algorithm the provided page frame may no longer be considered as a potential eviction candidate.

This function will only be called with page frames that were submitted using [k\_mem\_paging\_eviction\_add()](#ga6bb19be3098cc839ae3f6e9528598867) beforehand.

This function is invoked with interrupts locked.

Parameters
:   | [in] | pf | The page frame to remove |
    | --- | --- | --- |

## [◆ ](#gaadbb4eb56c239f800daf995e6673ae1d)k\_mem\_paging\_eviction\_select()

| struct k\_mem\_page\_frame \* k\_mem\_paging\_eviction\_select | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *dirty* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Select a page frame for eviction.

The kernel will invoke this to choose a page frame to evict if there are no free page frames. It is not guaranteed that the returned page frame will actually be evicted. If it is then the kernel will call [k\_mem\_paging\_eviction\_remove()](#ga16a4df904cc7a9641d06741ed589949d) with it.

This function will never be called before the initial [k\_mem\_paging\_eviction\_init()](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4).

This function is invoked with interrupts locked.

Parameters
:   | [out] | dirty | Whether the page to evict is dirty |
    | --- | --- | --- |

Returns
:   The page frame to evict

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
