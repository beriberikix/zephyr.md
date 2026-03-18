---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm_2cortex__m_2exception_8h.html
original_path: doxygen/html/arm_2cortex__m_2exception_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h File Reference

ARM AArch32 Cortex-M public exception handling.
[More...](#details)

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/arch/arm/cortex_m/nvic.h](nvic_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](arm_2cortex__m_2exception_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arch\_esf](structarch__esf.md) |
|  | Exception Stack Frame. [More...](structarch__esf.md#details) |
| struct | [arch\_esf::\_\_basic\_sf](structarch__esf_1_1____basic__sf.md) |

| Macros | |
| --- | --- |
| #define | [IRQ\_PRIO\_LOWEST](#a4c24fa1a72ad3c5d08ba7dc48b7d6bd9)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([NUM\_IRQ\_PRIO\_BITS](nvic_8h.md#aea66dc68b7372ab771aab0b86d319b94)) - (\_IRQ\_PRIO\_OFFSET) - 1) |

## Detailed Description

ARM AArch32 Cortex-M public exception handling.

## Macro Definition Documentation

## [◆ ](#a4c24fa1a72ad3c5d08ba7dc48b7d6bd9)IRQ\_PRIO\_LOWEST

| #define IRQ\_PRIO\_LOWEST   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([NUM\_IRQ\_PRIO\_BITS](nvic_8h.md#aea66dc68b7372ab771aab0b86d319b94)) - (\_IRQ\_PRIO\_OFFSET) - 1) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [exception.h](arm_2cortex__m_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
