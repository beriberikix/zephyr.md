---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ft8xx__dl.html
original_path: doxygen/html/group__ft8xx__dl.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FT8xx display list

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md) » [FT8xx driver APIs](group__ft8xx__interface.md)

FT8xx display list commands.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [FT8XX\_BITMAPS](#ga28f7596c367f67f73d701b792300aa09)   1U |
|  | Rectangular pixel arrays, in various color formats. |
| #define | [FT8XX\_POINTS](#ga1d6f49b3817f9927fa1cd3cd42820490)   2U |
|  | Anti-aliased points, point radius is 1-256 pixels. |
| #define | [FT8XX\_LINES](#ga62bcf30c7a9eae4c468e1c7de144ad01)   3U |
|  | Anti-aliased lines, with width from 0 to 4095 1/16th of pixel units. |
| #define | [FT8XX\_LINE\_STRIP](#gac1b1188c36a4078e7db50d3c5aee7d25)   4U |
|  | Anti-aliased lines, connected head-to-tail. |
| #define | [FT8XX\_EDGE\_STRIP\_R](#ga0b3ce2828323978e9648bfd07caa1065)   5U |
|  | Edge strips for right. |
| #define | [FT8XX\_EDGE\_STRIP\_L](#ga97229abf592bba4039f19a98451cdc5b)   6U |
|  | Edge strips for left. |
| #define | [FT8XX\_EDGE\_STRIP\_A](#gaf5ad60bbe137dbf64281ad8d0be051e0)   7U |
|  | Edge strips for above. |
| #define | [FT8XX\_EDGE\_STRIP\_B](#ga9aff3a3c58e12b990130271e845662a8)   8U |
|  | Edge strips for below. |
| #define | [FT8XX\_RECTS](#ga05077568fea624ed7e3f9e3f6e8d72b8)   9U |
|  | Round-cornered rectangles, curvature of the corners can be adjusted using FT8XX\_LINE\_WIDTH. |
| #define | [FT8XX\_BEGIN](#ga25324ac604e037baf26cdd37341bee44)(prim) |
|  | Begin drawing a graphics primitive. |
| #define | [FT8XX\_CLEAR](#gab0fb60eec6f4c3b68d47f61886e7b933)(c, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), t) |
|  | Clear buffers to preset values. |
| #define | [FT8XX\_CLEAR\_COLOR\_RGB](#ga180b0ed70243277462cf303bc788e094)(red, green, blue) |
|  | Specify clear values for red, green and blue channels. |
| #define | [FT8XX\_COLOR\_RGB](#ga3bc794705028fc7e8e1b742db180055d)(red, green, blue) |
|  | Set the current color red, green and blue. |
| #define | [FT8XX\_DISPLAY](#ga135472b1cdf30d4bd69372e36c9960ce)() |
|  | End the display list. |
| #define | [FT8XX\_END](#ga8a9d0eb6521459eb7ce50b397de194d9)() |
|  | End drawing a graphics primitive. |
| #define | [FT8XX\_LINE\_WIDTH](#ga1d22204625ef070a6b8d16af7ad97578)(width) |
|  | Specify the width of lines to be drawn with primitive [FT8XX\_LINES](#ga62bcf30c7a9eae4c468e1c7de144ad01). |
| #define | [FT8XX\_TAG](#gab0721051bb3f3cb9f555f696f36dfbbf)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Attach the tag value for the following graphics objects. |
| #define | [FT8XX\_VERTEX2F](#ga2648ab069991c02b2e8de62bf13913ab)(x, y) |
|  | Start the operation of graphics primitives at the specified coordinate. |
| #define | [FT8XX\_VERTEX2II](#ga560836cd8c85599f24e5623a3e286b12)(x, y, handle, cell) |
|  | Start the operation of graphics primitive at the specified coordinates. |

## Detailed Description

FT8xx display list commands.

## Macro Definition Documentation

## [◆ ](#ga25324ac604e037baf26cdd37341bee44)FT8XX\_BEGIN

| #define FT8XX\_BEGIN | ( |  | *prim* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x1f000000 | ((prim) & 0x0f))

Begin drawing a graphics primitive.

The valid primitives are defined as:

- [FT8XX\_BITMAPS](#ga28f7596c367f67f73d701b792300aa09)
- [FT8XX\_POINTS](#ga1d6f49b3817f9927fa1cd3cd42820490)
- [FT8XX\_LINES](#ga62bcf30c7a9eae4c468e1c7de144ad01)
- [FT8XX\_LINE\_STRIP](#gac1b1188c36a4078e7db50d3c5aee7d25)
- [FT8XX\_EDGE\_STRIP\_R](#ga0b3ce2828323978e9648bfd07caa1065)
- [FT8XX\_EDGE\_STRIP\_L](#ga97229abf592bba4039f19a98451cdc5b)
- [FT8XX\_EDGE\_STRIP\_A](#gaf5ad60bbe137dbf64281ad8d0be051e0)
- [FT8XX\_EDGE\_STRIP\_B](#ga9aff3a3c58e12b990130271e845662a8)
- [FT8XX\_RECTS](#ga05077568fea624ed7e3f9e3f6e8d72b8)

The primitive to be drawn is selected by the [FT8XX\_BEGIN](#ga25324ac604e037baf26cdd37341bee44) command. Once the primitive is selected, it will be valid till the new primitive is selected by the [FT8XX\_BEGIN](#ga25324ac604e037baf26cdd37341bee44) command.

Note
:   The primitive drawing operation will not be performed until [FT8XX\_VERTEX2II](#ga560836cd8c85599f24e5623a3e286b12) or [FT8XX\_VERTEX2F](#ga2648ab069991c02b2e8de62bf13913ab) is executed.

Parameters
:   | prim | Graphics primitive |
    | --- | --- |

## [◆ ](#ga28f7596c367f67f73d701b792300aa09)FT8XX\_BITMAPS

| #define FT8XX\_BITMAPS   1U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Rectangular pixel arrays, in various color formats.

## [◆ ](#gab0fb60eec6f4c3b68d47f61886e7b933)FT8XX\_CLEAR

| #define FT8XX\_CLEAR | ( |  | *c*, |
| --- | --- | --- | --- |
|  |  |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)*, |
|  |  |  | *t* ) |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x26000000 | \

((c) ? 0x04 : 0) | (([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) ? 0x02 : 0) | ((t) ? 0x01 : 0))

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

Clear buffers to preset values.

Setting `c` to true will clear the color buffer of the FT8xx to the preset value. Setting this bit to false will maintain the color buffer of the FT8xx with an unchanged value. The preset value is defined in command [FT8XX\_CLEAR\_COLOR\_RGB](#ga180b0ed70243277462cf303bc788e094) for RGB channel and FT8XX\_CLEAR\_COLOR\_A for alpha channel.

Setting `s` to true will clear the stencil buffer of the FT8xx to the preset value. Setting this bit to false will maintain the stencil buffer of the FT8xx with an unchanged value. The preset value is defined in command FT8XX\_CLEAR\_STENCIL.

Setting `t` to true will clear the tag buffer of the FT8xx to the preset value. Setting this bit to false will maintain the tag buffer of the FT8xx with an unchanged value. The preset value is defined in command FT8XX\_CLEAR\_TAG.

Parameters
:   | c | Clear color buffer |
    | --- | --- |
    | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Clear stencil buffer |
    | t | Clear tag buffer |

## [◆ ](#ga180b0ed70243277462cf303bc788e094)FT8XX\_CLEAR\_COLOR\_RGB

| #define FT8XX\_CLEAR\_COLOR\_RGB | ( |  | *red*, |
| --- | --- | --- | --- |
|  |  |  | *green*, |
|  |  |  | *blue* ) |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x02000000 | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(red) & 0xff) << 16) | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(green) & 0xff) << 8) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(blue) & 0xff))

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Specify clear values for red, green and blue channels.

Sets the color values used by a following [FT8XX\_CLEAR](#gab0fb60eec6f4c3b68d47f61886e7b933).

Parameters
:   | red | Red value used when the color buffer is cleared |
    | --- | --- |
    | green | Green value used when the color buffer is cleared |
    | blue | Blue value used when the color buffer is cleared |

## [◆ ](#ga3bc794705028fc7e8e1b742db180055d)FT8XX\_COLOR\_RGB

| #define FT8XX\_COLOR\_RGB | ( |  | *red*, |
| --- | --- | --- | --- |
|  |  |  | *green*, |
|  |  |  | *blue* ) |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x04000000 | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(red) & 0xff) << 16) | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(green) & 0xff) << 8) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(blue) & 0xff))

Set the current color red, green and blue.

Sets red, green and blue values of the FT8xx color buffer which will be applied to the following draw operation.

Parameters
:   | red | Red value for the current color |
    | --- | --- |
    | green | Green value for the current color |
    | blue | Blue value for the current color |

## [◆ ](#ga135472b1cdf30d4bd69372e36c9960ce)FT8XX\_DISPLAY

| #define FT8XX\_DISPLAY | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

0

End the display list.

FT8xx will ignore all the commands following this command.

## [◆ ](#gaf5ad60bbe137dbf64281ad8d0be051e0)FT8XX\_EDGE\_STRIP\_A

| #define FT8XX\_EDGE\_STRIP\_A   7U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Edge strips for above.

## [◆ ](#ga9aff3a3c58e12b990130271e845662a8)FT8XX\_EDGE\_STRIP\_B

| #define FT8XX\_EDGE\_STRIP\_B   8U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Edge strips for below.

## [◆ ](#ga97229abf592bba4039f19a98451cdc5b)FT8XX\_EDGE\_STRIP\_L

| #define FT8XX\_EDGE\_STRIP\_L   6U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Edge strips for left.

## [◆ ](#ga0b3ce2828323978e9648bfd07caa1065)FT8XX\_EDGE\_STRIP\_R

| #define FT8XX\_EDGE\_STRIP\_R   5U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Edge strips for right.

## [◆ ](#ga8a9d0eb6521459eb7ce50b397de194d9)FT8XX\_END

| #define FT8XX\_END | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

0x21000000

End drawing a graphics primitive.

It is recommended to have an [FT8XX\_END](#ga8a9d0eb6521459eb7ce50b397de194d9) for each [FT8XX\_BEGIN](#ga25324ac604e037baf26cdd37341bee44). Whereas advanced users can avoid the usage of [FT8XX\_END](#ga8a9d0eb6521459eb7ce50b397de194d9) in order to save extra graphics instructions in the display list RAM.

## [◆ ](#gac1b1188c36a4078e7db50d3c5aee7d25)FT8XX\_LINE\_STRIP

| #define FT8XX\_LINE\_STRIP   4U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Anti-aliased lines, connected head-to-tail.

## [◆ ](#ga1d22204625ef070a6b8d16af7ad97578)FT8XX\_LINE\_WIDTH

| #define FT8XX\_LINE\_WIDTH | ( |  | *width* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x0e000000 | (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(width) & 0xfff))

Specify the width of lines to be drawn with primitive [FT8XX\_LINES](#ga62bcf30c7a9eae4c468e1c7de144ad01).

Sets the width of drawn lines. The width is the distance from the center of the line to the outermost drawn pixel, in units of 1/16 pixel. The valid range is from 16 to 4095 in terms of 1/16th pixel units.

Note
:   The [FT8XX\_LINE\_WIDTH](#ga1d22204625ef070a6b8d16af7ad97578) command will affect the [FT8XX\_LINES](#ga62bcf30c7a9eae4c468e1c7de144ad01), [FT8XX\_LINE\_STRIP](#gac1b1188c36a4078e7db50d3c5aee7d25), [FT8XX\_RECTS](#ga05077568fea624ed7e3f9e3f6e8d72b8), [FT8XX\_EDGE\_STRIP\_A](#gaf5ad60bbe137dbf64281ad8d0be051e0) /B/R/L primitives.

Parameters
:   | width | Line width in 1/16 pixel |
    | --- | --- |

## [◆ ](#ga62bcf30c7a9eae4c468e1c7de144ad01)FT8XX\_LINES

| #define FT8XX\_LINES   3U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Anti-aliased lines, with width from 0 to 4095 1/16th of pixel units.

(width is from center of the line to boundary)

## [◆ ](#ga1d6f49b3817f9927fa1cd3cd42820490)FT8XX\_POINTS

| #define FT8XX\_POINTS   2U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Anti-aliased points, point radius is 1-256 pixels.

## [◆ ](#ga05077568fea624ed7e3f9e3f6e8d72b8)FT8XX\_RECTS

| #define FT8XX\_RECTS   9U |
| --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

Round-cornered rectangles, curvature of the corners can be adjusted using FT8XX\_LINE\_WIDTH.

## [◆ ](#gab0721051bb3f3cb9f555f696f36dfbbf)FT8XX\_TAG

| #define FT8XX\_TAG | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x03000000 | ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)))

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Attach the tag value for the following graphics objects.

The initial value of the tag buffer of the FT8xx is specified by command FT8XX\_CLEAR\_TAG and taken effect by command [FT8XX\_CLEAR](#gab0fb60eec6f4c3b68d47f61886e7b933). [FT8XX\_TAG](#gab0721051bb3f3cb9f555f696f36dfbbf) command can specify the value of the tag buffer of the FT8xx that applies to the graphics objects when they are drawn on the screen. This tag value will be assigned to all the following objects, unless the FT8XX\_TAG\_MASK command is used to disable it. Once the following graphics objects are drawn, they are attached with the tag value successfully. When the graphics objects attached with the tag value are touched, the register [FT800\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329 "FT800_REG_TOUCH_TAG") or [FT810\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23 "FT810_REG_TOUCH_TAG") will be updated with the tag value of the graphics object being touched. If there is no [FT8XX\_TAG](#gab0721051bb3f3cb9f555f696f36dfbbf) commands in one display list, all the graphics objects rendered by the display list will report tag value as 255 in [FT800\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329 "FT800_REG_TOUCH_TAG") or [FT810\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23 "FT810_REG_TOUCH_TAG") when they were touched.

Parameters
:   | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Tag value 1-255 |
    | --- | --- |

## [◆ ](#ga2648ab069991c02b2e8de62bf13913ab)FT8XX\_VERTEX2F

| #define FT8XX\_VERTEX2F | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *y* ) |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x40000000 | \

((([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(x) & 0x7fff) << 15) | \

(([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(y) & 0x7fff))

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

Start the operation of graphics primitives at the specified coordinate.

The range of coordinates is from -16384 to +16383 in terms of 1/16th pixel units. The negative x coordinate value means the coordinate in the left virtual screen from (0, 0), while the negative y coordinate value means the coordinate in the upper virtual screen from (0, 0). If drawing on the negative coordinate position, the drawing operation will not be visible.

Parameters
:   | x | Signed x-coordinate in 1/16 pixel precision |
    | --- | --- |
    | y | Signed y-coordinate in 1/16 pixel precision |

## [◆ ](#ga560836cd8c85599f24e5623a3e286b12)FT8XX\_VERTEX2II

| #define FT8XX\_VERTEX2II | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *y*, |
|  |  |  | *handle*, |
|  |  |  | *cell* ) |

`#include <[ft8xx_dl.h](ft8xx__dl_8h.md)>`

**Value:**

(0x80000000 | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(x) & 0x01ff) << 21) | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(y) & 0x01ff) << 12) | \

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(handle) & 0x1f) << 7) | \

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(cell) & 0x7f))

Start the operation of graphics primitive at the specified coordinates.

The valid range of `handle` is from 0 to 31. From 16 to 31 the bitmap handle is dedicated to the FT8xx built-in font.

Cell number is the index of bitmap with same bitmap layout and format. For example, for handle 31, the cell 65 means the character "A" in the largest built in font.

Parameters
:   | x | x-coordinate in pixels, from 0 to 511 |
    | --- | --- |
    | y | y-coordinate in pixels, from 0 to 511 |
    | handle | Bitmap handle |
    | cell | Cell number |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
