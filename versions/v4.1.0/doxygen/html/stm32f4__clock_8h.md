---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32f4__clock_8h.html
original_path: doxygen/html/stm32f4__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| #define | [STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
|  | PLL clock outputs. |
| #define | [STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27)   ([STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab) + 1) |
| #define | [STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439)   ([STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27) + 1) |
| #define | [STM32\_SRC\_PLLI2S\_Q](#a8b1667544712cc7844623ce4722ed76c)   ([STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439) + 1) |
|  | I2S sources. |
| #define | [STM32\_SRC\_PLLI2S\_R](#af7f88624feab3e965c74ef1789e62c5a)   ([STM32\_SRC\_PLLI2S\_Q](#a8b1667544712cc7844623ce4722ed76c) + 1) |
| #define | [STM32\_SRC\_CK48](#a9ed069ee6c3e053ea39ae391eff1f0f5)   ([STM32\_SRC\_PLLI2S\_R](#af7f88624feab3e965c74ef1789e62c5a) + 1) |
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
| #define | [MCO\_PRE\_DIV\_1](#aa6d6446aa7a1c84324475f6e8665fbb7)   0 |
| #define | [MCO\_PRE\_DIV\_2](#a36db847c7932669759f64844a15c42c3)   4 |
| #define | [MCO\_PRE\_DIV\_3](#a1d99057b6886474182adffcff4f246f2)   5 |
| #define | [MCO\_PRE\_DIV\_4](#a74c5b485d9169c489ab19e788b43c657)   6 |
| #define | [MCO\_PRE\_DIV\_5](#aad3773cb5fbea15e6cddf688dea3cd04)   7 |

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

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 23, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:35

Device domain clocks selection helpers.

CFGR devices

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 24, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 21, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 27, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 30, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#aa6d6446aa7a1c84324475f6e8665fbb7)MCO\_PRE\_DIV\_1

| #define MCO\_PRE\_DIV\_1   0 |
| --- |

## [◆ ](#a36db847c7932669759f64844a15c42c3)MCO\_PRE\_DIV\_2

| #define MCO\_PRE\_DIV\_2   4 |
| --- |

## [◆ ](#a1d99057b6886474182adffcff4f246f2)MCO\_PRE\_DIV\_3

| #define MCO\_PRE\_DIV\_3   5 |
| --- |

## [◆ ](#a74c5b485d9169c489ab19e788b43c657)MCO\_PRE\_DIV\_4

| #define MCO\_PRE\_DIV\_4   6 |
| --- |

## [◆ ](#aad3773cb5fbea15e6cddf688dea3cd04)MCO\_PRE\_DIV\_5

| #define MCO\_PRE\_DIV\_5   7 |
| --- |

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

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#a9ed069ee6c3e053ea39ae391eff1f0f5)STM32\_SRC\_CK48

| #define STM32\_SRC\_CK48   ([STM32\_SRC\_PLLI2S\_R](#af7f88624feab3e965c74ef1789e62c5a) + 1) |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#a473d0d57680b535a9e9298600a1e1aab)STM32\_SRC\_PLL\_P

| #define STM32\_SRC\_PLL\_P   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

PLL clock outputs.

## [◆ ](#ab3a03011d2d433feaff934c3828e1f27)STM32\_SRC\_PLL\_Q

| #define STM32\_SRC\_PLL\_Q   ([STM32\_SRC\_PLL\_P](#a473d0d57680b535a9e9298600a1e1aab) + 1) |
| --- |

## [◆ ](#aca252b1d875fbd9dce6350f1845e5439)STM32\_SRC\_PLL\_R

| #define STM32\_SRC\_PLL\_R   ([STM32\_SRC\_PLL\_Q](#ab3a03011d2d433feaff934c3828e1f27) + 1) |
| --- |

## [◆ ](#a8b1667544712cc7844623ce4722ed76c)STM32\_SRC\_PLLI2S\_Q

| #define STM32\_SRC\_PLLI2S\_Q   ([STM32\_SRC\_PLL\_R](#aca252b1d875fbd9dce6350f1845e5439) + 1) |
| --- |

I2S sources.

## [◆ ](#af7f88624feab3e965c74ef1789e62c5a)STM32\_SRC\_PLLI2S\_R

| #define STM32\_SRC\_PLLI2S\_R   ([STM32\_SRC\_PLLI2S\_Q](#a8b1667544712cc7844623ce4722ed76c) + 1) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f4\_clock.h](stm32f4__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
