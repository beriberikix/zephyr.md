---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32c0__clock_8h.html
original_path: doxygen/html/stm32c0__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32c0\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32c0__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_CLOCK\_BUS\_IOP](#afe5b12955e87bbfcee6107cc30e45566)   0x034 |
|  | Bus clocks. |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x038 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x03c |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x040 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_IOP](#afe5b12955e87bbfcee6107cc30e45566) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb) |
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| #define | [STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
|  | Peripheral bus clock. |
| #define | [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260)   0x54 |
|  | RCC\_CCIPR register offset. |
| #define | [CSR1\_REG](#aef1dabdfdb37922d3876f12a7ef193b4)   0x5C |
|  | RCC\_CSR1 register offset. |
| #define | [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)   0x08 |
|  | RCC\_CFGRx register offset. |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device domain clocks selection helpers. |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C2\_I2S1\_SEL](#ab6681395c0ed012d399bb8da480cc577)(val) |
| #define | [ADC\_SEL](#a635d17ad991ded52d41a6e7b0bec5773)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | CSR1 devices. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR1 devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MCO2\_PRE](#ab02a0ccbb8588979ca4742c72c59589f)(val) |
| #define | [MCO\_PRE\_DIV\_1](#aa6d6446aa7a1c84324475f6e8665fbb7)   0 |
| #define | [MCO\_PRE\_DIV\_2](#a36db847c7932669759f64844a15c42c3)   1 |
| #define | [MCO\_PRE\_DIV\_4](#a74c5b485d9169c489ab19e788b43c657)   2 |
| #define | [MCO\_PRE\_DIV\_8](#ad1bb69ff2fe6748978c31666f201947c)   3 |
| #define | [MCO\_PRE\_DIV\_16](#a111fd8dc5850b16b1308c8eaba8a9458)   4 |
| #define | [MCO\_PRE\_DIV\_32](#acd636581f9cbba9e66519929ecf620e2)   5 |
| #define | [MCO\_PRE\_DIV\_64](#ac2e5fb8f588e90b951a8962d1d0ce61e)   6 |
| #define | [MCO\_PRE\_DIV\_128](#a14d17d0a8cc9a70ddab9a1d2bf29661a)   7 |

## Macro Definition Documentation

## [◆ ](#a635d17ad991ded52d41a6e7b0bec5773)ADC\_SEL

| #define ADC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 30, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260)

#define CCIPR\_REG

RCC\_CCIPR register offset.

**Definition** stm32c0\_clock.h:33

## [◆ ](#af50f81a20c6e91a7a8611d1e59ca6260)CCIPR\_REG

| #define CCIPR\_REG   0x54 |
| --- |

RCC\_CCIPR register offset.

## [◆ ](#a6b894fe6e036f03831faddf28bce43c6)CFGR1\_REG

| #define CFGR1\_REG   0x08 |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#aef1dabdfdb37922d3876f12a7ef193b4)CSR1\_REG

| #define CSR1\_REG   0x5C |
| --- |

RCC\_CSR1 register offset.

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#ab6681395c0ed012d399bb8da480cc577)I2C2\_I2S1\_SEL

| #define I2C2\_I2S1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 14, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 28, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

[CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:39

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 24, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

CFGR1 devices.

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 20, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 16, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

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

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [CSR1\_REG](#aef1dabdfdb37922d3876f12a7ef193b4))

[CSR1\_REG](#aef1dabdfdb37922d3876f12a7ef193b4)

#define CSR1\_REG

RCC\_CSR1 register offset.

**Definition** stm32c0\_clock.h:36

CSR1 devices.

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x038 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x03c |
| --- |

## [◆ ](#ad25510091b50e823c9860089a9f23deb)STM32\_CLOCK\_BUS\_APB1\_2

| #define STM32\_CLOCK\_BUS\_APB1\_2   0x040 |
| --- |

## [◆ ](#afe5b12955e87bbfcee6107cc30e45566)STM32\_CLOCK\_BUS\_IOP

| #define STM32\_CLOCK\_BUS\_IOP   0x034 |
| --- |

Bus clocks.

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_IOP](#afe5b12955e87bbfcee6107cc30e45566) |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#a6cd4e305697f314401e5654b4dd5f25d)STM32\_SRC\_PCLK

| #define STM32\_SRC\_PCLK   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

Peripheral bus clock.

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

Device domain clocks selection helpers.

CCIPR devices

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32c0\_clock.h](stm32c0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
