---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__net__timeout.html
original_path: doxygen/html/group__net__timeout.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network long timeout primitives and helpers

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network long timeout primitives and helpers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_timeout](structnet__timeout.md) |
|  | Generic struct for handling network timeouts. [More...](structnet__timeout.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_TIMEOUT\_MAX\_VALUE](#gab59bff1cb36902a27ee8e887ef39a4ce)   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) |
|  | Divisor used to support ms resolution timeouts. |

| Functions | |
| --- | --- |
| void | [net\_timeout\_set](#ga833e08b83a671d4adff799d648a12417) (struct [net\_timeout](structnet__timeout.md) \*timeout, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now) |
|  | Configure a network timeout structure. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [net\_timeout\_deadline](#ga3d9804474050d070fc4224e834f8cefc) (const struct [net\_timeout](structnet__timeout.md) \*timeout, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) now) |
|  | Return the 64-bit system time at which the timeout will complete. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_timeout\_remaining](#ga34e39484b19c39b3e37a4799848ad502) (const struct [net\_timeout](structnet__timeout.md) \*timeout, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now) |
|  | Calculate the remaining time to the timeout in whole seconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_timeout\_evaluate](#ga07b07966dd10929f6d3774467614f006) (struct [net\_timeout](structnet__timeout.md) \*timeout, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now) |
|  | Update state to reflect elapsed time and get new delay. |

## Detailed Description

Network long timeout primitives and helpers.

Since
:   1.14

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gab59bff1cb36902a27ee8e887ef39a4ce)NET\_TIMEOUT\_MAX\_VALUE

| #define NET\_TIMEOUT\_MAX\_VALUE   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) |
| --- |

`#include <[net_timeout.h](net__timeout_8h.md)>`

Divisor used to support ms resolution timeouts.

Because delays are processed in work queues which are not invoked synchronously with clock changes we need to be able to detect timeouts after they occur, which requires comparing "deadline" to "now" with enough "slop" to handle any observable latency due to "now" advancing past "deadline".

The simplest solution is to use the native conversion of the well-defined 32-bit unsigned difference to a 32-bit signed difference, which caps the maximum delay at INT32\_MAX. This is compatible with the standard mechanism for detecting completion of deadlines that do not overflow their representation.

## Function Documentation

## [◆ ](#ga3d9804474050d070fc4224e834f8cefc)net\_timeout\_deadline()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) net\_timeout\_deadline | ( | const struct [net\_timeout](structnet__timeout.md) \* | *timeout*, |
| --- | --- | --- | --- |
|  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | *now* ) |

`#include <[net_timeout.h](net__timeout_8h.md)>`

Return the 64-bit system time at which the timeout will complete.

Note
:   Correct behavior requires invocation of [net\_timeout\_evaluate()](#ga07b07966dd10929f6d3774467614f006) at its specified intervals.

Parameters
:   | timeout | state a pointer to the timeout state, initialized by [net\_timeout\_set()](#ga833e08b83a671d4adff799d648a12417) and maintained by [net\_timeout\_evaluate()](#ga07b07966dd10929f6d3774467614f006). |
    | --- | --- |
    | now | the full-precision value of [k\_uptime\_get()](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69 "Get system uptime.") relative to which the deadline will be calculated. |

Returns
:   the value of [k\_uptime\_get()](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69 "Get system uptime.") at which the timeout will expire.

## [◆ ](#ga07b07966dd10929f6d3774467614f006)net\_timeout\_evaluate()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_timeout\_evaluate | ( | struct [net\_timeout](structnet__timeout.md) \* | *timeout*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *now* ) |

`#include <[net_timeout.h](net__timeout_8h.md)>`

Update state to reflect elapsed time and get new delay.

This function must be invoked periodically to (1) apply the effect of elapsed time on what remains of a total delay that exceeded the maximum representable delay, and (2) determine that either the timeout has completed or that the infrastructure must wait a certain period before checking again for completion.

Parameters
:   | timeout | a pointer to the timeout state |
    | --- | --- |
    | now | the time relative to which the estimate of remaining time should be calculated. This should be recently captured value from [k\_uptime\_get\_32()](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b "Get system uptime (32-bit version)."). |

Return values
:   | 0 | if the timeout has completed |
    | --- | --- |
    | positive | the maximum delay until the state of this timeout should be re-evaluated, in milliseconds. |

## [◆ ](#ga34e39484b19c39b3e37a4799848ad502)net\_timeout\_remaining()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_timeout\_remaining | ( | const struct [net\_timeout](structnet__timeout.md) \* | *timeout*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *now* ) |

`#include <[net_timeout.h](net__timeout_8h.md)>`

Calculate the remaining time to the timeout in whole seconds.

Note
:   This function rounds the remaining time down, i.e. if the timeout will occur in 3500 milliseconds the value 3 will be returned.
:   Correct behavior requires invocation of [net\_timeout\_evaluate()](#ga07b07966dd10929f6d3774467614f006) at its specified intervals.

Parameters
:   | timeout | a pointer to the timeout state |
    | --- | --- |
    | now | the time relative to which the estimate of remaining time should be calculated. This should be recently captured value from [k\_uptime\_get\_32()](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b "Get system uptime (32-bit version)."). |

Return values
:   | 0 | if the timeout has completed. |
    | --- | --- |
    | positive | the remaining duration of the timeout, in seconds. |

## [◆ ](#ga833e08b83a671d4adff799d648a12417)net\_timeout\_set()

| void net\_timeout\_set | ( | struct [net\_timeout](structnet__timeout.md) \* | *timeout*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *lifetime*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *now* ) |

`#include <[net_timeout.h](net__timeout_8h.md)>`

Configure a network timeout structure.

Parameters
:   | timeout | a pointer to the timeout state. |
    | --- | --- |
    | lifetime | the duration of the timeout in seconds. |
    | now | the time at which the timeout started counting down, in milliseconds. This is generally a captured value of [k\_uptime\_get\_32()](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b "Get system uptime (32-bit version)."). |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
