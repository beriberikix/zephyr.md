---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32f410__clock_8h.html
original_path: doxygen/html/stm32f410__clock_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f410\_clock.h File Reference

[Go to the source code of this file.](stm32f410__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36)   0x8C |
|  | RCC\_DCKCFGR register offset. |
| #define | [DCKCFGR2\_REG](#a3a648b98a1f91abbce18297038ba3e5f)   0x94 |
| #define | [CKDFSDM2A\_SEL](#a0d2c702f898f3c1d387ff326f55f00df)(val) |
|  | Device domain clocks selection helpers. |
| #define | [CKDFSDM1A\_SEL](#a716c5e5a49ad72a1a372e1731383bbe7)(val) |
| #define | [SAI1A\_SEL](#a2462f0bc95f94819a2936e6018e1e92a)(val) |
| #define | [SAI1B\_SEL](#a3fb1995fff0878225d9557dffeb16210)(val) |
| #define | [I2S1\_SEL](#abee394167f826cac3ec58db3e89dd092)(val) |
| #define | [I2S2\_SEL](#a00a15803773ade4655e63cc48b8e59ea)(val) |
| #define | [CKDFSDM\_SEL](#a62f4679935575cef0f3c40b48494be49)(val) |
| #define | [I2CFMP1\_SEL](#a8a02c7d6228c992585fc8275751121d4)(val) |
|  | DCKCFGR2 devices. |
| #define | [CK48M\_SEL](#a9629b95b8e2c432e890c69727b52a4d4)(val) |
| #define | [SDIO\_SEL](#a9dbb3de5ec91ea2898c73fa87817af67)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |

## Macro Definition Documentation

## [◆ ](#a9629b95b8e2c432e890c69727b52a4d4)CK48M\_SEL

| #define CK48M\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 27, [DCKCFGR2\_REG](#a3a648b98a1f91abbce18297038ba3e5f))

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)

#define STM32\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[DCKCFGR2\_REG](#a3a648b98a1f91abbce18297038ba3e5f)

#define DCKCFGR2\_REG

**Definition** stm32f410\_clock.h:11

## [◆ ](#a716c5e5a49ad72a1a372e1731383bbe7)CKDFSDM1A\_SEL

| #define CKDFSDM1A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 15, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

[DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36)

#define DCKCFGR\_REG

RCC\_DCKCFGR register offset.

**Definition** stm32f410\_clock.h:10

## [◆ ](#a0d2c702f898f3c1d387ff326f55f00df)CKDFSDM2A\_SEL

| #define CKDFSDM2A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 14, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

Device domain clocks selection helpers.

DCKCFGR devices

## [◆ ](#a62f4679935575cef0f3c40b48494be49)CKDFSDM\_SEL

| #define CKDFSDM\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 31, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a3a648b98a1f91abbce18297038ba3e5f)DCKCFGR2\_REG

| #define DCKCFGR2\_REG   0x94 |
| --- |

## [◆ ](#af74c2b28a777155a9cf8c8f457b8da36)DCKCFGR\_REG

| #define DCKCFGR\_REG   0x8C |
| --- |

RCC\_DCKCFGR register offset.

## [◆ ](#a8a02c7d6228c992585fc8275751121d4)I2CFMP1\_SEL

| #define I2CFMP1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 22, [DCKCFGR2\_REG](#a3a648b98a1f91abbce18297038ba3e5f))

DCKCFGR2 devices.

## [◆ ](#abee394167f826cac3ec58db3e89dd092)I2S1\_SEL

| #define I2S1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 25, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a00a15803773ade4655e63cc48b8e59ea)I2S2\_SEL

| #define I2S2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 27, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 30, [DCKCFGR2\_REG](#a3a648b98a1f91abbce18297038ba3e5f))

## [◆ ](#a2462f0bc95f94819a2936e6018e1e92a)SAI1A\_SEL

| #define SAI1A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 20, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a3fb1995fff0878225d9557dffeb16210)SAI1B\_SEL

| #define SAI1B\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 3, 22, [DCKCFGR\_REG](#af74c2b28a777155a9cf8c8f457b8da36))

## [◆ ](#a9dbb3de5ec91ea2898c73fa87817af67)SDIO\_SEL

| #define SDIO\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_CLOCK](stm32c0__clock_8h.md#a91fa38e1c3f4afa5d23b2bbc885c2bb9)(val, 1, 28, [DCKCFGR2\_REG](#a3a648b98a1f91abbce18297038ba3e5f))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f410\_clock.h](stm32f410__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
