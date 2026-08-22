---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp2__clock_8h_source.html
original_path: doxygen/html/stm32mp2__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp2\_clock.h

[Go to the documentation of this file.](stm32mp2__clock_8h.md)

1/\*

2 \* Copyright (C) 2025 Savoir-faire Linux, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32MP2\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32MP2\_CLOCK\_H\_

9

10#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

11

12/\* Undefine the common clocks macro \*/

13#undef STM32\_CLOCK

14

[ 22](stm32mp2__clock_8h.md#aeeec56ab8e50a43ce21a4dd459ac6c9a)#define STM32\_CLOCK(per, bit) (STM32\_CLOCK\_PERIPH\_##per) (1 << bit)

23

24/\* Clock reg \*/

[ 25](stm32mp2__clock_8h.md#aab77790587d5ff8d674beb25744a88ba)#define STM32\_CLK 1U

[ 26](stm32mp2__clock_8h.md#ae40a5105c1bf99aafd76f18d6957bc31)#define STM32\_LP\_CLK 2U

27

28/\* GPIO Peripheral \*/

[ 29](stm32mp2__clock_8h.md#a32bd45297022be14ed15c9772e8109f2)#define STM32\_CLOCK\_PERIPH\_GPIOA 0x52C

[ 30](stm32mp2__clock_8h.md#a32c6487ed7e24c991684f81f441f8d5d)#define STM32\_CLOCK\_PERIPH\_GPIOB 0x530

[ 31](stm32mp2__clock_8h.md#a3f2632c2cbff8cef0f93b8608ea1ae23)#define STM32\_CLOCK\_PERIPH\_GPIOC 0x534

[ 32](stm32mp2__clock_8h.md#a046f94e729a2cb3671b6d079f2fb11b7)#define STM32\_CLOCK\_PERIPH\_GPIOD 0x538

[ 33](stm32mp2__clock_8h.md#a3ad0bcfa60a4c8871e999969372e4e6f)#define STM32\_CLOCK\_PERIPH\_GPIOE 0x53C

[ 34](stm32mp2__clock_8h.md#aea08b708537234ca0f93966fcae019d3)#define STM32\_CLOCK\_PERIPH\_GPIOF 0x540

[ 35](stm32mp2__clock_8h.md#a2a1ac886c2d4dfa4f85c9d264533131a)#define STM32\_CLOCK\_PERIPH\_GPIOG 0x544

[ 36](stm32mp2__clock_8h.md#a52ffbf383d9153016a5535e4f00b0d06)#define STM32\_CLOCK\_PERIPH\_GPIOH 0x548

[ 37](stm32mp2__clock_8h.md#a87f8c3eae6c75c1ae6db2039ff453a26)#define STM32\_CLOCK\_PERIPH\_GPIOI 0x54C

[ 38](stm32mp2__clock_8h.md#ace35dbc8b0b11f7f455c068d554d583a)#define STM32\_CLOCK\_PERIPH\_GPIOJ 0x550

[ 39](stm32mp2__clock_8h.md#a2d841fc534ad733d599d4e7ad5982017)#define STM32\_CLOCK\_PERIPH\_GPIOK 0x554

[ 40](stm32mp2__clock_8h.md#ac7426ba0e6460abdeadf3fdc2905186e)#define STM32\_CLOCK\_PERIPH\_GPIOZ 0x558

41

42/\* USART/UART Peripheral \*/

[ 43](stm32mp2__clock_8h.md#a8189f9b07fd040c68981348ebd110bcf)#define STM32\_CLOCK\_PERIPH\_USART1 0x77C

[ 44](stm32mp2__clock_8h.md#a0cb50b85d43bf4d4d582fe50d2a22330)#define STM32\_CLOCK\_PERIPH\_USART2 0x780

[ 45](stm32mp2__clock_8h.md#a4e9105d91ff080466c92b81c613ac9cc)#define STM32\_CLOCK\_PERIPH\_USART3 0x784

[ 46](stm32mp2__clock_8h.md#a6a82f04d122f939ca9c8598864a3d23b)#define STM32\_CLOCK\_PERIPH\_UART4 0x788

[ 47](stm32mp2__clock_8h.md#a256ed97cebef2d9791352ccab17375ec)#define STM32\_CLOCK\_PERIPH\_UART5 0x78C

[ 48](stm32mp2__clock_8h.md#af10a9a7ee696c6eae472ba3d10f5ae12)#define STM32\_CLOCK\_PERIPH\_USART6 0x790

[ 49](stm32mp2__clock_8h.md#a29ab77f27485310a2de90462f849ee0f)#define STM32\_CLOCK\_PERIPH\_UART7 0x794

[ 50](stm32mp2__clock_8h.md#aab6dbf39e99478695f9218c41e24d107)#define STM32\_CLOCK\_PERIPH\_UART8 0x798

[ 51](stm32mp2__clock_8h.md#a8b0fd98a958ae01c8f329a68b24025af)#define STM32\_CLOCK\_PERIPH\_UART9 0x79C

52

[ 53](stm32mp2__clock_8h.md#a6d218dbd7c0503dbd31a87eb446b8905)#define STM32\_CLOCK\_PERIPH\_MIN STM32\_CLOCK\_PERIPH\_GPIOA

[ 54](stm32mp2__clock_8h.md#a57cecbd32ea98f98d52e348c7930dd1f)#define STM32\_CLOCK\_PERIPH\_MAX STM32\_CLOCK\_PERIPH\_UART9

55

56#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32MP2\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32mp2\_clock.h](stm32mp2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
