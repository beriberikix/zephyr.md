---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__priv__beacon__cli__cb.html
original_path: doxygen/html/structbt__mesh__priv__beacon__cli__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_priv\_beacon\_cli\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Private Beacon Client](group__bt__mesh__priv__beacon__cli.md)

Private Beacon Client Status messages callbacks.
[More...](#details)

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [priv\_beacon\_status](#ab4b58af5af27be22dc395df4b2fd35c4) )(struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*priv\_beacon) |
|  | Optional callback for Private Beacon Status message. |
| void(\* | [priv\_gatt\_proxy\_status](#a825bb5dee44075a8b6d14efc5f68c372) )(struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gatt\_proxy) |
|  | Optional callback for Private GATT Proxy Status message. |
| void(\* | [priv\_node\_id\_status](#aa1206f9a75beb79449e5a1bad8e62f41) )(struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*priv\_node\_id) |
|  | Optional callback for Private Node Identity Status message. |

## Detailed Description

Private Beacon Client Status messages callbacks.

## Field Documentation

## [◆ ](#ab4b58af5af27be22dc395df4b2fd35c4)priv\_beacon\_status

| void(\* bt\_mesh\_priv\_beacon\_cli\_cb::priv\_beacon\_status) (struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*priv\_beacon) |
| --- |

Optional callback for Private Beacon Status message.

Handles received Private Beacon Status messages from a Private Beacon server.

Parameters
:   | cli | Private Beacon client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | priv\_beacon | Mesh Private Beacon state received from the server. |

## [◆ ](#a825bb5dee44075a8b6d14efc5f68c372)priv\_gatt\_proxy\_status

| void(\* bt\_mesh\_priv\_beacon\_cli\_cb::priv\_gatt\_proxy\_status) (struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gatt\_proxy) |
| --- |

Optional callback for Private GATT Proxy Status message.

Handles received Private GATT Proxy Status messages from a Private Beacon server.

Parameters
:   | cli | Private Beacon client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | gatt\_proxy | Private GATT Proxy state received from the server. |

## [◆ ](#aa1206f9a75beb79449e5a1bad8e62f41)priv\_node\_id\_status

| void(\* bt\_mesh\_priv\_beacon\_cli\_cb::priv\_node\_id\_status) (struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*priv\_node\_id) |
| --- |

Optional callback for Private Node Identity Status message.

Handles received Private Node Identity Status messages from a Private Beacon server.

Parameters
:   | cli | Private Beacon client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | priv\_node\_id | Private Node Identity state received from the server. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[priv\_beacon\_cli.h](priv__beacon__cli_8h_source.md)

- [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
