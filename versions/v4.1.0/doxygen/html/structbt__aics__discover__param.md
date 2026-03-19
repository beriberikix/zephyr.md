---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__aics__discover__param.html
original_path: doxygen/html/structbt__aics__discover__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_aics\_discover\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Audio Input Control Service (AICS)](group__bt__aics.md)

Structure for discovering a Audio Input Control Service instance.
[More...](#details)

`#include <[aics.h](aics_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_handle](#ab867f7d2ae219df0c479cce72d68842f) |
|  | The start handle of the discovering. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [end\_handle](#ab2931e7c4a627e717d943b2907b264cb) |
|  | The end handle of the discovering. |

## Detailed Description

Structure for discovering a Audio Input Control Service instance.

## Field Documentation

## [◆ ](#ab2931e7c4a627e717d943b2907b264cb)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_aics\_discover\_param::end\_handle |
| --- |

The end handle of the discovering.

Typically the `end_handle` of a [bt\_gatt\_include](structbt__gatt__include.md "bt_gatt_include").

## [◆ ](#ab867f7d2ae219df0c479cce72d68842f)start\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_aics\_discover\_param::start\_handle |
| --- |

The start handle of the discovering.

Typically the `start_handle` of a [bt\_gatt\_include](structbt__gatt__include.md "bt_gatt_include").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[aics.h](aics_8h_source.md)

- [bt\_aics\_discover\_param](structbt__aics__discover__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
