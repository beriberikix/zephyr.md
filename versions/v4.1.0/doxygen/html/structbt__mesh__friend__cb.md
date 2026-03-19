---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__friend__cb.html
original_path: doxygen/html/structbt__mesh__friend__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_friend\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Friend Node callback functions.
[More...](#details)

`#include <[main.h](main_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [established](#a824ed814a46a3954d2c6f669c8900156) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_delay, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) polltimeout) |
|  | Friendship established. |
| void(\* | [terminated](#a1c0d570eb1b857c65b3b5b4ce31999d6) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr) |
|  | Friendship terminated. |
| void(\* | [polled](#a7b904967d89173f82ac26216e3849d23) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr) |
|  | Friend Poll Request. |

## Detailed Description

Friend Node callback functions.

## Field Documentation

## [◆ ](#a824ed814a46a3954d2c6f669c8900156)established

| void(\* bt\_mesh\_friend\_cb::established) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_delay, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) polltimeout) |
| --- |

Friendship established.

This callback notifies the application that friendship has been successfully established.

Parameters
:   | net\_idx | NetKeyIndex used during friendship establishment. |
    | --- | --- |
    | lpn\_addr | Low Power Node address. |
    | recv\_delay | Receive Delay in units of 1 millisecond. |
    | polltimeout | PollTimeout in units of 1 millisecond. |

## [◆ ](#a7b904967d89173f82ac26216e3849d23)polled

| void(\* bt\_mesh\_friend\_cb::polled) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr) |
| --- |

Friend Poll Request.

This callback notifies the application that the low power node has polled the friend node.

This callback will be called before [bt\_mesh\_friend\_cb::established](#a824ed814a46a3954d2c6f669c8900156) when attempting to establish a friendship.

Parameters
:   | net\_idx | NetKeyIndex used during friendship establishment. |
    | --- | --- |
    | lpn\_addr | LPN address. |

## [◆ ](#a1c0d570eb1b857c65b3b5b4ce31999d6)terminated

| void(\* bt\_mesh\_friend\_cb::terminated) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr) |
| --- |

Friendship terminated.

This callback notifies the application that friendship has been terminated.

Parameters
:   | net\_idx | NetKeyIndex used during friendship establishment. |
    | --- | --- |
    | lpn\_addr | Low Power Node address. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[main.h](main_8h_source.md)

- [bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
