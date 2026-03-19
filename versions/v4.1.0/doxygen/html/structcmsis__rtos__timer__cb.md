---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsis__rtos__timer__cb.html
original_path: doxygen/html/structcmsis__rtos__timer__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_timer\_cb Struct Reference

Control block for a CMSIS-RTOSv2 timer.
[More...](#details)

`#include <[cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| osTimerType\_t | [type](#a9054df0b4e92854d20c0d202eaeea66c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [status](#a16a1cf8a0bc2eba418b64e1a35782526) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_cb\_dynamic\_allocation](#a2148d26c2386672ea72391839826e502) |
| char | [name](#aeea9a9cb04879526375d5eb51733dfe5) [16] |
| void(\* | [callback\_function](#a8819befff072e0a3cda4bf855e24dbf1) )(void \*argument) |
| void \* | [arg](#a854205b98234c4aeee8056d6bb64c4a3) |

## Detailed Description

Control block for a CMSIS-RTOSv2 timer.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to timer control block. Control block is initiazed within osTimerNew().

## Field Documentation

## [◆ ](#a854205b98234c4aeee8056d6bb64c4a3)arg

| void\* cmsis\_rtos\_timer\_cb::arg |
| --- |

## [◆ ](#a8819befff072e0a3cda4bf855e24dbf1)callback\_function

| void(\* cmsis\_rtos\_timer\_cb::callback\_function) (void \*argument) |
| --- |

## [◆ ](#a2148d26c2386672ea72391839826e502)is\_cb\_dynamic\_allocation

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cmsis\_rtos\_timer\_cb::is\_cb\_dynamic\_allocation |
| --- |

## [◆ ](#aeea9a9cb04879526375d5eb51733dfe5)name

| char cmsis\_rtos\_timer\_cb::name[16] |
| --- |

## [◆ ](#a16a1cf8a0bc2eba418b64e1a35782526)status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cmsis\_rtos\_timer\_cb::status |
| --- |

## [◆ ](#a9054df0b4e92854d20c0d202eaeea66c)type

| osTimerType\_t cmsis\_rtos\_timer\_cb::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_timer\_cb](structcmsis__rtos__timer__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
