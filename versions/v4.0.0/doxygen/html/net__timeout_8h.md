---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__timeout_8h.html
original_path: doxygen/html/net__timeout_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_timeout.h File Reference

Network timer with wrap around.
[More...](#details)

`#include <[string.h](string_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[limits.h](limits_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](net__timeout_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_timeout](structnet__timeout.md) |
|  | Generic struct for handling network timeouts. [More...](structnet__timeout.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_TIMEOUT\_MAX\_VALUE](group__net__timeout.md#gab59bff1cb36902a27ee8e887ef39a4ce)   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) |
|  | Divisor used to support ms resolution timeouts. |

| Functions | |
| --- | --- |
| void | [net\_timeout\_set](group__net__timeout.md#ga833e08b83a671d4adff799d648a12417) (struct [net\_timeout](structnet__timeout.md) \*timeout, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now) |
|  | Configure a network timeout structure. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [net\_timeout\_deadline](group__net__timeout.md#ga3d9804474050d070fc4224e834f8cefc) (const struct [net\_timeout](structnet__timeout.md) \*timeout, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) now) |
|  | Return the 64-bit system time at which the timeout will complete. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_timeout\_remaining](group__net__timeout.md#ga34e39484b19c39b3e37a4799848ad502) (const struct [net\_timeout](structnet__timeout.md) \*timeout, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now) |
|  | Calculate the remaining time to the timeout in whole seconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_timeout\_evaluate](group__net__timeout.md#ga07b07966dd10929f6d3774467614f006) (struct [net\_timeout](structnet__timeout.md) \*timeout, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now) |
|  | Update state to reflect elapsed time and get new delay. |

## Detailed Description

Network timer with wrap around.

Timer that runs longer than about 49 days needs to calculate wraps.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_timeout.h](net__timeout_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
