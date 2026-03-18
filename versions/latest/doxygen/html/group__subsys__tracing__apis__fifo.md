---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis__fifo.html
original_path: doxygen/html/group__subsys__tracing__apis__fifo.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FIFO Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

FIFO Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_fifo\_init\_enter](#gac0da5eca137a970c67b7b94a568c93e6)(fifo) |
|  | Trace initialization of FIFO Queue entry. |
| #define | [sys\_port\_trace\_k\_fifo\_init\_exit](#gaaf6c7c710377f449d52c5d6f5f7103c8)(fifo) |
|  | Trace initialization of FIFO Queue exit. |
| #define | [sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter](#ga81e706aff605468683a96b14940745e7)(fifo) |
|  | Trace FIFO Queue cancel wait entry. |
| #define | [sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit](#ga03ccb2bb3141c2842959ba77e4cd7337)(fifo) |
|  | Trace FIFO Queue cancel wait exit. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_enter](#gaac5f6b9e77dad9de4652d24502ab46d0)(fifo, data) |
|  | Trace FIFO Queue put entry. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_exit](#ga7a1d15a538f23d2b7f290435803cd73e)(fifo, data) |
|  | Trace FIFO Queue put exit. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_enter](#ga9c433ad8dc99ac38b8d5b4755da05c67)(fifo, data) |
|  | Trace FIFO Queue alloc put entry. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_exit](#gad9871fb1487a387a4f73e94bccb99a6d)(fifo, data, ret) |
|  | Trace FIFO Queue alloc put exit. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_list\_enter](#gace20fdce59a99b92c8ac3711c4085b28)(fifo, head, tail) |
|  | Trace FIFO Queue put list entry. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_list\_exit](#ga739360e2cefa158f22ce20a1e9369aea)(fifo, head, tail) |
|  | Trace FIFO Queue put list exit. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter](#gaf975d817bdefc64b9329330f6cd88d21)(fifo, list) |
|  | Trace FIFO Queue put slist entry. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit](#gae1c620ec17a1f7a899a1e5cba996644e)(fifo, list) |
|  | Trace FIFO Queue put slist exit. |
| #define | [sys\_port\_trace\_k\_fifo\_get\_enter](#gaa3539eea74888c6257c5f5d456748155)(fifo, timeout) |
|  | Trace FIFO Queue get entry. |
| #define | [sys\_port\_trace\_k\_fifo\_get\_exit](#gae6f06386f224063ee756e8ff0000dfe4)(fifo, timeout, ret) |
|  | Trace FIFO Queue get exit. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_head\_enter](#gab0fea5751e0296e623606e54efe5687b)(fifo) |
|  | Trace FIFO Queue peek head entry. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_head\_exit](#ga06b74415be416b137092cb72187c1fb6)(fifo, ret) |
|  | Trace FIFO Queue peek head exit. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_tail\_enter](#gad9f9b3193ed2c7270030036aef8d343d)(fifo) |
|  | Trace FIFO Queue peek tail entry. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_tail\_exit](#gae33baafbaac06ada7d6b53026a973d81)(fifo, ret) |
|  | Trace FIFO Queue peek tail exit. |

## Detailed Description

FIFO Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga9c433ad8dc99ac38b8d5b4755da05c67)sys\_port\_trace\_k\_fifo\_alloc\_put\_enter

| #define sys\_port\_trace\_k\_fifo\_alloc\_put\_enter | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue alloc put entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | data | Data item |

## [◆ ](#gad9871fb1487a387a4f73e94bccb99a6d)sys\_port\_trace\_k\_fifo\_alloc\_put\_exit

| #define sys\_port\_trace\_k\_fifo\_alloc\_put\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *data*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue alloc put exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | data | Data item |
    | ret | Return value |

## [◆ ](#gaf975d817bdefc64b9329330f6cd88d21)sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter

| #define sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *list* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue put slist entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | list | Syslist object |

## [◆ ](#gae1c620ec17a1f7a899a1e5cba996644e)sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit

| #define sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *list* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue put slist exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | list | Syslist object |

## [◆ ](#ga81e706aff605468683a96b14940745e7)sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter

| #define sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue cancel wait entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |

## [◆ ](#ga03ccb2bb3141c2842959ba77e4cd7337)sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit

| #define sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue cancel wait exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |

## [◆ ](#gaa3539eea74888c6257c5f5d456748155)sys\_port\_trace\_k\_fifo\_get\_enter

| #define sys\_port\_trace\_k\_fifo\_get\_enter | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue get entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gae6f06386f224063ee756e8ff0000dfe4)sys\_port\_trace\_k\_fifo\_get\_exit

| #define sys\_port\_trace\_k\_fifo\_get\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue get exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#gac0da5eca137a970c67b7b94a568c93e6)sys\_port\_trace\_k\_fifo\_init\_enter

| #define sys\_port\_trace\_k\_fifo\_init\_enter | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialization of FIFO Queue entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |

## [◆ ](#gaaf6c7c710377f449d52c5d6f5f7103c8)sys\_port\_trace\_k\_fifo\_init\_exit

| #define sys\_port\_trace\_k\_fifo\_init\_exit | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialization of FIFO Queue exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |

## [◆ ](#gab0fea5751e0296e623606e54efe5687b)sys\_port\_trace\_k\_fifo\_peek\_head\_enter

| #define sys\_port\_trace\_k\_fifo\_peek\_head\_enter | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue peek head entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |

## [◆ ](#ga06b74415be416b137092cb72187c1fb6)sys\_port\_trace\_k\_fifo\_peek\_head\_exit

| #define sys\_port\_trace\_k\_fifo\_peek\_head\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue peek head exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gad9f9b3193ed2c7270030036aef8d343d)sys\_port\_trace\_k\_fifo\_peek\_tail\_enter

| #define sys\_port\_trace\_k\_fifo\_peek\_tail\_enter | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue peek tail entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |

## [◆ ](#gae33baafbaac06ada7d6b53026a973d81)sys\_port\_trace\_k\_fifo\_peek\_tail\_exit

| #define sys\_port\_trace\_k\_fifo\_peek\_tail\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue peek tail exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaac5f6b9e77dad9de4652d24502ab46d0)sys\_port\_trace\_k\_fifo\_put\_enter

| #define sys\_port\_trace\_k\_fifo\_put\_enter | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue put entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | data | Data item |

## [◆ ](#ga7a1d15a538f23d2b7f290435803cd73e)sys\_port\_trace\_k\_fifo\_put\_exit

| #define sys\_port\_trace\_k\_fifo\_put\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue put exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | data | Data item |

## [◆ ](#gace20fdce59a99b92c8ac3711c4085b28)sys\_port\_trace\_k\_fifo\_put\_list\_enter

| #define sys\_port\_trace\_k\_fifo\_put\_list\_enter | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *head*, |
|  |  |  | *tail* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue put list entry.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | head | First ll-node |
    | tail | Last ll-node |

## [◆ ](#ga739360e2cefa158f22ce20a1e9369aea)sys\_port\_trace\_k\_fifo\_put\_list\_exit

| #define sys\_port\_trace\_k\_fifo\_put\_list\_exit | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *head*, |
|  |  |  | *tail* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace FIFO Queue put list exit.

Parameters
:   | fifo | FIFO object |
    | --- | --- |
    | head | First ll-node |
    | tail | Last ll-node |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
