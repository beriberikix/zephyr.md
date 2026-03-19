---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__subsys__tracing__apis__net.html
original_path: doxygen/html/group__subsys__tracing__apis__net.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Core Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Network Core Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_net\_recv\_data\_enter](#gab39c341e9aad487268cc934dd6104fc6)(iface, pkt) |
|  | Trace network data receive. |
| #define | [sys\_port\_trace\_net\_recv\_data\_exit](#ga4c0ba70ff0eef209005eb47c76e11682)(iface, pkt, ret) |
|  | Trace network data receive attempt. |
| #define | [sys\_port\_trace\_net\_send\_data\_enter](#ga9738aa7cefef4038974523bdf6d1a672)(pkt) |
|  | Trace network data send. |
| #define | [sys\_port\_trace\_net\_send\_data\_exit](#gaf3dde1664303355401f0765271dfedb4)(pkt, ret) |
|  | Trace network data send attempt. |
| #define | [sys\_port\_trace\_net\_rx\_time](#gace8a76a44fc01a1f14633c3a758d2811)(pkt, end\_time) |
|  | Trace network data receive time. |
| #define | [sys\_port\_trace\_net\_tx\_time](#ga1db4323543a538b3911b44f65ecf7d50)(pkt, end\_time) |
|  | Trace network data sent time. |

## Detailed Description

Network Core Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gab39c341e9aad487268cc934dd6104fc6)sys\_port\_trace\_net\_recv\_data\_enter

| #define sys\_port\_trace\_net\_recv\_data\_enter | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *pkt* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network data receive.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | pkt | Received network packet |

## [◆ ](#ga4c0ba70ff0eef209005eb47c76e11682)sys\_port\_trace\_net\_recv\_data\_exit

| #define sys\_port\_trace\_net\_recv\_data\_exit | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *pkt*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network data receive attempt.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | pkt | Received network packet |
    | ret | Return value |

## [◆ ](#gace8a76a44fc01a1f14633c3a758d2811)sys\_port\_trace\_net\_rx\_time

| #define sys\_port\_trace\_net\_rx\_time | ( |  | *pkt*, |
| --- | --- | --- | --- |
|  |  |  | *end\_time* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network data receive time.

Parameters
:   | pkt | Received network packet |
    | --- | --- |
    | end\_time | When the RX processing stopped for this pkt (in ticks) |

## [◆ ](#ga9738aa7cefef4038974523bdf6d1a672)sys\_port\_trace\_net\_send\_data\_enter

| #define sys\_port\_trace\_net\_send\_data\_enter | ( |  | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace network data send.

Parameters
:   | pkt | Network packet to send |
    | --- | --- |

## [◆ ](#gaf3dde1664303355401f0765271dfedb4)sys\_port\_trace\_net\_send\_data\_exit

| #define sys\_port\_trace\_net\_send\_data\_exit | ( |  | *pkt*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network data send attempt.

Parameters
:   | pkt | Received network packet |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga1db4323543a538b3911b44f65ecf7d50)sys\_port\_trace\_net\_tx\_time

| #define sys\_port\_trace\_net\_tx\_time | ( |  | *pkt*, |
| --- | --- | --- | --- |
|  |  |  | *end\_time* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network data sent time.

Parameters
:   | pkt | Sent network packet |
    | --- | --- |
    | end\_time | When the TX processing stopped for this pkt (in ticks) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
