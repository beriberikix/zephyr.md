---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/include_2zephyr_2arch_2riscv_2error_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2riscv_2error_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h File Reference

RISCV public error handling.
[More...](#details)

`#include <[zephyr/arch/riscv/syscall.h](arch_2riscv_2syscall_8h_source.md)>`  
`#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <zephyr/syscalls/error.h>`

[Go to the source code of this file.](include_2zephyr_2arch_2riscv_2error_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |

| Functions | |
| --- | --- |
| void | [user\_fault](#a1389d40b6fee2cbe28523075139aad72) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason) |

## Detailed Description

RISCV public error handling.

RISCV-specific kernel error handling interface. Included by [riscv/arch.h](riscv_2arch_8h.md "RISCV specific kernel interface header This header contains the RISCV specific kernel interface.").

## Macro Definition Documentation

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

if ([k\_is\_user\_context](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)()) { \

arch\_syscall\_invoke1(reason\_p, \

K\_SYSCALL\_USER\_FAULT); \

} else { \

compiler\_barrier(); \

arch\_syscall\_invoke1(reason\_p, \

[RV\_ECALL\_RUNTIME\_EXCEPT](arch_2riscv_2syscall_8h.md#aaaa314af66dac111544e3a307c40aa7c));\

} \

CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

} while (false)

[RV\_ECALL\_RUNTIME\_EXCEPT](arch_2riscv_2syscall_8h.md#aaaa314af66dac111544e3a307c40aa7c)

#define RV\_ECALL\_RUNTIME\_EXCEPT

**Definition** syscall.h:22

[k\_is\_user\_context](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)

static \_\_pinned\_func bool k\_is\_user\_context(void)

Indicate whether the CPU is currently in user mode.

**Definition** syscall.h:115

## Function Documentation

## [◆ ](#a1389d40b6fee2cbe28523075139aad72)user\_fault()

| void user\_fault | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [error.h](include_2zephyr_2arch_2riscv_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
