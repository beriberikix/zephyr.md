---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32f4xx-clocks_8h.html
original_path: doxygen/html/gd32f4xx-clocks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f4xx-clocks.h File Reference

`#include "[gd32-clocks-common.h](gd32-clocks-common_8h_source.md)"`

[Go to the source code of this file.](gd32f4xx-clocks_8h_source.md)

| Macros | |
| --- | --- |
| Register offsets | |
| #define | [GD32\_AHB1EN\_OFFSET](#a339c9d51e00c124e8c3fcb3f60d4ab11)   0x30U |
| #define | [GD32\_AHB2EN\_OFFSET](#a6e31d435e5f43b51f733ff72654e3028)   0x34U |
| #define | [GD32\_AHB3EN\_OFFSET](#a124c1f305697766c2e616b4102469a08)   0x38U |
| #define | [GD32\_APB1EN\_OFFSET](#a4b2aa082b4b2200b7f2b1663c30f205c)   0x40U |
| #define | [GD32\_APB2EN\_OFFSET](#a9d794746eea796b39b3ae55b1614d9d9)   0x44U |
| #define | [GD32\_ADDAPB1EN\_OFFSET](#a4202c14a67ad78724b05175ede3aaa99)   0xE4U |
| Clock enable/disable definitions for peripherals | |
| #define | [GD32\_CLOCK\_GPIOA](#a6d7de29e854deaa62412e302566efd23)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 0U) |
| #define | [GD32\_CLOCK\_GPIOB](#a4272044e59f7e6935b5fc231d7da4a3e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 1U) |
| #define | [GD32\_CLOCK\_GPIOC](#a8a415ead74c233d769ac7649bbc678ee)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 2U) |
| #define | [GD32\_CLOCK\_GPIOD](#a6e674cc73448d4c7487fb05a9368a5b0)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 3U) |
| #define | [GD32\_CLOCK\_GPIOE](#a77e5bd38cfd6018f8a5e518b388e764d)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 4U) |
| #define | [GD32\_CLOCK\_GPIOF](#a8eaec3ec9ef667aaad9553f9a24fbbfe)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 5U) |
| #define | [GD32\_CLOCK\_GPIOG](#a2f91cac90de074a5478c73392c107027)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 6U) |
| #define | [GD32\_CLOCK\_GPIOH](#aa61dad33dbaa553cdaff7c5e6d674758)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 7U) |
| #define | [GD32\_CLOCK\_GPIOI](#ac48646b69241ec518c12f5c92c982a4e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 8U) |
| #define | [GD32\_CLOCK\_CRC](#a0971986459094517a13221629cc89e95)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 12U) |
| #define | [GD32\_CLOCK\_BKPSRAM](#a07ab9ef3cb3d81f90c7363712725b55a)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 18U) |
| #define | [GD32\_CLOCK\_TCMSRAM](#a035e6888de8ffcd4793928015996cebf)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 20U) |
| #define | [GD32\_CLOCK\_DMA0](#a7728f090fb52201d3d1162881b80dc3e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 21U) |
| #define | [GD32\_CLOCK\_DMA1](#af6c6eb89797f088a78722ce007ae47e5)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 22U) |
| #define | [GD32\_CLOCK\_IPA](#ad37a43a7c3bafef7f5af454d9311607e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 23U) |
| #define | [GD32\_CLOCK\_ENET](#a824f638811c4469fedc65a1e29aac8d0)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 25U) |
| #define | [GD32\_CLOCK\_ENETTX](#a6b14717b0c1cf864f1fe63b8ca42a439)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 26U) |
| #define | [GD32\_CLOCK\_ENETRX](#a05dce9f9343146d02a71a50b1f9416f7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 27U) |
| #define | [GD32\_CLOCK\_ENETPTP](#afb7f99d35b7c726a99a7da0d1288697c)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 28U) |
| #define | [GD32\_CLOCK\_USBHS](#a9bb9a4af2877fa954bda83bb8fbc39a6)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 29U) |
| #define | [GD32\_CLOCK\_USBHSULPI](#a921ac30c07db5ab957c001cc0cbbdd0d)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 30U) |
| #define | [GD32\_CLOCK\_DCI](#a992085b45325f4ece017ca26d754b217)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 0U) |
| #define | [GD32\_CLOCK\_TRNG](#ad7e9e9d34e7acca03e2538e1d5f52c0e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 6U) |
| #define | [GD32\_CLOCK\_USBFS](#ae11c1f5ccf256d32377eb9a6f07026f2)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 7U) |
| #define | [GD32\_CLOCK\_EXMC](#af4ca0b77d98d8825493b868d19d7759a)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB3EN, 0U) |
| #define | [GD32\_CLOCK\_TIMER1](#af084c2bf11ddfe04c80c3fac272c30e7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 0U) |
| #define | [GD32\_CLOCK\_TIMER2](#a41623cb4499589163c0697a7a669ac25)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 1U) |
| #define | [GD32\_CLOCK\_TIMER3](#afb5aa7f1705febd51a92f9370bd03d14)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 2U) |
| #define | [GD32\_CLOCK\_TIMER4](#a9d52a01572ab9309c5ebd3a0def8542f)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 3U) |
| #define | [GD32\_CLOCK\_TIMER5](#aae8d2c65bc590e7147407099e8a938b7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 4U) |
| #define | [GD32\_CLOCK\_TIMER6](#a0e1b450d86f9e5b08a5738116742b429)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 5U) |
| #define | [GD32\_CLOCK\_TIMER11](#afffce8951164061ccedc46edad527cf8)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 6U) |
| #define | [GD32\_CLOCK\_TIMER12](#a285a372dc49a8df0888813b08c8804ef)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 7U) |
| #define | [GD32\_CLOCK\_TIMER13](#a60bfa7bc6aafc012fa45b395d4d22c00)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 8U) |
| #define | [GD32\_CLOCK\_WWDGT](#acd4e6949e5fb08e13129174ddd6f2e70)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 11U) |
| #define | [GD32\_CLOCK\_SPI1](#a61a4d4edd729635d5fcdd200a13a0b9b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 14U) |
| #define | [GD32\_CLOCK\_SPI2](#a4bb28caf86a54e343c75a597b0bddc20)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 15U) |
| #define | [GD32\_CLOCK\_USART1](#a0f4528cfba6c9b129cc3aeae8220a178)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 17U) |
| #define | [GD32\_CLOCK\_USART2](#a477baf1c1a265b4c86019a5f52820622)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 18U) |
| #define | [GD32\_CLOCK\_UART3](#a149bc461b6b4f81cafe38f9c7f40c8cd)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 19U) |
| #define | [GD32\_CLOCK\_UART4](#a82468e78744e139664daeb68f8f181da)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 20U) |
| #define | [GD32\_CLOCK\_I2C0](#a7aa5531ee97403c9ab9152c3fa9e4b47)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 21U) |
| #define | [GD32\_CLOCK\_I2C1](#a15d339475004b458aa5aa4a4a0692355)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 22U) |
| #define | [GD32\_CLOCK\_I2C2](#a9e36e327a61c6867c787d6648b8ec2ac)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 23U) |
| #define | [GD32\_CLOCK\_CAN0](#a567dfd2f603a04594ab82aeac7339655)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 25U) |
| #define | [GD32\_CLOCK\_CAN1](#a73858e2f6a1654e6114790c9dea80cd0)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 26U) |
| #define | [GD32\_CLOCK\_PMU](#a58267ff23e872483b53ff7e6bb64d69f)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 28U) |
| #define | [GD32\_CLOCK\_DAC](#aaef5ffeb0d314adf6faf2a9d8158763b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 29U) |
| #define | [GD32\_CLOCK\_UART6](#a8ec6e1dfab01b3652183c38eac160288)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 30U) |
| #define | [GD32\_CLOCK\_UART7](#a683cb88b874a2b6802bba5f99b85163e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 31U) |
| #define | [GD32\_CLOCK\_RTC](#a1f8cfe3ba991c9773b21c1e417bd3421)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(BDCTL, 15U) |
| #define | [GD32\_CLOCK\_TIMER0](#afa309eb7291fd4416d3a5d0184991212)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 0U) |
| #define | [GD32\_CLOCK\_TIMER7](#abb3f432fa2ef4e6c69a4c252493c0606)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 1U) |
| #define | [GD32\_CLOCK\_USART0](#ac1599e50ad14746470268bc14aa04318)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 4U) |
| #define | [GD32\_CLOCK\_USART5](#a736a4d8ae51d88226f8baeec49be4dc5)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 5U) |
| #define | [GD32\_CLOCK\_ADC0](#a59b782811760bb907d00801305564c94)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 8U) |
| #define | [GD32\_CLOCK\_ADC1](#a2ee53a1088b6dc17320d3d35ffdb1848)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 9U) |
| #define | [GD32\_CLOCK\_ADC2](#a5710e96c011ed3c8dc90f63b842751cc)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 10U) |
| #define | [GD32\_CLOCK\_SDIO](#ad1ba647a10df2ea0bd81676cb5f46064)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 11U) |
| #define | [GD32\_CLOCK\_SPI0](#aa1284de659aca3a7b279c4f691147fb7)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 12U) |
| #define | [GD32\_CLOCK\_SPI3](#adc1fc8ab68a58bc412e4560cdd56c25e)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 13U) |
| #define | [GD32\_CLOCK\_SYSCFG](#a82d39e45cb7402ed96ab29953f8e131f)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 14U) |
| #define | [GD32\_CLOCK\_TIMER8](#adbac39fc1c001fbb14036f08c81810ef)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 16U) |
| #define | [GD32\_CLOCK\_TIMER9](#a3981da513ef2eb351b403f6dc11a2c6b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 17U) |
| #define | [GD32\_CLOCK\_TIMER10](#a7c3b4d23aac8844faac79f458cc5e07b)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 18U) |
| #define | [GD32\_CLOCK\_SPI4](#a0fa21a935cec395aab91ba0394572d2c)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 20U) |
| #define | [GD32\_CLOCK\_SPI5](#adfe3187c5b24e430f5071e1855a51108)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 21U) |
| #define | [GD32\_CLOCK\_TLI](#ab04cbf84abb9f4923b6e9381c22bdae1)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 26U) |
| #define | [GD32\_CLOCK\_CTC](#a886d3e4e09c70277b45f6afd5ae77eae)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(ADDAPB1EN, 27U) |
| #define | [GD32\_CLOCK\_IREF](#ab2207ccb1c350c57aa19963285bf5470)   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(ADDAPB1EN, 31U) |

## Macro Definition Documentation

## [◆ ](#a4202c14a67ad78724b05175ede3aaa99)GD32\_ADDAPB1EN\_OFFSET

| #define GD32\_ADDAPB1EN\_OFFSET   0xE4U |
| --- |

## [◆ ](#a339c9d51e00c124e8c3fcb3f60d4ab11)GD32\_AHB1EN\_OFFSET

| #define GD32\_AHB1EN\_OFFSET   0x30U |
| --- |

## [◆ ](#a6e31d435e5f43b51f733ff72654e3028)GD32\_AHB2EN\_OFFSET

| #define GD32\_AHB2EN\_OFFSET   0x34U |
| --- |

## [◆ ](#a124c1f305697766c2e616b4102469a08)GD32\_AHB3EN\_OFFSET

| #define GD32\_AHB3EN\_OFFSET   0x38U |
| --- |

## [◆ ](#a4b2aa082b4b2200b7f2b1663c30f205c)GD32\_APB1EN\_OFFSET

| #define GD32\_APB1EN\_OFFSET   0x40U |
| --- |

## [◆ ](#a9d794746eea796b39b3ae55b1614d9d9)GD32\_APB2EN\_OFFSET

| #define GD32\_APB2EN\_OFFSET   0x44U |
| --- |

## [◆ ](#a59b782811760bb907d00801305564c94)GD32\_CLOCK\_ADC0

| #define GD32\_CLOCK\_ADC0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 8U) |
| --- |

## [◆ ](#a2ee53a1088b6dc17320d3d35ffdb1848)GD32\_CLOCK\_ADC1

| #define GD32\_CLOCK\_ADC1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 9U) |
| --- |

## [◆ ](#a5710e96c011ed3c8dc90f63b842751cc)GD32\_CLOCK\_ADC2

| #define GD32\_CLOCK\_ADC2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 10U) |
| --- |

## [◆ ](#a07ab9ef3cb3d81f90c7363712725b55a)GD32\_CLOCK\_BKPSRAM

| #define GD32\_CLOCK\_BKPSRAM   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 18U) |
| --- |

## [◆ ](#a567dfd2f603a04594ab82aeac7339655)GD32\_CLOCK\_CAN0

| #define GD32\_CLOCK\_CAN0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 25U) |
| --- |

## [◆ ](#a73858e2f6a1654e6114790c9dea80cd0)GD32\_CLOCK\_CAN1

| #define GD32\_CLOCK\_CAN1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 26U) |
| --- |

## [◆ ](#a0971986459094517a13221629cc89e95)GD32\_CLOCK\_CRC

| #define GD32\_CLOCK\_CRC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 12U) |
| --- |

## [◆ ](#a886d3e4e09c70277b45f6afd5ae77eae)GD32\_CLOCK\_CTC

| #define GD32\_CLOCK\_CTC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(ADDAPB1EN, 27U) |
| --- |

## [◆ ](#aaef5ffeb0d314adf6faf2a9d8158763b)GD32\_CLOCK\_DAC

| #define GD32\_CLOCK\_DAC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 29U) |
| --- |

## [◆ ](#a992085b45325f4ece017ca26d754b217)GD32\_CLOCK\_DCI

| #define GD32\_CLOCK\_DCI   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 0U) |
| --- |

## [◆ ](#a7728f090fb52201d3d1162881b80dc3e)GD32\_CLOCK\_DMA0

| #define GD32\_CLOCK\_DMA0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 21U) |
| --- |

## [◆ ](#af6c6eb89797f088a78722ce007ae47e5)GD32\_CLOCK\_DMA1

| #define GD32\_CLOCK\_DMA1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 22U) |
| --- |

## [◆ ](#a824f638811c4469fedc65a1e29aac8d0)GD32\_CLOCK\_ENET

| #define GD32\_CLOCK\_ENET   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 25U) |
| --- |

## [◆ ](#afb7f99d35b7c726a99a7da0d1288697c)GD32\_CLOCK\_ENETPTP

| #define GD32\_CLOCK\_ENETPTP   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 28U) |
| --- |

## [◆ ](#a05dce9f9343146d02a71a50b1f9416f7)GD32\_CLOCK\_ENETRX

| #define GD32\_CLOCK\_ENETRX   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 27U) |
| --- |

## [◆ ](#a6b14717b0c1cf864f1fe63b8ca42a439)GD32\_CLOCK\_ENETTX

| #define GD32\_CLOCK\_ENETTX   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 26U) |
| --- |

## [◆ ](#af4ca0b77d98d8825493b868d19d7759a)GD32\_CLOCK\_EXMC

| #define GD32\_CLOCK\_EXMC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB3EN, 0U) |
| --- |

## [◆ ](#a6d7de29e854deaa62412e302566efd23)GD32\_CLOCK\_GPIOA

| #define GD32\_CLOCK\_GPIOA   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 0U) |
| --- |

## [◆ ](#a4272044e59f7e6935b5fc231d7da4a3e)GD32\_CLOCK\_GPIOB

| #define GD32\_CLOCK\_GPIOB   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 1U) |
| --- |

## [◆ ](#a8a415ead74c233d769ac7649bbc678ee)GD32\_CLOCK\_GPIOC

| #define GD32\_CLOCK\_GPIOC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 2U) |
| --- |

## [◆ ](#a6e674cc73448d4c7487fb05a9368a5b0)GD32\_CLOCK\_GPIOD

| #define GD32\_CLOCK\_GPIOD   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 3U) |
| --- |

## [◆ ](#a77e5bd38cfd6018f8a5e518b388e764d)GD32\_CLOCK\_GPIOE

| #define GD32\_CLOCK\_GPIOE   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 4U) |
| --- |

## [◆ ](#a8eaec3ec9ef667aaad9553f9a24fbbfe)GD32\_CLOCK\_GPIOF

| #define GD32\_CLOCK\_GPIOF   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 5U) |
| --- |

## [◆ ](#a2f91cac90de074a5478c73392c107027)GD32\_CLOCK\_GPIOG

| #define GD32\_CLOCK\_GPIOG   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 6U) |
| --- |

## [◆ ](#aa61dad33dbaa553cdaff7c5e6d674758)GD32\_CLOCK\_GPIOH

| #define GD32\_CLOCK\_GPIOH   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 7U) |
| --- |

## [◆ ](#ac48646b69241ec518c12f5c92c982a4e)GD32\_CLOCK\_GPIOI

| #define GD32\_CLOCK\_GPIOI   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 8U) |
| --- |

## [◆ ](#a7aa5531ee97403c9ab9152c3fa9e4b47)GD32\_CLOCK\_I2C0

| #define GD32\_CLOCK\_I2C0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 21U) |
| --- |

## [◆ ](#a15d339475004b458aa5aa4a4a0692355)GD32\_CLOCK\_I2C1

| #define GD32\_CLOCK\_I2C1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 22U) |
| --- |

## [◆ ](#a9e36e327a61c6867c787d6648b8ec2ac)GD32\_CLOCK\_I2C2

| #define GD32\_CLOCK\_I2C2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 23U) |
| --- |

## [◆ ](#ad37a43a7c3bafef7f5af454d9311607e)GD32\_CLOCK\_IPA

| #define GD32\_CLOCK\_IPA   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 23U) |
| --- |

## [◆ ](#ab2207ccb1c350c57aa19963285bf5470)GD32\_CLOCK\_IREF

| #define GD32\_CLOCK\_IREF   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(ADDAPB1EN, 31U) |
| --- |

## [◆ ](#a58267ff23e872483b53ff7e6bb64d69f)GD32\_CLOCK\_PMU

| #define GD32\_CLOCK\_PMU   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 28U) |
| --- |

## [◆ ](#a1f8cfe3ba991c9773b21c1e417bd3421)GD32\_CLOCK\_RTC

| #define GD32\_CLOCK\_RTC   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(BDCTL, 15U) |
| --- |

## [◆ ](#ad1ba647a10df2ea0bd81676cb5f46064)GD32\_CLOCK\_SDIO

| #define GD32\_CLOCK\_SDIO   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 11U) |
| --- |

## [◆ ](#aa1284de659aca3a7b279c4f691147fb7)GD32\_CLOCK\_SPI0

| #define GD32\_CLOCK\_SPI0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 12U) |
| --- |

## [◆ ](#a61a4d4edd729635d5fcdd200a13a0b9b)GD32\_CLOCK\_SPI1

| #define GD32\_CLOCK\_SPI1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 14U) |
| --- |

## [◆ ](#a4bb28caf86a54e343c75a597b0bddc20)GD32\_CLOCK\_SPI2

| #define GD32\_CLOCK\_SPI2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 15U) |
| --- |

## [◆ ](#adc1fc8ab68a58bc412e4560cdd56c25e)GD32\_CLOCK\_SPI3

| #define GD32\_CLOCK\_SPI3   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 13U) |
| --- |

## [◆ ](#a0fa21a935cec395aab91ba0394572d2c)GD32\_CLOCK\_SPI4

| #define GD32\_CLOCK\_SPI4   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 20U) |
| --- |

## [◆ ](#adfe3187c5b24e430f5071e1855a51108)GD32\_CLOCK\_SPI5

| #define GD32\_CLOCK\_SPI5   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 21U) |
| --- |

## [◆ ](#a82d39e45cb7402ed96ab29953f8e131f)GD32\_CLOCK\_SYSCFG

| #define GD32\_CLOCK\_SYSCFG   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 14U) |
| --- |

## [◆ ](#a035e6888de8ffcd4793928015996cebf)GD32\_CLOCK\_TCMSRAM

| #define GD32\_CLOCK\_TCMSRAM   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 20U) |
| --- |

## [◆ ](#afa309eb7291fd4416d3a5d0184991212)GD32\_CLOCK\_TIMER0

| #define GD32\_CLOCK\_TIMER0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 0U) |
| --- |

## [◆ ](#af084c2bf11ddfe04c80c3fac272c30e7)GD32\_CLOCK\_TIMER1

| #define GD32\_CLOCK\_TIMER1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 0U) |
| --- |

## [◆ ](#a7c3b4d23aac8844faac79f458cc5e07b)GD32\_CLOCK\_TIMER10

| #define GD32\_CLOCK\_TIMER10   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 18U) |
| --- |

## [◆ ](#afffce8951164061ccedc46edad527cf8)GD32\_CLOCK\_TIMER11

| #define GD32\_CLOCK\_TIMER11   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 6U) |
| --- |

## [◆ ](#a285a372dc49a8df0888813b08c8804ef)GD32\_CLOCK\_TIMER12

| #define GD32\_CLOCK\_TIMER12   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 7U) |
| --- |

## [◆ ](#a60bfa7bc6aafc012fa45b395d4d22c00)GD32\_CLOCK\_TIMER13

| #define GD32\_CLOCK\_TIMER13   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 8U) |
| --- |

## [◆ ](#a41623cb4499589163c0697a7a669ac25)GD32\_CLOCK\_TIMER2

| #define GD32\_CLOCK\_TIMER2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 1U) |
| --- |

## [◆ ](#afb5aa7f1705febd51a92f9370bd03d14)GD32\_CLOCK\_TIMER3

| #define GD32\_CLOCK\_TIMER3   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 2U) |
| --- |

## [◆ ](#a9d52a01572ab9309c5ebd3a0def8542f)GD32\_CLOCK\_TIMER4

| #define GD32\_CLOCK\_TIMER4   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 3U) |
| --- |

## [◆ ](#aae8d2c65bc590e7147407099e8a938b7)GD32\_CLOCK\_TIMER5

| #define GD32\_CLOCK\_TIMER5   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 4U) |
| --- |

## [◆ ](#a0e1b450d86f9e5b08a5738116742b429)GD32\_CLOCK\_TIMER6

| #define GD32\_CLOCK\_TIMER6   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 5U) |
| --- |

## [◆ ](#abb3f432fa2ef4e6c69a4c252493c0606)GD32\_CLOCK\_TIMER7

| #define GD32\_CLOCK\_TIMER7   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 1U) |
| --- |

## [◆ ](#adbac39fc1c001fbb14036f08c81810ef)GD32\_CLOCK\_TIMER8

| #define GD32\_CLOCK\_TIMER8   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 16U) |
| --- |

## [◆ ](#a3981da513ef2eb351b403f6dc11a2c6b)GD32\_CLOCK\_TIMER9

| #define GD32\_CLOCK\_TIMER9   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 17U) |
| --- |

## [◆ ](#ab04cbf84abb9f4923b6e9381c22bdae1)GD32\_CLOCK\_TLI

| #define GD32\_CLOCK\_TLI   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 26U) |
| --- |

## [◆ ](#ad7e9e9d34e7acca03e2538e1d5f52c0e)GD32\_CLOCK\_TRNG

| #define GD32\_CLOCK\_TRNG   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 6U) |
| --- |

## [◆ ](#a149bc461b6b4f81cafe38f9c7f40c8cd)GD32\_CLOCK\_UART3

| #define GD32\_CLOCK\_UART3   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 19U) |
| --- |

## [◆ ](#a82468e78744e139664daeb68f8f181da)GD32\_CLOCK\_UART4

| #define GD32\_CLOCK\_UART4   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 20U) |
| --- |

## [◆ ](#a8ec6e1dfab01b3652183c38eac160288)GD32\_CLOCK\_UART6

| #define GD32\_CLOCK\_UART6   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 30U) |
| --- |

## [◆ ](#a683cb88b874a2b6802bba5f99b85163e)GD32\_CLOCK\_UART7

| #define GD32\_CLOCK\_UART7   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 31U) |
| --- |

## [◆ ](#ac1599e50ad14746470268bc14aa04318)GD32\_CLOCK\_USART0

| #define GD32\_CLOCK\_USART0   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 4U) |
| --- |

## [◆ ](#a0f4528cfba6c9b129cc3aeae8220a178)GD32\_CLOCK\_USART1

| #define GD32\_CLOCK\_USART1   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 17U) |
| --- |

## [◆ ](#a477baf1c1a265b4c86019a5f52820622)GD32\_CLOCK\_USART2

| #define GD32\_CLOCK\_USART2   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 18U) |
| --- |

## [◆ ](#a736a4d8ae51d88226f8baeec49be4dc5)GD32\_CLOCK\_USART5

| #define GD32\_CLOCK\_USART5   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB2EN, 5U) |
| --- |

## [◆ ](#ae11c1f5ccf256d32377eb9a6f07026f2)GD32\_CLOCK\_USBFS

| #define GD32\_CLOCK\_USBFS   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB2EN, 7U) |
| --- |

## [◆ ](#a9bb9a4af2877fa954bda83bb8fbc39a6)GD32\_CLOCK\_USBHS

| #define GD32\_CLOCK\_USBHS   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 29U) |
| --- |

## [◆ ](#a921ac30c07db5ab957c001cc0cbbdd0d)GD32\_CLOCK\_USBHSULPI

| #define GD32\_CLOCK\_USBHSULPI   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(AHB1EN, 30U) |
| --- |

## [◆ ](#acd4e6949e5fb08e13129174ddd6f2e70)GD32\_CLOCK\_WWDGT

| #define GD32\_CLOCK\_WWDGT   [GD32\_CLOCK\_CONFIG](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)(APB1EN, 11U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32f4xx-clocks.h](gd32f4xx-clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
