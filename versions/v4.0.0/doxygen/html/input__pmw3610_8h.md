---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__pmw3610_8h.html
original_path: doxygen/html/input__pmw3610_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_pmw3610.h File Reference

[Go to the source code of this file.](input__pmw3610_8h_source.md)

| Functions | |
| --- | --- |
| int | [pmw3610\_set\_resolution](#a7c20acd4c9ed5b1e16ebc2e093119e0b) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_cpi) |
|  | Set resolution on a pmw3610 device. |
| int | [pmw3610\_force\_awake](#aa70dd183377503db716ec6277dade83a) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set force awake mode on a pmw3610 device. |

## Function Documentation

## [◆ ](#aa70dd183377503db716ec6277dade83a)pmw3610\_force\_awake()

| int pmw3610\_force\_awake | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Set force awake mode on a pmw3610 device.

Parameters
:   | dev | pmw3610 device. |
    | --- | --- |
    | enable | whether to enable or disable force awake mode. |

## [◆ ](#a7c20acd4c9ed5b1e16ebc2e093119e0b)pmw3610\_set\_resolution()

| int pmw3610\_set\_resolution | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *res\_cpi* ) |

Set resolution on a pmw3610 device.

Parameters
:   | dev | pmw3610 device. |
    | --- | --- |
    | res\_cpi | CPI resolution, 200 to 3200. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_pmw3610.h](input__pmw3610_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
