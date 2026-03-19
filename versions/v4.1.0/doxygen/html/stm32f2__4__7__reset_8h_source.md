---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32f2__4__7__reset_8h_source.html
original_path: doxygen/html/stm32f2__4__7__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f2\_4\_7\_reset.h

[Go to the documentation of this file.](stm32f2__4__7__reset_8h.md)

1/\*

2 \* Copyright (c) 2022 Google Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32F2\_4\_7\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32F2\_4\_7\_RESET\_H\_

9

10#include "[stm32-common.h](stm32-common_8h.md)"

11

12/\* RCC bus reset register offset \*/

[ 13](stm32f2__4__7__reset_8h.md#a3a527d4f03ed172cd0217eeb28ca5670)#define STM32\_RESET\_BUS\_AHB1 0x10

[ 14](stm32f2__4__7__reset_8h.md#a0abdd5105ad8f47103e5905294bc503e)#define STM32\_RESET\_BUS\_AHB2 0x14

[ 15](stm32f2__4__7__reset_8h.md#a3b6e85f37b2348f7a57752430bbe9ed4)#define STM32\_RESET\_BUS\_AHB3 0x18

[ 16](stm32f2__4__7__reset_8h.md#a13b6ab32fc5f9ef5b246bb0b104c6652)#define STM32\_RESET\_BUS\_APB1 0x20

[ 17](stm32f2__4__7__reset_8h.md#adb41bde903446da14725436f08119509)#define STM32\_RESET\_BUS\_APB2 0x24

18

19#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32F2\_4\_7\_RESET\_H\_ \*/

[stm32-common.h](stm32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32f2\_4\_7\_reset.h](stm32f2__4__7__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
