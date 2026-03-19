---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mpsc__lockfree_8h.html
original_path: doxygen/html/mpsc__lockfree_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_lockfree.h File Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC Lockfree Queue API](group__mpsc__lockfree.md)

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](mpsc__lockfree_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mpsc\_node](structmpsc__node.md) |
|  | Queue member. [More...](structmpsc__node.md#details) |
| struct | [mpsc](structmpsc.md) |
|  | MPSC Queue. [More...](structmpsc.md#details) |

| Macros | |
| --- | --- |
| #define | [mpsc\_ptr\_get](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)(ptr) |
| #define | [mpsc\_ptr\_set](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(ptr, val) |
| #define | [mpsc\_ptr\_set\_get](group__mpsc__lockfree.md#gaf008a0ceddef3c8bee343175199a2ddc)(ptr, val) |
| #define | [MPSC\_INIT](group__mpsc__lockfree.md#ga378ad8e2b4cde0727996eb67b1751a2d)(symbol) |
|  | Static initializer for a mpsc queue. |

| Typedefs | |
| --- | --- |
| typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) | [mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626) |

| Functions | |
| --- | --- |
| static void | [mpsc\_init](group__mpsc__lockfree.md#gaf08a8c0094f998af98e4d1ec431fc490) (struct [mpsc](structmpsc.md) \*q) |
|  | Initialize queue. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37) (struct [mpsc](structmpsc.md) \*q, struct [mpsc\_node](structmpsc__node.md) \*n) |
|  | Push a node. |
| static struct [mpsc\_node](structmpsc__node.md) \* | [mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7) (struct [mpsc](structmpsc.md) \*q) |
|  | Pop a node off of the list. |

## Detailed Description

A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list.

Ordering is First-In-First-Out.

Based on the well known and widely used wait-free MPSC queue described by Dmitry Vyukov with some slight changes to account for needs of an RTOS on a variety of archs. Both consumer and producer are wait free. No CAS loop or lock is needed.

An MPSC queue is safe to produce or consume in an ISR with O(1) push/pop.

Warning
:   MPSC is *not* safe to consume in multiple execution contexts.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mpsc\_lockfree.h](mpsc__lockfree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
