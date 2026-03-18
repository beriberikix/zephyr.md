---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__dfu__metadata.html
original_path: doxygen/html/group__bt__mesh__dfu__metadata.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh Device Firmware Update (DFU) metadata

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md)

Common types and functions for the Bluetooth Mesh DFU metadata.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md) |
|  | Firmware version. [More...](structbt__mesh__dfu__metadata__fw__ver.md#details) |
| struct | [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) |
|  | Firmware metadata. [More...](structbt__mesh__dfu__metadata.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_dfu\_metadata\_fw\_core\_type](#gaec5fa6e61a6ae88ac7a14f1ec09585b8) { [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP](#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0) = BIT(0) , [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_NETWORK](#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692) = BIT(1) , [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP\_SPECIFIC\_BLOB](#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2) = BIT(2) } |
|  | Firmware core type. [More...](#gaec5fa6e61a6ae88ac7a14f1ec09585b8) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_dfu\_metadata\_decode](#ga7f9ab277a7a47ad9cd8e616d3aa810d4) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \*metadata) |
|  | Decode a firmware metadata from a network buffer. |
| int | [bt\_mesh\_dfu\_metadata\_encode](#ga94de2f3730f600d58ff2102257d7ead9) (const struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \*metadata, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Encode a firmware metadata into a network buffer. |
| int | [bt\_mesh\_dfu\_metadata\_comp\_hash\_get](#ga3c5de8cefc6a47805a9c1af166e956c7) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*hash) |
|  | Compute hash of the Composition Data state. |
| int | [bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get](#gadc818fb83b429b0f1bef0ba83ae7a52a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*hash) |
|  | Compute hash of the Composition Data Page 0 of this device. |

## Detailed Description

Common types and functions for the Bluetooth Mesh DFU metadata.

## Enumeration Type Documentation

## [◆ ](#gaec5fa6e61a6ae88ac7a14f1ec09585b8)bt\_mesh\_dfu\_metadata\_fw\_core\_type

| enum [bt\_mesh\_dfu\_metadata\_fw\_core\_type](#gaec5fa6e61a6ae88ac7a14f1ec09585b8) |
| --- |

`#include <[dfu_metadata.h](dfu__metadata_8h.md)>`

Firmware core type.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP | Application core. |
| BT\_MESH\_DFU\_FW\_CORE\_TYPE\_NETWORK | Network core. |
| BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP\_SPECIFIC\_BLOB | Application-specific BLOB. |

## Function Documentation

## [◆ ](#ga3c5de8cefc6a47805a9c1af166e956c7)bt\_mesh\_dfu\_metadata\_comp\_hash\_get()

| int bt\_mesh\_dfu\_metadata\_comp\_hash\_get | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *key*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *hash* ) |

`#include <[dfu_metadata.h](dfu__metadata_8h.md)>`

Compute hash of the Composition Data state.

The format of the Composition Data is defined in MshPRTv1.1: 4.2.2.1.

Parameters
:   | buf | Pointer to buffer holding Composition Data. |
    | --- | --- |
    | key | 128-bit key to be used in the hash computation. |
    | hash | Pointer to a memory location to which the hash will be stored. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gadc818fb83b429b0f1bef0ba83ae7a52a)bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get()

| int bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *key*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *hash* ) |

`#include <[dfu_metadata.h](dfu__metadata_8h.md)>`

Compute hash of the Composition Data Page 0 of this device.

Parameters
:   | key | 128-bit key to be used in the hash computation. |
    | --- | --- |
    | hash | Pointer to a memory location to which the hash will be stored. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga7f9ab277a7a47ad9cd8e616d3aa810d4)bt\_mesh\_dfu\_metadata\_decode()

| int bt\_mesh\_dfu\_metadata\_decode | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \* | *metadata* ) |

`#include <[dfu_metadata.h](dfu__metadata_8h.md)>`

Decode a firmware metadata from a network buffer.

Parameters
:   | buf | Buffer containing a raw metadata to be decoded. |
    | --- | --- |
    | metadata | Pointer to a metadata structure to be filled. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga94de2f3730f600d58ff2102257d7ead9)bt\_mesh\_dfu\_metadata\_encode()

| int bt\_mesh\_dfu\_metadata\_encode | ( | const struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \* | *metadata*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* ) |

`#include <[dfu_metadata.h](dfu__metadata_8h.md)>`

Encode a firmware metadata into a network buffer.

Parameters
:   | metadata | Firmware metadata to be encoded. |
    | --- | --- |
    | buf | Buffer to store the encoded metadata. |

Returns
:   0 on success, or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
