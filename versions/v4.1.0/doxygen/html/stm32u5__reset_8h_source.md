---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32u5__reset_8h_source.html
original_path: doxygen/html/stm32u5__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32u5\_reset.h

[Go to the documentation of this file.](stm32u5__reset_8h.md)

1/\*

2 \* Copyright (c) 2022 Google Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32U5\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32U5\_RESET\_H\_

9

10#include "[stm32-common.h](stm32-common_8h.md)"

11

12/\* RCC bus reset register offset \*/

[ 13](stm32u5__reset_8h.md#a3a527d4f03ed172cd0217eeb28ca5670)#define STM32\_RESET\_BUS\_AHB1 0x60

[ 14](stm32u5__reset_8h.md#aa7d17981058f6a4b26a1078a70f0c586)#define STM32\_RESET\_BUS\_AHB2L 0x64

[ 15](stm32u5__reset_8h.md#a0da2cb5433e759c66bb8578415c606c4)#define STM32\_RESET\_BUS\_AHB2H 0x68

[ 16](stm32u5__reset_8h.md#a3b6e85f37b2348f7a57752430bbe9ed4)#define STM32\_RESET\_BUS\_AHB3 0x6C

[ 17](stm32u5__reset_8h.md#af6147c04f9dc0679c14f750afbfdeb17)#define STM32\_RESET\_BUS\_APB1L 0x74

[ 18](stm32u5__reset_8h.md#a74bf429a826fb31d5d5623a2358e9062)#define STM32\_RESET\_BUS\_APB1H 0x78

[ 19](stm32u5__reset_8h.md#adb41bde903446da14725436f08119509)#define STM32\_RESET\_BUS\_APB2 0x7C

[ 20](stm32u5__reset_8h.md#a85fc5d8e3d9615f3df0ff8782bb3f79a)#define STM32\_RESET\_BUS\_APB3 0x80

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32U5\_RESET\_H\_ \*/

[stm32-common.h](stm32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32u5\_reset.h](stm32u5__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
