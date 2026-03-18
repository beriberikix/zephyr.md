---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32f3__clock_8h.html
original_path: doxygen/html/stm32f3__clock_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f3\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32f3__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x014 |
|  | Bus gatting clocks. |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x018 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x01c |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95) |
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
|  | Bus clock. |
| #define | [STM32\_SRC\_PLLCLK](#a4353a5ed9fb962c65382c60186c40c05)   ([STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d) + 1) |
|  | PLL clock. |
| #define | [STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)   0xFFU |
| #define | [STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)   0U |
| #define | [STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)   0x1FU |
| #define | [STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)   8U |
| #define | [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)   0x7U |
| #define | [STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)   13U |
| #define | [STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)   0x7U |
| #define | [STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)   16U |
| #define | [STM32\_CLOCK](#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, mask, shift, reg) |
|  | STM32 clock configuration bit field. |
| #define | [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)   0x04 |
|  | RCC\_CFGRx register offset. |
| #define | [CFGR3\_REG](#a949ab0a4140278eb878cd5f9f3809a00)   0x30 |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x20 |
|  | RCC\_BDCR register offset. |
| #define | [I2S\_SEL](#a2d34d604e16d874235b74bdbc8103bed)(val) |
|  | Device domain clocks selection helpers). |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | CFGR3 devices. |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I2C2\_SEL](#abdd79c9ce90458b53e81123d181fed98)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [TIM1\_SEL](#a72d364c49d3cb708b3b522240c7f2487)(val) |
| #define | [TIM8\_SEL](#a4265e0738cb6943d25db9a1425529034)(val) |
| #define | [TIM15\_SEL](#aec6c3536cdaa8545becc5d4575947ee1)(val) |
| #define | [TIM16\_SEL](#accdaf25454de23be65aa2865389c9c3d)(val) |
| #define | [TIM17\_SEL](#a584d523b64f1a5d31e44ba0ddb24a189)(val) |
| #define | [TIM20\_SEL](#a0044430b188b9104418943111be2cc01)(val) |
| #define | [USART2\_SEL](#ad67d92dfc439018a7a231e661d10d7f9)(val) |
| #define | [USART3\_SEL](#ad2f356c0bc0e43d6f629cdb840846526)(val) |
| #define | [USART4\_SEL](#aced9e983095cb40bc18f3a66e3818c98)(val) |
| #define | [USART5\_SEL](#a6a45e0ef8bd196574e241aefdb3a5350)(val) |
| #define | [TIM2\_SEL](#ae9e7ae1c9e0378ef4ec0d435d4449a16)(val) |
| #define | [TIM3\_4\_SEL](#abc0a25466b329ed2797a6f223f7c7e3a)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |

## Macro Definition Documentation

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x20 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#a949ab0a4140278eb878cd5f9f3809a00)CFGR3\_REG

| #define CFGR3\_REG   0x30 |
| --- |

## [◆ ](#afb2336a33a23f9671b26010594232ba3)CFGR\_REG

| #define CFGR\_REG   0x04 |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 4, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)

#define STM32\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00)

#define CFGR3\_REG

RCC\_CFGRx register offset.

**Definition** stm32f0\_clock.h:62

## [◆ ](#abdd79c9ce90458b53e81123d181fed98)I2C2\_SEL

| #define I2C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 5, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 6, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a2d34d604e16d874235b74bdbc8103bed)I2S\_SEL

| #define I2S\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 23, [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3))

[CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:63

Device domain clocks selection helpers).

CFGR devices

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 8, [BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a))

[BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)

#define BDCR\_REG

RCC\_BDCR register offset.

**Definition** stm32f0\_clock.h:65

BDCR devices.

## [◆ ](#a91fa38e1c3f4afa5d23b2bbc885c2bb9)STM32\_CLOCK

| #define STM32\_CLOCK | ( |  | *val*, |
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
:   | reg | RCC\_CFGRx register offset |
    | --- | --- |
    | shift | Position within RCC\_CFGRx. |
    | mask | Mask for the RCC\_CFGRx field. |
    | val | Clock value (0, 1, ... 7). |

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x014 |
| --- |

Bus gatting clocks.

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x01c |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x018 |
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

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#a6cd4e305697f314401e5654b4dd5f25d)STM32\_SRC\_PCLK

| #define STM32\_SRC\_PCLK   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

Bus clock.

## [◆ ](#a4353a5ed9fb962c65382c60186c40c05)STM32\_SRC\_PLLCLK

| #define STM32\_SRC\_PLLCLK   ([STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d) + 1) |
| --- |

PLL clock.

## [◆ ](#aec6c3536cdaa8545becc5d4575947ee1)TIM15\_SEL

| #define TIM15\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 10, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#accdaf25454de23be65aa2865389c9c3d)TIM16\_SEL

| #define TIM16\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 11, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a584d523b64f1a5d31e44ba0ddb24a189)TIM17\_SEL

| #define TIM17\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 13, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a72d364c49d3cb708b3b522240c7f2487)TIM1\_SEL

| #define TIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 8, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a0044430b188b9104418943111be2cc01)TIM20\_SEL

| #define TIM20\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 15, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#ae9e7ae1c9e0378ef4ec0d435d4449a16)TIM2\_SEL

| #define TIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 24, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#abc0a25466b329ed2797a6f223f7c7e3a)TIM3\_4\_SEL

| #define TIM3\_4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 25, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a4265e0738cb6943d25db9a1425529034)TIM8\_SEL

| #define TIM8\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 9, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 0, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

CFGR3 devices.

## [◆ ](#ad67d92dfc439018a7a231e661d10d7f9)USART2\_SEL

| #define USART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 16, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#ad2f356c0bc0e43d6f629cdb840846526)USART3\_SEL

| #define USART3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 18, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#aced9e983095cb40bc18f3a66e3818c98)USART4\_SEL

| #define USART4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 20, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

## [◆ ](#a6a45e0ef8bd196574e241aefdb3a5350)USART5\_SEL

| #define USART5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 22, [CFGR3\_REG](stm32f0__clock_8h.md#a949ab0a4140278eb878cd5f9f3809a00))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f3\_clock.h](stm32f3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
