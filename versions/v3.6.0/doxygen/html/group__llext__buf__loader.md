---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__llext__buf__loader.html
original_path: doxygen/html/group__llext__buf__loader.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Linkable loadable extensions buffer loader

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext.md)

LLEXT buffer loader.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [llext\_buf\_loader](structllext__buf__loader.md) |
|  | An extension loader from a provided buffer containing an ELF. [More...](structllext__buf__loader.md#details) |

| Macros | |
| --- | --- |
| #define | [LLEXT\_BUF\_LOADER](#ga9ca06c7c3e57f5284ce44c62f5cc2c02)(\_buf, \_buf\_len) |
|  | Initialize an extension buf loader. |

## Detailed Description

LLEXT buffer loader.

## Macro Definition Documentation

## [◆ ](#ga9ca06c7c3e57f5284ce44c62f5cc2c02)LLEXT\_BUF\_LOADER

| #define LLEXT\_BUF\_LOADER | ( |  | *\_buf*, |
| --- | --- | --- | --- |
|  |  |  | *\_buf\_len* ) |

`#include <[buf_loader.h](buf__loader_8h.md)>`

**Value:**

{ \

.loader = { \

.read = llext\_buf\_read, \

.seek = llext\_buf\_seek, \

.peek = llext\_buf\_peek, \

}, \

.buf = (\_buf), \

.len = (\_buf\_len), \

.pos = 0 \

}

Initialize an extension buf loader.

Parameters
:   | \_buf | Buffer containing an ELF binary |
    | --- | --- |
    | \_buf\_len | Buffer length in bytes |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
