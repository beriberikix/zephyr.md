---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32f3x0-clocks_8h_source.html
original_path: doxygen/html/gd32f3x0-clocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f3x0-clocks.h

[Go to the documentation of this file.](gd32f3x0-clocks_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F3X0\_CLOCKS\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F3X0\_CLOCKS\_H\_

9

10#include "[gd32-clocks-common.h](gd32-clocks-common_8h.md)"

11

16

[ 17](gd32f3x0-clocks_8h.md#a510e385774abf879310b061273eb4068)#define GD32\_AHBEN\_OFFSET 0x14U

[ 18](gd32f3x0-clocks_8h.md#a4b2aa082b4b2200b7f2b1663c30f205c)#define GD32\_APB1EN\_OFFSET 0x1CU

[ 19](gd32f3x0-clocks_8h.md#a9d794746eea796b39b3ae55b1614d9d9)#define GD32\_APB2EN\_OFFSET 0x18U

[ 20](gd32f3x0-clocks_8h.md#a4202c14a67ad78724b05175ede3aaa99)#define GD32\_ADDAPB1EN\_OFFSET 0xF8U

21

23

28

29/\* AHB peripherals \*/

[ 30](gd32f3x0-clocks_8h.md#aa4a3b682dbd3877c0e505f89ce572729)#define GD32\_CLOCK\_DMA GD32\_CLOCK\_CONFIG(AHBEN, 0U)

[ 31](gd32f3x0-clocks_8h.md#a7f201b05f8c284e62be5bf9290a84a67)#define GD32\_CLOCK\_SRAMSP GD32\_CLOCK\_CONFIG(AHBEN, 2U)

[ 32](gd32f3x0-clocks_8h.md#acdbf40a9d897a38daca0d8bd5f81fc1a)#define GD32\_CLOCK\_FMCSP GD32\_CLOCK\_CONFIG(AHBEN, 4U)

[ 33](gd32f3x0-clocks_8h.md#a0971986459094517a13221629cc89e95)#define GD32\_CLOCK\_CRC GD32\_CLOCK\_CONFIG(AHBEN, 6U)

[ 34](gd32f3x0-clocks_8h.md#ae11c1f5ccf256d32377eb9a6f07026f2)#define GD32\_CLOCK\_USBFS GD32\_CLOCK\_CONFIG(AHBEN, 12U)

[ 35](gd32f3x0-clocks_8h.md#a6d7de29e854deaa62412e302566efd23)#define GD32\_CLOCK\_GPIOA GD32\_CLOCK\_CONFIG(AHBEN, 17U)

[ 36](gd32f3x0-clocks_8h.md#a4272044e59f7e6935b5fc231d7da4a3e)#define GD32\_CLOCK\_GPIOB GD32\_CLOCK\_CONFIG(AHBEN, 18U)

[ 37](gd32f3x0-clocks_8h.md#a8a415ead74c233d769ac7649bbc678ee)#define GD32\_CLOCK\_GPIOC GD32\_CLOCK\_CONFIG(AHBEN, 19U)

[ 38](gd32f3x0-clocks_8h.md#a6e674cc73448d4c7487fb05a9368a5b0)#define GD32\_CLOCK\_GPIOD GD32\_CLOCK\_CONFIG(AHBEN, 20U)

[ 39](gd32f3x0-clocks_8h.md#a8eaec3ec9ef667aaad9553f9a24fbbfe)#define GD32\_CLOCK\_GPIOF GD32\_CLOCK\_CONFIG(AHBEN, 22U)

[ 40](gd32f3x0-clocks_8h.md#a2d044ca898ee3b1909c1de4411c139c2)#define GD32\_CLOCK\_TSI GD32\_CLOCK\_CONFIG(AHBEN, 24U)

41

42/\* APB1 peripherals \*/

[ 43](gd32f3x0-clocks_8h.md#af084c2bf11ddfe04c80c3fac272c30e7)#define GD32\_CLOCK\_TIMER1 GD32\_CLOCK\_CONFIG(APB1EN, 0U)

[ 44](gd32f3x0-clocks_8h.md#a41623cb4499589163c0697a7a669ac25)#define GD32\_CLOCK\_TIMER2 GD32\_CLOCK\_CONFIG(APB1EN, 1U)

[ 45](gd32f3x0-clocks_8h.md#aae8d2c65bc590e7147407099e8a938b7)#define GD32\_CLOCK\_TIMER5 GD32\_CLOCK\_CONFIG(APB1EN, 4U)

[ 46](gd32f3x0-clocks_8h.md#a60bfa7bc6aafc012fa45b395d4d22c00)#define GD32\_CLOCK\_TIMER13 GD32\_CLOCK\_CONFIG(APB1EN, 8U)

[ 47](gd32f3x0-clocks_8h.md#acd4e6949e5fb08e13129174ddd6f2e70)#define GD32\_CLOCK\_WWDGT GD32\_CLOCK\_CONFIG(APB1EN, 11U)

[ 48](gd32f3x0-clocks_8h.md#a61a4d4edd729635d5fcdd200a13a0b9b)#define GD32\_CLOCK\_SPI1 GD32\_CLOCK\_CONFIG(APB1EN, 14U)

[ 49](gd32f3x0-clocks_8h.md#a0f4528cfba6c9b129cc3aeae8220a178)#define GD32\_CLOCK\_USART1 GD32\_CLOCK\_CONFIG(APB1EN, 17U)

[ 50](gd32f3x0-clocks_8h.md#a7aa5531ee97403c9ab9152c3fa9e4b47)#define GD32\_CLOCK\_I2C0 GD32\_CLOCK\_CONFIG(APB1EN, 21U)

[ 51](gd32f3x0-clocks_8h.md#a15d339475004b458aa5aa4a4a0692355)#define GD32\_CLOCK\_I2C1 GD32\_CLOCK\_CONFIG(APB1EN, 22U)

[ 52](gd32f3x0-clocks_8h.md#a58267ff23e872483b53ff7e6bb64d69f)#define GD32\_CLOCK\_PMU GD32\_CLOCK\_CONFIG(APB1EN, 28U)

[ 53](gd32f3x0-clocks_8h.md#aaef5ffeb0d314adf6faf2a9d8158763b)#define GD32\_CLOCK\_DAC GD32\_CLOCK\_CONFIG(APB1EN, 29U)

[ 54](gd32f3x0-clocks_8h.md#a8f2a7136ffb5e7065bc28bd4782ab696)#define GD32\_CLOCK\_CEC GD32\_CLOCK\_CONFIG(APB1EN, 30U)

55

56/\* APB2 peripherals \*/

[ 57](gd32f3x0-clocks_8h.md#a795715aba6d275407e6237b06cb6e6df)#define GD32\_CLOCK\_CFGCMP GD32\_CLOCK\_CONFIG(APB2EN, 0U)

[ 58](gd32f3x0-clocks_8h.md#a49fb3dfb6cb0c66ed5ee81185896f2ab)#define GD32\_CLOCK\_ADC GD32\_CLOCK\_CONFIG(APB2EN, 9U)

[ 59](gd32f3x0-clocks_8h.md#afa309eb7291fd4416d3a5d0184991212)#define GD32\_CLOCK\_TIMER0 GD32\_CLOCK\_CONFIG(APB2EN, 11U)

[ 60](gd32f3x0-clocks_8h.md#aa1284de659aca3a7b279c4f691147fb7)#define GD32\_CLOCK\_SPI0 GD32\_CLOCK\_CONFIG(APB2EN, 12U)

[ 61](gd32f3x0-clocks_8h.md#ac1599e50ad14746470268bc14aa04318)#define GD32\_CLOCK\_USART0 GD32\_CLOCK\_CONFIG(APB2EN, 14U)

[ 62](gd32f3x0-clocks_8h.md#aa7ef737a5e522950f2ed231e987c208d)#define GD32\_CLOCK\_TIMER14 GD32\_CLOCK\_CONFIG(APB2EN, 16U)

[ 63](gd32f3x0-clocks_8h.md#a36e688b72edf92678346f5a6371b33dd)#define GD32\_CLOCK\_TIMER15 GD32\_CLOCK\_CONFIG(APB2EN, 17U)

[ 64](gd32f3x0-clocks_8h.md#a3e6797f4cc3c3dd54a9fc3ca1088ec63)#define GD32\_CLOCK\_TIMER16 GD32\_CLOCK\_CONFIG(APB2EN, 18U)

65

66/\* APB1 additional peripherals \*/

[ 67](gd32f3x0-clocks_8h.md#a886d3e4e09c70277b45f6afd5ae77eae)#define GD32\_CLOCK\_CTC GD32\_CLOCK\_CONFIG(ADDAPB1EN, 27U)

68

70

71#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32F3X0\_CLOCKS\_H\_ \*/

[gd32-clocks-common.h](gd32-clocks-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32f3x0-clocks.h](gd32f3x0-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
