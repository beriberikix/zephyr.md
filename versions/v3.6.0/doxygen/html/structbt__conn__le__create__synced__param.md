---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__conn__le__create__synced__param.html
original_path: doxygen/html/structbt__conn__le__create__synced__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_create\_synced\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [peer](#ac5872dda4042e3ba6c161dce60784b70) |
|  | Remote address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent](#ac7b4e4144aaf914bdef1dc305b5e297f) |
|  | The subevent where the connection will be initiated. |

## Field Documentation

## [◆ ](#ac5872dda4042e3ba6c161dce60784b70)peer

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_conn\_le\_create\_synced\_param::peer |
| --- |

Remote address.

The peer must be synchronized to the PAwR train.

## [◆ ](#ac7b4e4144aaf914bdef1dc305b5e297f)subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_create\_synced\_param::subevent |
| --- |

The subevent where the connection will be initiated.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
