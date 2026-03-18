---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__conn__remote__info.html
original_path: doxygen/html/structbt__conn__remote__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_remote\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Connection Remote Info Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a8bb514196bde5df561dbf76b68060729) |
|  | Connection Type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [version](#a2664f6ed3bd22f9a011126daf5d81376) |
|  | Remote Link Layer version. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [manufacturer](#a47cc5a4b8888a0b8faaf6880c37418b8) |
|  | Remote manufacturer identifier. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subversion](#a360979a15c958706157fc630fd55cbca) |
|  | Per-manufacturer unique revision. |
| union { |  |
| struct [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md)   [le](#ae75530b09c6dea416630a4a19a1d64cc) |  |
|  | LE connection remote info. [More...](#ae75530b09c6dea416630a4a19a1d64cc) |
| struct [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md)   [br](#ab73365f09cdb5ce870272546543bcfeb) |  |
|  | BR/EDR connection remote info. [More...](#ab73365f09cdb5ce870272546543bcfeb) |
| }; |  |

## Detailed Description

Connection Remote Info Structure.

Note
:   The version, manufacturer and subversion fields will only contain valid data if `CONFIG_BT_REMOTE_VERSION` is enabled.

## Field Documentation

## [◆ ](#a6de5ee17bde4e508be99553ce21e8c55)[union]

| union { ... } [bt\_conn\_remote\_info](structbt__conn__remote__info.md) |
| --- |

## [◆ ](#ab73365f09cdb5ce870272546543bcfeb)br

| struct [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md) bt\_conn\_remote\_info::br |
| --- |

BR/EDR connection remote info.

## [◆ ](#ae75530b09c6dea416630a4a19a1d64cc)le

| struct [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md) bt\_conn\_remote\_info::le |
| --- |

LE connection remote info.

## [◆ ](#a47cc5a4b8888a0b8faaf6880c37418b8)manufacturer

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_remote\_info::manufacturer |
| --- |

Remote manufacturer identifier.

## [◆ ](#a360979a15c958706157fc630fd55cbca)subversion

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_remote\_info::subversion |
| --- |

Per-manufacturer unique revision.

## [◆ ](#a8bb514196bde5df561dbf76b68060729)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_remote\_info::type |
| --- |

Connection Type.

## [◆ ](#a2664f6ed3bd22f9a011126daf5d81376)version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_remote\_info::version |
| --- |

Remote Link Layer version.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_remote\_info](structbt__conn__remote__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
