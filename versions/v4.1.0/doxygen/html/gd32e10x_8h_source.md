---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32e10x_8h_source.html
original_path: doxygen/html/gd32e10x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32e10x.h

[Go to the documentation of this file.](gd32e10x_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32E10X\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32E10X\_H\_

9

10#include "[gd32-common.h](gd32-common_8h.md)"

11

16

[ 17](gd32e10x_8h.md#ab3c4f1337d87a22178010c65d48d3d30)#define GD32\_APB2RST\_OFFSET 0x0CU

[ 18](gd32e10x_8h.md#aa81c1cadc283f658cea5c611e75fef5e)#define GD32\_APB1RST\_OFFSET 0x10U

[ 19](gd32e10x_8h.md#a848c40f9a0d2b60863f461273f0fa37e)#define GD32\_AHBRST\_OFFSET 0x28U

[ 20](gd32e10x_8h.md#a9197e68ba74b9955a45ce4e720099e1a)#define GD32\_ADDAPB1RST\_OFFSET 0xE0U

21

23

28

29/\* APB2 peripherals \*/

[ 30](gd32e10x_8h.md#a185b70daaff8ee9db604008a0d3b0029)#define GD32\_RESET\_AFIO GD32\_RESET\_CONFIG(APB2RST, 0U)

[ 31](gd32e10x_8h.md#a3757cebbf6f3557b95ad38f58eeeec6f)#define GD32\_RESET\_GPIOA GD32\_RESET\_CONFIG(APB2RST, 2U)

[ 32](gd32e10x_8h.md#af5961280a760bba841a7d9f2ba1b4e2f)#define GD32\_RESET\_GPIOB GD32\_RESET\_CONFIG(APB2RST, 3U)

[ 33](gd32e10x_8h.md#a5a20c0f1febc4709b3038cb0c5ef55bc)#define GD32\_RESET\_GPIOC GD32\_RESET\_CONFIG(APB2RST, 4U)

[ 34](gd32e10x_8h.md#ab9da13b274d377bdce3b3cce159c0cd4)#define GD32\_RESET\_GPIOD GD32\_RESET\_CONFIG(APB2RST, 5U)

[ 35](gd32e10x_8h.md#a846d86e02331a6b4b1cf1c7cc7132fdf)#define GD32\_RESET\_GPIOE GD32\_RESET\_CONFIG(APB2RST, 6U)

[ 36](gd32e10x_8h.md#aa94c4237849ff01aecbf9024ba7b9cd1)#define GD32\_RESET\_ADC0 GD32\_RESET\_CONFIG(APB2RST, 9U)

[ 37](gd32e10x_8h.md#a92af4e6fa98371a209c79d7a81e68f36)#define GD32\_RESET\_ADC1 GD32\_RESET\_CONFIG(APB2RST, 10U)

[ 38](gd32e10x_8h.md#a2a7fd67d22598a774386a49ded2a9c72)#define GD32\_RESET\_TIMER0 GD32\_RESET\_CONFIG(APB2RST, 11U)

[ 39](gd32e10x_8h.md#a64f740c7f65d696deb5f617654be9c5d)#define GD32\_RESET\_SPI0 GD32\_RESET\_CONFIG(APB2RST, 12U)

[ 40](gd32e10x_8h.md#aa705f811b509f9aa4e671a3651b22bec)#define GD32\_RESET\_TIMER7 GD32\_RESET\_CONFIG(APB2RST, 13U)

[ 41](gd32e10x_8h.md#a6a03a7368d1e153ddf89547962711d35)#define GD32\_RESET\_USART0 GD32\_RESET\_CONFIG(APB2RST, 14U)

[ 42](gd32e10x_8h.md#a3304de281ad58c3daa7539c0c13baa3a)#define GD32\_RESET\_TIMER8 GD32\_RESET\_CONFIG(APB2RST, 19U)

[ 43](gd32e10x_8h.md#a9422ecb4a384c91d6498c2cba75a4b78)#define GD32\_RESET\_TIMER9 GD32\_RESET\_CONFIG(APB2RST, 20U)

[ 44](gd32e10x_8h.md#ace4a405286adfe6212497aa14d6ec8b1)#define GD32\_RESET\_TIMER10 GD32\_RESET\_CONFIG(APB2RST, 21U)

45

46/\* APB1 peripherals \*/

[ 47](gd32e10x_8h.md#a97beb7e8223a64c2fca25679a466f9e0)#define GD32\_RESET\_TIMER1 GD32\_RESET\_CONFIG(APB1RST, 0U)

[ 48](gd32e10x_8h.md#a113cfc98af5cb46151d0545cf54fe5aa)#define GD32\_RESET\_TIMER2 GD32\_RESET\_CONFIG(APB1RST, 1U)

[ 49](gd32e10x_8h.md#a0e077bd7bba73a98e2dc97de52dfef81)#define GD32\_RESET\_TIMER3 GD32\_RESET\_CONFIG(APB1RST, 2U)

[ 50](gd32e10x_8h.md#a8c2042627d0c1e0248ea51b0a1c2fd63)#define GD32\_RESET\_TIMER4 GD32\_RESET\_CONFIG(APB1RST, 3U)

[ 51](gd32e10x_8h.md#a532af4dda1790a9b56bb8c023a3d01b7)#define GD32\_RESET\_TIMER5 GD32\_RESET\_CONFIG(APB1RST, 4U)

[ 52](gd32e10x_8h.md#ab23dd190237e1223cd5273742f9d2e10)#define GD32\_RESET\_TIMER6 GD32\_RESET\_CONFIG(APB1RST, 5U)

[ 53](gd32e10x_8h.md#a9e880d91571e3cba08beddf6a4b51afd)#define GD32\_RESET\_TIMER11 GD32\_RESET\_CONFIG(APB1RST, 6U)

[ 54](gd32e10x_8h.md#a949b2dd18643f528ec987cfadfd179e6)#define GD32\_RESET\_TIMER12 GD32\_RESET\_CONFIG(APB1RST, 7U)

[ 55](gd32e10x_8h.md#a012ec5ec4ff3dca4b788f9839be1c2f6)#define GD32\_RESET\_TIMER13 GD32\_RESET\_CONFIG(APB1RST, 8U)

[ 56](gd32e10x_8h.md#a8aac1c0ab090d8568076f6d8556e5c7a)#define GD32\_RESET\_WWDGT GD32\_RESET\_CONFIG(APB1RST, 11U)

[ 57](gd32e10x_8h.md#a27ae8979a4889e95867ed833d9843d07)#define GD32\_RESET\_SPI1 GD32\_RESET\_CONFIG(APB1RST, 14U)

[ 58](gd32e10x_8h.md#a9ee38df6bff18cb40a16bce410aae937)#define GD32\_RESET\_SPI2 GD32\_RESET\_CONFIG(APB1RST, 15U)

[ 59](gd32e10x_8h.md#aeb24e0ab9ae6be1c82593220c9719117)#define GD32\_RESET\_USART1 GD32\_RESET\_CONFIG(APB1RST, 17U)

[ 60](gd32e10x_8h.md#a362e90b2303107bd5ec1cd57662e986a)#define GD32\_RESET\_USART2 GD32\_RESET\_CONFIG(APB1RST, 18U)

[ 61](gd32e10x_8h.md#a58caa0f60b03f664298bd75c8f198e9b)#define GD32\_RESET\_UART3 GD32\_RESET\_CONFIG(APB1RST, 19U)

[ 62](gd32e10x_8h.md#a9787ffdf0edba62357937f3bd4e33f53)#define GD32\_RESET\_UART4 GD32\_RESET\_CONFIG(APB1RST, 20U)

[ 63](gd32e10x_8h.md#a12b532298a73feed3aa42ad53cf6ca79)#define GD32\_RESET\_I2C0 GD32\_RESET\_CONFIG(APB1RST, 21U)

[ 64](gd32e10x_8h.md#a9b9bec0c724fce490ba57090fe5329cc)#define GD32\_RESET\_I2C1 GD32\_RESET\_CONFIG(APB1RST, 22U)

[ 65](gd32e10x_8h.md#a2d54a57f102daf1a931e340dff46567e)#define GD32\_RESET\_CAN0 GD32\_RESET\_CONFIG(APB1RST, 25U)

[ 66](gd32e10x_8h.md#ab8248f4b27355ae5eed7876294bf54ca)#define GD32\_RESET\_CAN1 GD32\_RESET\_CONFIG(APB1RST, 26U)

[ 67](gd32e10x_8h.md#a3e5ef6ea3472891a835e1a3d2ae84454)#define GD32\_RESET\_BKPI GD32\_RESET\_CONFIG(APB1RST, 27U)

[ 68](gd32e10x_8h.md#a02b6250ebdbfa5de5f39f49c6d81f1ef)#define GD32\_RESET\_PMU GD32\_RESET\_CONFIG(APB1RST, 28U)

[ 69](gd32e10x_8h.md#a4db6ebe67389f81c9fa20bc7747df578)#define GD32\_RESET\_DAC GD32\_RESET\_CONFIG(APB1RST, 29U)

70

71/\* AHB peripherals \*/

[ 72](gd32e10x_8h.md#afd49566055b04e1ad0c58397379d6fca)#define GD32\_RESET\_USBFS GD32\_RESET\_CONFIG(AHBRST, 12U)

73

74/\* APB1 additional peripherals \*/

[ 75](gd32e10x_8h.md#a595597cd5801d9255a07b0d3b87fb649)#define GD32\_RESET\_CTC GD32\_RESET\_CONFIG(ADDAPB1RST, 27U)

76

78

79#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32E10X\_H\_ \*/

[gd32-common.h](gd32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32e10x.h](gd32e10x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
