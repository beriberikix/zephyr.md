---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__scan__cb.html
original_path: doxygen/html/structbt__le__scan__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_scan\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Listener context for (LE) scanning.
[More...](#details)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [recv](#a71d73c1da28d4a27626f77d96a5b3541) )(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Advertisement packet and scan response received callback. |
| void(\* | [timeout](#a2f57f3fee46bd137065f4c57d0cd5157) )(void) |
|  | The scanner has stopped scanning after scan timeout. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a50dbc5e7618fd488e9acb7ad8f104a63) |

## Detailed Description

Listener context for (LE) scanning.

## Field Documentation

## [◆ ](#a50dbc5e7618fd488e9acb7ad8f104a63)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_le\_scan\_cb::node |
| --- |

## [◆ ](#a71d73c1da28d4a27626f77d96a5b3541)recv

| void(\* bt\_le\_scan\_cb::recv) (const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Advertisement packet and scan response received callback.

Parameters
:   | info | Advertiser packet and scan response information. |
    | --- | --- |
    | buf | Buffer containing advertiser data. |

## [◆ ](#a2f57f3fee46bd137065f4c57d0cd5157)timeout

| void(\* bt\_le\_scan\_cb::timeout) (void) |
| --- |

The scanner has stopped scanning after scan timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_scan\_cb](structbt__le__scan__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
