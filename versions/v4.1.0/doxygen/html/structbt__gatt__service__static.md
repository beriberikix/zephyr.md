---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__gatt__service__static.html
original_path: doxygen/html/structbt__gatt__service__static.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_service\_static Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

Static GATT Service structure.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [attrs](#a38f9e02241fe37f68df5dd8782b59e9f) |
|  | Service Attributes. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [attr\_count](#a84c35a391e372396e2ec89eaf0d4d047) |
|  | Service Attribute count. |

## Detailed Description

Static GATT Service structure.

Allows the user the declare static GATT Services with the aim of reducing the used RAM. The [BT\_GATT\_SERVICE\_DEFINE](group__bt__gatt__server.md#ga04c7887fb67107bd060dd023fd3186d5 "BT_GATT_SERVICE_DEFINE") macro can be used to statically define and register a service.

## Field Documentation

## [◆ ](#a84c35a391e372396e2ec89eaf0d4d047)attr\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_gatt\_service\_static::attr\_count |
| --- |

Service Attribute count.

## [◆ ](#a38f9e02241fe37f68df5dd8782b59e9f)attrs

| const struct [bt\_gatt\_attr](structbt__gatt__attr.md)\* bt\_gatt\_service\_static::attrs |
| --- |

Service Attributes.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_service\_static](structbt__gatt__service__static.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
