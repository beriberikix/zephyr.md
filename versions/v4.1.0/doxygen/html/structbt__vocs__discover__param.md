---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__vocs__discover__param.html
original_path: doxygen/html/structbt__vocs__discover__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vocs\_discover\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Offset Control Service (VOCS)](group__bt__vocs.md)

Structure for discovering a Volume Offset Control Service instance.
[More...](#details)

`#include <[vocs.h](vocs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_handle](#aca830a50436def0f422d05eba34273ed) |
|  | The start handle of the discovering. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [end\_handle](#a3811da3035bb1f0ff5d290eb60fb2fda) |
|  | The end handle of the discovering. |

## Detailed Description

Structure for discovering a Volume Offset Control Service instance.

## Field Documentation

## [◆ ](#a3811da3035bb1f0ff5d290eb60fb2fda)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_vocs\_discover\_param::end\_handle |
| --- |

The end handle of the discovering.

Typically the `end_handle` of a [bt\_gatt\_include](structbt__gatt__include.md "bt_gatt_include").

## [◆ ](#aca830a50436def0f422d05eba34273ed)start\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_vocs\_discover\_param::start\_handle |
| --- |

The start handle of the discovering.

Typically the `start_handle` of a [bt\_gatt\_include](structbt__gatt__include.md "bt_gatt_include").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vocs.h](vocs_8h_source.md)

- [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
