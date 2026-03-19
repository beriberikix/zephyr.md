---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32n6__reset_8h_source.html
original_path: doxygen/html/stm32n6__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32n6\_reset.h

[Go to the documentation of this file.](stm32n6__reset_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32N6\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32N6\_RESET\_H\_

9

10#include "[stm32-common.h](stm32-common_8h.md)"

11

12/\* RCC bus reset register offset \*/

[ 13](stm32n6__reset_8h.md#a3a527d4f03ed172cd0217eeb28ca5670)#define STM32\_RESET\_BUS\_AHB1 0x210

[ 14](stm32n6__reset_8h.md#a0abdd5105ad8f47103e5905294bc503e)#define STM32\_RESET\_BUS\_AHB2 0x214

[ 15](stm32n6__reset_8h.md#a3b6e85f37b2348f7a57752430bbe9ed4)#define STM32\_RESET\_BUS\_AHB3 0x218

[ 16](stm32n6__reset_8h.md#ab3c50488687aae8e2e1deb2624f5221c)#define STM32\_RESET\_BUS\_AHB4 0x21C

[ 17](stm32n6__reset_8h.md#a46ea9f7abcdf8026c74ffc5afb842819)#define STM32\_RESET\_BUS\_AHB5 0x220

[ 18](stm32n6__reset_8h.md#af6147c04f9dc0679c14f750afbfdeb17)#define STM32\_RESET\_BUS\_APB1L 0x224

[ 19](stm32n6__reset_8h.md#a74bf429a826fb31d5d5623a2358e9062)#define STM32\_RESET\_BUS\_APB1H 0x228

[ 20](stm32n6__reset_8h.md#adb41bde903446da14725436f08119509)#define STM32\_RESET\_BUS\_APB2 0x22C

[ 21](stm32n6__reset_8h.md#a5f45d493e42cef86a1a5077e1ac93a95)#define STM32\_RESET\_BUS\_APB4L 0x234

[ 22](stm32n6__reset_8h.md#ae6c7492056f352ea3b35789a44e119fc)#define STM32\_RESET\_BUS\_APB4H 0x238

[ 23](stm32n6__reset_8h.md#a5075dae938866f5f8e066d0caf3053ce)#define STM32\_RESET\_BUS\_APB5 0x23C

24

25#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32N6\_RESET\_H\_ \*/

[stm32-common.h](stm32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32n6\_reset.h](stm32n6__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
