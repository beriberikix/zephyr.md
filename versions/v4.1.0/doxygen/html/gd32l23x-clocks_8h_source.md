---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32l23x-clocks_8h_source.html
original_path: doxygen/html/gd32l23x-clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32l23x-clocks.h

[Go to the documentation of this file.](gd32l23x-clocks_8h.md)

1/\*

2 \* Copyright (c) 2022 BrainCo.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32L23X\_CLOCKS\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32L23X\_CLOCKS\_H\_

9

10#include "[gd32-clocks-common.h](gd32-clocks-common_8h.md)"

11

16

[ 17](gd32l23x-clocks_8h.md#a339c9d51e00c124e8c3fcb3f60d4ab11)#define GD32\_AHB1EN\_OFFSET 0x14U

[ 18](gd32l23x-clocks_8h.md#a4b2aa082b4b2200b7f2b1663c30f205c)#define GD32\_APB1EN\_OFFSET 0x1CU

[ 19](gd32l23x-clocks_8h.md#a9d794746eea796b39b3ae55b1614d9d9)#define GD32\_APB2EN\_OFFSET 0x18U

20

22

27

28/\* AHB1 peripherals \*/

[ 29](gd32l23x-clocks_8h.md#aa4a3b682dbd3877c0e505f89ce572729)#define GD32\_CLOCK\_DMA GD32\_CLOCK\_CONFIG(AHB1EN, 0U)

[ 30](gd32l23x-clocks_8h.md#aa492c4ed7ca62ad488bd34a9c39f7ee7)#define GD32\_CLOCK\_SRAM0 GD32\_CLOCK\_CONFIG(AHB1EN, 2U)

[ 31](gd32l23x-clocks_8h.md#a695eb7a95fa6b5d57b763629757bf1b1)#define GD32\_CLOCK\_FMC GD32\_CLOCK\_CONFIG(AHB1EN, 4U)

[ 32](gd32l23x-clocks_8h.md#a0971986459094517a13221629cc89e95)#define GD32\_CLOCK\_CRC GD32\_CLOCK\_CONFIG(AHB1EN, 6U)

[ 33](gd32l23x-clocks_8h.md#aa72ff0249d857ac302e3b247cc08d8c8)#define GD32\_CLOCK\_SRAM1 GD32\_CLOCK\_CONFIG(AHB1EN, 7U)

[ 34](gd32l23x-clocks_8h.md#a6d7de29e854deaa62412e302566efd23)#define GD32\_CLOCK\_GPIOA GD32\_CLOCK\_CONFIG(AHB1EN, 17U)

[ 35](gd32l23x-clocks_8h.md#a4272044e59f7e6935b5fc231d7da4a3e)#define GD32\_CLOCK\_GPIOB GD32\_CLOCK\_CONFIG(AHB1EN, 18U)

[ 36](gd32l23x-clocks_8h.md#a8a415ead74c233d769ac7649bbc678ee)#define GD32\_CLOCK\_GPIOC GD32\_CLOCK\_CONFIG(AHB1EN, 19U)

[ 37](gd32l23x-clocks_8h.md#a6e674cc73448d4c7487fb05a9368a5b0)#define GD32\_CLOCK\_GPIOD GD32\_CLOCK\_CONFIG(AHB1EN, 20U)

[ 38](gd32l23x-clocks_8h.md#a8eaec3ec9ef667aaad9553f9a24fbbfe)#define GD32\_CLOCK\_GPIOF GD32\_CLOCK\_CONFIG(AHB1EN, 22U)

39

40/\* AHB2 peripherals \*/

[ 41](gd32l23x-clocks_8h.md#a0654988b7208162ddcdf649167734784)#define GD32\_CLOCK\_CAU GD32\_CLOCK\_CONFIG(AHB2EN, 1U)

[ 42](gd32l23x-clocks_8h.md#ad7e9e9d34e7acca03e2538e1d5f52c0e)#define GD32\_CLOCK\_TRNG GD32\_CLOCK\_CONFIG(AHB2EN, 3U)

43

44/\* APB1 peripherals \*/

[ 45](gd32l23x-clocks_8h.md#af084c2bf11ddfe04c80c3fac272c30e7)#define GD32\_CLOCK\_TIMER1 GD32\_CLOCK\_CONFIG(APB1EN, 0U)

[ 46](gd32l23x-clocks_8h.md#a41623cb4499589163c0697a7a669ac25)#define GD32\_CLOCK\_TIMER2 GD32\_CLOCK\_CONFIG(APB1EN, 1U)

[ 47](gd32l23x-clocks_8h.md#aae8d2c65bc590e7147407099e8a938b7)#define GD32\_CLOCK\_TIMER5 GD32\_CLOCK\_CONFIG(APB1EN, 4U)

[ 48](gd32l23x-clocks_8h.md#a0e1b450d86f9e5b08a5738116742b429)#define GD32\_CLOCK\_TIMER6 GD32\_CLOCK\_CONFIG(APB1EN, 5U)

[ 49](gd32l23x-clocks_8h.md#afffce8951164061ccedc46edad527cf8)#define GD32\_CLOCK\_TIMER11 GD32\_CLOCK\_CONFIG(APB1EN, 8U)

[ 50](gd32l23x-clocks_8h.md#af2dcccd27d498112f102c9148abb42f7)#define GD32\_CLOCK\_LPTIMER GD32\_CLOCK\_CONFIG(APB1EN, 9U)

[ 51](gd32l23x-clocks_8h.md#ae41c4f96dae0097b82ff22932f90aefe)#define GD32\_CLOCK\_SLCD GD32\_CLOCK\_CONFIG(APB1EN, 10U)

[ 52](gd32l23x-clocks_8h.md#acd4e6949e5fb08e13129174ddd6f2e70)#define GD32\_CLOCK\_WWDGT GD32\_CLOCK\_CONFIG(APB1EN, 11U)

[ 53](gd32l23x-clocks_8h.md#a61a4d4edd729635d5fcdd200a13a0b9b)#define GD32\_CLOCK\_SPI1 GD32\_CLOCK\_CONFIG(APB1EN, 14U)

[ 54](gd32l23x-clocks_8h.md#a0f4528cfba6c9b129cc3aeae8220a178)#define GD32\_CLOCK\_USART1 GD32\_CLOCK\_CONFIG(APB1EN, 17U)

[ 55](gd32l23x-clocks_8h.md#a6bc2e3226c496d0c1f754dac515fe568)#define GD32\_CLOCK\_LPUART GD32\_CLOCK\_CONFIG(APB1EN, 18U)

[ 56](gd32l23x-clocks_8h.md#a149bc461b6b4f81cafe38f9c7f40c8cd)#define GD32\_CLOCK\_UART3 GD32\_CLOCK\_CONFIG(APB1EN, 19U)

[ 57](gd32l23x-clocks_8h.md#a82468e78744e139664daeb68f8f181da)#define GD32\_CLOCK\_UART4 GD32\_CLOCK\_CONFIG(APB1EN, 20U)

[ 58](gd32l23x-clocks_8h.md#a7aa5531ee97403c9ab9152c3fa9e4b47)#define GD32\_CLOCK\_I2C0 GD32\_CLOCK\_CONFIG(APB1EN, 21U)

[ 59](gd32l23x-clocks_8h.md#a15d339475004b458aa5aa4a4a0692355)#define GD32\_CLOCK\_I2C1 GD32\_CLOCK\_CONFIG(APB1EN, 22U)

[ 60](gd32l23x-clocks_8h.md#a0e6ade78ea2b16517f960f4dd9de12f3)#define GD32\_CLOCK\_USBD GD32\_CLOCK\_CONFIG(APB1EN, 23U)

[ 61](gd32l23x-clocks_8h.md#a9e36e327a61c6867c787d6648b8ec2ac)#define GD32\_CLOCK\_I2C2 GD32\_CLOCK\_CONFIG(APB1EN, 24U)

[ 62](gd32l23x-clocks_8h.md#a58267ff23e872483b53ff7e6bb64d69f)#define GD32\_CLOCK\_PMU GD32\_CLOCK\_CONFIG(APB1EN, 28U)

[ 63](gd32l23x-clocks_8h.md#aaef5ffeb0d314adf6faf2a9d8158763b)#define GD32\_CLOCK\_DAC GD32\_CLOCK\_CONFIG(APB1EN, 29U)

[ 64](gd32l23x-clocks_8h.md#a886d3e4e09c70277b45f6afd5ae77eae)#define GD32\_CLOCK\_CTC GD32\_CLOCK\_CONFIG(APB1EN, 30U)

[ 65](gd32l23x-clocks_8h.md#a45f1e755993e4ccdda57966c147309dc)#define GD32\_CLOCK\_BKP GD32\_CLOCK\_CONFIG(APB1EN, 31U)

66

67/\* APB2 peripherals \*/

[ 68](gd32l23x-clocks_8h.md#a82d39e45cb7402ed96ab29953f8e131f)#define GD32\_CLOCK\_SYSCFG GD32\_CLOCK\_CONFIG(APB2EN, 0U)

[ 69](gd32l23x-clocks_8h.md#a86ba69950ab9daffa9c98d898a8b1186)#define GD32\_CLOCK\_CMP GD32\_CLOCK\_CONFIG(APB2EN, 1U)

[ 70](gd32l23x-clocks_8h.md#a49fb3dfb6cb0c66ed5ee81185896f2ab)#define GD32\_CLOCK\_ADC GD32\_CLOCK\_CONFIG(APB2EN, 9U)

[ 71](gd32l23x-clocks_8h.md#adbac39fc1c001fbb14036f08c81810ef)#define GD32\_CLOCK\_TIMER8 GD32\_CLOCK\_CONFIG(APB2EN, 11U)

[ 72](gd32l23x-clocks_8h.md#aa1284de659aca3a7b279c4f691147fb7)#define GD32\_CLOCK\_SPI0 GD32\_CLOCK\_CONFIG(APB2EN, 12U)

[ 73](gd32l23x-clocks_8h.md#ac1599e50ad14746470268bc14aa04318)#define GD32\_CLOCK\_USART0 GD32\_CLOCK\_CONFIG(APB2EN, 14U)

[ 74](gd32l23x-clocks_8h.md#a8d82d9131757c46462c8d983a919b94b)#define GD32\_CLOCK\_DBGMCU GD32\_CLOCK\_CONFIG(APB2EN, 22U)

75

77

78#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F4XX\_CLOCKS\_H\_ \*/

[gd32-clocks-common.h](gd32-clocks-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32l23x-clocks.h](gd32l23x-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
