---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__send__cb.html
original_path: doxygen/html/structbt__mesh__send__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_send\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Callback structure for monitoring model message sending.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [start](#a2f84ef4cb2d28729cd98b844a3d25f55) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration, int err, void \*cb\_data) |
|  | Handler called at the start of the transmission. |
| void(\* | [end](#aa169dbec8c96fd41a35616c009604685) )(int err, void \*cb\_data) |
|  | Handler called at the end of the transmission. |

## Detailed Description

Callback structure for monitoring model message sending.

## Field Documentation

## [◆ ](#aa169dbec8c96fd41a35616c009604685)end

| void(\* bt\_mesh\_send\_cb::end) (int err, void \*cb\_data) |
| --- |

Handler called at the end of the transmission.

Parameters
:   | err | Error occurring during sending. |
    | --- | --- |
    | cb\_data | Callback data, as passed to the send API. |

## [◆ ](#a2f84ef4cb2d28729cd98b844a3d25f55)start

| void(\* bt\_mesh\_send\_cb::start) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration, int err, void \*cb\_data) |
| --- |

Handler called at the start of the transmission.

Parameters
:   | duration | The duration of the full transmission. |
    | --- | --- |
    | err | Error occurring during sending. |
    | cb\_data | Callback data, as passed to the send API. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
