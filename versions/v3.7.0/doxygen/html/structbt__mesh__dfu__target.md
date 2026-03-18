---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__dfu__target.html
original_path: doxygen/html/structbt__mesh__dfu__target.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_target Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

DFU Target node.
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) | [blob](#a96393388212d4bffd8fb00c82e58d364) |
|  | BLOB Target node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [img\_idx](#a986a58915c0b0ab509ddbbbe475976d2) |
|  | Image index on the Target node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [effect](#a3d18d0ae1d0902cf84402b090a9aaa99) |
|  | Expected DFU effect, see [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8 "bt_mesh_dfu_effect"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a4ad51f9dc3fdb39afeef55e4cd22b968) |
|  | Current DFU status, see [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d "bt_mesh_dfu_status"). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phase](#a43730ff708da06fe31e801adf7a79c0e) |
|  | Current DFU phase, see [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2 "bt_mesh_dfu_phase"). |

## Detailed Description

DFU Target node.

## Field Documentation

## [◆ ](#a96393388212d4bffd8fb00c82e58d364)blob

| struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) bt\_mesh\_dfu\_target::blob |
| --- |

BLOB Target node.

## [◆ ](#a3d18d0ae1d0902cf84402b090a9aaa99)effect

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_target::effect |
| --- |

Expected DFU effect, see [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8 "bt_mesh_dfu_effect").

## [◆ ](#a986a58915c0b0ab509ddbbbe475976d2)img\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_target::img\_idx |
| --- |

Image index on the Target node.

## [◆ ](#a43730ff708da06fe31e801adf7a79c0e)phase

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_target::phase |
| --- |

Current DFU phase, see [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2 "bt_mesh_dfu_phase").

## [◆ ](#a4ad51f9dc3fdb39afeef55e4cd22b968)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_target::status |
| --- |

Current DFU status, see [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d "bt_mesh_dfu_status").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
