---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ra-pinctrl_8h.html
original_path: doxygen/html/ra-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra-pinctrl.h File Reference

[Go to the source code of this file.](ra-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RA\_PORT\_NUM\_POS](#a677d4ff97e792bb9b3369b5f2f17018e)   0 |
| #define | [RA\_PORT\_NUM\_MASK](#a0473c603687c04018b96071a0c99d600)   0xf |
| #define | [RA\_PIN\_NUM\_POS](#a1e51a7480d6f3d77eea8d7dd52b2623c)   4 |
| #define | [RA\_PIN\_NUM\_MASK](#a61830f3cee48ee8caa7af15ae5220565)   0xf |
| #define | [RA\_PSEL\_HIZ\_JTAG\_SWD](#afaed554a358de18c6cc6548f6b25bd76)   0x0 |
| #define | [RA\_PSEL\_AGT](#ab93cf559fecab2cd319dde64cb32fb05)   0x1 |
| #define | [RA\_PSEL\_GPT0](#a4c29ecef20fa0ad9e2c52e4bed5607c0)   0x2 |
| #define | [RA\_PSEL\_GPT1](#a2c7f41c5813ff56a3434eed762554dc7)   0x3 |
| #define | [RA\_PSEL\_SCI\_0](#a16cf995560956577ef10fd4396c17c53)   0x4 |
| #define | [RA\_PSEL\_SCI\_2](#afdf9e4b96799435f94e8db4973ca9f5b)   0x4 |
| #define | [RA\_PSEL\_SCI\_4](#acb904b70cfddea59211b81bd2101aed4)   0x4 |
| #define | [RA\_PSEL\_SCI\_6](#a69aee47b66ab1e6a8ebe4c9062145fb4)   0x4 |
| #define | [RA\_PSEL\_SCI\_8](#a1282209663de934b4b523045a1816b68)   0x4 |
| #define | [RA\_PSEL\_SCI\_1](#a858885382f50f3376ce2d1b0125dfc49)   0x5 |
| #define | [RA\_PSEL\_SCI\_3](#a6860ab1d96ecddbe976d8cc292629990)   0x5 |
| #define | [RA\_PSEL\_SCI\_5](#a4b74f4742e6336e571bb731ae0a71961)   0x5 |
| #define | [RA\_PSEL\_SCI\_7](#a55f438cc9fcb43e350152129fedc4fcc)   0x5 |
| #define | [RA\_PSEL\_SCI\_9](#ad72d8611591a97878b493c610019e682)   0x5 |
| #define | [RA\_PSEL\_SPI](#a2f891a502696032fc264a48961078a54)   0x6 |
| #define | [RA\_PSEL\_I2C](#a6905e3e86fa46127217081707d3454e9)   0x7 |
| #define | [RA\_PSEL\_CLKOUT\_RTC](#a869043eaf8f376149eb9e8b3a09df41e)   0x9 |
| #define | [RA\_PSEL\_CAC\_ADC](#a8aa63c1bf6b5fdca37dec1d66417bec9)   0xa |
| #define | [RA\_PSEL\_BUS](#a02d5cce81df69f0cdace1aed46613422)   0xb |
| #define | [RA\_PSEL\_CANFD](#a02cd530e8a72c739351a41967d9b811a)   0x10 |
| #define | [RA\_PSEL\_QSPI](#af34c827566a453f61f7a6aff92bba180)   0x11 |
| #define | [RA\_PSEL\_SSIE](#a047eb43ed2d5734bf59ff55284628737)   0x12 |
| #define | [RA\_PSEL\_USBFS](#a7b4d3662537c785aa5e8ac284c8068b3)   0x13 |
| #define | [RA\_PSEL\_USBHS](#ad95c25a2066430bc076c4bfc63647298)   0x14 |
| #define | [RA\_PSEL\_SDHI](#a985004a21e22a2e1cf63e18f86aa9cbe)   0x15 |
| #define | [RA\_PSEL\_ETH\_MII](#a59d92838618726010e2adcc18807780e)   0x16 |
| #define | [RA\_PSEL\_ETH\_RMII](#a0f6039ed42d661f8cfd736cbca79139b)   0x17 |
| #define | [RA\_PSEL\_GLCDC](#ac55a667e4ac45fe9d6b485493507432d)   0x19 |
| #define | [RA\_PSEL\_OSPI](#afd7fed80f75f05d2e003f554c30f50b8)   0x1c |
| #define | [RA\_PSEL\_POS](#adec701d28121ee10eee96c4c4781316f)   8 |
| #define | [RA\_PSEL\_MASK](#a9082fcf206510ad3b42d48817a3f6e18)   0x1f |
| #define | [RA\_MODE\_POS](#aba5d1993a94006b39534addf1d8e6e1b)   13 |
| #define | [RA\_MODE\_MASK](#a02a2c8ef99c23f120890e0a2d82b76af)   0x1 |
| #define | [RA\_PSEL](#a9125cbda50cb1752ced9dfaa948be2e2)(psel, port\_num, pin\_num) |

## Macro Definition Documentation

## [◆ ](#a02a2c8ef99c23f120890e0a2d82b76af)RA\_MODE\_MASK

| #define RA\_MODE\_MASK   0x1 |
| --- |

## [◆ ](#aba5d1993a94006b39534addf1d8e6e1b)RA\_MODE\_POS

| #define RA\_MODE\_POS   13 |
| --- |

## [◆ ](#a61830f3cee48ee8caa7af15ae5220565)RA\_PIN\_NUM\_MASK

| #define RA\_PIN\_NUM\_MASK   0xf |
| --- |

## [◆ ](#a1e51a7480d6f3d77eea8d7dd52b2623c)RA\_PIN\_NUM\_POS

| #define RA\_PIN\_NUM\_POS   4 |
| --- |

## [◆ ](#a0473c603687c04018b96071a0c99d600)RA\_PORT\_NUM\_MASK

| #define RA\_PORT\_NUM\_MASK   0xf |
| --- |

## [◆ ](#a677d4ff97e792bb9b3369b5f2f17018e)RA\_PORT\_NUM\_POS

| #define RA\_PORT\_NUM\_POS   0 |
| --- |

## [◆ ](#a9125cbda50cb1752ced9dfaa948be2e2)RA\_PSEL

| #define RA\_PSEL | ( |  | *psel*, |
| --- | --- | --- | --- |
|  |  |  | *port\_num*, |
|  |  |  | *pin\_num* ) |

**Value:**

(1 << [RA\_MODE\_POS](#aba5d1993a94006b39534addf1d8e6e1b) | psel << [RA\_PSEL\_POS](#adec701d28121ee10eee96c4c4781316f) | port\_num << [RA\_PORT\_NUM\_POS](#a677d4ff97e792bb9b3369b5f2f17018e) | \

pin\_num << [RA\_PIN\_NUM\_POS](#a1e51a7480d6f3d77eea8d7dd52b2623c))

[RA\_PIN\_NUM\_POS](#a1e51a7480d6f3d77eea8d7dd52b2623c)

#define RA\_PIN\_NUM\_POS

**Definition** ra-pinctrl.h:13

[RA\_PORT\_NUM\_POS](#a677d4ff97e792bb9b3369b5f2f17018e)

#define RA\_PORT\_NUM\_POS

**Definition** ra-pinctrl.h:10

[RA\_MODE\_POS](#aba5d1993a94006b39534addf1d8e6e1b)

#define RA\_MODE\_POS

**Definition** ra-pinctrl.h:49

[RA\_PSEL\_POS](#adec701d28121ee10eee96c4c4781316f)

#define RA\_PSEL\_POS

**Definition** ra-pinctrl.h:46

## [◆ ](#ab93cf559fecab2cd319dde64cb32fb05)RA\_PSEL\_AGT

| #define RA\_PSEL\_AGT   0x1 |
| --- |

## [◆ ](#a02d5cce81df69f0cdace1aed46613422)RA\_PSEL\_BUS

| #define RA\_PSEL\_BUS   0xb |
| --- |

## [◆ ](#a8aa63c1bf6b5fdca37dec1d66417bec9)RA\_PSEL\_CAC\_ADC

| #define RA\_PSEL\_CAC\_ADC   0xa |
| --- |

## [◆ ](#a02cd530e8a72c739351a41967d9b811a)RA\_PSEL\_CANFD

| #define RA\_PSEL\_CANFD   0x10 |
| --- |

## [◆ ](#a869043eaf8f376149eb9e8b3a09df41e)RA\_PSEL\_CLKOUT\_RTC

| #define RA\_PSEL\_CLKOUT\_RTC   0x9 |
| --- |

## [◆ ](#a59d92838618726010e2adcc18807780e)RA\_PSEL\_ETH\_MII

| #define RA\_PSEL\_ETH\_MII   0x16 |
| --- |

## [◆ ](#a0f6039ed42d661f8cfd736cbca79139b)RA\_PSEL\_ETH\_RMII

| #define RA\_PSEL\_ETH\_RMII   0x17 |
| --- |

## [◆ ](#ac55a667e4ac45fe9d6b485493507432d)RA\_PSEL\_GLCDC

| #define RA\_PSEL\_GLCDC   0x19 |
| --- |

## [◆ ](#a4c29ecef20fa0ad9e2c52e4bed5607c0)RA\_PSEL\_GPT0

| #define RA\_PSEL\_GPT0   0x2 |
| --- |

## [◆ ](#a2c7f41c5813ff56a3434eed762554dc7)RA\_PSEL\_GPT1

| #define RA\_PSEL\_GPT1   0x3 |
| --- |

## [◆ ](#afaed554a358de18c6cc6548f6b25bd76)RA\_PSEL\_HIZ\_JTAG\_SWD

| #define RA\_PSEL\_HIZ\_JTAG\_SWD   0x0 |
| --- |

## [◆ ](#a6905e3e86fa46127217081707d3454e9)RA\_PSEL\_I2C

| #define RA\_PSEL\_I2C   0x7 |
| --- |

## [◆ ](#a9082fcf206510ad3b42d48817a3f6e18)RA\_PSEL\_MASK

| #define RA\_PSEL\_MASK   0x1f |
| --- |

## [◆ ](#afd7fed80f75f05d2e003f554c30f50b8)RA\_PSEL\_OSPI

| #define RA\_PSEL\_OSPI   0x1c |
| --- |

## [◆ ](#adec701d28121ee10eee96c4c4781316f)RA\_PSEL\_POS

| #define RA\_PSEL\_POS   8 |
| --- |

## [◆ ](#af34c827566a453f61f7a6aff92bba180)RA\_PSEL\_QSPI

| #define RA\_PSEL\_QSPI   0x11 |
| --- |

## [◆ ](#a16cf995560956577ef10fd4396c17c53)RA\_PSEL\_SCI\_0

| #define RA\_PSEL\_SCI\_0   0x4 |
| --- |

## [◆ ](#a858885382f50f3376ce2d1b0125dfc49)RA\_PSEL\_SCI\_1

| #define RA\_PSEL\_SCI\_1   0x5 |
| --- |

## [◆ ](#afdf9e4b96799435f94e8db4973ca9f5b)RA\_PSEL\_SCI\_2

| #define RA\_PSEL\_SCI\_2   0x4 |
| --- |

## [◆ ](#a6860ab1d96ecddbe976d8cc292629990)RA\_PSEL\_SCI\_3

| #define RA\_PSEL\_SCI\_3   0x5 |
| --- |

## [◆ ](#acb904b70cfddea59211b81bd2101aed4)RA\_PSEL\_SCI\_4

| #define RA\_PSEL\_SCI\_4   0x4 |
| --- |

## [◆ ](#a4b74f4742e6336e571bb731ae0a71961)RA\_PSEL\_SCI\_5

| #define RA\_PSEL\_SCI\_5   0x5 |
| --- |

## [◆ ](#a69aee47b66ab1e6a8ebe4c9062145fb4)RA\_PSEL\_SCI\_6

| #define RA\_PSEL\_SCI\_6   0x4 |
| --- |

## [◆ ](#a55f438cc9fcb43e350152129fedc4fcc)RA\_PSEL\_SCI\_7

| #define RA\_PSEL\_SCI\_7   0x5 |
| --- |

## [◆ ](#a1282209663de934b4b523045a1816b68)RA\_PSEL\_SCI\_8

| #define RA\_PSEL\_SCI\_8   0x4 |
| --- |

## [◆ ](#ad72d8611591a97878b493c610019e682)RA\_PSEL\_SCI\_9

| #define RA\_PSEL\_SCI\_9   0x5 |
| --- |

## [◆ ](#a985004a21e22a2e1cf63e18f86aa9cbe)RA\_PSEL\_SDHI

| #define RA\_PSEL\_SDHI   0x15 |
| --- |

## [◆ ](#a2f891a502696032fc264a48961078a54)RA\_PSEL\_SPI

| #define RA\_PSEL\_SPI   0x6 |
| --- |

## [◆ ](#a047eb43ed2d5734bf59ff55284628737)RA\_PSEL\_SSIE

| #define RA\_PSEL\_SSIE   0x12 |
| --- |

## [◆ ](#a7b4d3662537c785aa5e8ac284c8068b3)RA\_PSEL\_USBFS

| #define RA\_PSEL\_USBFS   0x13 |
| --- |

## [◆ ](#ad95c25a2066430bc076c4bfc63647298)RA\_PSEL\_USBHS

| #define RA\_PSEL\_USBHS   0x14 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [ra-pinctrl.h](ra-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
