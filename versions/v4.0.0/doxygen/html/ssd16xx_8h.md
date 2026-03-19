---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ssd16xx_8h.html
original_path: doxygen/html/ssd16xx_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ssd16xx.h File Reference

`#include <[zephyr/drivers/display.h](display_8h_source.md)>`

[Go to the source code of this file.](ssd16xx_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [ssd16xx\_ram](#af3596acb60f20fbecef01e82672ea765) { [SSD16XX\_RAM\_BLACK](#af3596acb60f20fbecef01e82672ea765ae3ae0ce9601034f1030f7114dcfedab0) = 0 , [SSD16XX\_RAM\_RED](#af3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466) } |
|  | SSD16xx RAM type for direct RAM access. [More...](#af3596acb60f20fbecef01e82672ea765) |

| Functions | |
| --- | --- |
| int | [ssd16xx\_read\_ram](#a876bae07401b2ccc3889414706ae4d97) (const struct [device](structdevice.md) \*dev, enum [ssd16xx\_ram](#af3596acb60f20fbecef01e82672ea765) ram\_type, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, void \*buf) |
|  | Read data directly from the display controller's internal RAM. |

## Enumeration Type Documentation

## [◆ ](#af3596acb60f20fbecef01e82672ea765)ssd16xx\_ram

| enum [ssd16xx\_ram](#af3596acb60f20fbecef01e82672ea765) |
| --- |

SSD16xx RAM type for direct RAM access.

| Enumerator | |
| --- | --- |
| SSD16XX\_RAM\_BLACK | The black RAM buffer.  This is typically the buffer used to compose the contents that will be displayed after the next refresh. |
| SSD16XX\_RAM\_RED |  |

## Function Documentation

## [◆ ](#a876bae07401b2ccc3889414706ae4d97)ssd16xx\_read\_ram()

| int ssd16xx\_read\_ram | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [ssd16xx\_ram](#af3596acb60f20fbecef01e82672ea765) | *ram\_type*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *y*, |
|  |  | const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \* | *desc*, |
|  |  | void \* | *buf* ) |

Read data directly from the display controller's internal RAM.

Parameters
:   | dev | Pointer to device structure |
    | --- | --- |
    | ram\_type | Type of RAM to read from |
    | x | Coordinate relative to the upper left corner |
    | y | Coordinate relative to the upper left corner |
    | desc | Structure describing the buffer layout |
    | buf | Output buffer |

Return values
:   | 0 | on success, negative errno on failure. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [ssd16xx.h](ssd16xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
