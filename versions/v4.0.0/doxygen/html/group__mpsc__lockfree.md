---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mpsc__lockfree.html
original_path: doxygen/html/group__mpsc__lockfree.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MPSC Lockfree Queue API

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Multiple Producer Single Consumer (MPSC) Lockfree Queue API.
[More...](#details)

| Files | |
| --- | --- |
| file | [mpsc\_lockfree.h](mpsc__lockfree_8h.md) |
|  | A wait-free intrusive multi producer single consumer (MPSC) queue using a singly linked list. |

| Data Structures | |
| --- | --- |
| struct | [mpsc\_node](structmpsc__node.md) |
|  | Queue member. [More...](structmpsc__node.md#details) |
| struct | [mpsc](structmpsc.md) |
|  | MPSC Queue. [More...](structmpsc.md#details) |

| Macros | |
| --- | --- |
| #define | [mpsc\_ptr\_get](#gab8d9c4ffe87940152156e90471b794a3)(ptr) |
| #define | [mpsc\_ptr\_set](#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(ptr, val) |
| #define | [mpsc\_ptr\_set\_get](#gaf008a0ceddef3c8bee343175199a2ddc)(ptr, val) |
| #define | [MPSC\_INIT](#ga378ad8e2b4cde0727996eb67b1751a2d)(symbol) |
|  | Static initializer for a mpsc queue. |

| Typedefs | |
| --- | --- |
| typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) | [mpsc\_ptr\_t](#ga15b6ff032fa4602e72415cf95c69e626) |

| Functions | |
| --- | --- |
| static void | [mpsc\_init](#gaf08a8c0094f998af98e4d1ec431fc490) (struct [mpsc](structmpsc.md) \*q) |
|  | Initialize queue. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [mpsc\_push](#ga403add133841ef88e10d74141e782b37) (struct [mpsc](structmpsc.md) \*q, struct [mpsc\_node](structmpsc__node.md) \*n) |
|  | Push a node. |
| static struct [mpsc\_node](structmpsc__node.md) \* | [mpsc\_pop](#ga823ec37b84ac43e46167aac954bce9d7) (struct [mpsc](structmpsc.md) \*q) |
|  | Pop a node off of the list. |

## Detailed Description

Multiple Producer Single Consumer (MPSC) Lockfree Queue API.

## Macro Definition Documentation

## [◆ ](#ga378ad8e2b4cde0727996eb67b1751a2d)MPSC\_INIT

| #define MPSC\_INIT | ( |  | *symbol* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

**Value:**

{ \

.head = (struct [mpsc\_node](structmpsc__node.md) \*)&symbol.stub, \

.tail = (struct [mpsc\_node](structmpsc__node.md) \*)&symbol.stub, \

.stub = { \

.next = NULL, \

}, \

}

[mpsc\_node](structmpsc__node.md)

Queue member.

**Definition** mpsc\_lockfree.h:79

Static initializer for a mpsc queue.

Since the queue is

Parameters
:   | symbol | name of the queue |
    | --- | --- |

## [◆ ](#gab8d9c4ffe87940152156e90471b794a3)mpsc\_ptr\_get

| #define mpsc\_ptr\_get | ( |  | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

**Value:**

[atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)(&(ptr))

[atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)

atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)

Atomic get a pointer value.

## [◆ ](#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)mpsc\_ptr\_set

| #define mpsc\_ptr\_set | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

**Value:**

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)(&(ptr), val)

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)

atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)

Atomic get-and-set for pointer values.

## [◆ ](#gaf008a0ceddef3c8bee343175199a2ddc)mpsc\_ptr\_set\_get

| #define mpsc\_ptr\_set\_get | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

**Value:**

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)(&(ptr), val)

## Typedef Documentation

## [◆ ](#ga15b6ff032fa4602e72415cf95c69e626)mpsc\_ptr\_t

| typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) [mpsc\_ptr\_t](#ga15b6ff032fa4602e72415cf95c69e626) |
| --- |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

## Function Documentation

## [◆ ](#gaf08a8c0094f998af98e4d1ec431fc490)mpsc\_init()

| | void mpsc\_init | ( | struct [mpsc](structmpsc.md) \* | *q* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

Initialize queue.

Parameters
:   | q | Queue to initialize or reset |
    | --- | --- |

## [◆ ](#ga823ec37b84ac43e46167aac954bce9d7)mpsc\_pop()

| | struct [mpsc\_node](structmpsc__node.md) \* mpsc\_pop | ( | struct [mpsc](structmpsc.md) \* | *q* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

Pop a node off of the list.

Return values
:   | NULL | When no node is available |
    | --- | --- |
    | node | When node is available |

## [◆ ](#ga403add133841ef88e10d74141e782b37)mpsc\_push()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void mpsc\_push | ( | struct [mpsc](structmpsc.md) \* | *q*, | | --- | --- | --- | --- | |  |  | struct [mpsc\_node](structmpsc__node.md) \* | *n* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mpsc_lockfree.h](mpsc__lockfree_8h.md)>`

Push a node.

Parameters
:   | q | Queue to push the node to |
    | --- | --- |
    | n | Node to push into the queue |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
