---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__ots__obj__created__desc.html
original_path: doxygen/html/structbt__ots__obj__created__desc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ots\_obj\_created\_desc Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Object Transfer Service (OTS)](group__bt__ots.md)

Descriptor for OTS created object.
[More...](#details)

`#include <[ots.h](ots_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [name](#af69db0a3c56c6d3085f20fbb405b436e) |
|  | Object name. |
| struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) | [size](#adb52cffa29c08ee1131415faeaf13cda) |
|  | Object size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [props](#a50b2b2ae0b87690d1995187bae577e8c) |
|  | Object properties. |

## Detailed Description

Descriptor for OTS created object.

Descriptor for OTS object created by the application. This descriptor is returned by [bt\_ots\_cb::obj\_created](structbt__ots__cb.md#a0c95b2bc382474be3c1ae849936a8206 "bt_ots_cb::obj_created") callback which contains further documentation on distinguishing between server and client object creation.

## Field Documentation

## [◆ ](#af69db0a3c56c6d3085f20fbb405b436e)name

| char\* bt\_ots\_obj\_created\_desc::name |
| --- |

Object name.

The object name as a NULL terminated string.

When the server creates a new object the name shall be > 0 and <= BT\_OTS\_OBJ\_MAX\_NAME\_LEN When the client creates a new object the name shall be an empty string

## [◆ ](#a50b2b2ae0b87690d1995187bae577e8c)props

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_ots\_obj\_created\_desc::props |
| --- |

Object properties.

## [◆ ](#adb52cffa29c08ee1131415faeaf13cda)size

| struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) bt\_ots\_obj\_created\_desc::size |
| --- |

Object size.

[bt\_ots\_obj\_size::alloc](structbt__ots__obj__size.md#a86a5675532eae69d40b3305436e81cfb "bt_ots_obj_size::alloc") shall be >= [bt\_ots\_obj\_add\_param::size](structbt__ots__obj__add__param.md#a721734439b43e40324c3a548b5a4eb34 "bt_ots_obj_add_param::size")

When the server creates a new object [bt\_ots\_obj\_size::cur](structbt__ots__obj__size.md#a217290f0fae68a54046eef50ac2a3773 "bt_ots_obj_size::cur") shall be <= [bt\_ots\_obj\_add\_param::size](structbt__ots__obj__add__param.md#a721734439b43e40324c3a548b5a4eb34 "bt_ots_obj_add_param::size") When the client creates a new object [bt\_ots\_obj\_size::cur](structbt__ots__obj__size.md#a217290f0fae68a54046eef50ac2a3773 "bt_ots_obj_size::cur") shall be 0

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ots.h](ots_8h_source.md)

- [bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
