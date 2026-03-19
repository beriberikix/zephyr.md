---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/kernel__structs_8h.html
original_path: doxygen/html/kernel__structs_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_structs.h File Reference

`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/sys_heap.h](sys__heap_8h_source.md)>`  
`#include <[zephyr/arch/structs.h](structs_8h_source.md)>`  
`#include <[zephyr/kernel/stats.h](kernel_2stats_8h_source.md)>`  
`#include <[zephyr/kernel/obj_core.h](obj__core_8h_source.md)>`  
`#include <[zephyr/sys/rb.h](rb_8h_source.md)>`

[Go to the source code of this file.](kernel__structs_8h_source.md)

| Macros | |
| --- | --- |
| #define | [K\_NUM\_THREAD\_PRIO](#ae861b4805a52e8bd99d5481d3943dc5c)   (CONFIG\_NUM\_PREEMPT\_PRIORITIES + CONFIG\_NUM\_COOP\_PRIORITIES + 1) |
| #define | [PRIQ\_BITMAP\_SIZE](#a3fcfea2426c3da024f627c8ab9e754ad)   ([DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([K\_NUM\_THREAD\_PRIO](#ae861b4805a52e8bd99d5481d3943dc5c), [BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3))) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_thread\_timeslice\_fn\_t](#a44c6f88a879877ad8da28706e274064f)) (struct [k\_thread](structk__thread.md) \*thread, void \*data) |

## Macro Definition Documentation

## [◆ ](#ae861b4805a52e8bd99d5481d3943dc5c)K\_NUM\_THREAD\_PRIO

| #define K\_NUM\_THREAD\_PRIO   (CONFIG\_NUM\_PREEMPT\_PRIORITIES + CONFIG\_NUM\_COOP\_PRIORITIES + 1) |
| --- |

## [◆ ](#a3fcfea2426c3da024f627c8ab9e754ad)PRIQ\_BITMAP\_SIZE

| #define PRIQ\_BITMAP\_SIZE   ([DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([K\_NUM\_THREAD\_PRIO](#ae861b4805a52e8bd99d5481d3943dc5c), [BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3))) |
| --- |

## Typedef Documentation

## [◆ ](#a44c6f88a879877ad8da28706e274064f)k\_thread\_timeslice\_fn\_t

| typedef void(\* k\_thread\_timeslice\_fn\_t) (struct [k\_thread](structk__thread.md) \*thread, void \*data) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel\_structs.h](kernel__structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
