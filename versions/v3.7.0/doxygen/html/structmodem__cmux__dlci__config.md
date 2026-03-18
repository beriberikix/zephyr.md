---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodem__cmux__dlci__config.html
original_path: doxygen/html/structmodem__cmux__dlci__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_cmux\_dlci\_config Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem CMUX](group__modem__cmux.md)

CMUX DLCI configuration.
[More...](#details)

`#include <[cmux.h](cmux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dlci\_address](#ad0b1fe93bbee6343c8446da5a0ad88c9) |
|  | DLCI channel address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#ad3d6c1e0adce243aa536e52e5e4c4374) |
|  | Receive buffer used by pipe. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#af7715440c78d87466f91464000db1fef) |
|  | Size of receive buffer used by pipe [127, ...]. |

## Detailed Description

CMUX DLCI configuration.

## Field Documentation

## [◆ ](#ad0b1fe93bbee6343c8446da5a0ad88c9)dlci\_address

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_cmux\_dlci\_config::dlci\_address |
| --- |

DLCI channel address.

## [◆ ](#ad3d6c1e0adce243aa536e52e5e4c4374)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_cmux\_dlci\_config::receive\_buf |
| --- |

Receive buffer used by pipe.

## [◆ ](#af7715440c78d87466f91464000db1fef)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_cmux\_dlci\_config::receive\_buf\_size |
| --- |

Size of receive buffer used by pipe [127, ...].

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[cmux.h](cmux_8h_source.md)

- [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
