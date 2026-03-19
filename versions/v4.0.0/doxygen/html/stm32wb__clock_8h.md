---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32wb__clock_8h.html
original_path: doxygen/html/stm32wb__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wb\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32wb__clock_8h_source.md)

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
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c) + 1) |
| #define | [STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
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
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x90 |
|  | RCC\_BDCR register offset. |
| #define | [CSR\_REG](#a16c4f3ac8a8c6255620516b3a32b7a70)   0x94 |
|  | RCC\_CSR register offset. |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device domain clocks selection helpers. |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [CLK48\_SEL](#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)(val) |
| #define | [ADC\_SEL](#a635d17ad991ded52d41a6e7b0bec5773)(val) |
| #define | [RNG\_SEL](#abfff4355a498febbcf4ebcb237930a57)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |
| #define | [RFWKP\_SEL](#a1812acd6f7e09cbe8f6f6c4fc7fe6f13)(val) |
|  | CSR devices. |

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

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x90 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#af50f81a20c6e91a7a8611d1e59ca6260)CCIPR\_REG

| #define CCIPR\_REG   0x88 |
| --- |

RCC\_CCIPR register offset.

## [◆ ](#a3f3b40e4fdebc11d7a2dd4a86e1fefc8)CLK48\_SEL

| #define CLK48\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 26, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a16c4f3ac8a8c6255620516b3a32b7a70)CSR\_REG

| #define CSR\_REG   0x94 |
| --- |

RCC\_CSR register offset.

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 12, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 16, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

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

## [◆ ](#a1812acd6f7e09cbe8f6f6c4fc7fe6f13)RFWKP\_SEL

| #define RFWKP\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 14, [CSR\_REG](stm32l0__clock_8h.md#a16c4f3ac8a8c6255620516b3a32b7a70))

[CSR\_REG](stm32l0__clock_8h.md#a16c4f3ac8a8c6255620516b3a32b7a70)

#define CSR\_REG

RCC\_CSR register offset.

**Definition** stm32l0\_clock.h:66

CSR devices.

## [◆ ](#abfff4355a498febbcf4ebcb237930a57)RNG\_SEL

| #define RNG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 30, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

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

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c) + 1) |
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

| #define STM32\_SRC\_PCLK   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
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

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [CCIPR\_REG](stm32c0__clock_8h.md#af50f81a20c6e91a7a8611d1e59ca6260))

Device domain clocks selection helpers.

CCIPR devices

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32wb\_clock.h](stm32wb__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
