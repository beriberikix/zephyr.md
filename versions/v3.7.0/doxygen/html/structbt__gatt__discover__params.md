---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__gatt__discover__params.html
original_path: doxygen/html/structbt__gatt__discover__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_discover\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Client APIs](group__bt__gatt__client.md)

GATT Discover Attributes parameters.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#a77d6665c01902e4e23cf8de8a9436262) |
|  | Discover UUID type. |
| [bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13) | [func](#a337d7366c12451938f12eec4dc60903e) |
|  | Discover attribute callback. |
| union { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [start\_handle](#a0d2604e7c3ee8969cb5096cbf5793fdb) |  |
|  | Discover start handle. [More...](#a0d2604e7c3ee8969cb5096cbf5793fdb) |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#ab0f056c90954e1246d897019abd1e7fc) |
|  | Discover type. |
| struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \* | [sub\_params](#a87b130c520ce50f835d0589fd22a844c) |
|  | Only for stack-internal use, used for automatic discovery. |
| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) | [chan\_opt](#aba7585e3d0eefb323fcde9bcc88e287d) |

## Detailed Description

GATT Discover Attributes parameters.

## Field Documentation

## [◆ ](#aa154a2c9ecd52861a69846831d006277)[union]

| union { ... } [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) |
| --- |

## [◆ ](#a65ca3c9aad7c02d48fd35c4d6f69dc70)attr\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_discover\_params::attr\_handle |
| --- |

Include service attribute declaration handle.

## [◆ ](#aba7585e3d0eefb323fcde9bcc88e287d)chan\_opt

| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) bt\_gatt\_discover\_params::chan\_opt |
| --- |

## [◆ ](#a225868498c34411cc3fc2be8e678e85e)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_discover\_params::end\_handle |
| --- |

Included service end handle.

Discover end handle.

## [◆ ](#a337d7366c12451938f12eec4dc60903e)func

| [bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13) bt\_gatt\_discover\_params::func |
| --- |

Discover attribute callback.

## [◆ ](#a0d2604e7c3ee8969cb5096cbf5793fdb)start\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_discover\_params::start\_handle |
| --- |

Included service start handle.

Discover start handle.

## [◆ ](#a87b130c520ce50f835d0589fd22a844c)sub\_params

| struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md)\* bt\_gatt\_discover\_params::sub\_params |
| --- |

Only for stack-internal use, used for automatic discovery.

## [◆ ](#ab0f056c90954e1246d897019abd1e7fc)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_gatt\_discover\_params::type |
| --- |

Discover type.

## [◆ ](#a77d6665c01902e4e23cf8de8a9436262)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_discover\_params::uuid |
| --- |

Discover UUID type.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
