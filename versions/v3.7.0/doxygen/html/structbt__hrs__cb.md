---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__hrs__cb.html
original_path: doxygen/html/structbt__hrs__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

## Detailed Description

Heart rate service callback structure.

## Field Documentation

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
