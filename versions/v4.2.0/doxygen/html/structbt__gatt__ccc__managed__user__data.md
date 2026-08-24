---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__gatt__ccc__managed__user__data.html
original_path: doxygen/html/structbt__gatt__ccc__managed__user__data.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_ccc\_managed\_user\_data Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Server APIs](group__bt__gatt__server.md)

Internal representation of CCC value.
[More...](#details)

`#include <[zephyr/bluetooth/gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) | [cfg](#a44987dc5be9442436f6033c30bbb42fd) [0] |
|  | Configuration for each connection. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [value](#a883177671ea068f1dcbab36197abfdfd) |
|  | Highest value of all connected peer's subscriptions. |
| void(\* | [cfg\_changed](#a166073fca5a342b859fb42482547b80c) )(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](#a883177671ea068f1dcbab36197abfdfd)) |
|  | CCC attribute changed callback. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [cfg\_write](#a7ba4c03ef2a0c2c85e17ef1147934536) )(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](#a883177671ea068f1dcbab36197abfdfd)) |
|  | CCC attribute write validation callback. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [cfg\_match](#afc0c5226be7d9b2d3d039f86960a2ed3) )(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | CCC attribute match handler. |

## Detailed Description

Internal representation of CCC value.

Note
:   Only use this as an argument for [BT\_GATT\_CCC\_MANAGED](group__bt__gatt__server.md#gad8b296ecfd1139680f21da7904b9f585 "BT_GATT_CCC_MANAGED")

## Field Documentation

## [◆ ](#a44987dc5be9442436f6033c30bbb42fd)cfg

| struct [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) bt\_gatt\_ccc\_managed\_user\_data::cfg[0] |
| --- |

Configuration for each connection.

## [◆ ](#a166073fca5a342b859fb42482547b80c)cfg\_changed

| void(\* bt\_gatt\_ccc\_managed\_user\_data::cfg\_changed) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](#a883177671ea068f1dcbab36197abfdfd)) |
| --- |

CCC attribute changed callback.

Parameters
:   | attr | The attribute that's changed value |
    | --- | --- |
    | [value](#a883177671ea068f1dcbab36197abfdfd) | New value |

## [◆ ](#afc0c5226be7d9b2d3d039f86960a2ed3)cfg\_match

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_gatt\_ccc\_managed\_user\_data::cfg\_match) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
| --- |

CCC attribute match handler.

Indicate if it is OK to send a notification or indication to the subscriber.

Parameters
:   | conn | The connection that is being checked |
    | --- | --- |
    | attr | The attribute that's being checked |

Returns
:   true if application has approved notification/indication, false if application does not approve.

## [◆ ](#a7ba4c03ef2a0c2c85e17ef1147934536)cfg\_write

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* bt\_gatt\_ccc\_managed\_user\_data::cfg\_write) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [value](#a883177671ea068f1dcbab36197abfdfd)) |
| --- |

CCC attribute write validation callback.

Parameters
:   | conn | The connection that is requesting to write |
    | --- | --- |
    | attr | The attribute that's being written |
    | [value](#a883177671ea068f1dcbab36197abfdfd) | CCC value to write |

Returns
:   Number of bytes to write, or in case of an error [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific error code.

## [◆ ](#a883177671ea068f1dcbab36197abfdfd)value

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_ccc\_managed\_user\_data::value |
| --- |

Highest value of all connected peer's subscriptions.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_ccc\_managed\_user\_data](structbt__gatt__ccc__managed__user__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
