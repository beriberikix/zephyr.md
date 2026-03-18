---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gd32l23x-clocks_8h.html
original_path: doxygen/html/gd32l23x-clocks_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32l23x-clocks.h File Reference

`#include "[gd32-clocks-common.h](gd32-clocks-common_8h_source.md)"`

[Go to the source code of this file.](gd32l23x-clocks_8h_source.md)

| Macros | |
| --- | --- |
| Register offsets | |
| #define | [GD32\_AHB1EN\_OFFSET](#a339c9d51e00c124e8c3fcb3f60d4ab11)   0x14U |
| #define | [GD32\_APB1EN\_OFFSET](#a4b2aa082b4b2200b7f2b1663c30f205c)   0x1CU |
| #define | [GD32\_APB2EN\_OFFSET](#a9d794746eea796b39b3ae55b1614d9d9)   0x18U |
| Clock enable/disable definitions for peripherals | |
| #define | [GD32\_CLOCK\_DMA](#aa4a3b682dbd3877c0e505f89ce572729)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 0U) |
| #define | [GD32\_CLOCK\_SRAM0](#aa492c4ed7ca62ad488bd34a9c39f7ee7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 2U) |
| #define | [GD32\_CLOCK\_FMC](#a695eb7a95fa6b5d57b763629757bf1b1)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 4U) |
| #define | [GD32\_CLOCK\_CRC](#a0971986459094517a13221629cc89e95)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 6U) |
| #define | [GD32\_CLOCK\_SRAM1](#aa72ff0249d857ac302e3b247cc08d8c8)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 7U) |
| #define | [GD32\_CLOCK\_GPIOA](#a6d7de29e854deaa62412e302566efd23)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 17U) |
| #define | [GD32\_CLOCK\_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 18U) |
| #define | [GD32\_CLOCK\_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 19U) |
| #define | [GD32\_CLOCK\_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 20U) |
| #define | [GD32\_CLOCK\_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 22U) |
| #define | [GD32\_CLOCK\_CAU](#a0654988b7208162ddcdf649167734784)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 1U) |
| #define | [GD32\_CLOCK\_TRNG](#ad7e9e9d34e7acca03e2538e1d5f52c0e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 3U) |
| #define | [GD32\_CLOCK\_TIMER1](#af084c2bf11ddfe04c80c3fac272c30e7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 0U) |
| #define | [GD32\_CLOCK\_TIMER2](#a41623cb4499589163c0697a7a669ac25)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 1U) |
| #define | [GD32\_CLOCK\_TIMER5](#aae8d2c65bc590e7147407099e8a938b7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 4U) |
| #define | [GD32\_CLOCK\_TIMER6](#a0e1b450d86f9e5b08a5738116742b429)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 5U) |
| #define | [GD32\_CLOCK\_TIMER11](#afffce8951164061ccedc46edad527cf8)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 8U) |
| #define | [GD32\_CLOCK\_LPTIMER](#af2dcccd27d498112f102c9148abb42f7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 9U) |
| #define | [GD32\_CLOCK\_SLCD](#ae41c4f96dae0097b82ff22932f90aefe)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 10U) |
| #define | [GD32\_CLOCK\_WWDGT](#acd4e6949e5fb08e13129174ddd6f2e70)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 11U) |
| #define | [GD32\_CLOCK\_SPI1](#a61a4d4edd729635d5fcdd200a13a0b9b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 14U) |
| #define | [GD32\_CLOCK\_USART1](#a0f4528cfba6c9b129cc3aeae8220a178)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 17U) |
| #define | [GD32\_CLOCK\_LPUART](#a6bc2e3226c496d0c1f754dac515fe568)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 18U) |
| #define | [GD32\_CLOCK\_UART3](#a149bc461b6b4f81cafe38f9c7f40c8cd)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 19U) |
| #define | [GD32\_CLOCK\_UART4](#a82468e78744e139664daeb68f8f181da)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 20U) |
| #define | [GD32\_CLOCK\_I2C0](#a7aa5531ee97403c9ab9152c3fa9e4b47)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 21U) |
| #define | [GD32\_CLOCK\_I2C1](#a15d339475004b458aa5aa4a4a0692355)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 22U) |
| #define | [GD32\_CLOCK\_USBD](#a0e6ade78ea2b16517f960f4dd9de12f3)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 23U) |
| #define | [GD32\_CLOCK\_I2C2](#a9e36e327a61c6867c787d6648b8ec2ac)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 24U) |
| #define | [GD32\_CLOCK\_PMU](#a58267ff23e872483b53ff7e6bb64d69f)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 28U) |
| #define | [GD32\_CLOCK\_DAC](#aaef5ffeb0d314adf6faf2a9d8158763b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 29U) |
| #define | [GD32\_CLOCK\_CTC](#a886d3e4e09c70277b45f6afd5ae77eae)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 30U) |
| #define | [GD32\_CLOCK\_BKP](#a45f1e755993e4ccdda57966c147309dc)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 31U) |
| #define | [GD32\_CLOCK\_SYSCFG](#a82d39e45cb7402ed96ab29953f8e131f)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 0U) |
| #define | [GD32\_CLOCK\_CMP](#a86ba69950ab9daffa9c98d898a8b1186)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 1U) |
| #define | [GD32\_CLOCK\_ADC](#a49fb3dfb6cb0c66ed5ee81185896f2ab)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 9U) |
| #define | [GD32\_CLOCK\_TIMER8](#adbac39fc1c001fbb14036f08c81810ef)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 11U) |
| #define | [GD32\_CLOCK\_SPI0](#aa1284de659aca3a7b279c4f691147fb7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 12U) |
| #define | [GD32\_CLOCK\_USART0](#ac1599e50ad14746470268bc14aa04318)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 14U) |
| #define | [GD32\_CLOCK\_DBGMCU](#a8d82d9131757c46462c8d983a919b94b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 22U) |

## Macro Definition Documentation

## [◆ ](#a339c9d51e00c124e8c3fcb3f60d4ab11)GD32\_AHB1EN\_OFFSET

| #define GD32\_AHB1EN\_OFFSET   0x14U |
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

## [◆ ](#a45f1e755993e4ccdda57966c147309dc)GD32\_CLOCK\_BKP

| #define GD32\_CLOCK\_BKP   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 31U) |
| --- |

## [◆ ](#a0654988b7208162ddcdf649167734784)GD32\_CLOCK\_CAU

| #define GD32\_CLOCK\_CAU   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 1U) |
| --- |

## [◆ ](#a86ba69950ab9daffa9c98d898a8b1186)GD32\_CLOCK\_CMP

| #define GD32\_CLOCK\_CMP   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 1U) |
| --- |

## [◆ ](#a0971986459094517a13221629cc89e95)GD32\_CLOCK\_CRC

| #define GD32\_CLOCK\_CRC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 6U) |
| --- |

## [◆ ](#a886d3e4e09c70277b45f6afd5ae77eae)GD32\_CLOCK\_CTC

| #define GD32\_CLOCK\_CTC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 30U) |
| --- |

## [◆ ](#aaef5ffeb0d314adf6faf2a9d8158763b)GD32\_CLOCK\_DAC

| #define GD32\_CLOCK\_DAC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 29U) |
| --- |

## [◆ ](#a8d82d9131757c46462c8d983a919b94b)GD32\_CLOCK\_DBGMCU

| #define GD32\_CLOCK\_DBGMCU   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 22U) |
| --- |

## [◆ ](#aa4a3b682dbd3877c0e505f89ce572729)GD32\_CLOCK\_DMA

| #define GD32\_CLOCK\_DMA   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 0U) |
| --- |

## [◆ ](#a695eb7a95fa6b5d57b763629757bf1b1)GD32\_CLOCK\_FMC

| #define GD32\_CLOCK\_FMC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 4U) |
| --- |

## [◆ ](#a6d7de29e854deaa62412e302566efd23)GD32\_CLOCK\_GPIOA

| #define GD32\_CLOCK\_GPIOA   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 17U) |
| --- |

## [◆ ](#a4272044e59f7e6935b5fc231d7da4a3e)GD32\_CLOCK\_GPIOB

| #define GD32\_CLOCK\_GPIOB   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 18U) |
| --- |

## [◆ ](#a8a415ead74c233d769ac7649bbc678ee)GD32\_CLOCK\_GPIOC

| #define GD32\_CLOCK\_GPIOC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 19U) |
| --- |

## [◆ ](#a6e674cc73448d4c7487fb05a9368a5b0)GD32\_CLOCK\_GPIOD

| #define GD32\_CLOCK\_GPIOD   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 20U) |
| --- |

## [◆ ](#a8eaec3ec9ef667aaad9553f9a24fbbfe)GD32\_CLOCK\_GPIOF

| #define GD32\_CLOCK\_GPIOF   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 22U) |
| --- |

## [◆ ](#a7aa5531ee97403c9ab9152c3fa9e4b47)GD32\_CLOCK\_I2C0

| #define GD32\_CLOCK\_I2C0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 21U) |
| --- |

## [◆ ](#a15d339475004b458aa5aa4a4a0692355)GD32\_CLOCK\_I2C1

| #define GD32\_CLOCK\_I2C1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 22U) |
| --- |

## [◆ ](#a9e36e327a61c6867c787d6648b8ec2ac)GD32\_CLOCK\_I2C2

| #define GD32\_CLOCK\_I2C2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 24U) |
| --- |

## [◆ ](#af2dcccd27d498112f102c9148abb42f7)GD32\_CLOCK\_LPTIMER

| #define GD32\_CLOCK\_LPTIMER   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 9U) |
| --- |

## [◆ ](#a6bc2e3226c496d0c1f754dac515fe568)GD32\_CLOCK\_LPUART

| #define GD32\_CLOCK\_LPUART   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 18U) |
| --- |

## [◆ ](#a58267ff23e872483b53ff7e6bb64d69f)GD32\_CLOCK\_PMU

| #define GD32\_CLOCK\_PMU   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 28U) |
| --- |

## [◆ ](#ae41c4f96dae0097b82ff22932f90aefe)GD32\_CLOCK\_SLCD

| #define GD32\_CLOCK\_SLCD   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 10U) |
| --- |

## [◆ ](#aa1284de659aca3a7b279c4f691147fb7)GD32\_CLOCK\_SPI0

| #define GD32\_CLOCK\_SPI0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 12U) |
| --- |

## [◆ ](#a61a4d4edd729635d5fcdd200a13a0b9b)GD32\_CLOCK\_SPI1

| #define GD32\_CLOCK\_SPI1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 14U) |
| --- |

## [◆ ](#aa492c4ed7ca62ad488bd34a9c39f7ee7)GD32\_CLOCK\_SRAM0

| #define GD32\_CLOCK\_SRAM0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 2U) |
| --- |

## [◆ ](#aa72ff0249d857ac302e3b247cc08d8c8)GD32\_CLOCK\_SRAM1

| #define GD32\_CLOCK\_SRAM1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 7U) |
| --- |

## [◆ ](#a82d39e45cb7402ed96ab29953f8e131f)GD32\_CLOCK\_SYSCFG

| #define GD32\_CLOCK\_SYSCFG   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 0U) |
| --- |

## [◆ ](#af084c2bf11ddfe04c80c3fac272c30e7)GD32\_CLOCK\_TIMER1

| #define GD32\_CLOCK\_TIMER1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 0U) |
| --- |

## [◆ ](#afffce8951164061ccedc46edad527cf8)GD32\_CLOCK\_TIMER11

| #define GD32\_CLOCK\_TIMER11   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 8U) |
| --- |

## [◆ ](#a41623cb4499589163c0697a7a669ac25)GD32\_CLOCK\_TIMER2

| #define GD32\_CLOCK\_TIMER2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 1U) |
| --- |

## [◆ ](#aae8d2c65bc590e7147407099e8a938b7)GD32\_CLOCK\_TIMER5

| #define GD32\_CLOCK\_TIMER5   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 4U) |
| --- |

## [◆ ](#a0e1b450d86f9e5b08a5738116742b429)GD32\_CLOCK\_TIMER6

| #define GD32\_CLOCK\_TIMER6   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 5U) |
| --- |

## [◆ ](#adbac39fc1c001fbb14036f08c81810ef)GD32\_CLOCK\_TIMER8

| #define GD32\_CLOCK\_TIMER8   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 11U) |
| --- |

## [◆ ](#ad7e9e9d34e7acca03e2538e1d5f52c0e)GD32\_CLOCK\_TRNG

| #define GD32\_CLOCK\_TRNG   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 3U) |
| --- |

## [◆ ](#a149bc461b6b4f81cafe38f9c7f40c8cd)GD32\_CLOCK\_UART3

| #define GD32\_CLOCK\_UART3   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 19U) |
| --- |

## [◆ ](#a82468e78744e139664daeb68f8f181da)GD32\_CLOCK\_UART4

| #define GD32\_CLOCK\_UART4   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 20U) |
| --- |

## [◆ ](#ac1599e50ad14746470268bc14aa04318)GD32\_CLOCK\_USART0

| #define GD32\_CLOCK\_USART0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 14U) |
| --- |

## [◆ ](#a0f4528cfba6c9b129cc3aeae8220a178)GD32\_CLOCK\_USART1

| #define GD32\_CLOCK\_USART1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 17U) |
| --- |

## [◆ ](#a0e6ade78ea2b16517f960f4dd9de12f3)GD32\_CLOCK\_USBD

| #define GD32\_CLOCK\_USBD   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 23U) |
| --- |

## [◆ ](#acd4e6949e5fb08e13129174ddd6f2e70)GD32\_CLOCK\_WWDGT

| #define GD32\_CLOCK\_WWDGT   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 11U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32l23x-clocks.h](gd32l23x-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
