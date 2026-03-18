---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__gatt__write__params.html
original_path: doxygen/html/structbt__gatt__write__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_write\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Client APIs](group__bt__gatt__client.md)

GATT Write parameters.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50) | [func](#a3468e3b75f3f9eda12bc4963f48cf9aa) |
|  | Response callback. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#a384c5c15f248df5b327423ca32637bad) |
|  | Attribute handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [offset](#add53cc08465d28f33bc48a1e8649ac1a) |
|  | Attribute data offset. |
| const void \* | [data](#ab6510ef242e73325adb074322746c27c) |
|  | Data to be written. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [length](#aded956dac2d398b642faeec81fdb9ec3) |
|  | Length of the data. |
| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) | [chan\_opt](#ad79905c16f7ba5289817de552ece1a48) |

## Detailed Description

GATT Write parameters.

## Field Documentation

## [◆ ](#ad79905c16f7ba5289817de552ece1a48)chan\_opt

| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) bt\_gatt\_write\_params::chan\_opt |
| --- |

## [◆ ](#ab6510ef242e73325adb074322746c27c)data

| const void\* bt\_gatt\_write\_params::data |
| --- |

Data to be written.

## [◆ ](#a3468e3b75f3f9eda12bc4963f48cf9aa)func

| [bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50) bt\_gatt\_write\_params::func |
| --- |

Response callback.

## [◆ ](#a384c5c15f248df5b327423ca32637bad)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_write\_params::handle |
| --- |

Attribute handle.

## [◆ ](#aded956dac2d398b642faeec81fdb9ec3)length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_write\_params::length |
| --- |

Length of the data.

## [◆ ](#add53cc08465d28f33bc48a1e8649ac1a)offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_write\_params::offset |
| --- |

Attribute data offset.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_write\_params](structbt__gatt__write__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
