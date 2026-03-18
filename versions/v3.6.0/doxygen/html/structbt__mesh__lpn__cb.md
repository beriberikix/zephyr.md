---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__lpn__cb.html
original_path: doxygen/html/structbt__mesh__lpn__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_lpn\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Low Power Node callback functions.
[More...](#details)

`#include <[main.h](main_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [established](#a74b8b398b383518af069266cf3b0be91) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) queue\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_window) |
|  | Friendship established. |
| void(\* | [terminated](#af2e2f5043503c62926f96a5fcb48890c) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr) |
|  | Friendship terminated. |
| void(\* | [polled](#a9805ad8578faec5b371d6f39178332ef) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) retry) |
|  | Local Poll Request. |

## Detailed Description

Low Power Node callback functions.

## Field Documentation

## [◆ ](#a74b8b398b383518af069266cf3b0be91)established

| void(\* bt\_mesh\_lpn\_cb::established) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) queue\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_window) |
| --- |

Friendship established.

This callback notifies the application that friendship has been successfully established.

Parameters
:   | net\_idx | NetKeyIndex used during friendship establishment. |
    | --- | --- |
    | friend\_addr | Friend address. |
    | queue\_size | Friend queue size. |
    | recv\_window | Low Power Node's listens duration for Friend response. |

## [◆ ](#a9805ad8578faec5b371d6f39178332ef)polled

| void(\* bt\_mesh\_lpn\_cb::polled) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) retry) |
| --- |

Local Poll Request.

This callback notifies the application that the local node has polled the friend node.

This callback will be called before [bt\_mesh\_lpn\_cb::established](#a74b8b398b383518af069266cf3b0be91) when attempting to establish a friendship.

Parameters
:   | net\_idx | NetKeyIndex used during friendship establishment. |
    | --- | --- |
    | friend\_addr | Friend address. |
    | retry | Retry or first poll request for each transaction. |

## [◆ ](#af2e2f5043503c62926f96a5fcb48890c)terminated

| void(\* bt\_mesh\_lpn\_cb::terminated) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) friend\_addr) |
| --- |

Friendship terminated.

This callback notifies the application that friendship has been terminated.

Parameters
:   | net\_idx | NetKeyIndex used during friendship establishment. |
    | --- | --- |
    | friend\_addr | Friend address. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[main.h](main_8h_source.md)

- [bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
