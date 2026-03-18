---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__gatt__include.html
original_path: doxygen/html/structbt__gatt__include.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_include Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

Include Attribute Value.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#afa028e8daae00e3b1bc0b866c4335af3) |
|  | Service UUID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_handle](#ac7f6c1a8018f483dce14f0fe21031232) |
|  | Service start handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [end\_handle](#a54d20cebfd6ba62b692c363acdc25d61) |
|  | Service end handle. |

## Detailed Description

Include Attribute Value.

## Field Documentation

## [◆ ](#a54d20cebfd6ba62b692c363acdc25d61)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_include::end\_handle |
| --- |

Service end handle.

## [◆ ](#ac7f6c1a8018f483dce14f0fe21031232)start\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_include::start\_handle |
| --- |

Service start handle.

## [◆ ](#afa028e8daae00e3b1bc0b866c4335af3)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_include::uuid |
| --- |

Service UUID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_include](structbt__gatt__include.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
