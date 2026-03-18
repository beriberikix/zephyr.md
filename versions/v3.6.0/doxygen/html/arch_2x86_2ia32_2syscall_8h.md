---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2x86_2ia32_2syscall_8h.html
original_path: doxygen/html/arch_2x86_2ia32_2syscall_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h File Reference

x86 (IA32) specific syscall header
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`

[Go to the source code of this file.](arch_2x86_2ia32_2syscall_8h_source.md)

| Macros | |
| --- | --- |
| #define | [USER\_CODE\_SEG](#a719fbb690b1312f487003392d29970b0)   0x2b /\* at dpl=3 \*/ |
| #define | [USER\_DATA\_SEG](#a4a394d2afb6791022239b7526f24782c)   0x33 /\* at dpl=3 \*/ |

| Functions | |
| --- | --- |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke6](#ac9d314e4cd03416c9327a90cf71ce7b8) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke5](#a892f88703053430c55312fe146b6967b) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke4](#ae592b58d4430222fe9cd598b6ccbeb0a) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke3](#a7804d200754b8dc00b211a6419241a6d) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke2](#adea10ca87424364cafb2e784873473f1) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke1](#a41d16c05d5ea97ba21f84120d9254d8c) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke0](#a3e917733f2f35e18d5b2813558fa375e) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static \_\_pinned\_func [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_is\_user\_context](#a4c6ec696182878eab8c1093b1d25157c) (void) |

## Detailed Description

x86 (IA32) specific syscall header

This header contains the x86 specific syscall interface. It is included by the syscall interface architecture-abstraction header (include/arch/syscall.h)

## Macro Definition Documentation

## [◆ ](#a719fbb690b1312f487003392d29970b0)USER\_CODE\_SEG

| #define USER\_CODE\_SEG   0x2b /\* at dpl=3 \*/ |
| --- |

## [◆ ](#a4a394d2afb6791022239b7526f24782c)USER\_DATA\_SEG

| #define USER\_DATA\_SEG   0x33 /\* at dpl=3 \*/ |
| --- |

## Function Documentation

## [◆ ](#a4c6ec696182878eab8c1093b1d25157c)arch\_is\_user\_context()

| | \_\_pinned\_func [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_is\_user\_context | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3e917733f2f35e18d5b2813558fa375e)arch\_syscall\_invoke0()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke0 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a41d16c05d5ea97ba21f84120d9254d8c)arch\_syscall\_invoke1()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke1 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adea10ca87424364cafb2e784873473f1)arch\_syscall\_invoke2()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke2 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7804d200754b8dc00b211a6419241a6d)arch\_syscall\_invoke3()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke3 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae592b58d4430222fe9cd598b6ccbeb0a)arch\_syscall\_invoke4()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke4 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a892f88703053430c55312fe146b6967b)arch\_syscall\_invoke5()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke5 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg5*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac9d314e4cd03416c9327a90cf71ce7b8)arch\_syscall\_invoke6()

| | \_\_pinned\_func [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke6 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg5*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg6*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [syscall.h](arch_2x86_2ia32_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
