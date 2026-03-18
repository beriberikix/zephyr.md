---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis__lifo.html
original_path: doxygen/html/group__subsys__tracing__apis__lifo.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LIFO Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

LIFO Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_lifo\_init\_enter](#gaad81b60363467b56d887baee8c8b5bf2)(lifo) |
|  | Trace initialization of LIFO Queue entry. |
| #define | [sys\_port\_trace\_k\_lifo\_init\_exit](#ga4f08168ded97456265abb3a903585ecf)(lifo) |
|  | Trace initialization of LIFO Queue exit. |
| #define | [sys\_port\_trace\_k\_lifo\_put\_enter](#gafd9c45a171a2fb146defa356ff0bc0f5)(lifo, data) |
|  | Trace LIFO Queue put entry. |
| #define | [sys\_port\_trace\_k\_lifo\_put\_exit](#ga0e5372c37bdd3a47adf11ab9d3a5e22d)(lifo, data) |
|  | Trace LIFO Queue put exit. |
| #define | [sys\_port\_trace\_k\_lifo\_alloc\_put\_enter](#ga0d9717f4b43e344518cc451a2fe9d224)(lifo, data) |
|  | Trace LIFO Queue alloc put entry. |
| #define | [sys\_port\_trace\_k\_lifo\_alloc\_put\_exit](#ga19bb748367aba8f576e72cdc30834ab1)(lifo, data, ret) |
|  | Trace LIFO Queue alloc put exit. |
| #define | [sys\_port\_trace\_k\_lifo\_get\_enter](#ga61556928453492dc6ed4efc999668f01)(lifo, timeout) |
|  | Trace LIFO Queue get entry. |
| #define | [sys\_port\_trace\_k\_lifo\_get\_exit](#ga2f7e8e680cac03844ca5dbab0438a754)(lifo, timeout, ret) |
|  | Trace LIFO Queue get exit. |

## Detailed Description

LIFO Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga0d9717f4b43e344518cc451a2fe9d224)sys\_port\_trace\_k\_lifo\_alloc\_put\_enter

| #define sys\_port\_trace\_k\_lifo\_alloc\_put\_enter | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace LIFO Queue alloc put entry.

Parameters
:   | lifo | LIFO object |
    | --- | --- |
    | data | Data item |

## [◆ ](#ga19bb748367aba8f576e72cdc30834ab1)sys\_port\_trace\_k\_lifo\_alloc\_put\_exit

| #define sys\_port\_trace\_k\_lifo\_alloc\_put\_exit | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *data*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace LIFO Queue alloc put exit.

Parameters
:   | lifo | LIFO object |
    | --- | --- |
    | data | Data item |
    | ret | Return value |

## [◆ ](#ga61556928453492dc6ed4efc999668f01)sys\_port\_trace\_k\_lifo\_get\_enter

| #define sys\_port\_trace\_k\_lifo\_get\_enter | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace LIFO Queue get entry.

Parameters
:   | lifo | LIFO object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga2f7e8e680cac03844ca5dbab0438a754)sys\_port\_trace\_k\_lifo\_get\_exit

| #define sys\_port\_trace\_k\_lifo\_get\_exit | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace LIFO Queue get exit.

Parameters
:   | lifo | LIFO object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#gaad81b60363467b56d887baee8c8b5bf2)sys\_port\_trace\_k\_lifo\_init\_enter

| #define sys\_port\_trace\_k\_lifo\_init\_enter | ( |  | *lifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialization of LIFO Queue entry.

Parameters
:   | lifo | LIFO object |
    | --- | --- |

## [◆ ](#ga4f08168ded97456265abb3a903585ecf)sys\_port\_trace\_k\_lifo\_init\_exit

| #define sys\_port\_trace\_k\_lifo\_init\_exit | ( |  | *lifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialization of LIFO Queue exit.

Parameters
:   | lifo | LIFO object |
    | --- | --- |

## [◆ ](#gafd9c45a171a2fb146defa356ff0bc0f5)sys\_port\_trace\_k\_lifo\_put\_enter

| #define sys\_port\_trace\_k\_lifo\_put\_enter | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace LIFO Queue put entry.

Parameters
:   | lifo | LIFO object |
    | --- | --- |
    | data | Data item |

## [◆ ](#ga0e5372c37bdd3a47adf11ab9d3a5e22d)sys\_port\_trace\_k\_lifo\_put\_exit

| #define sys\_port\_trace\_k\_lifo\_put\_exit | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace LIFO Queue put exit.

Parameters
:   | lifo | LIFO object |
    | --- | --- |
    | data | Data item |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
