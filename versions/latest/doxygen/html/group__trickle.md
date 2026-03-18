---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__trickle.html
original_path: doxygen/html/group__trickle.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Trickle Algorithm Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Trickle algorithm library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_trickle](structnet__trickle.md) |
|  | The variable names are taken directly from RFC 6206 when applicable. [More...](structnet__trickle.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_trickle\_cb\_t](#gaef7719dc563ae9bb93ed5313ed568b44)) (struct [net\_trickle](structnet__trickle.md) \*trickle, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) do\_suppress, void \*user\_data) |
|  | Trickle timer callback. |

| Functions | |
| --- | --- |
| int | [net\_trickle\_create](#gac412d65ad2a8483920de32c1e0ae6be5) (struct [net\_trickle](structnet__trickle.md) \*trickle, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) Imin, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) Imax, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k) |
|  | Create a Trickle timer. |
| int | [net\_trickle\_start](#ga6674fac118a187320d73dc742f0e216f) (struct [net\_trickle](structnet__trickle.md) \*trickle, [net\_trickle\_cb\_t](#gaef7719dc563ae9bb93ed5313ed568b44) cb, void \*user\_data) |
|  | Start a Trickle timer. |
| int | [net\_trickle\_stop](#ga8477e45a95abccfb714e3f3369686c6d) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | Stop a Trickle timer. |
| void | [net\_trickle\_consistency](#gacefb4b5ba518fd1e3f776df012998a9b) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | To be called by the protocol handler when it hears a consistent network transmission. |
| void | [net\_trickle\_inconsistency](#gad0815f9368a17532c8b5293a122cd8a9) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | To be called by the protocol handler when it hears an inconsistent network transmission. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_trickle\_is\_running](#ga95ceb01a7d56ce5a9d9128a42e1f8eb9) (struct [net\_trickle](structnet__trickle.md) \*trickle) |
|  | Check if the Trickle timer is running or not. |

## Detailed Description

Trickle algorithm library.

## Typedef Documentation

## [◆ ](#gaef7719dc563ae9bb93ed5313ed568b44)net\_trickle\_cb\_t

| typedef void(\* net\_trickle\_cb\_t) (struct [net\_trickle](structnet__trickle.md) \*trickle, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) do\_suppress, void \*user\_data) |
| --- |

`#include <[trickle.h](trickle_8h.md)>`

Trickle timer callback.

The callback is called after Trickle timeout expires.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | The trickle context to use. |
    | --- | --- |
    | do\_suppress | Is TX allowed (true) or not (false). |
    | user\_data | The user data given in [net\_trickle\_start()](#ga6674fac118a187320d73dc742f0e216f) call. |

## Function Documentation

## [◆ ](#gacefb4b5ba518fd1e3f776df012998a9b)net\_trickle\_consistency()

| void net\_trickle\_consistency | ( | struct [net\_trickle](structnet__trickle.md) \* | *trickle* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[trickle.h](trickle_8h.md)>`

To be called by the protocol handler when it hears a consistent network transmission.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | Pointer to Trickle struct. |
    | --- | --- |

## [◆ ](#gac412d65ad2a8483920de32c1e0ae6be5)net\_trickle\_create()

| int net\_trickle\_create | ( | struct [net\_trickle](structnet__trickle.md) \* | *trickle*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *Imin*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *Imax*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *k* ) |

`#include <[trickle.h](trickle_8h.md)>`

Create a Trickle timer.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | Pointer to Trickle struct. |
    | --- | --- |
    | Imin | Imin configuration parameter in ms. |
    | Imax | Max number of doublings. |
    | k | Redundancy constant parameter. See RFC 6206 for details. |

Returns
:   Return 0 if ok and <0 if error.

## [◆ ](#gad0815f9368a17532c8b5293a122cd8a9)net\_trickle\_inconsistency()

| void net\_trickle\_inconsistency | ( | struct [net\_trickle](structnet__trickle.md) \* | *trickle* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[trickle.h](trickle_8h.md)>`

To be called by the protocol handler when it hears an inconsistent network transmission.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | Pointer to Trickle struct. |
    | --- | --- |

## [◆ ](#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)net\_trickle\_is\_running()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_trickle\_is\_running | ( | struct [net\_trickle](structnet__trickle.md) \* | *trickle* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[trickle.h](trickle_8h.md)>`

Check if the Trickle timer is running or not.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | Pointer to Trickle struct. |
    | --- | --- |

Returns
:   Return True if timer is running and False if not.

## [◆ ](#ga6674fac118a187320d73dc742f0e216f)net\_trickle\_start()

| int net\_trickle\_start | ( | struct [net\_trickle](structnet__trickle.md) \* | *trickle*, |
| --- | --- | --- | --- |
|  |  | [net\_trickle\_cb\_t](#gaef7719dc563ae9bb93ed5313ed568b44) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[trickle.h](trickle_8h.md)>`

Start a Trickle timer.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | Pointer to Trickle struct. |
    | --- | --- |
    | cb | User callback to call at time T within the current trickle interval |
    | user\_data | User pointer that is passed to callback. |

Returns
:   Return 0 if ok and <0 if error.

## [◆ ](#ga8477e45a95abccfb714e3f3369686c6d)net\_trickle\_stop()

| int net\_trickle\_stop | ( | struct [net\_trickle](structnet__trickle.md) \* | *trickle* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[trickle.h](trickle_8h.md)>`

Stop a Trickle timer.

Parameters
:   | [Trickle Algorithm Library](group__trickle.md "Trickle algorithm library.") | Pointer to Trickle struct. |
    | --- | --- |

Returns
:   Return 0 if ok and <0 if error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
