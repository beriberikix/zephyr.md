---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32wb0__clock_8h.html
original_path: doxygen/html/stm32wb0__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wb0\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32wb0__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_CLKSLOWMUX](#a577b1cb1a04e486119c9834374728190)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Define system & low-speed clocks. |
| #define | [STM32\_SRC\_CLK16MHZ](#a7495e637711c2545d1450de275ea0e72)   ([STM32\_SRC\_CLKSLOWMUX](#a577b1cb1a04e486119c9834374728190) + 1) |
| #define | [STM32\_SRC\_CLK32MHZ](#a41eda33344045e079dba6b5858b15315)   ([STM32\_SRC\_CLK16MHZ](#a7495e637711c2545d1450de275ea0e72) + 1) |
| #define | [STM32\_CLOCK\_BUS\_AHB0](#afebca0f2112b116cb43cc8759c0e5580)   0x50 |
|  | Bus clocks. |
| #define | [STM32\_CLOCK\_BUS\_APB0](#a479869134499d0ddd172b0cbede44ea1)   0x54 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x58 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x60 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB0](#afebca0f2112b116cb43cc8759c0e5580) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db) |
| #define | [STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)   (0xFFFFU) |
| #define | [STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)   (0U) |
| #define | [STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)   (0x3FU) |
| #define | [STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)   (16U) |
| #define | [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)   (0x1FU) |
| #define | [STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)   (22U) |
| #define | [STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)   [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9) |
| #define | [STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)   (27U) |
| #define | [STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, mask, shift, reg) |
|  | STM32 clock configuration bit field. |
| #define | [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)   0x08 |
|  | RCC\_CFGR register offset. |
| #define | [APB2ENR\_REG](#a54b415b2adb40a9ddfa18049a94621fd)   0x60 |
|  | RCC\_APB2ENR register offset. |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
|  | Device clk sources selection helpers. |
| #define | [SPI2\_I2S2\_SEL](#ac7c015b568c293db3e2601cc7d8cefa6)(val) |
| #define | [SPI3\_I2S3\_SEL](#ad432f60ec25ceaec41b9017bf4f62708)(val) |

## Macro Definition Documentation

## [◆ ](#a54b415b2adb40a9ddfa18049a94621fd)APB2ENR\_REG

| #define APB2ENR\_REG   0x60 |
| --- |

RCC\_APB2ENR register offset.

## [◆ ](#afb2336a33a23f9671b26010594232ba3)CFGR\_REG

| #define CFGR\_REG   0x08 |
| --- |

RCC\_CFGR register offset.

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 13, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)) /\* WB05/WB09 only \*/

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:63

Device clk sources selection helpers.

## [◆ ](#ac7c015b568c293db3e2601cc7d8cefa6)SPI2\_I2S2\_SEL

| #define SPI2\_I2S2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 22, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)) /\* WB06/WB07 only \*/

## [◆ ](#ad432f60ec25ceaec41b9017bf4f62708)SPI3\_I2S3\_SEL

| #define SPI3\_I2S3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 22, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#afebca0f2112b116cb43cc8759c0e5580)STM32\_CLOCK\_BUS\_AHB0

| #define STM32\_CLOCK\_BUS\_AHB0   0x50 |
| --- |

Bus clocks.

## [◆ ](#a479869134499d0ddd172b0cbede44ea1)STM32\_CLOCK\_BUS\_APB0

| #define STM32\_CLOCK\_BUS\_APB0   0x54 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x58 |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x60 |
| --- |

## [◆ ](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)STM32\_CLOCK\_MASK\_MASK

| #define STM32\_CLOCK\_MASK\_MASK   (0x1FU) |
| --- |

## [◆ ](#abfdb31d824fc5c6cf809a1dcff022b5d)STM32\_CLOCK\_MASK\_SHIFT

| #define STM32\_CLOCK\_MASK\_SHIFT   (22U) |
| --- |

## [◆ ](#a33d66849c63db64784317260b06ceb24)STM32\_CLOCK\_REG\_MASK

| #define STM32\_CLOCK\_REG\_MASK   (0xFFFFU) |
| --- |

## [◆ ](#a2e73bdb1691751ffd616a5c4e2762423)STM32\_CLOCK\_REG\_SHIFT

| #define STM32\_CLOCK\_REG\_SHIFT   (0U) |
| --- |

## [◆ ](#af3001a7541ea4df9e4948fd559352f60)STM32\_CLOCK\_SHIFT\_MASK

| #define STM32\_CLOCK\_SHIFT\_MASK   (0x3FU) |
| --- |

## [◆ ](#a147846b77bd51e42c85bea5aca50ad4f)STM32\_CLOCK\_SHIFT\_SHIFT

| #define STM32\_CLOCK\_SHIFT\_SHIFT   (16U) |
| --- |

## [◆ ](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)STM32\_CLOCK\_VAL\_MASK

| #define STM32\_CLOCK\_VAL\_MASK   [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9) |
| --- |

## [◆ ](#adf2ca8c7f707b82b7ec4820dfc32929a)STM32\_CLOCK\_VAL\_SHIFT

| #define STM32\_CLOCK\_VAL\_SHIFT   (27U) |
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

Parameters
:   | reg | Offset to target configuration register in RCC |
    | --- | --- |
    | shift | Position of field within RCC register (= field LSB's index) |
    | mask | Mask of field in RCC register |
    | val | Field value |

Note
:   'reg' range: 0x0~0xFFFF [ 00 : 15 ]
:   'shift' range: 0~63 [ 16 : 21 ]
:   'mask' range: 0x00~0x1F [ 22 : 26 ]
:   'val' range: 0x00~0x1F [ 27 : 31 ]

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB0](#afebca0f2112b116cb43cc8759c0e5580) |
| --- |

## [◆ ](#a7495e637711c2545d1450de275ea0e72)STM32\_SRC\_CLK16MHZ

| #define STM32\_SRC\_CLK16MHZ   ([STM32\_SRC\_CLKSLOWMUX](#a577b1cb1a04e486119c9834374728190) + 1) |
| --- |

## [◆ ](#a41eda33344045e079dba6b5858b15315)STM32\_SRC\_CLK32MHZ

| #define STM32\_SRC\_CLK32MHZ   ([STM32\_SRC\_CLK16MHZ](#a7495e637711c2545d1450de275ea0e72) + 1) |
| --- |

## [◆ ](#a577b1cb1a04e486119c9834374728190)STM32\_SRC\_CLKSLOWMUX

| #define STM32\_SRC\_CLKSLOWMUX   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Define system & low-speed clocks.

Other fixed clocks.

- CLKSLOWMUX: used to query slow clock tree frequency
- CLK16MHZ: secondary clock for LPUART, SPI3/I2S and BLE
- CLK32MHZ: secondary clock for SPI3/I2S and BLE

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32wb0\_clock.h](stm32wb0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
