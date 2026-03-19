---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32wba__clock_8h.html
original_path: doxygen/html/stm32wba__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wba\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32wba__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Peripheral clock sources. |
| #define | [STM32\_SRC\_HSI16](#a5e1f2346bda03742e59614bf3d727be0)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_HCLK1](#af4cce65567b57af5b512a97d3aadbbc9)   ([STM32\_SRC\_HSI16](#a5e1f2346bda03742e59614bf3d727be0) + 1) |
|  | Bus clock. |
| #define | [STM32\_SRC\_HCLK5](#a9a565ff797b5d040c194e11a969e2a4f)   ([STM32\_SRC\_HCLK1](#af4cce65567b57af5b512a97d3aadbbc9) + 1) |
| #define | [STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831)   ([STM32\_SRC\_HCLK5](#a9a565ff797b5d040c194e11a969e2a4f) + 1) |
| #define | [STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3)   ([STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831) + 1) |
| #define | [STM32\_SRC\_PCLK7](#a78478906687374cfcdbec3d498895200)   ([STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3) + 1) |
| #define | [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62)   ([STM32\_SRC\_PCLK7](#a78478906687374cfcdbec3d498895200) + 1) |
|  | PLL outputs. |
| #define | [STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637)   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| #define | [STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9)   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| #define | [STM32\_SRC\_CLOCK\_MIN](#a58011c928870ee9a5f3f94298ee98ba2)   [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) |
| #define | [STM32\_SRC\_CLOCK\_MAX](#aa6f33e6e948988ae8a962860ce5ce4fc)   [STM32\_SRC\_SYSCLK](stm32__common__clocks_8h.md#a79a13b49235b90035b5ed7f62c9bf9bf) |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x088 |
|  | Bus clocks (Register address offsets). |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x08C |
| #define | [STM32\_CLOCK\_BUS\_AHB4](#a49bccabc3065f192086f16929a7b762d)   0x094 |
| #define | [STM32\_CLOCK\_BUS\_AHB5](#a623a8ba4dc47622dfbf76801f1582f58)   0x098 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x09C |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x0A0 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x0A4 |
| #define | [STM32\_CLOCK\_BUS\_APB7](#a9f9e2ac99429770af882a00dfadb1552)   0x0A8 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB7](#a9f9e2ac99429770af882a00dfadb1552) |
| #define | [STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)   0xFFU |
|  | STM32WBA clock configuration bit field. |
| #define | [STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)   0U |
| #define | [STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)   0x1FU |
| #define | [STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)   8U |
| #define | [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)   0x7U |
| #define | [STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)   13U |
| #define | [STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)   0x7U |
| #define | [STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)   16U |
| #define | [STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, mask, shift, reg) |
| #define | [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2)   0xE0 |
|  | RCC\_CCIPRx register offset (RM0493.pdf). |
| #define | [CCIPR2\_REG](#a60349691a29a48b727f302acb8025b89)   0xE4 |
| #define | [CCIPR3\_REG](#a302577067fac290b578130da822dc146)   0xE8 |
| #define | [BCDR1\_REG](#a6ec3713a2b3ac22d283abeb2d0e129bf)   0xF0 |
|  | RCC\_BCDR1 register offset (RM0493.pdf). |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | Device clk sources selection helpers. |
| #define | [USART2\_SEL](#ad67d92dfc439018a7a231e661d10d7f9)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
| #define | [SYSTICK\_SEL](#a9319a91fb044022ba812f616cf192f65)(val) |
| #define | [TIMIC\_SEL](#ad39b85aaa947648b1b833b1414116f51)(val) |
| #define | [RNG\_SEL](#abfff4355a498febbcf4ebcb237930a57)(val) |
|  | CCIPR2 devices. |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
|  | CCIPR3 devices. |
| #define | [SPI3\_SEL](#aaa096904d8a97bedc81f9a565e65c332)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [ADC\_SEL](#a635d17ad991ded52d41a6e7b0bec5773)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BCDR1 devices. |

## Macro Definition Documentation

## [◆ ](#a635d17ad991ded52d41a6e7b0bec5773)ADC\_SEL

| #define ADC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 12, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146)

#define CCIPR3\_REG

**Definition** stm32h5\_clock.h:85

## [◆ ](#a6ec3713a2b3ac22d283abeb2d0e129bf)BCDR1\_REG

| #define BCDR1\_REG   0xF0 |
| --- |

RCC\_BCDR1 register offset (RM0493.pdf).

## [◆ ](#a5a41b990eca365907d09bb4416fb22d2)CCIPR1\_REG

| #define CCIPR1\_REG   0xE0 |
| --- |

RCC\_CCIPRx register offset (RM0493.pdf).

## [◆ ](#a60349691a29a48b727f302acb8025b89)CCIPR2\_REG

| #define CCIPR2\_REG   0xE4 |
| --- |

## [◆ ](#a302577067fac290b578130da822dc146)CCIPR3\_REG

| #define CCIPR3\_REG   0xE8 |
| --- |

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 10, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

[CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)

#define CCIPR1\_REG

RCC\_CCIPRx register offset (RM0456.pdf).

**Definition** stm32h5\_clock.h:83

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 6, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 10, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#aa713f6ff001bfa6352747e7a66e3f98a)LPTIM2\_SEL

| #define LPTIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 18, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

CCIPR3 devices.

## [◆ ](#abfff4355a498febbcf4ebcb237930a57)RNG\_SEL

| #define RNG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 12, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

[CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89)

#define CCIPR2\_REG

**Definition** stm32g0\_clock.h:68

CCIPR2 devices.

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [BCDR1\_REG](#a6ec3713a2b3ac22d283abeb2d0e129bf))

[BCDR1\_REG](#a6ec3713a2b3ac22d283abeb2d0e129bf)

#define BCDR1\_REG

RCC\_BCDR1 register offset (RM0493.pdf).

**Definition** stm32wba\_clock.h:82

BCDR1 devices.

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 20, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#aaa096904d8a97bedc81f9a565e65c332)SPI3\_SEL

| #define SPI3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 3, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x088 |
| --- |

Bus clocks (Register address offsets).

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x08C |
| --- |

## [◆ ](#a49bccabc3065f192086f16929a7b762d)STM32\_CLOCK\_BUS\_AHB4

| #define STM32\_CLOCK\_BUS\_AHB4   0x094 |
| --- |

## [◆ ](#a623a8ba4dc47622dfbf76801f1582f58)STM32\_CLOCK\_BUS\_AHB5

| #define STM32\_CLOCK\_BUS\_AHB5   0x098 |
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

## [◆ ](#a9f9e2ac99429770af882a00dfadb1552)STM32\_CLOCK\_BUS\_APB7

| #define STM32\_CLOCK\_BUS\_APB7   0x0A8 |
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

STM32WBA clock configuration bit field.

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

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB7](#a9f9e2ac99429770af882a00dfadb1552) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#aa6f33e6e948988ae8a962860ce5ce4fc)STM32\_SRC\_CLOCK\_MAX

| #define STM32\_SRC\_CLOCK\_MAX   [STM32\_SRC\_SYSCLK](stm32__common__clocks_8h.md#a79a13b49235b90035b5ed7f62c9bf9bf) |
| --- |

## [◆ ](#a58011c928870ee9a5f3f94298ee98ba2)STM32\_SRC\_CLOCK\_MIN

| #define STM32\_SRC\_CLOCK\_MIN   [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) |
| --- |

## [◆ ](#af4cce65567b57af5b512a97d3aadbbc9)STM32\_SRC\_HCLK1

| #define STM32\_SRC\_HCLK1   ([STM32\_SRC\_HSI16](#a5e1f2346bda03742e59614bf3d727be0) + 1) |
| --- |

Bus clock.

## [◆ ](#a9a565ff797b5d040c194e11a969e2a4f)STM32\_SRC\_HCLK5

| #define STM32\_SRC\_HCLK5   ([STM32\_SRC\_HCLK1](#af4cce65567b57af5b512a97d3aadbbc9) + 1) |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Peripheral clock sources.

System clock Fixed clocks

## [◆ ](#a5e1f2346bda03742e59614bf3d727be0)STM32\_SRC\_HSI16

| #define STM32\_SRC\_HSI16   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#a72ffaa9863e167f47e06e91151b47831)STM32\_SRC\_PCLK1

| #define STM32\_SRC\_PCLK1   ([STM32\_SRC\_HCLK5](#a9a565ff797b5d040c194e11a969e2a4f) + 1) |
| --- |

## [◆ ](#a68f7335900538f3beb2c2d09e33376b3)STM32\_SRC\_PCLK2

| #define STM32\_SRC\_PCLK2   ([STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831) + 1) |
| --- |

## [◆ ](#a78478906687374cfcdbec3d498895200)STM32\_SRC\_PCLK7

| #define STM32\_SRC\_PCLK7   ([STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3) + 1) |
| --- |

## [◆ ](#aa074615a92c5ff479f4fbed6fdf27f62)STM32\_SRC\_PLL1\_P

| #define STM32\_SRC\_PLL1\_P   ([STM32\_SRC\_PCLK7](#a78478906687374cfcdbec3d498895200) + 1) |
| --- |

PLL outputs.

## [◆ ](#a6edb3dc598055ceeb82045fdee647637)STM32\_SRC\_PLL1\_Q

| #define STM32\_SRC\_PLL1\_Q   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| --- |

## [◆ ](#a6063632b32a970b9abbf711bab8a77c9)STM32\_SRC\_PLL1\_R

| #define STM32\_SRC\_PLL1\_R   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| --- |

## [◆ ](#a9319a91fb044022ba812f616cf192f65)SYSTICK\_SEL

| #define SYSTICK\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 22, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#ad39b85aaa947648b1b833b1414116f51)TIMIC\_SEL

| #define TIMIC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 31, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

Device clk sources selection helpers.

CCIPR1 devices

## [◆ ](#ad67d92dfc439018a7a231e661d10d7f9)USART2\_SEL

| #define USART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 2, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32wba\_clock.h](stm32wba__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
