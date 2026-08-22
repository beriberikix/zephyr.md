---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp2__reset_8h_source.html
original_path: doxygen/html/stm32mp2__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp2\_reset.h

[Go to the documentation of this file.](stm32mp2__reset_8h.md)

1/\*

2 \* Copyright (C) 2025 Savoir-faire Linux, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32MP2\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32MP2\_RESET\_H\_

9

[ 20](stm32mp2__reset_8h.md#a47abaeb040742e28fdb98aac76d5bc38)#define STM32\_RESET(per, bit) (((STM32\_RESET\_PERIPH\_##per##) << 5U) | (bit))

21

22/\* Reset reg \*/

[ 23](stm32mp2__reset_8h.md#a1eee43a8d6b28956f35c394a1917b363)#define STM32\_RST 0U

24

25/\* USART/UART Peripheral \*/

[ 26](stm32mp2__reset_8h.md#a43b84745610e5dbdea3cfb253dc07b1c)#define STM32\_RESET\_PERIPH\_USART1 0x77C

[ 27](stm32mp2__reset_8h.md#a6a85d397faeb4b9dbcba84b82cb46312)#define STM32\_RESET\_PERIPH\_USART2 0x780

[ 28](stm32mp2__reset_8h.md#a97840fd9714543ef1702c08f330a8aa8)#define STM32\_RESET\_PERIPH\_USART3 0x784

[ 29](stm32mp2__reset_8h.md#a300d2fa9b0d1f3e45fa6602c8961294a)#define STM32\_RESET\_PERIPH\_UART4 0x788

[ 30](stm32mp2__reset_8h.md#a027d34aecea80dba893a640ec8fe7c7f)#define STM32\_RESET\_PERIPH\_UART5 0x78C

[ 31](stm32mp2__reset_8h.md#a8a5634c095db0805d72bab6013df0fdb)#define STM32\_RESET\_PERIPH\_USART6 0x790

[ 32](stm32mp2__reset_8h.md#aed8be264b66a3722b3c2145aa000a13f)#define STM32\_RESET\_PERIPH\_UART7 0x794

[ 33](stm32mp2__reset_8h.md#a8cd02f97af1db57427c652132b9dc065)#define STM32\_RESET\_PERIPH\_UART8 0x798

[ 34](stm32mp2__reset_8h.md#aeb438be7b039d1d301273bd557f6d3ae)#define STM32\_RESET\_PERIPH\_UART9 0x79C

35

36#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32MP2\_RESET\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32mp2\_reset.h](stm32mp2__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
