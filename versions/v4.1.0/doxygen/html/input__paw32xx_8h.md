---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/input__paw32xx_8h.html
original_path: doxygen/html/input__paw32xx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_paw32xx.h File Reference

[Go to the source code of this file.](input__paw32xx_8h_source.md)

| Functions | |
| --- | --- |
| int | [paw32xx\_set\_resolution](#a7c15c20653486833cb07a43cd92c97cf) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_cpi) |
|  | Set resolution on a paw32xx device. |
| int | [paw32xx\_force\_awake](#a03c6aa7e9e7b370791c16292055b9fff) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set force awake mode on a paw32xx device. |

## Function Documentation

## [◆ ](#a03c6aa7e9e7b370791c16292055b9fff)paw32xx\_force\_awake()

| int paw32xx\_force\_awake | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Set force awake mode on a paw32xx device.

Parameters
:   | dev | paw32xx device. |
    | --- | --- |
    | enable | whether to enable or disable force awake mode. |

## [◆ ](#a7c15c20653486833cb07a43cd92c97cf)paw32xx\_set\_resolution()

| int paw32xx\_set\_resolution | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *res\_cpi* ) |

Set resolution on a paw32xx device.

Parameters
:   | dev | paw32xx device. |
    | --- | --- |
    | res\_cpi | CPI resolution, 200 to 3200. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_paw32xx.h](input__paw32xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
