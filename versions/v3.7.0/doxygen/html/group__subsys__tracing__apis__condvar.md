---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__condvar.html
original_path: doxygen/html/group__subsys__tracing__apis__condvar.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Conditional Variable Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Conditional Variable Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_condvar\_init](#gab9d1ce42bb6e6c2a762ed242ba364fa8)(condvar, ret) |
|  | Trace initialization of Conditional Variable. |
| #define | [sys\_port\_trace\_k\_condvar\_signal\_enter](#ga4b0f79f49b710928a38dc10ce22039e5)(condvar) |
|  | Trace Conditional Variable signaling start. |
| #define | [sys\_port\_trace\_k\_condvar\_signal\_blocking](#gab946fada5e51a069a13a21736a500669)(condvar, timeout) |
|  | Trace Conditional Variable signaling blocking. |
| #define | [sys\_port\_trace\_k\_condvar\_signal\_exit](#ga3992a8afdc375a4ecaa83cac302c7198)(condvar, ret) |
|  | Trace Conditional Variable signaling outcome. |
| #define | [sys\_port\_trace\_k\_condvar\_broadcast\_enter](#gadd5affb8afb73b5f76e24477d3d853bb)(condvar) |
|  | Trace Conditional Variable broadcast enter. |
| #define | [sys\_port\_trace\_k\_condvar\_broadcast\_exit](#ga9a013d5ab1bdd0752ec9bafb2ef4f370)(condvar, ret) |
|  | Trace Conditional Variable broadcast exit. |
| #define | [sys\_port\_trace\_k\_condvar\_wait\_enter](#ga30572aefa29d161af4e9e1841c59d98c)(condvar) |
|  | Trace Conditional Variable wait enter. |
| #define | [sys\_port\_trace\_k\_condvar\_wait\_exit](#ga07e95689443fb483886695a1533a5b08)(condvar, ret) |
|  | Trace Conditional Variable wait exit. |

## Detailed Description

Conditional Variable Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gadd5affb8afb73b5f76e24477d3d853bb)sys\_port\_trace\_k\_condvar\_broadcast\_enter

| #define sys\_port\_trace\_k\_condvar\_broadcast\_enter | ( |  | *condvar* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable broadcast enter.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |

## [◆ ](#ga9a013d5ab1bdd0752ec9bafb2ef4f370)sys\_port\_trace\_k\_condvar\_broadcast\_exit

| #define sys\_port\_trace\_k\_condvar\_broadcast\_exit | ( |  | *condvar*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable broadcast exit.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gab9d1ce42bb6e6c2a762ed242ba364fa8)sys\_port\_trace\_k\_condvar\_init

| #define sys\_port\_trace\_k\_condvar\_init | ( |  | *condvar*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Conditional Variable.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gab946fada5e51a069a13a21736a500669)sys\_port\_trace\_k\_condvar\_signal\_blocking

| #define sys\_port\_trace\_k\_condvar\_signal\_blocking | ( |  | *condvar*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable signaling blocking.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga4b0f79f49b710928a38dc10ce22039e5)sys\_port\_trace\_k\_condvar\_signal\_enter

| #define sys\_port\_trace\_k\_condvar\_signal\_enter | ( |  | *condvar* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable signaling start.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |

## [◆ ](#ga3992a8afdc375a4ecaa83cac302c7198)sys\_port\_trace\_k\_condvar\_signal\_exit

| #define sys\_port\_trace\_k\_condvar\_signal\_exit | ( |  | *condvar*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable signaling outcome.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga30572aefa29d161af4e9e1841c59d98c)sys\_port\_trace\_k\_condvar\_wait\_enter

| #define sys\_port\_trace\_k\_condvar\_wait\_enter | ( |  | *condvar* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable wait enter.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |

## [◆ ](#ga07e95689443fb483886695a1533a5b08)sys\_port\_trace\_k\_condvar\_wait\_exit

| #define sys\_port\_trace\_k\_condvar\_wait\_exit | ( |  | *condvar*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Conditional Variable wait exit.

Parameters
:   | condvar | Conditional Variable object |
    | --- | --- |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
