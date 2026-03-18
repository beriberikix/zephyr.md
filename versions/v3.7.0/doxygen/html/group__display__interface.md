---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__display__interface.html
original_path: doxygen/html/group__display__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Display Interface

[Device Driver APIs](group__io__interfaces.md)

Display Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [LCD Interface](group__lcd__interface.md) |
|  | LCD Interface. |

| Data Structures | |
| --- | --- |
| struct | [display\_capabilities](structdisplay__capabilities.md) |
|  | Structure holding display capabilities. [More...](structdisplay__capabilities.md#details) |
| struct | [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) |
|  | Structure to describe display data buffer layout. [More...](structdisplay__buffer__descriptor.md#details) |
| struct | [display\_driver\_api](structdisplay__driver__api.md) |
|  | Display driver API API which a display driver should expose. [More...](structdisplay__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [DISPLAY\_BITS\_PER\_PIXEL](#ga3b305be04da5921ca4087498627dc061)(fmt) |
|  | Bits required per pixel for display format. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [display\_blanking\_on\_api](#gacf66a054396ccd8e178591b8fc98ff4d)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to turn on display blanking See [display\_blanking\_on()](#gac6ad1f33067165e4c3bf7c0c345bb4e4) for argument description. |
| typedef int(\* | [display\_blanking\_off\_api](#gab23bbd9305792d6e37d2e4ff91a2b175)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to turn off display blanking See [display\_blanking\_off()](#ga4d9e288891a6bde679c3aa00b9913e1d) for argument description. |
| typedef int(\* | [display\_write\_api](#ga5cab904b24062fdea531f450a8e5c367)) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, const void \*buf) |
|  | Callback API for writing data to the display See [display\_write()](#ga3a5114b4537039fc4d3258678b82cd18) for argument description. |
| typedef int(\* | [display\_read\_api](#ga9ed51d3f666f747d9fb7f1f7746611b3)) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, void \*buf) |
|  | Callback API for reading data from the display See [display\_read()](#ga3f497776520b0eac16b8aea80ccbbcfc) for argument description. |
| typedef void \*(\* | [display\_get\_framebuffer\_api](#ga6dd281032ad400d3adc7f5f812c5fe12)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get framebuffer pointer See [display\_get\_framebuffer()](#ga4b66d380e46909caaa7317857f84a9e8) for argument description. |
| typedef int(\* | [display\_set\_brightness\_api](#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
|  | Callback API to set display brightness See [display\_set\_brightness()](#gad5cdeb245d17c8d680a5843b3cce1f8c) for argument description. |
| typedef int(\* | [display\_set\_contrast\_api](#gadf115352908f94b0a0bf225dbdd8ee85)) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast) |
|  | Callback API to set display contrast See [display\_set\_contrast()](#ga855c72f72238b25f23e95e50546e2f27) for argument description. |
| typedef void(\* | [display\_get\_capabilities\_api](#ga474f85a33aef019dddb1c720ea23f3fb)) (const struct [device](structdevice.md) \*dev, struct [display\_capabilities](structdisplay__capabilities.md) \*capabilities) |
|  | Callback API to get display capabilities See [display\_get\_capabilities()](#ga6a13e42773be13b141ebd8f047f8db50) for argument description. |
| typedef int(\* | [display\_set\_pixel\_format\_api](#ga2637286cf3a97c2b532bb33f22263303)) (const struct [device](structdevice.md) \*dev, const enum [display\_pixel\_format](#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format) |
|  | Callback API to set pixel format used by the display See [display\_set\_pixel\_format()](#ga7ede828663090760c2558a231d9f2150) for argument description. |
| typedef int(\* | [display\_set\_orientation\_api](#gaff3b76a6601cf176782be940139ccb48)) (const struct [device](structdevice.md) \*dev, const enum [display\_orientation](#gac59b091a3ed39431ab97a5f19fdc4855) orientation) |
|  | Callback API to set orientation used by the display See [display\_set\_orientation()](#ga4e0a4dc2e434144874af014b8e7c4394) for argument description. |

| Enumerations | |
| --- | --- |
| enum | [display\_pixel\_format](#gac346bc56771052a8fe919c3ec23d7c9c) {     [PIXEL\_FORMAT\_RGB\_888](#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a) = BIT(0) , [PIXEL\_FORMAT\_MONO01](#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c) = BIT(1) , [PIXEL\_FORMAT\_MONO10](#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c) = BIT(2) , [PIXEL\_FORMAT\_ARGB\_8888](#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9) = BIT(3) ,     [PIXEL\_FORMAT\_RGB\_565](#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16) = BIT(4) , [PIXEL\_FORMAT\_BGR\_565](#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289) = BIT(5)   } |
|  | Display pixel formats. [More...](#gac346bc56771052a8fe919c3ec23d7c9c) |
| enum | [display\_screen\_info](#ga23030b6c27446c4579103fe38e821341) {     [SCREEN\_INFO\_MONO\_VTILED](#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804) = BIT(0) , [SCREEN\_INFO\_MONO\_MSB\_FIRST](#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d) = BIT(1) , [SCREEN\_INFO\_EPD](#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85) = BIT(2) , [SCREEN\_INFO\_DOUBLE\_BUFFER](#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842) = BIT(3) ,     [SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH](#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) = BIT(4)   } |
|  | Display screen information. [More...](#ga23030b6c27446c4579103fe38e821341) |
| enum | [display\_orientation](#gac59b091a3ed39431ab97a5f19fdc4855) { [DISPLAY\_ORIENTATION\_NORMAL](#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2) , [DISPLAY\_ORIENTATION\_ROTATED\_90](#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc) , [DISPLAY\_ORIENTATION\_ROTATED\_180](#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29) , [DISPLAY\_ORIENTATION\_ROTATED\_270](#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4) } |
|  | Enumeration with possible display orientation. [More...](#gac59b091a3ed39431ab97a5f19fdc4855) |

| Functions | |
| --- | --- |
| static int | [display\_write](#ga3a5114b4537039fc4d3258678b82cd18) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, const void \*buf) |
|  | Write data to display. |
| static int | [display\_read](#ga3f497776520b0eac16b8aea80ccbbcfc) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, void \*buf) |
|  | Read data from display. |
| static void \* | [display\_get\_framebuffer](#ga4b66d380e46909caaa7317857f84a9e8) (const struct [device](structdevice.md) \*dev) |
|  | Get pointer to framebuffer for direct access. |
| static int | [display\_blanking\_on](#gac6ad1f33067165e4c3bf7c0c345bb4e4) (const struct [device](structdevice.md) \*dev) |
|  | Turn display blanking on. |
| static int | [display\_blanking\_off](#ga4d9e288891a6bde679c3aa00b9913e1d) (const struct [device](structdevice.md) \*dev) |
|  | Turn display blanking off. |
| static int | [display\_set\_brightness](#gad5cdeb245d17c8d680a5843b3cce1f8c) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
|  | Set the brightness of the display. |
| static int | [display\_set\_contrast](#ga855c72f72238b25f23e95e50546e2f27) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast) |
|  | Set the contrast of the display. |
| static void | [display\_get\_capabilities](#ga6a13e42773be13b141ebd8f047f8db50) (const struct [device](structdevice.md) \*dev, struct [display\_capabilities](structdisplay__capabilities.md) \*capabilities) |
|  | Get display capabilities. |
| static int | [display\_set\_pixel\_format](#ga7ede828663090760c2558a231d9f2150) (const struct [device](structdevice.md) \*dev, const enum [display\_pixel\_format](#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format) |
|  | Set pixel format used by the display. |
| static int | [display\_set\_orientation](#ga4e0a4dc2e434144874af014b8e7c4394) (const struct [device](structdevice.md) \*dev, const enum [display\_orientation](#gac59b091a3ed39431ab97a5f19fdc4855) orientation) |
|  | Set display orientation. |

## Detailed Description

Display Interface.

Since
:   1.14

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga3b305be04da5921ca4087498627dc061)DISPLAY\_BITS\_PER\_PIXEL

| #define DISPLAY\_BITS\_PER\_PIXEL | ( |  | *fmt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

**Value:**

((((fmt & [PIXEL\_FORMAT\_RGB\_888](#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)) >> 0) \* 24U) + \

(((fmt & [PIXEL\_FORMAT\_MONO01](#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)) >> 1) \* 1U) + \

(((fmt & [PIXEL\_FORMAT\_MONO10](#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)) >> 2) \* 1U) + \

(((fmt & [PIXEL\_FORMAT\_ARGB\_8888](#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)) >> 3) \* 32U) + \

(((fmt & [PIXEL\_FORMAT\_RGB\_565](#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)) >> 4) \* 16U) + \

(((fmt & [PIXEL\_FORMAT\_BGR\_565](#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289)) >> 5) \* 16U))

[PIXEL\_FORMAT\_MONO10](#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)

@ PIXEL\_FORMAT\_MONO10

Monochrome (1=Black 0=White).

**Definition** display.h:45

[PIXEL\_FORMAT\_ARGB\_8888](#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)

@ PIXEL\_FORMAT\_ARGB\_8888

32-bit ARGB

**Definition** display.h:46

[PIXEL\_FORMAT\_MONO01](#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)

@ PIXEL\_FORMAT\_MONO01

Monochrome (0=Black 1=White).

**Definition** display.h:44

[PIXEL\_FORMAT\_RGB\_565](#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)

@ PIXEL\_FORMAT\_RGB\_565

16-bit RGB

**Definition** display.h:47

[PIXEL\_FORMAT\_RGB\_888](#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)

@ PIXEL\_FORMAT\_RGB\_888

24-bit RGB

**Definition** display.h:43

[PIXEL\_FORMAT\_BGR\_565](#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289)

@ PIXEL\_FORMAT\_BGR\_565

16-bit BGR

**Definition** display.h:48

Bits required per pixel for display format.

This macro expands to the number of bits required for a given display format. It can be used to allocate a framebuffer based on a given display format type

## Typedef Documentation

## [◆ ](#gab23bbd9305792d6e37d2e4ff91a2b175)display\_blanking\_off\_api

| typedef int(\* display\_blanking\_off\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to turn off display blanking See [display\_blanking\_off()](#ga4d9e288891a6bde679c3aa00b9913e1d) for argument description.

## [◆ ](#gacf66a054396ccd8e178591b8fc98ff4d)display\_blanking\_on\_api

| typedef int(\* display\_blanking\_on\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to turn on display blanking See [display\_blanking\_on()](#gac6ad1f33067165e4c3bf7c0c345bb4e4) for argument description.

## [◆ ](#ga474f85a33aef019dddb1c720ea23f3fb)display\_get\_capabilities\_api

| typedef void(\* display\_get\_capabilities\_api) (const struct [device](structdevice.md) \*dev, struct [display\_capabilities](structdisplay__capabilities.md) \*capabilities) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to get display capabilities See [display\_get\_capabilities()](#ga6a13e42773be13b141ebd8f047f8db50) for argument description.

## [◆ ](#ga6dd281032ad400d3adc7f5f812c5fe12)display\_get\_framebuffer\_api

| typedef void \*(\* display\_get\_framebuffer\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to get framebuffer pointer See [display\_get\_framebuffer()](#ga4b66d380e46909caaa7317857f84a9e8) for argument description.

## [◆ ](#ga9ed51d3f666f747d9fb7f1f7746611b3)display\_read\_api

| typedef int(\* display\_read\_api) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, void \*buf) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API for reading data from the display See [display\_read()](#ga3f497776520b0eac16b8aea80ccbbcfc) for argument description.

## [◆ ](#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)display\_set\_brightness\_api

| typedef int(\* display\_set\_brightness\_api) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to set display brightness See [display\_set\_brightness()](#gad5cdeb245d17c8d680a5843b3cce1f8c) for argument description.

## [◆ ](#gadf115352908f94b0a0bf225dbdd8ee85)display\_set\_contrast\_api

| typedef int(\* display\_set\_contrast\_api) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to set display contrast See [display\_set\_contrast()](#ga855c72f72238b25f23e95e50546e2f27) for argument description.

## [◆ ](#gaff3b76a6601cf176782be940139ccb48)display\_set\_orientation\_api

| typedef int(\* display\_set\_orientation\_api) (const struct [device](structdevice.md) \*dev, const enum [display\_orientation](#gac59b091a3ed39431ab97a5f19fdc4855) orientation) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to set orientation used by the display See [display\_set\_orientation()](#ga4e0a4dc2e434144874af014b8e7c4394) for argument description.

## [◆ ](#ga2637286cf3a97c2b532bb33f22263303)display\_set\_pixel\_format\_api

| typedef int(\* display\_set\_pixel\_format\_api) (const struct [device](structdevice.md) \*dev, const enum [display\_pixel\_format](#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API to set pixel format used by the display See [display\_set\_pixel\_format()](#ga7ede828663090760c2558a231d9f2150) for argument description.

## [◆ ](#ga5cab904b24062fdea531f450a8e5c367)display\_write\_api

| typedef int(\* display\_write\_api) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, const void \*buf) |
| --- |

`#include <[display.h](display_8h.md)>`

Callback API for writing data to the display See [display\_write()](#ga3a5114b4537039fc4d3258678b82cd18) for argument description.

## Enumeration Type Documentation

## [◆ ](#gac59b091a3ed39431ab97a5f19fdc4855)display\_orientation

| enum [display\_orientation](#gac59b091a3ed39431ab97a5f19fdc4855) |
| --- |

`#include <[display.h](display_8h.md)>`

Enumeration with possible display orientation.

| Enumerator | |
| --- | --- |
| DISPLAY\_ORIENTATION\_NORMAL | No rotation. |
| DISPLAY\_ORIENTATION\_ROTATED\_90 | Rotated 90 degrees clockwise. |
| DISPLAY\_ORIENTATION\_ROTATED\_180 | Rotated 180 degrees clockwise. |
| DISPLAY\_ORIENTATION\_ROTATED\_270 | Rotated 270 degrees clockwise. |

## [◆ ](#gac346bc56771052a8fe919c3ec23d7c9c)display\_pixel\_format

| enum [display\_pixel\_format](#gac346bc56771052a8fe919c3ec23d7c9c) |
| --- |

`#include <[display.h](display_8h.md)>`

Display pixel formats.

Display pixel format enumeration.

In case a pixel format consists out of multiple bytes the byte order is big endian.

| Enumerator | |
| --- | --- |
| PIXEL\_FORMAT\_RGB\_888 | 24-bit RGB |
| PIXEL\_FORMAT\_MONO01 | Monochrome (0=Black 1=White). |
| PIXEL\_FORMAT\_MONO10 | Monochrome (1=Black 0=White). |
| PIXEL\_FORMAT\_ARGB\_8888 | 32-bit ARGB |
| PIXEL\_FORMAT\_RGB\_565 | 16-bit RGB |
| PIXEL\_FORMAT\_BGR\_565 | 16-bit BGR |

## [◆ ](#ga23030b6c27446c4579103fe38e821341)display\_screen\_info

| enum [display\_screen\_info](#ga23030b6c27446c4579103fe38e821341) |
| --- |

`#include <[display.h](display_8h.md)>`

Display screen information.

| Enumerator | |
| --- | --- |
| SCREEN\_INFO\_MONO\_VTILED | If selected, one octet represents 8 pixels ordered vertically, otherwise ordered horizontally. |
| SCREEN\_INFO\_MONO\_MSB\_FIRST | If selected, the MSB represents the first pixel, otherwise MSB represents the last pixel. |
| SCREEN\_INFO\_EPD | Electrophoretic Display. |
| SCREEN\_INFO\_DOUBLE\_BUFFER | Screen has two alternating ram buffers. |
| SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH | Screen has x alignment constrained to width. |

## Function Documentation

## [◆ ](#ga4d9e288891a6bde679c3aa00b9913e1d)display\_blanking\_off()

| | int display\_blanking\_off | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Turn display blanking off.

Restore the frame buffer content to the display. In case backlight control is supported by the driver the backlight configuration is restored.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#gac6ad1f33067165e4c3bf7c0c345bb4e4)display\_blanking\_on()

| | int display\_blanking\_on | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Turn display blanking on.

This function blanks the complete display. The content of the frame buffer will be retained while blanking is enabled and the frame buffer will be accessible for read and write operations.

In case backlight control is supported by the driver the backlight is turned off. The backlight configuration is retained and accessible for configuration.

In case the driver supports display blanking the initial state of the driver would be the same as if this function was called.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#ga6a13e42773be13b141ebd8f047f8db50)display\_get\_capabilities()

| | void display\_get\_capabilities | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [display\_capabilities](structdisplay__capabilities.md) \* | *capabilities* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Get display capabilities.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | capabilities | Pointer to capabilities structure to populate |

## [◆ ](#ga4b66d380e46909caaa7317857f84a9e8)display\_get\_framebuffer()

| | void \* display\_get\_framebuffer | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Get pointer to framebuffer for direct access.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |

Return values
:   | Pointer | to frame buffer or NULL if direct framebuffer access is not supported |
    | --- | --- |

## [◆ ](#ga3f497776520b0eac16b8aea80ccbbcfc)display\_read()

| | int display\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, | |  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *y*, | |  |  | const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \* | *desc*, | |  |  | void \* | *buf* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Read data from display.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | x | x Coordinate of the upper left corner where to read from |
    | y | y Coordinate of the upper left corner where to read from |
    | desc | Pointer to a structure describing the buffer layout |
    | buf | Pointer to buffer array |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#gad5cdeb245d17c8d680a5843b3cce1f8c)display\_set\_brightness()

| | int display\_set\_brightness | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *brightness* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Set the brightness of the display.

Set the brightness of the display in steps of 1/256, where 255 is full brightness and 0 is minimal.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | brightness | Brightness in steps of 1/256 |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#ga855c72f72238b25f23e95e50546e2f27)display\_set\_contrast()

| | int display\_set\_contrast | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *contrast* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Set the contrast of the display.

Set the contrast of the display in steps of 1/256, where 255 is maximum difference and 0 is minimal.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | contrast | Contrast in steps of 1/256 |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#ga4e0a4dc2e434144874af014b8e7c4394)display\_set\_orientation()

| | int display\_set\_orientation | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const enum [display\_orientation](#gac59b091a3ed39431ab97a5f19fdc4855) | *orientation* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Set display orientation.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | orientation | Orientation to be used by display |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#ga7ede828663090760c2558a231d9f2150)display\_set\_pixel\_format()

| | int display\_set\_pixel\_format | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const enum [display\_pixel\_format](#gac346bc56771052a8fe919c3ec23d7c9c) | *pixel\_format* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Set pixel format used by the display.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | pixel\_format | Pixel format to be used by display |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |
    | -ENOSYS | if not implemented. |

## [◆ ](#ga3a5114b4537039fc4d3258678b82cd18)display\_write()

| | int display\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, | |  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *y*, | |  |  | const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \* | *desc*, | |  |  | const void \* | *buf* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[display.h](display_8h.md)>`

Write data to display.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | x | x Coordinate of the upper left corner where to write the buffer |
    | y | y Coordinate of the upper left corner where to write the buffer |
    | desc | Pointer to a structure describing the buffer layout |
    | buf | Pointer to buffer array |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
