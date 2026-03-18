---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__blob__chunk.html
original_path: doxygen/html/structbt__mesh__blob__chunk.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_chunk Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB model API](group__bt__mesh__blob.md)

BLOB data chunk.
[More...](#details)

`#include <[blob.h](blob_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [offset](#aabd55d7c8acf726cbc3470af55cb6bc5) |
|  | Offset of the chunk data from the start of the block. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#afd2be87f4cd91f29eb24ebd0dfd9bccb) |
|  | Chunk data size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#ad6f5ff266346af1ab0ba29f5339cb83f) |
|  | Chunk data. |

## Detailed Description

BLOB data chunk.

## Field Documentation

## [◆ ](#ad6f5ff266346af1ab0ba29f5339cb83f)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_blob\_chunk::data |
| --- |

Chunk data.

## [◆ ](#aabd55d7c8acf726cbc3470af55cb6bc5)offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) bt\_mesh\_blob\_chunk::offset |
| --- |

Offset of the chunk data from the start of the block.

## [◆ ](#afd2be87f4cd91f29eb24ebd0dfd9bccb)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_blob\_chunk::size |
| --- |

Chunk data size.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob.h](blob_8h_source.md)

- [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
