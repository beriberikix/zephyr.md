---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__pm__system.html
original_path: doxygen/html/group__subsys__tracing__apis__pm__system.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

System PM Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

System PM Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_pm\_system\_suspend\_enter](#ga1d8c01fe22ef0f7ac8fdfb47de55f58e)(ticks) |
|  | Trace system suspend call entry. |
| #define | [sys\_port\_trace\_pm\_system\_suspend\_exit](#gaabc547256f20c5da3b25a14dbd047014)(ticks, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Trace system suspend call exit. |

## Detailed Description

System PM Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga1d8c01fe22ef0f7ac8fdfb47de55f58e)sys\_port\_trace\_pm\_system\_suspend\_enter

| #define sys\_port\_trace\_pm\_system\_suspend\_enter | ( |  | *ticks* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace system suspend call entry.

Parameters
:   | ticks | Ticks. |
    | --- | --- |

## [◆ ](#gaabc547256f20c5da3b25a14dbd047014)sys\_port\_trace\_pm\_system\_suspend\_exit

| #define sys\_port\_trace\_pm\_system\_suspend\_exit | ( |  | *ticks*, |
| --- | --- | --- | --- |
|  |  |  | *[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace system suspend call exit.

Parameters
:   | ticks | Ticks. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | PM state. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
