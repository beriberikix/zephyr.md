---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__blob__block.html
original_path: doxygen/html/structbt__mesh__blob__block.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_block Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB model API](group__bt__mesh__blob.md)

BLOB transfer data block.
[More...](#details)

`#include <[blob.h](blob_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a67632460e4a37407074105f8ff3f97fd) |
|  | Block size in bytes. |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [offset](#a7521b8121a2a1f280d14e9e222b7d6cf) |
|  | Offset in bytes from the start of the BLOB. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [number](#a57f92c3b0ef68128d44a90802788dfa3) |
|  | Block number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chunk\_count](#a6bd9a432a789edeafc5d425232a32b4e) |
|  | Number of chunks in block. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [missing](#accf9cb6d7d838a45284b28268f6e83c8) [[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(0, 8)] |
|  | Bitmap of missing chunks. |

## Detailed Description

BLOB transfer data block.

## Field Documentation

## [◆ ](#a6bd9a432a789edeafc5d425232a32b4e)chunk\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_block::chunk\_count |
| --- |

Number of chunks in block.

## [◆ ](#accf9cb6d7d838a45284b28268f6e83c8)missing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_block::missing[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(0, 8)] |
| --- |

Bitmap of missing chunks.

## [◆ ](#a57f92c3b0ef68128d44a90802788dfa3)number

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_block::number |
| --- |

Block number.

## [◆ ](#a7521b8121a2a1f280d14e9e222b7d6cf)offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) bt\_mesh\_blob\_block::offset |
| --- |

Offset in bytes from the start of the BLOB.

## [◆ ](#a67632460e4a37407074105f8ff3f97fd)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_blob\_block::size |
| --- |

Block size in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob.h](blob_8h_source.md)

- [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
