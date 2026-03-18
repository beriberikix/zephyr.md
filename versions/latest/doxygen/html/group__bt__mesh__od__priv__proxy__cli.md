---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html
original_path: doxygen/html/group__bt__mesh__od__priv__proxy__cli.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh On-Demand Private GATT Proxy Client

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md) |
|  | On-Demand Private Proxy Client Model Context. [More...](structbt__mesh__od__priv__proxy__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_CLI](#ga037391820efab2b953805f6373431ca9)(cli\_data) |
|  | On-Demand Private Proxy Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_od\_priv\_proxy\_cli\_get](#ga11357595b2d837f6172a2ec98d1e9973) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val\_rsp) |
|  | Get the target's On-Demand Private GATT Proxy state. |
| int | [bt\_mesh\_od\_priv\_proxy\_cli\_set](#ga9b239c221f8c74108e2a7e5276122e1f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val\_rsp) |
|  | Set the target's On-Demand Private GATT Proxy state. |
| void | [bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set](#gad613c78e708f0df5aabda9e16fae6a2c) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga037391820efab2b953805f6373431ca9)BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_CLI

| #define BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_CLI | ( |  | *cli\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[od_priv_proxy_cli.h](od__priv__proxy__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI](group__bt__mesh__access.md#gadd36546fb2cb6d1c731f7ae7674af6a7), \

\_bt\_mesh\_od\_priv\_proxy\_cli\_op, NULL, cli\_data, \

&\_bt\_mesh\_od\_priv\_proxy\_cli\_cb)

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI](group__bt__mesh__access.md#gadd36546fb2cb6d1c731f7ae7674af6a7)

#define BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI

Private Proxy Client.

**Definition** access.h:213

On-Demand Private Proxy Client model composition data entry.

## Function Documentation

## [◆ ](#ga11357595b2d837f6172a2ec98d1e9973)bt\_mesh\_od\_priv\_proxy\_cli\_get()

| int bt\_mesh\_od\_priv\_proxy\_cli\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *val\_rsp* ) |

`#include <[od_priv_proxy_cli.h](od__priv__proxy__cli_8h.md)>`

Get the target's On-Demand Private GATT Proxy state.

This method can be used asynchronously by setting `val_rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `od_status` callback in `[bt_mesh_od_priv_proxy_cli](structbt__mesh__od__priv__proxy__cli.md "On-Demand Private Proxy Client Model Context.")` struct.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val\_rsp | Response buffer for On-Demand Private GATT Proxy value. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga9b239c221f8c74108e2a7e5276122e1f)bt\_mesh\_od\_priv\_proxy\_cli\_set()

| int bt\_mesh\_od\_priv\_proxy\_cli\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *val\_rsp* ) |

`#include <[od_priv_proxy_cli.h](od__priv__proxy__cli_8h.md)>`

Set the target's On-Demand Private GATT Proxy state.

This method can be used asynchronously by setting `val_rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

To process the response arguments of an async method, register the `od_status` callback in `[bt_mesh_od_priv_proxy_cli](structbt__mesh__od__priv__proxy__cli.md "On-Demand Private Proxy Client Model Context.")` struct.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | On-Demand Private GATT Proxy state to be set |
    | val\_rsp | Response buffer for On-Demand Private GATT Proxy value. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gad613c78e708f0df5aabda9e16fae6a2c)bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set()

| void bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[od_priv_proxy_cli.h](od__priv__proxy__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout in milliseconds. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
