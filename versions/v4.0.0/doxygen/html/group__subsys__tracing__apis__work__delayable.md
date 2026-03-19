---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__subsys__tracing__apis__work__delayable.html
original_path: doxygen/html/group__subsys__tracing__apis__work__delayable.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Work Delayable Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Work Delayable Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_work\_delayable\_init](#ga2b7d8ad2173665808061ccc1afd52a06)(dwork) |
|  | Trace initialisation of a Delayable Work structure. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_for\_queue\_enter](#gab71fd0042892d3e6c3e486cee63c9564)(queue, dwork, delay) |
|  | Trace schedule delayable work for queue enter. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_for\_queue\_exit](#ga4d2160569df2886318039bfdae69d979)(queue, dwork, delay, ret) |
|  | Trace schedule delayable work for queue exit. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_enter](#gacda1641af1768d815d3cc3e83c1e2456)(dwork, delay) |
|  | Trace schedule delayable work for system work queue enter. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_exit](#ga8c5b232168b9bede0cd73f20513e081c)(dwork, delay, ret) |
|  | Trace schedule delayable work for system work queue exit. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_enter](#ga8d6e93ed7d85a17ffdb651e3399b0e16)(queue, dwork, delay) |
|  | Trace reschedule delayable work for queue enter. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_exit](#ga636e418e8baf90aaffe3e86b86b3b047)(queue, dwork, delay, ret) |
|  | Trace reschedule delayable work for queue exit. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_enter](#gafe5b13e8aae388e9b855081450a065e1)(dwork, delay) |
|  | Trace reschedule delayable work for system queue enter. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_exit](#gaf7789cfa1a943b58e6ee93e8ec9dee57)(dwork, delay, ret) |
|  | Trace reschedule delayable work for system queue exit. |
| #define | [sys\_port\_trace\_k\_work\_flush\_delayable\_enter](#ga949c751bc5226d1b46fbf7478c1ee5a3)(dwork, sync) |
|  | Trace delayable work flush enter. |
| #define | [sys\_port\_trace\_k\_work\_flush\_delayable\_exit](#gab62f6bce942728370aefa0903a8b79a0)(dwork, sync, ret) |
|  | Trace delayable work flush exit. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_enter](#gae80301ae580a3de83f239d9973b3829d)(dwork) |
|  | Trace delayable work cancel enter. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_exit](#gaef6b739acf79e63e94d172e6667269ce)(dwork, ret) |
|  | Trace delayable work cancel enter. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_enter](#gaaa466d5bd2529b6a8ec5672a0054b8f7)(dwork, sync) |
|  | Trace delayable work cancel sync enter. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_exit](#ga7f2934c863c45a5bb71d1ba0401a9fe9)(dwork, sync, ret) |
|  | Trace delayable work cancel sync enter. |

## Detailed Description

Work Delayable Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gae80301ae580a3de83f239d9973b3829d)sys\_port\_trace\_k\_work\_cancel\_delayable\_enter

| #define sys\_port\_trace\_k\_work\_cancel\_delayable\_enter | ( |  | *dwork* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace delayable work cancel enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |

## [◆ ](#gaef6b739acf79e63e94d172e6667269ce)sys\_port\_trace\_k\_work\_cancel\_delayable\_exit

| #define sys\_port\_trace\_k\_work\_cancel\_delayable\_exit | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace delayable work cancel enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaaa466d5bd2529b6a8ec5672a0054b8f7)sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_enter

| #define sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_enter | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *sync* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace delayable work cancel sync enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | sync | Sync object |

## [◆ ](#ga7f2934c863c45a5bb71d1ba0401a9fe9)sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_exit

| #define sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_exit | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *sync*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace delayable work cancel sync enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | sync | Sync object |
    | ret | Return value |

## [◆ ](#ga2b7d8ad2173665808061ccc1afd52a06)sys\_port\_trace\_k\_work\_delayable\_init

| #define sys\_port\_trace\_k\_work\_delayable\_init | ( |  | *dwork* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialisation of a Delayable Work structure.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |

## [◆ ](#ga949c751bc5226d1b46fbf7478c1ee5a3)sys\_port\_trace\_k\_work\_flush\_delayable\_enter

| #define sys\_port\_trace\_k\_work\_flush\_delayable\_enter | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *sync* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace delayable work flush enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | sync | Sync object |

## [◆ ](#gab62f6bce942728370aefa0903a8b79a0)sys\_port\_trace\_k\_work\_flush\_delayable\_exit

| #define sys\_port\_trace\_k\_work\_flush\_delayable\_exit | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *sync*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace delayable work flush exit.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | sync | Sync object |
    | ret | Return value |

## [◆ ](#gafe5b13e8aae388e9b855081450a065e1)sys\_port\_trace\_k\_work\_reschedule\_enter

| #define sys\_port\_trace\_k\_work\_reschedule\_enter | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *delay* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace reschedule delayable work for system queue enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | delay | Delay period |

## [◆ ](#gaf7789cfa1a943b58e6ee93e8ec9dee57)sys\_port\_trace\_k\_work\_reschedule\_exit

| #define sys\_port\_trace\_k\_work\_reschedule\_exit | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *delay*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace reschedule delayable work for system queue exit.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | delay | Delay period |
    | ret | Return value |

## [◆ ](#ga8d6e93ed7d85a17ffdb651e3399b0e16)sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_enter

| #define sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_enter | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *dwork*, |
|  |  |  | *delay* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace reschedule delayable work for queue enter.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |
    | dwork | Delayable Work structure |
    | delay | Delay period |

## [◆ ](#ga636e418e8baf90aaffe3e86b86b3b047)sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_exit

| #define sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *dwork*, |
|  |  |  | *delay*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace reschedule delayable work for queue exit.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |
    | dwork | Delayable Work structure |
    | delay | Delay period |
    | ret | Return value |

## [◆ ](#gacda1641af1768d815d3cc3e83c1e2456)sys\_port\_trace\_k\_work\_schedule\_enter

| #define sys\_port\_trace\_k\_work\_schedule\_enter | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *delay* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace schedule delayable work for system work queue enter.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | delay | Delay period |

## [◆ ](#ga8c5b232168b9bede0cd73f20513e081c)sys\_port\_trace\_k\_work\_schedule\_exit

| #define sys\_port\_trace\_k\_work\_schedule\_exit | ( |  | *dwork*, |
| --- | --- | --- | --- |
|  |  |  | *delay*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace schedule delayable work for system work queue exit.

Parameters
:   | dwork | Delayable Work structure |
    | --- | --- |
    | delay | Delay period |
    | ret | Return value |

## [◆ ](#gab71fd0042892d3e6c3e486cee63c9564)sys\_port\_trace\_k\_work\_schedule\_for\_queue\_enter

| #define sys\_port\_trace\_k\_work\_schedule\_for\_queue\_enter | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *dwork*, |
|  |  |  | *delay* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace schedule delayable work for queue enter.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |
    | dwork | Delayable Work structure |
    | delay | Delay period |

## [◆ ](#ga4d2160569df2886318039bfdae69d979)sys\_port\_trace\_k\_work\_schedule\_for\_queue\_exit

| #define sys\_port\_trace\_k\_work\_schedule\_for\_queue\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *dwork*, |
|  |  |  | *delay*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace schedule delayable work for queue exit.

Parameters
:   | queue | Work Queue structure |
    | --- | --- |
    | dwork | Delayable Work structure |
    | delay | Delay period |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
