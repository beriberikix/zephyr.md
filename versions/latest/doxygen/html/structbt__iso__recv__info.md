---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__recv__info.html
original_path: doxygen/html/structbt__iso__recv__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_recv\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Meta Data structure for received ISO packets.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ts](#a4bf778ae9be39eb4a740c2eb9670d98a) |
|  | ISO timestamp. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [seq\_num](#a7c5b950df0359bb561140d0c2726fae6) |
|  | ISO packet sequence number of the first fragment in the SDU. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a0a7842fcb3251ed89b99fde43ba235a5) |
|  | ISO packet flags bitfield (BT\_ISO\_FLAGS\_\*). |

## Detailed Description

ISO Meta Data structure for received ISO packets.

## Field Documentation

## [◆ ](#a0a7842fcb3251ed89b99fde43ba235a5)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_recv\_info::flags |
| --- |

ISO packet flags bitfield (BT\_ISO\_FLAGS\_\*).

## [◆ ](#a7c5b950df0359bb561140d0c2726fae6)seq\_num

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_recv\_info::seq\_num |
| --- |

ISO packet sequence number of the first fragment in the SDU.

## [◆ ](#a4bf778ae9be39eb4a740c2eb9670d98a)ts

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_recv\_info::ts |
| --- |

ISO timestamp.

Only valid if `flags` has the BT\_ISO\_FLAGS\_TS bit set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_recv\_info](structbt__iso__recv__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
