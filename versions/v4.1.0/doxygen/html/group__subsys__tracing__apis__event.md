---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__event.html
original_path: doxygen/html/group__subsys__tracing__apis__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Event Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Event Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_event\_init](#gae212c1b330d476613629501d62be0994)(event) |
|  | Trace initialisation of an Event. |
| #define | [sys\_port\_trace\_k\_event\_post\_enter](#ga20092082696c6c9fe3b8870bd3523b52)(event, events, events\_mask) |
|  | Trace posting of an Event call entry. |
| #define | [sys\_port\_trace\_k\_event\_post\_exit](#gac58a047db800cca608087d6b2cec37f9)(event, events, events\_mask) |
|  | Trace posting of an Event call exit. |
| #define | [sys\_port\_trace\_k\_event\_wait\_enter](#ga6b01461ff2fa0cf2c3c19dbed2f8c4c3)(event, events, options, timeout) |
|  | Trace waiting of an Event call entry. |
| #define | [sys\_port\_trace\_k\_event\_wait\_blocking](#ga008a96d80f3f90dcffbc74f43d66b9be)(event, events, options, timeout) |
|  | Trace waiting of an Event call exit. |
| #define | [sys\_port\_trace\_k\_event\_wait\_exit](#ga874698f8eff5237fefacc1be761b2661)(event, events, ret) |
|  | Trace waiting of an Event call exit. |

## Detailed Description

Event Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gae212c1b330d476613629501d62be0994)sys\_port\_trace\_k\_event\_init

| #define sys\_port\_trace\_k\_event\_init | ( |  | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialisation of an Event.

Parameters
:   | event | Event object |
    | --- | --- |

## [◆ ](#ga20092082696c6c9fe3b8870bd3523b52)sys\_port\_trace\_k\_event\_post\_enter

| #define sys\_port\_trace\_k\_event\_post\_enter | ( |  | *event*, |
| --- | --- | --- | --- |
|  |  |  | *events*, |
|  |  |  | *events\_mask* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace posting of an Event call entry.

Parameters
:   | event | Event object |
    | --- | --- |
    | events | Set of posted events |
    | events\_mask | Mask to apply against posted events |

## [◆ ](#gac58a047db800cca608087d6b2cec37f9)sys\_port\_trace\_k\_event\_post\_exit

| #define sys\_port\_trace\_k\_event\_post\_exit | ( |  | *event*, |
| --- | --- | --- | --- |
|  |  |  | *events*, |
|  |  |  | *events\_mask* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace posting of an Event call exit.

Parameters
:   | event | Event object |
    | --- | --- |
    | events | Set of posted events |
    | events\_mask | Mask to apply against posted events |

## [◆ ](#ga008a96d80f3f90dcffbc74f43d66b9be)sys\_port\_trace\_k\_event\_wait\_blocking

| #define sys\_port\_trace\_k\_event\_wait\_blocking | ( |  | *event*, |
| --- | --- | --- | --- |
|  |  |  | *events*, |
|  |  |  | *options*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace waiting of an Event call exit.

Parameters
:   | event | Event object |
    | --- | --- |
    | events | Set of events for which to wait |
    | options | Event wait options |
    | timeout | Timeout period |

## [◆ ](#ga6b01461ff2fa0cf2c3c19dbed2f8c4c3)sys\_port\_trace\_k\_event\_wait\_enter

| #define sys\_port\_trace\_k\_event\_wait\_enter | ( |  | *event*, |
| --- | --- | --- | --- |
|  |  |  | *events*, |
|  |  |  | *options*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace waiting of an Event call entry.

Parameters
:   | event | Event object |
    | --- | --- |
    | events | Set of events for which to wait |
    | options | Event wait options |
    | timeout | Timeout period |

## [◆ ](#ga874698f8eff5237fefacc1be761b2661)sys\_port\_trace\_k\_event\_wait\_exit

| #define sys\_port\_trace\_k\_event\_wait\_exit | ( |  | *event*, |
| --- | --- | --- | --- |
|  |  |  | *events*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace waiting of an Event call exit.

Parameters
:   | event | Event object |
    | --- | --- |
    | events | Set of events for which to wait |
    | ret | Set of received events |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
