---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/it8xxx2-wuc_8h.html
original_path: doxygen/html/it8xxx2-wuc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it8xxx2-wuc.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](it8xxx2-wuc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IT8XXX2\_WUC\_UNUSED\_REG](#a61868a556512e102778c74ea81c0583f)   0 |
|  | WUC reserved register of reg property. |
| wakeup controller flags | |
| #define | [WUC\_TYPE\_EDGE\_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | WUC rising edge trigger mode. |
| #define | [WUC\_TYPE\_EDGE\_FALLING](#a21b4240f97f62e69f23ea614de699955)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | WUC falling edge trigger mode. |
| #define | [WUC\_TYPE\_EDGE\_BOTH](#a824c451f35efc9b287cd694a0c674095)   ([WUC\_TYPE\_EDGE\_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468) | [WUC\_TYPE\_EDGE\_FALLING](#a21b4240f97f62e69f23ea614de699955)) |
|  | WUC both edge trigger mode. |

## Macro Definition Documentation

## [◆ ](#a61868a556512e102778c74ea81c0583f)IT8XXX2\_WUC\_UNUSED\_REG

| #define IT8XXX2\_WUC\_UNUSED\_REG   0 |
| --- |

WUC reserved register of reg property.

## [◆ ](#a824c451f35efc9b287cd694a0c674095)WUC\_TYPE\_EDGE\_BOTH

| #define WUC\_TYPE\_EDGE\_BOTH   ([WUC\_TYPE\_EDGE\_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468) | [WUC\_TYPE\_EDGE\_FALLING](#a21b4240f97f62e69f23ea614de699955)) |
| --- |

WUC both edge trigger mode.

## [◆ ](#a21b4240f97f62e69f23ea614de699955)WUC\_TYPE\_EDGE\_FALLING

| #define WUC\_TYPE\_EDGE\_FALLING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

WUC falling edge trigger mode.

## [◆ ](#a679ab1940f920cfe6c0fa1d5ed14a468)WUC\_TYPE\_EDGE\_RISING

| #define WUC\_TYPE\_EDGE\_RISING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

WUC rising edge trigger mode.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [it8xxx2-wuc.h](it8xxx2-wuc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
