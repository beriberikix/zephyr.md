---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsis__rtos__mempool__cb.html
original_path: doxygen/html/structcmsis__rtos__mempool__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_mempool\_cb Struct Reference

Control block for a CMSIS-RTOSv2 memory pool.
[More...](#details)

`#include <[cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [pool](#a1a05ccc77a02197729db3e80f235e833) |
| char | [is\_dynamic\_allocation](#ad8d9c65555e6cba4d3d016ef0decf99f) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_cb\_dynamic\_allocation](#aad9668c546fcbbb232faf0790554cc60) |
| char | [name](#ac2ea885600f6fb48b2e0e17c068cce65) [16] |

## Detailed Description

Control block for a CMSIS-RTOSv2 memory pool.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to memory pool control block. Control block is initiazed within osMemoryPoolNew().

## Field Documentation

## [◆ ](#aad9668c546fcbbb232faf0790554cc60)is\_cb\_dynamic\_allocation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cmsis\_rtos\_mempool\_cb::is\_cb\_dynamic\_allocation |
| --- |

## [◆ ](#ad8d9c65555e6cba4d3d016ef0decf99f)is\_dynamic\_allocation

| char cmsis\_rtos\_mempool\_cb::is\_dynamic\_allocation |
| --- |

## [◆ ](#ac2ea885600f6fb48b2e0e17c068cce65)name

| char cmsis\_rtos\_mempool\_cb::name[16] |
| --- |

## [◆ ](#a1a05ccc77a02197729db3e80f235e833)pool

| void\* cmsis\_rtos\_mempool\_cb::pool |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_mempool\_cb](structcmsis__rtos__mempool__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
