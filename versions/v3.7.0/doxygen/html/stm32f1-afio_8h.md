---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32f1-afio_8h.html
original_path: doxygen/html/stm32f1-afio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1-afio.h File Reference

[Go to the source code of this file.](stm32f1-afio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_REMAP\_REG\_MASK](#ade5f8ba7372fa491075880f76e550b6c)   0x1U |
| #define | [STM32\_REMAP\_REG\_SHIFT](#acbb01f8e98a95fe5460465e4ca2ba3e0)   0U |
| #define | [STM32\_REMAP\_SHIFT\_MASK](#a3cebc2d1cda7877f745ea12092794223)   0x1FU |
| #define | [STM32\_REMAP\_SHIFT\_SHIFT](#a1e14e8db39fbc3e33132adc10ad7067d)   1U |
| #define | [STM32\_REMAP\_MASK\_MASK](#a6e9613bf8369a7d1efa96cb90345a97a)   0x3U |
| #define | [STM32\_REMAP\_MASK\_SHIFT](#a3ffdee2c3eb7a004285180731366c15d)   6U |
| #define | [STM32\_REMAP\_VAL\_MASK](#a9cb1b934dd4621ebfae5115459efbd6e)   0x3U |
| #define | [STM32\_REMAP\_VAL\_SHIFT](#a144bfbe208a98ddc641ff538aa4738cc)   8U |
| #define | [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(val, mask, shift, reg) |
|  | STM32F1 Remap configuration bit field. |
| #define | [STM32\_REMAP\_REG\_GET](#a9d21e2ff45da0e873e6c8d1012c001f5)(remap) |
|  | Obtain register field from remap configuration. |
| #define | [STM32\_REMAP\_SHIFT\_GET](#a7a61290a7587f5680a8ff183d1c2907d)(remap) |
|  | Obtain position field from remap configuration. |
| #define | [STM32\_REMAP\_MASK\_GET](#a71aeec8660001f84d3c55f426fdb7137)(remap) |
|  | Obtain mask field from remap configuration. |
| #define | [STM32\_REMAP\_VAL\_GET](#a60b741decc8673b9f9a99b7a05d5e9fc)(remap) |
|  | Obtain value field from remap configuration. |
| #define | [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)   0U |
| #define | [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)   1U |
| #define | [NO\_REMAP](#a1a8dfdc80d2d337f72699eca6ed3d957)   0 |
|  | Device not remappable. |
| #define | [SPI1\_REMAP0](#ae6f376590d4b2ec77260306a119ad235)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 0U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | SPI1 (no remap). |
| #define | [SPI1\_REMAP1](#ab655e58c31c71abbecb333cc6f91d9c4)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 0U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | SPI1 (remap). |
| #define | [I2C1\_REMAP0](#ad235d9e97ed9df493d76cd77f70ca951)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 1U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | I2C1 (no remap). |
| #define | [I2C1\_REMAP1](#a312613c6dc75976919fec8f63fcb2010)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 1U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | I2C1 (remap). |
| #define | [USART1\_REMAP0](#a5a79382b9eb0e4e502b8c84697a73433)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 2U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART1 (no remap). |
| #define | [USART1\_REMAP1](#ab002c165fc3d6a9e043164560a211f68)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 2U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART1 (remap). |
| #define | [USART2\_REMAP0](#afd7dc4010b32a1f10510cc39e1c911da)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 3U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART2 (no remap). |
| #define | [USART2\_REMAP1](#a472167bf97fff0caba80fe06a56b8084)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 3U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART2 (remap). |
| #define | [USART3\_REMAP0](#a45b45e1ad6629299c0efd15b2233cd0e)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 4U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART3 (no remap). |
| #define | [USART3\_REMAP1](#a3953583002841a586c85cbbb5d5fc931)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 4U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART3 (partial remap). |
| #define | [USART3\_REMAP2](#a9642c16b4169ed0552056f8ee638ceb2)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 4U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | USART3 (full remap). |
| #define | [TIM1\_REMAP0](#a65b1a18a202a22d8c9add530fd0a8313)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 6U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM1 (no remap). |
| #define | [TIM1\_REMAP1](#aa7a6c64fab50803704cfc5f6a3fe4c9f)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 6U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM1 (partial remap). |
| #define | [TIM1\_REMAP2](#a8de28395b1ecc659fbe3e4b33a8aaf76)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 6U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM1 (full remap). |
| #define | [TIM2\_REMAP0](#a9ac0bc54a91246b78d863ba3a215ea96)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM2 (no remap). |
| #define | [TIM2\_REMAP1](#a6fad8ce0389fa7b6d5a80c501ed99ce9)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM2 (partial remap 1). |
| #define | [TIM2\_REMAP2](#ae47bd66bc1f02dc89a624c7639ad492b)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(2U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM2 (partial remap 2). |
| #define | [TIM2\_REMAP3](#ae3739bffc6fef7ca2aed06327fe26259)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM2 (full remap). |
| #define | [TIM3\_REMAP0](#a535bdd60f1276bf660814c665c3ca349)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM3 (no remap). |
| #define | [TIM3\_REMAP1](#a068f135e7a2273b9eab28b934b0a7e53)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM3 (partial remap 1). |
| #define | [TIM3\_REMAP2](#a5c8aa22a44a0b6ef2fbc169aeebdc2ea)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(2U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM3 (partial remap 2). |
| #define | [TIM3\_REMAP3](#a811f621a99ec1b18a4b5fd4e52456a9f)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM3 (full remap). |
| #define | [TIM4\_REMAP0](#af19b67747576ad37c76dccc4c8a1ea16)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 12U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM4 (no remap). |
| #define | [TIM4\_REMAP1](#aafb51d9eacaf920f3c78425ecaf5478e)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 12U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | TIM4 (remap). |
| #define | [CAN\_REMAP0](#a6e8abc893ec0c03751427ff220eaf34a)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 13U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | CAN (no remap). |
| #define | [CAN\_REMAP1](#a20407640b3d6f5a1c326546a8b3a10e9)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(2U, 0x3U, 13U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | CAN (partial remap). |
| #define | [CAN\_REMAP2](#aa1aaf1eeddccdbfd3621145c709dc48d)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 13U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | CAN (full remap). |
| #define | [CAN1\_REMAP0](#a536898ad320fddd9754cca453f1b9223)   [CAN\_REMAP0](#a6e8abc893ec0c03751427ff220eaf34a) |
|  | CAN1 alias. |
| #define | [CAN1\_REMAP1](#a5b032fc54211b2ac4964bc924f09a75d)   [CAN\_REMAP1](#a20407640b3d6f5a1c326546a8b3a10e9) |
| #define | [CAN1\_REMAP2](#ab16bbfb04e8b2b73bdd560a9a14c4df1)   [CAN\_REMAP2](#aa1aaf1eeddccdbfd3621145c709dc48d) |
| #define | [ETH\_REMAP0](#a663f8f668fe27ac44a70990db3d19a40)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 21U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | ETH (no remap). |
| #define | [ETH\_REMAP1](#abcf6340d39300d1c33b0592160614de9)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 21U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | ETH (remap). |
| #define | [CAN2\_REMAP0](#a1c2991b25909c6297e22542cfa418548)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 22U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | CAN2 (no remap). |
| #define | [CAN2\_REMAP1](#aa048c7e4fb84a22c8ad40e9c0fc5e51a)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 22U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | CAN2 (remap). |
| #define | [SPI3\_REMAP0](#a7dcb5bfc48d08c9d4dbe793b8d232a45)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 28U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | SPI3 (no remap). |
| #define | [SPI3\_REMAP1](#a401e4124c07719248294b0ee08ebc83c)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 28U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
|  | SPI3 (remap). |
| #define | [I2S3\_REMAP0](#ac3b499810e4bcae2211adb6c02eb7815)   [SPI3\_REMAP0](#a7dcb5bfc48d08c9d4dbe793b8d232a45) |
|  | I2S3 (SPI3) (no remap). |
| #define | [I2S3\_REMAP1](#a47c88171fa34dbd74f7c163a9227ae28)   [SPI3\_REMAP1](#a401e4124c07719248294b0ee08ebc83c) |
|  | I2S3 (SPI3) (remap). |
| #define | [TIM9\_REMAP0](#a075dc7fea001772986dfe31d9d9e8f9a)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 5U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM9 (no remap). |
| #define | [TIM9\_REMAP1](#ad443ec934247e04996bf85b5ce9ef721)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 5U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM9 (remap). |
| #define | [TIM10\_REMAP0](#af5450df359cf37725a34f89b1af168e7)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 6U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM10 (no remap). |
| #define | [TIM10\_REMAP1](#a691a581fe6dd08fd9a5a048abc5eaa3e)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 6U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM10 (remap). |
| #define | [TIM11\_REMAP0](#a01e4adf5326f92d144d45ba4b898ed8e)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 7U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM11 (no remap). |
| #define | [TIM11\_REMAP1](#a7dcef4a23add63b6eb1254e6146dbe71)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 7U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM11 (remap). |
| #define | [TIM13\_REMAP0](#a2a6704eee24037ee9edd3873a5245ea0)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 8U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM13 (no remap). |
| #define | [TIM13\_REMAP1](#acdcdd0184a5d75722dd1cbdbe2f8212f)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 8U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM13 (remap). |
| #define | [TIM14\_REMAP0](#a6c0341b14e851b4093e72932d05de5f5)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 9U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM14 (no remap). |
| #define | [TIM14\_REMAP1](#ab047fa455523413d447f676fe9907c84)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 9U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM14 (remap). |
| #define | [TIM15\_REMAP0](#aa7da41d73e1ab29fef6020695f32f773)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 0U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM15 (no remap). |
| #define | [TIM15\_REMAP1](#a87f392ac52f61d12709744f1ae8470af)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 0U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM15 (remap). |
| #define | [TIM16\_REMAP0](#a26d271515c8666e49cff39a1e5bb8112)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 1U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM16 (no remap). |
| #define | [TIM16\_REMAP1](#a9459d0003315751cc5969c7ce1146947)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 1U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM16 (remap). |
| #define | [TIM17\_REMAP0](#a0c0e509d60821ac498a4fa03c4d5a47b)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 2U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM17 (no remap). |
| #define | [TIM17\_REMAP1](#ae5da6d9ae0c81a39ba7c7f51135be110)   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 2U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
|  | TIM17 (remap). |

## Macro Definition Documentation

## [◆ ](#a536898ad320fddd9754cca453f1b9223)CAN1\_REMAP0

| #define CAN1\_REMAP0   [CAN\_REMAP0](#a6e8abc893ec0c03751427ff220eaf34a) |
| --- |

CAN1 alias.

## [◆ ](#a5b032fc54211b2ac4964bc924f09a75d)CAN1\_REMAP1

| #define CAN1\_REMAP1   [CAN\_REMAP1](#a20407640b3d6f5a1c326546a8b3a10e9) |
| --- |

## [◆ ](#ab16bbfb04e8b2b73bdd560a9a14c4df1)CAN1\_REMAP2

| #define CAN1\_REMAP2   [CAN\_REMAP2](#aa1aaf1eeddccdbfd3621145c709dc48d) |
| --- |

## [◆ ](#a1c2991b25909c6297e22542cfa418548)CAN2\_REMAP0

| #define CAN2\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 22U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

CAN2 (no remap).

## [◆ ](#aa048c7e4fb84a22c8ad40e9c0fc5e51a)CAN2\_REMAP1

| #define CAN2\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 22U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

CAN2 (remap).

## [◆ ](#a6e8abc893ec0c03751427ff220eaf34a)CAN\_REMAP0

| #define CAN\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 13U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

CAN (no remap).

## [◆ ](#a20407640b3d6f5a1c326546a8b3a10e9)CAN\_REMAP1

| #define CAN\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(2U, 0x3U, 13U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

CAN (partial remap).

## [◆ ](#aa1aaf1eeddccdbfd3621145c709dc48d)CAN\_REMAP2

| #define CAN\_REMAP2   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 13U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

CAN (full remap).

## [◆ ](#a663f8f668fe27ac44a70990db3d19a40)ETH\_REMAP0

| #define ETH\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 21U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

ETH (no remap).

## [◆ ](#abcf6340d39300d1c33b0592160614de9)ETH\_REMAP1

| #define ETH\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 21U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

ETH (remap).

## [◆ ](#ad235d9e97ed9df493d76cd77f70ca951)I2C1\_REMAP0

| #define I2C1\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 1U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

I2C1 (no remap).

## [◆ ](#a312613c6dc75976919fec8f63fcb2010)I2C1\_REMAP1

| #define I2C1\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 1U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

I2C1 (remap).

## [◆ ](#ac3b499810e4bcae2211adb6c02eb7815)I2S3\_REMAP0

| #define I2S3\_REMAP0   [SPI3\_REMAP0](#a7dcb5bfc48d08c9d4dbe793b8d232a45) |
| --- |

I2S3 (SPI3) (no remap).

## [◆ ](#a47c88171fa34dbd74f7c163a9227ae28)I2S3\_REMAP1

| #define I2S3\_REMAP1   [SPI3\_REMAP1](#a401e4124c07719248294b0ee08ebc83c) |
| --- |

I2S3 (SPI3) (remap).

## [◆ ](#a1a8dfdc80d2d337f72699eca6ed3d957)NO\_REMAP

| #define NO\_REMAP   0 |
| --- |

Device not remappable.

## [◆ ](#ae6f376590d4b2ec77260306a119ad235)SPI1\_REMAP0

| #define SPI1\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 0U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

SPI1 (no remap).

## [◆ ](#ab655e58c31c71abbecb333cc6f91d9c4)SPI1\_REMAP1

| #define SPI1\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 0U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

SPI1 (remap).

## [◆ ](#a7dcb5bfc48d08c9d4dbe793b8d232a45)SPI3\_REMAP0

| #define SPI3\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 28U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

SPI3 (no remap).

## [◆ ](#a401e4124c07719248294b0ee08ebc83c)SPI3\_REMAP1

| #define SPI3\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 28U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

SPI3 (remap).

## [◆ ](#a2c91303d8a35d5fcbfa8621173d3fe07)STM32\_AFIO\_MAPR

| #define STM32\_AFIO\_MAPR   0U |
| --- |

## [◆ ](#aa60a0ba8748fc37c64efcd19947e664e)STM32\_AFIO\_MAPR2

| #define STM32\_AFIO\_MAPR2   1U |
| --- |

## [◆ ](#a200a3a748707c11bfd3129c16fc6a835)STM32\_REMAP

| #define STM32\_REMAP | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *shift*, |
|  |  |  | *reg* ) |

**Value:**

((((reg) & [STM32\_REMAP\_REG\_MASK](#ade5f8ba7372fa491075880f76e550b6c)) << [STM32\_REMAP\_REG\_SHIFT](#acbb01f8e98a95fe5460465e4ca2ba3e0)) | \

(((shift) & [STM32\_REMAP\_SHIFT\_MASK](#a3cebc2d1cda7877f745ea12092794223)) << [STM32\_REMAP\_SHIFT\_SHIFT](#a1e14e8db39fbc3e33132adc10ad7067d)) | \

(((mask) & [STM32\_REMAP\_MASK\_MASK](#a6e9613bf8369a7d1efa96cb90345a97a)) << [STM32\_REMAP\_MASK\_SHIFT](#a3ffdee2c3eb7a004285180731366c15d)) | \

(((val) & [STM32\_REMAP\_VAL\_MASK](#a9cb1b934dd4621ebfae5115459efbd6e)) << [STM32\_REMAP\_VAL\_SHIFT](#a144bfbe208a98ddc641ff538aa4738cc)))

[STM32\_REMAP\_VAL\_SHIFT](#a144bfbe208a98ddc641ff538aa4738cc)

#define STM32\_REMAP\_VAL\_SHIFT

**Definition** stm32f1-afio.h:17

[STM32\_REMAP\_SHIFT\_SHIFT](#a1e14e8db39fbc3e33132adc10ad7067d)

#define STM32\_REMAP\_SHIFT\_SHIFT

**Definition** stm32f1-afio.h:13

[STM32\_REMAP\_SHIFT\_MASK](#a3cebc2d1cda7877f745ea12092794223)

#define STM32\_REMAP\_SHIFT\_MASK

**Definition** stm32f1-afio.h:12

[STM32\_REMAP\_MASK\_SHIFT](#a3ffdee2c3eb7a004285180731366c15d)

#define STM32\_REMAP\_MASK\_SHIFT

**Definition** stm32f1-afio.h:15

[STM32\_REMAP\_MASK\_MASK](#a6e9613bf8369a7d1efa96cb90345a97a)

#define STM32\_REMAP\_MASK\_MASK

**Definition** stm32f1-afio.h:14

[STM32\_REMAP\_VAL\_MASK](#a9cb1b934dd4621ebfae5115459efbd6e)

#define STM32\_REMAP\_VAL\_MASK

**Definition** stm32f1-afio.h:16

[STM32\_REMAP\_REG\_SHIFT](#acbb01f8e98a95fe5460465e4ca2ba3e0)

#define STM32\_REMAP\_REG\_SHIFT

**Definition** stm32f1-afio.h:11

[STM32\_REMAP\_REG\_MASK](#ade5f8ba7372fa491075880f76e550b6c)

#define STM32\_REMAP\_REG\_MASK

**Definition** stm32f1-afio.h:10

STM32F1 Remap configuration bit field.

- reg (0/1) [ 0 : 0 ]
- shift (0..31) [ 1 : 5 ]
- mask (0x1, 0x3) [ 6 : 7 ]
- val (0..3) [ 8 : 9 ]

Parameters
:   | reg | AFIO\_MAPRx register (MAPR, MAPR2). |
    | --- | --- |
    | shift | Position within AFIO\_MAPRx. |
    | mask | Mask for the AFIO\_MAPRx field. |
    | val | Remap value (0, 1, 2 or 3). |

## [◆ ](#a71aeec8660001f84d3c55f426fdb7137)STM32\_REMAP\_MASK\_GET

| #define STM32\_REMAP\_MASK\_GET | ( |  | *remap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((remap) >> [STM32\_REMAP\_MASK\_SHIFT](#a3ffdee2c3eb7a004285180731366c15d)) & [STM32\_REMAP\_MASK\_MASK](#a6e9613bf8369a7d1efa96cb90345a97a))

Obtain mask field from remap configuration.

Parameters
:   | remap | Remap bit field value. |
    | --- | --- |

## [◆ ](#a6e9613bf8369a7d1efa96cb90345a97a)STM32\_REMAP\_MASK\_MASK

| #define STM32\_REMAP\_MASK\_MASK   0x3U |
| --- |

## [◆ ](#a3ffdee2c3eb7a004285180731366c15d)STM32\_REMAP\_MASK\_SHIFT

| #define STM32\_REMAP\_MASK\_SHIFT   6U |
| --- |

## [◆ ](#a9d21e2ff45da0e873e6c8d1012c001f5)STM32\_REMAP\_REG\_GET

| #define STM32\_REMAP\_REG\_GET | ( |  | *remap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((remap) >> [STM32\_REMAP\_REG\_SHIFT](#acbb01f8e98a95fe5460465e4ca2ba3e0)) & [STM32\_REMAP\_REG\_MASK](#ade5f8ba7372fa491075880f76e550b6c))

Obtain register field from remap configuration.

Parameters
:   | remap | Remap bit field value. |
    | --- | --- |

## [◆ ](#ade5f8ba7372fa491075880f76e550b6c)STM32\_REMAP\_REG\_MASK

| #define STM32\_REMAP\_REG\_MASK   0x1U |
| --- |

## [◆ ](#acbb01f8e98a95fe5460465e4ca2ba3e0)STM32\_REMAP\_REG\_SHIFT

| #define STM32\_REMAP\_REG\_SHIFT   0U |
| --- |

## [◆ ](#a7a61290a7587f5680a8ff183d1c2907d)STM32\_REMAP\_SHIFT\_GET

| #define STM32\_REMAP\_SHIFT\_GET | ( |  | *remap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((remap) >> [STM32\_REMAP\_SHIFT\_SHIFT](#a1e14e8db39fbc3e33132adc10ad7067d)) & [STM32\_REMAP\_SHIFT\_MASK](#a3cebc2d1cda7877f745ea12092794223))

Obtain position field from remap configuration.

Parameters
:   | remap | Remap bit field value. |
    | --- | --- |

## [◆ ](#a3cebc2d1cda7877f745ea12092794223)STM32\_REMAP\_SHIFT\_MASK

| #define STM32\_REMAP\_SHIFT\_MASK   0x1FU |
| --- |

## [◆ ](#a1e14e8db39fbc3e33132adc10ad7067d)STM32\_REMAP\_SHIFT\_SHIFT

| #define STM32\_REMAP\_SHIFT\_SHIFT   1U |
| --- |

## [◆ ](#a60b741decc8673b9f9a99b7a05d5e9fc)STM32\_REMAP\_VAL\_GET

| #define STM32\_REMAP\_VAL\_GET | ( |  | *remap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((remap) >> [STM32\_REMAP\_VAL\_SHIFT](#a144bfbe208a98ddc641ff538aa4738cc)) & [STM32\_REMAP\_VAL\_MASK](#a9cb1b934dd4621ebfae5115459efbd6e))

Obtain value field from remap configuration.

Parameters
:   | remap | Remap bit field value. |
    | --- | --- |

## [◆ ](#a9cb1b934dd4621ebfae5115459efbd6e)STM32\_REMAP\_VAL\_MASK

| #define STM32\_REMAP\_VAL\_MASK   0x3U |
| --- |

## [◆ ](#a144bfbe208a98ddc641ff538aa4738cc)STM32\_REMAP\_VAL\_SHIFT

| #define STM32\_REMAP\_VAL\_SHIFT   8U |
| --- |

## [◆ ](#af5450df359cf37725a34f89b1af168e7)TIM10\_REMAP0

| #define TIM10\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 6U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM10 (no remap).

## [◆ ](#a691a581fe6dd08fd9a5a048abc5eaa3e)TIM10\_REMAP1

| #define TIM10\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 6U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM10 (remap).

## [◆ ](#a01e4adf5326f92d144d45ba4b898ed8e)TIM11\_REMAP0

| #define TIM11\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 7U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM11 (no remap).

## [◆ ](#a7dcef4a23add63b6eb1254e6146dbe71)TIM11\_REMAP1

| #define TIM11\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 7U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM11 (remap).

## [◆ ](#a2a6704eee24037ee9edd3873a5245ea0)TIM13\_REMAP0

| #define TIM13\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 8U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM13 (no remap).

## [◆ ](#acdcdd0184a5d75722dd1cbdbe2f8212f)TIM13\_REMAP1

| #define TIM13\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 8U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM13 (remap).

## [◆ ](#a6c0341b14e851b4093e72932d05de5f5)TIM14\_REMAP0

| #define TIM14\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 9U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM14 (no remap).

## [◆ ](#ab047fa455523413d447f676fe9907c84)TIM14\_REMAP1

| #define TIM14\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 9U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM14 (remap).

## [◆ ](#aa7da41d73e1ab29fef6020695f32f773)TIM15\_REMAP0

| #define TIM15\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 0U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM15 (no remap).

## [◆ ](#a87f392ac52f61d12709744f1ae8470af)TIM15\_REMAP1

| #define TIM15\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 0U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM15 (remap).

## [◆ ](#a26d271515c8666e49cff39a1e5bb8112)TIM16\_REMAP0

| #define TIM16\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 1U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM16 (no remap).

## [◆ ](#a9459d0003315751cc5969c7ce1146947)TIM16\_REMAP1

| #define TIM16\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 1U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM16 (remap).

## [◆ ](#a0c0e509d60821ac498a4fa03c4d5a47b)TIM17\_REMAP0

| #define TIM17\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 2U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM17 (no remap).

## [◆ ](#ae5da6d9ae0c81a39ba7c7f51135be110)TIM17\_REMAP1

| #define TIM17\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 2U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM17 (remap).

## [◆ ](#a65b1a18a202a22d8c9add530fd0a8313)TIM1\_REMAP0

| #define TIM1\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 6U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM1 (no remap).

## [◆ ](#aa7a6c64fab50803704cfc5f6a3fe4c9f)TIM1\_REMAP1

| #define TIM1\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 6U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM1 (partial remap).

## [◆ ](#a8de28395b1ecc659fbe3e4b33a8aaf76)TIM1\_REMAP2

| #define TIM1\_REMAP2   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 6U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM1 (full remap).

## [◆ ](#a9ac0bc54a91246b78d863ba3a215ea96)TIM2\_REMAP0

| #define TIM2\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM2 (no remap).

## [◆ ](#a6fad8ce0389fa7b6d5a80c501ed99ce9)TIM2\_REMAP1

| #define TIM2\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM2 (partial remap 1).

## [◆ ](#ae47bd66bc1f02dc89a624c7639ad492b)TIM2\_REMAP2

| #define TIM2\_REMAP2   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(2U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM2 (partial remap 2).

## [◆ ](#ae3739bffc6fef7ca2aed06327fe26259)TIM2\_REMAP3

| #define TIM2\_REMAP3   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 8U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM2 (full remap).

## [◆ ](#a535bdd60f1276bf660814c665c3ca349)TIM3\_REMAP0

| #define TIM3\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM3 (no remap).

## [◆ ](#a068f135e7a2273b9eab28b934b0a7e53)TIM3\_REMAP1

| #define TIM3\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM3 (partial remap 1).

## [◆ ](#a5c8aa22a44a0b6ef2fbc169aeebdc2ea)TIM3\_REMAP2

| #define TIM3\_REMAP2   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(2U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM3 (partial remap 2).

## [◆ ](#a811f621a99ec1b18a4b5fd4e52456a9f)TIM3\_REMAP3

| #define TIM3\_REMAP3   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 10U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM3 (full remap).

## [◆ ](#af19b67747576ad37c76dccc4c8a1ea16)TIM4\_REMAP0

| #define TIM4\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 12U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM4 (no remap).

## [◆ ](#aafb51d9eacaf920f3c78425ecaf5478e)TIM4\_REMAP1

| #define TIM4\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 12U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

TIM4 (remap).

## [◆ ](#a075dc7fea001772986dfe31d9d9e8f9a)TIM9\_REMAP0

| #define TIM9\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 5U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM9 (no remap).

## [◆ ](#ad443ec934247e04996bf85b5ce9ef721)TIM9\_REMAP1

| #define TIM9\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 5U, [STM32\_AFIO\_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)) |
| --- |

TIM9 (remap).

## [◆ ](#a5a79382b9eb0e4e502b8c84697a73433)USART1\_REMAP0

| #define USART1\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 2U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART1 (no remap).

## [◆ ](#ab002c165fc3d6a9e043164560a211f68)USART1\_REMAP1

| #define USART1\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 2U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART1 (remap).

## [◆ ](#afd7dc4010b32a1f10510cc39e1c911da)USART2\_REMAP0

| #define USART2\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x1U, 3U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART2 (no remap).

## [◆ ](#a472167bf97fff0caba80fe06a56b8084)USART2\_REMAP1

| #define USART2\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x1U, 3U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART2 (remap).

## [◆ ](#a45b45e1ad6629299c0efd15b2233cd0e)USART3\_REMAP0

| #define USART3\_REMAP0   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(0U, 0x3U, 4U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART3 (no remap).

## [◆ ](#a3953583002841a586c85cbbb5d5fc931)USART3\_REMAP1

| #define USART3\_REMAP1   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(1U, 0x3U, 4U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART3 (partial remap).

## [◆ ](#a9642c16b4169ed0552056f8ee638ceb2)USART3\_REMAP2

| #define USART3\_REMAP2   [STM32\_REMAP](#a200a3a748707c11bfd3129c16fc6a835)(3U, 0x3U, 4U, [STM32\_AFIO\_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)) |
| --- |

USART3 (full remap).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32f1-afio.h](stm32f1-afio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
