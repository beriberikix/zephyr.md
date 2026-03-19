---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tpidruro_8h.html
original_path: doxygen/html/tpidruro_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tpidruro.h File Reference

tpidruro bits allocation
[More...](#details)

[Go to the source code of this file.](tpidruro_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TPIDRURO\_CURR\_CPU](#a2df1f988f05d98a639935e8cf014a6d1)   0xFFFFFFFCUL |

## Detailed Description

tpidruro bits allocation

Among other things, the tpidruro holds the address for the current CPU's struct \_cpu instance. But such a pointer is at least 4-bytes aligned. That leaves two of free bits for other purposes.

## Macro Definition Documentation

## [◆ ](#a2df1f988f05d98a639935e8cf014a6d1)TPIDRURO\_CURR\_CPU

| #define TPIDRURO\_CURR\_CPU   0xFFFFFFFCUL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [tpidruro.h](tpidruro_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
