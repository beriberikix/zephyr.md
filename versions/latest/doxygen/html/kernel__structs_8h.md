---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel__structs_8h.html
original_path: doxygen/html/kernel__structs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_structs.h File Reference

`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel/internal/sched_priq.h](sched__priq_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/sys_heap.h](sys__heap_8h_source.md)>`  
`#include <[zephyr/arch/structs.h](structs_8h_source.md)>`  
`#include <[zephyr/kernel/stats.h](kernel_2stats_8h_source.md)>`  
`#include <[zephyr/kernel/obj_core.h](obj__core_8h_source.md)>`

[Go to the source code of this file.](kernel__structs_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_thread\_timeslice\_fn\_t](#a44c6f88a879877ad8da28706e274064f)) (struct [k\_thread](structk__thread.md) \*thread, void \*data) |

## Typedef Documentation

## [◆ ](#a44c6f88a879877ad8da28706e274064f)k\_thread\_timeslice\_fn\_t

| typedef void(\* k\_thread\_timeslice\_fn\_t) (struct [k\_thread](structk__thread.md) \*thread, void \*data) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel\_structs.h](kernel__structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
