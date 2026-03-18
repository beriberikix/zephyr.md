---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sw__isr__table_8h.html
original_path: doxygen/html/sw__isr__table_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sw\_isr\_table.h File Reference

Software-managed ISR table.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](sw__isr__table_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ISR\_FLAG\_DIRECT](#a1376eec61303fcd20e7656175ddbaf19)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | This interrupt gets put directly in the vector table. |
| #define | [IRQ\_TABLE\_SIZE](#af36594d0586be77420bfe6eaf9f96a2c)   ([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) - [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)) |

## Detailed Description

Software-managed ISR table.

Data types for a software-managed ISR table, with a parameter per-ISR.

## Macro Definition Documentation

## [◆ ](#af36594d0586be77420bfe6eaf9f96a2c)IRQ\_TABLE\_SIZE

| #define IRQ\_TABLE\_SIZE   ([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) - [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)) |
| --- |

## [◆ ](#a1376eec61303fcd20e7656175ddbaf19)ISR\_FLAG\_DIRECT

| #define ISR\_FLAG\_DIRECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

This interrupt gets put directly in the vector table.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sw\_isr\_table.h](sw__isr__table_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
