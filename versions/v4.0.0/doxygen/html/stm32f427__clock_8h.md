---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f427__clock_8h.html
original_path: doxygen/html/stm32f427__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f427\_clock.h File Reference

[Go to the source code of this file.](stm32f427__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36)   0x8C |
|  | RCC\_DCKCFGR register offset. |
| #define | [CKDFSDM2A\_SEL](#a0d2c702f898f3c1d387ff326f55f00df)(val) |
|  | Device domain clocks selection helpers. |
| #define | [CKDFSDM1A\_SEL](#a716c5e5a49ad72a1a372e1731383bbe7)(val) |
| #define | [SAI1A\_SEL](#a2462f0bc95f94819a2936e6018e1e92a)(val) |
| #define | [SAI1B\_SEL](#a3fb1995fff0878225d9557dffeb16210)(val) |
| #define | [CLK48M\_SEL](#a4b6468847f959179fffc020d5d14439c)(val) |
| #define | [SDMMC\_SEL](#a42688c1d17e09ab58029feedd7491c0b)(val) |
| #define | [DSI\_SEL](#a2e82c24eb0c9e22635966752eebb2a05)(val) |

## Macro Definition Documentation

## [◆ ](#a716c5e5a49ad72a1a372e1731383bbe7)CKDFSDM1A\_SEL

| #define CKDFSDM1A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 15, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36)

#define DCKCFGR\_REG

RCC\_DCKCFGR register offset.

**Definition** stm32f410\_clock.h:10

## [◆ ](#a0d2c702f898f3c1d387ff326f55f00df)CKDFSDM2A\_SEL

| #define CKDFSDM2A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 14, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

Device domain clocks selection helpers.

DCKCFGR devices

## [◆ ](#a4b6468847f959179fffc020d5d14439c)CLK48M\_SEL

| #define CLK48M\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 27, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#af74c2b28a777155a9cf8c8f457b8da36)DCKCFGR\_REG

| #define DCKCFGR\_REG   0x8C |
| --- |

RCC\_DCKCFGR register offset.

## [◆ ](#a2e82c24eb0c9e22635966752eebb2a05)DSI\_SEL

| #define DSI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 29, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a2462f0bc95f94819a2936e6018e1e92a)SAI1A\_SEL

| #define SAI1A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 20, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a3fb1995fff0878225d9557dffeb16210)SAI1B\_SEL

| #define SAI1B\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 22, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a42688c1d17e09ab58029feedd7491c0b)SDMMC\_SEL

| #define SDMMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 28, [DCKCFGR\_REG](stm32f410__clock_8h.md#af74c2b28a777155a9cf8c8f457b8da36))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f427\_clock.h](stm32f427__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
