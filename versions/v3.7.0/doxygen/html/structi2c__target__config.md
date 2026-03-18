---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi2c__target__config.html
original_path: doxygen/html/structi2c__target__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_target\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I2C Interface](group__i2c__interface.md)

Structure describing a device that supports the I2C target API.
[More...](#details)

`#include <[i2c.h](drivers_2i2c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ab2393d22d8e1fb12a389cd457d30933a) |
|  | Private, do not modify. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a25d6920d44abb1e1ce8f4c3aeb600bc5) |
|  | Flags for the target device defined by I2C\_TARGET\_FLAGS\_\* constants. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [address](#a5d531acec2b530a21b8d646ce321b6fd) |
|  | Address for this target device. |
| const struct [i2c\_target\_callbacks](structi2c__target__callbacks.md) \* | [callbacks](#ad6c9573e97ac2569455f43f022600f77) |
|  | Callback functions. |

## Detailed Description

Structure describing a device that supports the I2C target API.

Instances of this are passed to the [i2c\_target\_register()](group__i2c__interface.md#gaa47c3fde397188fa126dcaa4a6e85b47 "Registers the provided config as Target device of a controller.") and [i2c\_target\_unregister()](group__i2c__interface.md#ga11eada869173f6bd91db39c794dc8979 "Unregisters the provided config as Target device.") functions to indicate addition and removal of a target device, respective.

Fields other than `node` must be initialized by the module that implements the device behavior prior to passing the object reference to [i2c\_target\_register()](group__i2c__interface.md#gaa47c3fde397188fa126dcaa4a6e85b47 "Registers the provided config as Target device of a controller.").

## Field Documentation

## [◆ ](#a5d531acec2b530a21b8d646ce321b6fd)address

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i2c\_target\_config::address |
| --- |

Address for this target device.

## [◆ ](#ad6c9573e97ac2569455f43f022600f77)callbacks

| const struct [i2c\_target\_callbacks](structi2c__target__callbacks.md)\* i2c\_target\_config::callbacks |
| --- |

Callback functions.

## [◆ ](#a25d6920d44abb1e1ce8f4c3aeb600bc5)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i2c\_target\_config::flags |
| --- |

Flags for the target device defined by I2C\_TARGET\_FLAGS\_\* constants.

## [◆ ](#ab2393d22d8e1fb12a389cd457d30933a)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) i2c\_target\_config::node |
| --- |

Private, do not modify.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i2c.h](drivers_2i2c_8h_source.md)

- [i2c\_target\_config](structi2c__target__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
