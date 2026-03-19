---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__subsys__tracing__apis__pipe.html
original_path: doxygen/html/group__subsys__tracing__apis__pipe.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Pipe Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Pipe Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_pipe\_init](#ga1d51dc4110aba7c23de9b8f47e7ad5a8)(pipe) |
|  | Trace initialization of Pipe. |
| #define | [sys\_port\_trace\_k\_pipe\_cleanup\_enter](#ga63bc37ca2dbcf84fc87e13fdb2f21834)(pipe) |
|  | Trace Pipe cleanup entry. |
| #define | [sys\_port\_trace\_k\_pipe\_cleanup\_exit](#gaa367f4e1019380dde77ee881f22ab278)(pipe, ret) |
|  | Trace Pipe cleanup exit. |
| #define | [sys\_port\_trace\_k\_pipe\_alloc\_init\_enter](#ga6fdcad7deb3be98acd88cd8febd39247)(pipe) |
|  | Trace Pipe alloc init entry. |
| #define | [sys\_port\_trace\_k\_pipe\_alloc\_init\_exit](#ga011af7de686c1b360f0696a7dd1b173f)(pipe, ret) |
|  | Trace Pipe alloc init exit. |
| #define | [sys\_port\_trace\_k\_pipe\_flush\_enter](#ga9e3f6058f2370488cfb4d57676c3d5cd)(pipe) |
|  | Trace Pipe flush entry. |
| #define | [sys\_port\_trace\_k\_pipe\_flush\_exit](#gafdba63af20781901576344ef198da8a4)(pipe) |
|  | Trace Pipe flush exit. |
| #define | [sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter](#gaa81b667947689ac7edb866cb7c5beb81)(pipe) |
|  | Trace Pipe buffer flush entry. |
| #define | [sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit](#ga47d9a997d8daff89a1c4a41ac4bb327e)(pipe) |
|  | Trace Pipe buffer flush exit. |
| #define | [sys\_port\_trace\_k\_pipe\_put\_enter](#gad16f0673669f9700ebd3e4fc0b1466d8)(pipe, timeout) |
|  | Trace Pipe put attempt entry. |
| #define | [sys\_port\_trace\_k\_pipe\_put\_blocking](#ga314cffd927b410d3670f39a774a42206)(pipe, timeout) |
|  | Trace Pipe put attempt blocking. |
| #define | [sys\_port\_trace\_k\_pipe\_put\_exit](#ga20a131258373e32379273dd0ff08a672)(pipe, timeout, ret) |
|  | Trace Pipe put attempt outcome. |
| #define | [sys\_port\_trace\_k\_pipe\_get\_enter](#gaafa10362c5042f0f2e02b40b79768dbb)(pipe, timeout) |
|  | Trace Pipe get attempt entry. |
| #define | [sys\_port\_trace\_k\_pipe\_get\_blocking](#ga2dfb7cfd0b08beac72d254ac3063d42c)(pipe, timeout) |
|  | Trace Pipe get attempt blocking. |
| #define | [sys\_port\_trace\_k\_pipe\_get\_exit](#ga192cb7bafd2d04898b13e30aa96d483d)(pipe, timeout, ret) |
|  | Trace Pipe get attempt outcome. |

## Detailed Description

Pipe Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga6fdcad7deb3be98acd88cd8febd39247)sys\_port\_trace\_k\_pipe\_alloc\_init\_enter

| #define sys\_port\_trace\_k\_pipe\_alloc\_init\_enter | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe alloc init entry.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#ga011af7de686c1b360f0696a7dd1b173f)sys\_port\_trace\_k\_pipe\_alloc\_init\_exit

| #define sys\_port\_trace\_k\_pipe\_alloc\_init\_exit | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe alloc init exit.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaa81b667947689ac7edb866cb7c5beb81)sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter

| #define sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe buffer flush entry.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#ga47d9a997d8daff89a1c4a41ac4bb327e)sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit

| #define sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe buffer flush exit.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#ga63bc37ca2dbcf84fc87e13fdb2f21834)sys\_port\_trace\_k\_pipe\_cleanup\_enter

| #define sys\_port\_trace\_k\_pipe\_cleanup\_enter | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe cleanup entry.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#gaa367f4e1019380dde77ee881f22ab278)sys\_port\_trace\_k\_pipe\_cleanup\_exit

| #define sys\_port\_trace\_k\_pipe\_cleanup\_exit | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe cleanup exit.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga9e3f6058f2370488cfb4d57676c3d5cd)sys\_port\_trace\_k\_pipe\_flush\_enter

| #define sys\_port\_trace\_k\_pipe\_flush\_enter | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe flush entry.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#gafdba63af20781901576344ef198da8a4)sys\_port\_trace\_k\_pipe\_flush\_exit

| #define sys\_port\_trace\_k\_pipe\_flush\_exit | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe flush exit.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#ga2dfb7cfd0b08beac72d254ac3063d42c)sys\_port\_trace\_k\_pipe\_get\_blocking

| #define sys\_port\_trace\_k\_pipe\_get\_blocking | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe get attempt blocking.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gaafa10362c5042f0f2e02b40b79768dbb)sys\_port\_trace\_k\_pipe\_get\_enter

| #define sys\_port\_trace\_k\_pipe\_get\_enter | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe get attempt entry.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga192cb7bafd2d04898b13e30aa96d483d)sys\_port\_trace\_k\_pipe\_get\_exit

| #define sys\_port\_trace\_k\_pipe\_get\_exit | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe get attempt outcome.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga1d51dc4110aba7c23de9b8f47e7ad5a8)sys\_port\_trace\_k\_pipe\_init

| #define sys\_port\_trace\_k\_pipe\_init | ( |  | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Pipe.

Parameters
:   | pipe | Pipe object |
    | --- | --- |

## [◆ ](#ga314cffd927b410d3670f39a774a42206)sys\_port\_trace\_k\_pipe\_put\_blocking

| #define sys\_port\_trace\_k\_pipe\_put\_blocking | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe put attempt blocking.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gad16f0673669f9700ebd3e4fc0b1466d8)sys\_port\_trace\_k\_pipe\_put\_enter

| #define sys\_port\_trace\_k\_pipe\_put\_enter | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe put attempt entry.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga20a131258373e32379273dd0ff08a672)sys\_port\_trace\_k\_pipe\_put\_exit

| #define sys\_port\_trace\_k\_pipe\_put\_exit | ( |  | *pipe*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Pipe put attempt outcome.

Parameters
:   | pipe | Pipe object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
