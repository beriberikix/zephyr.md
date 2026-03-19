---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__mutex.html
original_path: doxygen/html/group__subsys__tracing__apis__mutex.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Mutex Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Mutex Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_mutex\_init](#gaefe38feb9aa638b35fd4e723afcebf37)(mutex, ret) |
|  | Trace initialization of Mutex. |
| #define | [sys\_port\_trace\_k\_mutex\_lock\_enter](#ga5ed2f76aec9c128f163a2e3159e29c80)(mutex, timeout) |
|  | Trace Mutex lock attempt start. |
| #define | [sys\_port\_trace\_k\_mutex\_lock\_blocking](#gaae15023daa241367414afaab085acd2c)(mutex, timeout) |
|  | Trace Mutex lock attempt blocking. |
| #define | [sys\_port\_trace\_k\_mutex\_lock\_exit](#ga31bdc51723303de3bc93d41b36149e57)(mutex, timeout, ret) |
|  | Trace Mutex lock attempt outcome. |
| #define | [sys\_port\_trace\_k\_mutex\_unlock\_enter](#ga39611be3e36741442a62a98adeef9ee7)(mutex) |
|  | Trace Mutex unlock entry. |
| #define | [sys\_port\_trace\_k\_mutex\_unlock\_exit](#ga53c7bd3fc251865ae1a6e79da7a001b1)(mutex, ret) |
|  | Trace Mutex unlock exit. |

## Detailed Description

Mutex Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gaefe38feb9aa638b35fd4e723afcebf37)sys\_port\_trace\_k\_mutex\_init

| #define sys\_port\_trace\_k\_mutex\_init | ( |  | *mutex*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Mutex.

Parameters
:   | mutex | Mutex object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaae15023daa241367414afaab085acd2c)sys\_port\_trace\_k\_mutex\_lock\_blocking

| #define sys\_port\_trace\_k\_mutex\_lock\_blocking | ( |  | *mutex*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Mutex lock attempt blocking.

Parameters
:   | mutex | Mutex object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga5ed2f76aec9c128f163a2e3159e29c80)sys\_port\_trace\_k\_mutex\_lock\_enter

| #define sys\_port\_trace\_k\_mutex\_lock\_enter | ( |  | *mutex*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Mutex lock attempt start.

Parameters
:   | mutex | Mutex object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga31bdc51723303de3bc93d41b36149e57)sys\_port\_trace\_k\_mutex\_lock\_exit

| #define sys\_port\_trace\_k\_mutex\_lock\_exit | ( |  | *mutex*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Mutex lock attempt outcome.

Parameters
:   | mutex | Mutex object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga39611be3e36741442a62a98adeef9ee7)sys\_port\_trace\_k\_mutex\_unlock\_enter

| #define sys\_port\_trace\_k\_mutex\_unlock\_enter | ( |  | *mutex* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Mutex unlock entry.

Parameters
:   | mutex | Mutex object |
    | --- | --- |

## [◆ ](#ga53c7bd3fc251865ae1a6e79da7a001b1)sys\_port\_trace\_k\_mutex\_unlock\_exit

| #define sys\_port\_trace\_k\_mutex\_unlock\_exit | ( |  | *mutex*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Mutex unlock exit.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
