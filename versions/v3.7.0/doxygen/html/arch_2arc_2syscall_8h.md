---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2arc_2syscall_8h.html
original_path: doxygen/html/arch_2arc_2syscall_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h File Reference

ARC specific syscall header.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](arch_2arc_2syscall_8h_source.md)

| Functions | |
| --- | --- |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke6](#ac6cae2197637993a86b6ec6803b5742b) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke5](#a9971c78bc8f579a0dadf84225dc0c3ff) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke4](#a0ba3ae2290827385b226ebdbf3de3b53) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke3](#aacb1c66a1b7bf2293fea269f6b5e1c7e) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke2](#a1e78f1022aaf10e88727b142b56d4ef0) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke1](#a4cfb3b2b38e5afca889e8b9765d6c3df) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke0](#a5e9ab24b9c980e327903fbe3f5bd97f3) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_is\_user\_context](#a89ab53a218add419e37f89c1f5fd955f) (void) |

## Detailed Description

ARC specific syscall header.

This header contains the ARC specific syscall interface. It is included by the syscall interface architecture-abstraction header (include/arch/syscall.h)

## Function Documentation

## [◆ ](#a89ab53a218add419e37f89c1f5fd955f)arch\_is\_user\_context()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_is\_user\_context | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5e9ab24b9c980e327903fbe3f5bd97f3)arch\_syscall\_invoke0()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke0 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4cfb3b2b38e5afca889e8b9765d6c3df)arch\_syscall\_invoke1()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke1 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1e78f1022aaf10e88727b142b56d4ef0)arch\_syscall\_invoke2()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke2 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aacb1c66a1b7bf2293fea269f6b5e1c7e)arch\_syscall\_invoke3()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke3 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0ba3ae2290827385b226ebdbf3de3b53)arch\_syscall\_invoke4()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke4 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9971c78bc8f579a0dadf84225dc0c3ff)arch\_syscall\_invoke5()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke5 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg5*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac6cae2197637993a86b6ec6803b5742b)arch\_syscall\_invoke6()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke6 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg5*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg6*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [syscall.h](arch_2arc_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
