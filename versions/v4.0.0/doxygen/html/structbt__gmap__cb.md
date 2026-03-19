---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__gmap__cb.html
original_path: doxygen/html/structbt__gmap__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gmap\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Gaming Audio Profile](group__bt__gmap.md)

Hearing Access Service Client callback structure.
[More...](#details)

`#include <[gmap.h](gmap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discover](#a72c25ae277e04d419f41733d0b11aefc) )(struct bt\_conn \*conn, int err, enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features) |
|  | Callback function for bt\_has\_discover. |

## Detailed Description

Hearing Access Service Client callback structure.

## Field Documentation

## [◆ ](#a72c25ae277e04d419f41733d0b11aefc)discover

| void(\* bt\_gmap\_cb::discover) (struct bt\_conn \*conn, int err, enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features) |
| --- |

Callback function for bt\_has\_discover.

This callback is called when discovery procedure is complete.

Parameters
:   | conn | Bluetooth connection object. |
    | --- | --- |
    | err | 0 on success, ATT error or negative errno otherwise. |
    | role | Role of remote device. 0 on failure. |
    | features | Remote features. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[gmap.h](gmap_8h_source.md)

- [bt\_gmap\_cb](structbt__gmap__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
