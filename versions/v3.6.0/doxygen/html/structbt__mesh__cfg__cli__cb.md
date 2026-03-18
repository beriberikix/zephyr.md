---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__cfg__cli__cb.html
original_path: doxygen/html/structbt__mesh__cfg__cli__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cfg\_cli\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Mesh Configuration Client Status messages callback.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [comp\_data](#aaae4e3f64e2033a466ad87d362ceb318) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Optional callback for Composition data messages. |
| void(\* | [mod\_pub\_status](#ab4130e909826aa7746092f49f8b4c52e) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub) |
|  | Optional callback for Model Pub status messages. |
| void(\* | [mod\_sub\_status](#af4a43f4c65d111e95211b715048534cc) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mod\_id) |
|  | Optional callback for Model Sub Status messages. |
| void(\* | [mod\_sub\_list](#a0ad46d1d4793577679f66c62175e14cf) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Optional callback for Model Sub list messages. |
| void(\* | [node\_reset\_status](#acf88660364760442dfab5280ae735d2d) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Optional callback for Node Reset Status messages. |
| void(\* | [beacon\_status](#a5cf2c17a88c53c514fcaa73a6fd81b67) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Optional callback for Beacon Status messages. |
| void(\* | [ttl\_status](#ab937311c41af68b1cd52a8a1c86145b1) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Optional callback for Default TTL Status messages. |
| void(\* | [friend\_status](#a9487a159a6c838a9218b3d76fa53248d) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Optional callback for Friend Status messages. |
| void(\* | [gatt\_proxy\_status](#a6ef3730e9469bffd81cdd49c50cac7d5) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Optional callback for GATT Proxy Status messages. |
| void(\* | [network\_transmit\_status](#ad46ea40b75cc1d5d314fdefdca0076f8) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Optional callback for Network Transmit Status messages. |
| void(\* | [relay\_status](#a89eab453e00662f6f3f8a5d78f20d120) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) transmit) |
|  | Optional callback for Relay Status messages. |
| void(\* | [net\_key\_status](#a49a7a8cab34bb70d2edd87b0017f1cf7) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Optional callback for NetKey Status messages. |
| void(\* | [net\_key\_list](#acce08dfa5cb356a2203f0ef6c4e4bf5b) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Optional callback for Netkey list messages. |
| void(\* | [app\_key\_status](#a48ef4d0665d86d069b90533eb18e0fd0) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx) |
|  | Optional callback for AppKey Status messages. |
| void(\* | [app\_key\_list](#ac331fc103d0f331093929f39e5b9d6ba) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Optional callback for Appkey list messages. |
| void(\* | [mod\_app\_status](#a3ccff69f21e0f3c585b951eb60c1bf5c) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mod\_id) |
|  | Optional callback for Model App Status messages. |
| void(\* | [mod\_app\_list](#abf8501e73f44ab5ea7e54b8f2ff1f866) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Optional callback for Model App list messages. |
| void(\* | [node\_identity\_status](#aca2d779401fa4521813e6578bd3bbd91) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identity) |
|  | Optional callback for Node Identity Status messages. |
| void(\* | [lpn\_timeout\_status](#a66b5a8dd3bdd2468fe65496020b13495) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
|  | Optional callback for LPN PollTimeout Status messages. |
| void(\* | [krp\_status](#a4d89033676eb4570cdd80f1715fd9bfb) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phase) |
|  | Optional callback for Key Refresh Phase status messages. |
| void(\* | [hb\_pub\_status](#a615852027a841b1779a50c9fd50bef6a) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub) |
|  | Optional callback for Heartbeat pub status messages. |
| void(\* | [hb\_sub\_status](#aa60dfd72a43273e1ffae2160bcc0845d) )(struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub) |
|  | Optional callback for Heartbeat Sub status messages. |

## Detailed Description

Mesh Configuration Client Status messages callback.

## Field Documentation

## [◆ ](#ac331fc103d0f331093929f39e5b9d6ba)app\_key\_list

| void(\* bt\_mesh\_cfg\_cli\_cb::app\_key\_list) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Optional callback for Appkey list messages.

Handles received Appkey list messages from a server.

Note
:   The `buf` parameter should be decoded using the [bt\_mesh\_key\_idx\_unpack\_list](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c "bt_mesh_key_idx_unpack_list") helper function.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | net\_idx | The index of the NetKey. |
    | buf | Message buffer containing key indexes. |

## [◆ ](#a48ef4d0665d86d069b90533eb18e0fd0)app\_key\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::app\_key\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx) |
| --- |

Optional callback for AppKey Status messages.

Handles received AppKey Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |
    | net\_idx | The index of the NetKey. |
    | app\_idx | The index of the AppKey. |

## [◆ ](#a5cf2c17a88c53c514fcaa73a6fd81b67)beacon\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::beacon\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
| --- |

Optional callback for Beacon Status messages.

Handles received Beacon Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |

## [◆ ](#aaae4e3f64e2033a466ad87d362ceb318)comp\_data

| void(\* bt\_mesh\_cfg\_cli\_cb::comp\_data) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Optional callback for Composition data messages.

Handles received Composition data messages from a server.

Note
:   For decoding `buf`, please refer to [bt\_mesh\_comp\_p0\_get](group__bt__mesh__cfg__cli.md#ga1f79d98273a984f1c49b4d5dd5bf8d30 "bt_mesh_comp_p0_get") and [bt\_mesh\_comp\_p1\_elem\_pull](group__bt__mesh__cfg__cli.md#gae9a19b089d898af914ea5c287aca8fba "bt_mesh_comp_p1_elem_pull").

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | page | Composition data page. |
    | buf | Composition data buffer. |

## [◆ ](#a9487a159a6c838a9218b3d76fa53248d)friend\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::friend\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
| --- |

Optional callback for Friend Status messages.

Handles received Friend Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |

## [◆ ](#a6ef3730e9469bffd81cdd49c50cac7d5)gatt\_proxy\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::gatt\_proxy\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
| --- |

Optional callback for GATT Proxy Status messages.

Handles received GATT Proxy Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |

## [◆ ](#a615852027a841b1779a50c9fd50bef6a)hb\_pub\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::hb\_pub\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub) |
| --- |

Optional callback for Heartbeat pub status messages.

Handles received Heartbeat pub status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | pub | HB publication configuration parameters. |

## [◆ ](#aa60dfd72a43273e1ffae2160bcc0845d)hb\_sub\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::hb\_sub\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub) |
| --- |

Optional callback for Heartbeat Sub status messages.

Handles received Heartbeat Sub status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | sub | HB subscription configuration parameters. |

## [◆ ](#a4d89033676eb4570cdd80f1715fd9bfb)krp\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::krp\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) phase) |
| --- |

Optional callback for Key Refresh Phase status messages.

Handles received Key Refresh Phase status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | net\_idx | The index of the NetKey. |
    | phase | Phase of the KRP. |

## [◆ ](#a66b5a8dd3bdd2468fe65496020b13495)lpn\_timeout\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::lpn\_timeout\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
| --- |

Optional callback for LPN PollTimeout Status messages.

Handles received LPN PollTimeout Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | elem\_addr | The unicast address of the LPN. |
    | timeout | Current value of PollTimeout timer of the LPN. |

## [◆ ](#abf8501e73f44ab5ea7e54b8f2ff1f866)mod\_app\_list

| void(\* bt\_mesh\_cfg\_cli\_cb::mod\_app\_list) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Optional callback for Model App list messages.

Handles received Model App list messages from a server.

Note
:   The `buf` parameter should be decoded using the [bt\_mesh\_key\_idx\_unpack\_list](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c "bt_mesh_key_idx_unpack_list") helper function.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | elem\_addr | Address of the element. |
    | mod\_id | Model ID. |
    | cid | Company ID. |
    | buf | Message buffer containing key indexes. |

## [◆ ](#a3ccff69f21e0f3c585b951eb60c1bf5c)mod\_app\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::mod\_app\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mod\_id) |
| --- |

Optional callback for Model App Status messages.

Handles received Model App Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |
    | elem\_addr | The unicast address of the element. |
    | app\_idx | The sub address. |
    | mod\_id | The model ID within the element. |

## [◆ ](#ab4130e909826aa7746092f49f8b4c52e)mod\_pub\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::mod\_pub\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub) |
| --- |

Optional callback for Model Pub status messages.

Handles received Model Pub status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | elem\_addr | Address of the element. |
    | mod\_id | Model ID. |
    | cid | Company ID. |
    | pub | Publication configuration parameters. |

## [◆ ](#a0ad46d1d4793577679f66c62175e14cf)mod\_sub\_list

| void(\* bt\_mesh\_cfg\_cli\_cb::mod\_sub\_list) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Optional callback for Model Sub list messages.

Handles received Model Sub list messages from a server.

Note
:   The `buf` parameter should be decoded using [net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba "net_buf_simple_pull_le16") in iteration, as long as `buf->len` is greater than or equal to 2.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status code for the message. |
    | elem\_addr | Address of the element. |
    | mod\_id | Model ID. |
    | cid | Company ID. |
    | buf | Message buffer containing subscription addresses. |

## [◆ ](#af4a43f4c65d111e95211b715048534cc)mod\_sub\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::mod\_sub\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mod\_id) |
| --- |

Optional callback for Model Sub Status messages.

Handles received Model Sub Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |
    | elem\_addr | The unicast address of the element. |
    | sub\_addr | The sub address. |
    | mod\_id | The model ID within the element. |

## [◆ ](#acce08dfa5cb356a2203f0ef6c4e4bf5b)net\_key\_list

| void(\* bt\_mesh\_cfg\_cli\_cb::net\_key\_list) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Optional callback for Netkey list messages.

Handles received Netkey list messages from a server.

Note
:   The `buf` parameter should be decoded using the [bt\_mesh\_key\_idx\_unpack\_list](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c "bt_mesh_key_idx_unpack_list") helper function.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | buf | Message buffer containing key indexes. |

## [◆ ](#a49a7a8cab34bb70d2edd87b0017f1cf7)net\_key\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::net\_key\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
| --- |

Optional callback for NetKey Status messages.

Handles received NetKey Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |
    | net\_idx | The index of the NetKey. |

## [◆ ](#ad46ea40b75cc1d5d314fdefdca0076f8)network\_transmit\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::network\_transmit\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
| --- |

Optional callback for Network Transmit Status messages.

Handles received Network Transmit Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |

## [◆ ](#aca2d779401fa4521813e6578bd3bbd91)node\_identity\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::node\_identity\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identity) |
| --- |

Optional callback for Node Identity Status messages.

Handles received Node Identity Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |
    | net\_idx | The index of the NetKey. |
    | identity | The node identity state. |

## [◆ ](#acf88660364760442dfab5280ae735d2d)node\_reset\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::node\_reset\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
| --- |

Optional callback for Node Reset Status messages.

Handles received Node Reset Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |

## [◆ ](#a89eab453e00662f6f3f8a5d78f20d120)relay\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::relay\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) transmit) |
| --- |

Optional callback for Relay Status messages.

Handles received Relay Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |
    | transmit | The relay retransmit count and interval steps. |

## [◆ ](#ab937311c41af68b1cd52a8a1c86145b1)ttl\_status

| void(\* bt\_mesh\_cfg\_cli\_cb::ttl\_status) (struct [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
| --- |

Optional callback for Default TTL Status messages.

Handles received Default TTL Status messages from a server.

Parameters
:   | cli | Client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status Code for requesting message. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
