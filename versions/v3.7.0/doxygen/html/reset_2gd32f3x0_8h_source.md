---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/reset_2gd32f3x0_8h_source.html
original_path: doxygen/html/reset_2gd32f3x0_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f3x0.h

[Go to the documentation of this file.](reset_2gd32f3x0_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32F3X0\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32F3X0\_H\_

9

10#include "[gd32-common.h](gd32-common_8h.md)"

11

16

[ 17](reset_2gd32f3x0_8h.md#ab3c4f1337d87a22178010c65d48d3d30)#define GD32\_APB2RST\_OFFSET 0x0CU

[ 18](reset_2gd32f3x0_8h.md#aa81c1cadc283f658cea5c611e75fef5e)#define GD32\_APB1RST\_OFFSET 0x10U

[ 19](reset_2gd32f3x0_8h.md#a848c40f9a0d2b60863f461273f0fa37e)#define GD32\_AHBRST\_OFFSET 0x28U

[ 20](reset_2gd32f3x0_8h.md#a9197e68ba74b9955a45ce4e720099e1a)#define GD32\_ADDAPB1RST\_OFFSET 0xFCU

21

23

28

29/\* APB2 peripherals \*/

[ 30](reset_2gd32f3x0_8h.md#a02f94d0143c5ad76f2532d0b23e931d3)#define GD32\_RESET\_CFGCMP GD32\_RESET\_CONFIG(APB2RST, 0U)

[ 31](reset_2gd32f3x0_8h.md#aec7a7c37bfacf340a8e73b4f63d9bb8f)#define GD32\_RESET\_ADC GD32\_RESET\_CONFIG(APB2RST, 9U)

[ 32](reset_2gd32f3x0_8h.md#a2a7fd67d22598a774386a49ded2a9c72)#define GD32\_RESET\_TIMER0 GD32\_RESET\_CONFIG(APB2RST, 11U)

[ 33](reset_2gd32f3x0_8h.md#a64f740c7f65d696deb5f617654be9c5d)#define GD32\_RESET\_SPI0 GD32\_RESET\_CONFIG(APB2RST, 12U)

[ 34](reset_2gd32f3x0_8h.md#a6a03a7368d1e153ddf89547962711d35)#define GD32\_RESET\_USART0 GD32\_RESET\_CONFIG(APB2RST, 14U)

[ 35](reset_2gd32f3x0_8h.md#a2c23b5848b08dd9bb571408391764793)#define GD32\_RESET\_TIMER14 GD32\_RESET\_CONFIG(APB2RST, 16U)

[ 36](reset_2gd32f3x0_8h.md#ae1f1c4a1aa517935b9f76bc136a76809)#define GD32\_RESET\_TIMER15 GD32\_RESET\_CONFIG(APB2RST, 17U)

[ 37](reset_2gd32f3x0_8h.md#afe50a4990f8267250bd0b454ddfe2b73)#define GD32\_RESET\_TIMER16 GD32\_RESET\_CONFIG(APB2RST, 18U)

38

39/\* APB1 peripherals \*/

[ 40](reset_2gd32f3x0_8h.md#a97beb7e8223a64c2fca25679a466f9e0)#define GD32\_RESET\_TIMER1 GD32\_RESET\_CONFIG(APB1RST, 0U)

[ 41](reset_2gd32f3x0_8h.md#a113cfc98af5cb46151d0545cf54fe5aa)#define GD32\_RESET\_TIMER2 GD32\_RESET\_CONFIG(APB1RST, 1U)

[ 42](reset_2gd32f3x0_8h.md#a532af4dda1790a9b56bb8c023a3d01b7)#define GD32\_RESET\_TIMER5 GD32\_RESET\_CONFIG(APB1RST, 4U)

[ 43](reset_2gd32f3x0_8h.md#a012ec5ec4ff3dca4b788f9839be1c2f6)#define GD32\_RESET\_TIMER13 GD32\_RESET\_CONFIG(APB1RST, 8U)

[ 44](reset_2gd32f3x0_8h.md#a8aac1c0ab090d8568076f6d8556e5c7a)#define GD32\_RESET\_WWDGT GD32\_RESET\_CONFIG(APB1RST, 11U)

[ 45](reset_2gd32f3x0_8h.md#a27ae8979a4889e95867ed833d9843d07)#define GD32\_RESET\_SPI1 GD32\_RESET\_CONFIG(APB1RST, 14U)

[ 46](reset_2gd32f3x0_8h.md#aeb24e0ab9ae6be1c82593220c9719117)#define GD32\_RESET\_USART1 GD32\_RESET\_CONFIG(APB1RST, 17U)

[ 47](reset_2gd32f3x0_8h.md#a02b6250ebdbfa5de5f39f49c6d81f1ef)#define GD32\_RESET\_PMU GD32\_RESET\_CONFIG(APB1RST, 28U)

[ 48](reset_2gd32f3x0_8h.md#a4db6ebe67389f81c9fa20bc7747df578)#define GD32\_RESET\_DAC GD32\_RESET\_CONFIG(APB1RST, 29U)

[ 49](reset_2gd32f3x0_8h.md#a52ce71d770c8c34904d6adafaf360c40)#define GD32\_RESET\_CEC GD32\_RESET\_CONFIG(APB1RST, 30U)

50

51/\* AHB peripherals \*/

[ 52](reset_2gd32f3x0_8h.md#afd49566055b04e1ad0c58397379d6fca)#define GD32\_RESET\_USBFS GD32\_RESET\_CONFIG(AHBRST, 12U)

[ 53](reset_2gd32f3x0_8h.md#a3757cebbf6f3557b95ad38f58eeeec6f)#define GD32\_RESET\_GPIOA GD32\_RESET\_CONFIG(AHBRST, 17U)

[ 54](reset_2gd32f3x0_8h.md#af5961280a760bba841a7d9f2ba1b4e2f)#define GD32\_RESET\_GPIOB GD32\_RESET\_CONFIG(AHBRST, 18U)

[ 55](reset_2gd32f3x0_8h.md#a5a20c0f1febc4709b3038cb0c5ef55bc)#define GD32\_RESET\_GPIOC GD32\_RESET\_CONFIG(AHBRST, 19U)

[ 56](reset_2gd32f3x0_8h.md#ab9da13b274d377bdce3b3cce159c0cd4)#define GD32\_RESET\_GPIOD GD32\_RESET\_CONFIG(AHBRST, 20U)

[ 57](reset_2gd32f3x0_8h.md#a8cac628be929c7303ca2017b0e2a2798)#define GD32\_RESET\_GPIOF GD32\_RESET\_CONFIG(AHBRST, 22U)

[ 58](reset_2gd32f3x0_8h.md#ae81c4750d95cee3a16e9e7b08404b2ae)#define GD32\_RESET\_TSI GD32\_RESET\_CONFIG(AHBRST, 24U)

59

60/\* APB1 additional peripherals \*/

[ 61](reset_2gd32f3x0_8h.md#a595597cd5801d9255a07b0d3b87fb649)#define GD32\_RESET\_CTC GD32\_RESET\_CONFIG(ADDAPB1RST, 27U)

62

64

65#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32F3X0\_H\_ \*/

[gd32-common.h](gd32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32f3x0.h](reset_2gd32f3x0_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
