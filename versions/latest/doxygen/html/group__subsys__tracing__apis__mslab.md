---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis__mslab.html
original_path: doxygen/html/group__subsys__tracing__apis__mslab.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory Slab Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Memory Slab Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_mem\_slab\_init](#ga5a769fffc7611a57c8490b3f5c6047a5)(slab, rc) |
|  | Trace initialization of Memory Slab. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_alloc\_enter](#gac1ac5f1393b87ea84c2d53f08c251ff2)(slab, timeout) |
|  | Trace Memory Slab alloc attempt entry. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking](#gaea77ffa2dbbfad9ff2fec0041b0dbc59)(slab, timeout) |
|  | Trace Memory Slab alloc attempt blocking. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_alloc\_exit](#ga237bb89733ca9c483ef6b9ab6dd920a4)(slab, timeout, ret) |
|  | Trace Memory Slab alloc attempt outcome. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_free\_enter](#ga22fc4609185f6ddffd0abc85f3976914)(slab) |
|  | Trace Memory Slab free entry. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_free\_exit](#ga81dd030d4052e3092479e19616b4baec)(slab) |
|  | Trace Memory Slab free exit. |

## Detailed Description

Memory Slab Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gaea77ffa2dbbfad9ff2fec0041b0dbc59)sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking

| #define sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking | ( |  | *slab*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Memory Slab alloc attempt blocking.

Parameters
:   | slab | Memory Slab object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gac1ac5f1393b87ea84c2d53f08c251ff2)sys\_port\_trace\_k\_mem\_slab\_alloc\_enter

| #define sys\_port\_trace\_k\_mem\_slab\_alloc\_enter | ( |  | *slab*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Memory Slab alloc attempt entry.

Parameters
:   | slab | Memory Slab object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga237bb89733ca9c483ef6b9ab6dd920a4)sys\_port\_trace\_k\_mem\_slab\_alloc\_exit

| #define sys\_port\_trace\_k\_mem\_slab\_alloc\_exit | ( |  | *slab*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Memory Slab alloc attempt outcome.

Parameters
:   | slab | Memory Slab object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga22fc4609185f6ddffd0abc85f3976914)sys\_port\_trace\_k\_mem\_slab\_free\_enter

| #define sys\_port\_trace\_k\_mem\_slab\_free\_enter | ( |  | *slab* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Memory Slab free entry.

Parameters
:   | slab | Memory Slab object |
    | --- | --- |

## [◆ ](#ga81dd030d4052e3092479e19616b4baec)sys\_port\_trace\_k\_mem\_slab\_free\_exit

| #define sys\_port\_trace\_k\_mem\_slab\_free\_exit | ( |  | *slab* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Memory Slab free exit.

Parameters
:   | slab | Memory Slab object |
    | --- | --- |

## [◆ ](#ga5a769fffc7611a57c8490b3f5c6047a5)sys\_port\_trace\_k\_mem\_slab\_init

| #define sys\_port\_trace\_k\_mem\_slab\_init | ( |  | *slab*, |
| --- | --- | --- | --- |
|  |  |  | *rc* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialization of Memory Slab.

Parameters
:   | slab | Memory Slab object |
    | --- | --- |
    | rc | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
