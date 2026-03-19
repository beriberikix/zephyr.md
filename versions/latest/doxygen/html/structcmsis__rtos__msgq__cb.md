---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsis__rtos__msgq__cb.html
original_path: doxygen/html/structcmsis__rtos__msgq__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_msgq\_cb Struct Reference

Control block for a CMSIS-RTOSv2 message queue.
[More...](#details)

`#include <[cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [pool](#a1909f69f4b0f89a3aad0eec03fce9f7a) |
| char | [is\_dynamic\_allocation](#ab867f14725ef4c114b16d9ff4362b085) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_cb\_dynamic\_allocation](#aba512f3212825e79a291690e7577506e) |
| char | [name](#ad366606b20635db344f004bd60effd5f) [16] |

## Detailed Description

Control block for a CMSIS-RTOSv2 message queue.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to message queue control block. Control block is initiazed within osMessageQueueNew().

## Field Documentation

## [◆ ](#aba512f3212825e79a291690e7577506e)is\_cb\_dynamic\_allocation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cmsis\_rtos\_msgq\_cb::is\_cb\_dynamic\_allocation |
| --- |

## [◆ ](#ab867f14725ef4c114b16d9ff4362b085)is\_dynamic\_allocation

| char cmsis\_rtos\_msgq\_cb::is\_dynamic\_allocation |
| --- |

## [◆ ](#ad366606b20635db344f004bd60effd5f)name

| char cmsis\_rtos\_msgq\_cb::name[16] |
| --- |

## [◆ ](#a1909f69f4b0f89a3aad0eec03fce9f7a)pool

| void\* cmsis\_rtos\_msgq\_cb::pool |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_msgq\_cb](structcmsis__rtos__msgq__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
