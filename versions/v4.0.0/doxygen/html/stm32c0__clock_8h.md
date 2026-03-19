---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32c0__clock_8h.html
original_path: doxygen/html/stm32c0__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| #define | [STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
| #define | [STM32\_SRC\_PCLK](#a6cd4e305697f314401e5654b4dd5f25d)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
|  | Peripheral bus clock. |
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

## Macro Definition Documentation

## [◆ ](#a635d17ad991ded52d41a6e7b0bec5773)ADC\_SEL

| #define ADC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 30, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

[STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260)

#define CCIPR\_REG

RCC\_CCIPR register offset.

**Definition** stm32c0\_clock.h:61

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

[STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 12, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#ab6681395c0ed012d399bb8da480cc577)I2C2\_I2S1\_SEL

| #define I2C2\_I2S1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 14, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 28, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)

#define STM32\_MCO\_CFGR(val, mask, shift, reg)

STM32 MCO configuration register bit field.

**Definition** stm32\_common\_clocks.h:42

[CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:67

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 24, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

CFGR1 devices.

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 20, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 16, [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6))

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [CSR1\_REG](#aef1dabdfdb37922d3876f12a7ef193b4))

[CSR1\_REG](#aef1dabdfdb37922d3876f12a7ef193b4)

#define CSR1\_REG

RCC\_CSR1 register offset.

**Definition** stm32c0\_clock.h:64

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

((((reg) & [STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)) << [STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)) | \

(((shift) & [STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)) << [STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)) | \

(((mask) & [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)) << [STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)) | \

(((val) & [STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)) << [STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)))

[STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)

#define STM32\_CLOCK\_SHIFT\_SHIFT

**Definition** stm32c0\_clock.h:35

[STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)

#define STM32\_CLOCK\_REG\_SHIFT

**Definition** stm32c0\_clock.h:33

[STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)

#define STM32\_CLOCK\_REG\_MASK

**Definition** stm32c0\_clock.h:32

[STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)

#define STM32\_CLOCK\_MASK\_MASK

**Definition** stm32c0\_clock.h:36

[STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)

#define STM32\_CLOCK\_VAL\_MASK

**Definition** stm32c0\_clock.h:38

[STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)

#define STM32\_CLOCK\_MASK\_SHIFT

**Definition** stm32c0\_clock.h:37

[STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)

#define STM32\_CLOCK\_VAL\_SHIFT

**Definition** stm32c0\_clock.h:39

[STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)

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

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_IOP](#afe5b12955e87bbfcee6107cc30e45566) |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) |
| --- |

## [◆ ](#ae12e6bda1c30174c98303f692a42960f)STM32\_SRC\_HSI48

| #define STM32\_SRC\_HSI48   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
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

[STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [CCIPR\_REG](#af50f81a20c6e91a7a8611d1e59ca6260))

Device domain clocks selection helpers.

CCIPR devices

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32c0\_clock.h](stm32c0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
