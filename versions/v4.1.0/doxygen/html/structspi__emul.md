---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structspi__emul.html
original_path: doxygen/html/structspi__emul.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_emul Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md) » [SPI Emulation Interface](group__spi__emul__interface.md)

Node in a linked list of emulators for SPI devices.
[More...](#details)

`#include <[spi_emul.h](spi__emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a4c49c2c9966eec74a9d010d22176bdd1) |
| const struct [emul](structemul.md) \* | [target](#a371b2447cf16752c191cc5a0aff26a57) |
|  | Target emulator - REQUIRED for all bus emulators. |
| const struct [spi\_emul\_api](structspi__emul__api.md) \* | [api](#a96649e8ea8360ad07ebbd721f999b0e7) |
| struct [spi\_emul\_api](structspi__emul__api.md) \* | [mock\_api](#a4d174e7170a21e2f53c49e0da096a93e) |
|  | A mock API that if not NULL will take precedence over the actual API. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chipsel](#a81450c3d7701c20da8d945e390e7cd33) |

## Detailed Description

Node in a linked list of emulators for SPI devices.

## Field Documentation

## [◆ ](#a96649e8ea8360ad07ebbd721f999b0e7)api

| const struct [spi\_emul\_api](structspi__emul__api.md)\* spi\_emul::api |
| --- |

## [◆ ](#a81450c3d7701c20da8d945e390e7cd33)chipsel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) spi\_emul::chipsel |
| --- |

## [◆ ](#a4d174e7170a21e2f53c49e0da096a93e)mock\_api

| struct [spi\_emul\_api](structspi__emul__api.md)\* spi\_emul::mock\_api |
| --- |

A mock API that if not NULL will take precedence over the actual API.

If set, a return value of -ENOSYS will revert back to the default api.

## [◆ ](#a4c49c2c9966eec74a9d010d22176bdd1)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) spi\_emul::node |
| --- |

## [◆ ](#a371b2447cf16752c191cc5a0aff26a57)target

| const struct [emul](structemul.md)\* spi\_emul::target |
| --- |

Target emulator - REQUIRED for all bus emulators.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi\_emul.h](spi__emul_8h_source.md)

- [spi\_emul](structspi__emul.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
