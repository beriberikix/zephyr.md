---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32wb0__clock_8h_source.html
original_path: doxygen/html/stm32wb0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wb0\_clock.h

[Go to the documentation of this file.](stm32wb0__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WB0\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WB0\_CLOCK\_H\_

8

10#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

11

[ 17](stm32wb0__clock_8h.md#a577b1cb1a04e486119c9834374728190)#define STM32\_SRC\_CLKSLOWMUX (STM32\_SRC\_LSI + 1)

[ 18](stm32wb0__clock_8h.md#a7495e637711c2545d1450de275ea0e72)#define STM32\_SRC\_CLK16MHZ (STM32\_SRC\_CLKSLOWMUX + 1)

[ 19](stm32wb0__clock_8h.md#a41eda33344045e079dba6b5858b15315)#define STM32\_SRC\_CLK32MHZ (STM32\_SRC\_CLK16MHZ + 1)

20

[ 22](stm32wb0__clock_8h.md#afebca0f2112b116cb43cc8759c0e5580)#define STM32\_CLOCK\_BUS\_AHB0 0x50

[ 23](stm32wb0__clock_8h.md#a479869134499d0ddd172b0cbede44ea1)#define STM32\_CLOCK\_BUS\_APB0 0x54

[ 24](stm32wb0__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x58

[ 25](stm32wb0__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x60

26

[ 27](stm32wb0__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_AHB0

[ 28](stm32wb0__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_APB2

29

[ 31](stm32wb0__clock_8h.md#afb2336a33a23f9671b26010594232ba3)#define CFGR\_REG 0x08

32

[ 34](stm32wb0__clock_8h.md#a54b415b2adb40a9ddfa18049a94621fd)#define APB2ENR\_REG 0x60

35

37

38/\* WB05/WB09 only \*/

[ 39](stm32wb0__clock_8h.md#aac31ca48bf87a722f6e0519f25f764dd)#define LPUART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 13, CFGR\_REG)

40/\* WB06/WB07 only \*/

[ 41](stm32wb0__clock_8h.md#ac7c015b568c293db3e2601cc7d8cefa6)#define SPI2\_I2S2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 1, 22, CFGR\_REG)

42/\* `mask` is only 0x1 for WB06/WB07, but a single definition with mask=0x3 is acceptable \*/

[ 43](stm32wb0__clock_8h.md#ad432f60ec25ceaec41b9017bf4f62708)#define SPI3\_I2S3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 3, 22, CFGR\_REG)

44

45#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32WB0\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32wb0\_clock.h](stm32wb0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
