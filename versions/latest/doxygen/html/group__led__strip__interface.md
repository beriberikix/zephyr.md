---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__led__strip__interface.html
original_path: doxygen/html/group__led__strip__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LED Strip Interface

[Device Driver APIs](group__io__interfaces.md)

LED Strip Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [led\_rgb](structled__rgb.md) |
|  | Color value for a single RGB LED. [More...](structled__rgb.md#details) |
| struct | [led\_strip\_driver\_api](structled__strip__driver__api.md) |
|  | LED strip driver API. [More...](structled__strip__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [led\_api\_update\_rgb](#gaa36be40a962173021a547192d0d39151)) (const struct [device](structdevice.md) \*dev, struct [led\_rgb](structled__rgb.md) \*pixels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_pixels) |
|  | Callback API for updating an RGB LED strip. |
| typedef int(\* | [led\_api\_update\_channels](#gab11579a7b5b7febfd48fa12560254501)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Callback API for updating channels without an RGB interpretation. |

| Functions | |
| --- | --- |
| static int | [led\_strip\_update\_rgb](#ga6e63331a5be2430968ab8b60692f8d67) (const struct [device](structdevice.md) \*dev, struct [led\_rgb](structled__rgb.md) \*pixels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_pixels) |
|  | Update an LED strip made of RGB pixels. |
| static int | [led\_strip\_update\_channels](#ga846b1d37bc6f7ed2014bea9603788b34) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Update an LED strip on a per-channel basis. |

## Detailed Description

LED Strip Interface.

## Typedef Documentation

## [◆ ](#gab11579a7b5b7febfd48fa12560254501)led\_api\_update\_channels

| typedef int(\* led\_api\_update\_channels) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
| --- |

`#include <[led_strip.h](led__strip_8h.md)>`

Callback API for updating channels without an RGB interpretation.

See also
:   [led\_strip\_update\_channels()](#ga846b1d37bc6f7ed2014bea9603788b34) for argument descriptions.

## [◆ ](#gaa36be40a962173021a547192d0d39151)led\_api\_update\_rgb

| typedef int(\* led\_api\_update\_rgb) (const struct [device](structdevice.md) \*dev, struct [led\_rgb](structled__rgb.md) \*pixels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_pixels) |
| --- |

`#include <[led_strip.h](led__strip_8h.md)>`

Callback API for updating an RGB LED strip.

See also
:   [led\_strip\_update\_rgb()](#ga6e63331a5be2430968ab8b60692f8d67) for argument descriptions.

## Function Documentation

## [◆ ](#ga846b1d37bc6f7ed2014bea9603788b34)led\_strip\_update\_channels()

| | int led\_strip\_update\_channels | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *channels*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_channels* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[led_strip.h](led__strip_8h.md)>`

Update an LED strip on a per-channel basis.

Important: This routine may overwrite *channels*.

This routine immediately updates the strip display according to the given channels array. Each channel byte corresponds to an individually addressable color channel or LED. Channels are updated linearly in strip order.

Parameters
:   | dev | LED strip device |
    | --- | --- |
    | channels | Array of per-channel data |
    | num\_channels | Length of channels array |

Returns
:   0 on success, negative on error

Warning
:   May overwrite *channels*

## [◆ ](#ga6e63331a5be2430968ab8b60692f8d67)led\_strip\_update\_rgb()

| | int led\_strip\_update\_rgb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [led\_rgb](structled__rgb.md) \* | *pixels*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_pixels* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[led_strip.h](led__strip_8h.md)>`

Update an LED strip made of RGB pixels.

Important: This routine may overwrite *pixels*.

This routine immediately updates the strip display according to the given pixels array.

Parameters
:   | dev | LED strip device |
    | --- | --- |
    | pixels | Array of pixel data |
    | num\_pixels | Length of pixels array |

Returns
:   0 on success, negative on error

Warning
:   May overwrite *pixels*

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
