---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__nus__cb.html
original_path: doxygen/html/structbt__nus__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_nus\_cb Struct Reference

Callbacks for getting notified on NUS Service occurrences.
[More...](#details)

`#include <[nus.h](nus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [notif\_enabled](#a3fc8fcca9d16f18c506ad13d2356e32c) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled, void \*[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)) |
|  | Notifications subscription changed. |
| void(\* | [received](#ad95d3bb5f927c25058c4ec6a89c665a4) )(struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, void \*[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)) |
|  | Received Data. |
| void \* | [ctx](#ab28ef9120ed04be0c7dbdd5c76556864) |
|  | Internal member. |

## Detailed Description

Callbacks for getting notified on NUS Service occurrences.

## Field Documentation

## [◆ ](#ab28ef9120ed04be0c7dbdd5c76556864)ctx

| void\* bt\_nus\_cb::ctx |
| --- |

Internal member.

Provided as a callback argument for user context

## [◆ ](#a3fc8fcca9d16f18c506ad13d2356e32c)notif\_enabled

| void(\* bt\_nus\_cb::notif\_enabled) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled, void \*[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)) |
| --- |

Notifications subscription changed.

Parameters
:   | enabled | Flag that is true if notifications were enabled, false if they were disabled. |
    | --- | --- |
    | [ctx](#ab28ef9120ed04be0c7dbdd5c76556864) | User context provided in the callback structure. |

## [◆ ](#ad95d3bb5f927c25058c4ec6a89c665a4)received

| void(\* bt\_nus\_cb::received) (struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, void \*[ctx](#ab28ef9120ed04be0c7dbdd5c76556864)) |
| --- |

Received Data.

Parameters
:   | conn | Peer Connection object. |
    | --- | --- |
    | data | Pointer to buffer with data received. |
    | len | Size in bytes of data received. |
    | [ctx](#ab28ef9120ed04be0c7dbdd5c76556864) | User context provided in the callback structure. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[nus.h](nus_8h_source.md)

- [bt\_nus\_cb](structbt__nus__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
