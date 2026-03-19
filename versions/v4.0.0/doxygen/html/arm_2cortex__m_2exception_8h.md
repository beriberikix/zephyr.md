---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm_2cortex__m_2exception_8h.html
original_path: doxygen/html/arm_2cortex__m_2exception_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| #define | [sys\_define\_gpr\_with\_alias](#a59d42697fc33d0b600597145a7b76dc7)(name1, name2) |

## Detailed Description

ARM AArch32 Cortex-M public exception handling.

## Macro Definition Documentation

## [◆ ](#a4c24fa1a72ad3c5d08ba7dc48b7d6bd9)IRQ\_PRIO\_LOWEST

| #define IRQ\_PRIO\_LOWEST   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([NUM\_IRQ\_PRIO\_BITS](nvic_8h.md#aea66dc68b7372ab771aab0b86d319b94)) - (\_IRQ\_PRIO\_OFFSET) - 1) |
| --- |

## [◆ ](#a59d42697fc33d0b600597145a7b76dc7)sys\_define\_gpr\_with\_alias

| #define sys\_define\_gpr\_with\_alias | ( |  | *name1*, |
| --- | --- | --- | --- |
|  |  |  | *name2* ) |

**Value:**

union { [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) name1, name2; }

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [exception.h](arm_2cortex__m_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
