---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tmap_8h.html
original_path: doxygen/html/tmap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmap.h File Reference

Header for Bluetooth TMAP.
[More...](#details)

`#include <zephyr/autoconf.h>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](tmap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_tmap\_cb](structbt__tmap__cb.md) |
|  | TMAP callback structure. [More...](structbt__tmap__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_TMAP\_CG\_SUPPORTED](#a4415bbd383d428c9cc316fd0a5a79733) |
|  | Call Gateway (CG) supported. |
| #define | [BT\_TMAP\_CT\_SUPPORTED](#aadaddbccf51b9e7ad78962c1a5d05488) |
|  | Call Terminal (CT) supported. |
| #define | [BT\_TMAP\_UMS\_SUPPORTED](#a83b5ebc64ad7028a14276a8d6fa51a6a) |
|  | Unicast Media Sender (UMS) supported. |
| #define | [BT\_TMAP\_UMR\_SUPPORTED](#a197b2f5c0c894c2a7d82f415a5a59a47) |
|  | Unicast Media Receiver (UMR) supported. |
| #define | [BT\_TMAP\_BMS\_SUPPORTED](#a00b55b590540c664e9371ca2d0477af8)   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE)) |
|  | Broadcast Media Sender (BMS) supported. |
| #define | [BT\_TMAP\_BMR\_SUPPORTED](#a10e832a6c2cfefc4971d85f182141f3e)   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SINK)) |
|  | Broadcast Media Receiver (BMR) supported. |

| Enumerations | |
| --- | --- |
| enum | [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) {     [BT\_TMAP\_ROLE\_CG](#a4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6) = BIT(0) , [BT\_TMAP\_ROLE\_CT](#a4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d) = BIT(1) , [BT\_TMAP\_ROLE\_UMS](#a4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501) = BIT(2) , [BT\_TMAP\_ROLE\_UMR](#a4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22) = BIT(3) ,     [BT\_TMAP\_ROLE\_BMS](#a4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308) = BIT(4) , [BT\_TMAP\_ROLE\_BMR](#a4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8) = BIT(5)   } |
|  | TMAP Role characteristic. [More...](#a4ef8a550bb374a5f257860082e1411d4) |

| Functions | |
| --- | --- |
| int | [bt\_tmap\_register](#a2c93d1bce7db000cef76c42e5cab48cb) (enum [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) role) |
|  | Adds TMAS instance to database and sets the received TMAP role(s). |
| int | [bt\_tmap\_discover](#acb52c3e4c56f6b042398ac992628d521) (struct bt\_conn \*conn, const struct [bt\_tmap\_cb](structbt__tmap__cb.md) \*tmap\_cb) |
|  | Perform service discovery as TMAP Client. |
| void | [bt\_tmap\_set\_role](#a0b51b305d5a5d87df9f4082951bd28a5) (enum [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) role) |
|  | Set one or multiple TMAP roles dynamically. |

## Detailed Description

Header for Bluetooth TMAP.

Copyright 2023 NXP Copyright (c) 2024 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

## Macro Definition Documentation

## [◆ ](#a10e832a6c2cfefc4971d85f182141f3e)BT\_TMAP\_BMR\_SUPPORTED

| #define BT\_TMAP\_BMR\_SUPPORTED   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SINK)) |
| --- |

Broadcast Media Receiver (BMR) supported.

## [◆ ](#a00b55b590540c664e9371ca2d0477af8)BT\_TMAP\_BMS\_SUPPORTED

| #define BT\_TMAP\_BMS\_SUPPORTED   ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE)) |
| --- |

Broadcast Media Sender (BMS) supported.

## [◆ ](#a4415bbd383d428c9cc316fd0a5a79733)BT\_TMAP\_CG\_SUPPORTED

| #define BT\_TMAP\_CG\_SUPPORTED |
| --- |

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_UNICAST\_CLIENT) && \

IS\_ENABLED(CONFIG\_BT\_TBS) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_VCP\_VOL\_CTLR))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Call Gateway (CG) supported.

## [◆ ](#aadaddbccf51b9e7ad78962c1a5d05488)BT\_TMAP\_CT\_SUPPORTED

| #define BT\_TMAP\_CT\_SUPPORTED |
| --- |

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_BAP\_UNICAST\_SERVER) && \

IS\_ENABLED(CONFIG\_BT\_TBS\_CLIENT) && \

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_ASCS\_ASE\_SNK) && \

IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_REND) == [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_ASCS\_ASE\_SNK)))

Call Terminal (CT) supported.

## [◆ ](#a197b2f5c0c894c2a7d82f415a5a59a47)BT\_TMAP\_UMR\_SUPPORTED

| #define BT\_TMAP\_UMR\_SUPPORTED |
| --- |

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_ACCEPTOR) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_ASCS\_ASE\_SNK) && \

IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_REND))

Unicast Media Receiver (UMR) supported.

## [◆ ](#a83b5ebc64ad7028a14276a8d6fa51a6a)BT\_TMAP\_UMS\_SUPPORTED

| #define BT\_TMAP\_UMS\_SUPPORTED |
| --- |

**Value:**

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_CAP\_INITIATOR) && \

IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST\_CLIENT\_ASE\_SNK) && [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BT\_VCP\_VOL\_CTLR) && \

IS\_ENABLED(CONFIG\_BT\_MCS))

Unicast Media Sender (UMS) supported.

## Enumeration Type Documentation

## [◆ ](#a4ef8a550bb374a5f257860082e1411d4)bt\_tmap\_role

| enum [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) |
| --- |

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

## [◆ ](#acb52c3e4c56f6b042398ac992628d521)bt\_tmap\_discover()

| int bt\_tmap\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_tmap\_cb](structbt__tmap__cb.md) \* | *tmap\_cb* ) |

Perform service discovery as TMAP Client.

Parameters
:   | conn | Pointer to the connection. |
    | --- | --- |
    | tmap\_cb | Pointer to struct of TMAP callbacks. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#a2c93d1bce7db000cef76c42e5cab48cb)bt\_tmap\_register()

| int bt\_tmap\_register | ( | enum [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) | *role* | ) |  |
| --- | --- | --- | --- | --- | --- |

Adds TMAS instance to database and sets the received TMAP role(s).

Parameters
:   | role | TMAP role(s) of the device (one or multiple). |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#a0b51b305d5a5d87df9f4082951bd28a5)bt\_tmap\_set\_role()

| void bt\_tmap\_set\_role | ( | enum [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) | *role* | ) |  |
| --- | --- | --- | --- | --- | --- |

Set one or multiple TMAP roles dynamically.

Previously registered value will be overwritten.

Parameters
:   | role | TMAP role(s). |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [tmap.h](tmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
