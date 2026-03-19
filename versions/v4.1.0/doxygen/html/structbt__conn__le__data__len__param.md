---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__le__data__len__param.html
original_path: doxygen/html/structbt__conn__le__data__len__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_data\_len\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Connection data length parameters for LE connections.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_max\_len](#a8b279a0dc72c70aaf5205558fd4b4c4a) |
|  | Maximum Link Layer transmission payload size in bytes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_max\_time](#a9046542952fa822b944602b398562e6e) |
|  | Maximum Link Layer transmission payload time in us. |

## Detailed Description

Connection data length parameters for LE connections.

## Field Documentation

## [◆ ](#a8b279a0dc72c70aaf5205558fd4b4c4a)tx\_max\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_data\_len\_param::tx\_max\_len |
| --- |

Maximum Link Layer transmission payload size in bytes.

## [◆ ](#a9046542952fa822b944602b398562e6e)tx\_max\_time

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_data\_len\_param::tx\_max\_time |
| --- |

Maximum Link Layer transmission payload time in us.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
