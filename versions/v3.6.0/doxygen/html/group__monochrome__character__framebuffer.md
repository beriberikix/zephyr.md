---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__monochrome__character__framebuffer.html
original_path: doxygen/html/group__monochrome__character__framebuffer.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Monochrome Character Framebuffer

[Utilities](group__utilities.md)

Public Monochrome Character Framebuffer API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [cfb\_font](structcfb__font.md) |
| struct | [cfb\_position](structcfb__position.md) |

| Macros | |
| --- | --- |
| #define | [FONT\_ENTRY\_DEFINE](#ga1fe25d7d6b057a40715ad44db7bc9249)(\_name, \_width, \_height, \_caps, \_data, \_fc, \_lc) |
|  | Macro for creating a font entry. |

| Enumerations | |
| --- | --- |
| enum | [cfb\_display\_param](#ga32e8edb517093dbc1b612a1bef24c7af) {     [CFB\_DISPLAY\_HEIGH](#gga32e8edb517093dbc1b612a1bef24c7afaab99f7b44bcfca4e49a71df82ad3b3e1) = 0 , [CFB\_DISPLAY\_WIDTH](#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a) , [CFB\_DISPLAY\_PPT](#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630) , [CFB\_DISPLAY\_ROWS](#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c) ,     [CFB\_DISPLAY\_COLS](#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f)   } |
| enum | [cfb\_font\_caps](#gae98337479a5339d4171797e96313fee5) { [CFB\_FONT\_MONO\_VPACKED](#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6) = BIT(0) , [CFB\_FONT\_MONO\_HPACKED](#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c) = BIT(1) , [CFB\_FONT\_MSB\_FIRST](#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b) = BIT(2) } |

| Functions | |
| --- | --- |
| int | [cfb\_print](#ga8c55d057b1efcbcd667ad4fbc1c856d5) (const struct [device](structdevice.md) \*dev, const char \*const str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y) |
|  | Print a string into the framebuffer. |
| int | [cfb\_draw\_text](#ga496b3b161fa0bc2e42e3d5de83c4f544) (const struct [device](structdevice.md) \*dev, const char \*const str, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y) |
|  | Print a string into the framebuffer. |
| int | [cfb\_draw\_point](#gae1943e8d138f5e612f6508dd0f510134) (const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*pos) |
|  | Draw a point. |
| int | [cfb\_draw\_line](#ga81af74d2831d5a4fc1338da693401958) (const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*start, const struct [cfb\_position](structcfb__position.md) \*end) |
|  | Draw a line. |
| int | [cfb\_draw\_rect](#ga0b26cd0d9e2de71f754f85849ccba001) (const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*start, const struct [cfb\_position](structcfb__position.md) \*end) |
|  | Draw a rectangle. |
| int | [cfb\_framebuffer\_clear](#gac9a957b5dd6e99377d9c070085df3252) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) clear\_display) |
|  | Clear framebuffer. |
| int | [cfb\_framebuffer\_invert](#ga8e86d48a0c6d951de34089f5d6cf5fb1) (const struct [device](structdevice.md) \*dev) |
|  | Invert Pixels. |
| int | [cfb\_invert\_area](#gadc802c8fc630fd9dfb445c0f1fa81ab4) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) width, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) height) |
|  | Invert Pixels in selected area. |
| int | [cfb\_framebuffer\_finalize](#ga9d0b3f63c2b52458ab040993b3c3b97d) (const struct [device](structdevice.md) \*dev) |
|  | Finalize framebuffer and write it to display RAM, invert or reorder pixels if necessary. |
| int | [cfb\_get\_display\_parameter](#gaeb46dfb72c31474c1acbc46d2f08803e) (const struct [device](structdevice.md) \*dev, enum [cfb\_display\_param](#ga32e8edb517093dbc1b612a1bef24c7af)) |
|  | Get display parameter. |
| int | [cfb\_framebuffer\_set\_font](#ga29343c61a7a9e28c50cb384ba4f383cf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx) |
|  | Set font. |
| int | [cfb\_set\_kerning](#gac0918644cb24a39ef578e54acac46d64) (const struct [device](structdevice.md) \*dev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) kerning) |
|  | Set font kerning (spacing between individual letters). |
| int | [cfb\_get\_font\_size](#ga63ea5f559391ed735da8afa78745e458) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*width, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*height) |
|  | Get font size. |
| int | [cfb\_get\_numof\_fonts](#ga5ef3b84b6169eaef398cf47b3583c827) (const struct [device](structdevice.md) \*dev) |
|  | Get number of fonts. |
| int | [cfb\_framebuffer\_init](#ga2bbe913d7f0a10b4ba543d83ef6fac95) (const struct [device](structdevice.md) \*dev) |
|  | Initialize Character Framebuffer. |

## Detailed Description

Public Monochrome Character Framebuffer API.

## Macro Definition Documentation

## [◆ ](#ga1fe25d7d6b057a40715ad44db7bc9249)FONT\_ENTRY\_DEFINE

| #define FONT\_ENTRY\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_width*, |
|  |  |  | *\_height*, |
|  |  |  | *\_caps*, |
|  |  |  | *\_data*, |
|  |  |  | *\_fc*, |
|  |  |  | *\_lc* ) |

`#include <[cfb.h](cfb_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([cfb\_font](structcfb__font.md), \_name) = { \

.data = \_data, \

.caps = \_caps, \

.width = \_width, \

.height = \_height, \

.first\_char = \_fc, \

.last\_char = \_lc, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[cfb\_font](structcfb__font.md)

**Definition** cfb.h:44

Macro for creating a font entry.

Parameters
:   | \_name | Name of the font entry. |
    | --- | --- |
    | \_width | Width of the font in pixels |
    | \_height | Height of the font in pixels. |
    | \_caps | Font capabilities. |
    | \_data | Raw data of the font. |
    | \_fc | Character mapped to first font element. |
    | \_lc | Character mapped to last font element. |

## Enumeration Type Documentation

## [◆ ](#ga32e8edb517093dbc1b612a1bef24c7af)cfb\_display\_param

| enum [cfb\_display\_param](#ga32e8edb517093dbc1b612a1bef24c7af) |
| --- |

`#include <[cfb.h](cfb_8h.md)>`

| Enumerator | |
| --- | --- |
| CFB\_DISPLAY\_HEIGH |  |
| CFB\_DISPLAY\_WIDTH |  |
| CFB\_DISPLAY\_PPT |  |
| CFB\_DISPLAY\_ROWS |  |
| CFB\_DISPLAY\_COLS |  |

## [◆ ](#gae98337479a5339d4171797e96313fee5)cfb\_font\_caps

| enum [cfb\_font\_caps](#gae98337479a5339d4171797e96313fee5) |
| --- |

`#include <[cfb.h](cfb_8h.md)>`

| Enumerator | |
| --- | --- |
| CFB\_FONT\_MONO\_VPACKED |  |
| CFB\_FONT\_MONO\_HPACKED |  |
| CFB\_FONT\_MSB\_FIRST |  |

## Function Documentation

## [◆ ](#ga81af74d2831d5a4fc1338da693401958)cfb\_draw\_line()

| int cfb\_draw\_line | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [cfb\_position](structcfb__position.md) \* | *start*, |
|  |  | const struct [cfb\_position](structcfb__position.md) \* | *end* ) |

`#include <[cfb.h](cfb_8h.md)>`

Draw a line.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | start | start position of the line |
    | end | end position of the line |

Returns
:   0 on success, negative value otherwise

## [◆ ](#gae1943e8d138f5e612f6508dd0f510134)cfb\_draw\_point()

| int cfb\_draw\_point | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [cfb\_position](structcfb__position.md) \* | *pos* ) |

`#include <[cfb.h](cfb_8h.md)>`

Draw a point.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | pos | position of the point |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga0b26cd0d9e2de71f754f85849ccba001)cfb\_draw\_rect()

| int cfb\_draw\_rect | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [cfb\_position](structcfb__position.md) \* | *start*, |
|  |  | const struct [cfb\_position](structcfb__position.md) \* | *end* ) |

`#include <[cfb.h](cfb_8h.md)>`

Draw a rectangle.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | start | Top-Left position of the rectangle |
    | end | Bottom-Right position of the rectangle |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga496b3b161fa0bc2e42e3d5de83c4f544)cfb\_draw\_text()

| int cfb\_draw\_text | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const char \*const | *str*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y* ) |

`#include <[cfb.h](cfb_8h.md)>`

Print a string into the framebuffer.

For compare to cfb\_print, cfb\_draw\_text accept non tile-aligned coords and not line wrapping.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | str | String to print |
    | x | Position in X direction of the beginning of the string |
    | y | Position in Y direction of the beginning of the string |

Returns
:   0 on success, negative value otherwise

## [◆ ](#gac9a957b5dd6e99377d9c070085df3252)cfb\_framebuffer\_clear()

| int cfb\_framebuffer\_clear | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *clear\_display* ) |

`#include <[cfb.h](cfb_8h.md)>`

Clear framebuffer.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | clear\_display | Clear the display as well |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga9d0b3f63c2b52458ab040993b3c3b97d)cfb\_framebuffer\_finalize()

| int cfb\_framebuffer\_finalize | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfb.h](cfb_8h.md)>`

Finalize framebuffer and write it to display RAM, invert or reorder pixels if necessary.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga2bbe913d7f0a10b4ba543d83ef6fac95)cfb\_framebuffer\_init()

| int cfb\_framebuffer\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfb.h](cfb_8h.md)>`

Initialize Character Framebuffer.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga8e86d48a0c6d951de34089f5d6cf5fb1)cfb\_framebuffer\_invert()

| int cfb\_framebuffer\_invert | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfb.h](cfb_8h.md)>`

Invert Pixels.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga29343c61a7a9e28c50cb384ba4f383cf)cfb\_framebuffer\_set\_font()

| int cfb\_framebuffer\_set\_font | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *idx* ) |

`#include <[cfb.h](cfb_8h.md)>`

Set font.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | idx | Font index |

Returns
:   0 on success, negative value otherwise

## [◆ ](#gaeb46dfb72c31474c1acbc46d2f08803e)cfb\_get\_display\_parameter()

| int cfb\_get\_display\_parameter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum | *cfb\_display\_param* ) |

`#include <[cfb.h](cfb_8h.md)>`

Get display parameter.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | [cfb\_display\_param](#ga32e8edb517093dbc1b612a1bef24c7af) | One of the display parameters |

Returns
:   Display parameter value

## [◆ ](#ga63ea5f559391ed735da8afa78745e458)cfb\_get\_font\_size()

| int cfb\_get\_font\_size | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *width*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *height* ) |

`#include <[cfb.h](cfb_8h.md)>`

Get font size.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | idx | Font index |
    | width | Pointers to the variable where the font width will be stored. |
    | height | Pointers to the variable where the font height will be stored. |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga5ef3b84b6169eaef398cf47b3583c827)cfb\_get\_numof\_fonts()

| int cfb\_get\_numof\_fonts | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfb.h](cfb_8h.md)>`

Get number of fonts.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |

Returns
:   number of fonts

## [◆ ](#gadc802c8fc630fd9dfb445c0f1fa81ab4)cfb\_invert\_area()

| int cfb\_invert\_area | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *y*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *width*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *height* ) |

`#include <[cfb.h](cfb_8h.md)>`

Invert Pixels in selected area.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | x | Position in X direction of the beginning of area |
    | y | Position in Y direction of the beginning of area |
    | width | Width of area in pixels |
    | height | Height of area in pixels |

Returns
:   0 on success, negative value otherwise

## [◆ ](#ga8c55d057b1efcbcd667ad4fbc1c856d5)cfb\_print()

| int cfb\_print | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const char \*const | *str*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *y* ) |

`#include <[cfb.h](cfb_8h.md)>`

Print a string into the framebuffer.

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | str | String to print |
    | x | Position in X direction of the beginning of the string |
    | y | Position in Y direction of the beginning of the string |

Returns
:   0 on success, negative value otherwise

## [◆ ](#gac0918644cb24a39ef578e54acac46d64)cfb\_set\_kerning()

| int cfb\_set\_kerning | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *kerning* ) |

`#include <[cfb.h](cfb_8h.md)>`

Set font kerning (spacing between individual letters).

Parameters
:   | dev | Pointer to device structure for driver instance |
    | --- | --- |
    | kerning | Font kerning |

Returns
:   0 on success, negative value otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
