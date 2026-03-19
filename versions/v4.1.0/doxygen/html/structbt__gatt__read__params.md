---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__gatt__read__params.html
original_path: doxygen/html/structbt__gatt__read__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_read\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Client APIs](group__bt__gatt__client.md)

GATT Read parameters.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569) | [func](#a3ea107db0b7537c9dccb2aa6d8f916fb) |
|  | Read attribute callback. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [handle\_count](#a0a36063ac0b110fbf57ef6a66f7bece8) |
|  | If equals to 1 single.handle and single.offset are used. |
| union { |  |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [handle](#af37beb6a69b3a6b90da0594b099bd64d) |  |
|  | Attribute handle. [More...](#af37beb6a69b3a6b90da0594b099bd64d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [offset](#a27f685a45c405bb2784fe369513724ad) |  |
|  | Attribute data offset. [More...](#a27f685a45c405bb2784fe369513724ad) |
| }   [single](#a83a9fa7adc2ba377e15156877d9a0461) |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*   [handles](#a2794b8806933d0e16cfc77f4087fdeda) |  |
|  | Attribute handles to read with Read Multiple Characteristic Values. [More...](#a2794b8806933d0e16cfc77f4087fdeda) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [variable](#a77d05cbc54b125fc35d180cf91bf9cb9) |  |
|  | If true use Read Multiple Variable Length Characteristic Values procedure. [More...](#a77d05cbc54b125fc35d180cf91bf9cb9) |
| }   [multiple](#a179a4a97b72819b670f10103b1946917) |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [start\_handle](#ac11db1652cd5cee567d666d3697f3a4b) |  |
|  | Attribute handle to start reading from. [More...](#ac11db1652cd5cee567d666d3697f3a4b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [end\_handle](#a8b2a2b912efe557e24276a654087e75c) |  |
|  | Attribute handle to stop reading at. [More...](#a8b2a2b912efe557e24276a654087e75c) |
| const struct [bt\_uuid](structbt__uuid.md) \*   [uuid](#ae2ba6ce4043769b86a050fd767248111) |  |
|  | 2 or 16 octet UUID. [More...](#ae2ba6ce4043769b86a050fd767248111) |
| }   [by\_uuid](#afef3c0fbbfc29c5476253ba738e5a1f1) |
| }; |  |
| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) | [chan\_opt](#a1335d1f9aefeff89a57efe78335cb41b) |
|  | Att channel options. |

## Detailed Description

GATT Read parameters.

## Field Documentation

## [◆ ](#a5e9291e0dd1a79b8120a0834daac2a57)[union]

| union { ... } [bt\_gatt\_read\_params](structbt__gatt__read__params.md) |
| --- |

## [◆ ](#afef3c0fbbfc29c5476253ba738e5a1f1)[struct]

| struct { ... } bt\_gatt\_read\_params::by\_uuid |
| --- |

## [◆ ](#a1335d1f9aefeff89a57efe78335cb41b)chan\_opt

| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) bt\_gatt\_read\_params::chan\_opt |
| --- |

Att channel options.

## [◆ ](#a8b2a2b912efe557e24276a654087e75c)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_read\_params::end\_handle |
| --- |

Attribute handle to stop reading at.

## [◆ ](#a3ea107db0b7537c9dccb2aa6d8f916fb)func

| [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569) bt\_gatt\_read\_params::func |
| --- |

Read attribute callback.

## [◆ ](#af37beb6a69b3a6b90da0594b099bd64d)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_read\_params::handle |
| --- |

Attribute handle.

## [◆ ](#a0a36063ac0b110fbf57ef6a66f7bece8)handle\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_gatt\_read\_params::handle\_count |
| --- |

If equals to 1 single.handle and single.offset are used.

If greater than 1 multiple.handles are used. If equals to 0 by\_uuid is used for Read Using Characteristic UUID.

## [◆ ](#a2794b8806933d0e16cfc77f4087fdeda)handles

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* bt\_gatt\_read\_params::handles |
| --- |

Attribute handles to read with Read Multiple Characteristic Values.

## [◆ ](#a179a4a97b72819b670f10103b1946917)[struct]

| struct { ... } bt\_gatt\_read\_params::multiple |
| --- |

## [◆ ](#a27f685a45c405bb2784fe369513724ad)offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_read\_params::offset |
| --- |

Attribute data offset.

## [◆ ](#a83a9fa7adc2ba377e15156877d9a0461)[struct]

| struct { ... } bt\_gatt\_read\_params::single |
| --- |

## [◆ ](#ac11db1652cd5cee567d666d3697f3a4b)start\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_read\_params::start\_handle |
| --- |

Attribute handle to start reading from.

## [◆ ](#ae2ba6ce4043769b86a050fd767248111)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_read\_params::uuid |
| --- |

2 or 16 octet UUID.

## [◆ ](#a77d05cbc54b125fc35d180cf91bf9cb9)variable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_gatt\_read\_params::variable |
| --- |

If true use Read Multiple Variable Length Characteristic Values procedure.

The values of the set of attributes may be of variable or unknown length. If false use Read Multiple Characteristic Values procedure. The values of the set of attributes must be of a known fixed length, with the exception of the last value that can have a variable length.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_read\_params](structbt__gatt__read__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
