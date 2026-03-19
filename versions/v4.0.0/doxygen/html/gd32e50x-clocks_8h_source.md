---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gd32e50x-clocks_8h_source.html
original_path: doxygen/html/gd32e50x-clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32e50x-clocks.h

[Go to the documentation of this file.](gd32e50x-clocks_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32E50X\_CLOCKS\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32E50X\_CLOCKS\_H\_

9

10#include "[gd32-clocks-common.h](gd32-clocks-common_8h.md)"

11

16

[ 17](gd32e50x-clocks_8h.md#a510e385774abf879310b061273eb4068)#define GD32\_AHBEN\_OFFSET 0x14U

[ 18](gd32e50x-clocks_8h.md#a4b2aa082b4b2200b7f2b1663c30f205c)#define GD32\_APB1EN\_OFFSET 0x1CU

[ 19](gd32e50x-clocks_8h.md#a9d794746eea796b39b3ae55b1614d9d9)#define GD32\_APB2EN\_OFFSET 0x18U

[ 20](gd32e50x-clocks_8h.md#a4202c14a67ad78724b05175ede3aaa99)#define GD32\_ADDAPB1EN\_OFFSET 0xE4U

21

23

28

29/\* AHB peripherals \*/

[ 30](gd32e50x-clocks_8h.md#a7728f090fb52201d3d1162881b80dc3e)#define GD32\_CLOCK\_DMA0 GD32\_CLOCK\_CONFIG(AHBEN, 0U)

[ 31](gd32e50x-clocks_8h.md#af6c6eb89797f088a78722ce007ae47e5)#define GD32\_CLOCK\_DMA1 GD32\_CLOCK\_CONFIG(AHBEN, 1U)

[ 32](gd32e50x-clocks_8h.md#a7f201b05f8c284e62be5bf9290a84a67)#define GD32\_CLOCK\_SRAMSP GD32\_CLOCK\_CONFIG(AHBEN, 2U)

[ 33](gd32e50x-clocks_8h.md#acdbf40a9d897a38daca0d8bd5f81fc1a)#define GD32\_CLOCK\_FMCSP GD32\_CLOCK\_CONFIG(AHBEN, 4U)

[ 34](gd32e50x-clocks_8h.md#a0971986459094517a13221629cc89e95)#define GD32\_CLOCK\_CRC GD32\_CLOCK\_CONFIG(AHBEN, 6U)

[ 35](gd32e50x-clocks_8h.md#af4ca0b77d98d8825493b868d19d7759a)#define GD32\_CLOCK\_EXMC GD32\_CLOCK\_CONFIG(AHBEN, 8U)

[ 36](gd32e50x-clocks_8h.md#a9bb9a4af2877fa954bda83bb8fbc39a6)#define GD32\_CLOCK\_USBHS GD32\_CLOCK\_CONFIG(AHBEN, 12U)

[ 37](gd32e50x-clocks_8h.md#a742d7e1f918e4c0d585fe2fcfc779507)#define GD32\_CLOCK\_ULPI GD32\_CLOCK\_CONFIG(AHBEN, 13U)

[ 38](gd32e50x-clocks_8h.md#a824f638811c4469fedc65a1e29aac8d0)#define GD32\_CLOCK\_ENET GD32\_CLOCK\_CONFIG(AHBEN, 14U)

[ 39](gd32e50x-clocks_8h.md#a6b14717b0c1cf864f1fe63b8ca42a439)#define GD32\_CLOCK\_ENETTX GD32\_CLOCK\_CONFIG(AHBEN, 15U)

[ 40](gd32e50x-clocks_8h.md#a05dce9f9343146d02a71a50b1f9416f7)#define GD32\_CLOCK\_ENETRX GD32\_CLOCK\_CONFIG(AHBEN, 16U)

[ 41](gd32e50x-clocks_8h.md#a07193a9076085c1afda13725e18f6fee)#define GD32\_CLOCK\_TMU GD32\_CLOCK\_CONFIG(AHBEN, 30U)

[ 42](gd32e50x-clocks_8h.md#a2b45bf6fa005602e21fb2baec1db3d68)#define GD32\_CLOCK\_SQPI GD32\_CLOCK\_CONFIG(AHBEN, 31U)

43

44/\* APB1 peripherals \*/

[ 45](gd32e50x-clocks_8h.md#af084c2bf11ddfe04c80c3fac272c30e7)#define GD32\_CLOCK\_TIMER1 GD32\_CLOCK\_CONFIG(APB1EN, 0U)

[ 46](gd32e50x-clocks_8h.md#a41623cb4499589163c0697a7a669ac25)#define GD32\_CLOCK\_TIMER2 GD32\_CLOCK\_CONFIG(APB1EN, 1U)

[ 47](gd32e50x-clocks_8h.md#afb5aa7f1705febd51a92f9370bd03d14)#define GD32\_CLOCK\_TIMER3 GD32\_CLOCK\_CONFIG(APB1EN, 2U)

[ 48](gd32e50x-clocks_8h.md#a9d52a01572ab9309c5ebd3a0def8542f)#define GD32\_CLOCK\_TIMER4 GD32\_CLOCK\_CONFIG(APB1EN, 3U)

[ 49](gd32e50x-clocks_8h.md#aae8d2c65bc590e7147407099e8a938b7)#define GD32\_CLOCK\_TIMER5 GD32\_CLOCK\_CONFIG(APB1EN, 4U)

[ 50](gd32e50x-clocks_8h.md#a0e1b450d86f9e5b08a5738116742b429)#define GD32\_CLOCK\_TIMER6 GD32\_CLOCK\_CONFIG(APB1EN, 5U)

[ 51](gd32e50x-clocks_8h.md#afffce8951164061ccedc46edad527cf8)#define GD32\_CLOCK\_TIMER11 GD32\_CLOCK\_CONFIG(APB1EN, 6U)

[ 52](gd32e50x-clocks_8h.md#a285a372dc49a8df0888813b08c8804ef)#define GD32\_CLOCK\_TIMER12 GD32\_CLOCK\_CONFIG(APB1EN, 7U)

[ 53](gd32e50x-clocks_8h.md#a60bfa7bc6aafc012fa45b395d4d22c00)#define GD32\_CLOCK\_TIMER13 GD32\_CLOCK\_CONFIG(APB1EN, 8U)

[ 54](gd32e50x-clocks_8h.md#acd4e6949e5fb08e13129174ddd6f2e70)#define GD32\_CLOCK\_WWDGT GD32\_CLOCK\_CONFIG(APB1EN, 11U)

[ 55](gd32e50x-clocks_8h.md#a61a4d4edd729635d5fcdd200a13a0b9b)#define GD32\_CLOCK\_SPI1 GD32\_CLOCK\_CONFIG(APB1EN, 14U)

[ 56](gd32e50x-clocks_8h.md#a4bb28caf86a54e343c75a597b0bddc20)#define GD32\_CLOCK\_SPI2 GD32\_CLOCK\_CONFIG(APB1EN, 15U)

[ 57](gd32e50x-clocks_8h.md#a0f4528cfba6c9b129cc3aeae8220a178)#define GD32\_CLOCK\_USART1 GD32\_CLOCK\_CONFIG(APB1EN, 17U)

[ 58](gd32e50x-clocks_8h.md#a477baf1c1a265b4c86019a5f52820622)#define GD32\_CLOCK\_USART2 GD32\_CLOCK\_CONFIG(APB1EN, 18U)

[ 59](gd32e50x-clocks_8h.md#a149bc461b6b4f81cafe38f9c7f40c8cd)#define GD32\_CLOCK\_UART3 GD32\_CLOCK\_CONFIG(APB1EN, 19U)

[ 60](gd32e50x-clocks_8h.md#a82468e78744e139664daeb68f8f181da)#define GD32\_CLOCK\_UART4 GD32\_CLOCK\_CONFIG(APB1EN, 20U)

[ 61](gd32e50x-clocks_8h.md#a7aa5531ee97403c9ab9152c3fa9e4b47)#define GD32\_CLOCK\_I2C0 GD32\_CLOCK\_CONFIG(APB1EN, 21U)

[ 62](gd32e50x-clocks_8h.md#a15d339475004b458aa5aa4a4a0692355)#define GD32\_CLOCK\_I2C1 GD32\_CLOCK\_CONFIG(APB1EN, 22U)

[ 63](gd32e50x-clocks_8h.md#a9e36e327a61c6867c787d6648b8ec2ac)#define GD32\_CLOCK\_I2C2 GD32\_CLOCK\_CONFIG(APB1EN, 24U)

[ 64](gd32e50x-clocks_8h.md#a567dfd2f603a04594ab82aeac7339655)#define GD32\_CLOCK\_CAN0 GD32\_CLOCK\_CONFIG(APB1EN, 25U)

[ 65](gd32e50x-clocks_8h.md#a73858e2f6a1654e6114790c9dea80cd0)#define GD32\_CLOCK\_CAN1 GD32\_CLOCK\_CONFIG(APB1EN, 26U)

[ 66](gd32e50x-clocks_8h.md#afc77331b3e1cf36be2e04366ea15ff52)#define GD32\_CLOCK\_BKPI GD32\_CLOCK\_CONFIG(APB1EN, 27U)

[ 67](gd32e50x-clocks_8h.md#a58267ff23e872483b53ff7e6bb64d69f)#define GD32\_CLOCK\_PMU GD32\_CLOCK\_CONFIG(APB1EN, 28U)

[ 68](gd32e50x-clocks_8h.md#aaef5ffeb0d314adf6faf2a9d8158763b)#define GD32\_CLOCK\_DAC GD32\_CLOCK\_CONFIG(APB1EN, 29U)

69

70/\* APB2 peripherals \*/

[ 71](gd32e50x-clocks_8h.md#a084da3f645ceb69f3b454cd089c0a6fc)#define GD32\_CLOCK\_AFIO GD32\_CLOCK\_CONFIG(APB2EN, 0U)

[ 72](gd32e50x-clocks_8h.md#a6d7de29e854deaa62412e302566efd23)#define GD32\_CLOCK\_GPIOA GD32\_CLOCK\_CONFIG(APB2EN, 2U)

[ 73](gd32e50x-clocks_8h.md#a4272044e59f7e6935b5fc231d7da4a3e)#define GD32\_CLOCK\_GPIOB GD32\_CLOCK\_CONFIG(APB2EN, 3U)

[ 74](gd32e50x-clocks_8h.md#a8a415ead74c233d769ac7649bbc678ee)#define GD32\_CLOCK\_GPIOC GD32\_CLOCK\_CONFIG(APB2EN, 4U)

[ 75](gd32e50x-clocks_8h.md#a6e674cc73448d4c7487fb05a9368a5b0)#define GD32\_CLOCK\_GPIOD GD32\_CLOCK\_CONFIG(APB2EN, 5U)

[ 76](gd32e50x-clocks_8h.md#a77e5bd38cfd6018f8a5e518b388e764d)#define GD32\_CLOCK\_GPIOE GD32\_CLOCK\_CONFIG(APB2EN, 6U)

[ 77](gd32e50x-clocks_8h.md#a8eaec3ec9ef667aaad9553f9a24fbbfe)#define GD32\_CLOCK\_GPIOF GD32\_CLOCK\_CONFIG(APB2EN, 7U)

[ 78](gd32e50x-clocks_8h.md#a2f91cac90de074a5478c73392c107027)#define GD32\_CLOCK\_GPIOG GD32\_CLOCK\_CONFIG(APB2EN, 8U)

[ 79](gd32e50x-clocks_8h.md#a59b782811760bb907d00801305564c94)#define GD32\_CLOCK\_ADC0 GD32\_CLOCK\_CONFIG(APB2EN, 9U)

[ 80](gd32e50x-clocks_8h.md#a2ee53a1088b6dc17320d3d35ffdb1848)#define GD32\_CLOCK\_ADC1 GD32\_CLOCK\_CONFIG(APB2EN, 10U)

[ 81](gd32e50x-clocks_8h.md#afa309eb7291fd4416d3a5d0184991212)#define GD32\_CLOCK\_TIMER0 GD32\_CLOCK\_CONFIG(APB2EN, 11U)

[ 82](gd32e50x-clocks_8h.md#aa1284de659aca3a7b279c4f691147fb7)#define GD32\_CLOCK\_SPI0 GD32\_CLOCK\_CONFIG(APB2EN, 12U)

[ 83](gd32e50x-clocks_8h.md#abb3f432fa2ef4e6c69a4c252493c0606)#define GD32\_CLOCK\_TIMER7 GD32\_CLOCK\_CONFIG(APB2EN, 13U)

[ 84](gd32e50x-clocks_8h.md#ac1599e50ad14746470268bc14aa04318)#define GD32\_CLOCK\_USART0 GD32\_CLOCK\_CONFIG(APB2EN, 14U)

[ 85](gd32e50x-clocks_8h.md#a5710e96c011ed3c8dc90f63b842751cc)#define GD32\_CLOCK\_ADC2 GD32\_CLOCK\_CONFIG(APB2EN, 15U)

[ 86](gd32e50x-clocks_8h.md#adbac39fc1c001fbb14036f08c81810ef)#define GD32\_CLOCK\_TIMER8 GD32\_CLOCK\_CONFIG(APB2EN, 19U)

[ 87](gd32e50x-clocks_8h.md#a3981da513ef2eb351b403f6dc11a2c6b)#define GD32\_CLOCK\_TIMER9 GD32\_CLOCK\_CONFIG(APB2EN, 20U)

[ 88](gd32e50x-clocks_8h.md#a7c3b4d23aac8844faac79f458cc5e07b)#define GD32\_CLOCK\_TIMER10 GD32\_CLOCK\_CONFIG(APB2EN, 21U)

[ 89](gd32e50x-clocks_8h.md#a736a4d8ae51d88226f8baeec49be4dc5)#define GD32\_CLOCK\_USART5 GD32\_CLOCK\_CONFIG(APB2EN, 28U)

[ 90](gd32e50x-clocks_8h.md#a9f0d13badbb24cd8941c1ec0eec2d1b9)#define GD32\_CLOCK\_SHRTIMER GD32\_CLOCK\_CONFIG(APB2EN, 29U)

[ 91](gd32e50x-clocks_8h.md#a86ba69950ab9daffa9c98d898a8b1186)#define GD32\_CLOCK\_CMP GD32\_CLOCK\_CONFIG(APB2EN, 31U)

92

93/\* APB1 additional peripherals \*/

[ 94](gd32e50x-clocks_8h.md#a886d3e4e09c70277b45f6afd5ae77eae)#define GD32\_CLOCK\_CTC GD32\_CLOCK\_CONFIG(ADDAPB1EN, 27U)

[ 95](gd32e50x-clocks_8h.md#a4e69feed6dc4b5bdec634f57c407a6f6)#define GD32\_CLOCK\_CAN2 GD32\_CLOCK\_CONFIG(ADDAPB1EN, 31U)

96

98

99#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32E50X\_CLOCKS\_H\_ \*/

[gd32-clocks-common.h](gd32-clocks-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32e50x-clocks.h](gd32e50x-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
