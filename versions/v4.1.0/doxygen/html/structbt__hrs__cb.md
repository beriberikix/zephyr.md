---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hrs__cb.html
original_path: doxygen/html/structbt__hrs__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hrs\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Heart Rate Service (HRS)](group__bt__hrs.md)

Heart rate service callback structure.
[More...](#details)

`#include <[hrs.h](hrs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [ntf\_changed](#a7374b6196a258e874628c703b2e5ad35) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Heart rate notifications changed. |
| int(\* | [ctrl\_point\_write](#ade0afff87b9ba420f5bfacd73a947dc4) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request) |
|  | Heart rate control point write callback. |

## Detailed Description

Heart rate service callback structure.

## Field Documentation

## [◆ ](#ade0afff87b9ba420f5bfacd73a947dc4)ctrl\_point\_write

| int(\* bt\_hrs\_cb::ctrl\_point\_write) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request) |
| --- |

Heart rate control point write callback.

Note
:   if Server supports the Energy Expended feature then application shall implement and support [BT\_HRS\_CONTROL\_POINT\_RESET\_ENERGY\_EXPANDED\_REQ](group__bt__hrs.md#ga4ff20fff68b19602a8857d29f8dd822d "BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ") request code

Parameters
:   | request | control point request code |
    | --- | --- |

Returns
:   0 on successful handling of control point request
:   -ENOTSUP if not supported. It can be used to pass handling to other listeners in case of multiple listeners
:   other negative error codes will result in immediate error response

## [◆ ](#a7374b6196a258e874628c703b2e5ad35)ntf\_changed

| void(\* bt\_hrs\_cb::ntf\_changed) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
| --- |

Heart rate notifications changed.

Parameters
:   | enabled | Flag that is true if notifications were enabled, false if they were disabled. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[hrs.h](hrs_8h_source.md)

- [bt\_hrs\_cb](structbt__hrs__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
