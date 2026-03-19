---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structzms__ate.html
original_path: doxygen/html/structzms__ate.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zms\_ate Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Zephyr Memory Storage (ZMS)](group__zms.md) » [ZMS data structures](group__zms__data__structures.md)

ZMS Allocation Table Entry (ATE) structure.
[More...](#details)

`#include <[zms_priv.h](zms__priv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8](#ac96dfde8f44e1af031c11490a0add94a) |
|  | crc8 check of the entry |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cycle\_cnt](#a9d5e9e8ac241b613fd2db14cc85d0323) |
|  | cycle counter for non erasable devices |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#aa71a3cb51572eaaa348c3644f332fc7e) |
|  | data len within sector |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#ae624bc7570e77b75fcdc0fa1d74224c8) |
|  | data id |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [data](#a54e3d4ebd6e5eda65e56033e6e2d379b) [8] |  |
|  | data field used to store small sized data [More...](#a54e3d4ebd6e5eda65e56033e6e2d379b) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [offset](#a7d623901562467778185ef61b3f9bb0f) |  |
|  | data offset within sector [More...](#a7d623901562467778185ef61b3f9bb0f) |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [data\_crc](#a8b70dd09e10545dae52bba3eb5f167e8) |  |
|  | crc for data: The data CRC is checked only when the whole data of the element is read. [More...](#a8b70dd09e10545dae52bba3eb5f167e8) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [metadata](#a26388b50787341e09efb85c5c115645d) |  |
|  | Used to store metadata information such as storage version. [More...](#a26388b50787341e09efb85c5c115645d) |
| } |  |
| } |  |
| }; |  |

## Detailed Description

ZMS Allocation Table Entry (ATE) structure.

## Field Documentation

## [◆ ](#a2c98649a1446ee236d7c9d456673aaa3)[union]

| union { ... } [zms\_ate](structzms__ate.md) |
| --- |

## [◆ ](#ac96dfde8f44e1af031c11490a0add94a)crc8

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) zms\_ate::crc8 |
| --- |

crc8 check of the entry

## [◆ ](#a9d5e9e8ac241b613fd2db14cc85d0323)cycle\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) zms\_ate::cycle\_cnt |
| --- |

cycle counter for non erasable devices

## [◆ ](#a54e3d4ebd6e5eda65e56033e6e2d379b)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) zms\_ate::data[8] |
| --- |

data field used to store small sized data

## [◆ ](#a8b70dd09e10545dae52bba3eb5f167e8)data\_crc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zms\_ate::data\_crc |
| --- |

crc for data: The data CRC is checked only when the whole data of the element is read.

The data CRC is not checked for a partial read, as it is computed for the complete set of data.

## [◆ ](#ae624bc7570e77b75fcdc0fa1d74224c8)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zms\_ate::id |
| --- |

data id

## [◆ ](#aa71a3cb51572eaaa348c3644f332fc7e)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) zms\_ate::len |
| --- |

data len within sector

## [◆ ](#a26388b50787341e09efb85c5c115645d)metadata

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zms\_ate::metadata |
| --- |

Used to store metadata information such as storage version.

## [◆ ](#a7d623901562467778185ef61b3f9bb0f)offset

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zms\_ate::offset |
| --- |

data offset within sector

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/fs/zms/[zms\_priv.h](zms__priv_8h_source.md)

- [zms\_ate](structzms__ate.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
