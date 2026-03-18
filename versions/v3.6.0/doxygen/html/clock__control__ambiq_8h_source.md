---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/clock__control__ambiq_8h_source.html
original_path: doxygen/html/clock__control__ambiq_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_ambiq.h

[Go to the documentation of this file.](clock__control__ambiq_8h.md)

1/\*

2 \* Copyright (c) 2023 Ambiq Micro Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_CLOCK\_CONTROL\_AMBIQ\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_CLOCK\_CONTROL\_AMBIQ\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 18](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8c)enum [clock\_control\_ambiq\_type](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8c) {

[ 19](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_BLE](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83),

[ 20](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_USB](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727),

[ 21](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_ADC](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e),

[ 22](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_AUADC](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208),

[ 23](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_DBGCTRL](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8),

[ 24](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_MISC](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc),

[ 25](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_CLKOUT](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3),

[ 26](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_PDM](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3),

[ 27](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IIS](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9),

[ 28](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IOM](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658),

[ 29](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_LFXTAL](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f),

[ 30](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b) [CLOCK\_CONTROL\_AMBIQ\_TYPE\_MAX](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b)

31};

32

33#ifdef \_\_cplusplus

34}

35#endif

36

37#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_CLOCK\_CONTROL\_AMBIQ\_H\_ \*/

[clock\_control\_ambiq\_type](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8c)

clock\_control\_ambiq\_type

Clocks handled by the CLOCK peripheral.

**Definition** clock\_control\_ambiq.h:18

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_ADC](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_ADC

**Definition** clock\_control\_ambiq.h:21

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_DBGCTRL](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_DBGCTRL

**Definition** clock\_control\_ambiq.h:23

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_AUADC](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_AUADC

**Definition** clock\_control\_ambiq.h:22

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_USB](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_USB

**Definition** clock\_control\_ambiq.h:20

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_MAX](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_MAX

**Definition** clock\_control\_ambiq.h:30

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IOM](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IOM

**Definition** clock\_control\_ambiq.h:28

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_BLE](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_BLE

**Definition** clock\_control\_ambiq.h:19

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_CLKOUT](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_CLKOUT

**Definition** clock\_control\_ambiq.h:25

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_MISC](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_MISC

**Definition** clock\_control\_ambiq.h:24

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_LFXTAL](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_LFXTAL

**Definition** clock\_control\_ambiq.h:29

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_PDM](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_PDM

**Definition** clock\_control\_ambiq.h:26

[CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IIS](clock__control__ambiq_8h.md#abe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9)

@ CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IIS

**Definition** clock\_control\_ambiq.h:27

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_ambiq.h](clock__control__ambiq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
