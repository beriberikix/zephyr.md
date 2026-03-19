---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__gatt__authorization__cb.html
original_path: doxygen/html/structbt__gatt__authorization__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_authorization\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

GATT authorization callback structure.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [read\_authorize](#a7b1bcbe10f12c90ee4e3214e36e9c2a3) )(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Authorize the GATT read operation. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [write\_authorize](#a7c12bd14f87f91e672eaaf92e1aa6e7b) )(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Authorize the GATT write operation. |

## Detailed Description

GATT authorization callback structure.

## Field Documentation

## [◆ ](#a7b1bcbe10f12c90ee4e3214e36e9c2a3)read\_authorize

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_gatt\_authorization\_cb::read\_authorize) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
| --- |

Authorize the GATT read operation.

This callback allows the application to authorize the GATT read operation for the attribute that is being read.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | The attribute that is being read. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Authorize the operation and allow it to execute. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Reject the operation and prevent it from executing. |

## [◆ ](#a7c12bd14f87f91e672eaaf92e1aa6e7b)write\_authorize

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_gatt\_authorization\_cb::write\_authorize) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
| --- |

Authorize the GATT write operation.

This callback allows the application to authorize the GATT write operation for the attribute that is being written.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | The attribute that is being written. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Authorize the operation and allow it to execute. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Reject the operation and prevent it from executing. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
