---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis__work__poll.html
original_path: doxygen/html/group__subsys__tracing__apis__work__poll.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Work Poll Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Work Poll Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_work\_poll\_init\_enter](#gab720957a26a7e34d06af38200965b809)(work) |
|  | Trace initialisation of a Work Poll structure enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_init\_exit](#gab3f6f18ab804f82386fbf478e6f1925d)(work) |
|  | Trace initialisation of a Work Poll structure exit. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_enter](#gad81098506ed138f835230dec3af15076)(work\_q, work, timeout) |
|  | Trace work poll submit to queue enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_blocking](#gabfe31b99d03a49d4b2a5cb9e0403fed9)(work\_q, work, timeout) |
|  | Trace work poll submit to queue blocking. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_exit](#ga7605f1925f1f0e86d890c896586d8776)(work\_q, work, timeout, ret) |
|  | Trace work poll submit to queue exit. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_enter](#ga44a78c45b0bae26008d9ae5b410753b7)(work, timeout) |
|  | Trace work poll submit to system queue enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_exit](#ga5917fef8383ffdb6fb3f02a42f940059)(work, timeout, ret) |
|  | Trace work poll submit to system queue exit. |
| #define | [sys\_port\_trace\_k\_work\_poll\_cancel\_enter](#ga57e8e57814797b50e7e87e06503dc1f9)(work) |
|  | Trace work poll cancel enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_cancel\_exit](#ga3045330b53fa50489a2d3a17b14aa295)(work, ret) |
|  | Trace work poll cancel exit. |

## Detailed Description

Work Poll Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga57e8e57814797b50e7e87e06503dc1f9)sys\_port\_trace\_k\_work\_poll\_cancel\_enter

| #define sys\_port\_trace\_k\_work\_poll\_cancel\_enter | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll cancel enter.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#ga3045330b53fa50489a2d3a17b14aa295)sys\_port\_trace\_k\_work\_poll\_cancel\_exit

| #define sys\_port\_trace\_k\_work\_poll\_cancel\_exit | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll cancel exit.

Parameters
:   | work | Work structure |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gab720957a26a7e34d06af38200965b809)sys\_port\_trace\_k\_work\_poll\_init\_enter

| #define sys\_port\_trace\_k\_work\_poll\_init\_enter | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialisation of a Work Poll structure enter.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#gab3f6f18ab804f82386fbf478e6f1925d)sys\_port\_trace\_k\_work\_poll\_init\_exit

| #define sys\_port\_trace\_k\_work\_poll\_init\_exit | ( |  | *work* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialisation of a Work Poll structure exit.

Parameters
:   | work | Work structure |
    | --- | --- |

## [◆ ](#ga44a78c45b0bae26008d9ae5b410753b7)sys\_port\_trace\_k\_work\_poll\_submit\_enter

| #define sys\_port\_trace\_k\_work\_poll\_submit\_enter | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll submit to system queue enter.

Parameters
:   | work | Work structure |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga5917fef8383ffdb6fb3f02a42f940059)sys\_port\_trace\_k\_work\_poll\_submit\_exit

| #define sys\_port\_trace\_k\_work\_poll\_submit\_exit | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll submit to system queue exit.

Parameters
:   | work | Work structure |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#gabfe31b99d03a49d4b2a5cb9e0403fed9)sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_blocking

| #define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_blocking | ( |  | *work\_q*, |
| --- | --- | --- | --- |
|  |  |  | *work*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll submit to queue blocking.

Parameters
:   | work\_q | Work queue |
    | --- | --- |
    | work | Work structure |
    | timeout | Timeout period |

## [◆ ](#gad81098506ed138f835230dec3af15076)sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_enter

| #define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_enter | ( |  | *work\_q*, |
| --- | --- | --- | --- |
|  |  |  | *work*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll submit to queue enter.

Parameters
:   | work\_q | Work queue |
    | --- | --- |
    | work | Work structure |
    | timeout | Timeout period |

## [◆ ](#ga7605f1925f1f0e86d890c896586d8776)sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_exit

| #define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_exit | ( |  | *work\_q*, |
| --- | --- | --- | --- |
|  |  |  | *work*, |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace work poll submit to queue exit.

Parameters
:   | work\_q | Work queue |
    | --- | --- |
    | work | Work structure |
    | timeout | Timeout period |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
