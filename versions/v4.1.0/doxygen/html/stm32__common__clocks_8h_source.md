---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32__common__clocks_8h_source.html
original_path: doxygen/html/stm32__common__clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_common\_clocks.h

[Go to the documentation of this file.](stm32__common__clocks_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_COMMON\_CLOCKS\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_COMMON\_CLOCKS\_H\_

8

[ 10](stm32__common__clocks_8h.md#a79a13b49235b90035b5ed7f62c9bf9bf)#define STM32\_SRC\_SYSCLK 0x001

[ 12](stm32__common__clocks_8h.md#a42412accdd52b7ef9460583db634a4b1)#define STM32\_SRC\_LSE 0x002

[ 13](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640)#define STM32\_SRC\_LSI 0x003

14

[ 16](stm32__common__clocks_8h.md#ae998967c5f8ed059e757a6906b46ed4e)#define NO\_SEL 0xFF

17

[ 18](stm32__common__clocks_8h.md#a208c97071646d6a363fa8abcd44908f0)#define STM32\_CLOCK\_DIV\_SHIFT 12

19

[ 21](stm32__common__clocks_8h.md#a49981976097d7e684ac5e5e094ecdf9b)#define STM32\_CLOCK\_DIV(div) (((div) - 1) << STM32\_CLOCK\_DIV\_SHIFT)

22

[ 24](stm32__common__clocks_8h.md#a9ad0be6cd421f8b608f74a3676bf9d6d)#define STM32\_DT\_CLKSEL\_REG\_MASK 0xFFFFU

[ 25](stm32__common__clocks_8h.md#a007f65a597867a03a6dc9b1e73d27a2d)#define STM32\_DT\_CLKSEL\_REG\_SHIFT 0U

[ 26](stm32__common__clocks_8h.md#a01c12bdd437dd33ff01e2ed45617dfff)#define STM32\_DT\_CLKSEL\_SHIFT\_MASK 0x3FU

[ 27](stm32__common__clocks_8h.md#a6db7bff4699d60cc318494bdebd85b42)#define STM32\_DT\_CLKSEL\_SHIFT\_SHIFT 16U

[ 28](stm32__common__clocks_8h.md#afaa23be867f51da7ddb8b72ef429e51a)#define STM32\_DT\_CLKSEL\_MASK\_MASK 0x1FU

[ 29](stm32__common__clocks_8h.md#a627de44bae59bdf8febc6518bcaeb595)#define STM32\_DT\_CLKSEL\_MASK\_SHIFT 22U

[ 30](stm32__common__clocks_8h.md#a7ba7ca05cdad21911bc39d69e5674e3b)#define STM32\_DT\_CLKSEL\_VAL\_MASK 0x1FU

[ 31](stm32__common__clocks_8h.md#a7353643376cec80b57a89886e19ad6d9)#define STM32\_DT\_CLKSEL\_VAL\_SHIFT 27U

32

[ 46](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg) \

47 ((((reg) & STM32\_DT\_CLKSEL\_REG\_MASK) << STM32\_DT\_CLKSEL\_REG\_SHIFT) | \

48 (((shift) & STM32\_DT\_CLKSEL\_SHIFT\_MASK) << STM32\_DT\_CLKSEL\_SHIFT\_SHIFT) | \

49 (((mask) & STM32\_DT\_CLKSEL\_MASK\_MASK) << STM32\_DT\_CLKSEL\_MASK\_SHIFT) | \

50 (((val) & STM32\_DT\_CLKSEL\_VAL\_MASK) << STM32\_DT\_CLKSEL\_VAL\_SHIFT))

51

[ 59](stm32__common__clocks_8h.md#a0fec36253cbc233df3b564feb5d873a4)#define STM32\_CLOCK(bus, bit) (STM32\_CLOCK\_BUS\_##bus) (1 << bit)

60

61#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_COMMON\_CLOCKS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32\_common\_clocks.h](stm32__common__clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
