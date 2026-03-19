---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm__arch__timer_8h_source.html
original_path: doxygen/html/arm__arch__timer_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_arch\_timer.h

[Go to the documentation of this file.](arm__arch__timer_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_ARM\_ARCH\_TIMER\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_ARM\_ARCH\_TIMER\_H\_

10

11#include <[zephyr/dt-bindings/interrupt-controller/arm-gic.h](arm-gic_8h.md)>

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13

[ 14](arm__arch__timer_8h.md#aea7a05797c3c8202e22fbde7784e6f42)#define ARM\_TIMER\_NODE DT\_INST(0, arm\_armv8\_timer)

15

[ 16](arm__arch__timer_8h.md#ab20a2e64d841b305054bb1e5463de625)#define ARM\_TIMER\_SECURE\_IRQ DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 0, irq)

[ 17](arm__arch__timer_8h.md#a62df9aa2725c6cc49641bad7eddedfb2)#define ARM\_TIMER\_NON\_SECURE\_IRQ DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 1, irq)

[ 18](arm__arch__timer_8h.md#a22468e93135e790458d9c2bfd493c070)#define ARM\_TIMER\_VIRTUAL\_IRQ DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 2, irq)

[ 19](arm__arch__timer_8h.md#abb6827272e664d5f0ebc05efaacf4a8c)#define ARM\_TIMER\_HYP\_IRQ DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 3, irq)

20

[ 21](arm__arch__timer_8h.md#a10a91fd36630255fb88f08558b96be7a)#define ARM\_TIMER\_SECURE\_PRIO DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 0,\

22 priority)

[ 23](arm__arch__timer_8h.md#a48f3d216ea1166a40f7c5ab333e269b8)#define ARM\_TIMER\_NON\_SECURE\_PRIO DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 1,\

24 priority)

[ 25](arm__arch__timer_8h.md#acafac307be9d89ff4ebb72ab23c75ac6)#define ARM\_TIMER\_VIRTUAL\_PRIO DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 2,\

26 priority)

[ 27](arm__arch__timer_8h.md#a5b8a919fcfd8e4346aca7eefa382a1f0)#define ARM\_TIMER\_HYP\_PRIO DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 3,\

28 priority)

29

[ 30](arm__arch__timer_8h.md#ab43f20d1d6d366b921817c2c463c5025)#define ARM\_TIMER\_SECURE\_FLAGS DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 0, flags)

[ 31](arm__arch__timer_8h.md#a7852b4d22a08d2bef99c14495daff57a)#define ARM\_TIMER\_NON\_SECURE\_FLAGS DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 1, flags)

[ 32](arm__arch__timer_8h.md#a373af60653667562ca2ca950c45e4b20)#define ARM\_TIMER\_VIRTUAL\_FLAGS DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 2, flags)

[ 33](arm__arch__timer_8h.md#a9c6a0c6b52a600627958024cf80929de)#define ARM\_TIMER\_HYP\_FLAGS DT\_IRQ\_BY\_IDX(ARM\_TIMER\_NODE, 3, flags)

34

35#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_TIMER\_ARM\_ARCH\_TIMER\_H\_ \*/

[arm-gic.h](arm-gic_8h.md)

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [arm\_arch\_timer.h](arm__arch__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
