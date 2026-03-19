---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32__common__clocks_8h_source.html
original_path: doxygen/html/stm32__common__clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 19](stm32__common__clocks_8h.md#ae14130ea70f0df4747f357dc863ea456)#define STM32\_MCO\_CFGR\_REG\_MASK 0xFFFFU

[ 20](stm32__common__clocks_8h.md#ab5cb026c26c0059a2920288ea0305170)#define STM32\_MCO\_CFGR\_REG\_SHIFT 0U

[ 21](stm32__common__clocks_8h.md#ace1dd95ce384cbd71a7cf71e23b450b6)#define STM32\_MCO\_CFGR\_SHIFT\_MASK 0x3FU

[ 22](stm32__common__clocks_8h.md#a90ef8b401020d2d31233ab5e0aef3953)#define STM32\_MCO\_CFGR\_SHIFT\_SHIFT 16U

[ 23](stm32__common__clocks_8h.md#af4128292c207270d5abfe104ebf723da)#define STM32\_MCO\_CFGR\_MASK\_MASK 0x1FU

[ 24](stm32__common__clocks_8h.md#abe5f0de675895eb047ad7d8ba15b444b)#define STM32\_MCO\_CFGR\_MASK\_SHIFT 22U

[ 25](stm32__common__clocks_8h.md#aa0fd0438f4f39510b942f085443da629)#define STM32\_MCO\_CFGR\_VAL\_MASK 0x1FU

[ 26](stm32__common__clocks_8h.md#a1c2cadfeafe266885df8e3b6ca22aa1c)#define STM32\_MCO\_CFGR\_VAL\_SHIFT 27U

27

[ 42](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)#define STM32\_MCO\_CFGR(val, mask, shift, reg) \

43 ((((reg) & STM32\_MCO\_CFGR\_REG\_MASK) << STM32\_MCO\_CFGR\_REG\_SHIFT) | \

44 (((shift) & STM32\_MCO\_CFGR\_SHIFT\_MASK) << STM32\_MCO\_CFGR\_SHIFT\_SHIFT) | \

45 (((mask) & STM32\_MCO\_CFGR\_MASK\_MASK) << STM32\_MCO\_CFGR\_MASK\_SHIFT) | \

46 (((val) & STM32\_MCO\_CFGR\_VAL\_MASK) << STM32\_MCO\_CFGR\_VAL\_SHIFT))

47

[ 55](stm32__common__clocks_8h.md#a0fec36253cbc233df3b564feb5d873a4)#define STM32\_CLOCK(bus, bit) (STM32\_CLOCK\_BUS\_##bus) (1 << bit)

56

57#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32\_COMMON\_CLOCKS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32\_common\_clocks.h](stm32__common__clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
