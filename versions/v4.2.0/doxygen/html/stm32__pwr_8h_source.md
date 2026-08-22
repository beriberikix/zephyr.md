---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32__pwr_8h_source.html
original_path: doxygen/html/stm32__pwr_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_pwr.h

[Go to the documentation of this file.](stm32__pwr_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_POWER\_STM32\_PWR\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_POWER\_STM32\_PWR\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

16

21

22/\* Use this flag on series where wake-up event source is fixed/not configurable \*/

[ 23](stm32__pwr_8h.md#adf19445e60cddb3648576b0d00286037)#define STM32\_PWR\_WKUP\_PIN\_NOT\_MUXED STM32\_PWR\_WKUP\_EVT\_SRC\_0

[ 24](stm32__pwr_8h.md#ae42d060e1acd34b67f6abafd1c3beb0c)#define STM32\_PWR\_WKUP\_EVT\_SRC\_0 BIT(0)

[ 25](stm32__pwr_8h.md#afe3257abb473831116e1a4de37967643)#define STM32\_PWR\_WKUP\_EVT\_SRC\_1 BIT(1)

[ 26](stm32__pwr_8h.md#ab8da300a49d90c217e7ca5636f728579)#define STM32\_PWR\_WKUP\_EVT\_SRC\_2 BIT(2)

27

29

31

32#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_POWER\_STM32\_PWR\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [power](dir_69b170904c37bf233464183190e7a190.md)
- [stm32\_pwr.h](stm32__pwr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
