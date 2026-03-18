---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__rtio__mpsc.html
original_path: doxygen/html/group__rtio__mpsc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTIO MPSC API

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

RTIO Multiple Producer Single Consumer (MPSC) Queue API.
[More...](#details)

| Files | |
| --- | --- |
| file | [rtio\_mpsc.h](rtio__mpsc_8h.md) |
|  | A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list. |

| Data Structures | |
| --- | --- |
| struct | [rtio\_mpsc\_node](structrtio__mpsc__node.md) |
|  | Queue member. [More...](structrtio__mpsc__node.md#details) |
| struct | [rtio\_mpsc](structrtio__mpsc.md) |
|  | MPSC Queue. [More...](structrtio__mpsc.md#details) |

| Macros | |
| --- | --- |
| #define | [mpsc\_ptr\_get](#gab8d9c4ffe87940152156e90471b794a3)(ptr) |
| #define | [mpsc\_ptr\_set](#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(ptr, val) |
| #define | [mpsc\_ptr\_set\_get](#gaf008a0ceddef3c8bee343175199a2ddc)(ptr, val) |
| #define | [RTIO\_MPSC\_INIT](#ga28bb135e2b2387928d8b1ece175c2387)(symbol) |
|  | Static initializer for a mpsc queue. |

| Typedefs | |
| --- | --- |
| typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) | [mpsc\_ptr\_t](#ga15b6ff032fa4602e72415cf95c69e626) |

| Functions | |
| --- | --- |
| static void | [rtio\_mpsc\_init](#ga8e10263b8b3897d57625e710de9abda3) (struct [rtio\_mpsc](structrtio__mpsc.md) \*q) |
|  | Initialize queue. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [rtio\_mpsc\_push](#ga3ef9810ee938ecbc352a985baf60ade2) (struct [rtio\_mpsc](structrtio__mpsc.md) \*q, struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*n) |
|  | Push a node. |
| static struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \* | [rtio\_mpsc\_pop](#ga11697747c5377ccff4556d9d5dc96e56) (struct [rtio\_mpsc](structrtio__mpsc.md) \*q) |
|  | Pop a node off of the list. |

## Detailed Description

RTIO Multiple Producer Single Consumer (MPSC) Queue API.

## Macro Definition Documentation

## [◆ ](#gab8d9c4ffe87940152156e90471b794a3)mpsc\_ptr\_get

| #define mpsc\_ptr\_get | ( |  | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

**Value:**

[atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)(&(ptr))

[atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)

atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)

Atomic get a pointer value.

## [◆ ](#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)mpsc\_ptr\_set

| #define mpsc\_ptr\_set | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

**Value:**

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)(&(ptr), val)

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)

atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)

Atomic get-and-set for pointer values.

## [◆ ](#gaf008a0ceddef3c8bee343175199a2ddc)mpsc\_ptr\_set\_get

| #define mpsc\_ptr\_set\_get | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

**Value:**

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)(&(ptr), val)

## [◆ ](#ga28bb135e2b2387928d8b1ece175c2387)RTIO\_MPSC\_INIT

| #define RTIO\_MPSC\_INIT | ( |  | *symbol* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

**Value:**

{ \

.head = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)&symbol.stub, \

.tail = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)&symbol.stub, \

.stub = { \

.next = NULL, \

}, \

}

[rtio\_mpsc\_node](structrtio__mpsc__node.md)

Queue member.

**Definition** rtio\_mpsc.h:81

Static initializer for a mpsc queue.

Since the queue is

Parameters
:   | symbol | name of the queue |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga15b6ff032fa4602e72415cf95c69e626)mpsc\_ptr\_t

| typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) [mpsc\_ptr\_t](#ga15b6ff032fa4602e72415cf95c69e626) |
| --- |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

## Function Documentation

## [◆ ](#ga8e10263b8b3897d57625e710de9abda3)rtio\_mpsc\_init()

| | void rtio\_mpsc\_init | ( | struct [rtio\_mpsc](structrtio__mpsc.md) \* | *q* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

Initialize queue.

Parameters
:   | q | Queue to initialize or reset |
    | --- | --- |

## [◆ ](#ga11697747c5377ccff4556d9d5dc96e56)rtio\_mpsc\_pop()

| | struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \* rtio\_mpsc\_pop | ( | struct [rtio\_mpsc](structrtio__mpsc.md) \* | *q* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

Pop a node off of the list.

Return values
:   | NULL | When no node is available |
    | --- | --- |
    | node | When node is available |

## [◆ ](#ga3ef9810ee938ecbc352a985baf60ade2)rtio\_mpsc\_push()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void rtio\_mpsc\_push | ( | struct [rtio\_mpsc](structrtio__mpsc.md) \* | *q*, | | --- | --- | --- | --- | |  |  | struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \* | *n* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio_mpsc.h](rtio__mpsc_8h.md)>`

Push a node.

Parameters
:   | q | Queue to push the node to |
    | --- | --- |
    | n | Node to push into the queue |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
