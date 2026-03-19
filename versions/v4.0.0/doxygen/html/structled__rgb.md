---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structled__rgb.html
original_path: doxygen/html/structled__rgb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led\_rgb Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [LED Strip Interface](group__led__strip__interface.md)

Color value for a single RGB LED.
[More...](#details)

`#include <[led_strip.h](led__strip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [r](#a2b3072dbddc32f7a93b87b9ed01e1a33) |
|  | Red channel. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [g](#ab24a1948906fcb4c5978a84ac46b779a) |
|  | Green channel. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [b](#abf071f86f224daa42b3b905071e550af) |
|  | Blue channel. |

## Detailed Description

Color value for a single RGB LED.

Individual strip drivers may ignore lower-order bits if their resolution in any channel is less than a full byte.

## Field Documentation

## [◆ ](#abf071f86f224daa42b3b905071e550af)b

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) led\_rgb::b |
| --- |

Blue channel.

## [◆ ](#ab24a1948906fcb4c5978a84ac46b779a)g

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) led\_rgb::g |
| --- |

Green channel.

## [◆ ](#a2b3072dbddc32f7a93b87b9ed01e1a33)r

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) led\_rgb::r |
| --- |

Red channel.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[led\_strip.h](led__strip_8h_source.md)

- [led\_rgb](structled__rgb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
