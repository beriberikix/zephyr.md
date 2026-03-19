---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__has__preset__ops.html
original_path: doxygen/html/structbt__has__preset__ops.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_has\_preset\_ops Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hearing Access Service (HAS)](group__bt__has.md)

Preset operations structure.
[More...](#details)

`#include <[has.h](has_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [select](#aec9d0f01c03f02f0a6f124527b72235e) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Preset select callback. |
| void(\* | [name\_changed](#a7f0069639eb3b1f8b0d290a752b68770) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, const char \*name) |
|  | Preset name changed callback. |

## Detailed Description

Preset operations structure.

## Field Documentation

## [◆ ](#a7f0069639eb3b1f8b0d290a752b68770)name\_changed

| void(\* bt\_has\_preset\_ops::name\_changed) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, const char \*name) |
| --- |

Preset name changed callback.

This callback is called when the name of the preset identified by `index` has changed.

Parameters
:   | index | Preset index that name has been changed. |
    | --- | --- |
    | name | Preset current name. |

## [◆ ](#aec9d0f01c03f02f0a6f124527b72235e)select

| int(\* bt\_has\_preset\_ops::select) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
| --- |

Preset select callback.

This callback is called when the client requests to select preset identified by `index`.

Parameters
:   | index | Preset index requested to activate. |
    | --- | --- |
    | sync | Whether the server must relay this change to the other member of the Binaural Hearing Aid Set. |

Returns
:   0 in case of success or negative value in case of error.
:   -EBUSY if operation cannot be performed at the time.
:   -EINPROGRESS in case where user has to confirm once the requested preset becomes active by calling [bt\_has\_preset\_active\_set](group__bt__has.md#ga2c0fe62baa63b72703d6f553f1de072b "bt_has_preset_active_set").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[has.h](has_8h_source.md)

- [bt\_has\_preset\_ops](structbt__has__preset__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
