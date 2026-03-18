---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tmap_8h.html
original_path: doxygen/html/tmap_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmap.h File Reference

Header for Bluetooth TMAP.
[More...](#details)

`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](tmap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_tmap\_cb](structbt__tmap__cb.md) |
|  | TMAP callback structure. [More...](structbt__tmap__cb.md#details) |

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

Copyright 2023 NXP

SPDX-License-Identifier: Apache-2.0

## Enumeration Type Documentation

## [◆ ](#a4ef8a550bb374a5f257860082e1411d4)bt\_tmap\_role

| enum [bt\_tmap\_role](#a4ef8a550bb374a5f257860082e1411d4) |
| --- |

TMAP Role characteristic.

| Enumerator | |
| --- | --- |
| BT\_TMAP\_ROLE\_CG |  |
| BT\_TMAP\_ROLE\_CT |  |
| BT\_TMAP\_ROLE\_UMS |  |
| BT\_TMAP\_ROLE\_UMR |  |
| BT\_TMAP\_ROLE\_BMS |  |
| BT\_TMAP\_ROLE\_BMR |  |

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
