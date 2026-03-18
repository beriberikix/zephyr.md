---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__timer.html
original_path: doxygen/html/group__subsys__tracing__apis__timer.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Timer Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Timer Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_timer\_init](#ga03a70d84ea0227829fb9528b0156c147)(timer) |
|  | Trace initialization of Timer. |
| #define | [sys\_port\_trace\_k\_timer\_start](#ga95b998ea6bf00692cb654a18787ab185)(timer, duration, period) |
|  | Trace Timer start. |
| #define | [sys\_port\_trace\_k\_timer\_stop](#ga81b6cba81190cc61cdd33f4ddb6f4550)(timer) |
|  | Trace Timer stop. |
| #define | [sys\_port\_trace\_k\_timer\_status\_sync\_enter](#ga0adf7e6ca5bdd89b7676836101ef37df)(timer) |
|  | Trace Timer status sync entry. |
| #define | [sys\_port\_trace\_k\_timer\_status\_sync\_blocking](#gaa3cd4ca118fd987560ae1855c904e1aa)(timer, timeout) |
|  | Trace Timer Status sync blocking. |
| #define | [sys\_port\_trace\_k\_timer\_status\_sync\_exit](#gab51aa6682136eb86a4fd141f61ece779)(timer, result) |
|  | Trace Time Status sync outcome. |

## Detailed Description

Timer Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga03a70d84ea0227829fb9528b0156c147)sys\_port\_trace\_k\_timer\_init

| #define sys\_port\_trace\_k\_timer\_init | ( |  | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Timer.

Parameters
:   | timer | Timer object |
    | --- | --- |

## [◆ ](#ga95b998ea6bf00692cb654a18787ab185)sys\_port\_trace\_k\_timer\_start

| #define sys\_port\_trace\_k\_timer\_start | ( |  | *timer*, |
| --- | --- | --- | --- |
|  |  |  | *duration*, |
|  |  |  | *period* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Timer start.

Parameters
:   | timer | Timer object |
    | --- | --- |
    | duration | Timer duration |
    | period | Timer period |

## [◆ ](#gaa3cd4ca118fd987560ae1855c904e1aa)sys\_port\_trace\_k\_timer\_status\_sync\_blocking

| #define sys\_port\_trace\_k\_timer\_status\_sync\_blocking | ( |  | *timer*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Timer Status sync blocking.

Parameters
:   | timer | Timer object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga0adf7e6ca5bdd89b7676836101ef37df)sys\_port\_trace\_k\_timer\_status\_sync\_enter

| #define sys\_port\_trace\_k\_timer\_status\_sync\_enter | ( |  | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Timer status sync entry.

Parameters
:   | timer | Timer object |
    | --- | --- |

## [◆ ](#gab51aa6682136eb86a4fd141f61ece779)sys\_port\_trace\_k\_timer\_status\_sync\_exit

| #define sys\_port\_trace\_k\_timer\_status\_sync\_exit | ( |  | *timer*, |
| --- | --- | --- | --- |
|  |  |  | *result* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Time Status sync outcome.

Parameters
:   | timer | Timer object |
    | --- | --- |
    | result | Return value |

## [◆ ](#ga81b6cba81190cc61cdd33f4ddb6f4550)sys\_port\_trace\_k\_timer\_stop

| #define sys\_port\_trace\_k\_timer\_stop | ( |  | *timer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Timer stop.

Parameters
:   | timer | Timer object |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
