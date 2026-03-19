---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32u5__clock_8h.html
original_path: doxygen/html/stm32u5__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32u5\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32u5__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSI16](#a5e1f2346bda03742e59614bf3d727be0)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f)   ([STM32\_SRC\_HSI16](#a5e1f2346bda03742e59614bf3d727be0) + 1) |
| #define | [STM32\_SRC\_MSIS](#a632bcd9ada69ab27033a3d46406fd4fb)   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
| #define | [STM32\_SRC\_MSIK](#a6cdbd60c77934e2e1ecbdf281c670550)   ([STM32\_SRC\_MSIS](#a632bcd9ada69ab27033a3d46406fd4fb) + 1) |
| #define | [STM32\_SRC\_HCLK](#a2c2165a735dc0763cd972d464ececc5d)   ([STM32\_SRC\_MSIK](#a6cdbd60c77934e2e1ecbdf281c670550) + 1) |
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
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x088 |
|  | Clock muxes. |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x08C |
| #define | [STM32\_CLOCK\_BUS\_AHB2\_2](#a76e35461c02d9c020948f980c864e9b3)   0x090 |
| #define | [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569)   0x094 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x09C |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x0A0 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x0A4 |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x0A8 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| #define | [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2)   0xE0 |
|  | RCC\_CCIPRx register offset (RM0456.pdf). |
| #define | [CCIPR2\_REG](#a60349691a29a48b727f302acb8025b89)   0xE4 |
| #define | [CCIPR3\_REG](#a302577067fac290b578130da822dc146)   0xE8 |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0xF0 |
|  | RCC\_BDCR register offset. |
| #define | [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)   0x1C |
|  | RCC\_CFGRx register offset. |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device domain clocks selection helpers. |
| #define | [USART2\_SEL](#ad67d92dfc439018a7a231e661d10d7f9)(val) |
| #define | [USART3\_SEL](#ad2f356c0bc0e43d6f629cdb840846526)(val) |
| #define | [UART4\_SEL](#a091d597b4979c49951f880bc6ccb4d71)(val) |
| #define | [UART5\_SEL](#a136c2c36c89ebdf2c5b97686bbce0209)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C2\_SEL](#abdd79c9ce90458b53e81123d181fed98)(val) |
| #define | [I2C4\_SEL](#a55880006ae28021de4d148924c06001e)(val) |
| #define | [SPI2\_SEL](#ad3e84eac634b9d943acea9b2ab884fb5)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
| #define | [SYSTICK\_SEL](#a9319a91fb044022ba812f616cf192f65)(val) |
| #define | [FDCAN1\_SEL](#a11874554108542cecbce3f012940ab0c)(val) |
| #define | [ICKLK\_SEL](#a1b856889f9c1e43ff7c61fe6216d9e83)(val) |
| #define | [TIMIC\_SEL](#ad39b85aaa947648b1b833b1414116f51)(val) |
| #define | [MDF1\_SEL](#adf9b2f5b55d6b8629128b60b578df9a6)(val) |
|  | CCIPR2 devices. |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [SAI2\_SEL](#a4fb9a6b79339e822f0ae426e8bba7486)(val) |
| #define | [SAE\_SEL](#ae2cb1fc32c1940791b8532dbcd923880)(val) |
| #define | [RNG\_SEL](#abfff4355a498febbcf4ebcb237930a57)(val) |
| #define | [SDMMC\_SEL](#a42688c1d17e09ab58029feedd7491c0b)(val) |
| #define | [DSIHOST\_SEL](#a59241c4cd74e02fa6d48b7ebc90d87c8)(val) |
| #define | [USART6\_SEL](#a99c9026d61766ec9b91872ee64ad63eb)(val) |
| #define | [LTDC\_SEL](#ac299465bc5d655ecc6dd1e8e7a347e0c)(val) |
| #define | [OCTOSPI\_SEL](#a121f4f2f299d0ab56293512df1ac6b2c)(val) |
| #define | [HSPI\_SEL](#aca5233e2f676feba6b622f0068047437)(val) |
| #define | [I2C5\_SEL](#ab9c645c57c03d284386ba0b4fd37d11f)(val) |
| #define | [I2C6\_SEL](#a06c4da4e35e9d6a8db04172f24d8a0e4)(val) |
| #define | [OTGHS\_SEL](#a3b059f3ee4d562325d2c1371d39dc08a)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
|  | CCIPR3 devices. |
| #define | [SPI3\_SEL](#aaa096904d8a97bedc81f9a565e65c332)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [LPTIM34\_SEL](#a7f929ce6942d82e8eeedbd8b563ce093)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [ADCDAC\_SEL](#a454d6254cea3749ac4502fb51739e27c)(val) |
| #define | [DAC1\_SEL](#a4674bd2e234d3e510bf576d03d42d45c)(val) |
| #define | [ADF1\_SEL](#a2965fce3cbae0a73506ddf383c78783f)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR1 devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO\_PRE\_DIV\_1](#aa6d6446aa7a1c84324475f6e8665fbb7)   0 |
| #define | [MCO\_PRE\_DIV\_2](#a36db847c7932669759f64844a15c42c3)   1 |
| #define | [MCO\_PRE\_DIV\_4](#a74c5b485d9169c489ab19e788b43c657)   2 |
| #define | [MCO\_PRE\_DIV\_8](#ad1bb69ff2fe6748978c31666f201947c)   3 |
| #define | [MCO\_PRE\_DIV\_16](#a111fd8dc5850b16b1308c8eaba8a9458)   4 |

## Macro Definition Documentation

## [◆ ](#a454d6254cea3749ac4502fb51739e27c)ADCDAC\_SEL

| #define ADCDAC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146)

#define CCIPR3\_REG

**Definition** stm32h5\_clock.h:57

## [◆ ](#a2965fce3cbae0a73506ddf383c78783f)ADF1\_SEL

| #define ADF1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0xF0 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#a5a41b990eca365907d09bb4416fb22d2)CCIPR1\_REG

| #define CCIPR1\_REG   0xE0 |
| --- |

RCC\_CCIPRx register offset (RM0456.pdf).

## [◆ ](#a60349691a29a48b727f302acb8025b89)CCIPR2\_REG

| #define CCIPR2\_REG   0xE4 |
| --- |

## [◆ ](#a302577067fac290b578130da822dc146)CCIPR3\_REG

| #define CCIPR3\_REG   0xE8 |
| --- |

## [◆ ](#a6b894fe6e036f03831faddf28bce43c6)CFGR1\_REG

| #define CFGR1\_REG   0x1C |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#a4674bd2e234d3e510bf576d03d42d45c)DAC1\_SEL

| #define DAC1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 15, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a59241c4cd74e02fa6d48b7ebc90d87c8)DSIHOST\_SEL

| #define DSIHOST\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 15, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

[CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89)

#define CCIPR2\_REG

**Definition** stm32g0\_clock.h:40

## [◆ ](#a11874554108542cecbce3f012940ab0c)FDCAN1\_SEL

| #define FDCAN1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 24, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

[CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)

#define CCIPR1\_REG

RCC\_CCIPRx register offset (RM0456.pdf).

**Definition** stm32h5\_clock.h:55

## [◆ ](#aca5233e2f676feba6b622f0068047437)HSPI\_SEL

| #define HSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 22, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 10, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#abdd79c9ce90458b53e81123d181fed98)I2C2\_SEL

| #define I2C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 6, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a55880006ae28021de4d148924c06001e)I2C4\_SEL

| #define I2C4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 14, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ab9c645c57c03d284386ba0b4fd37d11f)I2C5\_SEL

| #define I2C5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 24, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a06c4da4e35e9d6a8db04172f24d8a0e4)I2C6\_SEL

| #define I2C6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 26, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a1b856889f9c1e43ff7c61fe6216d9e83)ICKLK\_SEL

| #define ICKLK\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 26, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 10, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#aa713f6ff001bfa6352747e7a66e3f98a)LPTIM2\_SEL

| #define LPTIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 18, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a7f929ce6942d82e8eeedbd8b563ce093)LPTIM34\_SEL

| #define LPTIM34\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

CCIPR3 devices.

## [◆ ](#ac299465bc5d655ecc6dd1e8e7a347e0c)LTDC\_SEL

| #define LTDC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 18, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 28, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

[CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:39

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xF, 24, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

CFGR1 devices.

## [◆ ](#aa6d6446aa7a1c84324475f6e8665fbb7)MCO\_PRE\_DIV\_1

| #define MCO\_PRE\_DIV\_1   0 |
| --- |

## [◆ ](#a111fd8dc5850b16b1308c8eaba8a9458)MCO\_PRE\_DIV\_16

| #define MCO\_PRE\_DIV\_16   4 |
| --- |

## [◆ ](#a36db847c7932669759f64844a15c42c3)MCO\_PRE\_DIV\_2

| #define MCO\_PRE\_DIV\_2   1 |
| --- |

## [◆ ](#a74c5b485d9169c489ab19e788b43c657)MCO\_PRE\_DIV\_4

| #define MCO\_PRE\_DIV\_4   2 |
| --- |

## [◆ ](#ad1bb69ff2fe6748978c31666f201947c)MCO\_PRE\_DIV\_8

| #define MCO\_PRE\_DIV\_8   3 |
| --- |

## [◆ ](#adf9b2f5b55d6b8629128b60b578df9a6)MDF1\_SEL

| #define MDF1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

CCIPR2 devices.

## [◆ ](#a121f4f2f299d0ab56293512df1ac6b2c)OCTOSPI\_SEL

| #define OCTOSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 20, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a3b059f3ee4d562325d2c1371d39dc08a)OTGHS\_SEL

| #define OTGHS\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 30, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#abfff4355a498febbcf4ebcb237930a57)RNG\_SEL

| #define RNG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

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

## [◆ ](#ae2cb1fc32c1940791b8532dbcd923880)SAE\_SEL

| #define SAE\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 11, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#ab8e49f6309adb53edd9ad3d051d451db)SAI1\_SEL

| #define SAI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 5, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a4fb9a6b79339e822f0ae426e8bba7486)SAI2\_SEL

| #define SAI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a42688c1d17e09ab58029feedd7491c0b)SDMMC\_SEL

| #define SDMMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 14, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 20, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ad3e84eac634b9d943acea9b2ab884fb5)SPI2\_SEL

| #define SPI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 16, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aaa096904d8a97bedc81f9a565e65c332)SPI3\_SEL

| #define SPI3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 3, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x088 |
| --- |

Clock muxes.

Bus clocks

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x08C |
| --- |

## [◆ ](#a76e35461c02d9c020948f980c864e9b3)STM32\_CLOCK\_BUS\_AHB2\_2

| #define STM32\_CLOCK\_BUS\_AHB2\_2   0x090 |
| --- |

## [◆ ](#ab2a3c819828eb0186ac3a3f15f4b4569)STM32\_CLOCK\_BUS\_AHB3

| #define STM32\_CLOCK\_BUS\_AHB3   0x094 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x09C |
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

## [◆ ](#a2c2165a735dc0763cd972d464ececc5d)STM32\_SRC\_HCLK

| #define STM32\_SRC\_HCLK   ([STM32\_SRC\_MSIK](#a6cdbd60c77934e2e1ecbdf281c670550) + 1) |
| --- |

Bus clock.

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#a5e1f2346bda03742e59614bf3d727be0)STM32\_SRC\_HSI16

| #define STM32\_SRC\_HSI16   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#ae12e6bda1c30174c98303f692a42960f)STM32\_SRC\_HSI48

| #define STM32\_SRC\_HSI48   ([STM32\_SRC\_HSI16](#a5e1f2346bda03742e59614bf3d727be0) + 1) |
| --- |

## [◆ ](#a6cdbd60c77934e2e1ecbdf281c670550)STM32\_SRC\_MSIK

| #define STM32\_SRC\_MSIK   ([STM32\_SRC\_MSIS](#a632bcd9ada69ab27033a3d46406fd4fb) + 1) |
| --- |

## [◆ ](#a632bcd9ada69ab27033a3d46406fd4fb)STM32\_SRC\_MSIS

| #define STM32\_SRC\_MSIS   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 22, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ad39b85aaa947648b1b833b1414116f51)TIMIC\_SEL

| #define TIMIC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 29, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a091d597b4979c49951f880bc6ccb4d71)UART4\_SEL

| #define UART4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 6, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a136c2c36c89ebdf2c5b97686bbce0209)UART5\_SEL

| #define UART5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

Device domain clocks selection helpers.

CCIPR1 devices

## [◆ ](#ad67d92dfc439018a7a231e661d10d7f9)USART2\_SEL

| #define USART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 2, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ad2f356c0bc0e43d6f629cdb840846526)USART3\_SEL

| #define USART3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a99c9026d61766ec9b91872ee64ad63eb)USART6\_SEL

| #define USART6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 16, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32u5\_clock.h](stm32u5__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
