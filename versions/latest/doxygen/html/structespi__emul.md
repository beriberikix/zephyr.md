---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structespi__emul.html
original_path: doxygen/html/structespi__emul.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_emul Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md) » [eSPI Emulation Interface](group__espi__emul__interface.md)

Node in a linked list of emulators for eSPI devices.
[More...](#details)

`#include <[espi_emul.h](espi__emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a495cddd3fc6300f2c7eb3e98caafecd5) |
| const struct [emul](structemul.md) \* | [target](#a27aa4069611f537b470a9c64d7913c91) |
|  | Target emulator - REQUIRED for all emulated bus nodes of any type. |
| const struct [emul\_espi\_device\_api](structemul__espi__device__api.md) \* | [api](#a1c80c40cdc25bb5440d57c3aef7379eb) |
|  | API provided for this device. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chipsel](#a29554137c4ef3fbf4f7a087d01602adb) |
|  | eSPI chip-select of the emulated device |

## Detailed Description

Node in a linked list of emulators for eSPI devices.

## Field Documentation

## [◆ ](#a1c80c40cdc25bb5440d57c3aef7379eb)api

| const struct [emul\_espi\_device\_api](structemul__espi__device__api.md)\* espi\_emul::api |
| --- |

API provided for this device.

## [◆ ](#a29554137c4ef3fbf4f7a087d01602adb)chipsel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) espi\_emul::chipsel |
| --- |

eSPI chip-select of the emulated device

## [◆ ](#a495cddd3fc6300f2c7eb3e98caafecd5)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) espi\_emul::node |
| --- |

## [◆ ](#a27aa4069611f537b470a9c64d7913c91)target

| const struct [emul](structemul.md)\* espi\_emul::target |
| --- |

Target emulator - REQUIRED for all emulated bus nodes of any type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi\_emul.h](espi__emul_8h_source.md)

- [espi\_emul](structespi__emul.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
