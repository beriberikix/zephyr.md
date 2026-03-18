---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__conn__le__data__len__info.html
original_path: doxygen/html/structbt__conn__le__data__len__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_data\_len\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Connection data length information for LE connections.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_max\_len](#a48d175f3c4b03dbdee129feae3edab23) |
|  | Maximum Link Layer transmission payload size in bytes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_max\_time](#a14288429cbbcce2ef34580a581815eb7) |
|  | Maximum Link Layer transmission payload time in us. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_max\_len](#a18ddc603e922586e331187c9b29f2908) |
|  | Maximum Link Layer reception payload size in bytes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_max\_time](#af2316cdc921e9ec19491501e15248f73) |
|  | Maximum Link Layer reception payload time in us. |

## Detailed Description

Connection data length information for LE connections.

## Field Documentation

## [◆ ](#a18ddc603e922586e331187c9b29f2908)rx\_max\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_data\_len\_info::rx\_max\_len |
| --- |

Maximum Link Layer reception payload size in bytes.

## [◆ ](#af2316cdc921e9ec19491501e15248f73)rx\_max\_time

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_data\_len\_info::rx\_max\_time |
| --- |

Maximum Link Layer reception payload time in us.

## [◆ ](#a48d175f3c4b03dbdee129feae3edab23)tx\_max\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_data\_len\_info::tx\_max\_len |
| --- |

Maximum Link Layer transmission payload size in bytes.

## [◆ ](#a14288429cbbcce2ef34580a581815eb7)tx\_max\_time

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_data\_len\_info::tx\_max\_time |
| --- |

Maximum Link Layer transmission payload time in us.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
