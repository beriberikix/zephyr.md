---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__dev__list.html
original_path: doxygen/html/structi3c__dev__list.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_dev\_list Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

Structure for describing known devices for a controller.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \*const | [i3c](#aba1871e32e1ee9e6a809dd11a7a44dce) |
|  | Pointer to array of known I3C devices. |
| struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*const | [i2c](#a7993101f7b5fa3961773f58fd8b1985e) |
|  | Pointer to array of known I2C devices. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_i3c](#ab13b77da61fc829c3f6414963f5f2985) |
|  | Number of I3C devices in array. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_i2c](#ae1b33a38150098463187d4016e31b318) |
|  | Number of I2C devices in array. |

## Detailed Description

Structure for describing known devices for a controller.

This contains arrays of known I3C and I2C devices.

This is a helper struct that can be used by controller device driver to aid in device management.

## Field Documentation

## [◆ ](#a7993101f7b5fa3961773f58fd8b1985e)i2c

| struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md)\* const i3c\_dev\_list::i2c |
| --- |

Pointer to array of known I2C devices.

## [◆ ](#aba1871e32e1ee9e6a809dd11a7a44dce)i3c

| struct [i3c\_device\_desc](structi3c__device__desc.md)\* const i3c\_dev\_list::i3c |
| --- |

Pointer to array of known I3C devices.

## [◆ ](#ae1b33a38150098463187d4016e31b318)num\_i2c

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_dev\_list::num\_i2c |
| --- |

Number of I2C devices in array.

## [◆ ](#ab13b77da61fc829c3f6414963f5f2985)num\_i3c

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_dev\_list::num\_i3c |
| --- |

Number of I3C devices in array.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_dev\_list](structi3c__dev__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
