---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structcmsis__rtos__event__cb.html
original_path: doxygen/html/structcmsis__rtos__event__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_event\_cb Struct Reference

Control block for a CMSIS-RTOSv2 event flag.
[More...](#details)

`#include <[zephyr/portability/cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_poll\_signal](structk__poll__signal.md) | [poll\_signal](#ae9750a0ffc6a3f83916760d67a4edb63) |
| struct [k\_poll\_event](structk__poll__event.md) | [poll\_event](#a3b96b29e2866966d1ddd0ff71a1bbfac) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [signal\_results](#ab9218a355d3b3a943a1a9eea4656160a) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_cb\_dynamic\_allocation](#af1898a60748c3a1f3c2d2839eecaff64) |
| const char \* | [name](#adaa7a7ce302215e694c4866f5fbcd991) |

## Detailed Description

Control block for a CMSIS-RTOSv2 event flag.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to event flag control block. Control block is initiazed within osEventFlagsNew().

## Field Documentation

## [◆ ](#af1898a60748c3a1f3c2d2839eecaff64)is\_cb\_dynamic\_allocation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cmsis\_rtos\_event\_cb::is\_cb\_dynamic\_allocation |
| --- |

## [◆ ](#adaa7a7ce302215e694c4866f5fbcd991)name

| const char\* cmsis\_rtos\_event\_cb::name |
| --- |

## [◆ ](#a3b96b29e2866966d1ddd0ff71a1bbfac)poll\_event

| struct [k\_poll\_event](structk__poll__event.md) cmsis\_rtos\_event\_cb::poll\_event |
| --- |

## [◆ ](#ae9750a0ffc6a3f83916760d67a4edb63)poll\_signal

| struct [k\_poll\_signal](structk__poll__signal.md) cmsis\_rtos\_event\_cb::poll\_signal |
| --- |

## [◆ ](#ab9218a355d3b3a943a1a9eea4656160a)signal\_results

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cmsis\_rtos\_event\_cb::signal\_results |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_event\_cb](structcmsis__rtos__event__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
