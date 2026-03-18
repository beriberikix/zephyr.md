---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32f1__adc_8h_source.html
original_path: doxygen/html/stm32f1__adc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1\_adc.h

[Go to the documentation of this file.](stm32f1__adc_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicrelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32F1\_ADC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32F1\_ADC\_H\_

8

9#include <[zephyr/dt-bindings/adc/stm32\_adc.h](stm32__adc_8h.md)>

10

11/\*

12 \* For STM32 F1 and similar, the only available resolution is 12-bit

13 \* and there is no register to set it.

14 \* We still need the macro to get the value of the resolution but the driver

15 \* does not set the resolution in any register by checking that the register

16 \* address is configured as 0xFF

17 \*/

[ 18](stm32f1__adc_8h.md#a172393ce17e4f6f94c78b5b171354120)#define STM32\_ADC\_RES\_REG 0xFF

[ 19](stm32f1__adc_8h.md#abd31ebaa20fd7e23b81c61926ff9adbe)#define STM32\_ADC\_RES\_SHIFT 0

[ 20](stm32f1__adc_8h.md#a2a727c7d9a6496b2fdc3da2d24841e3f)#define STM32\_ADC\_RES\_MASK 0x00

[ 21](stm32f1__adc_8h.md#a2a1f597025647c8f33b562804ce9e312)#define STM32\_ADC\_RES\_REG\_VAL 0x00

22

[ 23](stm32f1__adc_8h.md#ad4bec6dade85253c3ea3152f87786471)#define STM32F1\_ADC\_RES(resolution) \

24 STM32\_ADC\_RES(resolution, STM32\_ADC\_RES\_REG\_VAL)

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32F1\_ADC\_H\_ \*/

[stm32\_adc.h](stm32__adc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [stm32f1\_adc.h](stm32f1__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
