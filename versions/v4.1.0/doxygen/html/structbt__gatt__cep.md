---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__gatt__cep.html
original_path: doxygen/html/structbt__gatt__cep.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_cep Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

Characteristic Extended Properties Attribute Value.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [properties](#a317442dc204f7632b0c5da8a8a9a98b5) |
|  | Characteristic Extended properties, a bitmap of BT\_GATT\_CEP\_\* macros. |

## Detailed Description

Characteristic Extended Properties Attribute Value.

Used in the discovery of standard characteristic descriptor values. Shall exist if the [BT\_GATT\_CHRC\_EXT\_PROP](group__bt__gatt.md#gac84d73a0ad50bfd149ad83181315de1a "BT_GATT_CHRC_EXT_PROP") bit is set in the characteristic properties. Can be used with the [BT\_GATT\_CEP](group__bt__gatt__server.md#ga55a82cada1093c4ff75fe5504ac504b1 "BT_GATT_CEP") macro to declare the CEP descriptor.

## Field Documentation

## [◆ ](#a317442dc204f7632b0c5da8a8a9a98b5)properties

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_cep::properties |
| --- |

Characteristic Extended properties, a bitmap of BT\_GATT\_CEP\_\* macros.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_cep](structbt__gatt__cep.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
