---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2arch_2rx_2error_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2rx_2error_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h File Reference

Renesas RX arch public error handling.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2arch_2rx_2error_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |

## Detailed Description

Renesas RX arch public error handling.

Renesas RX-specific kernel error handling interface. Included by [rx/arch.h](rx_2arch_8h.md "Renesas RX specific kernel interface header.").

## Macro Definition Documentation

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

arch\_irq\_unlock(0); \

\_\_asm\_\_ volatile("mov %[\_reason], r1\n\t" \

"int #2\n\t" ::[\_reason] "r"(reason\_p) \

: "r1", "memory"); \

} while (false)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [rx](dir_eb52b7f9d95392aedf108916f743bdaf.md)
- [error.h](include_2zephyr_2arch_2rx_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
