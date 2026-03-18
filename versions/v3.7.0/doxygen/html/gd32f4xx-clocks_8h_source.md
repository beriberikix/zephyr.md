---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gd32f4xx-clocks_8h_source.html
original_path: doxygen/html/gd32f4xx-clocks_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f4xx-clocks.h

[Go to the documentation of this file.](gd32f4xx-clocks_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F4XX\_CLOCKS\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F4XX\_CLOCKS\_H\_

9

10#include "[gd32-clocks-common.h](gd32-clocks-common_8h.md)"

11

16

[ 17](gd32f4xx-clocks_8h.md#a339c9d51e00c124e8c3fcb3f60d4ab11)#define GD32\_AHB1EN\_OFFSET 0x30U

[ 18](gd32f4xx-clocks_8h.md#a6e31d435e5f43b51f733ff72654e3028)#define GD32\_AHB2EN\_OFFSET 0x34U

[ 19](gd32f4xx-clocks_8h.md#a124c1f305697766c2e616b4102469a08)#define GD32\_AHB3EN\_OFFSET 0x38U

[ 20](gd32f4xx-clocks_8h.md#a4b2aa082b4b2200b7f2b1663c30f205c)#define GD32\_APB1EN\_OFFSET 0x40U

[ 21](gd32f4xx-clocks_8h.md#a9d794746eea796b39b3ae55b1614d9d9)#define GD32\_APB2EN\_OFFSET 0x44U

[ 22](gd32f4xx-clocks_8h.md#a4202c14a67ad78724b05175ede3aaa99)#define GD32\_ADDAPB1EN\_OFFSET 0xE4U

23

25

30

31/\* AHB1 peripherals \*/

[ 32](gd32f4xx-clocks_8h.md#a6d7de29e854deaa62412e302566efd23)#define GD32\_CLOCK\_GPIOA GD32\_CLOCK\_CONFIG(AHB1EN, 0U)

[ 33](gd32f4xx-clocks_8h.md#a4272044e59f7e6935b5fc231d7da4a3e)#define GD32\_CLOCK\_GPIOB GD32\_CLOCK\_CONFIG(AHB1EN, 1U)

[ 34](gd32f4xx-clocks_8h.md#a8a415ead74c233d769ac7649bbc678ee)#define GD32\_CLOCK\_GPIOC GD32\_CLOCK\_CONFIG(AHB1EN, 2U)

[ 35](gd32f4xx-clocks_8h.md#a6e674cc73448d4c7487fb05a9368a5b0)#define GD32\_CLOCK\_GPIOD GD32\_CLOCK\_CONFIG(AHB1EN, 3U)

[ 36](gd32f4xx-clocks_8h.md#a77e5bd38cfd6018f8a5e518b388e764d)#define GD32\_CLOCK\_GPIOE GD32\_CLOCK\_CONFIG(AHB1EN, 4U)

[ 37](gd32f4xx-clocks_8h.md#a8eaec3ec9ef667aaad9553f9a24fbbfe)#define GD32\_CLOCK\_GPIOF GD32\_CLOCK\_CONFIG(AHB1EN, 5U)

[ 38](gd32f4xx-clocks_8h.md#a2f91cac90de074a5478c73392c107027)#define GD32\_CLOCK\_GPIOG GD32\_CLOCK\_CONFIG(AHB1EN, 6U)

[ 39](gd32f4xx-clocks_8h.md#aa61dad33dbaa553cdaff7c5e6d674758)#define GD32\_CLOCK\_GPIOH GD32\_CLOCK\_CONFIG(AHB1EN, 7U)

[ 40](gd32f4xx-clocks_8h.md#ac48646b69241ec518c12f5c92c982a4e)#define GD32\_CLOCK\_GPIOI GD32\_CLOCK\_CONFIG(AHB1EN, 8U)

[ 41](gd32f4xx-clocks_8h.md#a0971986459094517a13221629cc89e95)#define GD32\_CLOCK\_CRC GD32\_CLOCK\_CONFIG(AHB1EN, 12U)

[ 42](gd32f4xx-clocks_8h.md#a07ab9ef3cb3d81f90c7363712725b55a)#define GD32\_CLOCK\_BKPSRAM GD32\_CLOCK\_CONFIG(AHB1EN, 18U)

[ 43](gd32f4xx-clocks_8h.md#a035e6888de8ffcd4793928015996cebf)#define GD32\_CLOCK\_TCMSRAM GD32\_CLOCK\_CONFIG(AHB1EN, 20U)

[ 44](gd32f4xx-clocks_8h.md#a7728f090fb52201d3d1162881b80dc3e)#define GD32\_CLOCK\_DMA0 GD32\_CLOCK\_CONFIG(AHB1EN, 21U)

[ 45](gd32f4xx-clocks_8h.md#af6c6eb89797f088a78722ce007ae47e5)#define GD32\_CLOCK\_DMA1 GD32\_CLOCK\_CONFIG(AHB1EN, 22U)

[ 46](gd32f4xx-clocks_8h.md#ad37a43a7c3bafef7f5af454d9311607e)#define GD32\_CLOCK\_IPA GD32\_CLOCK\_CONFIG(AHB1EN, 23U)

[ 47](gd32f4xx-clocks_8h.md#a824f638811c4469fedc65a1e29aac8d0)#define GD32\_CLOCK\_ENET GD32\_CLOCK\_CONFIG(AHB1EN, 25U)

[ 48](gd32f4xx-clocks_8h.md#a6b14717b0c1cf864f1fe63b8ca42a439)#define GD32\_CLOCK\_ENETTX GD32\_CLOCK\_CONFIG(AHB1EN, 26U)

[ 49](gd32f4xx-clocks_8h.md#a05dce9f9343146d02a71a50b1f9416f7)#define GD32\_CLOCK\_ENETRX GD32\_CLOCK\_CONFIG(AHB1EN, 27U)

[ 50](gd32f4xx-clocks_8h.md#afb7f99d35b7c726a99a7da0d1288697c)#define GD32\_CLOCK\_ENETPTP GD32\_CLOCK\_CONFIG(AHB1EN, 28U)

[ 51](gd32f4xx-clocks_8h.md#a9bb9a4af2877fa954bda83bb8fbc39a6)#define GD32\_CLOCK\_USBHS GD32\_CLOCK\_CONFIG(AHB1EN, 29U)

[ 52](gd32f4xx-clocks_8h.md#a921ac30c07db5ab957c001cc0cbbdd0d)#define GD32\_CLOCK\_USBHSULPI GD32\_CLOCK\_CONFIG(AHB1EN, 30U)

53

54/\* AHB2 peripherals \*/

[ 55](gd32f4xx-clocks_8h.md#a992085b45325f4ece017ca26d754b217)#define GD32\_CLOCK\_DCI GD32\_CLOCK\_CONFIG(AHB2EN, 0U)

[ 56](gd32f4xx-clocks_8h.md#ad7e9e9d34e7acca03e2538e1d5f52c0e)#define GD32\_CLOCK\_TRNG GD32\_CLOCK\_CONFIG(AHB2EN, 6U)

[ 57](gd32f4xx-clocks_8h.md#ae11c1f5ccf256d32377eb9a6f07026f2)#define GD32\_CLOCK\_USBFS GD32\_CLOCK\_CONFIG(AHB2EN, 7U)

58

59/\* AHB3 peripherals \*/

[ 60](gd32f4xx-clocks_8h.md#af4ca0b77d98d8825493b868d19d7759a)#define GD32\_CLOCK\_EXMC GD32\_CLOCK\_CONFIG(AHB3EN, 0U)

61

62/\* APB1 peripherals \*/

[ 63](gd32f4xx-clocks_8h.md#af084c2bf11ddfe04c80c3fac272c30e7)#define GD32\_CLOCK\_TIMER1 GD32\_CLOCK\_CONFIG(APB1EN, 0U)

[ 64](gd32f4xx-clocks_8h.md#a41623cb4499589163c0697a7a669ac25)#define GD32\_CLOCK\_TIMER2 GD32\_CLOCK\_CONFIG(APB1EN, 1U)

[ 65](gd32f4xx-clocks_8h.md#afb5aa7f1705febd51a92f9370bd03d14)#define GD32\_CLOCK\_TIMER3 GD32\_CLOCK\_CONFIG(APB1EN, 2U)

[ 66](gd32f4xx-clocks_8h.md#a9d52a01572ab9309c5ebd3a0def8542f)#define GD32\_CLOCK\_TIMER4 GD32\_CLOCK\_CONFIG(APB1EN, 3U)

[ 67](gd32f4xx-clocks_8h.md#aae8d2c65bc590e7147407099e8a938b7)#define GD32\_CLOCK\_TIMER5 GD32\_CLOCK\_CONFIG(APB1EN, 4U)

[ 68](gd32f4xx-clocks_8h.md#a0e1b450d86f9e5b08a5738116742b429)#define GD32\_CLOCK\_TIMER6 GD32\_CLOCK\_CONFIG(APB1EN, 5U)

[ 69](gd32f4xx-clocks_8h.md#afffce8951164061ccedc46edad527cf8)#define GD32\_CLOCK\_TIMER11 GD32\_CLOCK\_CONFIG(APB1EN, 6U)

[ 70](gd32f4xx-clocks_8h.md#a285a372dc49a8df0888813b08c8804ef)#define GD32\_CLOCK\_TIMER12 GD32\_CLOCK\_CONFIG(APB1EN, 7U)

[ 71](gd32f4xx-clocks_8h.md#a60bfa7bc6aafc012fa45b395d4d22c00)#define GD32\_CLOCK\_TIMER13 GD32\_CLOCK\_CONFIG(APB1EN, 8U)

[ 72](gd32f4xx-clocks_8h.md#acd4e6949e5fb08e13129174ddd6f2e70)#define GD32\_CLOCK\_WWDGT GD32\_CLOCK\_CONFIG(APB1EN, 11U)

[ 73](gd32f4xx-clocks_8h.md#a61a4d4edd729635d5fcdd200a13a0b9b)#define GD32\_CLOCK\_SPI1 GD32\_CLOCK\_CONFIG(APB1EN, 14U)

[ 74](gd32f4xx-clocks_8h.md#a4bb28caf86a54e343c75a597b0bddc20)#define GD32\_CLOCK\_SPI2 GD32\_CLOCK\_CONFIG(APB1EN, 15U)

[ 75](gd32f4xx-clocks_8h.md#a0f4528cfba6c9b129cc3aeae8220a178)#define GD32\_CLOCK\_USART1 GD32\_CLOCK\_CONFIG(APB1EN, 17U)

[ 76](gd32f4xx-clocks_8h.md#a477baf1c1a265b4c86019a5f52820622)#define GD32\_CLOCK\_USART2 GD32\_CLOCK\_CONFIG(APB1EN, 18U)

[ 77](gd32f4xx-clocks_8h.md#a149bc461b6b4f81cafe38f9c7f40c8cd)#define GD32\_CLOCK\_UART3 GD32\_CLOCK\_CONFIG(APB1EN, 19U)

[ 78](gd32f4xx-clocks_8h.md#a82468e78744e139664daeb68f8f181da)#define GD32\_CLOCK\_UART4 GD32\_CLOCK\_CONFIG(APB1EN, 20U)

[ 79](gd32f4xx-clocks_8h.md#a7aa5531ee97403c9ab9152c3fa9e4b47)#define GD32\_CLOCK\_I2C0 GD32\_CLOCK\_CONFIG(APB1EN, 21U)

[ 80](gd32f4xx-clocks_8h.md#a15d339475004b458aa5aa4a4a0692355)#define GD32\_CLOCK\_I2C1 GD32\_CLOCK\_CONFIG(APB1EN, 22U)

[ 81](gd32f4xx-clocks_8h.md#a9e36e327a61c6867c787d6648b8ec2ac)#define GD32\_CLOCK\_I2C2 GD32\_CLOCK\_CONFIG(APB1EN, 23U)

[ 82](gd32f4xx-clocks_8h.md#a567dfd2f603a04594ab82aeac7339655)#define GD32\_CLOCK\_CAN0 GD32\_CLOCK\_CONFIG(APB1EN, 25U)

[ 83](gd32f4xx-clocks_8h.md#a73858e2f6a1654e6114790c9dea80cd0)#define GD32\_CLOCK\_CAN1 GD32\_CLOCK\_CONFIG(APB1EN, 26U)

[ 84](gd32f4xx-clocks_8h.md#a58267ff23e872483b53ff7e6bb64d69f)#define GD32\_CLOCK\_PMU GD32\_CLOCK\_CONFIG(APB1EN, 28U)

[ 85](gd32f4xx-clocks_8h.md#aaef5ffeb0d314adf6faf2a9d8158763b)#define GD32\_CLOCK\_DAC GD32\_CLOCK\_CONFIG(APB1EN, 29U)

[ 86](gd32f4xx-clocks_8h.md#a8ec6e1dfab01b3652183c38eac160288)#define GD32\_CLOCK\_UART6 GD32\_CLOCK\_CONFIG(APB1EN, 30U)

[ 87](gd32f4xx-clocks_8h.md#a683cb88b874a2b6802bba5f99b85163e)#define GD32\_CLOCK\_UART7 GD32\_CLOCK\_CONFIG(APB1EN, 31U)

[ 88](gd32f4xx-clocks_8h.md#a1f8cfe3ba991c9773b21c1e417bd3421)#define GD32\_CLOCK\_RTC GD32\_CLOCK\_CONFIG(BDCTL, 15U)

89

90/\* APB2 peripherals \*/

[ 91](gd32f4xx-clocks_8h.md#afa309eb7291fd4416d3a5d0184991212)#define GD32\_CLOCK\_TIMER0 GD32\_CLOCK\_CONFIG(APB2EN, 0U)

[ 92](gd32f4xx-clocks_8h.md#abb3f432fa2ef4e6c69a4c252493c0606)#define GD32\_CLOCK\_TIMER7 GD32\_CLOCK\_CONFIG(APB2EN, 1U)

[ 93](gd32f4xx-clocks_8h.md#ac1599e50ad14746470268bc14aa04318)#define GD32\_CLOCK\_USART0 GD32\_CLOCK\_CONFIG(APB2EN, 4U)

[ 94](gd32f4xx-clocks_8h.md#a736a4d8ae51d88226f8baeec49be4dc5)#define GD32\_CLOCK\_USART5 GD32\_CLOCK\_CONFIG(APB2EN, 5U)

[ 95](gd32f4xx-clocks_8h.md#a59b782811760bb907d00801305564c94)#define GD32\_CLOCK\_ADC0 GD32\_CLOCK\_CONFIG(APB2EN, 8U)

[ 96](gd32f4xx-clocks_8h.md#a2ee53a1088b6dc17320d3d35ffdb1848)#define GD32\_CLOCK\_ADC1 GD32\_CLOCK\_CONFIG(APB2EN, 9U)

[ 97](gd32f4xx-clocks_8h.md#a5710e96c011ed3c8dc90f63b842751cc)#define GD32\_CLOCK\_ADC2 GD32\_CLOCK\_CONFIG(APB2EN, 10U)

[ 98](gd32f4xx-clocks_8h.md#ad1ba647a10df2ea0bd81676cb5f46064)#define GD32\_CLOCK\_SDIO GD32\_CLOCK\_CONFIG(APB2EN, 11U)

[ 99](gd32f4xx-clocks_8h.md#aa1284de659aca3a7b279c4f691147fb7)#define GD32\_CLOCK\_SPI0 GD32\_CLOCK\_CONFIG(APB2EN, 12U)

[ 100](gd32f4xx-clocks_8h.md#adc1fc8ab68a58bc412e4560cdd56c25e)#define GD32\_CLOCK\_SPI3 GD32\_CLOCK\_CONFIG(APB2EN, 13U)

[ 101](gd32f4xx-clocks_8h.md#a82d39e45cb7402ed96ab29953f8e131f)#define GD32\_CLOCK\_SYSCFG GD32\_CLOCK\_CONFIG(APB2EN, 14U)

[ 102](gd32f4xx-clocks_8h.md#adbac39fc1c001fbb14036f08c81810ef)#define GD32\_CLOCK\_TIMER8 GD32\_CLOCK\_CONFIG(APB2EN, 16U)

[ 103](gd32f4xx-clocks_8h.md#a3981da513ef2eb351b403f6dc11a2c6b)#define GD32\_CLOCK\_TIMER9 GD32\_CLOCK\_CONFIG(APB2EN, 17U)

[ 104](gd32f4xx-clocks_8h.md#a7c3b4d23aac8844faac79f458cc5e07b)#define GD32\_CLOCK\_TIMER10 GD32\_CLOCK\_CONFIG(APB2EN, 18U)

[ 105](gd32f4xx-clocks_8h.md#a0fa21a935cec395aab91ba0394572d2c)#define GD32\_CLOCK\_SPI4 GD32\_CLOCK\_CONFIG(APB2EN, 20U)

[ 106](gd32f4xx-clocks_8h.md#adfe3187c5b24e430f5071e1855a51108)#define GD32\_CLOCK\_SPI5 GD32\_CLOCK\_CONFIG(APB2EN, 21U)

[ 107](gd32f4xx-clocks_8h.md#ab04cbf84abb9f4923b6e9381c22bdae1)#define GD32\_CLOCK\_TLI GD32\_CLOCK\_CONFIG(APB2EN, 26U)

108

109/\* APB1 additional peripherals \*/

[ 110](gd32f4xx-clocks_8h.md#a886d3e4e09c70277b45f6afd5ae77eae)#define GD32\_CLOCK\_CTC GD32\_CLOCK\_CONFIG(ADDAPB1EN, 27U)

[ 111](gd32f4xx-clocks_8h.md#ab2207ccb1c350c57aa19963285bf5470)#define GD32\_CLOCK\_IREF GD32\_CLOCK\_CONFIG(ADDAPB1EN, 31U)

112

114

115#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F4XX\_CLOCKS\_H\_ \*/

[gd32-clocks-common.h](gd32-clocks-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32f4xx-clocks.h](gd32f4xx-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
