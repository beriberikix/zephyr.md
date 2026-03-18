---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmspi__emul.html
original_path: doxygen/html/structmspi__emul.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_emul Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md) » [MSPI Emulation Interface](group__mspi__emul__interface.md)

Node in a linked list of emulators for MSPI devices.
[More...](#details)

`#include <[mspi_emul.h](mspi__emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#aa3e45d11717b737ea8c6b4b19459991a) |
| const struct [emul](structemul.md) \* | [target](#aa2b65e70ab7c2218929a6042bd0fd548) |
|  | Target emulator - REQUIRED for all emulated bus nodes of any type. |
| const struct [emul\_mspi\_device\_api](structemul__mspi__device__api.md) \* | [api](#a2d247195c375c1aac30beec32dc11099) |
|  | API provided for this device. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dev\_idx](#a5386510f101d186581abbde6b624be09) |
|  | device index |

## Detailed Description

Node in a linked list of emulators for MSPI devices.

## Field Documentation

## [◆ ](#a2d247195c375c1aac30beec32dc11099)api

| const struct [emul\_mspi\_device\_api](structemul__mspi__device__api.md)\* mspi\_emul::api |
| --- |

API provided for this device.

## [◆ ](#a5386510f101d186581abbde6b624be09)dev\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mspi\_emul::dev\_idx |
| --- |

device index

## [◆ ](#aa3e45d11717b737ea8c6b4b19459991a)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) mspi\_emul::node |
| --- |

## [◆ ](#aa2b65e70ab7c2218929a6042bd0fd548)target

| const struct [emul](structemul.md)\* mspi\_emul::target |
| --- |

Target emulator - REQUIRED for all emulated bus nodes of any type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi\_emul.h](mspi__emul_8h_source.md)

- [mspi\_emul](structmspi__emul.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
