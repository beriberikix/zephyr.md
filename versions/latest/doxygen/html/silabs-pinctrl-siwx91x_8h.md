---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/silabs-pinctrl-siwx91x_8h.html
original_path: doxygen/html/silabs-pinctrl-siwx91x_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

silabs-pinctrl-siwx91x.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](silabs-pinctrl-siwx91x_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LSB\_GET](#a92235ab2e350fbdc01ddf0f894e5e4c0)(value) |
| #define | [FIELD\_GET](#aa49a456f06f7bdbedfcf3517e461947e)(mask, value) |
| #define | [FIELD\_PREP](#aa03c8b31bf67a097dd9f8153a04ef86b)(mask, value) |
| #define | [SIWX91X\_PINCTRL\_PORT\_MASK](#a50d5c19898298b48138dbd1e35a1789d)   0x0000000FUL |
| #define | [SIWX91X\_PINCTRL\_PIN\_MASK](#a7ccfd879f82aa28433bb31b86861a6b3)   0x000000F0UL |
| #define | [SIWX91X\_PINCTRL\_ULPPIN\_MASK](#a6c1b75f5d3e9c46c74a5bd67161f23d6)   0x00000F00UL |
| #define | [SIWX91X\_PINCTRL\_MODE\_MASK](#a2f7374a4ef333a2972e406a826e2f697)   0x0003F000UL |
| #define | [SIWX91X\_PINCTRL\_ULPMODE\_MASK](#a6d3ea759c0a75addbe3495b9817fa90a)   0x00FC0000UL |
| #define | [SIWX91X\_PINCTRL\_PAD\_MASK](#a9a5fa9fa0c3d65eae582fedd3585cd0d)   0xFF000000UL |
| #define | [SIWX91X\_GPIO](#a34a2f79af3f9aa9c434bb25c0c711d97)(mode, ulpmode, pad, port, pin, ulppin) |

## Macro Definition Documentation

## [◆ ](#aa49a456f06f7bdbedfcf3517e461947e)FIELD\_GET

| #define FIELD\_GET | ( |  | *mask*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

**Value:**

(((value) & (mask)) / [LSB\_GET](#a92235ab2e350fbdc01ddf0f894e5e4c0)(mask))

[LSB\_GET](#a92235ab2e350fbdc01ddf0f894e5e4c0)

#define LSB\_GET(value)

**Definition** silabs-pinctrl-siwx91x.h:13

## [◆ ](#aa03c8b31bf67a097dd9f8153a04ef86b)FIELD\_PREP

| #define FIELD\_PREP | ( |  | *mask*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

**Value:**

(((value) \* [LSB\_GET](#a92235ab2e350fbdc01ddf0f894e5e4c0)(mask)) & (mask))

## [◆ ](#a92235ab2e350fbdc01ddf0f894e5e4c0)LSB\_GET

| #define LSB\_GET | ( |  | *value* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((value) & -(value))

## [◆ ](#a34a2f79af3f9aa9c434bb25c0c711d97)SIWX91X\_GPIO

| #define SIWX91X\_GPIO | ( |  | *mode*, |
| --- | --- | --- | --- |
|  |  |  | *ulpmode*, |
|  |  |  | *pad*, |
|  |  |  | *port*, |
|  |  |  | *pin*, |
|  |  |  | *ulppin* ) |

**Value:**

([FIELD\_PREP](#aa03c8b31bf67a097dd9f8153a04ef86b)([SIWX91X\_PINCTRL\_PORT\_MASK](#a50d5c19898298b48138dbd1e35a1789d), port) | [FIELD\_PREP](#aa03c8b31bf67a097dd9f8153a04ef86b)([SIWX91X\_PINCTRL\_PIN\_MASK](#a7ccfd879f82aa28433bb31b86861a6b3), pin) | \

FIELD\_PREP([SIWX91X\_PINCTRL\_ULPPIN\_MASK](#a6c1b75f5d3e9c46c74a5bd67161f23d6), ulppin) | \

FIELD\_PREP([SIWX91X\_PINCTRL\_MODE\_MASK](#a2f7374a4ef333a2972e406a826e2f697), mode) | \

FIELD\_PREP([SIWX91X\_PINCTRL\_ULPMODE\_MASK](#a6d3ea759c0a75addbe3495b9817fa90a), ulpmode) | \

FIELD\_PREP([SIWX91X\_PINCTRL\_PAD\_MASK](#a9a5fa9fa0c3d65eae582fedd3585cd0d), pad))

[SIWX91X\_PINCTRL\_MODE\_MASK](#a2f7374a4ef333a2972e406a826e2f697)

#define SIWX91X\_PINCTRL\_MODE\_MASK

**Definition** silabs-pinctrl-siwx91x.h:21

[SIWX91X\_PINCTRL\_PORT\_MASK](#a50d5c19898298b48138dbd1e35a1789d)

#define SIWX91X\_PINCTRL\_PORT\_MASK

**Definition** silabs-pinctrl-siwx91x.h:18

[SIWX91X\_PINCTRL\_ULPPIN\_MASK](#a6c1b75f5d3e9c46c74a5bd67161f23d6)

#define SIWX91X\_PINCTRL\_ULPPIN\_MASK

**Definition** silabs-pinctrl-siwx91x.h:20

[SIWX91X\_PINCTRL\_ULPMODE\_MASK](#a6d3ea759c0a75addbe3495b9817fa90a)

#define SIWX91X\_PINCTRL\_ULPMODE\_MASK

**Definition** silabs-pinctrl-siwx91x.h:22

[SIWX91X\_PINCTRL\_PIN\_MASK](#a7ccfd879f82aa28433bb31b86861a6b3)

#define SIWX91X\_PINCTRL\_PIN\_MASK

**Definition** silabs-pinctrl-siwx91x.h:19

[SIWX91X\_PINCTRL\_PAD\_MASK](#a9a5fa9fa0c3d65eae582fedd3585cd0d)

#define SIWX91X\_PINCTRL\_PAD\_MASK

**Definition** silabs-pinctrl-siwx91x.h:23

[FIELD\_PREP](#aa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:15

## [◆ ](#a2f7374a4ef333a2972e406a826e2f697)SIWX91X\_PINCTRL\_MODE\_MASK

| #define SIWX91X\_PINCTRL\_MODE\_MASK   0x0003F000UL |
| --- |

## [◆ ](#a9a5fa9fa0c3d65eae582fedd3585cd0d)SIWX91X\_PINCTRL\_PAD\_MASK

| #define SIWX91X\_PINCTRL\_PAD\_MASK   0xFF000000UL |
| --- |

## [◆ ](#a7ccfd879f82aa28433bb31b86861a6b3)SIWX91X\_PINCTRL\_PIN\_MASK

| #define SIWX91X\_PINCTRL\_PIN\_MASK   0x000000F0UL |
| --- |

## [◆ ](#a50d5c19898298b48138dbd1e35a1789d)SIWX91X\_PINCTRL\_PORT\_MASK

| #define SIWX91X\_PINCTRL\_PORT\_MASK   0x0000000FUL |
| --- |

## [◆ ](#a6d3ea759c0a75addbe3495b9817fa90a)SIWX91X\_PINCTRL\_ULPMODE\_MASK

| #define SIWX91X\_PINCTRL\_ULPMODE\_MASK   0x00FC0000UL |
| --- |

## [◆ ](#a6c1b75f5d3e9c46c74a5bd67161f23d6)SIWX91X\_PINCTRL\_ULPPIN\_MASK

| #define SIWX91X\_PINCTRL\_ULPPIN\_MASK   0x00000F00UL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs-pinctrl-siwx91x.h](silabs-pinctrl-siwx91x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
