---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mdf__interface__max22017.html
original_path: doxygen/html/group__mdf__interface__max22017.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD MAX22017 interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Functions | |
| --- | --- |
| int | [max22017\_reg\_read](#ga7c051fa0697ae672a4dddbfa84059ad0) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Read register from max22017. |
| int | [max22017\_reg\_write](#gac4a4a29f7ae31af97f19d700264a604d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Write register to max22017. |

## Detailed Description

## Function Documentation

## [◆ ](#ga7c051fa0697ae672a4dddbfa84059ad0)max22017\_reg\_read()

| int max22017\_reg\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *value* ) |

`#include <[max22017.h](max22017_8h.md)>`

Read register from max22017.

Parameters
:   | dev | max22017 mfd device |
    | --- | --- |
    | addr | register address to read from |
    | value | pointer to buffer for received data |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any error (see [spi\_transceive\_dt()](group__spi__interface.md#ga52c017066736414b31ff709ddc67c4ff "Read/write data from an SPI bus specified in spi_dt_spec.")) |

## [◆ ](#gac4a4a29f7ae31af97f19d700264a604d)max22017\_reg\_write()

| int max22017\_reg\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

`#include <[max22017.h](max22017_8h.md)>`

Write register to max22017.

Parameters
:   | dev | max22017 mfd device |
    | --- | --- |
    | addr | register address to write to |
    | value | content to write |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any error (see [spi\_write\_dt()](group__spi__interface.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b "Write data to a SPI bus specified in spi_dt_spec.")) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
