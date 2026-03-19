---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/include_2zephyr_2arch_2arm64_2error_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2arm64_2error_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h File Reference

ARM AArch64 public error handling.
[More...](#details)

`#include <[zephyr/arch/arm64/syscall.h](arch_2arm64_2syscall_8h_source.md)>`  
`#include <[zephyr/arch/arm64/exception.h](arm64_2exception_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2arch_2arm64_2error_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |

## Detailed Description

ARM AArch64 public error handling.

ARM AArch64-specific kernel error handling interface. Included by arch.h.

## Macro Definition Documentation

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x8 \_\_asm\_\_("x8") = reason\_p; \

\

\_\_asm\_\_ volatile("svc %[id]\n" \

: \

: [id] "i" (\_SVC\_CALL\_RUNTIME\_EXCEPT), \

"r" (x8) \

: "memory"); \

} while (false)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [error.h](include_2zephyr_2arch_2arm64_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
