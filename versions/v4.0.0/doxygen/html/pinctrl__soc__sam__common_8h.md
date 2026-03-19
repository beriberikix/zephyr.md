---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl__soc__sam__common_8h.html
original_path: doxygen/html/pinctrl__soc__sam__common_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_sam\_common.h File Reference

Atmel SAM SoC specific helpers for pinctrl driver.
[More...](#details)

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <dt-bindings/pinctrl/atmel_sam_pinctrl.h>`

[Go to the source code of this file.](pinctrl__soc__sam__common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SAM\_PINCTRL\_FLAG\_GET](#ac0d76820e58e8d0ef6a65663ccd488d4)(pincfg, pos) |
|  | Obtain Flag value from [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d "Type for R-Car pin.") configuration. |
| #define | [SAM\_PINCTRL\_FLAGS\_GET](#a65850f6768e47ce900ab6ae615764570)(pincfg) |
|  | |
| #define | [SAM\_PINCTRL\_FLAGS\_DEFAULT](#a966bab3a458ab5d74319cd296f25f756)   (0U) |
|  | Pin flags/attributes . |
| #define | [SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)   (0U) |
| #define | [SAM\_PINCTRL\_FLAGS\_MASK](#a47928c213072d5e26923570e8ef14bd9)   (0x3F << [SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)) |
| #define | [SAM\_PINCTRL\_FLAG\_MASK](#aea986207fa829b606d47d4919a1fb515)   (1U) |
| #define | [SAM\_PINCTRL\_PULLUP\_POS](#a60ca2e906d19a30ac9168163301491c0)   ([SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)) |
| #define | [SAM\_PINCTRL\_PULLUP](#a72052ca63d8cac12fdb6314dc9db7f12)   (1U << [SAM\_PINCTRL\_PULLUP\_POS](#a60ca2e906d19a30ac9168163301491c0)) |
| #define | [SAM\_PINCTRL\_PULLDOWN\_POS](#a3d1ff6f736aed51318196736067db4c9)   ([SAM\_PINCTRL\_PULLUP\_POS](#a60ca2e906d19a30ac9168163301491c0) + 1U) |
| #define | [SAM\_PINCTRL\_PULLDOWN](#ac39a6835941c340ee1bb0fb71bb34c9c)   (1U << [SAM\_PINCTRL\_PULLDOWN\_POS](#a3d1ff6f736aed51318196736067db4c9)) |
| #define | [SAM\_PINCTRL\_OPENDRAIN\_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc)   ([SAM\_PINCTRL\_PULLDOWN\_POS](#a3d1ff6f736aed51318196736067db4c9) + 1U) |
| #define | [SAM\_PINCTRL\_OPENDRAIN](#a41a3c21a35fbe8baaea766ffeb56d6ea)   (1U << [SAM\_PINCTRL\_OPENDRAIN\_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc)) |
| #define | [SAM\_PINCTRL\_INPUTENABLE\_POS](#a32af1969f02a3f5ac5c92f19258c6b71)   ([SAM\_PINCTRL\_OPENDRAIN\_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc) + 1U) |
| #define | [SAM\_PINCTRL\_INPUTENABLE](#a354e8d543c70ab5affdffeda7c0e84d9)   (1U << [SAM\_PINCTRL\_INPUTENABLE\_POS](#a32af1969f02a3f5ac5c92f19258c6b71)) |
| #define | [SAM\_PINCTRL\_OUTPUTENABLE\_POS](#a078ce2bd47b20adc4d31756373a343a1)   ([SAM\_PINCTRL\_INPUTENABLE\_POS](#a32af1969f02a3f5ac5c92f19258c6b71) + 1U) |
| #define | [SAM\_PINCTRL\_OUTPUTENABLE](#a3d0d020327f4ce53c3e8a705551e01bf)   (1U << [SAM\_PINCTRL\_OUTPUTENABLE\_POS](#a078ce2bd47b20adc4d31756373a343a1)) |
| #define | [SAM\_PINCTRL\_DRIVESTRENGTH\_POS](#a984860553e4a824427b86ab627e9e48a)   ([SAM\_PINCTRL\_OUTPUTENABLE\_POS](#a078ce2bd47b20adc4d31756373a343a1) + 1U) |
| #define | [SAM\_PINCTRL\_DRIVESTRENGTH](#a510309503bbe70010329b11748f94b23)   (1U << [SAM\_PINCTRL\_DRIVESTRENGTH\_POS](#a984860553e4a824427b86ab627e9e48a)) |

## Detailed Description

Atmel SAM SoC specific helpers for pinctrl driver.

## Macro Definition Documentation

## [◆ ](#a510309503bbe70010329b11748f94b23)SAM\_PINCTRL\_DRIVESTRENGTH

| #define SAM\_PINCTRL\_DRIVESTRENGTH   (1U << [SAM\_PINCTRL\_DRIVESTRENGTH\_POS](#a984860553e4a824427b86ab627e9e48a)) |
| --- |

## [◆ ](#a984860553e4a824427b86ab627e9e48a)SAM\_PINCTRL\_DRIVESTRENGTH\_POS

| #define SAM\_PINCTRL\_DRIVESTRENGTH\_POS   ([SAM\_PINCTRL\_OUTPUTENABLE\_POS](#a078ce2bd47b20adc4d31756373a343a1) + 1U) |
| --- |

## [◆ ](#ac0d76820e58e8d0ef6a65663ccd488d4)SAM\_PINCTRL\_FLAG\_GET

| #define SAM\_PINCTRL\_FLAG\_GET | ( |  | *pincfg*, |
| --- | --- | --- | --- |
|  |  |  | *pos* ) |

**Value:**

(((pincfg) >> pos) & [SAM\_PINCTRL\_FLAG\_MASK](#aea986207fa829b606d47d4919a1fb515))

[SAM\_PINCTRL\_FLAG\_MASK](#aea986207fa829b606d47d4919a1fb515)

#define SAM\_PINCTRL\_FLAG\_MASK

**Definition** pinctrl\_soc\_sam\_common.h:83

Obtain Flag value from [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d "Type for R-Car pin.") configuration.

Parameters
:   | pincfg | [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d "Type for R-Car pin.") bit field value. |
    | --- | --- |
    | pos | attribute/flags bit position ([SAM\_PINFLAGS](#SAM_PINFLAGS)). |

## [◆ ](#aea986207fa829b606d47d4919a1fb515)SAM\_PINCTRL\_FLAG\_MASK

| #define SAM\_PINCTRL\_FLAG\_MASK   (1U) |
| --- |

## [◆ ](#a966bab3a458ab5d74319cd296f25f756)SAM\_PINCTRL\_FLAGS\_DEFAULT

| #define SAM\_PINCTRL\_FLAGS\_DEFAULT   (0U) |
| --- |

Pin flags/attributes .

## [◆ ](#a65850f6768e47ce900ab6ae615764570)SAM\_PINCTRL\_FLAGS\_GET

| #define SAM\_PINCTRL\_FLAGS\_GET | ( |  | *pincfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pincfg) >> [SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)) & [SAM\_PINCTRL\_FLAGS\_MASK](#a47928c213072d5e26923570e8ef14bd9))

[SAM\_PINCTRL\_FLAGS\_MASK](#a47928c213072d5e26923570e8ef14bd9)

#define SAM\_PINCTRL\_FLAGS\_MASK

**Definition** pinctrl\_soc\_sam\_common.h:82

[SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)

#define SAM\_PINCTRL\_FLAGS\_POS

**Definition** pinctrl\_soc\_sam\_common.h:81

## [◆ ](#a47928c213072d5e26923570e8ef14bd9)SAM\_PINCTRL\_FLAGS\_MASK

| #define SAM\_PINCTRL\_FLAGS\_MASK   (0x3F << [SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)) |
| --- |

## [◆ ](#ae42a8c43d997c40238c0cb3af2855ea8)SAM\_PINCTRL\_FLAGS\_POS

| #define SAM\_PINCTRL\_FLAGS\_POS   (0U) |
| --- |

## [◆ ](#a354e8d543c70ab5affdffeda7c0e84d9)SAM\_PINCTRL\_INPUTENABLE

| #define SAM\_PINCTRL\_INPUTENABLE   (1U << [SAM\_PINCTRL\_INPUTENABLE\_POS](#a32af1969f02a3f5ac5c92f19258c6b71)) |
| --- |

## [◆ ](#a32af1969f02a3f5ac5c92f19258c6b71)SAM\_PINCTRL\_INPUTENABLE\_POS

| #define SAM\_PINCTRL\_INPUTENABLE\_POS   ([SAM\_PINCTRL\_OPENDRAIN\_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc) + 1U) |
| --- |

## [◆ ](#a41a3c21a35fbe8baaea766ffeb56d6ea)SAM\_PINCTRL\_OPENDRAIN

| #define SAM\_PINCTRL\_OPENDRAIN   (1U << [SAM\_PINCTRL\_OPENDRAIN\_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc)) |
| --- |

## [◆ ](#af23ac8ff95ef934f2d8dd6f3727ef5fc)SAM\_PINCTRL\_OPENDRAIN\_POS

| #define SAM\_PINCTRL\_OPENDRAIN\_POS   ([SAM\_PINCTRL\_PULLDOWN\_POS](#a3d1ff6f736aed51318196736067db4c9) + 1U) |
| --- |

## [◆ ](#a3d0d020327f4ce53c3e8a705551e01bf)SAM\_PINCTRL\_OUTPUTENABLE

| #define SAM\_PINCTRL\_OUTPUTENABLE   (1U << [SAM\_PINCTRL\_OUTPUTENABLE\_POS](#a078ce2bd47b20adc4d31756373a343a1)) |
| --- |

## [◆ ](#a078ce2bd47b20adc4d31756373a343a1)SAM\_PINCTRL\_OUTPUTENABLE\_POS

| #define SAM\_PINCTRL\_OUTPUTENABLE\_POS   ([SAM\_PINCTRL\_INPUTENABLE\_POS](#a32af1969f02a3f5ac5c92f19258c6b71) + 1U) |
| --- |

## [◆ ](#ac39a6835941c340ee1bb0fb71bb34c9c)SAM\_PINCTRL\_PULLDOWN

| #define SAM\_PINCTRL\_PULLDOWN   (1U << [SAM\_PINCTRL\_PULLDOWN\_POS](#a3d1ff6f736aed51318196736067db4c9)) |
| --- |

## [◆ ](#a3d1ff6f736aed51318196736067db4c9)SAM\_PINCTRL\_PULLDOWN\_POS

| #define SAM\_PINCTRL\_PULLDOWN\_POS   ([SAM\_PINCTRL\_PULLUP\_POS](#a60ca2e906d19a30ac9168163301491c0) + 1U) |
| --- |

## [◆ ](#a72052ca63d8cac12fdb6314dc9db7f12)SAM\_PINCTRL\_PULLUP

| #define SAM\_PINCTRL\_PULLUP   (1U << [SAM\_PINCTRL\_PULLUP\_POS](#a60ca2e906d19a30ac9168163301491c0)) |
| --- |

## [◆ ](#a60ca2e906d19a30ac9168163301491c0)SAM\_PINCTRL\_PULLUP\_POS

| #define SAM\_PINCTRL\_PULLUP\_POS   ([SAM\_PINCTRL\_FLAGS\_POS](#ae42a8c43d997c40238c0cb3af2855ea8)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_soc\_sam\_common.h](pinctrl__soc__sam__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
