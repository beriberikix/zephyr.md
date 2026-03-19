---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32h7rs__clock_8h.html
original_path: doxygen/html/stm32h7rs__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h7rs\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32h7rs__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_HSI\_KER](#ab574ca48f488778e54bdabcd78588ed4)   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) /\* HSI + HSIKERON \*/ |
| #define | [STM32\_SRC\_CSI\_KER](#a469a687b3d587b881bd607634251faf4)   ([STM32\_SRC\_HSI\_KER](#ab574ca48f488778e54bdabcd78588ed4) + 1) /\* CSI + CSIKERON \*/ |
| #define | [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62)   ([STM32\_SRC\_CSI\_KER](#a469a687b3d587b881bd607634251faf4) + 1) |
|  | PLL outputs. |
| #define | [STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637)   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| #define | [STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9)   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| #define | [STM32\_SRC\_PLL1\_S](#a1f1f827655145092dcab97dfe64e1635)   ([STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9) + 1) |
| #define | [STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac)   ([STM32\_SRC\_PLL1\_S](#a1f1f827655145092dcab97dfe64e1635) + 1) |
| #define | [STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717)   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| #define | [STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd)   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| #define | [STM32\_SRC\_PLL2\_S](#a889eff1dbeacc7caa4c4c7652a0d97cd)   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| #define | [STM32\_SRC\_PLL2\_T](#a723ae1f1b3d7270a9ea197c7fff27e8b)   ([STM32\_SRC\_PLL2\_S](#a889eff1dbeacc7caa4c4c7652a0d97cd) + 1) |
| #define | [STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206)   ([STM32\_SRC\_PLL2\_T](#a723ae1f1b3d7270a9ea197c7fff27e8b) + 1) |
| #define | [STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9)   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| #define | [STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a)   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| #define | [STM32\_SRC\_PLL3\_S](#a4f7f8d0ce944e5cdb1a3722d0487c73f)   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
| #define | [STM32\_SRC\_CKPER](#a8b7025d7f4be00a152c53097a414668e)   ([STM32\_SRC\_PLL3\_S](#a4f7f8d0ce944e5cdb1a3722d0487c73f) + 1) |
|  | Clock muxes. |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x138 |
|  | Others: Not yet supported. |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x13C |
| #define | [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569)   0x158 |
| #define | [STM32\_CLOCK\_BUS\_AHB4](#a49bccabc3065f192086f16929a7b762d)   0x140 |
| #define | [STM32\_CLOCK\_BUS\_AHB5](#a623a8ba4dc47622dfbf76801f1582f58)   0x134 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x148 |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x14C |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x150 |
| #define | [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51)   0x154 |
| #define | [STM32\_CLOCK\_BUS\_APB5](#a02ec780a692439efebf0bf8181bf7803)   0x144 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB5](#a623a8ba4dc47622dfbf76801f1582f58) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569) |
| #define | [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9)   0x4C |
|  | RCC\_DxCCIP register offset (RM0477.pdf). |
| #define | [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd)   0x50 |
| #define | [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda)   0x54 |
| #define | [D4CCIPR\_REG](#af95b3aebb687a8508719c0e93bda8b74)   0x58 |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x70 |
|  | RCC\_BDCR register offset. |
| #define | [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)   0x10 |
|  | RCC\_CFGRx register offset. |
| #define | [FMC\_SEL](#a0de89c03e0cd384de7f594aa5c5e82de)(val) |
|  | Device domain clocks selection helpers (RM0477.pdf). |
| #define | [SDMMC\_SEL](#a42688c1d17e09ab58029feedd7491c0b)(val) |
| #define | [XSPI1\_SEL](#a15df14366d6921bac34208b0c1af0ebb)(val) |
| #define | [XSPI2\_SEL](#a58f2e1e8be7e4e9b50783f03afc687ff)(val) |
| #define | [OTGFS\_SEL](#a90c95e4ec769bc6c8e22384ad7b77473)(val) |
| #define | [ADC\_SEL](#a635d17ad991ded52d41a6e7b0bec5773)(val) |
| #define | [CKPER\_SEL](#adc32e4d489d72766d6df1783eedf7628)(val) |
| #define | [USART234578\_SEL](#af81b9ee44136b6468393f807e70bbbf0)(val) |
|  | D2CCIPR devices. |
| #define | [SPI23\_SEL](#ad760ef96e4fd9ca527e7d9c746d1c9f3)(val) |
| #define | [I2C23\_SEL](#a490889daf5612d2f0f08b3cab473ef10)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
| #define | [I3C1\_SEL](#a576dca08c22370326fefc540bf056b81)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [FDCAN\_SEL](#ac1df6369669b4b3febd0525426e76499)(val) |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | D3CCIPR devices. |
| #define | [SPI45\_SEL](#a6919b0ea063667adb88c7c2d79877426)(val) |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [SAI2\_SEL](#a4fb9a6b79339e822f0ae426e8bba7486)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
|  | D4CCIPR devices. |
| #define | [SPI6\_SEL](#ab43d49ec71267eb1d8002909cc3360bf)(val) |
| #define | [LPTIM23\_SEL](#a07706332b9bea6a82d90e93b9ea70293)(val) |
| #define | [LPTIM45\_SEL](#ad44ca291fceaacfa1794f08034143dc8)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MCO2\_PRE](#ab02a0ccbb8588979ca4742c72c59589f)(val) |
| #define | [MCO\_PRE\_DIV\_1](#aa6d6446aa7a1c84324475f6e8665fbb7)   1 |
| #define | [MCO\_PRE\_DIV\_2](#a36db847c7932669759f64844a15c42c3)   2 |
| #define | [MCO\_PRE\_DIV\_3](#a1d99057b6886474182adffcff4f246f2)   3 |
| #define | [MCO\_PRE\_DIV\_4](#a74c5b485d9169c489ab19e788b43c657)   4 |
| #define | [MCO\_PRE\_DIV\_5](#aad3773cb5fbea15e6cddf688dea3cd04)   5 |
| #define | [MCO\_PRE\_DIV\_6](#a3cb780fda9d369607e1c51a7cddff300)   6 |
| #define | [MCO\_PRE\_DIV\_7](#a08634986618842af08073f59c6da3e8f)   7 |
| #define | [MCO\_PRE\_DIV\_8](#ad1bb69ff2fe6748978c31666f201947c)   8 |
| #define | [MCO\_PRE\_DIV\_9](#a7841c7ceb21754059717c5996a081cb4)   9 |
| #define | [MCO\_PRE\_DIV\_10](#aecc309343fad5680088593eff549748c)   10 |
| #define | [MCO\_PRE\_DIV\_11](#a3c4b271ad0c50ec7eb9edd779c30b3d9)   11 |
| #define | [MCO\_PRE\_DIV\_12](#aa93517f599cd367844383018b962319f)   12 |
| #define | [MCO\_PRE\_DIV\_13](#a3fcce904cb4650ec093f4aba0a8b7a51)   13 |
| #define | [MCO\_PRE\_DIV\_14](#aff3b9f97c2b1b70f090a7c27ca57ca58)   14 |
| #define | [MCO\_PRE\_DIV\_15](#affa380b0a33facd4d5fdd9dc405c6ddc)   15 |

## Macro Definition Documentation

## [◆ ](#a635d17ad991ded52d41a6e7b0bec5773)ADC\_SEL

| #define ADC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 24, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9)

#define D1CCIPR\_REG

RCC\_DxCCIP register offset (RM0399.pdf).

**Definition** stm32h7\_clock.h:62

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x70 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#afb2336a33a23f9671b26010594232ba3)CFGR\_REG

| #define CFGR\_REG   0x10 |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#adc32e4d489d72766d6df1783eedf7628)CKPER\_SEL

| #define CKPER\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 28, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#a9a43f736d68c30870b3f1ee545b2cff9)D1CCIPR\_REG

| #define D1CCIPR\_REG   0x4C |
| --- |

RCC\_DxCCIP register offset (RM0477.pdf).

## [◆ ](#a48fb7022d239e385aa7f41d21e43cefd)D2CCIPR\_REG

| #define D2CCIPR\_REG   0x50 |
| --- |

## [◆ ](#aeda9dd86b920e734a85ce06acbd75eda)D3CCIPR\_REG

| #define D3CCIPR\_REG   0x54 |
| --- |

## [◆ ](#af95b3aebb687a8508719c0e93bda8b74)D4CCIPR\_REG

| #define D4CCIPR\_REG   0x58 |
| --- |

## [◆ ](#ac1df6369669b4b3febd0525426e76499)FDCAN\_SEL

| #define FDCAN\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 22, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

[D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd)

#define D2CCIPR\_REG

**Definition** stm32h7rs\_clock.h:59

## [◆ ](#a0de89c03e0cd384de7f594aa5c5e82de)FMC\_SEL

| #define FMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

Device domain clocks selection helpers (RM0477.pdf).

D1CCIPR devices

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

## [◆ ](#a490889daf5612d2f0f08b3cab473ef10)I2C23\_SEL

| #define I2C23\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

## [◆ ](#a576dca08c22370326fefc540bf056b81)I3C1\_SEL

| #define I3C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

## [◆ ](#a07706332b9bea6a82d90e93b9ea70293)LPTIM23\_SEL

| #define LPTIM23\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [D4CCIPR\_REG](#af95b3aebb687a8508719c0e93bda8b74))

[D4CCIPR\_REG](#af95b3aebb687a8508719c0e93bda8b74)

#define D4CCIPR\_REG

**Definition** stm32h7rs\_clock.h:61

## [◆ ](#ad44ca291fceaacfa1794f08034143dc8)LPTIM45\_SEL

| #define LPTIM45\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [D4CCIPR\_REG](#af95b3aebb687a8508719c0e93bda8b74))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [D4CCIPR\_REG](#af95b3aebb687a8508719c0e93bda8b74))

D4CCIPR devices.

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xF, 18, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:35

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 22, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

CFGR devices.

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xF, 25, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 29, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#aa6d6446aa7a1c84324475f6e8665fbb7)MCO\_PRE\_DIV\_1

| #define MCO\_PRE\_DIV\_1   1 |
| --- |

## [◆ ](#aecc309343fad5680088593eff549748c)MCO\_PRE\_DIV\_10

| #define MCO\_PRE\_DIV\_10   10 |
| --- |

## [◆ ](#a3c4b271ad0c50ec7eb9edd779c30b3d9)MCO\_PRE\_DIV\_11

| #define MCO\_PRE\_DIV\_11   11 |
| --- |

## [◆ ](#aa93517f599cd367844383018b962319f)MCO\_PRE\_DIV\_12

| #define MCO\_PRE\_DIV\_12   12 |
| --- |

## [◆ ](#a3fcce904cb4650ec093f4aba0a8b7a51)MCO\_PRE\_DIV\_13

| #define MCO\_PRE\_DIV\_13   13 |
| --- |

## [◆ ](#aff3b9f97c2b1b70f090a7c27ca57ca58)MCO\_PRE\_DIV\_14

| #define MCO\_PRE\_DIV\_14   14 |
| --- |

## [◆ ](#affa380b0a33facd4d5fdd9dc405c6ddc)MCO\_PRE\_DIV\_15

| #define MCO\_PRE\_DIV\_15   15 |
| --- |

## [◆ ](#a36db847c7932669759f64844a15c42c3)MCO\_PRE\_DIV\_2

| #define MCO\_PRE\_DIV\_2   2 |
| --- |

## [◆ ](#a1d99057b6886474182adffcff4f246f2)MCO\_PRE\_DIV\_3

| #define MCO\_PRE\_DIV\_3   3 |
| --- |

## [◆ ](#a74c5b485d9169c489ab19e788b43c657)MCO\_PRE\_DIV\_4

| #define MCO\_PRE\_DIV\_4   4 |
| --- |

## [◆ ](#aad3773cb5fbea15e6cddf688dea3cd04)MCO\_PRE\_DIV\_5

| #define MCO\_PRE\_DIV\_5   5 |
| --- |

## [◆ ](#a3cb780fda9d369607e1c51a7cddff300)MCO\_PRE\_DIV\_6

| #define MCO\_PRE\_DIV\_6   6 |
| --- |

## [◆ ](#a08634986618842af08073f59c6da3e8f)MCO\_PRE\_DIV\_7

| #define MCO\_PRE\_DIV\_7   7 |
| --- |

## [◆ ](#ad1bb69ff2fe6748978c31666f201947c)MCO\_PRE\_DIV\_8

| #define MCO\_PRE\_DIV\_8   8 |
| --- |

## [◆ ](#a7841c7ceb21754059717c5996a081cb4)MCO\_PRE\_DIV\_9

| #define MCO\_PRE\_DIV\_9   9 |
| --- |

## [◆ ](#a90c95e4ec769bc6c8e22384ad7b77473)OTGFS\_SEL

| #define OTGFS\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 14, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [D3CCIPR\_REG](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda))

[D3CCIPR\_REG](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda)

#define D3CCIPR\_REG

**Definition** stm32h7\_clock.h:65

## [◆ ](#a4fb9a6b79339e822f0ae426e8bba7486)SAI2\_SEL

| #define SAI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [D3CCIPR\_REG](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#a42688c1d17e09ab58029feedd7491c0b)SDMMC\_SEL

| #define SDMMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 2, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [D3CCIPR\_REG](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#ad760ef96e4fd9ca527e7d9c746d1c9f3)SPI23\_SEL

| #define SPI23\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

## [◆ ](#a6919b0ea063667adb88c7c2d79877426)SPI45\_SEL

| #define SPI45\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [D3CCIPR\_REG](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#ab43d49ec71267eb1d8002909cc3360bf)SPI6\_SEL

| #define SPI6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [D4CCIPR\_REG](#af95b3aebb687a8508719c0e93bda8b74))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x138 |
| --- |

Others: Not yet supported.

Bus clocks

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x13C |
| --- |

## [◆ ](#ab2a3c819828eb0186ac3a3f15f4b4569)STM32\_CLOCK\_BUS\_AHB3

| #define STM32\_CLOCK\_BUS\_AHB3   0x158 |
| --- |

## [◆ ](#a49bccabc3065f192086f16929a7b762d)STM32\_CLOCK\_BUS\_AHB4

| #define STM32\_CLOCK\_BUS\_AHB4   0x140 |
| --- |

## [◆ ](#a623a8ba4dc47622dfbf76801f1582f58)STM32\_CLOCK\_BUS\_AHB5

| #define STM32\_CLOCK\_BUS\_AHB5   0x134 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x148 |
| --- |

## [◆ ](#ad25510091b50e823c9860089a9f23deb)STM32\_CLOCK\_BUS\_APB1\_2

| #define STM32\_CLOCK\_BUS\_APB1\_2   0x14C |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x150 |
| --- |

## [◆ ](#a537105e6125ce3b95a2d69435f47dd51)STM32\_CLOCK\_BUS\_APB4

| #define STM32\_CLOCK\_BUS\_APB4   0x154 |
| --- |

## [◆ ](#a02ec780a692439efebf0bf8181bf7803)STM32\_CLOCK\_BUS\_APB5

| #define STM32\_CLOCK\_BUS\_APB5   0x144 |
| --- |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB5](#a623a8ba4dc47622dfbf76801f1582f58) |
| --- |

## [◆ ](#a8b7025d7f4be00a152c53097a414668e)STM32\_SRC\_CKPER

| #define STM32\_SRC\_CKPER   ([STM32\_SRC\_PLL3\_S](#a4f7f8d0ce944e5cdb1a3722d0487c73f) + 1) |
| --- |

Clock muxes.

## [◆ ](#a469a687b3d587b881bd607634251faf4)STM32\_SRC\_CSI\_KER

| #define STM32\_SRC\_CSI\_KER   ([STM32\_SRC\_HSI\_KER](#ab574ca48f488778e54bdabcd78588ed4) + 1) /\* CSI + CSIKERON \*/ |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#ae12e6bda1c30174c98303f692a42960f)STM32\_SRC\_HSI48

| #define STM32\_SRC\_HSI48   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#ab574ca48f488778e54bdabcd78588ed4)STM32\_SRC\_HSI\_KER

| #define STM32\_SRC\_HSI\_KER   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) /\* HSI + HSIKERON \*/ |
| --- |

## [◆ ](#aa074615a92c5ff479f4fbed6fdf27f62)STM32\_SRC\_PLL1\_P

| #define STM32\_SRC\_PLL1\_P   ([STM32\_SRC\_CSI\_KER](#a469a687b3d587b881bd607634251faf4) + 1) |
| --- |

PLL outputs.

## [◆ ](#a6edb3dc598055ceeb82045fdee647637)STM32\_SRC\_PLL1\_Q

| #define STM32\_SRC\_PLL1\_Q   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| --- |

## [◆ ](#a6063632b32a970b9abbf711bab8a77c9)STM32\_SRC\_PLL1\_R

| #define STM32\_SRC\_PLL1\_R   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| --- |

## [◆ ](#a1f1f827655145092dcab97dfe64e1635)STM32\_SRC\_PLL1\_S

| #define STM32\_SRC\_PLL1\_S   ([STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9) + 1) |
| --- |

## [◆ ](#ae568673a4eca1b42afc59faabb5810ac)STM32\_SRC\_PLL2\_P

| #define STM32\_SRC\_PLL2\_P   ([STM32\_SRC\_PLL1\_S](#a1f1f827655145092dcab97dfe64e1635) + 1) |
| --- |

## [◆ ](#aaf0a956dda42c2a031cabce49dd3e717)STM32\_SRC\_PLL2\_Q

| #define STM32\_SRC\_PLL2\_Q   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| --- |

## [◆ ](#a57af8944eefa865aa75b6286c13a53cd)STM32\_SRC\_PLL2\_R

| #define STM32\_SRC\_PLL2\_R   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| --- |

## [◆ ](#a889eff1dbeacc7caa4c4c7652a0d97cd)STM32\_SRC\_PLL2\_S

| #define STM32\_SRC\_PLL2\_S   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| --- |

## [◆ ](#a723ae1f1b3d7270a9ea197c7fff27e8b)STM32\_SRC\_PLL2\_T

| #define STM32\_SRC\_PLL2\_T   ([STM32\_SRC\_PLL2\_S](#a889eff1dbeacc7caa4c4c7652a0d97cd) + 1) |
| --- |

## [◆ ](#a17c753e0bb8547ea9452f48a65a0a206)STM32\_SRC\_PLL3\_P

| #define STM32\_SRC\_PLL3\_P   ([STM32\_SRC\_PLL2\_T](#a723ae1f1b3d7270a9ea197c7fff27e8b) + 1) |
| --- |

## [◆ ](#a9a31a3adebff6a1eee31c287673412c9)STM32\_SRC\_PLL3\_Q

| #define STM32\_SRC\_PLL3\_Q   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| --- |

## [◆ ](#a604c22ff137a35cd1725b70991696f9a)STM32\_SRC\_PLL3\_R

| #define STM32\_SRC\_PLL3\_R   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| --- |

## [◆ ](#a4f7f8d0ce944e5cdb1a3722d0487c73f)STM32\_SRC\_PLL3\_S

| #define STM32\_SRC\_PLL3\_S   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
| --- |

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [D3CCIPR\_REG](stm32h7__clock_8h.md#aeda9dd86b920e734a85ce06acbd75eda))

D3CCIPR devices.

## [◆ ](#af81b9ee44136b6468393f807e70bbbf0)USART234578\_SEL

| #define USART234578\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [D2CCIPR\_REG](#a48fb7022d239e385aa7f41d21e43cefd))

D2CCIPR devices.

## [◆ ](#a15df14366d6921bac34208b0c1af0ebb)XSPI1\_SEL

| #define XSPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#a58f2e1e8be7e4e9b50783f03afc687ff)XSPI2\_SEL

| #define XSPI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 6, [D1CCIPR\_REG](stm32h7__clock_8h.md#a9a43f736d68c30870b3f1ee545b2cff9))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
