---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__msgq.html
original_path: doxygen/html/group__subsys__tracing__apis__msgq.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Message Queue Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Message Queue Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_msgq\_init](#ga94eae512e590d61c1c74f5d7eb552d50)(msgq) |
|  | Trace initialization of Message Queue. |
| #define | [sys\_port\_trace\_k\_msgq\_alloc\_init\_enter](#ga392ac9fe978d78ee1ca23c27f93e5053)(msgq) |
|  | Trace Message Queue alloc init attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_alloc\_init\_exit](#ga60973fcaae9be0a6b292bf2a5dfb4fb2)(msgq, ret) |
|  | Trace Message Queue alloc init attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_cleanup\_enter](#ga370c16cd808037db5dc605e91d3c21b8)(msgq) |
|  | Trace Message Queue cleanup attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_cleanup\_exit](#gaff32cb729fd32c7b008191cac1e2c881)(msgq, ret) |
|  | Trace Message Queue cleanup attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_put\_enter](#ga829e2b0d3420079777362f0b78f28d50)(msgq, timeout) |
|  | Trace Message Queue put attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_put\_blocking](#gaead1e1b345e029017b1951a3d112554f)(msgq, timeout) |
|  | Trace Message Queue put attempt blocking. |
| #define | [sys\_port\_trace\_k\_msgq\_put\_exit](#gab4794be3e4a68af3ada3667d98286747)(msgq, timeout, ret) |
|  | Trace Message Queue put attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_get\_enter](#ga1d79dbc50b8ddd0d3db803b7c747ede5)(msgq, timeout) |
|  | Trace Message Queue get attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_get\_blocking](#ga448baf7df9ec1abc4ec3a12609400b68)(msgq, timeout) |
|  | Trace Message Queue get attempt blockings. |
| #define | [sys\_port\_trace\_k\_msgq\_get\_exit](#ga2a549f567cda0646b853a9cb0b7e1eb2)(msgq, timeout, ret) |
|  | Trace Message Queue get attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_peek](#gad11e9f22177bf004f95d23750a2046a3)(msgq, ret) |
|  | Trace Message Queue peek. |
| #define | [sys\_port\_trace\_k\_msgq\_purge](#ga91530d1c6d10ce72cc5c9319c28b5e32)(msgq) |
|  | Trace Message Queue purge. |

## Detailed Description

Message Queue Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga392ac9fe978d78ee1ca23c27f93e5053)sys\_port\_trace\_k\_msgq\_alloc\_init\_enter

| #define sys\_port\_trace\_k\_msgq\_alloc\_init\_enter | ( |  | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue alloc init attempt entry.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |

## [◆ ](#ga60973fcaae9be0a6b292bf2a5dfb4fb2)sys\_port\_trace\_k\_msgq\_alloc\_init\_exit

| #define sys\_port\_trace\_k\_msgq\_alloc\_init\_exit | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue alloc init attempt outcome.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga370c16cd808037db5dc605e91d3c21b8)sys\_port\_trace\_k\_msgq\_cleanup\_enter

| #define sys\_port\_trace\_k\_msgq\_cleanup\_enter | ( |  | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue cleanup attempt entry.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |

## [◆ ](#gaff32cb729fd32c7b008191cac1e2c881)sys\_port\_trace\_k\_msgq\_cleanup\_exit

| #define sys\_port\_trace\_k\_msgq\_cleanup\_exit | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue cleanup attempt outcome.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga448baf7df9ec1abc4ec3a12609400b68)sys\_port\_trace\_k\_msgq\_get\_blocking

| #define sys\_port\_trace\_k\_msgq\_get\_blocking | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue get attempt blockings.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga1d79dbc50b8ddd0d3db803b7c747ede5)sys\_port\_trace\_k\_msgq\_get\_enter

| #define sys\_port\_trace\_k\_msgq\_get\_enter | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue get attempt entry.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga2a549f567cda0646b853a9cb0b7e1eb2)sys\_port\_trace\_k\_msgq\_get\_exit

| #define sys\_port\_trace\_k\_msgq\_get\_exit | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue get attempt outcome.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga94eae512e590d61c1c74f5d7eb552d50)sys\_port\_trace\_k\_msgq\_init

| #define sys\_port\_trace\_k\_msgq\_init | ( |  | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Message Queue.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |

## [◆ ](#gad11e9f22177bf004f95d23750a2046a3)sys\_port\_trace\_k\_msgq\_peek

| #define sys\_port\_trace\_k\_msgq\_peek | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue peek.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga91530d1c6d10ce72cc5c9319c28b5e32)sys\_port\_trace\_k\_msgq\_purge

| #define sys\_port\_trace\_k\_msgq\_purge | ( |  | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue purge.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |

## [◆ ](#gaead1e1b345e029017b1951a3d112554f)sys\_port\_trace\_k\_msgq\_put\_blocking

| #define sys\_port\_trace\_k\_msgq\_put\_blocking | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue put attempt blocking.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga829e2b0d3420079777362f0b78f28d50)sys\_port\_trace\_k\_msgq\_put\_enter

| #define sys\_port\_trace\_k\_msgq\_put\_enter | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue put attempt entry.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gab4794be3e4a68af3ada3667d98286747)sys\_port\_trace\_k\_msgq\_put\_exit

| #define sys\_port\_trace\_k\_msgq\_put\_exit | ( |  | *msgq*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Message Queue put attempt outcome.

Parameters
:   | msgq | Message Queue object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
