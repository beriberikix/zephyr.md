---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gd32l23x_8h_source.html
original_path: doxygen/html/gd32l23x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32l23x.h

[Go to the documentation of this file.](gd32l23x_8h.md)

1/\*

2 \* Copyright (c) 2022 BrainCo.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32L23X\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32L23X\_H\_

9

10#include "[gd32-common.h](gd32-common_8h.md)"

11

16

[ 17](gd32l23x_8h.md#a4f5347051ef3b9897ce80d198ebe69ff)#define GD32\_AHB1RST\_OFFSET 0x28U

[ 18](gd32l23x_8h.md#aa81c1cadc283f658cea5c611e75fef5e)#define GD32\_APB1RST\_OFFSET 0x10U

[ 19](gd32l23x_8h.md#ab3c4f1337d87a22178010c65d48d3d30)#define GD32\_APB2RST\_OFFSET 0x0CU

20

22

27

28/\* AHB1 peripherals \*/

[ 29](gd32l23x_8h.md#af47b6e0af43b63f4ee07bafa70290a38)#define GD32\_RESET\_CRC GD32\_RESET\_CONFIG(AHB1RST, 6U)

[ 30](gd32l23x_8h.md#a3757cebbf6f3557b95ad38f58eeeec6f)#define GD32\_RESET\_GPIOA GD32\_RESET\_CONFIG(AHB1RST, 17U)

[ 31](gd32l23x_8h.md#af5961280a760bba841a7d9f2ba1b4e2f)#define GD32\_RESET\_GPIOB GD32\_RESET\_CONFIG(AHB1RST, 18U)

[ 32](gd32l23x_8h.md#a5a20c0f1febc4709b3038cb0c5ef55bc)#define GD32\_RESET\_GPIOC GD32\_RESET\_CONFIG(AHB1RST, 19U)

[ 33](gd32l23x_8h.md#ab9da13b274d377bdce3b3cce159c0cd4)#define GD32\_RESET\_GPIOD GD32\_RESET\_CONFIG(AHB1RST, 20U)

[ 34](gd32l23x_8h.md#a8cac628be929c7303ca2017b0e2a2798)#define GD32\_RESET\_GPIOF GD32\_RESET\_CONFIG(AHB1RST, 22U)

35

36/\* AHB2 peripherals \*/

[ 37](gd32l23x_8h.md#af5246b2bf8a46533a89390bddbd68460)#define GD32\_RESET\_CAU GD32\_RESET\_CONFIG(AHB2RST, 1U)

[ 38](gd32l23x_8h.md#ac811f656607426b5ef151ae7a829549d)#define GD32\_RESET\_TRNG GD32\_RESET\_CONFIG(AHB2RST, 3U)

39

40/\* APB1 peripherals \*/

[ 41](gd32l23x_8h.md#a97beb7e8223a64c2fca25679a466f9e0)#define GD32\_RESET\_TIMER1 GD32\_RESET\_CONFIG(APB1RST, 0U)

[ 42](gd32l23x_8h.md#a113cfc98af5cb46151d0545cf54fe5aa)#define GD32\_RESET\_TIMER2 GD32\_RESET\_CONFIG(APB1RST, 1U)

[ 43](gd32l23x_8h.md#a532af4dda1790a9b56bb8c023a3d01b7)#define GD32\_RESET\_TIMER5 GD32\_RESET\_CONFIG(APB1RST, 4U)

[ 44](gd32l23x_8h.md#ab23dd190237e1223cd5273742f9d2e10)#define GD32\_RESET\_TIMER6 GD32\_RESET\_CONFIG(APB1RST, 5U)

[ 45](gd32l23x_8h.md#a9e880d91571e3cba08beddf6a4b51afd)#define GD32\_RESET\_TIMER11 GD32\_RESET\_CONFIG(APB1RST, 8U)

[ 46](gd32l23x_8h.md#a2cc5718a46d67152a7f630ea70cbd913)#define GD32\_RESET\_LPTIMER GD32\_RESET\_CONFIG(APB1RST, 9U)

[ 47](gd32l23x_8h.md#ab7a15bcc11e5a9a8d64f74756e3d9dc7)#define GD32\_RESET\_SLCD GD32\_RESET\_CONFIG(APB1RST, 10U)

[ 48](gd32l23x_8h.md#a8aac1c0ab090d8568076f6d8556e5c7a)#define GD32\_RESET\_WWDGT GD32\_RESET\_CONFIG(APB1RST, 11U)

[ 49](gd32l23x_8h.md#a27ae8979a4889e95867ed833d9843d07)#define GD32\_RESET\_SPI1 GD32\_RESET\_CONFIG(APB1RST, 14U)

[ 50](gd32l23x_8h.md#aeb24e0ab9ae6be1c82593220c9719117)#define GD32\_RESET\_USART1 GD32\_RESET\_CONFIG(APB1RST, 17U)

[ 51](gd32l23x_8h.md#a7291f2e2117e9404590ece160bbbc9ee)#define GD32\_RESET\_LPUART GD32\_RESET\_CONFIG(APB1RST, 18U)

[ 52](gd32l23x_8h.md#a58caa0f60b03f664298bd75c8f198e9b)#define GD32\_RESET\_UART3 GD32\_RESET\_CONFIG(APB1RST, 19U)

[ 53](gd32l23x_8h.md#a9787ffdf0edba62357937f3bd4e33f53)#define GD32\_RESET\_UART4 GD32\_RESET\_CONFIG(APB1RST, 20U)

[ 54](gd32l23x_8h.md#a12b532298a73feed3aa42ad53cf6ca79)#define GD32\_RESET\_I2C0 GD32\_RESET\_CONFIG(APB1RST, 21U)

[ 55](gd32l23x_8h.md#a9b9bec0c724fce490ba57090fe5329cc)#define GD32\_RESET\_I2C1 GD32\_RESET\_CONFIG(APB1RST, 22U)

[ 56](gd32l23x_8h.md#adb48cf6c15c86d0d99c529c6597abc34)#define GD32\_RESET\_USBD GD32\_RESET\_CONFIG(APB1RST, 23U)

[ 57](gd32l23x_8h.md#ad37ee8c46a981ed4fb73dcde74ca051c)#define GD32\_RESET\_I2C2 GD32\_RESET\_CONFIG(APB1RST, 24U)

[ 58](gd32l23x_8h.md#a02b6250ebdbfa5de5f39f49c6d81f1ef)#define GD32\_RESET\_PMU GD32\_RESET\_CONFIG(APB1RST, 28U)

[ 59](gd32l23x_8h.md#a4db6ebe67389f81c9fa20bc7747df578)#define GD32\_RESET\_DAC GD32\_RESET\_CONFIG(APB1RST, 29U)

[ 60](gd32l23x_8h.md#a595597cd5801d9255a07b0d3b87fb649)#define GD32\_RESET\_CTC GD32\_RESET\_CONFIG(APB1RST, 30U)

61

62/\* APB2 peripherals \*/

[ 63](gd32l23x_8h.md#afd91e374f836fdf42970966e9d4677c4)#define GD32\_RESET\_SYSCFG GD32\_RESET\_CONFIG(APB2RST, 0U)

[ 64](gd32l23x_8h.md#a492c3d07d5e6280710cefe442cb0d951)#define GD32\_RESET\_CMP GD32\_RESET\_CONFIG(APB2RST, 1U)

[ 65](gd32l23x_8h.md#aec7a7c37bfacf340a8e73b4f63d9bb8f)#define GD32\_RESET\_ADC GD32\_RESET\_CONFIG(APB2RST, 9U)

[ 66](gd32l23x_8h.md#a3304de281ad58c3daa7539c0c13baa3a)#define GD32\_RESET\_TIMER8 GD32\_RESET\_CONFIG(APB2RST, 11U)

[ 67](gd32l23x_8h.md#a64f740c7f65d696deb5f617654be9c5d)#define GD32\_RESET\_SPI0 GD32\_RESET\_CONFIG(APB2RST, 12U)

[ 68](gd32l23x_8h.md#a6a03a7368d1e153ddf89547962711d35)#define GD32\_RESET\_USART0 GD32\_RESET\_CONFIG(APB2RST, 14U)

69

71

72#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32L23X\_H\_ \*/

[gd32-common.h](gd32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32l23x.h](gd32l23x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
