---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__sync__state__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__state__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_state\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Information about the state of periodic advertising sync.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [recv\_enabled](#a4b0a3b7e36f935e06072304d6b92579f) |
|  | True if receiving periodic advertisements, false otherwise. |

## Detailed Description

Information about the state of periodic advertising sync.

This struct provides information about the current state of a periodic advertising sync. It indicates whether periodic advertising reception is enabled or not. It is typically used to report the state change via callbacks in the [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md "bt_le_per_adv_sync_cb") structure.

## Field Documentation

## [◆ ](#a4b0a3b7e36f935e06072304d6b92579f)recv\_enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_le\_per\_adv\_sync\_state\_info::recv\_enabled |
| --- |

True if receiving periodic advertisements, false otherwise.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
