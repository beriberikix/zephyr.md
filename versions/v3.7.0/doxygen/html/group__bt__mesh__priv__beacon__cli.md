---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__priv__beacon__cli.html
original_path: doxygen/html/group__bt__mesh__priv__beacon__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh Private Beacon Client

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) |
|  | Private Beacon. [More...](structbt__mesh__priv__beacon.md#details) |
| struct | [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) |
|  | Private Node Identity. [More...](structbt__mesh__priv__node__id.md#details) |
| struct | [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md) |
|  | Private Beacon Client Status messages callbacks. [More...](structbt__mesh__priv__beacon__cli__cb.md#details) |
| struct | [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) |
|  | Mesh Private Beacon Client model. [More...](structbt__mesh__priv__beacon__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_PRIV\_BEACON\_CLI](#ga65008412f2fc89aa9f71c067ad3fe264)(cli\_data) |
|  | Private Beacon Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_priv\_beacon\_cli\_set](#ga8a535d31954d8871fed557808b6abc71) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*val, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*rsp) |
|  | Set the target's Private Beacon state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_get](#ga76d797a76d8f8fda31feacce840a6f9e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*val) |
|  | Get the target's Private Beacon state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set](#ga389626a517c1bb9cae31501663725483) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp) |
|  | Set the target's Private GATT Proxy state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get](#ga838880ae8391b33d0481fba069ea921b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Get the target's Private GATT Proxy state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_node\_id\_set](#ga2a581e49b8812bd78604fc829bd1d79a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*val, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*rsp) |
|  | Set the target's Private Node Identity state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_node\_id\_get](#gadd6fc3321cd536771921566bbc650396) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*val) |
|  | Get the target's Private Node Identity state. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga65008412f2fc89aa9f71c067ad3fe264)BT\_MESH\_MODEL\_PRIV\_BEACON\_CLI

| #define BT\_MESH\_MODEL\_PRIV\_BEACON\_CLI | ( |  | *cli\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI](group__bt__mesh__access.md#gab3b21cbee4e11319a6e0ba3b02b24a91), \

bt\_mesh\_priv\_beacon\_cli\_op, NULL, cli\_data, \

&[bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md))

[BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI](group__bt__mesh__access.md#gab3b21cbee4e11319a6e0ba3b02b24a91)

#define BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI

Private Beacon Client.

**Definition** access.h:193

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md)

Private Beacon Client Status messages callbacks.

**Definition** priv\_beacon\_cli.h:56

Private Beacon Client model composition data entry.

Parameters
:   | cli\_data | Pointer to a [Bluetooth Mesh Private Beacon Client](group__bt__mesh__priv__beacon__cli.md "Bluetooth Mesh Private Beacon Client") instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga838880ae8391b33d0481fba069ea921b)bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get()

| int bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *val* ) |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

Get the target's Private GATT Proxy state.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | Response buffer for Private GATT Proxy value. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga389626a517c1bb9cae31501663725483)bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set()

| int bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rsp* ) |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

Set the target's Private GATT Proxy state.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New Private GATT Proxy value. |
    | rsp | If set, returns response status on success. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga76d797a76d8f8fda31feacce840a6f9e)bt\_mesh\_priv\_beacon\_cli\_get()

| int bt\_mesh\_priv\_beacon\_cli\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \* | *val* ) |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

Get the target's Private Beacon state.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | Response buffer for Private Beacon value. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gadd6fc3321cd536771921566bbc650396)bt\_mesh\_priv\_beacon\_cli\_node\_id\_get()

| int bt\_mesh\_priv\_beacon\_cli\_node\_id\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \* | *val* ) |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

Get the target's Private Node Identity state.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network index to get the Private Node Identity state of. |
    | val | Response buffer for Private Node Identity value. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga2a581e49b8812bd78604fc829bd1d79a)bt\_mesh\_priv\_beacon\_cli\_node\_id\_set()

| int bt\_mesh\_priv\_beacon\_cli\_node\_id\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \* | *val*, |
|  |  | struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \* | *rsp* ) |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

Set the target's Private Node Identity state.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New Private Node Identity value. |
    | rsp | If set, returns response status on success. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga8a535d31954d8871fed557808b6abc71)bt\_mesh\_priv\_beacon\_cli\_set()

| int bt\_mesh\_priv\_beacon\_cli\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \* | *val*, |
|  |  | struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \* | *rsp* ) |

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h.md)>`

Set the target's Private Beacon state.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New Private Beacon value. |
    | rsp | If set, returns response status on success. |

Returns
:   0 on success, or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
