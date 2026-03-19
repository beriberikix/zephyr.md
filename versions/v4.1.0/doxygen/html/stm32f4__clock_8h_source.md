---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32f4__clock_8h_source.html
original_path: doxygen/html/stm32f4__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f4\_clock.h

[Go to the documentation of this file.](stm32f4__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F4\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F4\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12

[ 14](stm32f4__clock_8h.md#a186de4b3566a20794e4483a9569abe3c)#define STM32\_CLOCK\_BUS\_AHB1 0x030

[ 15](stm32f4__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x034

[ 16](stm32f4__clock_8h.md#ab2a3c819828eb0186ac3a3f15f4b4569)#define STM32\_CLOCK\_BUS\_AHB3 0x038

[ 17](stm32f4__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x040

[ 18](stm32f4__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x044

[ 19](stm32f4__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x0A8

20

[ 21](stm32f4__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB1

[ 22](stm32f4__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB3

23

25/\* RM0386, 0390, 0402, 0430 § Dedicated Clock configuration register (RCC\_DCKCFGRx) \*/

26

28/\* defined in stm32\_common\_clocks.h \*/

30/\* Low speed clocks defined in stm32\_common\_clocks.h \*/

[ 31](stm32f4__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_LSI + 1)

[ 32](stm32f4__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_HSI + 1)

[ 34](stm32f4__clock_8h.md#a473d0d57680b535a9e9298600a1e1aab)#define STM32\_SRC\_PLL\_P (STM32\_SRC\_HSE + 1)

[ 35](stm32f4__clock_8h.md#ab3a03011d2d433feaff934c3828e1f27)#define STM32\_SRC\_PLL\_Q (STM32\_SRC\_PLL\_P + 1)

[ 36](stm32f4__clock_8h.md#aca252b1d875fbd9dce6350f1845e5439)#define STM32\_SRC\_PLL\_R (STM32\_SRC\_PLL\_Q + 1)

[ 38](stm32f4__clock_8h.md#a8b1667544712cc7844623ce4722ed76c)#define STM32\_SRC\_PLLI2S\_Q (STM32\_SRC\_PLL\_R + 1)

[ 39](stm32f4__clock_8h.md#af7f88624feab3e965c74ef1789e62c5a)#define STM32\_SRC\_PLLI2S\_R (STM32\_SRC\_PLLI2S\_Q + 1)

40/\* CLK48MHz sources \*/

[ 41](stm32f4__clock_8h.md#a9ed069ee6c3e053ea39ae391eff1f0f5)#define STM32\_SRC\_CK48 (STM32\_SRC\_PLLI2S\_R + 1)

42

43/\* I2S\_CKIN not supported yet \*/

44/\* #define STM32\_SRC\_I2S\_CKIN TBD \*/

45

[ 47](stm32f4__clock_8h.md#afb2336a33a23f9671b26010594232ba3)#define CFGR\_REG 0x08

[ 49](stm32f4__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)#define BDCR\_REG 0x70

50

[ 53](stm32f4__clock_8h.md#a2d34d604e16d874235b74bdbc8103bed)#define I2S\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 23, CFGR\_REG)

[ 54](stm32f4__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 21, CFGR\_REG)

[ 55](stm32f4__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 24, CFGR\_REG)

[ 56](stm32f4__clock_8h.md#ab5fc05cb6aa1154c54c29b95f3154a75)#define MCO2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 30, CFGR\_REG)

[ 57](stm32f4__clock_8h.md#ab02a0ccbb8588979ca4742c72c59589f)#define MCO2\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 27, CFGR\_REG)

[ 59](stm32f4__clock_8h.md#a4836377699efa295c56d340e150695b0)#define RTC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 8, BDCR\_REG)

60

61/\* MCO prescaler : division factor \*/

[ 62](stm32f4__clock_8h.md#aa6d6446aa7a1c84324475f6e8665fbb7)#define MCO\_PRE\_DIV\_1 0

[ 63](stm32f4__clock_8h.md#a36db847c7932669759f64844a15c42c3)#define MCO\_PRE\_DIV\_2 4

[ 64](stm32f4__clock_8h.md#a1d99057b6886474182adffcff4f246f2)#define MCO\_PRE\_DIV\_3 5

[ 65](stm32f4__clock_8h.md#a74c5b485d9169c489ab19e788b43c657)#define MCO\_PRE\_DIV\_4 6

[ 66](stm32f4__clock_8h.md#aad3773cb5fbea15e6cddf688dea3cd04)#define MCO\_PRE\_DIV\_5 7

67

68#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32F4\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f4\_clock.h](stm32f4__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
