---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/clock__control__silabs_8h_source.html
original_path: doxygen/html/clock__control__silabs_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_silabs.h

[Go to the documentation of this file.](clock__control__silabs_8h.md)

1/\*

2 \* Copyright (c) 2024 Silicon Laboratories Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_SILABS\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_SILABS\_H\_

9

10#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

11

12#if defined(CONFIG\_SOC\_SERIES\_EFR32MG21)

13#include <[zephyr/dt-bindings/clock/silabs/xg21-clock.h](xg21-clock_8h.md)>

14#elif defined(CONFIG\_SOC\_SERIES\_EFR32BG22)

15#include <[zephyr/dt-bindings/clock/silabs/xg22-clock.h](xg22-clock_8h.md)>

16#elif defined(CONFIG\_SOC\_SERIES\_EFR32MG24)

17#include <[zephyr/dt-bindings/clock/silabs/xg24-clock.h](xg24-clock_8h.md)>

18#elif defined(CONFIG\_SOC\_SERIES\_EFR32BG27)

19#include <[zephyr/dt-bindings/clock/silabs/xg27-clock.h](xg27-clock_8h.md)>

20#endif

21

[ 22](structsilabs__clock__control__cmu__config.md)struct [silabs\_clock\_control\_cmu\_config](structsilabs__clock__control__cmu__config.md) {

[ 23](structsilabs__clock__control__cmu__config.md#a5792da0cf4363d3127cff97562763f45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus\_clock](structsilabs__clock__control__cmu__config.md#a5792da0cf4363d3127cff97562763f45);

[ 24](structsilabs__clock__control__cmu__config.md#a8e9a65a261eae1fefcf0d697a8a59bf9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [branch](structsilabs__clock__control__cmu__config.md#a8e9a65a261eae1fefcf0d697a8a59bf9);

25};

26

[ 27](clock__control__silabs_8h.md#a2238842842469b06a3cb0d0cf187583c)#define SILABS\_DT\_CLOCK\_CFG(node\_id) \

28 { \

29 .bus\_clock = DT\_CLOCKS\_CELL(node\_id, enable), \

30 .branch = DT\_CLOCKS\_CELL(node\_id, branch), \

31 }

32

[ 33](clock__control__silabs_8h.md#a109d85a9e8fe8ec3730927a91d885721)#define SILABS\_DT\_INST\_CLOCK\_CFG(inst) \

34 { \

35 .bus\_clock = DT\_INST\_CLOCKS\_CELL(inst, enable), \

36 .branch = DT\_INST\_CLOCKS\_CELL(inst, branch), \

37 }

38

39#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_SILABS\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[silabs\_clock\_control\_cmu\_config](structsilabs__clock__control__cmu__config.md)

**Definition** clock\_control\_silabs.h:22

[silabs\_clock\_control\_cmu\_config::bus\_clock](structsilabs__clock__control__cmu__config.md#a5792da0cf4363d3127cff97562763f45)

uint32\_t bus\_clock

**Definition** clock\_control\_silabs.h:23

[silabs\_clock\_control\_cmu\_config::branch](structsilabs__clock__control__cmu__config.md#a8e9a65a261eae1fefcf0d697a8a59bf9)

uint8\_t branch

**Definition** clock\_control\_silabs.h:24

[xg21-clock.h](xg21-clock_8h.md)

[xg22-clock.h](xg22-clock_8h.md)

[xg24-clock.h](xg24-clock_8h.md)

[xg27-clock.h](xg27-clock_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_silabs.h](clock__control__silabs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
