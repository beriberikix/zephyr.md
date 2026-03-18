---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kinetis__sim_8h_source.html
original_path: doxygen/html/kinetis__sim_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kinetis\_sim.h

[Go to the documentation of this file.](kinetis__sim_8h.md)

1/\*

2 \* Copyright (c) 2017, NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_SIM\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_SIM\_H\_

9

[ 10](kinetis__sim_8h.md#a0684d47ba26fd4908fa10bb2c40894b9)#define KINETIS\_SIM\_CORESYS\_CLK 0

[ 11](kinetis__sim_8h.md#ac083afde9dfc09d77be337ccec8613c6)#define KINETIS\_SIM\_PLATFORM\_CLK 1

[ 12](kinetis__sim_8h.md#a2fde3204425c877c1e0e409cac4d3f2c)#define KINETIS\_SIM\_BUS\_CLK 2

[ 13](kinetis__sim_8h.md#a3b8468dcc04b28ec8c8e08c80848d9a1)#define KINETIS\_SIM\_FAST\_PERIPHERAL\_CLK 5

[ 14](kinetis__sim_8h.md#aa1c209ae87c6971eb0f737baa768516b)#define KINETIS\_SIM\_LPO\_CLK 19

[ 15](kinetis__sim_8h.md#a504e4baefda2add7e54aac44cadb428d)#define KINETIS\_SIM\_DMAMUX\_CLK KINETIS\_SIM\_BUS\_CLK

[ 16](kinetis__sim_8h.md#a236c80919664e4d41414beab57ec1fea)#define KINETIS\_SIM\_DMA\_CLK KINETIS\_SIM\_CORESYS\_CLK

[ 17](kinetis__sim_8h.md#aef35b68542fef8df938f4a7238299ae7)#define KINETIS\_SIM\_SIM\_SOPT7 7

18

[ 19](kinetis__sim_8h.md#a02aa044f83da5dca652327df3dbce5d8)#define KINETIS\_SIM\_PLLFLLSEL\_MCGFLLCLK 0

[ 20](kinetis__sim_8h.md#a3b28905b525cde569f367e17274accf8)#define KINETIS\_SIM\_PLLFLLSEL\_MCGPLLCLK 1

[ 21](kinetis__sim_8h.md#a04fcbc9ade8eb94807dbf78922ee3177)#define KINETIS\_SIM\_PLLFLLSEL\_IRC48MHZ 3

22

[ 23](kinetis__sim_8h.md#ad107887d2ac9f8fed754889548a7ee92)#define KINETIS\_SIM\_ER32KSEL\_OSC32KCLK 0

[ 24](kinetis__sim_8h.md#a12c607155d49c7a83fce3619e63048a8)#define KINETIS\_SIM\_ER32KSEL\_RTC 2

[ 25](kinetis__sim_8h.md#a31926a82e92f3e7f9df4438661bdc381)#define KINETIS\_SIM\_ER32KSEL\_LPO1KHZ 3

26

[ 27](kinetis__sim_8h.md#a0ccfe586de3c6ab968c1440263fcd858)#define KINETIS\_SIM\_ENET\_CLK 4321

28

29

30#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_SIM\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [kinetis\_sim.h](kinetis__sim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
