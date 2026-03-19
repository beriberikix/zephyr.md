---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/include_2zephyr_2arch_2arc_2v2_2error_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2arc_2v2_2error_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h File Reference

ARCv2 public error handling.
[More...](#details)

`#include <[zephyr/arch/arc/syscall.h](arch_2arc_2syscall_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/exception.h](arc_2v2_2exception_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2arch_2arc_2v2_2error_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |

## Detailed Description

ARCv2 public error handling.

ARC-specific kernel error handling interface. Included by arc/arch.h.

## Macro Definition Documentation

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

\_\_asm\_\_ volatile ( \

"mov %%r0, %[reason]\n\t" \

"trap\_s %[id]\n\t" \

: \

: [reason] "i" (reason\_p), \

[id] "i" (\_TRAP\_S\_CALL\_RUNTIME\_EXCEPT) \

: "memory"); \

CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

} while (false)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [error.h](include_2zephyr_2arch_2arc_2v2_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
