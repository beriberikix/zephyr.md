---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsis__rtos__semaphore__cb.html
original_path: doxygen/html/structcmsis__rtos__semaphore__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_semaphore\_cb Struct Reference

Control block for a CMSIS-RTOSv2 semaphore.
[More...](#details)

`#include <[cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_cb\_dynamic\_allocation](#a375bd0bcaa18d236449a3ceb2e21eeb2) |
| char | [name](#a0fcd03ebf15c9bccb348180c601daa6a) [16] |

## Detailed Description

Control block for a CMSIS-RTOSv2 semaphore.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to semaphore control block. Control block is initiazed within osSemaphoreNew().

## Field Documentation

## [◆ ](#a375bd0bcaa18d236449a3ceb2e21eeb2)is\_cb\_dynamic\_allocation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cmsis\_rtos\_semaphore\_cb::is\_cb\_dynamic\_allocation |
| --- |

## [◆ ](#a0fcd03ebf15c9bccb348180c601daa6a)name

| char cmsis\_rtos\_semaphore\_cb::name[16] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_semaphore\_cb](structcmsis__rtos__semaphore__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
