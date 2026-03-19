---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32f3x0-clocks_8h.html
original_path: doxygen/html/gd32f3x0-clocks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f3x0-clocks.h File Reference

`#include "[gd32-clocks-common.h](gd32-clocks-common_8h_source.md)"`

[Go to the source code of this file.](gd32f3x0-clocks_8h_source.md)

| Macros | |
| --- | --- |
| Register offsets | |
| #define | [GD32\_AHBEN\_OFFSET](#a510e385774abf879310b061273eb4068)   0x14U |
| #define | [GD32\_APB1EN\_OFFSET](#a4b2aa082b4b2200b7f2b1663c30f205c)   0x1CU |
| #define | [GD32\_APB2EN\_OFFSET](#a9d794746eea796b39b3ae55b1614d9d9)   0x18U |
| #define | [GD32\_ADDAPB1EN\_OFFSET](#a4202c14a67ad78724b05175ede3aaa99)   0xF8U |
| Clock enable/disable definitions for peripherals | |
| #define | [GD32\_CLOCK\_DMA](#aa4a3b682dbd3877c0e505f89ce572729)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 0U) |
| #define | [GD32\_CLOCK\_SRAMSP](#a7f201b05f8c284e62be5bf9290a84a67)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 2U) |
| #define | [GD32\_CLOCK\_FMCSP](#acdbf40a9d897a38daca0d8bd5f81fc1a)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 4U) |
| #define | [GD32\_CLOCK\_CRC](#a0971986459094517a13221629cc89e95)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 6U) |
| #define | [GD32\_CLOCK\_USBFS](#ae11c1f5ccf256d32377eb9a6f07026f2)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 12U) |
| #define | [GD32\_CLOCK\_GPIOA](#a6d7de29e854deaa62412e302566efd23)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 17U) |
| #define | [GD32\_CLOCK\_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 18U) |
| #define | [GD32\_CLOCK\_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 19U) |
| #define | [GD32\_CLOCK\_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 20U) |
| #define | [GD32\_CLOCK\_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 22U) |
| #define | [GD32\_CLOCK\_TSI](#a2d044ca898ee3b1909c1de4411c139c2)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 24U) |
| #define | [GD32\_CLOCK\_TIMER1](#af084c2bf11ddfe04c80c3fac272c30e7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 0U) |
| #define | [GD32\_CLOCK\_TIMER2](#a41623cb4499589163c0697a7a669ac25)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 1U) |
| #define | [GD32\_CLOCK\_TIMER5](#aae8d2c65bc590e7147407099e8a938b7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 4U) |
| #define | [GD32\_CLOCK\_TIMER13](#a60bfa7bc6aafc012fa45b395d4d22c00)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 8U) |
| #define | [GD32\_CLOCK\_WWDGT](#acd4e6949e5fb08e13129174ddd6f2e70)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 11U) |
| #define | [GD32\_CLOCK\_SPI1](#a61a4d4edd729635d5fcdd200a13a0b9b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 14U) |
| #define | [GD32\_CLOCK\_USART1](#a0f4528cfba6c9b129cc3aeae8220a178)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 17U) |
| #define | [GD32\_CLOCK\_I2C0](#a7aa5531ee97403c9ab9152c3fa9e4b47)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 21U) |
| #define | [GD32\_CLOCK\_I2C1](#a15d339475004b458aa5aa4a4a0692355)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 22U) |
| #define | [GD32\_CLOCK\_PMU](#a58267ff23e872483b53ff7e6bb64d69f)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 28U) |
| #define | [GD32\_CLOCK\_DAC](#aaef5ffeb0d314adf6faf2a9d8158763b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 29U) |
| #define | [GD32\_CLOCK\_CEC](#a8f2a7136ffb5e7065bc28bd4782ab696)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 30U) |
| #define | [GD32\_CLOCK\_CFGCMP](#a795715aba6d275407e6237b06cb6e6df)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 0U) |
| #define | [GD32\_CLOCK\_ADC](#a49fb3dfb6cb0c66ed5ee81185896f2ab)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 9U) |
| #define | [GD32\_CLOCK\_TIMER0](#afa309eb7291fd4416d3a5d0184991212)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 11U) |
| #define | [GD32\_CLOCK\_SPI0](#aa1284de659aca3a7b279c4f691147fb7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 12U) |
| #define | [GD32\_CLOCK\_USART0](#ac1599e50ad14746470268bc14aa04318)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 14U) |
| #define | [GD32\_CLOCK\_TIMER14](#aa7ef737a5e522950f2ed231e987c208d)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 16U) |
| #define | [GD32\_CLOCK\_TIMER15](#a36e688b72edf92678346f5a6371b33dd)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 17U) |
| #define | [GD32\_CLOCK\_TIMER16](#a3e6797f4cc3c3dd54a9fc3ca1088ec63)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 18U) |
| #define | [GD32\_CLOCK\_CTC](#a886d3e4e09c70277b45f6afd5ae77eae)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(ADDAPB1EN, 27U) |

## Macro Definition Documentation

## [◆ ](#a4202c14a67ad78724b05175ede3aaa99)GD32\_ADDAPB1EN\_OFFSET

| #define GD32\_ADDAPB1EN\_OFFSET   0xF8U |
| --- |

## [◆ ](#a510e385774abf879310b061273eb4068)GD32\_AHBEN\_OFFSET

| #define GD32\_AHBEN\_OFFSET   0x14U |
| --- |

## [◆ ](#a4b2aa082b4b2200b7f2b1663c30f205c)GD32\_APB1EN\_OFFSET

| #define GD32\_APB1EN\_OFFSET   0x1CU |
| --- |

## [◆ ](#a9d794746eea796b39b3ae55b1614d9d9)GD32\_APB2EN\_OFFSET

| #define GD32\_APB2EN\_OFFSET   0x18U |
| --- |

## [◆ ](#a49fb3dfb6cb0c66ed5ee81185896f2ab)GD32\_CLOCK\_ADC

| #define GD32\_CLOCK\_ADC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 9U) |
| --- |

## [◆ ](#a8f2a7136ffb5e7065bc28bd4782ab696)GD32\_CLOCK\_CEC

| #define GD32\_CLOCK\_CEC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 30U) |
| --- |

## [◆ ](#a795715aba6d275407e6237b06cb6e6df)GD32\_CLOCK\_CFGCMP

| #define GD32\_CLOCK\_CFGCMP   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 0U) |
| --- |

## [◆ ](#a0971986459094517a13221629cc89e95)GD32\_CLOCK\_CRC

| #define GD32\_CLOCK\_CRC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 6U) |
| --- |

## [◆ ](#a886d3e4e09c70277b45f6afd5ae77eae)GD32\_CLOCK\_CTC

| #define GD32\_CLOCK\_CTC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(ADDAPB1EN, 27U) |
| --- |

## [◆ ](#aaef5ffeb0d314adf6faf2a9d8158763b)GD32\_CLOCK\_DAC

| #define GD32\_CLOCK\_DAC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 29U) |
| --- |

## [◆ ](#aa4a3b682dbd3877c0e505f89ce572729)GD32\_CLOCK\_DMA

| #define GD32\_CLOCK\_DMA   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 0U) |
| --- |

## [◆ ](#acdbf40a9d897a38daca0d8bd5f81fc1a)GD32\_CLOCK\_FMCSP

| #define GD32\_CLOCK\_FMCSP   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 4U) |
| --- |

## [◆ ](#a6d7de29e854deaa62412e302566efd23)GD32\_CLOCK\_GPIOA

| #define GD32\_CLOCK\_GPIOA   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 17U) |
| --- |

## [◆ ](#a4272044e59f7e6935b5fc231d7da4a3e)GD32\_CLOCK\_GPIOB

| #define GD32\_CLOCK\_GPIOB   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 18U) |
| --- |

## [◆ ](#a8a415ead74c233d769ac7649bbc678ee)GD32\_CLOCK\_GPIOC

| #define GD32\_CLOCK\_GPIOC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 19U) |
| --- |

## [◆ ](#a6e674cc73448d4c7487fb05a9368a5b0)GD32\_CLOCK\_GPIOD

| #define GD32\_CLOCK\_GPIOD   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 20U) |
| --- |

## [◆ ](#a8eaec3ec9ef667aaad9553f9a24fbbfe)GD32\_CLOCK\_GPIOF

| #define GD32\_CLOCK\_GPIOF   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 22U) |
| --- |

## [◆ ](#a7aa5531ee97403c9ab9152c3fa9e4b47)GD32\_CLOCK\_I2C0

| #define GD32\_CLOCK\_I2C0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 21U) |
| --- |

## [◆ ](#a15d339475004b458aa5aa4a4a0692355)GD32\_CLOCK\_I2C1

| #define GD32\_CLOCK\_I2C1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 22U) |
| --- |

## [◆ ](#a58267ff23e872483b53ff7e6bb64d69f)GD32\_CLOCK\_PMU

| #define GD32\_CLOCK\_PMU   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 28U) |
| --- |

## [◆ ](#aa1284de659aca3a7b279c4f691147fb7)GD32\_CLOCK\_SPI0

| #define GD32\_CLOCK\_SPI0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 12U) |
| --- |

## [◆ ](#a61a4d4edd729635d5fcdd200a13a0b9b)GD32\_CLOCK\_SPI1

| #define GD32\_CLOCK\_SPI1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 14U) |
| --- |

## [◆ ](#a7f201b05f8c284e62be5bf9290a84a67)GD32\_CLOCK\_SRAMSP

| #define GD32\_CLOCK\_SRAMSP   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 2U) |
| --- |

## [◆ ](#afa309eb7291fd4416d3a5d0184991212)GD32\_CLOCK\_TIMER0

| #define GD32\_CLOCK\_TIMER0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 11U) |
| --- |

## [◆ ](#af084c2bf11ddfe04c80c3fac272c30e7)GD32\_CLOCK\_TIMER1

| #define GD32\_CLOCK\_TIMER1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 0U) |
| --- |

## [◆ ](#a60bfa7bc6aafc012fa45b395d4d22c00)GD32\_CLOCK\_TIMER13

| #define GD32\_CLOCK\_TIMER13   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 8U) |
| --- |

## [◆ ](#aa7ef737a5e522950f2ed231e987c208d)GD32\_CLOCK\_TIMER14

| #define GD32\_CLOCK\_TIMER14   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 16U) |
| --- |

## [◆ ](#a36e688b72edf92678346f5a6371b33dd)GD32\_CLOCK\_TIMER15

| #define GD32\_CLOCK\_TIMER15   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 17U) |
| --- |

## [◆ ](#a3e6797f4cc3c3dd54a9fc3ca1088ec63)GD32\_CLOCK\_TIMER16

| #define GD32\_CLOCK\_TIMER16   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 18U) |
| --- |

## [◆ ](#a41623cb4499589163c0697a7a669ac25)GD32\_CLOCK\_TIMER2

| #define GD32\_CLOCK\_TIMER2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 1U) |
| --- |

## [◆ ](#aae8d2c65bc590e7147407099e8a938b7)GD32\_CLOCK\_TIMER5

| #define GD32\_CLOCK\_TIMER5   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 4U) |
| --- |

## [◆ ](#a2d044ca898ee3b1909c1de4411c139c2)GD32\_CLOCK\_TSI

| #define GD32\_CLOCK\_TSI   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 24U) |
| --- |

## [◆ ](#ac1599e50ad14746470268bc14aa04318)GD32\_CLOCK\_USART0

| #define GD32\_CLOCK\_USART0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 14U) |
| --- |

## [◆ ](#a0f4528cfba6c9b129cc3aeae8220a178)GD32\_CLOCK\_USART1

| #define GD32\_CLOCK\_USART1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 17U) |
| --- |

## [◆ ](#ae11c1f5ccf256d32377eb9a6f07026f2)GD32\_CLOCK\_USBFS

| #define GD32\_CLOCK\_USBFS   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHBEN, 12U) |
| --- |

## [◆ ](#acd4e6949e5fb08e13129174ddd6f2e70)GD32\_CLOCK\_WWDGT

| #define GD32\_CLOCK\_WWDGT   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 11U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32f3x0-clocks.h](gd32f3x0-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
