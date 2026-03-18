---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__gatt__cpf.html
original_path: doxygen/html/structbt__gatt__cpf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_cpf Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

GATT Characteristic Presentation Format Attribute Value.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [format](#ab0ca135a75130b3ffc0c5bf375f3528f) |
|  | Format of the value of the characteristic. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [exponent](#a3690a86c942badb2d2698481b03e436d) |
|  | Exponent field to determine how the value of this characteristic is further formatted. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [unit](#a2a9f3d3f72b9acb1ef7f2dc765e5a231) |
|  | Unit of the characteristic. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [name\_space](#a1dfbb9fc1e1397d2abec04b216d7ae33) |
|  | Name space of the description. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [description](#a3c48dd5ea717fbaf510d13c64a370c06) |
|  | Description of the characteristic as defined in a higher layer profile. |

## Detailed Description

GATT Characteristic Presentation Format Attribute Value.

## Field Documentation

## [◆ ](#a3c48dd5ea717fbaf510d13c64a370c06)description

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_cpf::description |
| --- |

Description of the characteristic as defined in a higher layer profile.

## [◆ ](#a3690a86c942badb2d2698481b03e436d)exponent

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_gatt\_cpf::exponent |
| --- |

Exponent field to determine how the value of this characteristic is further formatted.

## [◆ ](#ab0ca135a75130b3ffc0c5bf375f3528f)format

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_gatt\_cpf::format |
| --- |

Format of the value of the characteristic.

## [◆ ](#a1dfbb9fc1e1397d2abec04b216d7ae33)name\_space

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_gatt\_cpf::name\_space |
| --- |

Name space of the description.

## [◆ ](#a2a9f3d3f72b9acb1ef7f2dc765e5a231)unit

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_cpf::unit |
| --- |

Unit of the characteristic.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_cpf](structbt__gatt__cpf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
