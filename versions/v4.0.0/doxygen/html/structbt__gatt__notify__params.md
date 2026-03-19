---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__gatt__notify__params.html
original_path: doxygen/html/structbt__gatt__notify__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_notify\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Server APIs](group__bt__gatt__server.md)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#a2994cbe737fad725c60427000c21c373) |
|  | Notification Attribute UUID type. |
| const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [attr](#a6187d0457763a15a623129e3e9e98e13) |
|  | Notification Attribute object. |
| const void \* | [data](#afaa276cff9cbf204c433ca776904ef32) |
|  | Notification Value data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a4a511da0b099ca88d895594caf7aaa6a) |
|  | Notification Value length. |
| [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) | [func](#ace3c6b5f5ed78b9f64c25b868d3bfbe2) |
|  | Notification Value callback. |
| void \* | [user\_data](#adec9a6f6ea0604e82b90dd47bb9951fa) |
|  | Notification Value callback user data. |
| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) | [chan\_opt](#a978d7a42c39a098cedf751936f280fac) |

## Field Documentation

## [◆ ](#a6187d0457763a15a623129e3e9e98e13)attr

| const struct [bt\_gatt\_attr](structbt__gatt__attr.md)\* bt\_gatt\_notify\_params::attr |
| --- |

Notification Attribute object.

Optional if uuid is provided, in this case it will be used as start range to search for the attribute with the given UUID.

## [◆ ](#a978d7a42c39a098cedf751936f280fac)chan\_opt

| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) bt\_gatt\_notify\_params::chan\_opt |
| --- |

## [◆ ](#afaa276cff9cbf204c433ca776904ef32)data

| const void\* bt\_gatt\_notify\_params::data |
| --- |

Notification Value data.

## [◆ ](#ace3c6b5f5ed78b9f64c25b868d3bfbe2)func

| [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) bt\_gatt\_notify\_params::func |
| --- |

Notification Value callback.

## [◆ ](#a4a511da0b099ca88d895594caf7aaa6a)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_notify\_params::len |
| --- |

Notification Value length.

## [◆ ](#adec9a6f6ea0604e82b90dd47bb9951fa)user\_data

| void\* bt\_gatt\_notify\_params::user\_data |
| --- |

Notification Value callback user data.

## [◆ ](#a2994cbe737fad725c60427000c21c373)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_notify\_params::uuid |
| --- |

Notification Attribute UUID type.

Optional, use to search for an attribute with matching UUID when the attribute object pointer is not known.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
