---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__gatt__chrc.html
original_path: doxygen/html/structbt__gatt__chrc.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_chrc Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

Characteristic Attribute Value.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#af3b4c22ae37b912c8edf58294cc50702) |
|  | Characteristic UUID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [value\_handle](#a2ca6aec1a621fdfd12142a1188d37bd3) |
|  | Characteristic Value handle. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [properties](#a81bb8257052d7c8d03b51acaa51e5011) |
|  | Characteristic properties. |

## Detailed Description

Characteristic Attribute Value.

## Field Documentation

## [◆ ](#a81bb8257052d7c8d03b51acaa51e5011)properties

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_gatt\_chrc::properties |
| --- |

Characteristic properties.

## [◆ ](#af3b4c22ae37b912c8edf58294cc50702)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_chrc::uuid |
| --- |

Characteristic UUID.

## [◆ ](#a2ca6aec1a621fdfd12142a1188d37bd3)value\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_chrc::value\_handle |
| --- |

Characteristic Value handle.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_chrc](structbt__gatt__chrc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
