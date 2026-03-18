---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__cfg__cli__hb__pub.html
original_path: doxygen/html/structbt__mesh__cfg__cli__hb__pub.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cfg\_cli\_hb\_pub Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Heartbeat publication configuration parameters.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst](#a473df7dd958683d7502dcc983c4ceb8a) |
|  | Heartbeat destination address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [count](#a13c7c155f30ca94d30090a25df50e4b2) |
|  | Logarithmic Heartbeat count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [period](#a8d17dd2df4be23cadad4b5746ddb50ad) |
|  | Logarithmic Heartbeat publication transmit interval in seconds. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#ac7f24f7bf942587ef83ca47d9ee4e7fb) |
|  | Publication message Time To Live value. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [feat](#a94598c9b733075abe22d70f62293b5a1) |
|  | Bitmap of features that trigger Heartbeat publications. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx](#a90a79d8b7ea91c6ba872dca15d87b356) |
|  | Network index to publish with. |

## Detailed Description

Heartbeat publication configuration parameters.

## Field Documentation

## [◆ ](#a13c7c155f30ca94d30090a25df50e4b2)count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_pub::count |
| --- |

Logarithmic Heartbeat count.

Decoded as (1 << (count - 1)) if count is between 1 and 0x11, 0 if count is 0, or "indefinitely" if count is 0xff.

When used in Heartbeat publication set, this parameter denotes the number of Heartbeat messages to send.

When returned from Heartbeat publication get, this parameter denotes the number of Heartbeat messages remaining to be sent.

## [◆ ](#a473df7dd958683d7502dcc983c4ceb8a)dst

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_hb\_pub::dst |
| --- |

Heartbeat destination address.

## [◆ ](#a94598c9b733075abe22d70f62293b5a1)feat

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_hb\_pub::feat |
| --- |

Bitmap of features that trigger Heartbeat publications.

Legal values are [BT\_MESH\_FEAT\_RELAY](group__bt__mesh.md#gac588eefe83db94784a420ce063f02b55 "BT_MESH_FEAT_RELAY"), [BT\_MESH\_FEAT\_PROXY](group__bt__mesh.md#gaee648ce202316c56d4d588cb0ad5aeb4 "BT_MESH_FEAT_PROXY"), [BT\_MESH\_FEAT\_FRIEND](group__bt__mesh.md#ga8f27086b3bc3c4a6e14621836f9f8e80 "BT_MESH_FEAT_FRIEND") and [BT\_MESH\_FEAT\_LOW\_POWER](group__bt__mesh.md#gaad71a36c82b4e4d3fa334ecff5cc0171 "BT_MESH_FEAT_LOW_POWER")

## [◆ ](#a90a79d8b7ea91c6ba872dca15d87b356)net\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cfg\_cli\_hb\_pub::net\_idx |
| --- |

Network index to publish with.

## [◆ ](#a8d17dd2df4be23cadad4b5746ddb50ad)period

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_pub::period |
| --- |

Logarithmic Heartbeat publication transmit interval in seconds.

Decoded as (1 << (period - 1)) if period is between 1 and 0x11. If period is 0, Heartbeat publication is disabled.

## [◆ ](#ac7f24f7bf942587ef83ca47d9ee4e7fb)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cfg\_cli\_hb\_pub::ttl |
| --- |

Publication message Time To Live value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
