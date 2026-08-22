---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__ext__adv__scanned__info.html
original_path: doxygen/html/structbt__le__ext__adv__scanned__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_scanned\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Info of the advertising scanned event.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a4431f157891d2c1a7d0e40f7e879ac3d) |
|  | Active scanner LE address and type. |

## Detailed Description

Info of the advertising scanned event.

Note
:   Used in [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md "bt_le_ext_adv_cb").

## Field Documentation

## [◆ ](#a4431f157891d2c1a7d0e40f7e879ac3d)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_ext\_adv\_scanned\_info::addr |
| --- |

Active scanner LE address and type.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
