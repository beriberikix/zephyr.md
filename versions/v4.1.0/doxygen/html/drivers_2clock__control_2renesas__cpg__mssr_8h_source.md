---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h_source.html
original_path: doxygen/html/drivers_2clock__control_2renesas__cpg__mssr_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_cpg\_mssr.h

[Go to the documentation of this file.](drivers_2clock__control_2renesas__cpg__mssr_8h.md)

1/\*

2 \* Copyright (c) 2016 Open-RnD Sp. z o.o.

3 \* Copyright (c) 2016 BayLibre, SAS

4 \* Copyright (c) 2017 Linaro Limited.

5 \* Copyright (c) 2017 RnDity Sp. z o.o.

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RCAR\_CLOCK\_CONTROL\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RCAR\_CLOCK\_CONTROL\_H\_

11

12#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

13#include <[zephyr/dt-bindings/clock/renesas\_cpg\_mssr.h](dt-bindings_2clock_2renesas__cpg__mssr_8h.md)>

14

[ 15](structrcar__cpg__clk.md)struct [rcar\_cpg\_clk](structrcar__cpg__clk.md) {

[ 16](structrcar__cpg__clk.md#a126cf65226ac7e3521c724d4c9d7b3a4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [domain](structrcar__cpg__clk.md#a126cf65226ac7e3521c724d4c9d7b3a4);

[ 17](structrcar__cpg__clk.md#aff97932d122b50e3d7546adfe2fc29f5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [module](structrcar__cpg__clk.md#aff97932d122b50e3d7546adfe2fc29f5);

[ 18](structrcar__cpg__clk.md#a84f173b12e610177932cf58d85659f0e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rate](structrcar__cpg__clk.md#a84f173b12e610177932cf58d85659f0e);

19};

20

21#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RCAR\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[renesas\_cpg\_mssr.h](dt-bindings_2clock_2renesas__cpg__mssr_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[rcar\_cpg\_clk](structrcar__cpg__clk.md)

**Definition** renesas\_cpg\_mssr.h:15

[rcar\_cpg\_clk::domain](structrcar__cpg__clk.md#a126cf65226ac7e3521c724d4c9d7b3a4)

uint32\_t domain

**Definition** renesas\_cpg\_mssr.h:16

[rcar\_cpg\_clk::rate](structrcar__cpg__clk.md#a84f173b12e610177932cf58d85659f0e)

uint32\_t rate

**Definition** renesas\_cpg\_mssr.h:18

[rcar\_cpg\_clk::module](structrcar__cpg__clk.md#aff97932d122b50e3d7546adfe2fc29f5)

uint32\_t module

**Definition** renesas\_cpg\_mssr.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [renesas\_cpg\_mssr.h](drivers_2clock__control_2renesas__cpg__mssr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
