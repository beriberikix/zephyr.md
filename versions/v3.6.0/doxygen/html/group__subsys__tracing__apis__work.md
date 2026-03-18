---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis__work.html
original_path: doxygen/html/group__subsys__tracing__apis__work.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Work Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Work Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_work\_init](#gab31f3a43ff4a836a28ba0c21a24370e7)(work) |
|  | Trace initialisation of a Work structure. |
| #define | [sys\_port\_trace\_k\_work\_submit\_to\_queue\_enter](#gac4ec7fb1a85aaf608d0b46734fabc812)(queue, work) |
|  | Trace submit work to work queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_submit\_to\_queue\_exit](#ga8807dc91f2f025f400a4e3a435b13588)(queue, work, ret) |
|  | Trace submit work to work queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_submit\_enter](#ga597a2efeb4fc680149a51e7abceba2a7)(work) |
|  | Trace submit work to system work queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_submit\_exit](#ga4996ec4ae496a2a55dd756f6e4474107)(work, ret) |
|  | Trace submit work to system work queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_flush\_enter](#ga20f5d05e4c1be9a21e42072291272fc9)(work) |
|  | Trace flush work call entry. |
| #define | [sys\_port\_trace\_k\_work\_flush\_blocking](#gae21005546cf2025ac4eff76e09da4d0e)(work, timeout) |
|  | Trace flush work call blocking. |
| #define | [sys\_port\_trace\_k\_work\_flush\_exit](#gaa50f5a34b4cdc0ba46a4d153f0d48b39)(work, ret) |
|  | Trace flush work call exit. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_enter](#gaa2ffb1718ddc49a4f3a727e15d3e1f11)(work) |
|  | Trace cancel work call entry. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_exit](#ga9a2aa3433ec4a0a2fceb8d1c5ce682f3)(work, ret) |
|  | Trace cancel work call exit. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_sync\_enter](#ga8f2b37c2740c6883939a94ae6aa3ea51)(work, sync) |
|  | Trace cancel sync work call entry. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_sync\_blocking](#ga9d05cb22b905b5ae99174fe8523a8033)(work, sync) |
|  | Trace cancel sync work call blocking. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_sync\_exit](#gae59b7476b056d828bbf269c3f60e5687)(work, sync, ret) |
|  | Trace cancel sync work call exit. |

## Detailed Description

Work Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gaa2ffb1718ddc49a4f3a727e15d3e1f11)sys\_port\_trace\_k\_work\_cancel\_enter

| #define sys\_port\_trace\_k\_work\_cancel\_enter | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace cancel work call entry.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#ga9a2aa3433ec4a0a2fceb8d1c5ce682f3)sys\_port\_trace\_k\_work\_cancel\_exit

| #define sys\_port\_trace\_k\_work\_cancel\_exit | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace cancel work call exit.

Parameters
:   | work | Work structure |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga9d05cb22b905b5ae99174fe8523a8033)sys\_port\_trace\_k\_work\_cancel\_sync\_blocking

| #define sys\_port\_trace\_k\_work\_cancel\_sync\_blocking | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *sync* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace cancel sync work call blocking.

Parameters
:   | work | Work structure |
    | --- | --- |
    | sync | Sync object |

## [◆ ](#ga8f2b37c2740c6883939a94ae6aa3ea51)sys\_port\_trace\_k\_work\_cancel\_sync\_enter

| #define sys\_port\_trace\_k\_work\_cancel\_sync\_enter | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *sync* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace cancel sync work call entry.

Parameters
:   | work | Work structure |
    | --- | --- |
    | sync | Sync object |

## [◆ ](#gae59b7476b056d828bbf269c3f60e5687)sys\_port\_trace\_k\_work\_cancel\_sync\_exit

| #define sys\_port\_trace\_k\_work\_cancel\_sync\_exit | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *sync*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace cancel sync work call exit.

Parameters
:   | work | Work structure |
    | --- | --- |
    | sync | Sync object |
    | ret | Return value |

## [◆ ](#gae21005546cf2025ac4eff76e09da4d0e)sys\_port\_trace\_k\_work\_flush\_blocking

| #define sys\_port\_trace\_k\_work\_flush\_blocking | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace flush work call blocking.

Parameters
:   | work | Work structure |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga20f5d05e4c1be9a21e42072291272fc9)sys\_port\_trace\_k\_work\_flush\_enter

| #define sys\_port\_trace\_k\_work\_flush\_enter | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace flush work call entry.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#gaa50f5a34b4cdc0ba46a4d153f0d48b39)sys\_port\_trace\_k\_work\_flush\_exit

| #define sys\_port\_trace\_k\_work\_flush\_exit | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace flush work call exit.

Parameters
:   | work | Work structure |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gab31f3a43ff4a836a28ba0c21a24370e7)sys\_port\_trace\_k\_work\_init

| #define sys\_port\_trace\_k\_work\_init | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialisation of a Work structure.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#ga597a2efeb4fc680149a51e7abceba2a7)sys\_port\_trace\_k\_work\_submit\_enter

| #define sys\_port\_trace\_k\_work\_submit\_enter | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace submit work to system work queue call entry.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#ga4996ec4ae496a2a55dd756f6e4474107)sys\_port\_trace\_k\_work\_submit\_exit

| #define sys\_port\_trace\_k\_work\_submit\_exit | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace submit work to system work queue call exit.

Parameters
:   | work | Work structure |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gac4ec7fb1a85aaf608d0b46734fabc812)sys\_port\_trace\_k\_work\_submit\_to\_queue\_enter

| #define sys\_port\_trace\_k\_work\_submit\_to\_queue\_enter | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *work* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace submit work to work queue call entry.

Parameters
:   | queue | Work queue structure |
    | --- | --- |
    | work | Work structure |

## [◆ ](#ga8807dc91f2f025f400a4e3a435b13588)sys\_port\_trace\_k\_work\_submit\_to\_queue\_exit

| #define sys\_port\_trace\_k\_work\_submit\_to\_queue\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *work*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace submit work to work queue call exit.

Parameters
:   | queue | Work queue structure |
    | --- | --- |
    | work | Work structure |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
