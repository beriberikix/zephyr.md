---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__sar__rx.html
original_path: doxygen/html/structbt__mesh__sar__rx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_sar\_rx Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [SAR Configuration common header](group__bt__mesh__sar__cfg.md)

SAR Receiver Configuration state structure.
[More...](#details)

`#include <[sar_cfg.h](sar__cfg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [seg\_thresh](#a32a790589ddebee397d536b18518558d) |
|  | SAR Segments Threshold state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ack\_delay\_inc](#a5517a0f2167340cf59ef6fc72077f010) |
|  | SAR Acknowledgment Delay Increment state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [discard\_timeout](#a70615d8df27b6f8291291b73abc57c9c) |
|  | SAR Discard Timeout state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_seg\_int\_step](#ad277cc6c5d221aab7fd22581bfccd83c) |
|  | SAR Receiver Segment Interval Step state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ack\_retrans\_count](#aac228432bddf7f112ccbcb9e3d05d2ce) |
|  | SAR Acknowledgment Retransmissions Count state. |

## Detailed Description

SAR Receiver Configuration state structure.

## Field Documentation

## [◆ ](#a5517a0f2167340cf59ef6fc72077f010)ack\_delay\_inc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_rx::ack\_delay\_inc |
| --- |

SAR Acknowledgment Delay Increment state.

## [◆ ](#aac228432bddf7f112ccbcb9e3d05d2ce)ack\_retrans\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_rx::ack\_retrans\_count |
| --- |

SAR Acknowledgment Retransmissions Count state.

## [◆ ](#a70615d8df27b6f8291291b73abc57c9c)discard\_timeout

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_rx::discard\_timeout |
| --- |

SAR Discard Timeout state.

## [◆ ](#ad277cc6c5d221aab7fd22581bfccd83c)rx\_seg\_int\_step

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_rx::rx\_seg\_int\_step |
| --- |

SAR Receiver Segment Interval Step state.

## [◆ ](#a32a790589ddebee397d536b18518558d)seg\_thresh

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_rx::seg\_thresh |
| --- |

SAR Segments Threshold state.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[sar\_cfg.h](sar__cfg_8h_source.md)

- [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
