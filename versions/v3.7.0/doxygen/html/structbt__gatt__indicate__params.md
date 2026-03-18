---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__gatt__indicate__params.html
original_path: doxygen/html/structbt__gatt__indicate__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_indicate\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Server APIs](group__bt__gatt__server.md)

GATT Indicate Value parameters.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#afde06f47d7a817291e437593ea01bccd) |
|  | Indicate Attribute UUID type. |
| const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [attr](#acbbee3a71838492416b20bb5cff89801) |
|  | Indicate Attribute object. |
| [bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8) | [func](#af9eb83c3fba49ee3cd6162d5a2791707) |
|  | Indicate Value callback. |
| [bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe) | [destroy](#aeb346dc4c0e4a298c66f394d037a6514) |
|  | Indicate operation complete callback. |
| const void \* | [data](#ae1d657512c99d5bba6fc99a450a6da32) |
|  | Indicate Value data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a10ad44140371165951eeac18cb3d0e7f) |
|  | Indicate Value length. |
| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) | [chan\_opt](#a0e536938123ecb4f3ba6736c1de2a599) |

## Detailed Description

GATT Indicate Value parameters.

## Field Documentation

## [◆ ](#acbbee3a71838492416b20bb5cff89801)attr

| const struct [bt\_gatt\_attr](structbt__gatt__attr.md)\* bt\_gatt\_indicate\_params::attr |
| --- |

Indicate Attribute object.

Optional if uuid is provided, in this case it will be used as start range to search for the attribute with the given UUID.

## [◆ ](#a0e536938123ecb4f3ba6736c1de2a599)chan\_opt

| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) bt\_gatt\_indicate\_params::chan\_opt |
| --- |

## [◆ ](#ae1d657512c99d5bba6fc99a450a6da32)data

| const void\* bt\_gatt\_indicate\_params::data |
| --- |

Indicate Value data.

## [◆ ](#aeb346dc4c0e4a298c66f394d037a6514)destroy

| [bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe) bt\_gatt\_indicate\_params::destroy |
| --- |

Indicate operation complete callback.

## [◆ ](#af9eb83c3fba49ee3cd6162d5a2791707)func

| [bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8) bt\_gatt\_indicate\_params::func |
| --- |

Indicate Value callback.

## [◆ ](#a10ad44140371165951eeac18cb3d0e7f)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_indicate\_params::len |
| --- |

Indicate Value length.

## [◆ ](#afde06f47d7a817291e437593ea01bccd)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_indicate\_params::uuid |
| --- |

Indicate Attribute UUID type.

Optional, use to search for an attribute with matching UUID when the attribute object pointer is not known.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
