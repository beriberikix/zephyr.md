---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32h5__clock_8h.html
original_path: doxygen/html/stm32h5__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h5\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32h5__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_CSI](#ac1c5062f5053fe96a5c2ba12d868eeda)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_CSI](#ac1c5062f5053fe96a5c2ba12d868eeda) + 1) |
| #define | [STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| #define | [STM32\_SRC\_HCLK](#a2c2165a735dc0763cd972d464ececc5d)   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
|  | Bus clock. |
| #define | [STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831)   ([STM32\_SRC\_HCLK](#a2c2165a735dc0763cd972d464ececc5d) + 1) |
| #define | [STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3)   ([STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831) + 1) |
| #define | [STM32\_SRC\_PCLK3](#ae54654dc761dca391f56e95ebd6db625)   ([STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3) + 1) |
| #define | [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62)   ([STM32\_SRC\_PCLK3](#ae54654dc761dca391f56e95ebd6db625) + 1) |
|  | PLL outputs. |
| #define | [STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637)   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| #define | [STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9)   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| #define | [STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac)   ([STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9) + 1) |
| #define | [STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717)   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| #define | [STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd)   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| #define | [STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206)   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| #define | [STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9)   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| #define | [STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a)   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| #define | [STM32\_SRC\_CKPER](#a8b7025d7f4be00a152c53097a414668e)   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
|  | Clock muxes. |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x088 |
|  | Bus clocks. |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x08C |
| #define | [STM32\_CLOCK\_BUS\_AHB4](#a49bccabc3065f192086f16929a7b762d)   0x094 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x09c |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x0A0 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x0A4 |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x0A8 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| #define | [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2)   0xD8 |
|  | RCC\_CCIPRx register offset (RM0456.pdf). |
| #define | [CCIPR2\_REG](#a60349691a29a48b727f302acb8025b89)   0xDC |
| #define | [CCIPR3\_REG](#a302577067fac290b578130da822dc146)   0xE0 |
| #define | [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723)   0xE4 |
| #define | [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148)   0xE8 |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0xF0 |
|  | RCC\_BDCR register offset. |
| #define | [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)   0x1C |
|  | RCC\_CFGRx register offset. |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device domain clocks selection helpers. |
| #define | [USART2\_SEL](#ad67d92dfc439018a7a231e661d10d7f9)(val) |
| #define | [USART3\_SEL](#ad2f356c0bc0e43d6f629cdb840846526)(val) |
| #define | [USART4\_SEL](#aced9e983095cb40bc18f3a66e3818c98)(val) |
| #define | [USART5\_SEL](#a6a45e0ef8bd196574e241aefdb3a5350)(val) |
| #define | [USART6\_SEL](#a99c9026d61766ec9b91872ee64ad63eb)(val) |
| #define | [USART7\_SEL](#a085ea149cac54d39aef4cb9f5c03402c)(val) |
| #define | [USART8\_SEL](#adf99875c4c7a62e255871678fe848645)(val) |
| #define | [USART9\_SEL](#a2bb43ceb46c7cb47f946c868a9e5b0aa)(val) |
| #define | [USART10\_SEL](#a5eef37bd8c6a90bf0de08faf5d05f410)(val) |
| #define | [TIMIC\_SEL](#ad39b85aaa947648b1b833b1414116f51)(val) |
| #define | [USART11\_SEL](#adc9bd02facff6c4513f4fe8cb43fe9be)(val) |
|  | CCIPR2 devices. |
| #define | [USART12\_SEL](#a2ce5c32e9d923116b1ef96e415876866)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [LPTIM3\_SEL](#ac705aa5789ca3b11ac5115d22ec2a5e5)(val) |
| #define | [LPTIM4\_SEL](#a7c23812b481c3743f393d301d7cf7e27)(val) |
| #define | [LPTIM5\_SEL](#ad508257c2f92e7ced0f6317ea3397965)(val) |
| #define | [LPTIM6\_SEL](#a6ed1256c9ec56f7377d16aa4993379b1)(val) |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
|  | CCIPR3 devices. |
| #define | [SPI2\_SEL](#ad3e84eac634b9d943acea9b2ab884fb5)(val) |
| #define | [SPI3\_SEL](#aaa096904d8a97bedc81f9a565e65c332)(val) |
| #define | [SPI4\_SEL](#a55086a94321a6e1af527a46c644f6c5e)(val) |
| #define | [SPI5\_SEL](#ac7193e508815171a4d73795d24086136)(val) |
| #define | [SPI6\_SEL](#ab43d49ec71267eb1d8002909cc3360bf)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
| #define | [OCTOSPI1\_SEL](#a50fd0ec19b392357f55331cc031b34fd)(val) |
|  | CCIPR4 devices. |
| #define | [SYSTICK\_SEL](#a9319a91fb044022ba812f616cf192f65)(val) |
| #define | [USB\_SEL](#a3247ad782f1e2c7db84989d03831139b)(val) |
| #define | [SDMMC1\_SEL](#a1a4999da331afff86581c8a6cea6afe9)(val) |
| #define | [SDMMC2\_SEL](#a7319710d63129ad13039565cad2b4950)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C2\_SEL](#abdd79c9ce90458b53e81123d181fed98)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [I2C4\_SEL](#a55880006ae28021de4d148924c06001e)(val) |
| #define | [I3C1\_SEL](#a576dca08c22370326fefc540bf056b81)(val) |
| #define | [ADCDAC\_SEL](#a454d6254cea3749ac4502fb51739e27c)(val) |
|  | CCIPR5 devices. |
| #define | [DAC\_SEL](#a08f184d6404d9982facc8fe8a92ed5a8)(val) |
| #define | [RNG\_SEL](#abfff4355a498febbcf4ebcb237930a57)(val) |
| #define | [CEC\_SEL](#affd653e901474991857a29deba53cf82)(val) |
| #define | [FDCAN\_SEL](#ac1df6369669b4b3febd0525426e76499)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [SAI2\_SEL](#a4fb9a6b79339e822f0ae426e8bba7486)(val) |
| #define | [CKPER\_SEL](#adc32e4d489d72766d6df1783eedf7628)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR1 devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MCO2\_PRE](#ab02a0ccbb8588979ca4742c72c59589f)(val) |
| #define | [MCO\_PRE\_DIV\_1](#aa6d6446aa7a1c84324475f6e8665fbb7)   1 |
| #define | [MCO\_PRE\_DIV\_2](#a36db847c7932669759f64844a15c42c3)   2 |
| #define | [MCO\_PRE\_DIV\_3](#a1d99057b6886474182adffcff4f246f2)   3 |
| #define | [MCO\_PRE\_DIV\_4](#a74c5b485d9169c489ab19e788b43c657)   4 |
| #define | [MCO\_PRE\_DIV\_5](#aad3773cb5fbea15e6cddf688dea3cd04)   5 |
| #define | [MCO\_PRE\_DIV\_6](#a3cb780fda9d369607e1c51a7cddff300)   6 |
| #define | [MCO\_PRE\_DIV\_7](#a08634986618842af08073f59c6da3e8f)   7 |
| #define | [MCO\_PRE\_DIV\_8](#ad1bb69ff2fe6748978c31666f201947c)   8 |
| #define | [MCO\_PRE\_DIV\_9](#a7841c7ceb21754059717c5996a081cb4)   9 |
| #define | [MCO\_PRE\_DIV\_10](#aecc309343fad5680088593eff549748c)   10 |
| #define | [MCO\_PRE\_DIV\_11](#a3c4b271ad0c50ec7eb9edd779c30b3d9)   11 |
| #define | [MCO\_PRE\_DIV\_12](#aa93517f599cd367844383018b962319f)   12 |
| #define | [MCO\_PRE\_DIV\_13](#a3fcce904cb4650ec093f4aba0a8b7a51)   13 |
| #define | [MCO\_PRE\_DIV\_14](#aff3b9f97c2b1b70f090a7c27ca57ca58)   14 |
| #define | [MCO\_PRE\_DIV\_15](#affa380b0a33facd4d5fdd9dc405c6ddc)   15 |

## Macro Definition Documentation

## [◆ ](#a454d6254cea3749ac4502fb51739e27c)ADCDAC\_SEL

| #define ADCDAC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148)

#define CCIPR5\_REG

**Definition** stm32h5\_clock.h:59

CCIPR5 devices.

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0xF0 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#a5a41b990eca365907d09bb4416fb22d2)CCIPR1\_REG

| #define CCIPR1\_REG   0xD8 |
| --- |

RCC\_CCIPRx register offset (RM0456.pdf).

## [◆ ](#a60349691a29a48b727f302acb8025b89)CCIPR2\_REG

| #define CCIPR2\_REG   0xDC |
| --- |

## [◆ ](#a302577067fac290b578130da822dc146)CCIPR3\_REG

| #define CCIPR3\_REG   0xE0 |
| --- |

## [◆ ](#a92eb5c50a767e0f704356d52398f9723)CCIPR4\_REG

| #define CCIPR4\_REG   0xE4 |
| --- |

## [◆ ](#a62e39113c018ae0b2c31254ff003d148)CCIPR5\_REG

| #define CCIPR5\_REG   0xE8 |
| --- |

## [◆ ](#affd653e901474991857a29deba53cf82)CEC\_SEL

| #define CEC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 6, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a6b894fe6e036f03831faddf28bce43c6)CFGR1\_REG

| #define CFGR1\_REG   0x1C |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#adc32e4d489d72766d6df1783eedf7628)CKPER\_SEL

| #define CKPER\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 30, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a08f184d6404d9982facc8fe8a92ed5a8)DAC\_SEL

| #define DAC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 3, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#ac1df6369669b4b3febd0525426e76499)FDCAN\_SEL

| #define FDCAN\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 16, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

[CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723)

#define CCIPR4\_REG

**Definition** stm32h5\_clock.h:58

## [◆ ](#abdd79c9ce90458b53e81123d181fed98)I2C2\_SEL

| #define I2C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 18, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 20, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a55880006ae28021de4d148924c06001e)I2C4\_SEL

| #define I2C4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 22, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a576dca08c22370326fefc540bf056b81)I3C1\_SEL

| #define I3C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 24, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

[CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89)

#define CCIPR2\_REG

**Definition** stm32g0\_clock.h:40

## [◆ ](#aa713f6ff001bfa6352747e7a66e3f98a)LPTIM2\_SEL

| #define LPTIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#ac705aa5789ca3b11ac5115d22ec2a5e5)LPTIM3\_SEL

| #define LPTIM3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a7c23812b481c3743f393d301d7cf7e27)LPTIM4\_SEL

| #define LPTIM4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#ad508257c2f92e7ced0f6317ea3397965)LPTIM5\_SEL

| #define LPTIM5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a6ed1256c9ec56f7377d16aa4993379b1)LPTIM6\_SEL

| #define LPTIM6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 28, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR3\_REG](#a302577067fac290b578130da822dc146))

[CCIPR3\_REG](#a302577067fac290b578130da822dc146)

#define CCIPR3\_REG

**Definition** stm32h5\_clock.h:57

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xF, 18, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

[CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:39

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 22, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

CFGR1 devices.

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xF, 29, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 25, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

## [◆ ](#aa6d6446aa7a1c84324475f6e8665fbb7)MCO\_PRE\_DIV\_1

| #define MCO\_PRE\_DIV\_1   1 |
| --- |

## [◆ ](#aecc309343fad5680088593eff549748c)MCO\_PRE\_DIV\_10

| #define MCO\_PRE\_DIV\_10   10 |
| --- |

## [◆ ](#a3c4b271ad0c50ec7eb9edd779c30b3d9)MCO\_PRE\_DIV\_11

| #define MCO\_PRE\_DIV\_11   11 |
| --- |

## [◆ ](#aa93517f599cd367844383018b962319f)MCO\_PRE\_DIV\_12

| #define MCO\_PRE\_DIV\_12   12 |
| --- |

## [◆ ](#a3fcce904cb4650ec093f4aba0a8b7a51)MCO\_PRE\_DIV\_13

| #define MCO\_PRE\_DIV\_13   13 |
| --- |

## [◆ ](#aff3b9f97c2b1b70f090a7c27ca57ca58)MCO\_PRE\_DIV\_14

| #define MCO\_PRE\_DIV\_14   14 |
| --- |

## [◆ ](#affa380b0a33facd4d5fdd9dc405c6ddc)MCO\_PRE\_DIV\_15

| #define MCO\_PRE\_DIV\_15   15 |
| --- |

## [◆ ](#a36db847c7932669759f64844a15c42c3)MCO\_PRE\_DIV\_2

| #define MCO\_PRE\_DIV\_2   2 |
| --- |

## [◆ ](#a1d99057b6886474182adffcff4f246f2)MCO\_PRE\_DIV\_3

| #define MCO\_PRE\_DIV\_3   3 |
| --- |

## [◆ ](#a74c5b485d9169c489ab19e788b43c657)MCO\_PRE\_DIV\_4

| #define MCO\_PRE\_DIV\_4   4 |
| --- |

## [◆ ](#aad3773cb5fbea15e6cddf688dea3cd04)MCO\_PRE\_DIV\_5

| #define MCO\_PRE\_DIV\_5   5 |
| --- |

## [◆ ](#a3cb780fda9d369607e1c51a7cddff300)MCO\_PRE\_DIV\_6

| #define MCO\_PRE\_DIV\_6   6 |
| --- |

## [◆ ](#a08634986618842af08073f59c6da3e8f)MCO\_PRE\_DIV\_7

| #define MCO\_PRE\_DIV\_7   7 |
| --- |

## [◆ ](#ad1bb69ff2fe6748978c31666f201947c)MCO\_PRE\_DIV\_8

| #define MCO\_PRE\_DIV\_8   8 |
| --- |

## [◆ ](#a7841c7ceb21754059717c5996a081cb4)MCO\_PRE\_DIV\_9

| #define MCO\_PRE\_DIV\_9   9 |
| --- |

## [◆ ](#a50fd0ec19b392357f55331cc031b34fd)OCTOSPI1\_SEL

| #define OCTOSPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

CCIPR4 devices.

## [◆ ](#abfff4355a498febbcf4ebcb237930a57)RNG\_SEL

| #define RNG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a))

[BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)

#define BDCR\_REG

RCC\_BDCR register offset.

**Definition** stm32f0\_clock.h:38

BDCR devices.

## [◆ ](#ab8e49f6309adb53edd9ad3d051d451db)SAI1\_SEL

| #define SAI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a4fb9a6b79339e822f0ae426e8bba7486)SAI2\_SEL

| #define SAI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 19, [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a1a4999da331afff86581c8a6cea6afe9)SDMMC1\_SEL

| #define SDMMC1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 6, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a7319710d63129ad13039565cad2b4950)SDMMC2\_SEL

| #define SDMMC2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 7, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR3\_REG](#a302577067fac290b578130da822dc146))

CCIPR3 devices.

## [◆ ](#ad3e84eac634b9d943acea9b2ab884fb5)SPI2\_SEL

| #define SPI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 3, [CCIPR3\_REG](#a302577067fac290b578130da822dc146))

## [◆ ](#aaa096904d8a97bedc81f9a565e65c332)SPI3\_SEL

| #define SPI3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 6, [CCIPR3\_REG](#a302577067fac290b578130da822dc146))

## [◆ ](#a55086a94321a6e1af527a46c644f6c5e)SPI4\_SEL

| #define SPI4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 9, [CCIPR3\_REG](#a302577067fac290b578130da822dc146))

## [◆ ](#ac7193e508815171a4d73795d24086136)SPI5\_SEL

| #define SPI5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR3\_REG](#a302577067fac290b578130da822dc146))

## [◆ ](#ab43d49ec71267eb1d8002909cc3360bf)SPI6\_SEL

| #define SPI6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 15, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x088 |
| --- |

Bus clocks.

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x08C |
| --- |

## [◆ ](#a49bccabc3065f192086f16929a7b762d)STM32\_CLOCK\_BUS\_AHB4

| #define STM32\_CLOCK\_BUS\_AHB4   0x094 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x09c |
| --- |

## [◆ ](#ad25510091b50e823c9860089a9f23deb)STM32\_CLOCK\_BUS\_APB1\_2

| #define STM32\_CLOCK\_BUS\_APB1\_2   0x0A0 |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x0A4 |
| --- |

## [◆ ](#af7165e22b71d1beaf0dd4f59d5b4db6d)STM32\_CLOCK\_BUS\_APB3

| #define STM32\_CLOCK\_BUS\_APB3   0x0A8 |
| --- |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#a8b7025d7f4be00a152c53097a414668e)STM32\_SRC\_CKPER

| #define STM32\_SRC\_CKPER   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
| --- |

Clock muxes.

## [◆ ](#ac1c5062f5053fe96a5c2ba12d868eeda)STM32\_SRC\_CSI

| #define STM32\_SRC\_CSI   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#a2c2165a735dc0763cd972d464ececc5d)STM32\_SRC\_HCLK

| #define STM32\_SRC\_HCLK   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
| --- |

Bus clock.

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_CSI](#ac1c5062f5053fe96a5c2ba12d868eeda) + 1) |
| --- |

## [◆ ](#ae12e6bda1c30174c98303f692a42960f)STM32\_SRC\_HSI48

| #define STM32\_SRC\_HSI48   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

## [◆ ](#a72ffaa9863e167f47e06e91151b47831)STM32\_SRC\_PCLK1

| #define STM32\_SRC\_PCLK1   ([STM32\_SRC\_HCLK](#a2c2165a735dc0763cd972d464ececc5d) + 1) |
| --- |

## [◆ ](#a68f7335900538f3beb2c2d09e33376b3)STM32\_SRC\_PCLK2

| #define STM32\_SRC\_PCLK2   ([STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831) + 1) |
| --- |

## [◆ ](#ae54654dc761dca391f56e95ebd6db625)STM32\_SRC\_PCLK3

| #define STM32\_SRC\_PCLK3   ([STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3) + 1) |
| --- |

## [◆ ](#aa074615a92c5ff479f4fbed6fdf27f62)STM32\_SRC\_PLL1\_P

| #define STM32\_SRC\_PLL1\_P   ([STM32\_SRC\_PCLK3](#ae54654dc761dca391f56e95ebd6db625) + 1) |
| --- |

PLL outputs.

## [◆ ](#a6edb3dc598055ceeb82045fdee647637)STM32\_SRC\_PLL1\_Q

| #define STM32\_SRC\_PLL1\_Q   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| --- |

## [◆ ](#a6063632b32a970b9abbf711bab8a77c9)STM32\_SRC\_PLL1\_R

| #define STM32\_SRC\_PLL1\_R   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| --- |

## [◆ ](#ae568673a4eca1b42afc59faabb5810ac)STM32\_SRC\_PLL2\_P

| #define STM32\_SRC\_PLL2\_P   ([STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9) + 1) |
| --- |

## [◆ ](#aaf0a956dda42c2a031cabce49dd3e717)STM32\_SRC\_PLL2\_Q

| #define STM32\_SRC\_PLL2\_Q   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| --- |

## [◆ ](#a57af8944eefa865aa75b6286c13a53cd)STM32\_SRC\_PLL2\_R

| #define STM32\_SRC\_PLL2\_R   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| --- |

## [◆ ](#a17c753e0bb8547ea9452f48a65a0a206)STM32\_SRC\_PLL3\_P

| #define STM32\_SRC\_PLL3\_P   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| --- |

## [◆ ](#a9a31a3adebff6a1eee31c287673412c9)STM32\_SRC\_PLL3\_Q

| #define STM32\_SRC\_PLL3\_Q   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| --- |

## [◆ ](#a604c22ff137a35cd1725b70991696f9a)STM32\_SRC\_PLL3\_R

| #define STM32\_SRC\_PLL3\_R   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| --- |

## [◆ ](#a9319a91fb044022ba812f616cf192f65)SYSTICK\_SEL

| #define SYSTICK\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 2, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#ad39b85aaa947648b1b833b1414116f51)TIMIC\_SEL

| #define TIMIC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 31, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

[CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2)

#define CCIPR1\_REG

RCC\_CCIPRx register offset (RM0456.pdf).

**Definition** stm32h5\_clock.h:55

## [◆ ](#a5eef37bd8c6a90bf0de08faf5d05f410)USART10\_SEL

| #define USART10\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 27, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#adc9bd02facff6c4513f4fe8cb43fe9be)USART11\_SEL

| #define USART11\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

CCIPR2 devices.

## [◆ ](#a2ce5c32e9d923116b1ef96e415876866)USART12\_SEL

| #define USART12\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

Device domain clocks selection helpers.

CCIPR1 devices

## [◆ ](#ad67d92dfc439018a7a231e661d10d7f9)USART2\_SEL

| #define USART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 3, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ad2f356c0bc0e43d6f629cdb840846526)USART3\_SEL

| #define USART3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 6, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aced9e983095cb40bc18f3a66e3818c98)USART4\_SEL

| #define USART4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 9, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a6a45e0ef8bd196574e241aefdb3a5350)USART5\_SEL

| #define USART5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a99c9026d61766ec9b91872ee64ad63eb)USART6\_SEL

| #define USART6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 15, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a085ea149cac54d39aef4cb9f5c03402c)USART7\_SEL

| #define USART7\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 18, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#adf99875c4c7a62e255871678fe848645)USART8\_SEL

| #define USART8\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 21, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a2bb43ceb46c7cb47f946c868a9e5b0aa)USART9\_SEL

| #define USART9\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a3247ad782f1e2c7db84989d03831139b)USB\_SEL

| #define USB\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32h5\_clock.h](stm32h5__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
