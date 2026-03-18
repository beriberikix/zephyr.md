---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/max32-pinctrl_8h.html
original_path: doxygen/html/max32-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32-pinctrl.h File Reference

[Go to the source code of this file.](max32-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MAX32\_MODE\_GPIO](#a7087cd825f7f43739fa57ce0a4e4297d)   0x00 |
|  | Pin modes. |
| #define | [MAX32\_MODE\_AF1](#a4e3439dc886a1ed097d698847ab3cb92)   0x01 |
| #define | [MAX32\_MODE\_AF2](#af4e13cd1ef71b77ae882aadb467e5115)   0x02 |
| #define | [MAX32\_MODE\_AF3](#a33afd156fac8c0ccb588230b3f787947)   0x03 |
| #define | [MAX32\_MODE\_AF4](#a6112caaab6ce78c337c40adfa1977a90)   0x04 |
| #define | [MAX32\_MODE\_AF5](#aae02581685aaeb495a8ea2bbabe0999b)   0x05 |
| #define | [MAX32\_MODE\_SHIFT](#ac45646bd5514a406cbb87dc24a3a2f4c)   0U |
|  | Mode, port, pin shift number. |
| #define | [MAX32\_MODE\_MASK](#a071a95ac6147954a5b9086cc27f02ce0)   0x0FU |
| #define | [MAX32\_PORT\_SHIFT](#ad103d747f01d57dc2cbc547fde45c988)   4U |
| #define | [MAX32\_PORT\_MASK](#a668dddf52782f061e623e8d0837ba513)   0x0FU |
| #define | [MAX32\_PIN\_SHIFT](#aa3b3d363ef790d1def3402ceb47b2f97)   8U |
| #define | [MAX32\_PIN\_MASK](#abf4c75ee139d0abcc10ab3c4fe116ae2)   0xFFU |
| #define | [MAX32\_PINMUX](#a6af2b3feddf92906fe3ba315b8debc41)(port, pin, mode) |
|  | Pin configuration bit field. |
| #define | [MAX32\_PINMUX\_PORT](#a9e2b0cc6ad6fb0e043f805be98900cad)(pinmux) |
| #define | [MAX32\_PINMUX\_PIN](#ae9b72f2da84eca73ba5d0958946d2d6e)(pinmux) |
| #define | [MAX32\_PINMUX\_MODE](#a1f3ef03ff93e7fe57781eb831aaf5afb)(pinmux) |
| #define | [MAX32\_VSEL\_VDDIO](#a4e18fd313d30f6f69376cd769ea2347c)   0 |
| #define | [MAX32\_VSEL\_VDDIOH](#a6c2d4fea363165d857f5a79608d52aa0)   1 |
| #define | [MAX32\_INPUT\_ENABLE\_SHIFT](#a05fd9141c140ccf54d0723a3511d0c9b)   0x00 |
|  | Pin configuration. |
| #define | [MAX32\_BIAS\_PULL\_UP\_SHIFT](#a6ffa10ef6074415084575c88a12069cc)   0x01 |
| #define | [MAX32\_BIAS\_PULL\_DOWN\_SHIFT](#afa7dd8f4020995627e8b9f2ee60316bd)   0x02 |
| #define | [MAX32\_OUTPUT\_ENABLE\_SHIFT](#a3f1a5cd6c9da2ad726155b40a9cea865)   0x03 |
| #define | [MAX32\_POWER\_SOURCE\_SHIFT](#a88dcd8d7eee992eecd0e430a667d3353)   0x04 |
| #define | [MAX32\_OUTPUT\_HIGH\_SHIFT](#aa8cf639ff885ef23a51857b56bc6f113)   0x05 |
| #define | [MAX32\_DRV\_STRENGTH\_SHIFT](#a1082e5021dc5bcceb337a6286c3d69a2)   0x06 /\* 2 bits \*/ |

## Macro Definition Documentation

## [◆ ](#afa7dd8f4020995627e8b9f2ee60316bd)MAX32\_BIAS\_PULL\_DOWN\_SHIFT

| #define MAX32\_BIAS\_PULL\_DOWN\_SHIFT   0x02 |
| --- |

## [◆ ](#a6ffa10ef6074415084575c88a12069cc)MAX32\_BIAS\_PULL\_UP\_SHIFT

| #define MAX32\_BIAS\_PULL\_UP\_SHIFT   0x01 |
| --- |

## [◆ ](#a1082e5021dc5bcceb337a6286c3d69a2)MAX32\_DRV\_STRENGTH\_SHIFT

| #define MAX32\_DRV\_STRENGTH\_SHIFT   0x06 /\* 2 bits \*/ |
| --- |

## [◆ ](#a05fd9141c140ccf54d0723a3511d0c9b)MAX32\_INPUT\_ENABLE\_SHIFT

| #define MAX32\_INPUT\_ENABLE\_SHIFT   0x00 |
| --- |

Pin configuration.

## [◆ ](#a4e3439dc886a1ed097d698847ab3cb92)MAX32\_MODE\_AF1

| #define MAX32\_MODE\_AF1   0x01 |
| --- |

## [◆ ](#af4e13cd1ef71b77ae882aadb467e5115)MAX32\_MODE\_AF2

| #define MAX32\_MODE\_AF2   0x02 |
| --- |

## [◆ ](#a33afd156fac8c0ccb588230b3f787947)MAX32\_MODE\_AF3

| #define MAX32\_MODE\_AF3   0x03 |
| --- |

## [◆ ](#a6112caaab6ce78c337c40adfa1977a90)MAX32\_MODE\_AF4

| #define MAX32\_MODE\_AF4   0x04 |
| --- |

## [◆ ](#aae02581685aaeb495a8ea2bbabe0999b)MAX32\_MODE\_AF5

| #define MAX32\_MODE\_AF5   0x05 |
| --- |

## [◆ ](#a7087cd825f7f43739fa57ce0a4e4297d)MAX32\_MODE\_GPIO

| #define MAX32\_MODE\_GPIO   0x00 |
| --- |

Pin modes.

## [◆ ](#a071a95ac6147954a5b9086cc27f02ce0)MAX32\_MODE\_MASK

| #define MAX32\_MODE\_MASK   0x0FU |
| --- |

## [◆ ](#ac45646bd5514a406cbb87dc24a3a2f4c)MAX32\_MODE\_SHIFT

| #define MAX32\_MODE\_SHIFT   0U |
| --- |

Mode, port, pin shift number.

## [◆ ](#a3f1a5cd6c9da2ad726155b40a9cea865)MAX32\_OUTPUT\_ENABLE\_SHIFT

| #define MAX32\_OUTPUT\_ENABLE\_SHIFT   0x03 |
| --- |

## [◆ ](#aa8cf639ff885ef23a51857b56bc6f113)MAX32\_OUTPUT\_HIGH\_SHIFT

| #define MAX32\_OUTPUT\_HIGH\_SHIFT   0x05 |
| --- |

## [◆ ](#abf4c75ee139d0abcc10ab3c4fe116ae2)MAX32\_PIN\_MASK

| #define MAX32\_PIN\_MASK   0xFFU |
| --- |

## [◆ ](#aa3b3d363ef790d1def3402ceb47b2f97)MAX32\_PIN\_SHIFT

| #define MAX32\_PIN\_SHIFT   8U |
| --- |

## [◆ ](#a6af2b3feddf92906fe3ba315b8debc41)MAX32\_PINMUX

| #define MAX32\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *mode* ) |

**Value:**

((((port)&[MAX32\_PORT\_MASK](#a668dddf52782f061e623e8d0837ba513)) << [MAX32\_PORT\_SHIFT](#ad103d747f01d57dc2cbc547fde45c988)) | \

(((pin)&[MAX32\_PIN\_MASK](#abf4c75ee139d0abcc10ab3c4fe116ae2)) << [MAX32\_PIN\_SHIFT](#aa3b3d363ef790d1def3402ceb47b2f97)) | \

(((MAX32\_MODE\_##mode) & [MAX32\_MODE\_MASK](#a071a95ac6147954a5b9086cc27f02ce0)) << [MAX32\_MODE\_SHIFT](#ac45646bd5514a406cbb87dc24a3a2f4c)))

[MAX32\_MODE\_MASK](#a071a95ac6147954a5b9086cc27f02ce0)

#define MAX32\_MODE\_MASK

**Definition** max32-pinctrl.h:24

[MAX32\_PORT\_MASK](#a668dddf52782f061e623e8d0837ba513)

#define MAX32\_PORT\_MASK

**Definition** max32-pinctrl.h:26

[MAX32\_PIN\_SHIFT](#aa3b3d363ef790d1def3402ceb47b2f97)

#define MAX32\_PIN\_SHIFT

**Definition** max32-pinctrl.h:27

[MAX32\_PIN\_MASK](#abf4c75ee139d0abcc10ab3c4fe116ae2)

#define MAX32\_PIN\_MASK

**Definition** max32-pinctrl.h:28

[MAX32\_MODE\_SHIFT](#ac45646bd5514a406cbb87dc24a3a2f4c)

#define MAX32\_MODE\_SHIFT

Mode, port, pin shift number.

**Definition** max32-pinctrl.h:23

[MAX32\_PORT\_SHIFT](#ad103d747f01d57dc2cbc547fde45c988)

#define MAX32\_PORT\_SHIFT

**Definition** max32-pinctrl.h:25

Pin configuration bit field.

Fields:

- mode [ 0 : 3 ]
- port [ 4 : 7 ]
- pin [ 8 : 15 ]

Parameters
:   | port | Port (0 .. 15) |
    | --- | --- |
    | pin | Pin (0..31) |
    | mode | Mode (GPIO, AF1, AF2...). |

## [◆ ](#a1f3ef03ff93e7fe57781eb831aaf5afb)MAX32\_PINMUX\_MODE

| #define MAX32\_PINMUX\_MODE | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pinmux) >> [MAX32\_MODE\_SHIFT](#ac45646bd5514a406cbb87dc24a3a2f4c)) & [MAX32\_MODE\_MASK](#a071a95ac6147954a5b9086cc27f02ce0))

## [◆ ](#ae9b72f2da84eca73ba5d0958946d2d6e)MAX32\_PINMUX\_PIN

| #define MAX32\_PINMUX\_PIN | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pinmux) >> [MAX32\_PIN\_SHIFT](#aa3b3d363ef790d1def3402ceb47b2f97)) & [MAX32\_PIN\_MASK](#abf4c75ee139d0abcc10ab3c4fe116ae2))

## [◆ ](#a9e2b0cc6ad6fb0e043f805be98900cad)MAX32\_PINMUX\_PORT

| #define MAX32\_PINMUX\_PORT | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pinmux) >> [MAX32\_PORT\_SHIFT](#ad103d747f01d57dc2cbc547fde45c988)) & [MAX32\_PORT\_MASK](#a668dddf52782f061e623e8d0837ba513))

## [◆ ](#a668dddf52782f061e623e8d0837ba513)MAX32\_PORT\_MASK

| #define MAX32\_PORT\_MASK   0x0FU |
| --- |

## [◆ ](#ad103d747f01d57dc2cbc547fde45c988)MAX32\_PORT\_SHIFT

| #define MAX32\_PORT\_SHIFT   4U |
| --- |

## [◆ ](#a88dcd8d7eee992eecd0e430a667d3353)MAX32\_POWER\_SOURCE\_SHIFT

| #define MAX32\_POWER\_SOURCE\_SHIFT   0x04 |
| --- |

## [◆ ](#a4e18fd313d30f6f69376cd769ea2347c)MAX32\_VSEL\_VDDIO

| #define MAX32\_VSEL\_VDDIO   0 |
| --- |

## [◆ ](#a6c2d4fea363165d857f5a79608d52aa0)MAX32\_VSEL\_VDDIOH

| #define MAX32\_VSEL\_VDDIOH   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [max32-pinctrl.h](max32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
