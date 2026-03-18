---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__sem.html
original_path: doxygen/html/group__subsys__tracing__apis__sem.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Semaphore Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Semaphore Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_sem\_init](#gace327a058d058a940df14c95b031795b)(sem, ret) |
|  | Trace initialisation of a Semaphore. |
| #define | [sys\_port\_trace\_k\_sem\_give\_enter](#ga552d549c1e8346dbe1445a93e7fc17e9)(sem) |
|  | Trace giving a Semaphore entry. |
| #define | [sys\_port\_trace\_k\_sem\_give\_exit](#ga70d31e53b6e72d2343aa009fa5a98054)(sem) |
|  | Trace giving a Semaphore exit. |
| #define | [sys\_port\_trace\_k\_sem\_take\_enter](#ga216fe8bc373edbb0b48fc4ca7b1816c9)(sem, timeout) |
|  | Trace taking a Semaphore attempt start. |
| #define | [sys\_port\_trace\_k\_sem\_take\_blocking](#gade7546e098a12ce6d935b39f4978ac8d)(sem, timeout) |
|  | Trace taking a Semaphore attempt blocking. |
| #define | [sys\_port\_trace\_k\_sem\_take\_exit](#ga8085db47b86d539e65c107bb33469ee2)(sem, timeout, ret) |
|  | Trace taking a Semaphore attempt outcome. |
| #define | [sys\_port\_trace\_k\_sem\_reset](#ga1300af0463f93de0b29751b7a20307cb)(sem) |
|  | Trace resetting a Semaphore. |

## Detailed Description

Semaphore Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga552d549c1e8346dbe1445a93e7fc17e9)sys\_port\_trace\_k\_sem\_give\_enter

| #define sys\_port\_trace\_k\_sem\_give\_enter | ( |  | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace giving a Semaphore entry.

Parameters
:   | sem | Semaphore object |
    | --- | --- |

## [◆ ](#ga70d31e53b6e72d2343aa009fa5a98054)sys\_port\_trace\_k\_sem\_give\_exit

| #define sys\_port\_trace\_k\_sem\_give\_exit | ( |  | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace giving a Semaphore exit.

Parameters
:   | sem | Semaphore object |
    | --- | --- |

## [◆ ](#gace327a058d058a940df14c95b031795b)sys\_port\_trace\_k\_sem\_init

| #define sys\_port\_trace\_k\_sem\_init | ( |  | *sem*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialisation of a Semaphore.

Parameters
:   | sem | Semaphore object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga1300af0463f93de0b29751b7a20307cb)sys\_port\_trace\_k\_sem\_reset

| #define sys\_port\_trace\_k\_sem\_reset | ( |  | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace resetting a Semaphore.

Parameters
:   | sem | Semaphore object |
    | --- | --- |

## [◆ ](#gade7546e098a12ce6d935b39f4978ac8d)sys\_port\_trace\_k\_sem\_take\_blocking

| #define sys\_port\_trace\_k\_sem\_take\_blocking | ( |  | *sem*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace taking a Semaphore attempt blocking.

Parameters
:   | sem | Semaphore object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga216fe8bc373edbb0b48fc4ca7b1816c9)sys\_port\_trace\_k\_sem\_take\_enter

| #define sys\_port\_trace\_k\_sem\_take\_enter | ( |  | *sem*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace taking a Semaphore attempt start.

Parameters
:   | sem | Semaphore object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga8085db47b86d539e65c107bb33469ee2)sys\_port\_trace\_k\_sem\_take\_exit

| #define sys\_port\_trace\_k\_sem\_take\_exit | ( |  | *sem*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace taking a Semaphore attempt outcome.

Parameters
:   | sem | Semaphore object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
