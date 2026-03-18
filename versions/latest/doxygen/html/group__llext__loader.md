---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__llext__loader.html
original_path: doxygen/html/group__llext__loader.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Loader context for llext

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md)

Loader context for llext.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [llext\_loader](structllext__loader.md) |
|  | Linkable loadable extension loader context. [More...](structllext__loader.md#details) |

| Functions | |
| --- | --- |
| static int | [llext\_read](#gaf3d8bb89579039b77b10e6d15ff8a712) (struct [llext\_loader](structllext__loader.md) \*l, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| static int | [llext\_seek](#gabbf3d285c9787cebe7bb105bacce15fa) (struct [llext\_loader](structllext__loader.md) \*l, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
| static void \* | [llext\_peek](#ga241589ea6309b55ceb59f7e4b583600f) (struct [llext\_loader](structllext__loader.md) \*l, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |

## Detailed Description

Loader context for llext.

## Function Documentation

## [◆ ](#ga241589ea6309b55ceb59f7e4b583600f)llext\_peek()

| | void \* llext\_peek | ( | struct [llext\_loader](structllext__loader.md) \* | *l*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *pos* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[loader.h](loader_8h.md)>`

## [◆ ](#gaf3d8bb89579039b77b10e6d15ff8a712)llext\_read()

| | int llext\_read | ( | struct [llext\_loader](structllext__loader.md) \* | *l*, | | --- | --- | --- | --- | |  |  | void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[loader.h](loader_8h.md)>`

## [◆ ](#gabbf3d285c9787cebe7bb105bacce15fa)llext\_seek()

| | int llext\_seek | ( | struct [llext\_loader](structllext__loader.md) \* | *l*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *pos* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[loader.h](loader_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
