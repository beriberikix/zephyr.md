---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__blob__srv.html
original_path: doxygen/html/structbt__mesh__blob__srv.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_srv Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Server model API](group__bt__mesh__blob__srv.md)

BLOB Transfer Server model instance.
[More...](#details)

`#include <[blob_srv.h](blob__srv_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md) |

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) \* | [cb](#a65d08187dce1ed86cbfbb4f977cd32df) |
|  | Event handler callbacks. |
| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \* | [io](#a23d12a803a2414aa1460ea9a862cc78b) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [rx\_timeout](#a82a5c7fc2ad37e531ec10bada27bf10a) |
| struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) | [block](#a8d6a01849e95c4a26d3270f4320c214f) |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#a1066d309b56748223183d39e8fc7fd82) |
| enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) | [phase](#a75b8ecd846fcf96708d31fb5efb0bea1) |
| struct [bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md) | [state](#a86ed657bc97fc3c299e6fca6cdaee4e4) |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [chunk\_idx](#aa3ac872db59f2f1cd67d25e97020d484) |  |
| struct [k\_work\_delayable](structk__work__delayable.md)   [report](#aad6ef41a187cc5489d6a8d5f4a5b3003) |  |
| } | [pull](#afec2237da95cc7ffbbdeb99d8ffb12b6) |

## Detailed Description

BLOB Transfer Server model instance.

## Field Documentation

## [◆ ](#a8d6a01849e95c4a26d3270f4320c214f)block

| struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) bt\_mesh\_blob\_srv::block |
| --- |

## [◆ ](#a65d08187dce1ed86cbfbb4f977cd32df)cb

| const struct [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md)\* bt\_mesh\_blob\_srv::cb |
| --- |

Event handler callbacks.

## [◆ ](#aa3ac872db59f2f1cd67d25e97020d484)chunk\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_srv::chunk\_idx |
| --- |

## [◆ ](#a23d12a803a2414aa1460ea9a862cc78b)io

| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)\* bt\_mesh\_blob\_srv::io |
| --- |

## [◆ ](#a1066d309b56748223183d39e8fc7fd82)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_blob\_srv::mod |
| --- |

## [◆ ](#a75b8ecd846fcf96708d31fb5efb0bea1)phase

| enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) bt\_mesh\_blob\_srv::phase |
| --- |

## [◆ ](#afec2237da95cc7ffbbdeb99d8ffb12b6)[struct]

| struct { ... } bt\_mesh\_blob\_srv::pull |
| --- |

## [◆ ](#aad6ef41a187cc5489d6a8d5f4a5b3003)report

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_blob\_srv::report |
| --- |

## [◆ ](#a82a5c7fc2ad37e531ec10bada27bf10a)rx\_timeout

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_blob\_srv::rx\_timeout |
| --- |

## [◆ ](#a86ed657bc97fc3c299e6fca6cdaee4e4)state

| struct [bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md) bt\_mesh\_blob\_srv::state |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_srv.h](blob__srv_8h_source.md)

- [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
