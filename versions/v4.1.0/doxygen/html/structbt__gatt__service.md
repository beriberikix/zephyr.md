---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__gatt__service.html
original_path: doxygen/html/structbt__gatt__service.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_service Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

GATT Service structure.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [attrs](#a0281e96ab54519df641f6c489fdc6b5b) |
|  | Service Attributes. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [attr\_count](#a87d8316a92ae04678d7be0ae76ed86cb) |
|  | Service Attribute count. |

## Detailed Description

GATT Service structure.

This structure is used to define GATT services which can be registered and unregistered at runtime. See [bt\_gatt\_service\_register](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64 "bt_gatt_service_register") for when services should be registered.

## Field Documentation

## [◆ ](#a87d8316a92ae04678d7be0ae76ed86cb)attr\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_gatt\_service::attr\_count |
| --- |

Service Attribute count.

## [◆ ](#a0281e96ab54519df641f6c489fdc6b5b)attrs

| struct [bt\_gatt\_attr](structbt__gatt__attr.md)\* bt\_gatt\_service::attrs |
| --- |

Service Attributes.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_service](structbt__gatt__service.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
