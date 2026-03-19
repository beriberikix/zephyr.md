---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32h7rs__reset_8h_source.html
original_path: doxygen/html/stm32h7rs__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h7rs\_reset.h

[Go to the documentation of this file.](stm32h7rs__reset_8h.md)

1/\*

2 \* Copyright (c) 2022 Google Inc

3 \* Copyright (c) 2024 STMicroelectronics

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32H7RS\_RESET\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32H7RS\_RESET\_H\_

10

11#include "[stm32-common.h](stm32-common_8h.md)"

12

13/\* RCC bus reset register offset \*/

[ 14](stm32h7rs__reset_8h.md#a3a527d4f03ed172cd0217eeb28ca5670)#define STM32\_RESET\_BUS\_AHB1 0x80

[ 15](stm32h7rs__reset_8h.md#a0abdd5105ad8f47103e5905294bc503e)#define STM32\_RESET\_BUS\_AHB2 0x84

[ 16](stm32h7rs__reset_8h.md#a3b6e85f37b2348f7a57752430bbe9ed4)#define STM32\_RESET\_BUS\_AHB3 0xA4

[ 17](stm32h7rs__reset_8h.md#a46ea9f7abcdf8026c74ffc5afb842819)#define STM32\_RESET\_BUS\_AHB5 0x7C

[ 18](stm32h7rs__reset_8h.md#a5075dae938866f5f8e066d0caf3053ce)#define STM32\_RESET\_BUS\_APB5 0x8C

[ 19](stm32h7rs__reset_8h.md#ab3c50488687aae8e2e1deb2624f5221c)#define STM32\_RESET\_BUS\_AHB4 0x88

[ 20](stm32h7rs__reset_8h.md#af6147c04f9dc0679c14f750afbfdeb17)#define STM32\_RESET\_BUS\_APB1L 0x90

[ 21](stm32h7rs__reset_8h.md#a74bf429a826fb31d5d5623a2358e9062)#define STM32\_RESET\_BUS\_APB1H 0x94

[ 22](stm32h7rs__reset_8h.md#adb41bde903446da14725436f08119509)#define STM32\_RESET\_BUS\_APB2 0x98

[ 23](stm32h7rs__reset_8h.md#a8d4a6e3b1fd48eebc8a22ac16960eff7)#define STM32\_RESET\_BUS\_APB4 0x9C

24

25#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32H7RS\_RESET\_H\_ \*/

[stm32-common.h](stm32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32h7rs\_reset.h](stm32h7rs__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
