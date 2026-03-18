---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__llext__loader__apis.html
original_path: doxygen/html/group__llext__loader__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ELF loader context

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md)

| Data Structures | |
| --- | --- |
| struct | [llext\_buf\_loader](structllext__buf__loader.md) |
|  | Implementation of [llext\_loader](structllext__loader.md "llext_loader") that reads from a memory buffer. [More...](structllext__buf__loader.md#details) |
| struct | [llext\_loader](structllext__loader.md) |
|  | Linkable loadable extension loader context. [More...](structllext__loader.md#details) |

| Macros | |
| --- | --- |
| #define | [LLEXT\_BUF\_LOADER](#ga9ca06c7c3e57f5284ce44c62f5cc2c02)(\_buf, \_buf\_len) |
|  | Initializer for an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure. |

## Detailed Description

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

Initializer for an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure.

Parameters
:   | \_buf | Buffer containing the ELF binary |
    | --- | --- |
    | \_buf\_len | Buffer length in bytes |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
