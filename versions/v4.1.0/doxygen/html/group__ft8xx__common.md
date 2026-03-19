---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ft8xx__common.html
original_path: doxygen/html/group__ft8xx__common.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FT8xx common functions

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md) » [FT8xx driver APIs](group__ft8xx__interface.md)

FT8xx functions to write and read memory.
[More...](#details)

| Functions | |
| --- | --- |
| void | [ft8xx\_wr8](#ga2c8c5d06b09549ab041bbff4612b4620) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write 1 byte (8 bits) to FT8xx memory. |
| void | [ft8xx\_wr16](#gaa6d306b1e2701e0de415c64d33e575a4) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write 2 bytes (16 bits) to FT8xx memory. |
| void | [ft8xx\_wr32](#gada8d996d58f0f46f3f56534ee0da4c68) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write 4 bytes (32 bits) to FT8xx memory. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ft8xx\_rd8](#gab8235ed0c0f7373628457fcf64e15fbd) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 1 byte (8 bits) from FT8xx memory. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ft8xx\_rd16](#ga743c2d25f728451e98417b2ebcc9c722) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 2 bytes (16 bits) from FT8xx memory. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ft8xx\_rd32](#gaed670a8410224f8f3970fad86705f513) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 4 bytes (32 bits) from FT8xx memory. |

## Detailed Description

FT8xx functions to write and read memory.

## Function Documentation

## [◆ ](#ga743c2d25f728451e98417b2ebcc9c722)ft8xx\_rd16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ft8xx\_rd16 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Read 2 bytes (16 bits) from FT8xx memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | address | Memory address to read from |

Returns
:   Value read from memory

## [◆ ](#gaed670a8410224f8f3970fad86705f513)ft8xx\_rd32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ft8xx\_rd32 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Read 4 bytes (32 bits) from FT8xx memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | address | Memory address to read from |

Returns
:   Value read from memory

## [◆ ](#gab8235ed0c0f7373628457fcf64e15fbd)ft8xx\_rd8()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ft8xx\_rd8 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Read 1 byte (8 bits) from FT8xx memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | address | Memory address to read from |

Returns
:   Value read from memory

## [◆ ](#gaa6d306b1e2701e0de415c64d33e575a4)ft8xx\_wr16()

| void ft8xx\_wr16 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Write 2 bytes (16 bits) to FT8xx memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | address | Memory address to write to |
    | data | Value to write |

## [◆ ](#gada8d996d58f0f46f3f56534ee0da4c68)ft8xx\_wr32()

| void ft8xx\_wr32 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Write 4 bytes (32 bits) to FT8xx memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | address | Memory address to write to |
    | data | Value to write |

## [◆ ](#ga2c8c5d06b09549ab041bbff4612b4620)ft8xx\_wr8()

| void ft8xx\_wr8 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Write 1 byte (8 bits) to FT8xx memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | address | Memory address to write to |
    | data | Byte to write |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
