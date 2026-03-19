---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm-gic_8h.html
original_path: doxygen/html/arm-gic_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-gic.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](arm-gic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GIC\_INT\_VIRT\_MAINT](#a8688f8eec1ec9ecbacafbec20e32807e)   25 |
| #define | [GIC\_INT\_HYP\_TIMER](#a88ef9b1e5027f1e6b1b13896d84ba7e9)   26 |
| #define | [GIC\_INT\_VIRT\_TIMER](#a3faa32072c74bcb2d79387085322f661)   27 |
| #define | [GIC\_INT\_LEGACY\_FIQ](#adfb3434e71e3da30646b94ecfd3d192f)   28 |
| #define | [GIC\_INT\_PHYS\_TIMER](#a9ae0a769a0e37b134971553a73865d55)   29 |
| #define | [GIC\_INT\_NS\_PHYS\_TIMER](#af01b2804853035ed3f111ecf3d8778ad)   30 |
| #define | [GIC\_INT\_LEGACY\_IRQ](#abb56dd46d1d35f1137881b9dc0db2036)   31 |
| #define | [IRQ\_TYPE\_LEVEL](#a296e915831223a614a6ea87dbe7735e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [IRQ\_TYPE\_EDGE](#aff68b0efbc719bc28f0d56c9ba8607bc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [GIC\_SPI](#ab5dc7ac388a5501a92f0c26d3995217f)   0x0 |
| #define | [GIC\_PPI](#a25633bd9b6e14b0f6ded91b2fcfd614a)   0x1 |
| #define | [IRQ\_DEFAULT\_PRIORITY](#a2dbeaa0c017cdff0982b381cc96f0a6c)   0xa0 |

## Macro Definition Documentation

## [◆ ](#a88ef9b1e5027f1e6b1b13896d84ba7e9)GIC\_INT\_HYP\_TIMER

| #define GIC\_INT\_HYP\_TIMER   26 |
| --- |

## [◆ ](#adfb3434e71e3da30646b94ecfd3d192f)GIC\_INT\_LEGACY\_FIQ

| #define GIC\_INT\_LEGACY\_FIQ   28 |
| --- |

## [◆ ](#abb56dd46d1d35f1137881b9dc0db2036)GIC\_INT\_LEGACY\_IRQ

| #define GIC\_INT\_LEGACY\_IRQ   31 |
| --- |

## [◆ ](#af01b2804853035ed3f111ecf3d8778ad)GIC\_INT\_NS\_PHYS\_TIMER

| #define GIC\_INT\_NS\_PHYS\_TIMER   30 |
| --- |

## [◆ ](#a9ae0a769a0e37b134971553a73865d55)GIC\_INT\_PHYS\_TIMER

| #define GIC\_INT\_PHYS\_TIMER   29 |
| --- |

## [◆ ](#a8688f8eec1ec9ecbacafbec20e32807e)GIC\_INT\_VIRT\_MAINT

| #define GIC\_INT\_VIRT\_MAINT   25 |
| --- |

## [◆ ](#a3faa32072c74bcb2d79387085322f661)GIC\_INT\_VIRT\_TIMER

| #define GIC\_INT\_VIRT\_TIMER   27 |
| --- |

## [◆ ](#a25633bd9b6e14b0f6ded91b2fcfd614a)GIC\_PPI

| #define GIC\_PPI   0x1 |
| --- |

## [◆ ](#ab5dc7ac388a5501a92f0c26d3995217f)GIC\_SPI

| #define GIC\_SPI   0x0 |
| --- |

## [◆ ](#a2dbeaa0c017cdff0982b381cc96f0a6c)IRQ\_DEFAULT\_PRIORITY

| #define IRQ\_DEFAULT\_PRIORITY   0xa0 |
| --- |

## [◆ ](#aff68b0efbc719bc28f0d56c9ba8607bc)IRQ\_TYPE\_EDGE

| #define IRQ\_TYPE\_EDGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a296e915831223a614a6ea87dbe7735e7)IRQ\_TYPE\_LEVEL

| #define IRQ\_TYPE\_LEVEL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [arm-gic.h](arm-gic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
