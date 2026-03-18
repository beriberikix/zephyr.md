---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__blob__target__pull.html
original_path: doxygen/html/structbt__mesh__blob__target__pull.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_target\_pull Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

Target node's Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target node.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [block\_report\_timestamp](#a9234ee3246890285b5cd30c32866b718) |
|  | Timestamp when the Block Report Timeout Timer expires for this Target node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [missing](#a19fc9a8a0b5202887e7fd73028805774) [[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e), 8)] |
|  | Missing chunks reported by this Target node. |

## Detailed Description

Target node's Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target node.

## Field Documentation

## [◆ ](#a9234ee3246890285b5cd30c32866b718)block\_report\_timestamp

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) bt\_mesh\_blob\_target\_pull::block\_report\_timestamp |
| --- |

Timestamp when the Block Report Timeout Timer expires for this Target node.

## [◆ ](#a19fc9a8a0b5202887e7fd73028805774)missing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_target\_pull::missing[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e), 8)] |
| --- |

Missing chunks reported by this Target node.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
