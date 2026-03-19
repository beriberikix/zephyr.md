---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structuart__emul.html
original_path: doxygen/html/structuart__emul.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_emul Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md) » [UART Emulation Interface](group__uart__emul__interface.md)

Node in a linked list of emulators for UART devices.
[More...](#details)

`#include <[uart_emul.h](uart__emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a5d363d3cd85e7fed7ce2f24f5a75243a) |
| const struct [emul](structemul.md) \* | [target](#ab0fa46fc3bae0c089555ca1045924e60) |
|  | Target emulator - REQUIRED for all emulated bus nodes of any type. |
| const struct [uart\_emul\_device\_api](structuart__emul__device__api.md) \* | [api](#a6bf13a7090376d6f3419f5c6a6ca1608) |
|  | API provided for this device. |

## Detailed Description

Node in a linked list of emulators for UART devices.

## Field Documentation

## [◆ ](#a6bf13a7090376d6f3419f5c6a6ca1608)api

| const struct [uart\_emul\_device\_api](structuart__emul__device__api.md)\* uart\_emul::api |
| --- |

API provided for this device.

## [◆ ](#a5d363d3cd85e7fed7ce2f24f5a75243a)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) uart\_emul::node |
| --- |

## [◆ ](#ab0fa46fc3bae0c089555ca1045924e60)target

| const struct [emul](structemul.md)\* uart\_emul::target |
| --- |

Target emulator - REQUIRED for all emulated bus nodes of any type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[uart\_emul.h](uart__emul_8h_source.md)

- [uart\_emul](structuart__emul.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
