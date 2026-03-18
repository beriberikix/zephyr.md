---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi2c__emul.html
original_path: doxygen/html/structi2c__emul.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_emul Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md) » [I2C Emulation Interface](group__i2c__emul__interface.md)

Node in a linked list of emulators for I2C devices.
[More...](#details)

`#include <[i2c_emul.h](i2c__emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a72324f94030625a8be49101f49875a7a) |
| const struct [emul](structemul.md) \* | [target](#a33461303343c3f513a87f1783491324a) |
|  | Target emulator - REQUIRED for all emulated bus nodes of any type. |
| const struct [i2c\_emul\_api](structi2c__emul__api.md) \* | [api](#a7e6f7e6e69064df666584027c94bf98c) |
| struct [i2c\_emul\_api](structi2c__emul__api.md) \* | [mock\_api](#abf57cb711e20ab11aa5af247ccc652b2) |
|  | A mock API that if not NULL will take precedence over the actual API. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a8d3924790bd825afe41095bfdf0087eb) |

## Detailed Description

Node in a linked list of emulators for I2C devices.

## Field Documentation

## [◆ ](#a8d3924790bd825afe41095bfdf0087eb)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i2c\_emul::addr |
| --- |

## [◆ ](#a7e6f7e6e69064df666584027c94bf98c)api

| const struct [i2c\_emul\_api](structi2c__emul__api.md)\* i2c\_emul::api |
| --- |

## [◆ ](#abf57cb711e20ab11aa5af247ccc652b2)mock\_api

| struct [i2c\_emul\_api](structi2c__emul__api.md)\* i2c\_emul::mock\_api |
| --- |

A mock API that if not NULL will take precedence over the actual API.

If set, a return value of -ENOSYS will revert back to the default api.

## [◆ ](#a72324f94030625a8be49101f49875a7a)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) i2c\_emul::node |
| --- |

## [◆ ](#a33461303343c3f513a87f1783491324a)target

| const struct [emul](structemul.md)\* i2c\_emul::target |
| --- |

Target emulator - REQUIRED for all emulated bus nodes of any type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i2c\_emul.h](i2c__emul_8h_source.md)

- [i2c\_emul](structi2c__emul.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
