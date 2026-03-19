---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__tmap.html
original_path: doxygen/html/group__bt__tmap.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

| Macros | |
| --- | --- |
| #define | [BT\_TMAP\_CG\_SUPPORTED](#ga4415bbd383d428c9cc316fd0a5a79733) |
|  | Call Gateway (CG) supported. |
| #define | [BT\_TMAP\_CT\_SUPPORTED](#gaadaddbccf51b9e7ad78962c1a5d05488) |
|  | Call Terminal (CT) supported. |
| #define | [BT\_TMAP\_UMS\_SUPPORTED](#ga83b5ebc64ad7028a14276a8d6fa51a6a) |
|  | Unicast Media Sender (UMS) supported. |
| #define | [BT\_TMAP\_UMR\_SUPPORTED](#ga197b2f5c0c894c2a7d82f415a5a59a47) |
|  | Unicast Media Receiver (UMR) supported. |
| #define | [BT\_TMAP\_BMS\_SUPPORTED](#ga00b55b590540c664e9371ca2d0477af8)   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE)) |
|  | Broadcast Media Sender (BMS) supported. |
| #define | [BT\_TMAP\_BMR\_SUPPORTED](#ga10e832a6c2cfefc4971d85f182141f3e)   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SINK)) |
|  | Broadcast Media Receiver (BMR) supported. |

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

## Macro Definition Documentation

## [◆ ](#ga10e832a6c2cfefc4971d85f182141f3e)BT\_TMAP\_BMR\_SUPPORTED

| #define BT\_TMAP\_BMR\_SUPPORTED   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SINK)) |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

Broadcast Media Receiver (BMR) supported.

## [◆ ](#ga00b55b590540c664e9371ca2d0477af8)BT\_TMAP\_BMS\_SUPPORTED

| #define BT\_TMAP\_BMS\_SUPPORTED   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE)) |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

Broadcast Media Sender (BMS) supported.

## [◆ ](#ga4415bbd383d428c9cc316fd0a5a79733)BT\_TMAP\_CG\_SUPPORTED

| #define BT\_TMAP\_CG\_SUPPORTED |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_UNICAST\_CLIENT) && \

IS\_ENABLED(CONFIG\_BT\_TBS) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_VCP\_VOL\_CTLR))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

Call Gateway (CG) supported.

## [◆ ](#gaadaddbccf51b9e7ad78962c1a5d05488)BT\_TMAP\_CT\_SUPPORTED

| #define BT\_TMAP\_CT\_SUPPORTED |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_UNICAST\_SERVER) && \

IS\_ENABLED(CONFIG\_BT\_TBS\_CLIENT) && \

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_ASCS\_ASE\_SNK) && \

IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_REND) == [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_ASCS\_ASE\_SNK)))

Call Terminal (CT) supported.

## [◆ ](#ga197b2f5c0c894c2a7d82f415a5a59a47)BT\_TMAP\_UMR\_SUPPORTED

| #define BT\_TMAP\_UMR\_SUPPORTED |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_ASCS\_ASE\_SNK) && \

IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_REND))

Unicast Media Receiver (UMR) supported.

## [◆ ](#ga83b5ebc64ad7028a14276a8d6fa51a6a)BT\_TMAP\_UMS\_SUPPORTED

| #define BT\_TMAP\_UMS\_SUPPORTED |
| --- |

`#include <[tmap.h](tmap_8h.md)>`

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && \

IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST\_CLIENT\_ASE\_SNK) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_VCP\_VOL\_CTLR) && \

IS\_ENABLED(CONFIG\_BT\_MCS))

Unicast Media Sender (UMS) supported.

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
