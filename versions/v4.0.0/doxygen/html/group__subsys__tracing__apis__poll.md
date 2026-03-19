---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__subsys__tracing__apis__poll.html
original_path: doxygen/html/group__subsys__tracing__apis__poll.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Poll Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Poll Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_poll\_api\_event\_init](#ga83053d6bfc7ad8b070741f38d6606bc1)(event) |
|  | Trace initialisation of a Poll Event. |
| #define | [sys\_port\_trace\_k\_poll\_api\_poll\_enter](#gac44ecc90dc3b407b09e2d45590496e17)(events) |
|  | Trace Polling call start. |
| #define | [sys\_port\_trace\_k\_poll\_api\_poll\_exit](#gaf8794133d6ddc29740dfc73b9edbee12)(events, ret) |
|  | Trace Polling call outcome. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_init](#gaab0dc4527d89c0e0b41d21a76ecfb120)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Trace initialisation of a Poll Signal. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_reset](#ga5addc3fa68d6afe454ad7721c8fa17c4)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Trace resetting of Poll Signal. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_check](#ga336dab8d86b07908e641e9845d75be70)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Trace checking of Poll Signal. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_raise](#gaeb1f753becfbe92f089eed23825acb4b)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), ret) |
|  | Trace raising of Poll Signal. |

## Detailed Description

Poll Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga83053d6bfc7ad8b070741f38d6606bc1)sys\_port\_trace\_k\_poll\_api\_event\_init

| #define sys\_port\_trace\_k\_poll\_api\_event\_init | ( |  | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialisation of a Poll Event.

Parameters
:   | event | Poll Event |
    | --- | --- |

## [◆ ](#gac44ecc90dc3b407b09e2d45590496e17)sys\_port\_trace\_k\_poll\_api\_poll\_enter

| #define sys\_port\_trace\_k\_poll\_api\_poll\_enter | ( |  | *events* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Polling call start.

Parameters
:   | events | Poll Events |
    | --- | --- |

## [◆ ](#gaf8794133d6ddc29740dfc73b9edbee12)sys\_port\_trace\_k\_poll\_api\_poll\_exit

| #define sys\_port\_trace\_k\_poll\_api\_poll\_exit | ( |  | *events*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Polling call outcome.

Parameters
:   | events | Poll Events |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga336dab8d86b07908e641e9845d75be70)sys\_port\_trace\_k\_poll\_api\_signal\_check

| #define sys\_port\_trace\_k\_poll\_api\_signal\_check | ( |  | *[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace checking of Poll Signal.

Parameters
:   | [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69) | Poll Signal |
    | --- | --- |

## [◆ ](#gaab0dc4527d89c0e0b41d21a76ecfb120)sys\_port\_trace\_k\_poll\_api\_signal\_init

| #define sys\_port\_trace\_k\_poll\_api\_signal\_init | ( |  | *[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialisation of a Poll Signal.

Parameters
:   | [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69) | Poll Signal |
    | --- | --- |

## [◆ ](#gaeb1f753becfbe92f089eed23825acb4b)sys\_port\_trace\_k\_poll\_api\_signal\_raise

| #define sys\_port\_trace\_k\_poll\_api\_signal\_raise | ( |  | *[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace raising of Poll Signal.

Parameters
:   | [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69) | Poll Signal |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga5addc3fa68d6afe454ad7721c8fa17c4)sys\_port\_trace\_k\_poll\_api\_signal\_reset

| #define sys\_port\_trace\_k\_poll\_api\_signal\_reset | ( |  | *[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace resetting of Poll Signal.

Parameters
:   | [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69) | Poll Signal |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
