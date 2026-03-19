---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f4__clock_8h.html
original_path: doxygen/html/stm32f4__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f4\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32f4__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x030 |
|  | Domain clocks. |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x034 |
| #define | [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569)   0x038 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x040 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x044 |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x0A8 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| #define | [STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27)   ([STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab) + 1) |
| #define | [STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439)   ([STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27) + 1) |
| #define | [STM32\_SRC\_PLLI2S\_R](#af7f88624feab3e965c74ef1789e62c5a)   ([STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439) + 1) |
|  | I2S sources. |
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
| #define | [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)   0x08 |
|  | RCC\_CFGRx register offset. |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x70 |
|  | RCC\_BDCR register offset. |
| #define | [I2S\_SEL](#a2d34d604e16d874235b74bdbc8103bed)(val) |
|  | Device domain clocks selection helpers. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MCO2\_PRE](#ab02a0ccbb8588979ca4742c72c59589f)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |

## Macro Definition Documentation

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x70 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#afb2336a33a23f9671b26010594232ba3)CFGR\_REG

| #define CFGR\_REG   0x08 |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#a2d34d604e16d874235b74bdbc8103bed)I2S\_SEL

| #define I2S\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 23, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:63

Device domain clocks selection helpers.

CFGR devices

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 24, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)

#define STM32\_MCO\_CFGR(val, mask, shift, reg)

STM32 MCO configuration register bit field.

**Definition** stm32\_common\_clocks.h:42

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x3, 21, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 27, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x3, 30, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

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

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x030 |
| --- |

Domain clocks.

Bus clocks

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x034 |
| --- |

## [◆ ](#ab2a3c819828eb0186ac3a3f15f4b4569)STM32\_CLOCK\_BUS\_AHB3

| #define STM32\_CLOCK\_BUS\_AHB3   0x038 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x040 |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x044 |
| --- |

## [◆ ](#af7165e22b71d1beaf0dd4f59d5b4db6d)STM32\_CLOCK\_BUS\_APB3

| #define STM32\_CLOCK\_BUS\_APB3   0x0A8 |
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
:   | reg | RCC\_CFGRx register offset |
    | --- | --- |
    | shift | Position within RCC\_CFGRx. |
    | mask | Mask for the RCC\_CFGRx field. |
    | val | Clock value (0, 1, ... 7). |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#a473d0d57680b535a9e9298600a1e1aab)STM32\_SRC\_PLL\_P

| #define STM32\_SRC\_PLL\_P   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks PLL clock outputs

## [◆ ](#ab3a03011d2d433feaff934c3828e1f27)STM32\_SRC\_PLL\_Q

| #define STM32\_SRC\_PLL\_Q   ([STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab) + 1) |
| --- |

## [◆ ](#aca252b1d875fbd9dce6350f1845e5439)STM32\_SRC\_PLL\_R

| #define STM32\_SRC\_PLL\_R   ([STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27) + 1) |
| --- |

## [◆ ](#af7f88624feab3e965c74ef1789e62c5a)STM32\_SRC\_PLLI2S\_R

| #define STM32\_SRC\_PLLI2S\_R   ([STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439) + 1) |
| --- |

I2S sources.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f4\_clock.h](stm32f4__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
