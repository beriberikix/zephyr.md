---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gd32vf103-clocks_8h_source.html
original_path: doxygen/html/gd32vf103-clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32vf103-clocks.h

[Go to the documentation of this file.](gd32vf103-clocks_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32VF103\_CLOCKS\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32VF103\_CLOCKS\_H\_

9

10#include "[gd32-clocks-common.h](gd32-clocks-common_8h.md)"

11

16

[ 17](gd32vf103-clocks_8h.md#a510e385774abf879310b061273eb4068)#define GD32\_AHBEN\_OFFSET 0x14U

[ 18](gd32vf103-clocks_8h.md#a4b2aa082b4b2200b7f2b1663c30f205c)#define GD32\_APB1EN\_OFFSET 0x1CU

[ 19](gd32vf103-clocks_8h.md#a9d794746eea796b39b3ae55b1614d9d9)#define GD32\_APB2EN\_OFFSET 0x18U

20

22

27

28/\* AHB peripherals \*/

[ 29](gd32vf103-clocks_8h.md#a7728f090fb52201d3d1162881b80dc3e)#define GD32\_CLOCK\_DMA0 GD32\_CLOCK\_CONFIG(AHBEN, 0U)

[ 30](gd32vf103-clocks_8h.md#af6c6eb89797f088a78722ce007ae47e5)#define GD32\_CLOCK\_DMA1 GD32\_CLOCK\_CONFIG(AHBEN, 1U)

[ 31](gd32vf103-clocks_8h.md#a7f201b05f8c284e62be5bf9290a84a67)#define GD32\_CLOCK\_SRAMSP GD32\_CLOCK\_CONFIG(AHBEN, 2U)

[ 32](gd32vf103-clocks_8h.md#acdbf40a9d897a38daca0d8bd5f81fc1a)#define GD32\_CLOCK\_FMCSP GD32\_CLOCK\_CONFIG(AHBEN, 4U)

[ 33](gd32vf103-clocks_8h.md#a0971986459094517a13221629cc89e95)#define GD32\_CLOCK\_CRC GD32\_CLOCK\_CONFIG(AHBEN, 6U)

[ 34](gd32vf103-clocks_8h.md#af4ca0b77d98d8825493b868d19d7759a)#define GD32\_CLOCK\_EXMC GD32\_CLOCK\_CONFIG(AHBEN, 8U)

[ 35](gd32vf103-clocks_8h.md#ae11c1f5ccf256d32377eb9a6f07026f2)#define GD32\_CLOCK\_USBFS GD32\_CLOCK\_CONFIG(AHBEN, 12U)

36

37/\* APB1 peripherals \*/

[ 38](gd32vf103-clocks_8h.md#af084c2bf11ddfe04c80c3fac272c30e7)#define GD32\_CLOCK\_TIMER1 GD32\_CLOCK\_CONFIG(APB1EN, 0U)

[ 39](gd32vf103-clocks_8h.md#a41623cb4499589163c0697a7a669ac25)#define GD32\_CLOCK\_TIMER2 GD32\_CLOCK\_CONFIG(APB1EN, 1U)

[ 40](gd32vf103-clocks_8h.md#afb5aa7f1705febd51a92f9370bd03d14)#define GD32\_CLOCK\_TIMER3 GD32\_CLOCK\_CONFIG(APB1EN, 2U)

[ 41](gd32vf103-clocks_8h.md#a9d52a01572ab9309c5ebd3a0def8542f)#define GD32\_CLOCK\_TIMER4 GD32\_CLOCK\_CONFIG(APB1EN, 3U)

[ 42](gd32vf103-clocks_8h.md#aae8d2c65bc590e7147407099e8a938b7)#define GD32\_CLOCK\_TIMER5 GD32\_CLOCK\_CONFIG(APB1EN, 4U)

[ 43](gd32vf103-clocks_8h.md#a0e1b450d86f9e5b08a5738116742b429)#define GD32\_CLOCK\_TIMER6 GD32\_CLOCK\_CONFIG(APB1EN, 5U)

[ 44](gd32vf103-clocks_8h.md#acd4e6949e5fb08e13129174ddd6f2e70)#define GD32\_CLOCK\_WWDGT GD32\_CLOCK\_CONFIG(APB1EN, 11U)

[ 45](gd32vf103-clocks_8h.md#a61a4d4edd729635d5fcdd200a13a0b9b)#define GD32\_CLOCK\_SPI1 GD32\_CLOCK\_CONFIG(APB1EN, 14U)

[ 46](gd32vf103-clocks_8h.md#a4bb28caf86a54e343c75a597b0bddc20)#define GD32\_CLOCK\_SPI2 GD32\_CLOCK\_CONFIG(APB1EN, 15U)

[ 47](gd32vf103-clocks_8h.md#a0f4528cfba6c9b129cc3aeae8220a178)#define GD32\_CLOCK\_USART1 GD32\_CLOCK\_CONFIG(APB1EN, 17U)

[ 48](gd32vf103-clocks_8h.md#a477baf1c1a265b4c86019a5f52820622)#define GD32\_CLOCK\_USART2 GD32\_CLOCK\_CONFIG(APB1EN, 18U)

[ 49](gd32vf103-clocks_8h.md#a149bc461b6b4f81cafe38f9c7f40c8cd)#define GD32\_CLOCK\_UART3 GD32\_CLOCK\_CONFIG(APB1EN, 19U)

[ 50](gd32vf103-clocks_8h.md#a82468e78744e139664daeb68f8f181da)#define GD32\_CLOCK\_UART4 GD32\_CLOCK\_CONFIG(APB1EN, 20U)

[ 51](gd32vf103-clocks_8h.md#a7aa5531ee97403c9ab9152c3fa9e4b47)#define GD32\_CLOCK\_I2C0 GD32\_CLOCK\_CONFIG(APB1EN, 21U)

[ 52](gd32vf103-clocks_8h.md#a15d339475004b458aa5aa4a4a0692355)#define GD32\_CLOCK\_I2C1 GD32\_CLOCK\_CONFIG(APB1EN, 22U)

[ 53](gd32vf103-clocks_8h.md#a567dfd2f603a04594ab82aeac7339655)#define GD32\_CLOCK\_CAN0 GD32\_CLOCK\_CONFIG(APB1EN, 25U)

[ 54](gd32vf103-clocks_8h.md#a73858e2f6a1654e6114790c9dea80cd0)#define GD32\_CLOCK\_CAN1 GD32\_CLOCK\_CONFIG(APB1EN, 26U)

[ 55](gd32vf103-clocks_8h.md#afc77331b3e1cf36be2e04366ea15ff52)#define GD32\_CLOCK\_BKPI GD32\_CLOCK\_CONFIG(APB1EN, 27U)

[ 56](gd32vf103-clocks_8h.md#a58267ff23e872483b53ff7e6bb64d69f)#define GD32\_CLOCK\_PMU GD32\_CLOCK\_CONFIG(APB1EN, 28U)

[ 57](gd32vf103-clocks_8h.md#aaef5ffeb0d314adf6faf2a9d8158763b)#define GD32\_CLOCK\_DAC GD32\_CLOCK\_CONFIG(APB1EN, 29U)

58

59/\* APB2 peripherals \*/

[ 60](gd32vf103-clocks_8h.md#a084da3f645ceb69f3b454cd089c0a6fc)#define GD32\_CLOCK\_AFIO GD32\_CLOCK\_CONFIG(APB2EN, 0U)

[ 61](gd32vf103-clocks_8h.md#a6d7de29e854deaa62412e302566efd23)#define GD32\_CLOCK\_GPIOA GD32\_CLOCK\_CONFIG(APB2EN, 2U)

[ 62](gd32vf103-clocks_8h.md#a4272044e59f7e6935b5fc231d7da4a3e)#define GD32\_CLOCK\_GPIOB GD32\_CLOCK\_CONFIG(APB2EN, 3U)

[ 63](gd32vf103-clocks_8h.md#a8a415ead74c233d769ac7649bbc678ee)#define GD32\_CLOCK\_GPIOC GD32\_CLOCK\_CONFIG(APB2EN, 4U)

[ 64](gd32vf103-clocks_8h.md#a6e674cc73448d4c7487fb05a9368a5b0)#define GD32\_CLOCK\_GPIOD GD32\_CLOCK\_CONFIG(APB2EN, 5U)

[ 65](gd32vf103-clocks_8h.md#a77e5bd38cfd6018f8a5e518b388e764d)#define GD32\_CLOCK\_GPIOE GD32\_CLOCK\_CONFIG(APB2EN, 6U)

[ 66](gd32vf103-clocks_8h.md#a59b782811760bb907d00801305564c94)#define GD32\_CLOCK\_ADC0 GD32\_CLOCK\_CONFIG(APB2EN, 9U)

[ 67](gd32vf103-clocks_8h.md#a2ee53a1088b6dc17320d3d35ffdb1848)#define GD32\_CLOCK\_ADC1 GD32\_CLOCK\_CONFIG(APB2EN, 10U)

[ 68](gd32vf103-clocks_8h.md#afa309eb7291fd4416d3a5d0184991212)#define GD32\_CLOCK\_TIMER0 GD32\_CLOCK\_CONFIG(APB2EN, 11U)

[ 69](gd32vf103-clocks_8h.md#aa1284de659aca3a7b279c4f691147fb7)#define GD32\_CLOCK\_SPI0 GD32\_CLOCK\_CONFIG(APB2EN, 12U)

[ 70](gd32vf103-clocks_8h.md#ac1599e50ad14746470268bc14aa04318)#define GD32\_CLOCK\_USART0 GD32\_CLOCK\_CONFIG(APB2EN, 14U)

71

73

74#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32VF103\_CLOCKS\_H\_ \*/

[gd32-clocks-common.h](gd32-clocks-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32vf103-clocks.h](gd32vf103-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
