---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structinput__touchscreen__common__config.html
original_path: doxygen/html/structinput__touchscreen__common__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_touchscreen\_common\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Touchscreen Event Report API](group__touch__events.md)

Common touchscreen config.
[More...](#details)

`#include <[input_touch.h](input__touch_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [screen\_width](#a35b6d8ccd36aa95d46cc24be2f94144b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [screen\_height](#ae534425e6069853cb80a3925fce8e2ad) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [inverted\_x](#a147cc66f165b5bf9e42b591ad77824c5) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [inverted\_y](#abba0c9353f867287b047635ea358e057) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [swapped\_x\_y](#a408e21f2a9e57267d87d24f8a054f999) |

## Detailed Description

Common touchscreen config.

This structure **must** be placed first in the driver's config structure.

Parameters
:   | [screen\_width](#a35b6d8ccd36aa95d46cc24be2f94144b) | Horizontal resolution of touchscreen |
    | --- | --- |
    | [screen\_height](#ae534425e6069853cb80a3925fce8e2ad) | Vertical resolution of touchscreen |
    | [inverted\_x](#a147cc66f165b5bf9e42b591ad77824c5) | X axis is inverted |
    | [inverted\_y](#abba0c9353f867287b047635ea358e057) | Y axis is inverted |
    | [swapped\_x\_y](#a408e21f2a9e57267d87d24f8a054f999) | X and Y axes are swapped |

see touchscreem-common.yaml for more details

## Field Documentation

## [◆ ](#a147cc66f165b5bf9e42b591ad77824c5)inverted\_x

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) input\_touchscreen\_common\_config::inverted\_x |
| --- |

## [◆ ](#abba0c9353f867287b047635ea358e057)inverted\_y

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) input\_touchscreen\_common\_config::inverted\_y |
| --- |

## [◆ ](#ae534425e6069853cb80a3925fce8e2ad)screen\_height

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_touchscreen\_common\_config::screen\_height |
| --- |

## [◆ ](#a35b6d8ccd36aa95d46cc24be2f94144b)screen\_width

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input\_touchscreen\_common\_config::screen\_width |
| --- |

## [◆ ](#a408e21f2a9e57267d87d24f8a054f999)swapped\_x\_y

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) input\_touchscreen\_common\_config::swapped\_x\_y |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input\_touch.h](input__touch_8h_source.md)

- [input\_touchscreen\_common\_config](structinput__touchscreen__common__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
