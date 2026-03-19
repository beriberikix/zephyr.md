---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__ias__client__cb.html
original_path: doxygen/html/structbt__ias__client__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ias\_client\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Immediate Alert Service (IAS)](group__bt__ias.md)

`#include <[ias.h](ias_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discover](#a325ad34a67f9d9948740eb87862945b7) )(struct bt\_conn \*conn, int err) |
|  | Callback function for bt\_ias\_discover. |

## Field Documentation

## [◆ ](#a325ad34a67f9d9948740eb87862945b7)discover

| void(\* bt\_ias\_client\_cb::discover) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for bt\_ias\_discover.

This callback is called when discovery procedure is complete.

Parameters
:   | conn | Bluetooth connection object. |
    | --- | --- |
    | err | 0 on success, ATT error or negative errno otherwise |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ias.h](ias_8h_source.md)

- [bt\_ias\_client\_cb](structbt__ias__client__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
