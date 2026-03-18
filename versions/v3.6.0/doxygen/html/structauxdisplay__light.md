---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structauxdisplay__light.html
original_path: doxygen/html/structauxdisplay__light.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

auxdisplay\_light Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Text Display Interface](group__auxdisplay__interface.md)

Light levels for brightness and/or backlight.
[More...](#details)

`#include <[auxdisplay.h](auxdisplay_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [minimum](#a4cd0c416ce77a45949feb90ae9f254a1) |
|  | Minimum light level supported. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [maximum](#a8f40f5fd3f825f1ee8c34891804cc003) |
|  | Maximum light level supported. |

## Detailed Description

Light levels for brightness and/or backlight.

If not supported by a display/driver, both minimum and maximum will be AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED.

## Field Documentation

## [◆ ](#a8f40f5fd3f825f1ee8c34891804cc003)maximum

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_light::maximum |
| --- |

Maximum light level supported.

## [◆ ](#a4cd0c416ce77a45949feb90ae9f254a1)minimum

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_light::minimum |
| --- |

Minimum light level supported.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[auxdisplay.h](auxdisplay_8h_source.md)

- [auxdisplay\_light](structauxdisplay__light.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
