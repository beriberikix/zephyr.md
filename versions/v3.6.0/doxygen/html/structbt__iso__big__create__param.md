---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__big__create__param.html
original_path: doxygen/html/structbt__iso__big__create__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_big\_create\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

Broadcast Isochronous Group (BIG) creation parameters.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_iso\_chan](structbt__iso__chan.md) \*\* | [bis\_channels](#a7548bbb75f240a70435cb86a48846d0a) |
|  | Array of pointers to BIS channels. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_bis](#a8ae9c225798e9f5b72fe0b8c3b6f2cf0) |
|  | Number channels in `bis_channels`. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval](#a7aaef1f7a78ae1088886a78739fd6849) |
|  | Channel interval in us. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#ab847021da2e604036cecf90483e12132) |
|  | Channel Latency in ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#ad478d7b36fb34b8e57a25ae0029e4c51) |
|  | Channel packing mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [framing](#aab0e9f66cb10643e72d6382718ed4c0d) |
|  | Channel framing mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a1288fa2a8f6bb3e2ab26729e245277e1) |
|  | Whether or not to encrypt the streams. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcode](#aaee9af5a21b2f9812f9635c526f3a923) [16] |
|  | Broadcast code. |

## Detailed Description

Broadcast Isochronous Group (BIG) creation parameters.

## Field Documentation

## [◆ ](#aaee9af5a21b2f9812f9635c526f3a923)bcode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_big\_create\_param::bcode[16] |
| --- |

Broadcast code.

The code used to derive the session key that is used to encrypt and decrypt BIS payloads.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a7548bbb75f240a70435cb86a48846d0a)bis\_channels

| struct [bt\_iso\_chan](structbt__iso__chan.md)\*\* bt\_iso\_big\_create\_param::bis\_channels |
| --- |

Array of pointers to BIS channels.

## [◆ ](#a1288fa2a8f6bb3e2ab26729e245277e1)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_iso\_big\_create\_param::encryption |
| --- |

Whether or not to encrypt the streams.

## [◆ ](#aab0e9f66cb10643e72d6382718ed4c0d)framing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_big\_create\_param::framing |
| --- |

Channel framing mode.

BT\_ISO\_FRAMING\_UNFRAMED for unframed and BT\_ISO\_FRAMING\_FRAMED for framed.

## [◆ ](#a7aaef1f7a78ae1088886a78739fd6849)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_big\_create\_param::interval |
| --- |

Channel interval in us.

Value range BT\_ISO\_SDU\_INTERVAL\_MIN - BT\_ISO\_SDU\_INTERVAL\_MAX.

## [◆ ](#ab847021da2e604036cecf90483e12132)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_big\_create\_param::latency |
| --- |

Channel Latency in ms.

Value range BT\_ISO\_LATENCY\_MIN - BT\_ISO\_LATENCY\_MAX.

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#a8ae9c225798e9f5b72fe0b8c3b6f2cf0)num\_bis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_big\_create\_param::num\_bis |
| --- |

Number channels in `bis_channels`.

Maximum number of channels in a single group is BT\_ISO\_MAX\_GROUP\_ISO\_COUNT

## [◆ ](#ad478d7b36fb34b8e57a25ae0029e4c51)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_big\_create\_param::packing |
| --- |

Channel packing mode.

BT\_ISO\_PACKING\_SEQUENTIAL or BT\_ISO\_PACKING\_INTERLEAVED

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
