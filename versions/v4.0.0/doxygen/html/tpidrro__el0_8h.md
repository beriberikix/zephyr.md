---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tpidrro__el0_8h.html
original_path: doxygen/html/tpidrro__el0_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tpidrro\_el0.h File Reference

tpidrro\_el0 bits allocation
[More...](#details)

[Go to the source code of this file.](tpidrro__el0_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TPIDRROEL0\_IN\_EL0](#a7350edf399cb3e4a9cf63010bf3954b7)   0x0000000000000001 |
| #define | [TPIDRROEL0\_CURR\_CPU](#a4f694ec0eb4b87138023e08242aafe7e)   0x0000fffffffffff8 |
| #define | [TPIDRROEL0\_EXC\_DEPTH](#acde61f1bf3b88e63b6e587528ad001d8)   0xff00000000000000 |
| #define | [TPIDRROEL0\_EXC\_UNIT](#a1fe4c8cd6065cb0f174be6ded38fc7a2)   0x0100000000000000 |
| #define | [TPIDRROEL0\_EXC\_SHIFT](#a6297d2dc8c22898de15e52ba6e00adc0)   56 |

## Detailed Description

tpidrro\_el0 bits allocation

Among other things, the tpidrro\_el0 holds the address for the current CPU's struct \_cpu instance. But such a pointer is at least 8-bytes aligned, and the address space is 48 bits max. That leaves plenty of free bits for other purposes.

## Macro Definition Documentation

## [◆ ](#a4f694ec0eb4b87138023e08242aafe7e)TPIDRROEL0\_CURR\_CPU

| #define TPIDRROEL0\_CURR\_CPU   0x0000fffffffffff8 |
| --- |

## [◆ ](#acde61f1bf3b88e63b6e587528ad001d8)TPIDRROEL0\_EXC\_DEPTH

| #define TPIDRROEL0\_EXC\_DEPTH   0xff00000000000000 |
| --- |

## [◆ ](#a6297d2dc8c22898de15e52ba6e00adc0)TPIDRROEL0\_EXC\_SHIFT

| #define TPIDRROEL0\_EXC\_SHIFT   56 |
| --- |

## [◆ ](#a1fe4c8cd6065cb0f174be6ded38fc7a2)TPIDRROEL0\_EXC\_UNIT

| #define TPIDRROEL0\_EXC\_UNIT   0x0100000000000000 |
| --- |

## [◆ ](#a7350edf399cb3e4a9cf63010bf3954b7)TPIDRROEL0\_IN\_EL0

| #define TPIDRROEL0\_IN\_EL0   0x0000000000000001 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [tpidrro\_el0.h](tpidrro__el0_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
