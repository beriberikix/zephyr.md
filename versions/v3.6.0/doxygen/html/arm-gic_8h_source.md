---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm-gic_8h_source.html
original_path: doxygen/html/arm-gic_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-gic.h

[Go to the documentation of this file.](arm-gic_8h.md)

1/\*

2 \* Copyright (c) 2018 Lexmark International, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_DT\_BINDING\_ARM\_GIC\_H

7#define \_\_DT\_BINDING\_ARM\_GIC\_H

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\* CPU Interrupt numbers \*/

[ 12](arm-gic_8h.md#a8688f8eec1ec9ecbacafbec20e32807e)#define GIC\_INT\_VIRT\_MAINT 25

[ 13](arm-gic_8h.md#a88ef9b1e5027f1e6b1b13896d84ba7e9)#define GIC\_INT\_HYP\_TIMER 26

[ 14](arm-gic_8h.md#a3faa32072c74bcb2d79387085322f661)#define GIC\_INT\_VIRT\_TIMER 27

[ 15](arm-gic_8h.md#adfb3434e71e3da30646b94ecfd3d192f)#define GIC\_INT\_LEGACY\_FIQ 28

[ 16](arm-gic_8h.md#a9ae0a769a0e37b134971553a73865d55)#define GIC\_INT\_PHYS\_TIMER 29

[ 17](arm-gic_8h.md#af01b2804853035ed3f111ecf3d8778ad)#define GIC\_INT\_NS\_PHYS\_TIMER 30

[ 18](arm-gic_8h.md#abb56dd46d1d35f1137881b9dc0db2036)#define GIC\_INT\_LEGACY\_IRQ 31

19

20/\* BIT(0) reserved for IRQ\_ZERO\_LATENCY \*/

[ 21](arm-gic_8h.md#a296e915831223a614a6ea87dbe7735e7)#define IRQ\_TYPE\_LEVEL BIT(1)

[ 22](arm-gic_8h.md#aff68b0efbc719bc28f0d56c9ba8607bc)#define IRQ\_TYPE\_EDGE BIT(2)

23

[ 24](arm-gic_8h.md#ab5dc7ac388a5501a92f0c26d3995217f)#define GIC\_SPI 0x0

[ 25](arm-gic_8h.md#a25633bd9b6e14b0f6ded91b2fcfd614a)#define GIC\_PPI 0x1

26

[ 27](arm-gic_8h.md#a2dbeaa0c017cdff0982b381cc96f0a6c)#define IRQ\_DEFAULT\_PRIORITY 0xa0

28

29#endif

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [arm-gic.h](arm-gic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
