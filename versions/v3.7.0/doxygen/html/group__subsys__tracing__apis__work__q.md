---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__work__q.html
original_path: doxygen/html/group__subsys__tracing__apis__work__q.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Work Queue Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Work Queue Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_work\_queue\_init](#ga9e25524cb89a9cabd6ad70459e8bd641)(queue) |
|  | Trace initialisation of a Work Queue structure. |
| #define | [sys\_port\_trace\_k\_work\_queue\_start\_enter](#ga79eba7247bd2c52480ac09e6ecef8635)(queue) |
|  | Trace start of a Work Queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_start\_exit](#gae25756a58b450b2d1e8c3475cbfc1758)(queue) |
|  | Trace start of a Work Queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_queue\_drain\_enter](#ga88af757f4867f3c65f2d0eff605e0736)(queue) |
|  | Trace Work Queue drain call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_drain\_exit](#ga24ca38662182a01185c9815f3cc87385)(queue, ret) |
|  | Trace Work Queue drain call exit. |
| #define | [sys\_port\_trace\_k\_work\_queue\_unplug\_enter](#ga1ca826910efe678127cdc1f9fdae75e7)(queue) |
|  | Trace Work Queue unplug call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_unplug\_exit](#gaae2cf0379cbcf040f36fbba39821be2f)(queue, ret) |
|  | Trace Work Queue unplug call exit. |

## Detailed Description

Work Queue Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga88af757f4867f3c65f2d0eff605e0736)sys\_port\_trace\_k\_work\_queue\_drain\_enter

| #define sys\_port\_trace\_k\_work\_queue\_drain\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Work Queue drain call entry.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |

## [◆ ](#ga24ca38662182a01185c9815f3cc87385)sys\_port\_trace\_k\_work\_queue\_drain\_exit

| #define sys\_port\_trace\_k\_work\_queue\_drain\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Work Queue drain call exit.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga9e25524cb89a9cabd6ad70459e8bd641)sys\_port\_trace\_k\_work\_queue\_init

| #define sys\_port\_trace\_k\_work\_queue\_init | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialisation of a Work Queue structure.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |

## [◆ ](#ga79eba7247bd2c52480ac09e6ecef8635)sys\_port\_trace\_k\_work\_queue\_start\_enter

| #define sys\_port\_trace\_k\_work\_queue\_start\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace start of a Work Queue call entry.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |

## [◆ ](#gae25756a58b450b2d1e8c3475cbfc1758)sys\_port\_trace\_k\_work\_queue\_start\_exit

| #define sys\_port\_trace\_k\_work\_queue\_start\_exit | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace start of a Work Queue call exit.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |

## [◆ ](#ga1ca826910efe678127cdc1f9fdae75e7)sys\_port\_trace\_k\_work\_queue\_unplug\_enter

| #define sys\_port\_trace\_k\_work\_queue\_unplug\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Work Queue unplug call entry.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |

## [◆ ](#gaae2cf0379cbcf040f36fbba39821be2f)sys\_port\_trace\_k\_work\_queue\_unplug\_exit

| #define sys\_port\_trace\_k\_work\_queue\_unplug\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Work Queue unplug call exit.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
