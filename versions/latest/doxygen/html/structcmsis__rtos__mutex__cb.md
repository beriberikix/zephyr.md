---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsis__rtos__mutex__cb.html
original_path: doxygen/html/structcmsis__rtos__mutex__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_mutex\_cb Struct Reference

Control block for a CMSIS-RTOSv2 mutex.
[More...](#details)

`#include <[cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_cb\_dynamic\_allocation](#aa7df7554bcdeb9e14ce38771392482dc) |
| char | [name](#a007a75f7c1f6913922f05c63218eadff) [16] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [state](#a43e50207a92b6f5c1f4add8a537352e5) |

## Detailed Description

Control block for a CMSIS-RTOSv2 mutex.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to mutex control block. Control block is initiazed within osMutexNew().

## Field Documentation

## [◆ ](#aa7df7554bcdeb9e14ce38771392482dc)is\_cb\_dynamic\_allocation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cmsis\_rtos\_mutex\_cb::is\_cb\_dynamic\_allocation |
| --- |

## [◆ ](#a007a75f7c1f6913922f05c63218eadff)name

| char cmsis\_rtos\_mutex\_cb::name[16] |
| --- |

## [◆ ](#a43e50207a92b6f5c1f4add8a537352e5)state

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cmsis\_rtos\_mutex\_cb::state |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_mutex\_cb](structcmsis__rtos__mutex__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
