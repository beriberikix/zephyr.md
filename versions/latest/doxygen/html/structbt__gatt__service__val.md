---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__gatt__service__val.html
original_path: doxygen/html/structbt__gatt__service__val.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_service\_val Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

Service Attribute Value.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#a683e01db92400e76aed32b7a81369a55) |
|  | Service UUID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [end\_handle](#a75b6fcf0f9f29ad05ccac0e83bcb31b7) |
|  | Service end handle. |

## Detailed Description

Service Attribute Value.

## Field Documentation

## [◆ ](#a75b6fcf0f9f29ad05ccac0e83bcb31b7)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_service\_val::end\_handle |
| --- |

Service end handle.

## [◆ ](#a683e01db92400e76aed32b7a81369a55)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_gatt\_service\_val::uuid |
| --- |

Service UUID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_service\_val](structbt__gatt__service__val.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
