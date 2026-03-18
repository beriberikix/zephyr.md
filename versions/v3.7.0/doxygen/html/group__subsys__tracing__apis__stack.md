---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__stack.html
original_path: doxygen/html/group__subsys__tracing__apis__stack.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Stack Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Stack Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_stack\_init](#ga5bb95f74d8bc3eed2525be20c444824f)(stack) |
|  | Trace initialization of Stack. |
| #define | [sys\_port\_trace\_k\_stack\_alloc\_init\_enter](#gaa10d6cb275914bb25ad6ffad12807480)(stack) |
|  | Trace Stack alloc init attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_alloc\_init\_exit](#gabaabe367b83b39248112eadb07bdf714)(stack, ret) |
|  | Trace Stack alloc init outcome. |
| #define | [sys\_port\_trace\_k\_stack\_cleanup\_enter](#gaf8357d3d9a2cb8de7ba0b3473c5b063c)(stack) |
|  | Trace Stack cleanup attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_cleanup\_exit](#ga2225cab95abdd8188087e6a98641ec0c)(stack, ret) |
|  | Trace Stack cleanup outcome. |
| #define | [sys\_port\_trace\_k\_stack\_push\_enter](#gad6a42d93265b53540baab5c59f55fbf6)(stack) |
|  | Trace Stack push attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_push\_exit](#ga203d32ef138d041aa0c20db8a75ccd6a)(stack, ret) |
|  | Trace Stack push attempt outcome. |
| #define | [sys\_port\_trace\_k\_stack\_pop\_enter](#gaaf9ac378b0bbf09af91c1987dc5b777e)(stack, timeout) |
|  | Trace Stack pop attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_pop\_blocking](#gacbdaf326a104d3bdcd4ceb5ec72c9b4f)(stack, timeout) |
|  | Trace Stack pop attempt blocking. |
| #define | [sys\_port\_trace\_k\_stack\_pop\_exit](#ga11280d48a97cca4b65210791f9d8c591)(stack, timeout, ret) |
|  | Trace Stack pop attempt outcome. |

## Detailed Description

Stack Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gaa10d6cb275914bb25ad6ffad12807480)sys\_port\_trace\_k\_stack\_alloc\_init\_enter

| #define sys\_port\_trace\_k\_stack\_alloc\_init\_enter | ( |  | *stack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack alloc init attempt entry.

Parameters
:   | stack | Stack object |
    | --- | --- |

## [◆ ](#gabaabe367b83b39248112eadb07bdf714)sys\_port\_trace\_k\_stack\_alloc\_init\_exit

| #define sys\_port\_trace\_k\_stack\_alloc\_init\_exit | ( |  | *stack*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack alloc init outcome.

Parameters
:   | stack | Stack object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaf8357d3d9a2cb8de7ba0b3473c5b063c)sys\_port\_trace\_k\_stack\_cleanup\_enter

| #define sys\_port\_trace\_k\_stack\_cleanup\_enter | ( |  | *stack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack cleanup attempt entry.

Parameters
:   | stack | Stack object |
    | --- | --- |

## [◆ ](#ga2225cab95abdd8188087e6a98641ec0c)sys\_port\_trace\_k\_stack\_cleanup\_exit

| #define sys\_port\_trace\_k\_stack\_cleanup\_exit | ( |  | *stack*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack cleanup outcome.

Parameters
:   | stack | Stack object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga5bb95f74d8bc3eed2525be20c444824f)sys\_port\_trace\_k\_stack\_init

| #define sys\_port\_trace\_k\_stack\_init | ( |  | *stack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Stack.

Parameters
:   | stack | Stack object |
    | --- | --- |

## [◆ ](#gacbdaf326a104d3bdcd4ceb5ec72c9b4f)sys\_port\_trace\_k\_stack\_pop\_blocking

| #define sys\_port\_trace\_k\_stack\_pop\_blocking | ( |  | *stack*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack pop attempt blocking.

Parameters
:   | stack | Stack object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gaaf9ac378b0bbf09af91c1987dc5b777e)sys\_port\_trace\_k\_stack\_pop\_enter

| #define sys\_port\_trace\_k\_stack\_pop\_enter | ( |  | *stack*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack pop attempt entry.

Parameters
:   | stack | Stack object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga11280d48a97cca4b65210791f9d8c591)sys\_port\_trace\_k\_stack\_pop\_exit

| #define sys\_port\_trace\_k\_stack\_pop\_exit | ( |  | *stack*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack pop attempt outcome.

Parameters
:   | stack | Stack object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#gad6a42d93265b53540baab5c59f55fbf6)sys\_port\_trace\_k\_stack\_push\_enter

| #define sys\_port\_trace\_k\_stack\_push\_enter | ( |  | *stack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack push attempt entry.

Parameters
:   | stack | Stack object |
    | --- | --- |

## [◆ ](#ga203d32ef138d041aa0c20db8a75ccd6a)sys\_port\_trace\_k\_stack\_push\_exit

| #define sys\_port\_trace\_k\_stack\_push\_exit | ( |  | *stack*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Stack push attempt outcome.

Parameters
:   | stack | Stack object |
    | --- | --- |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
