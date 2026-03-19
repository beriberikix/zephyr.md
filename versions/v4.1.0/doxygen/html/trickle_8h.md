---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/trickle_8h.html
original_path: doxygen/html/trickle_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

trickle.h File Reference

Trickle timer library.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`

[Go to the source code of this file.](trickle_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_trickle](structnet__trickle.md) |
|  | The variable names are taken directly from RFC 6206 when applicable. [More...](structnet__trickle.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44)) (struct [net\_trickle](structnet__trickle.md) \*trickle, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) do\_suppress, void \*user\_data) |
|  | Trickle timer callback. |

| Functions | |
| --- | --- |
| int | [net\_trickle\_create](group__trickle.md#gac412d65ad2a8483920de32c1e0ae6be5) (struct [net\_trickle](structnet__trickle.md) \*trickle, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) Imin, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) Imax, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k) |
|  | Create a Trickle timer. |
| int | [net\_trickle\_start](group__trickle.md#ga6674fac118a187320d73dc742f0e216f) (struct [net\_trickle](structnet__trickle.md) \*trickle, [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) cb, void \*user\_data) |
|  | Start a Trickle timer. |
| int | [net\_trickle\_stop](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | Stop a Trickle timer. |
| void | [net\_trickle\_consistency](group__trickle.md#gacefb4b5ba518fd1e3f776df012998a9b) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | To be called by the protocol handler when it hears a consistent network transmission. |
| void | [net\_trickle\_inconsistency](group__trickle.md#gad0815f9368a17532c8b5293a122cd8a9) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | To be called by the protocol handler when it hears an inconsistent network transmission. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_trickle\_is\_running](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | Check if the Trickle timer is running or not. |

## Detailed Description

Trickle timer library.

This implements Trickle timer as specified in RFC 6206

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [trickle.h](trickle_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
