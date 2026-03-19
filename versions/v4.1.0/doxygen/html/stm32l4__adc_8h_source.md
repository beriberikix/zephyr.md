---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32l4__adc_8h_source.html
original_path: doxygen/html/stm32l4__adc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32l4\_adc.h

[Go to the documentation of this file.](stm32l4__adc_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicrelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32L4\_ADC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32L4\_ADC\_H\_

8

9#include <[zephyr/dt-bindings/adc/stm32\_adc.h](stm32__adc_8h.md)>

10

11/\* STM32 ADC resolution register for L4 and similar \*/

[ 12](stm32l4__adc_8h.md#a172393ce17e4f6f94c78b5b171354120)#define STM32\_ADC\_RES\_REG 0x0C

[ 13](stm32l4__adc_8h.md#abd31ebaa20fd7e23b81c61926ff9adbe)#define STM32\_ADC\_RES\_SHIFT 3

[ 14](stm32l4__adc_8h.md#a2a727c7d9a6496b2fdc3da2d24841e3f)#define STM32\_ADC\_RES\_MASK BIT\_MASK(2)

15

16#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32L4\_ADC\_H\_ \*/

[stm32\_adc.h](stm32__adc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [stm32l4\_adc.h](stm32l4__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
