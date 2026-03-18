---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi2c__msg.html
original_path: doxygen/html/structi2c__msg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_msg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I2C Interface](group__i2c__interface.md)

One I2C Message.
[More...](#details)

`#include <[i2c.h](drivers_2i2c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#ac4aa590487270589a51964b38f853a37) |
|  | Data buffer in bytes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#ae122c36d1fdc0829321fa116921d7a52) |
|  | Length of buffer in bytes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#ae6f9dc8a50b611adbca38e29b529ab9c) |
|  | Flags for this message. |

## Detailed Description

One I2C Message.

This defines one I2C message to transact on the I2C bus.

Note
:   Some of the configurations supported by this API may not be supported by specific SoC I2C hardware implementations, in particular features related to bus transactions intended to read or write data from different buffers within a single transaction. Invocations of [i2c\_transfer()](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e "Perform data transfer to another I2C device in controller mode.") may not indicate an error when an unsupported configuration is encountered. In some cases drivers will generate separate transactions for each message fragment, with or without presence of [I2C\_MSG\_RESTART](group__i2c__interface.md#ga8c6cf7be2a04979fdb9d0b7dd9c4f831 "I2C_MSG_RESTART") in [flags](#ae6f9dc8a50b611adbca38e29b529ab9c).

## Field Documentation

## [◆ ](#ac4aa590487270589a51964b38f853a37)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* i2c\_msg::buf |
| --- |

Data buffer in bytes.

## [◆ ](#ae6f9dc8a50b611adbca38e29b529ab9c)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i2c\_msg::flags |
| --- |

Flags for this message.

## [◆ ](#ae122c36d1fdc0829321fa116921d7a52)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i2c\_msg::len |
| --- |

Length of buffer in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i2c.h](drivers_2i2c_8h_source.md)

- [i2c\_msg](structi2c__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
