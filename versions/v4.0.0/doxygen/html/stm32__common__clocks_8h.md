---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32__common__clocks_8h.html
original_path: doxygen/html/stm32__common__clocks_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_common\_clocks.h File Reference

[Go to the source code of this file.](stm32__common__clocks_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_SYSCLK](#a79a13b49235b90035b5ed7f62c9bf9bf)   0x001 |
|  | System clock. |
| #define | [STM32\_SRC\_LSE](#a42412accdd52b7ef9460583db634a4b1)   0x002 |
|  | Fixed clocks. |
| #define | [STM32\_SRC\_LSI](#ac6233dbbaff45f6862b21debbf180640)   0x003 |
| #define | [NO\_SEL](#ae998967c5f8ed059e757a6906b46ed4e)   0xFF |
|  | Dummy: Add a specifier when no selection is possible. |
| #define | [STM32\_MCO\_CFGR\_REG\_MASK](#ae14130ea70f0df4747f357dc863ea456)   0xFFFFU |
|  | STM32 MCO configuration values. |
| #define | [STM32\_MCO\_CFGR\_REG\_SHIFT](#ab5cb026c26c0059a2920288ea0305170)   0U |
| #define | [STM32\_MCO\_CFGR\_SHIFT\_MASK](#ace1dd95ce384cbd71a7cf71e23b450b6)   0x3FU |
| #define | [STM32\_MCO\_CFGR\_SHIFT\_SHIFT](#a90ef8b401020d2d31233ab5e0aef3953)   16U |
| #define | [STM32\_MCO\_CFGR\_MASK\_MASK](#af4128292c207270d5abfe104ebf723da)   0x1FU |
| #define | [STM32\_MCO\_CFGR\_MASK\_SHIFT](#abe5f0de675895eb047ad7d8ba15b444b)   22U |
| #define | [STM32\_MCO\_CFGR\_VAL\_MASK](#aa0fd0438f4f39510b942f085443da629)   0x1FU |
| #define | [STM32\_MCO\_CFGR\_VAL\_SHIFT](#a1c2cadfeafe266885df8e3b6ca22aa1c)   27U |
| #define | [STM32\_MCO\_CFGR](#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, mask, shift, reg) |
|  | STM32 MCO configuration register bit field. |
| #define | [STM32\_CLOCK](#a0fec36253cbc233df3b564feb5d873a4)(bus, bit) |
|  | Pack RCC clock register offset and bit in two 32-bit values as expected for the Device Tree clocks property on STM32. |

## Macro Definition Documentation

## [◆ ](#ae998967c5f8ed059e757a6906b46ed4e)NO\_SEL

| #define NO\_SEL   0xFF |
| --- |

Dummy: Add a specifier when no selection is possible.

## [◆ ](#a0fec36253cbc233df3b564feb5d873a4)STM32\_CLOCK

| #define STM32\_CLOCK | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(STM32\_CLOCK\_BUS\_##bus) (1 << bit)

Pack RCC clock register offset and bit in two 32-bit values as expected for the Device Tree clocks property on STM32.

Parameters
:   | bus | STM32 bus name (expands to STM32\_CLOCK\_BUS\_{bus}) |
    | --- | --- |
    | bit | Clock bit |

## [◆ ](#ae14adf3f41ed69e7eb58397ab4d5dc44)STM32\_MCO\_CFGR

| #define STM32\_MCO\_CFGR | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *shift*, |
|  |  |  | *reg* ) |

**Value:**

((((reg) & [STM32\_MCO\_CFGR\_REG\_MASK](#ae14130ea70f0df4747f357dc863ea456)) << [STM32\_MCO\_CFGR\_REG\_SHIFT](#ab5cb026c26c0059a2920288ea0305170)) | \

(((shift) & [STM32\_MCO\_CFGR\_SHIFT\_MASK](#ace1dd95ce384cbd71a7cf71e23b450b6)) << [STM32\_MCO\_CFGR\_SHIFT\_SHIFT](#a90ef8b401020d2d31233ab5e0aef3953)) | \

(((mask) & [STM32\_MCO\_CFGR\_MASK\_MASK](#af4128292c207270d5abfe104ebf723da)) << [STM32\_MCO\_CFGR\_MASK\_SHIFT](#abe5f0de675895eb047ad7d8ba15b444b)) | \

(((val) & [STM32\_MCO\_CFGR\_VAL\_MASK](#aa0fd0438f4f39510b942f085443da629)) << [STM32\_MCO\_CFGR\_VAL\_SHIFT](#a1c2cadfeafe266885df8e3b6ca22aa1c)))

[STM32\_MCO\_CFGR\_VAL\_SHIFT](#a1c2cadfeafe266885df8e3b6ca22aa1c)

#define STM32\_MCO\_CFGR\_VAL\_SHIFT

**Definition** stm32\_common\_clocks.h:26

[STM32\_MCO\_CFGR\_SHIFT\_SHIFT](#a90ef8b401020d2d31233ab5e0aef3953)

#define STM32\_MCO\_CFGR\_SHIFT\_SHIFT

**Definition** stm32\_common\_clocks.h:22

[STM32\_MCO\_CFGR\_VAL\_MASK](#aa0fd0438f4f39510b942f085443da629)

#define STM32\_MCO\_CFGR\_VAL\_MASK

**Definition** stm32\_common\_clocks.h:25

[STM32\_MCO\_CFGR\_REG\_SHIFT](#ab5cb026c26c0059a2920288ea0305170)

#define STM32\_MCO\_CFGR\_REG\_SHIFT

**Definition** stm32\_common\_clocks.h:20

[STM32\_MCO\_CFGR\_MASK\_SHIFT](#abe5f0de675895eb047ad7d8ba15b444b)

#define STM32\_MCO\_CFGR\_MASK\_SHIFT

**Definition** stm32\_common\_clocks.h:24

[STM32\_MCO\_CFGR\_SHIFT\_MASK](#ace1dd95ce384cbd71a7cf71e23b450b6)

#define STM32\_MCO\_CFGR\_SHIFT\_MASK

**Definition** stm32\_common\_clocks.h:21

[STM32\_MCO\_CFGR\_REG\_MASK](#ae14130ea70f0df4747f357dc863ea456)

#define STM32\_MCO\_CFGR\_REG\_MASK

STM32 MCO configuration values.

**Definition** stm32\_common\_clocks.h:19

[STM32\_MCO\_CFGR\_MASK\_MASK](#af4128292c207270d5abfe104ebf723da)

#define STM32\_MCO\_CFGR\_MASK\_MASK

**Definition** stm32\_common\_clocks.h:23

STM32 MCO configuration register bit field.

Parameters
:   | reg | Offset to RCC register holding MCO configuration |
    | --- | --- |
    | shift | Position of field within RCC register (= field LSB's index) |
    | mask | Mask of register field in RCC register |
    | val | Clock configuration field value (0~0x1F) |

Note
:   'reg' range: 0x0~0xFFFF [ 00 : 15 ]
:   'shift' range: 0~63 [ 16 : 21 ]
:   'mask' range: 0x00~0x1F [ 22 : 26 ]
:   'val' range: 0x00~0x1F [ 27 : 31 ]

## [◆ ](#af4128292c207270d5abfe104ebf723da)STM32\_MCO\_CFGR\_MASK\_MASK

| #define STM32\_MCO\_CFGR\_MASK\_MASK   0x1FU |
| --- |

## [◆ ](#abe5f0de675895eb047ad7d8ba15b444b)STM32\_MCO\_CFGR\_MASK\_SHIFT

| #define STM32\_MCO\_CFGR\_MASK\_SHIFT   22U |
| --- |

## [◆ ](#ae14130ea70f0df4747f357dc863ea456)STM32\_MCO\_CFGR\_REG\_MASK

| #define STM32\_MCO\_CFGR\_REG\_MASK   0xFFFFU |
| --- |

STM32 MCO configuration values.

## [◆ ](#ab5cb026c26c0059a2920288ea0305170)STM32\_MCO\_CFGR\_REG\_SHIFT

| #define STM32\_MCO\_CFGR\_REG\_SHIFT   0U |
| --- |

## [◆ ](#ace1dd95ce384cbd71a7cf71e23b450b6)STM32\_MCO\_CFGR\_SHIFT\_MASK

| #define STM32\_MCO\_CFGR\_SHIFT\_MASK   0x3FU |
| --- |

## [◆ ](#a90ef8b401020d2d31233ab5e0aef3953)STM32\_MCO\_CFGR\_SHIFT\_SHIFT

| #define STM32\_MCO\_CFGR\_SHIFT\_SHIFT   16U |
| --- |

## [◆ ](#aa0fd0438f4f39510b942f085443da629)STM32\_MCO\_CFGR\_VAL\_MASK

| #define STM32\_MCO\_CFGR\_VAL\_MASK   0x1FU |
| --- |

## [◆ ](#a1c2cadfeafe266885df8e3b6ca22aa1c)STM32\_MCO\_CFGR\_VAL\_SHIFT

| #define STM32\_MCO\_CFGR\_VAL\_SHIFT   27U |
| --- |

## [◆ ](#a42412accdd52b7ef9460583db634a4b1)STM32\_SRC\_LSE

| #define STM32\_SRC\_LSE   0x002 |
| --- |

Fixed clocks.

## [◆ ](#ac6233dbbaff45f6862b21debbf180640)STM32\_SRC\_LSI

| #define STM32\_SRC\_LSI   0x003 |
| --- |

## [◆ ](#a79a13b49235b90035b5ed7f62c9bf9bf)STM32\_SRC\_SYSCLK

| #define STM32\_SRC\_SYSCLK   0x001 |
| --- |

System clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32\_common\_clocks.h](stm32__common__clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
