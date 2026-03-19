---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h_source.html
original_path: doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atmel\_sam\_pmc.h

[Go to the documentation of this file.](drivers_2clock__control_2atmel__sam__pmc_8h.md)

1/\*

2 \* Copyright (c) 2023 Gerson Fernando Budke <nandojve@gmail.com

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ATMEL\_SAM\_PMC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ATMEL\_SAM\_PMC\_H\_

9

10#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

11#include <[zephyr/dt-bindings/clock/atmel\_sam\_pmc.h](dt-bindings_2clock_2atmel__sam__pmc_8h.md)>

12

[ 13](drivers_2clock__control_2atmel__sam__pmc_8h.md#a90fa2e9a2226f7a2cb8926e9091b5eb3)#define SAM\_DT\_PMC\_CONTROLLER DEVICE\_DT\_GET(DT\_NODELABEL(pmc))

14

[ 15](structatmel__sam__pmc__config.md)struct [atmel\_sam\_pmc\_config](structatmel__sam__pmc__config.md) {

[ 16](structatmel__sam__pmc__config.md#a8e2bbec7dd455159da3f469c6fb45635) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clock\_type](structatmel__sam__pmc__config.md#a8e2bbec7dd455159da3f469c6fb45635);

[ 17](structatmel__sam__pmc__config.md#aab47279eb62b0d9fb6e097a935f09edd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [peripheral\_id](structatmel__sam__pmc__config.md#aab47279eb62b0d9fb6e097a935f09edd);

18};

19

[ 20](drivers_2clock__control_2atmel__sam__pmc_8h.md#afe5b223995886a213b8e9108fdce94d5)#define SAM\_DT\_CLOCK\_PMC\_CFG(clock\_id, node\_id) \

21 { \

22 .clock\_type = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clock\_id, clock\_type), \

23 .peripheral\_id = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clock\_id, peripheral\_id)\

24 }

25

[ 26](drivers_2clock__control_2atmel__sam__pmc_8h.md#a0f6e3f89dcfde77d27b2685220055109)#define SAM\_DT\_INST\_CLOCK\_PMC\_CFG(inst) SAM\_DT\_CLOCK\_PMC\_CFG(0, DT\_DRV\_INST(inst))

27

[ 28](drivers_2clock__control_2atmel__sam__pmc_8h.md#adc7b9d880d6ebcf81b47eafc223e8512)#define SAM\_DT\_CLOCKS\_PMC\_CFG(node\_id) \

29 { \

30 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

31 SAM\_DT\_CLOCK\_PMC\_CFG, (,), node\_id) \

32 }

33

[ 34](drivers_2clock__control_2atmel__sam__pmc_8h.md#af27b70e3c0fa178c3096748bb636b704)#define SAM\_DT\_INST\_CLOCKS\_PMC\_CFG(inst) \

35 SAM\_DT\_CLOCKS\_PMC\_CFG(DT\_DRV\_INST(inst))

36

37#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ATMEL\_SAM\_PMC\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[atmel\_sam\_pmc.h](dt-bindings_2clock_2atmel__sam__pmc_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[atmel\_sam\_pmc\_config](structatmel__sam__pmc__config.md)

**Definition** atmel\_sam\_pmc.h:15

[atmel\_sam\_pmc\_config::clock\_type](structatmel__sam__pmc__config.md#a8e2bbec7dd455159da3f469c6fb45635)

uint32\_t clock\_type

**Definition** atmel\_sam\_pmc.h:16

[atmel\_sam\_pmc\_config::peripheral\_id](structatmel__sam__pmc__config.md#aab47279eb62b0d9fb6e097a935f09edd)

uint32\_t peripheral\_id

**Definition** atmel\_sam\_pmc.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [atmel\_sam\_pmc.h](drivers_2clock__control_2atmel__sam__pmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
