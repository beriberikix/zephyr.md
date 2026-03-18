---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32-pinctrl-common_8h_source.html
original_path: doxygen/html/stm32-pinctrl-common_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-pinctrl-common.h

[Go to the documentation of this file.](stm32-pinctrl-common_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_STM32\_PINCTRL\_COMMON\_H\_

8#define ZEPHYR\_STM32\_PINCTRL\_COMMON\_H\_

9

13

[ 14](stm32-pinctrl-common_8h.md#a031a76d5d56cbb86e5c5dffad52732b5)#define STM32\_PORTA 0 /\* IO port A \*/

[ 15](stm32-pinctrl-common_8h.md#ab5be546a1dccb589e6be842575829019)#define STM32\_PORTB 1 /\* .. \*/

[ 16](stm32-pinctrl-common_8h.md#ac56b63d53a5c187035e4386bdb5e6ffa)#define STM32\_PORTC 2

[ 17](stm32-pinctrl-common_8h.md#a866773d51364d1821245a910c03e8686)#define STM32\_PORTD 3

[ 18](stm32-pinctrl-common_8h.md#a1402c542481316eedd39e3cda89410bf)#define STM32\_PORTE 4

[ 19](stm32-pinctrl-common_8h.md#aac43eb483c2b7b744c216b9e2cf62770)#define STM32\_PORTF 5

[ 20](stm32-pinctrl-common_8h.md#ac4464e020843f97772036ae27da7abd5)#define STM32\_PORTG 6

[ 21](stm32-pinctrl-common_8h.md#a744d089635ebefd4bfb65b673699256a)#define STM32\_PORTH 7

[ 22](stm32-pinctrl-common_8h.md#ab11184138506e9df5e93a10f28f45d63)#define STM32\_PORTI 8

[ 23](stm32-pinctrl-common_8h.md#a0ea163478aef753a739f96f9bf448d8b)#define STM32\_PORTJ 9

[ 24](stm32-pinctrl-common_8h.md#a057f431270f633fedc990bb971ce6a05)#define STM32\_PORTK 10 /\* IO port K \*/

[ 25](stm32-pinctrl-common_8h.md#a19abb84f712b1899d8aaadfad34301bd)#define STM32\_PORTM 12 /\* IO port M (0xC) \*/

[ 26](stm32-pinctrl-common_8h.md#ac354044c6615887e456a65a0aa5e226c)#define STM32\_PORTN 13

[ 27](stm32-pinctrl-common_8h.md#ac363d8900ccc9a9e7b022c8f558b53f7)#define STM32\_PORTO 14

[ 28](stm32-pinctrl-common_8h.md#a2bc75591bd6f3010c0b58b66bead967d)#define STM32\_PORTP 15 /\* IO port P (0xF) \*/

29

30#ifndef STM32\_PORTS\_MAX

[ 31](stm32-pinctrl-common_8h.md#a615b26e8931dfb9ed75e49368eac572d)#define STM32\_PORTS\_MAX (STM32\_PORTP + 1)

32#endif

33

[ 37](stm32-pinctrl-common_8h.md#ae496c0ca2dc170f1443b6e35db2a2d1e)#define STM32PIN(\_port, \_pin) \

38 (\_port << 4 | \_pin)

39

40#endif /\* ZEPHYR\_STM32\_PINCTRL\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32-pinctrl-common.h](stm32-pinctrl-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
