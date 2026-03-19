---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gd32a50x_8h_source.html
original_path: doxygen/html/gd32a50x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32a50x.h

[Go to the documentation of this file.](gd32a50x_8h.md)

1/\*

2 \* Copyright (c) 2022 YuLong Yao <feilongphone@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32A50X\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32A50X\_H\_

9

10#include "[gd32-common.h](gd32-common_8h.md)"

11

16

[ 17](gd32a50x_8h.md#a848c40f9a0d2b60863f461273f0fa37e)#define GD32\_AHBRST\_OFFSET 0x28U

[ 18](gd32a50x_8h.md#aa81c1cadc283f658cea5c611e75fef5e)#define GD32\_APB1RST\_OFFSET 0x10U

[ 19](gd32a50x_8h.md#ab3c4f1337d87a22178010c65d48d3d30)#define GD32\_APB2RST\_OFFSET 0x0CU

20

22

27

28

29/\* AHB peripherals \*/

[ 30](gd32a50x_8h.md#a030200dd583e944233eee559b7b31ea0)#define GD32\_RESET\_DMA0 GD32\_RESET\_CONFIG(AHBRST, 0U)

[ 31](gd32a50x_8h.md#a6dacbd858dd12980efab5f7f7ed6d646)#define GD32\_RESET\_DMA1 GD32\_RESET\_CONFIG(AHBRST, 1U)

[ 32](gd32a50x_8h.md#aacafe9c327da40b73ac774c0f2313dfa)#define GD32\_RESET\_SRAMSP GD32\_RESET\_CONFIG(AHBRST, 2U)

[ 33](gd32a50x_8h.md#a5fb8fd3b5dd036c91f777b2b15c8d09d)#define GD32\_RESET\_DMAMUX GD32\_RESET\_CONFIG(AHBRST, 3U)

[ 34](gd32a50x_8h.md#afaeeabf64ff1603fc382e96de3e531c8)#define GD32\_RESET\_FMCSP GD32\_RESET\_CONFIG(AHBRST, 4U)

[ 35](gd32a50x_8h.md#af47b6e0af43b63f4ee07bafa70290a38)#define GD32\_RESET\_CRC GD32\_RESET\_CONFIG(AHBRST, 6U)

[ 36](gd32a50x_8h.md#a8388a0042d5730c15efc9b65523f74ea)#define GD32\_RESET\_MFCOM GD32\_RESET\_CONFIG(AHBRST, 14U)

[ 37](gd32a50x_8h.md#a3757cebbf6f3557b95ad38f58eeeec6f)#define GD32\_RESET\_GPIOA GD32\_RESET\_CONFIG(AHBRST, 17U)

[ 38](gd32a50x_8h.md#af5961280a760bba841a7d9f2ba1b4e2f)#define GD32\_RESET\_GPIOB GD32\_RESET\_CONFIG(AHBRST, 18U)

[ 39](gd32a50x_8h.md#a5a20c0f1febc4709b3038cb0c5ef55bc)#define GD32\_RESET\_GPIOC GD32\_RESET\_CONFIG(AHBRST, 19U)

[ 40](gd32a50x_8h.md#ab9da13b274d377bdce3b3cce159c0cd4)#define GD32\_RESET\_GPIOD GD32\_RESET\_CONFIG(AHBRST, 20U)

[ 41](gd32a50x_8h.md#a846d86e02331a6b4b1cf1c7cc7132fdf)#define GD32\_RESET\_GPIOE GD32\_RESET\_CONFIG(AHBRST, 21U)

[ 42](gd32a50x_8h.md#a8cac628be929c7303ca2017b0e2a2798)#define GD32\_RESET\_GPIOF GD32\_RESET\_CONFIG(AHBRST, 22U)

43

44/\* APB1 peripherals \*/

[ 45](gd32a50x_8h.md#a97beb7e8223a64c2fca25679a466f9e0)#define GD32\_RESET\_TIMER1 GD32\_RESET\_CONFIG(APB1RST, 0U)

[ 46](gd32a50x_8h.md#a532af4dda1790a9b56bb8c023a3d01b7)#define GD32\_RESET\_TIMER5 GD32\_RESET\_CONFIG(APB1RST, 4U)

[ 47](gd32a50x_8h.md#ab23dd190237e1223cd5273742f9d2e10)#define GD32\_RESET\_TIMER6 GD32\_RESET\_CONFIG(APB1RST, 5U)

[ 48](gd32a50x_8h.md#a8aac1c0ab090d8568076f6d8556e5c7a)#define GD32\_RESET\_WWDGT GD32\_RESET\_CONFIG(APB1RST, 11U)

[ 49](gd32a50x_8h.md#a27ae8979a4889e95867ed833d9843d07)#define GD32\_RESET\_SPI1 GD32\_RESET\_CONFIG(APB1RST, 14U)

[ 50](gd32a50x_8h.md#aeb24e0ab9ae6be1c82593220c9719117)#define GD32\_RESET\_USART1 GD32\_RESET\_CONFIG(APB1RST, 17U)

[ 51](gd32a50x_8h.md#a362e90b2303107bd5ec1cd57662e986a)#define GD32\_RESET\_USART2 GD32\_RESET\_CONFIG(APB1RST, 18U)

[ 52](gd32a50x_8h.md#a12b532298a73feed3aa42ad53cf6ca79)#define GD32\_RESET\_I2C0 GD32\_RESET\_CONFIG(APB1RST, 21U)

[ 53](gd32a50x_8h.md#a9b9bec0c724fce490ba57090fe5329cc)#define GD32\_RESET\_I2C1 GD32\_RESET\_CONFIG(APB1RST, 22U)

[ 54](gd32a50x_8h.md#a4947823ca79706894ea1e9f39e96dfbd)#define GD32\_RESET\_BKP GD32\_RESET\_CONFIG(APB1RST, 26U)

[ 55](gd32a50x_8h.md#a02b6250ebdbfa5de5f39f49c6d81f1ef)#define GD32\_RESET\_PMU GD32\_RESET\_CONFIG(APB1RST, 28U)

[ 56](gd32a50x_8h.md#a4db6ebe67389f81c9fa20bc7747df578)#define GD32\_RESET\_DAC GD32\_RESET\_CONFIG(APB1RST, 29U)

57

58/\* APB2 peripherals \*/

[ 59](gd32a50x_8h.md#afd91e374f836fdf42970966e9d4677c4)#define GD32\_RESET\_SYSCFG GD32\_RESET\_CONFIG(APB2RST, 0U)

[ 60](gd32a50x_8h.md#a492c3d07d5e6280710cefe442cb0d951)#define GD32\_RESET\_CMP GD32\_RESET\_CONFIG(APB2RST, 1U)

[ 61](gd32a50x_8h.md#aa94c4237849ff01aecbf9024ba7b9cd1)#define GD32\_RESET\_ADC0 GD32\_RESET\_CONFIG(APB2RST, 9U)

[ 62](gd32a50x_8h.md#a92af4e6fa98371a209c79d7a81e68f36)#define GD32\_RESET\_ADC1 GD32\_RESET\_CONFIG(APB2RST, 10U)

[ 63](gd32a50x_8h.md#a2a7fd67d22598a774386a49ded2a9c72)#define GD32\_RESET\_TIMER0 GD32\_RESET\_CONFIG(APB2RST, 11U)

[ 64](gd32a50x_8h.md#a64f740c7f65d696deb5f617654be9c5d)#define GD32\_RESET\_SPI0 GD32\_RESET\_CONFIG(APB2RST, 12U)

[ 65](gd32a50x_8h.md#aa705f811b509f9aa4e671a3651b22bec)#define GD32\_RESET\_TIMER7 GD32\_RESET\_CONFIG(APB2RST, 13U)

[ 66](gd32a50x_8h.md#a6a03a7368d1e153ddf89547962711d35)#define GD32\_RESET\_USART0 GD32\_RESET\_CONFIG(APB2RST, 14U)

[ 67](gd32a50x_8h.md#a9a2bedc63e775b9df709f73830dc58d3)#define GD32\_RESET\_TIMER19 GD32\_RESET\_CONFIG(APB2RST, 20U)

[ 68](gd32a50x_8h.md#ad7c12971a83513f687ccaac10401864b)#define GD32\_RESET\_TIMER20 GD32\_RESET\_CONFIG(APB2RST, 21U)

[ 69](gd32a50x_8h.md#abd9db0f9def85c62e713f348faba27fb)#define GD32\_RESET\_TRIGSEL GD32\_RESET\_CONFIG(APB2RST, 29U)

[ 70](gd32a50x_8h.md#a2d54a57f102daf1a931e340dff46567e)#define GD32\_RESET\_CAN0 GD32\_RESET\_CONFIG(APB2RST, 30U)

[ 71](gd32a50x_8h.md#ab8248f4b27355ae5eed7876294bf54ca)#define GD32\_RESET\_CAN1 GD32\_RESET\_CONFIG(APB2RST, 31U)

72

74

75#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32A50X\_H\_ \*/

[gd32-common.h](gd32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32a50x.h](gd32a50x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
