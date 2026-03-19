---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structauxdisplay__character.html
original_path: doxygen/html/structauxdisplay__character.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

auxdisplay\_character Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Text Display Interface](group__auxdisplay__interface.md)

Structure for a custom character.
[More...](#details)

`#include <[auxdisplay.h](auxdisplay_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#a9f0bb424b9918e0f0c07c12eb4235677) |
|  | Custom character index on the display. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a4b011716576201818278aa853bfe542e) |
|  | Custom character pixel data, a character must be valid for a display consisting of a uint8 array of size character width by character height, values should be 0x00 for pixel off or 0xff for pixel on, if a display supports shades then values between 0x00 and 0xff may be used (display driver dependent). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [character\_code](#a217dd562886158efec238649fb4ade04) |
|  | Will be updated with custom character index to use in the display write function to disaplay this custom character. |

## Detailed Description

Structure for a custom character.

## Field Documentation

## [◆ ](#a217dd562886158efec238649fb4ade04)character\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_character::character\_code |
| --- |

Will be updated with custom character index to use in the display write function to disaplay this custom character.

## [◆ ](#a4b011716576201818278aa853bfe542e)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* auxdisplay\_character::data |
| --- |

Custom character pixel data, a character must be valid for a display consisting of a uint8 array of size character width by character height, values should be 0x00 for pixel off or 0xff for pixel on, if a display supports shades then values between 0x00 and 0xff may be used (display driver dependent).

## [◆ ](#a9f0bb424b9918e0f0c07c12eb4235677)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_character::index |
| --- |

Custom character index on the display.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[auxdisplay.h](auxdisplay_8h_source.md)

- [auxdisplay\_character](structauxdisplay__character.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
