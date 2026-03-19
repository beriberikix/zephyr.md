---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__tmap.html
original_path: doxygen/html/group__bt__tmap.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Telephone and Media Audio Profile (TMAP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Telephone and Media Audio Profile (TMAP).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_tmap\_cb](structbt__tmap__cb.md) |
|  | TMAP callback structure. [More...](structbt__tmap__cb.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_tmap\_role](#ga4ef8a550bb374a5f257860082e1411d4) {     [BT\_TMAP\_ROLE\_CG](#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6) = BIT(0) , [BT\_TMAP\_ROLE\_CT](#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d) = BIT(1) , [BT\_TMAP\_ROLE\_UMS](#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501) = BIT(2) , [BT\_TMAP\_ROLE\_UMR](#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22) = BIT(3) ,     [BT\_TMAP\_ROLE\_BMS](#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308) = BIT(4) , [BT\_TMAP\_ROLE\_BMR](#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8) = BIT(5)   } |
|  | TMAP Role characteristic. [More...](#ga4ef8a550bb374a5f257860082e1411d4) |

| Functions | |
| --- | --- |
| int | [bt\_tmap\_register](#ga2c93d1bce7db000cef76c42e5cab48cb) (enum [bt\_tmap\_role](#ga4ef8a550bb374a5f257860082e1411d4) role) |
|  | Adds TMAS instance to database and sets the received TMAP role(s). |
| int | [bt\_tmap\_discover](#gacb52c3e4c56f6b042398ac992628d521) (struct bt\_conn \*conn, const struct [bt\_tmap\_cb](structbt__tmap__cb.md) \*tmap\_cb) |
|  | Perform service discovery as TMAP Client. |
| void | [bt\_tmap\_set\_role](#ga0b51b305d5a5d87df9f4082951bd28a5) (enum [bt\_tmap\_role](#ga4ef8a550bb374a5f257860082e1411d4) role) |
|  | Set one or multiple TMAP roles dynamically. |

## Detailed Description

Telephone and Media Audio Profile (TMAP).

Since
:   3.4

Version
:   0.8.0

The Telephone and Media Audio Profile (TMAP) uses a collection of Bluetooth features and profiles to enable interoperability between devices for telephony and media audio.

## Enumeration Type Documentation

## [◆ ](#ga4ef8a550bb374a5f257860082e1411d4)bt\_tmap\_role

| enum [bt\_tmap\_role](#ga4ef8a550bb374a5f257860082e1411d4) |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

TMAP Role characteristic.

| Enumerator | |
| --- | --- |
| BT\_TMAP\_ROLE\_CG | TMAP Call Gateway role.  This role is defined to telephone and VoIP applications using the Call Control Profile to control calls on a remote TMAP Call Terminal. Audio streams in this role are typically bi-directional. |
| BT\_TMAP\_ROLE\_CT | TMAP Call Terminal role.  This role is defined to telephone and VoIP applications using the Call Control Profile to expose calls to remote TMAP Call Gateways. Audio streams in this role are typically bi-directional. |
| BT\_TMAP\_ROLE\_UMS | TMAP Unicast Media Sender role.  This role is defined send media audio to TMAP Unicast Media Receivers. Audio streams in this role are typically uni-directional. |
| BT\_TMAP\_ROLE\_UMR | TMAP Unicast Media Receiver role.  This role is defined receive media audio to TMAP Unicast Media Senders. Audio streams in this role are typically uni-directional. |
| BT\_TMAP\_ROLE\_BMS | TMAP Broadcast Media Sender role.  This role is defined send media audio to TMAP Broadcast Media Receivers. Audio streams in this role are always uni-directional. |
| BT\_TMAP\_ROLE\_BMR | TMAP Broadcast Media Receiver role.  This role is defined send media audio to TMAP Broadcast Media Senders. Audio streams in this role are always uni-directional. |

## Function Documentation

## [◆ ](#gacb52c3e4c56f6b042398ac992628d521)bt\_tmap\_discover()

| int bt\_tmap\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_tmap\_cb](structbt__tmap__cb.md) \* | *tmap\_cb* ) |

`#include <[tmap.h](tmap_8h.md)>`

Perform service discovery as TMAP Client.

Parameters
:   | conn | Pointer to the connection. |
    | --- | --- |
    | tmap\_cb | Pointer to struct of TMAP callbacks. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga2c93d1bce7db000cef76c42e5cab48cb)bt\_tmap\_register()

| int bt\_tmap\_register | ( | enum [bt\_tmap\_role](#ga4ef8a550bb374a5f257860082e1411d4) | *role* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tmap.h](tmap_8h.md)>`

Adds TMAS instance to database and sets the received TMAP role(s).

Parameters
:   | role | TMAP role(s) of the device (one or multiple). |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga0b51b305d5a5d87df9f4082951bd28a5)bt\_tmap\_set\_role()

| void bt\_tmap\_set\_role | ( | enum [bt\_tmap\_role](#ga4ef8a550bb374a5f257860082e1411d4) | *role* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tmap.h](tmap_8h.md)>`

Set one or multiple TMAP roles dynamically.

Previously registered value will be overwritten.

Parameters
:   | role | TMAP role(s). |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
