---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/realtek-gpio_8h.html
original_path: doxygen/html/realtek-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

realtek-gpio.h File Reference

[Go to the source code of this file.](realtek-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RTS5912\_GPIO\_INDETEN](#ae59327ac268671ea2e20014f17701529)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Enable input detect. |
| #define | [RTS5912\_GPIO\_OUTDRV](#a9f3289747c68c46fa5d8f92ebe0e2283)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Set pin driving current. |
| #define | [RTS5912\_GPIO\_SLEWRATE](#aa5af355318f8b6a034b85ed418de6cdd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Set GPIO slew rate. |
| #define | [RTS5912\_GPIO\_SCHEN](#ae65d41879bcb126213ac007808086cee)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Enable Schmitt-trigger. |
| #define | [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)   12 |
| #define | [RTS5912\_GPIO\_VOLTAGE\_MASK](#a9ab90e903840aec5172596492f12e6b5)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(13, 12) |
| #define | [RTS5912\_GPIO\_VOLTAGE\_DEFAULT](#a91e7d587b96806b3f8403d3532d5a888)   (0U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
|  | Set pin at the default voltage level. |
| #define | [RTS5912\_GPIO\_VOLTAGE\_1V8](#a83d8d0f0a827e770de9fe360fe566573)   (1U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
|  | Set pin voltage level at 1.8 V. |
| #define | [RTS5912\_GPIO\_VOLTAGE\_3V3](#a24268d0667f7a2266e519c03e6a04395)   (2U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
|  | Set pin voltage level at 3.3 V. |
| #define | [RTS5912\_GPIO\_VOLTAGE\_5V0](#a0ca327e5b979185b539f187eabcbc0be)   (3U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
|  | Set pin voltage level at 5.0 V. |
| #define | [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)   14 |
|  | Multi function. |
| #define | [RTS5912\_GPIO\_MFCTRL\_MASK](#a661de5a3eb9f6b97f44735718c29dc43)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 14) |
| #define | [RTS5912\_GPIO\_MFCTRL\_0](#a93faaacf50a46b2209231e7eae2da8b4)   (0U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
|  | 0x00:Function 0 0x01: Function 1 0x02: Function 2 0x03: Function 3 |
| #define | [RTS5912\_GPIO\_MFCTRL\_1](#adf7208d3ffb32ee5f1d65deff41aaa74)   (1U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| #define | [RTS5912\_GPIO\_MFCTRL\_2](#ae492ac80b7741521601d6885d2f1b530)   (2U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| #define | [RTS5912\_GPIO\_MFCTRL\_3](#abf987c5c5f861c3d2ff57c664264acd0)   (3U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| #define | [RTS5912\_GPIO\_INTR\_MASK](#a471603d5ffb1be381681a56d19b54757)   (1U << 21 | 1U << 22 | 1U << 24 | 1U << 25 | 1U << 26) |
|  | Interrupt Mask since rts5912 does not support GPIO\_INT\_LEVELS\_LOGICAL. |

## Macro Definition Documentation

## [◆ ](#ae59327ac268671ea2e20014f17701529)RTS5912\_GPIO\_INDETEN

| #define RTS5912\_GPIO\_INDETEN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

Enable input detect.

## [◆ ](#a471603d5ffb1be381681a56d19b54757)RTS5912\_GPIO\_INTR\_MASK

| #define RTS5912\_GPIO\_INTR\_MASK   (1U << 21 | 1U << 22 | 1U << 24 | 1U << 25 | 1U << 26) |
| --- |

Interrupt Mask since rts5912 does not support GPIO\_INT\_LEVELS\_LOGICAL.

## [◆ ](#a93faaacf50a46b2209231e7eae2da8b4)RTS5912\_GPIO\_MFCTRL\_0

| #define RTS5912\_GPIO\_MFCTRL\_0   (0U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| --- |

0x00:Function 0 0x01: Function 1 0x02: Function 2 0x03: Function 3

## [◆ ](#adf7208d3ffb32ee5f1d65deff41aaa74)RTS5912\_GPIO\_MFCTRL\_1

| #define RTS5912\_GPIO\_MFCTRL\_1   (1U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| --- |

## [◆ ](#ae492ac80b7741521601d6885d2f1b530)RTS5912\_GPIO\_MFCTRL\_2

| #define RTS5912\_GPIO\_MFCTRL\_2   (2U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| --- |

## [◆ ](#abf987c5c5f861c3d2ff57c664264acd0)RTS5912\_GPIO\_MFCTRL\_3

| #define RTS5912\_GPIO\_MFCTRL\_3   (3U << [RTS5912\_GPIO\_MFCTRL\_POS](#acea96124332b298d7f413105ed2c430f)) |
| --- |

## [◆ ](#a661de5a3eb9f6b97f44735718c29dc43)RTS5912\_GPIO\_MFCTRL\_MASK

| #define RTS5912\_GPIO\_MFCTRL\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 14) |
| --- |

## [◆ ](#acea96124332b298d7f413105ed2c430f)RTS5912\_GPIO\_MFCTRL\_POS

| #define RTS5912\_GPIO\_MFCTRL\_POS   14 |
| --- |

Multi function.

## [◆ ](#a9f3289747c68c46fa5d8f92ebe0e2283)RTS5912\_GPIO\_OUTDRV

| #define RTS5912\_GPIO\_OUTDRV   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

Set pin driving current.

## [◆ ](#ae65d41879bcb126213ac007808086cee)RTS5912\_GPIO\_SCHEN

| #define RTS5912\_GPIO\_SCHEN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

Enable Schmitt-trigger.

## [◆ ](#aa5af355318f8b6a034b85ed418de6cdd)RTS5912\_GPIO\_SLEWRATE

| #define RTS5912\_GPIO\_SLEWRATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

Set GPIO slew rate.

## [◆ ](#a83d8d0f0a827e770de9fe360fe566573)RTS5912\_GPIO\_VOLTAGE\_1V8

| #define RTS5912\_GPIO\_VOLTAGE\_1V8   (1U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
| --- |

Set pin voltage level at 1.8 V.

## [◆ ](#a24268d0667f7a2266e519c03e6a04395)RTS5912\_GPIO\_VOLTAGE\_3V3

| #define RTS5912\_GPIO\_VOLTAGE\_3V3   (2U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
| --- |

Set pin voltage level at 3.3 V.

## [◆ ](#a0ca327e5b979185b539f187eabcbc0be)RTS5912\_GPIO\_VOLTAGE\_5V0

| #define RTS5912\_GPIO\_VOLTAGE\_5V0   (3U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
| --- |

Set pin voltage level at 5.0 V.

## [◆ ](#a91e7d587b96806b3f8403d3532d5a888)RTS5912\_GPIO\_VOLTAGE\_DEFAULT

| #define RTS5912\_GPIO\_VOLTAGE\_DEFAULT   (0U << [RTS5912\_GPIO\_VOLTAGE\_POS](#a0381dff71143b0fadceaaade950340a3)) |
| --- |

Set pin at the default voltage level.

## [◆ ](#a9ab90e903840aec5172596492f12e6b5)RTS5912\_GPIO\_VOLTAGE\_MASK

| #define RTS5912\_GPIO\_VOLTAGE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(13, 12) |
| --- |

## [◆ ](#a0381dff71143b0fadceaaade950340a3)RTS5912\_GPIO\_VOLTAGE\_POS

| #define RTS5912\_GPIO\_VOLTAGE\_POS   12 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [realtek-gpio.h](realtek-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
