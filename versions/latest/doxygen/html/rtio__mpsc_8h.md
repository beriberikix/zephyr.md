---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtio__mpsc_8h.html
original_path: doxygen/html/rtio__mpsc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_mpsc.h File Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md) » [RTIO MPSC API](group__rtio__mpsc.md)

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/toolchain/common.h](common_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](rtio__mpsc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [rtio\_mpsc\_node](structrtio__mpsc__node.md) |
|  | Queue member. [More...](structrtio__mpsc__node.md#details) |
| struct | [rtio\_mpsc](structrtio__mpsc.md) |
|  | MPSC Queue. [More...](structrtio__mpsc.md#details) |

| Macros | |
| --- | --- |
| #define | [mpsc\_ptr\_get](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)(ptr) |
| #define | [mpsc\_ptr\_set](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(ptr, val) |
| #define | [mpsc\_ptr\_set\_get](group__rtio__mpsc.md#gaf008a0ceddef3c8bee343175199a2ddc)(ptr, val) |
| #define | [RTIO\_MPSC\_INIT](group__rtio__mpsc.md#ga28bb135e2b2387928d8b1ece175c2387)(symbol) |
|  | Static initializer for a mpsc queue. |

| Typedefs | |
| --- | --- |
| typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) | [mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626) |

| Functions | |
| --- | --- |
| static void | [rtio\_mpsc\_init](group__rtio__mpsc.md#ga8e10263b8b3897d57625e710de9abda3) (struct [rtio\_mpsc](structrtio__mpsc.md) \*q) |
|  | Initialize queue. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2) (struct [rtio\_mpsc](structrtio__mpsc.md) \*q, struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*n) |
|  | Push a node. |
| static struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \* | [rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56) (struct [rtio\_mpsc](structrtio__mpsc.md) \*q) |
|  | Pop a node off of the list. |

## Detailed Description

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.

Ordering is First-In-First-Out.

Based on the well known and widely used wait-free MPSC queue described by Dmitry Vyukov with some slight changes to account for needs of an RTOS on a variety of archs. Both consumer and producer are wait free. No CAS loop or lock is needed.

An MPSC queue is safe to produce or consume in an ISR with O(1) push/pop.

Warning
:   MPSC is *not* safe to consume in multiple execution contexts.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio\_mpsc.h](rtio__mpsc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
