---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__blob__xfer.html
original_path: doxygen/html/structbt__mesh__blob__xfer.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_xfer Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB model API](group__bt__mesh__blob.md)

BLOB transfer.
[More...](#details)

`#include <[blob.h](blob_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [id](#a9b4f37addd1271e26ab90c6e63608867) |
|  | BLOB ID. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a7a2ca36b08d1d55c2dfbca0120a5274d) |
|  | Total BLOB size in bytes. |
| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) | [mode](#a2c3d9365b5cb6e569d147acae7a74ed6) |
|  | BLOB transfer mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [block\_size\_log](#aa971742f85ccd94bbdef6c61203caeba) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chunk\_size](#a646c5c56d5290f6c65e2b9fca89e9835) |
|  | Base chunk size. |

## Detailed Description

BLOB transfer.

## Field Documentation

## [◆ ](#aa971742f85ccd94bbdef6c61203caeba)block\_size\_log

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_xfer::block\_size\_log |
| --- |

## [◆ ](#a646c5c56d5290f6c65e2b9fca89e9835)chunk\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_xfer::chunk\_size |
| --- |

Base chunk size.

May be smaller for the last chunk.

## [◆ ](#a9b4f37addd1271e26ab90c6e63608867)id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bt\_mesh\_blob\_xfer::id |
| --- |

BLOB ID.

## [◆ ](#a2c3d9365b5cb6e569d147acae7a74ed6)mode

| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) bt\_mesh\_blob\_xfer::mode |
| --- |

BLOB transfer mode.

## [◆ ](#a7a2ca36b08d1d55c2dfbca0120a5274d)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_blob\_xfer::size |
| --- |

Total BLOB size in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob.h](blob_8h_source.md)

- [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
