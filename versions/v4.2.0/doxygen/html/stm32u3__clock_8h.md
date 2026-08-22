---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32u3__clock_8h.html
original_path: doxygen/html/stm32u3__clock_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32u3\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32u3__clock_8h_source.md)

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
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x088 |
|  | Clock muxes. |
| #define | [STM32\_CLOCK\_BUS\_AHB1\_2](#af24118ede113167b5e40758432031ca9)   0x094 |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x08C |
| #define | [STM32\_CLOCK\_BUS\_AHB2\_2](#a76e35461c02d9c020948f980c864e9b3)   0x090 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x09C |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x0A0 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x0A4 |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x0A8 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| #define | [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2)   0x100 |
|  | RCC\_CCIPRx register offset (RM0487.pdf). |
| #define | [CCIPR2\_REG](#a60349691a29a48b727f302acb8025b89)   0x104 |
| #define | [CCIPR3\_REG](#a302577067fac290b578130da822dc146)   0x108 |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x110 |
|  | RCC\_BDCR register offset. |
| #define | [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)   0x0C |
|  | RCC\_CFGRx register offset. |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device domain clocks selection helpers. |
| #define | [USART3\_SEL](#ad2f356c0bc0e43d6f629cdb840846526)(val) |
| #define | [UART4\_SEL](#a091d597b4979c49951f880bc6ccb4d71)(val) |
| #define | [UART5\_SEL](#a136c2c36c89ebdf2c5b97686bbce0209)(val) |
| #define | [I3C1\_SEL](#a576dca08c22370326fefc540bf056b81)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C2\_SEL](#abdd79c9ce90458b53e81123d181fed98)(val) |
| #define | [I3C2\_SEL](#a647bc22bf65d67e9e2c5361d0dce925d)(val) |
| #define | [SPI2\_SEL](#ad3e84eac634b9d943acea9b2ab884fb5)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
| #define | [SYSTICK\_SEL](#a9319a91fb044022ba812f616cf192f65)(val) |
| #define | [FDCAN1\_SEL](#a11874554108542cecbce3f012940ab0c)(val) |
| #define | [ICLK\_SEL](#a467698cc8a5140a9aa169cb63de049f4)(val) |
| #define | [USB1\_SEL](#a1f29287e499d74135f886c7a12dee2db)(val) |
| #define | [TIMIC\_SEL](#ad39b85aaa947648b1b833b1414116f51)(val) |
| #define | [ADF1\_SEL](#a2965fce3cbae0a73506ddf383c78783f)(val) |
|  | CCIPR2 devices. |
| #define | [SPI3\_SEL](#aaa096904d8a97bedc81f9a565e65c332)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [RNG\_SEL](#abfff4355a498febbcf4ebcb237930a57)(val) |
| #define | [ADCDAC\_SEL](#a454d6254cea3749ac4502fb51739e27c)(val) |
| #define | [DAC1SH\_SEL](#a485e470fc68329d8eb13203614f36d20)(val) |
| #define | [OCTOSPI\_SEL](#a121f4f2f299d0ab56293512df1ac6b2c)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
|  | CCIPR3 devices. |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [LPTIM34\_SEL](#a7f929ce6942d82e8eeedbd8b563ce093)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
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
| #define | [MCO\_PRE\_DIV\_32](#acd636581f9cbba9e66519929ecf620e2)   5 |
| #define | [MCO\_PRE\_DIV\_64](#ac2e5fb8f588e90b951a8962d1d0ce61e)   6 |
| #define | [MCO\_PRE\_DIV\_128](#a14d17d0a8cc9a70ddab9a1d2bf29661a)   7 |

## Macro Definition Documentation

## [◆ ](#a454d6254cea3749ac4502fb51739e27c)ADCDAC\_SEL

| #define ADCDAC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 16, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89)

#define CCIPR2\_REG

**Definition** stm32c0\_clock.h:34

## [◆ ](#a2965fce3cbae0a73506ddf383c78783f)ADF1\_SEL

| #define ADF1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

CCIPR2 devices.

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x110 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#a5a41b990eca365907d09bb4416fb22d2)CCIPR1\_REG

| #define CCIPR1\_REG   0x100 |
| --- |

RCC\_CCIPRx register offset (RM0487.pdf).

## [◆ ](#a60349691a29a48b727f302acb8025b89)CCIPR2\_REG

| #define CCIPR2\_REG   0x104 |
| --- |

## [◆ ](#a302577067fac290b578130da822dc146)CCIPR3\_REG

| #define CCIPR3\_REG   0x108 |
| --- |

## [◆ ](#a6b894fe6e036f03831faddf28bce43c6)CFGR1\_REG

| #define CFGR1\_REG   0x0C |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#a485e470fc68329d8eb13203614f36d20)DAC1SH\_SEL

| #define DAC1SH\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 19, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a11874554108542cecbce3f012940ab0c)FDCAN1\_SEL

| #define FDCAN1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 24, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

[CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)

#define CCIPR1\_REG

RCC\_CCIPRx register offset (RM0456.pdf).

**Definition** stm32h5\_clock.h:55

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 10, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#abdd79c9ce90458b53e81123d181fed98)I2C2\_SEL

| #define I2C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 12, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 6, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

[CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146)

#define CCIPR3\_REG

**Definition** stm32h5\_clock.h:57

## [◆ ](#a576dca08c22370326fefc540bf056b81)I3C1\_SEL

| #define I3C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 8, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a647bc22bf65d67e9e2c5361d0dce925d)I3C2\_SEL

| #define I3C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 14, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a467698cc8a5140a9aa169cb63de049f4)ICLK\_SEL

| #define ICLK\_SEL | ( |  | *val* | ) |  |
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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

CCIPR3 devices.

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 28, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

[CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:40

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xF, 24, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

CFGR1 devices.

## [◆ ](#aa6d6446aa7a1c84324475f6e8665fbb7)MCO\_PRE\_DIV\_1

| #define MCO\_PRE\_DIV\_1   0 |
| --- |

## [◆ ](#a14d17d0a8cc9a70ddab9a1d2bf29661a)MCO\_PRE\_DIV\_128

| #define MCO\_PRE\_DIV\_128   7 |
| --- |

## [◆ ](#a111fd8dc5850b16b1308c8eaba8a9458)MCO\_PRE\_DIV\_16

| #define MCO\_PRE\_DIV\_16   4 |
| --- |

## [◆ ](#a36db847c7932669759f64844a15c42c3)MCO\_PRE\_DIV\_2

| #define MCO\_PRE\_DIV\_2   1 |
| --- |

## [◆ ](#acd636581f9cbba9e66519929ecf620e2)MCO\_PRE\_DIV\_32

| #define MCO\_PRE\_DIV\_32   5 |
| --- |

## [◆ ](#a74c5b485d9169c489ab19e788b43c657)MCO\_PRE\_DIV\_4

| #define MCO\_PRE\_DIV\_4   2 |
| --- |

## [◆ ](#ac2e5fb8f588e90b951a8962d1d0ce61e)MCO\_PRE\_DIV\_64

| #define MCO\_PRE\_DIV\_64   6 |
| --- |

## [◆ ](#ad1bb69ff2fe6748978c31666f201947c)MCO\_PRE\_DIV\_8

| #define MCO\_PRE\_DIV\_8   3 |
| --- |

## [◆ ](#a121f4f2f299d0ab56293512df1ac6b2c)OCTOSPI\_SEL

| #define OCTOSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 20, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#abfff4355a498febbcf4ebcb237930a57)RNG\_SEL

| #define RNG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 11, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 5, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 20, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ad3e84eac634b9d943acea9b2ab884fb5)SPI2\_SEL

| #define SPI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 16, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aaa096904d8a97bedc81f9a565e65c332)SPI3\_SEL

| #define SPI3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 3, [CCIPR2\_REG](stm32c0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x088 |
| --- |

Clock muxes.

Bus clocks

## [◆ ](#af24118ede113167b5e40758432031ca9)STM32\_CLOCK\_BUS\_AHB1\_2

| #define STM32\_CLOCK\_BUS\_AHB1\_2   0x094 |
| --- |

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x08C |
| --- |

## [◆ ](#a76e35461c02d9c020948f980c864e9b3)STM32\_CLOCK\_BUS\_AHB2\_2

| #define STM32\_CLOCK\_BUS\_AHB2\_2   0x090 |
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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 4, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a136c2c36c89ebdf2c5b97686bbce0209)UART5\_SEL

| #define UART5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 6, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 0, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

Device domain clocks selection helpers.

CCIPR1 devices

## [◆ ](#ad2f356c0bc0e43d6f629cdb840846526)USART3\_SEL

| #define USART3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 2, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a1f29287e499d74135f886c7a12dee2db)USB1\_SEL

| #define USB1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 28, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32u3\_clock.h](stm32u3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
