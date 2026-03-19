---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__ots__obj__metadata.html
original_path: doxygen/html/structbt__ots__obj__metadata.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ots\_obj\_metadata Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Object Transfer Service (OTS)](group__bt__ots.md)

Metadata of an OTS object.
[More...](#details)

`#include <[ots.h](ots_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_ots\_obj\_type](structbt__ots__obj__type.md) | [type](#aee93aef1932e9c8b4cb0c8055e5cb055) |
|  | Object Type. |
| struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) | [size](#afd451a3b531250db1d45eb6ddb4d9b0f) |
|  | Object Size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [props](#aa4ffe00ede40ff23ab5788c82ec2ac38) |
|  | Object Properties. |

## Detailed Description

Metadata of an OTS object.

Used by the server as a descriptor for OTS object initialization. Used by the client to present object metadata to the application.

## Field Documentation

## [◆ ](#aa4ffe00ede40ff23ab5788c82ec2ac38)props

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_ots\_obj\_metadata::props |
| --- |

Object Properties.

## [◆ ](#afd451a3b531250db1d45eb6ddb4d9b0f)size

| struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) bt\_ots\_obj\_metadata::size |
| --- |

Object Size.

## [◆ ](#aee93aef1932e9c8b4cb0c8055e5cb055)type

| struct [bt\_ots\_obj\_type](structbt__ots__obj__type.md) bt\_ots\_obj\_metadata::type |
| --- |

Object Type.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ots.h](ots_8h_source.md)

- [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
