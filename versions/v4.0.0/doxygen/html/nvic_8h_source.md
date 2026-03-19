---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nvic_8h_source.html
original_path: doxygen/html/nvic_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nvic.h

[Go to the documentation of this file.](nvic_8h.md)

1/\*

2 \* Copyright (c) 2020, Linaro Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_NVIC\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_NVIC\_H\_

9

10#include <[zephyr/devicetree.h](devicetree_8h.md)>

11

12#if defined(CONFIG\_ARMV8\_1\_M\_MAINLINE)

13/\* The order here is on purpose since ARMv8.1-M SoCs may define

14 \* CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE, CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE or

15 \* CONFIG\_ARMV8\_M\_MAINLINE so we want to check for ARMv8.1-M first.

16 \*/

17#define NVIC\_NODEID DT\_INST(0, arm\_v8\_1m\_nvic)

18#elif defined(CONFIG\_ARMV8\_M\_BASELINE) || defined(CONFIG\_ARMV8\_M\_MAINLINE)

19#define NVIC\_NODEID DT\_INST(0, arm\_v8m\_nvic)

20#elif defined(CONFIG\_ARMV7\_M\_ARMV8\_M\_MAINLINE)

21#define NVIC\_NODEID DT\_INST(0, arm\_v7m\_nvic)

22#elif defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

23#define NVIC\_NODEID DT\_INST(0, arm\_v6m\_nvic)

24#endif

25

[ 26](nvic_8h.md#aea66dc68b7372ab771aab0b86d319b94)#define NUM\_IRQ\_PRIO\_BITS DT\_PROP(NVIC\_NODEID, arm\_num\_irq\_priority\_bits)

27

28#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_NVIC\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [nvic.h](nvic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
