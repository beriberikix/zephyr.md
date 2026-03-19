---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32l4__clock_8h.html
original_path: doxygen/html/stm32l4__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32l4\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32l4__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x048 |
|  | Bus clocks. |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x04c |
| #define | [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569)   0x050 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x058 |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x05c |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x060 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db) |
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| #define | [STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c)   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
| #define | [STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d)   ([STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c) + 1) |
|  | Bus clock. |
| #define | [STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab)   ([STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d) + 1) |
|  | PLL clock outputs. |
| #define | [STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27)   ([STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab) + 1) |
| #define | [STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439)   ([STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27) + 1) |
| #define | [STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)   0xFFU |
| #define | [STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)   0U |
| #define | [STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)   0x1FU |
| #define | [STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)   8U |
| #define | [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)   0x7U |
| #define | [STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)   13U |
| #define | [STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)   0x7U |
| #define | [STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)   16U |
| #define | [STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, mask, shift, reg) |
|  | STM32 clock configuration bit field. |
| #define | [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260)   0x88 |
|  | RCC\_CCIPR register offset. |
| #define | [CCIPR2\_REG](#a60349691a29a48b727f302acb8025b89)   0x9C |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x90 |
|  | RCC\_BDCR register offset. |
| #define | [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)   0x08 |
|  | RCC\_CFGRx register offset. |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device domain clocks selection helpers. |
| #define | [USART2\_SEL](#ad67d92dfc439018a7a231e661d10d7f9)(val) |
| #define | [USART3\_SEL](#ad2f356c0bc0e43d6f629cdb840846526)(val) |
| #define | [UART4\_SEL](#a091d597b4979c49951f880bc6ccb4d71)(val) |
| #define | [UART5\_SEL](#a136c2c36c89ebdf2c5b97686bbce0209)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C2\_SEL](#abdd79c9ce90458b53e81123d181fed98)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [SAI2\_SEL](#a4fb9a6b79339e822f0ae426e8bba7486)(val) |
| #define | [CLK48\_SEL](#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)(val) |
| #define | [ADC\_SEL](#a635d17ad991ded52d41a6e7b0bec5773)(val) |
| #define | [SWPMI1\_SEL](#a45123bcb861fd2ed40c3ac3bf4aa4edd)(val) |
| #define | [DFSDM1\_SEL](#a5364dd3606acfca9d1c00e60255a6634)(val) |
| #define | [I2C4\_SEL](#a55880006ae28021de4d148924c06001e)(val) |
|  | CCIPR2 devices. |
| #define | [DFSDM\_SEL](#a4b0b71b1a3d25d7bd37eec532f98c018)(val) |
| #define | [ADFSDM\_SEL](#a7a9e2b88955eab5d77438aa9f3ef84b8)(val) |
| #define | [DSI\_SEL](#a2e82c24eb0c9e22635966752eebb2a05)(val) |
| #define | [SDMMC\_SEL](#a42688c1d17e09ab58029feedd7491c0b)(val) |
| #define | [OSPI\_SEL](#a098cb5d65a4a2b4cd7da394289eb38ff)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |

## Macro Definition Documentation

## [◆ ](#a635d17ad991ded52d41a6e7b0bec5773)ADC\_SEL

| #define ADC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 28, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260)

#define CCIPR\_REG

RCC\_CCIPR register offset.

**Definition** stm32c0\_clock.h:61

## [◆ ](#a7a9e2b88955eab5d77438aa9f3ef84b8)ADFSDM\_SEL

| #define ADFSDM\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 3, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

[CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89)

#define CCIPR2\_REG

**Definition** stm32g0\_clock.h:68

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x90 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#a60349691a29a48b727f302acb8025b89)CCIPR2\_REG

| #define CCIPR2\_REG   0x9C |
| --- |

## [◆ ](#af50f81a20c6e91a7a8611d1e59ca6260)CCIPR\_REG

| #define CCIPR\_REG   0x88 |
| --- |

RCC\_CCIPR register offset.

## [◆ ](#afb2336a33a23f9671b26010594232ba3)CFGR\_REG

| #define CFGR\_REG   0x08 |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)CLK48\_SEL

| #define CLK48\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 26, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a5364dd3606acfca9d1c00e60255a6634)DFSDM1\_SEL

| #define DFSDM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 31, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a4b0b71b1a3d25d7bd37eec532f98c018)DFSDM\_SEL

| #define DFSDM\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 2, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a2e82c24eb0c9e22635966752eebb2a05)DSI\_SEL

| #define DSI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 12, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 12, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#abdd79c9ce90458b53e81123d181fed98)I2C2\_SEL

| #define I2C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 14, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 16, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a55880006ae28021de4d148924c06001e)I2C4\_SEL

| #define I2C4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

CCIPR2 devices.

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 18, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#aa713f6ff001bfa6352747e7a66e3f98a)LPTIM2\_SEL

| #define LPTIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 20, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 10, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 28, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)

#define STM32\_MCO\_CFGR(val, mask, shift, reg)

STM32 MCO configuration register bit field.

**Definition** stm32\_common\_clocks.h:42

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:63

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0xF, 24, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

CFGR devices.

## [◆ ](#a098cb5d65a4a2b4cd7da394289eb38ff)OSPI\_SEL

| #define OSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 20, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a))

[BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)

#define BDCR\_REG

RCC\_BDCR register offset.

**Definition** stm32f0\_clock.h:66

BDCR devices.

## [◆ ](#ab8e49f6309adb53edd9ad3d051d451db)SAI1\_SEL

| #define SAI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 22, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a4fb9a6b79339e822f0ae426e8bba7486)SAI2\_SEL

| #define SAI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 24, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a42688c1d17e09ab58029feedd7491c0b)SDMMC\_SEL

| #define SDMMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 14, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x048 |
| --- |

Bus clocks.

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x04c |
| --- |

## [◆ ](#ab2a3c819828eb0186ac3a3f15f4b4569)STM32\_CLOCK\_BUS\_AHB3

| #define STM32\_CLOCK\_BUS\_AHB3   0x050 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x058 |
| --- |

## [◆ ](#ad25510091b50e823c9860089a9f23deb)STM32\_CLOCK\_BUS\_APB1\_2

| #define STM32\_CLOCK\_BUS\_APB1\_2   0x05c |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x060 |
| --- |

## [◆ ](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)STM32\_CLOCK\_MASK\_MASK

| #define STM32\_CLOCK\_MASK\_MASK   0x7U |
| --- |

## [◆ ](#abfdb31d824fc5c6cf809a1dcff022b5d)STM32\_CLOCK\_MASK\_SHIFT

| #define STM32\_CLOCK\_MASK\_SHIFT   13U |
| --- |

## [◆ ](#a33d66849c63db64784317260b06ceb24)STM32\_CLOCK\_REG\_MASK

| #define STM32\_CLOCK\_REG\_MASK   0xFFU |
| --- |

## [◆ ](#a2e73bdb1691751ffd616a5c4e2762423)STM32\_CLOCK\_REG\_SHIFT

| #define STM32\_CLOCK\_REG\_SHIFT   0U |
| --- |

## [◆ ](#af3001a7541ea4df9e4948fd559352f60)STM32\_CLOCK\_SHIFT\_MASK

| #define STM32\_CLOCK\_SHIFT\_MASK   0x1FU |
| --- |

## [◆ ](#a147846b77bd51e42c85bea5aca50ad4f)STM32\_CLOCK\_SHIFT\_SHIFT

| #define STM32\_CLOCK\_SHIFT\_SHIFT   8U |
| --- |

## [◆ ](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)STM32\_CLOCK\_VAL\_MASK

| #define STM32\_CLOCK\_VAL\_MASK   0x7U |
| --- |

## [◆ ](#adf2ca8c7f707b82b7ec4820dfc32929a)STM32\_CLOCK\_VAL\_SHIFT

| #define STM32\_CLOCK\_VAL\_SHIFT   16U |
| --- |

## [◆ ](#a13a09d4e73c5f6485cbbb541c9e81c35)STM32\_DOMAIN\_CLOCK

| #define STM32\_DOMAIN\_CLOCK | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *shift*, |
|  |  |  | *reg* ) |

**Value:**

((((reg) & [STM32\_CLOCK\_REG\_MASK](stm32c0__clock_8h.md#a33d66849c63db64784317260b06ceb24)) << [STM32\_CLOCK\_REG\_SHIFT](stm32c0__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)) | \

(((shift) & [STM32\_CLOCK\_SHIFT\_MASK](stm32c0__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)) << [STM32\_CLOCK\_SHIFT\_SHIFT](stm32c0__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)) | \

(((mask) & [STM32\_CLOCK\_MASK\_MASK](stm32c0__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)) << [STM32\_CLOCK\_MASK\_SHIFT](stm32c0__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)) | \

(((val) & [STM32\_CLOCK\_VAL\_MASK](stm32c0__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)) << [STM32\_CLOCK\_VAL\_SHIFT](stm32c0__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)))

[STM32\_CLOCK\_SHIFT\_SHIFT](stm32c0__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)

#define STM32\_CLOCK\_SHIFT\_SHIFT

**Definition** stm32c0\_clock.h:35

[STM32\_CLOCK\_REG\_SHIFT](stm32c0__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)

#define STM32\_CLOCK\_REG\_SHIFT

**Definition** stm32c0\_clock.h:33

[STM32\_CLOCK\_REG\_MASK](stm32c0__clock_8h.md#a33d66849c63db64784317260b06ceb24)

#define STM32\_CLOCK\_REG\_MASK

**Definition** stm32c0\_clock.h:32

[STM32\_CLOCK\_MASK\_MASK](stm32c0__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)

#define STM32\_CLOCK\_MASK\_MASK

**Definition** stm32c0\_clock.h:36

[STM32\_CLOCK\_VAL\_MASK](stm32c0__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)

#define STM32\_CLOCK\_VAL\_MASK

**Definition** stm32c0\_clock.h:38

[STM32\_CLOCK\_MASK\_SHIFT](stm32c0__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)

#define STM32\_CLOCK\_MASK\_SHIFT

**Definition** stm32c0\_clock.h:37

[STM32\_CLOCK\_VAL\_SHIFT](stm32c0__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)

#define STM32\_CLOCK\_VAL\_SHIFT

**Definition** stm32c0\_clock.h:39

[STM32\_CLOCK\_SHIFT\_MASK](stm32c0__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)

#define STM32\_CLOCK\_SHIFT\_MASK

**Definition** stm32c0\_clock.h:34

STM32 clock configuration bit field.

- reg (1/2/3) [ 0 : 7 ]
- shift (0..31) [ 8 : 12 ]
- mask (0x1, 0x3, 0x7) [ 13 : 15 ]
- val (0..7) [ 16 : 18 ]

Parameters
:   | reg | RCC\_CCIPRx register offset |
    | --- | --- |
    | shift | Position within RCC\_CCIPRx. |
    | mask | Mask for the RCC\_CCIPRx field. |
    | val | Clock value (0, 1, ... 7). |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#ae12e6bda1c30174c98303f692a42960f)STM32\_SRC\_HSI48

| #define STM32\_SRC\_HSI48   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

## [◆ ](#a542b4426a15d849545af2fd6012c520c)STM32\_SRC\_MSI

| #define STM32\_SRC\_MSI   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
| --- |

## [◆ ](#a6cd4e305697f314401e5654b4dd5f25d)STM32\_SRC\_PCLK

| #define STM32\_SRC\_PCLK   ([STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c) + 1) |
| --- |

Bus clock.

## [◆ ](#a473d0d57680b535a9e9298600a1e1aab)STM32\_SRC\_PLL\_P

| #define STM32\_SRC\_PLL\_P   ([STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d) + 1) |
| --- |

PLL clock outputs.

## [◆ ](#ab3a03011d2d433feaff934c3828e1f27)STM32\_SRC\_PLL\_Q

| #define STM32\_SRC\_PLL\_Q   ([STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab) + 1) |
| --- |

## [◆ ](#aca252b1d875fbd9dce6350f1845e5439)STM32\_SRC\_PLL\_R

| #define STM32\_SRC\_PLL\_R   ([STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27) + 1) |
| --- |

## [◆ ](#a45123bcb861fd2ed40c3ac3bf4aa4edd)SWPMI1\_SEL

| #define SWPMI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 30, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a091d597b4979c49951f880bc6ccb4d71)UART4\_SEL

| #define UART4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 6, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a136c2c36c89ebdf2c5b97686bbce0209)UART5\_SEL

| #define UART5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

Device domain clocks selection helpers.

CCIPR devices

## [◆ ](#ad67d92dfc439018a7a231e661d10d7f9)USART2\_SEL

| #define USART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 2, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#ad2f356c0bc0e43d6f629cdb840846526)USART3\_SEL

| #define USART3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 4, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32l4\_clock.h](stm32l4__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
