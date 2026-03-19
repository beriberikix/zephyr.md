---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xtensa_2arch__inlines_8h.html
original_path: doxygen/html/xtensa_2arch__inlines_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h File Reference

`#include <[zephyr/kernel_structs.h](kernel__structs_8h_source.md)>`  
`#include <zephyr/zsr.h>`

[Go to the source code of this file.](xtensa_2arch__inlines_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XTENSA\_RSR](#ad745bdf9b93a9019a1d373e9f50a35e5)(sr) |
|  | Read a special register. |
| #define | [XTENSA\_WSR](#a319bd616dfbeb56398294bcb9f7a0fdd)(sr, v) |
|  | Write to a special register. |
| #define | [XTENSA\_RUR](#aa297de6c2736557e7076e496ce25ec23)(ur) |
|  | Read a user register. |
| #define | [XTENSA\_WUR](#a22be7315733dd413f1c3253faa2e78da)(ur, v) |
|  | Write to a user register. |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \* | [arch\_curr\_cpu](#a3e8a7515c0c3b8de5a037ce5997c73b0) (void) |
|  | Implementation of [arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0 "arch_curr_cpu"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_proc\_id](#a4bf4475c062f66961e183d17fd4c22d3) (void) |
|  | Implementation of [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3 "arch_proc_id"). |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_num\_cpus](#a83c8ae933b0ec7d067569f17125c6a2c) (void) |
|  | Implementation of [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c "arch_num_cpus"). |

## Macro Definition Documentation

## [◆ ](#ad745bdf9b93a9019a1d373e9f50a35e5)XTENSA\_RSR

| #define XTENSA\_RSR | ( |  | *sr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v; \

\_\_asm\_\_ volatile ("rsr." sr " %0" : "=a"(v)); \

v; })

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Read a special register.

Parameters
:   | sr | Name of special register. |
    | --- | --- |

Returns
:   Value of special register.

## [◆ ](#aa297de6c2736557e7076e496ce25ec23)XTENSA\_RUR

| #define XTENSA\_RUR | ( |  | *ur* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) v; \

\_\_asm\_\_ volatile ("rur." ur " %0" : "=a"(v)); \

v; })

Read a user register.

Parameters
:   | ur | Name of user register. |
    | --- | --- |

Returns
:   Value of user register.

## [◆ ](#a319bd616dfbeb56398294bcb9f7a0fdd)XTENSA\_WSR

| #define XTENSA\_WSR | ( |  | *sr*, |
| --- | --- | --- | --- |
|  |  |  | *v* ) |

**Value:**

do { \

\_\_asm\_\_ volatile ("wsr." sr " %0" : : "r"(v)); \

} while (false)

Write to a special register.

Parameters
:   | sr | Name of special register. |
    | --- | --- |
    | v | Value to be written to special register. |

## [◆ ](#a22be7315733dd413f1c3253faa2e78da)XTENSA\_WUR

| #define XTENSA\_WUR | ( |  | *ur*, |
| --- | --- | --- | --- |
|  |  |  | *v* ) |

**Value:**

do { \

\_\_asm\_\_ volatile ("wur." ur " %0" : : "r"(v)); \

} while (false)

Write to a user register.

Parameters
:   | ur | Name of user register. |
    | --- | --- |
    | v | Value to be written to user register. |

## Function Documentation

## [◆ ](#a3e8a7515c0c3b8de5a037ce5997c73b0)arch\_curr\_cpu()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \* arch\_curr\_cpu | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0 "arch_curr_cpu").

## [◆ ](#a83c8ae933b0ec7d067569f17125c6a2c)arch\_num\_cpus()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_num\_cpus | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c "arch_num_cpus").

## [◆ ](#a4bf4475c062f66961e183d17fd4c22d3)arch\_proc\_id()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_proc\_id | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3 "arch_proc_id").

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [arch\_inlines.h](xtensa_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
