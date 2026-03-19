---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32__common__clocks_8h.html
original_path: doxygen/html/stm32__common__clocks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [STM32\_CLOCK\_DIV\_SHIFT](#a208c97071646d6a363fa8abcd44908f0)   12 |
| #define | [STM32\_CLOCK\_DIV](#a49981976097d7e684ac5e5e094ecdf9b)(div) |
|  | Clock divider. |
| #define | [STM32\_DT\_CLKSEL\_REG\_MASK](#a9ad0be6cd421f8b608f74a3676bf9d6d)   0xFFFFU |
|  | Helper macros to pack RCC clock source selection register info in the DT. |
| #define | [STM32\_DT\_CLKSEL\_REG\_SHIFT](#a007f65a597867a03a6dc9b1e73d27a2d)   0U |
| #define | [STM32\_DT\_CLKSEL\_SHIFT\_MASK](#a01c12bdd437dd33ff01e2ed45617dfff)   0x3FU |
| #define | [STM32\_DT\_CLKSEL\_SHIFT\_SHIFT](#a6db7bff4699d60cc318494bdebd85b42)   16U |
| #define | [STM32\_DT\_CLKSEL\_MASK\_MASK](#afaa23be867f51da7ddb8b72ef429e51a)   0x1FU |
| #define | [STM32\_DT\_CLKSEL\_MASK\_SHIFT](#a627de44bae59bdf8febc6518bcaeb595)   22U |
| #define | [STM32\_DT\_CLKSEL\_VAL\_MASK](#a7ba7ca05cdad21911bc39d69e5674e3b)   0x1FU |
| #define | [STM32\_DT\_CLKSEL\_VAL\_SHIFT](#a7353643376cec80b57a89886e19ad6d9)   27U |
| #define | [STM32\_DT\_CLOCK\_SELECT](#af00e387856ff4e47b7b7d47ab2f61c8d)(val, mask, shift, reg) |
|  | Pack STM32 source clock selection RCC register bit fields for the DT. |
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

## [◆ ](#a49981976097d7e684ac5e5e094ecdf9b)STM32\_CLOCK\_DIV

| #define STM32\_CLOCK\_DIV | ( |  | *div* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((div) - 1) << [STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0))

[STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0)

#define STM32\_CLOCK\_DIV\_SHIFT

**Definition** stm32\_clock.h:27

Clock divider.

## [◆ ](#a208c97071646d6a363fa8abcd44908f0)STM32\_CLOCK\_DIV\_SHIFT

| #define STM32\_CLOCK\_DIV\_SHIFT   12 |
| --- |

## [◆ ](#afaa23be867f51da7ddb8b72ef429e51a)STM32\_DT\_CLKSEL\_MASK\_MASK

| #define STM32\_DT\_CLKSEL\_MASK\_MASK   0x1FU |
| --- |

## [◆ ](#a627de44bae59bdf8febc6518bcaeb595)STM32\_DT\_CLKSEL\_MASK\_SHIFT

| #define STM32\_DT\_CLKSEL\_MASK\_SHIFT   22U |
| --- |

## [◆ ](#a9ad0be6cd421f8b608f74a3676bf9d6d)STM32\_DT\_CLKSEL\_REG\_MASK

| #define STM32\_DT\_CLKSEL\_REG\_MASK   0xFFFFU |
| --- |

Helper macros to pack RCC clock source selection register info in the DT.

## [◆ ](#a007f65a597867a03a6dc9b1e73d27a2d)STM32\_DT\_CLKSEL\_REG\_SHIFT

| #define STM32\_DT\_CLKSEL\_REG\_SHIFT   0U |
| --- |

## [◆ ](#a01c12bdd437dd33ff01e2ed45617dfff)STM32\_DT\_CLKSEL\_SHIFT\_MASK

| #define STM32\_DT\_CLKSEL\_SHIFT\_MASK   0x3FU |
| --- |

## [◆ ](#a6db7bff4699d60cc318494bdebd85b42)STM32\_DT\_CLKSEL\_SHIFT\_SHIFT

| #define STM32\_DT\_CLKSEL\_SHIFT\_SHIFT   16U |
| --- |

## [◆ ](#a7ba7ca05cdad21911bc39d69e5674e3b)STM32\_DT\_CLKSEL\_VAL\_MASK

| #define STM32\_DT\_CLKSEL\_VAL\_MASK   0x1FU |
| --- |

## [◆ ](#a7353643376cec80b57a89886e19ad6d9)STM32\_DT\_CLKSEL\_VAL\_SHIFT

| #define STM32\_DT\_CLKSEL\_VAL\_SHIFT   27U |
| --- |

## [◆ ](#af00e387856ff4e47b7b7d47ab2f61c8d)STM32\_DT\_CLOCK\_SELECT

| #define STM32\_DT\_CLOCK\_SELECT | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *shift*, |
|  |  |  | *reg* ) |

**Value:**

((((reg) & [STM32\_DT\_CLKSEL\_REG\_MASK](#a9ad0be6cd421f8b608f74a3676bf9d6d)) << [STM32\_DT\_CLKSEL\_REG\_SHIFT](#a007f65a597867a03a6dc9b1e73d27a2d)) | \

(((shift) & [STM32\_DT\_CLKSEL\_SHIFT\_MASK](#a01c12bdd437dd33ff01e2ed45617dfff)) << [STM32\_DT\_CLKSEL\_SHIFT\_SHIFT](#a6db7bff4699d60cc318494bdebd85b42)) | \

(((mask) & [STM32\_DT\_CLKSEL\_MASK\_MASK](#afaa23be867f51da7ddb8b72ef429e51a)) << [STM32\_DT\_CLKSEL\_MASK\_SHIFT](#a627de44bae59bdf8febc6518bcaeb595)) | \

(((val) & [STM32\_DT\_CLKSEL\_VAL\_MASK](#a7ba7ca05cdad21911bc39d69e5674e3b)) << [STM32\_DT\_CLKSEL\_VAL\_SHIFT](#a7353643376cec80b57a89886e19ad6d9)))

[STM32\_DT\_CLKSEL\_REG\_SHIFT](#a007f65a597867a03a6dc9b1e73d27a2d)

#define STM32\_DT\_CLKSEL\_REG\_SHIFT

**Definition** stm32\_common\_clocks.h:25

[STM32\_DT\_CLKSEL\_SHIFT\_MASK](#a01c12bdd437dd33ff01e2ed45617dfff)

#define STM32\_DT\_CLKSEL\_SHIFT\_MASK

**Definition** stm32\_common\_clocks.h:26

[STM32\_DT\_CLKSEL\_MASK\_SHIFT](#a627de44bae59bdf8febc6518bcaeb595)

#define STM32\_DT\_CLKSEL\_MASK\_SHIFT

**Definition** stm32\_common\_clocks.h:29

[STM32\_DT\_CLKSEL\_SHIFT\_SHIFT](#a6db7bff4699d60cc318494bdebd85b42)

#define STM32\_DT\_CLKSEL\_SHIFT\_SHIFT

**Definition** stm32\_common\_clocks.h:27

[STM32\_DT\_CLKSEL\_VAL\_SHIFT](#a7353643376cec80b57a89886e19ad6d9)

#define STM32\_DT\_CLKSEL\_VAL\_SHIFT

**Definition** stm32\_common\_clocks.h:31

[STM32\_DT\_CLKSEL\_VAL\_MASK](#a7ba7ca05cdad21911bc39d69e5674e3b)

#define STM32\_DT\_CLKSEL\_VAL\_MASK

**Definition** stm32\_common\_clocks.h:30

[STM32\_DT\_CLKSEL\_REG\_MASK](#a9ad0be6cd421f8b608f74a3676bf9d6d)

#define STM32\_DT\_CLKSEL\_REG\_MASK

Helper macros to pack RCC clock source selection register info in the DT.

**Definition** stm32\_common\_clocks.h:24

[STM32\_DT\_CLKSEL\_MASK\_MASK](#afaa23be867f51da7ddb8b72ef429e51a)

#define STM32\_DT\_CLKSEL\_MASK\_MASK

**Definition** stm32\_common\_clocks.h:28

Pack STM32 source clock selection RCC register bit fields for the DT.

Parameters
:   | val | Clock configuration field value |
    | --- | --- |
    | mask | Mask of register field in RCC register |
    | shift | Position of field within RCC register (= field LSB's index) |
    | reg | Offset to target clock configuration register in RCC |

Note
:   'reg' range: 0x0~0xFFFF [ 00 : 15 ]
:   'shift' range: 0~63 [ 16 : 21 ]
:   'mask' range: 0x00~0x1F [ 22 : 26 ]
:   'val' range: 0x00~0x1F [ 27 : 31 ]

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
