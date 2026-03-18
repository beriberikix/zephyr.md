---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mem-demand-paging-eviction.html
original_path: doxygen/html/group__mem-demand-paging-eviction.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| struct z\_page\_frame \* | [k\_mem\_paging\_eviction\_select](#ga12641d53942529c7d7364c08473a6eca) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*dirty) |
|  | Select a page frame for eviction. |
| void | [k\_mem\_paging\_eviction\_init](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4) (void) |
|  | Initialization function. |

## Detailed Description

Eviction algorithm APIs.

## Function Documentation

## [◆ ](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)k\_mem\_paging\_eviction\_init()

| void k\_mem\_paging\_eviction\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Initialization function.

Called at POST\_KERNEL to perform any necessary initialization tasks for the eviction algorithm. [k\_mem\_paging\_eviction\_select()](#ga12641d53942529c7d7364c08473a6eca) is guaranteed to never be called until this has returned, and this will only be called once.

## [◆ ](#ga12641d53942529c7d7364c08473a6eca)k\_mem\_paging\_eviction\_select()

| struct z\_page\_frame \* k\_mem\_paging\_eviction\_select | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *dirty* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[demand_paging.h](demand__paging_8h.md)>`

Select a page frame for eviction.

The kernel will invoke this to choose a page frame to evict if there are no free page frames.

This function will never be called before the initial [k\_mem\_paging\_eviction\_init()](#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4).

This function is invoked with interrupts locked.

Parameters
:   | [out] | dirty | Whether the page to evict is dirty |
    | --- | --- | --- |

Returns
:   The page frame to evict

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
