---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f10x__clock_8h.html
original_path: doxygen/html/stm32f10x__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f10x\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`  
`#include "[stm32f1_clock.h](stm32f1__clock_8h_source.md)"`

[Go to the source code of this file.](stm32f10x__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_PLL2CLK](#acabf91f55d604e7e6b3930d5fb4051c5)   ([STM32\_SRC\_PLLCLK](stm32f0__clock_8h.md#a4353a5ed9fb962c65382c60186c40c05) + 1) |
|  | Fixed clocks. |
| #define | [STM32\_SRC\_PLL3CLK](#ae5acc6d7e207c27d90f2e6d77fac9d5d)   ([STM32\_SRC\_PLL2CLK](#acabf91f55d604e7e6b3930d5fb4051c5) + 1) |
| #define | [STM32\_SRC\_EXT\_HSE](#a3afc97af21308c71d21b59d53946efad)   ([STM32\_SRC\_PLL3CLK](#ae5acc6d7e207c27d90f2e6d77fac9d5d) + 1) |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR1 devices. |

## Macro Definition Documentation

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0xF, 24, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)

#define STM32\_MCO\_CFGR(val, mask, shift, reg)

STM32 MCO configuration register bit field.

**Definition** stm32\_common\_clocks.h:42

[CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:67

CFGR1 devices.

## [◆ ](#a3afc97af21308c71d21b59d53946efad)STM32\_SRC\_EXT\_HSE

| #define STM32\_SRC\_EXT\_HSE   ([STM32\_SRC\_PLL3CLK](#ae5acc6d7e207c27d90f2e6d77fac9d5d) + 1) |
| --- |

## [◆ ](#acabf91f55d604e7e6b3930d5fb4051c5)STM32\_SRC\_PLL2CLK

| #define STM32\_SRC\_PLL2CLK   ([STM32\_SRC\_PLLCLK](stm32f0__clock_8h.md#a4353a5ed9fb962c65382c60186c40c05) + 1) |
| --- |

Fixed clocks.

## [◆ ](#ae5acc6d7e207c27d90f2e6d77fac9d5d)STM32\_SRC\_PLL3CLK

| #define STM32\_SRC\_PLL3CLK   ([STM32\_SRC\_PLL2CLK](#acabf91f55d604e7e6b3930d5fb4051c5) + 1) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32f10x\_clock.h](stm32f10x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
