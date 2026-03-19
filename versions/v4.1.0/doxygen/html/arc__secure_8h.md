---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arc__secure_8h.html
original_path: doxygen/html/arc__secure_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_secure.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/aux_regs.h](aux__regs_8h_source.md)>`

[Go to the source code of this file.](arc__secure_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SJLI\_CALL\_ARC\_SECURE](#a6e757e1dc0c8149d3491df2ff038bdea)   0 |
| #define | [ARC\_S\_CALL\_AUX\_READ](#a7d64353fd2cbf804771090d4310a15b5)   0 |
| #define | [ARC\_S\_CALL\_AUX\_WRITE](#a1d4d7c124a5ec3508fb3a7729dd6178e)   1 |
| #define | [ARC\_S\_CALL\_IRQ\_ALLOC](#afa6fae9a7ed92cc75dd71e70471898b4)   2 |
| #define | [ARC\_S\_CALL\_CLRI](#a28c873e308b53950680842fde7016be3)   3 |
| #define | [ARC\_S\_CALL\_SETI](#af0f3d548c3a14b8cf81da4e7c7276e8d)   4 |
| #define | [ARC\_S\_CALL\_LIMIT](#a1c174d5e43e7da15eb77c7c2d6f9daf8)   5 |
| #define | [ARC\_N\_IRQ\_START\_LEVEL](#a3edfd794bb6ea1db197006312d448402)   ((CONFIG\_NUM\_IRQ\_PRIO\_LEVELS + 1) / 2) |
| #define | [arc\_sjli](#a0c39c8bb33dd287c51cca9614b1f08fd)(id) |

## Macro Definition Documentation

## [◆ ](#a3edfd794bb6ea1db197006312d448402)ARC\_N\_IRQ\_START\_LEVEL

| #define ARC\_N\_IRQ\_START\_LEVEL   ((CONFIG\_NUM\_IRQ\_PRIO\_LEVELS + 1) / 2) |
| --- |

## [◆ ](#a7d64353fd2cbf804771090d4310a15b5)ARC\_S\_CALL\_AUX\_READ

| #define ARC\_S\_CALL\_AUX\_READ   0 |
| --- |

## [◆ ](#a1d4d7c124a5ec3508fb3a7729dd6178e)ARC\_S\_CALL\_AUX\_WRITE

| #define ARC\_S\_CALL\_AUX\_WRITE   1 |
| --- |

## [◆ ](#a28c873e308b53950680842fde7016be3)ARC\_S\_CALL\_CLRI

| #define ARC\_S\_CALL\_CLRI   3 |
| --- |

## [◆ ](#afa6fae9a7ed92cc75dd71e70471898b4)ARC\_S\_CALL\_IRQ\_ALLOC

| #define ARC\_S\_CALL\_IRQ\_ALLOC   2 |
| --- |

## [◆ ](#a1c174d5e43e7da15eb77c7c2d6f9daf8)ARC\_S\_CALL\_LIMIT

| #define ARC\_S\_CALL\_LIMIT   5 |
| --- |

## [◆ ](#af0f3d548c3a14b8cf81da4e7c7276e8d)ARC\_S\_CALL\_SETI

| #define ARC\_S\_CALL\_SETI   4 |
| --- |

## [◆ ](#a0c39c8bb33dd287c51cca9614b1f08fd)arc\_sjli

| #define arc\_sjli | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(\_\_asm\_\_ volatile("sjli %[sjli\_id]\n" :: [sjli\_id] "i" (id)))

## [◆ ](#a6e757e1dc0c8149d3491df2ff038bdea)SJLI\_CALL\_ARC\_SECURE

| #define SJLI\_CALL\_ARC\_SECURE   0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [secureshield](dir_edc7d92000172b2927e4f8467a5c7046.md)
- [arc\_secure.h](arc__secure_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
