---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__gatt__ccc__cfg.html
original_path: doxygen/html/structbt__gatt__ccc__cfg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_ccc\_cfg Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Server APIs](group__bt__gatt__server.md)

GATT CCC configuration entry.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#ac17ddefe7ca6dbac921ee4c6f44fbf51) |
|  | Local identity, BT\_ID\_DEFAULT in most cases. |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer](#ab316080693b2c4daf5fd45e2c0501c70) |
|  | Remote peer address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [value](#a92acf7329f66638ac6c657c8eaa795ac) |
|  | Configuration value. |

## Detailed Description

GATT CCC configuration entry.

## Field Documentation

## [◆ ](#ac17ddefe7ca6dbac921ee4c6f44fbf51)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_gatt\_ccc\_cfg::id |
| --- |

Local identity, BT\_ID\_DEFAULT in most cases.

## [◆ ](#ab316080693b2c4daf5fd45e2c0501c70)peer

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_gatt\_ccc\_cfg::peer |
| --- |

Remote peer address.

## [◆ ](#a92acf7329f66638ac6c657c8eaa795ac)value

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_ccc\_cfg::value |
| --- |

Configuration value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
