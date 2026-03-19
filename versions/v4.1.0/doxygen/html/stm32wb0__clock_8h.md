---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32wb0__clock_8h.html
original_path: doxygen/html/stm32wb0__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 13, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:35

Device clk sources selection helpers.

## [◆ ](#ac7c015b568c293db3e2601cc7d8cefa6)SPI2\_I2S2\_SEL

| #define SPI2\_I2S2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 22, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ad432f60ec25ceaec41b9017bf4f62708)SPI3\_I2S3\_SEL

| #define SPI3\_I2S3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 22, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

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
