---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__hb__pub.html
original_path: doxygen/html/structbt__mesh__hb__pub.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_hb\_pub Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Heartbeat](group__bt__mesh__heartbeat.md)

Heartbeat Publication parameters.
[More...](#details)

`#include <[heartbeat.h](heartbeat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst](#aaeb4c9000088418d8688b4f2f964335a) |
|  | Destination address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [count](#a7161896dd5e337b2b0ee671f59a2444a) |
|  | Remaining publish count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#a82dd3457291cc4a939883590e27fdbfb) |
|  | Time To Live value. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [feat](#a08f32f66fb5c7c0011651633ad212bc9) |
|  | Bitmap of features that trigger a Heartbeat publication if they change. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx](#af8ed3029b088c7b45be4912eb0d9024d) |
|  | Network index used for publishing. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [period](#a0bf6205724b157fe374e24c024f240c9) |
|  | Publication period in seconds. |

## Detailed Description

Heartbeat Publication parameters.

## Field Documentation

## [◆ ](#a7161896dd5e337b2b0ee671f59a2444a)count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_pub::count |
| --- |

Remaining publish count.

## [◆ ](#aaeb4c9000088418d8688b4f2f964335a)dst

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_pub::dst |
| --- |

Destination address.

## [◆ ](#a08f32f66fb5c7c0011651633ad212bc9)feat

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_pub::feat |
| --- |

Bitmap of features that trigger a Heartbeat publication if they change.

Legal values are [BT\_MESH\_FEAT\_RELAY](group__bt__mesh.md#gac588eefe83db94784a420ce063f02b55 "BT_MESH_FEAT_RELAY"), [BT\_MESH\_FEAT\_PROXY](group__bt__mesh.md#gaee648ce202316c56d4d588cb0ad5aeb4 "BT_MESH_FEAT_PROXY"), [BT\_MESH\_FEAT\_FRIEND](group__bt__mesh.md#ga8f27086b3bc3c4a6e14621836f9f8e80 "BT_MESH_FEAT_FRIEND") and [BT\_MESH\_FEAT\_LOW\_POWER](group__bt__mesh.md#gaad71a36c82b4e4d3fa334ecff5cc0171 "BT_MESH_FEAT_LOW_POWER").

## [◆ ](#af8ed3029b088c7b45be4912eb0d9024d)net\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_hb\_pub::net\_idx |
| --- |

Network index used for publishing.

## [◆ ](#a0bf6205724b157fe374e24c024f240c9)period

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_hb\_pub::period |
| --- |

Publication period in seconds.

## [◆ ](#a82dd3457291cc4a939883590e27fdbfb)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_hb\_pub::ttl |
| --- |

Time To Live value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[heartbeat.h](heartbeat_8h_source.md)

- [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
