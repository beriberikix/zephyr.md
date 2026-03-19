---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/led__strip_8h.html
original_path: doxygen/html/led__strip_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led\_strip.h File Reference

Public API for controlling linear strips of LEDs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](led__strip_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [led\_rgb](structled__rgb.md) |
|  | Color value for a single RGB LED. [More...](structled__rgb.md#details) |
| struct | [led\_strip\_driver\_api](structled__strip__driver__api.md) |
|  | LED strip driver API. [More...](structled__strip__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [led\_api\_update\_rgb](group__led__strip__interface.md#gaa36be40a962173021a547192d0d39151)) (const struct [device](structdevice.md) \*dev, struct [led\_rgb](structled__rgb.md) \*pixels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_pixels) |
|  | Callback API for updating an RGB LED strip. |
| typedef int(\* | [led\_api\_update\_channels](group__led__strip__interface.md#gab11579a7b5b7febfd48fa12560254501)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Callback API for updating channels without an RGB interpretation. |
| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)(\* | [led\_api\_length](group__led__strip__interface.md#ga3487e5d4a339898f88a225bb3678776b)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API for getting length of an LED strip. |

| Functions | |
| --- | --- |
| static int | [led\_strip\_update\_rgb](group__led__strip__interface.md#ga6e63331a5be2430968ab8b60692f8d67) (const struct [device](structdevice.md) \*dev, struct [led\_rgb](structled__rgb.md) \*pixels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_pixels) |
|  | Mandatory function to update an LED strip with the given RGB array. |
| static int | [led\_strip\_update\_channels](group__led__strip__interface.md#ga846b1d37bc6f7ed2014bea9603788b34) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channels, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_channels) |
|  | Optional function to update an LED strip with the given channel array (each channel byte corresponding to an individually addressable color channel or LED. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [led\_strip\_length](group__led__strip__interface.md#ga7f94eab0b357a81cccb5f0ea1575714a) (const struct [device](structdevice.md) \*dev) |
|  | Mandatory function to get chain length (in pixels) of an LED strip device. |

## Detailed Description

Public API for controlling linear strips of LEDs.

This library abstracts the chipset drivers for individually addressable strips of LEDs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led\_strip.h](led__strip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
