---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__object__tracking.html
original_path: doxygen/html/group__subsys__tracing__object__tracking.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Object tracking

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md)

Object tracking.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_PORT\_TRACK\_NEXT](#ga6c7340c07c55f462c00d9bca7fc00a58)(list) |
|  | Gets node's next element in a object tracking list. |

## Detailed Description

Object tracking.

Object tracking provides lists to kernel objects, so their existence and current status can be tracked.

The following global variables are the heads of available lists:

- \_track\_list\_k\_timer
- \_track\_list\_k\_mem\_slab
- \_track\_list\_k\_sem
- \_track\_list\_k\_mutex
- \_track\_list\_k\_stack
- \_track\_list\_k\_msgq
- \_track\_list\_k\_mbox
- \_track\_list\_k\_pipe
- \_track\_list\_k\_queue
- \_track\_list\_k\_event

## Macro Definition Documentation

## [◆ ](#ga6c7340c07c55f462c00d9bca7fc00a58)SYS\_PORT\_TRACK\_NEXT

| #define SYS\_PORT\_TRACK\_NEXT | ( |  | *list* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracking.h](tracking_8h.md)>`

**Value:**

((list)->\_obj\_track\_next)

Gets node's next element in a object tracking list.

Parameters
:   | list | Node to get next element from. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
