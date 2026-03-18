---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__sar__tx.html
original_path: doxygen/html/structbt__mesh__sar__tx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_sar\_tx Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [SAR Configuration common header](group__bt__mesh__sar__cfg.md)

SAR Transmitter Configuration state structure.
[More...](#details)

`#include <[sar_cfg.h](sar__cfg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [seg\_int\_step](#aa491eda390c1b9532e968ed566ec23c2) |
|  | SAR Segment Interval Step state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [unicast\_retrans\_count](#adaa856b561ac24c07706a04eea157183) |
|  | SAR Unicast Retransmissions Count state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [unicast\_retrans\_without\_prog\_count](#a1893bbeb473ebcf99db633e7f979b376) |
|  | SAR Unicast Retransmissions Without Progress Count state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [unicast\_retrans\_int\_step](#a8e0ad5b5977bd4aad20bd79977a0342d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [unicast\_retrans\_int\_inc](#a40a96d401f44345397bd605d6f25e04a) |
|  | SAR Unicast Retransmissions Interval Increment state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [multicast\_retrans\_count](#a686a6a4a7e6a7c6a532ddb8c8bad76df) |
|  | SAR Multicast Retransmissions Count state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [multicast\_retrans\_int](#a6fec529b66c04f0828f5d5d716fd9281) |
|  | SAR Multicast Retransmissions Interval state. |

## Detailed Description

SAR Transmitter Configuration state structure.

## Field Documentation

## [◆ ](#a686a6a4a7e6a7c6a532ddb8c8bad76df)multicast\_retrans\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::multicast\_retrans\_count |
| --- |

SAR Multicast Retransmissions Count state.

## [◆ ](#a6fec529b66c04f0828f5d5d716fd9281)multicast\_retrans\_int

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::multicast\_retrans\_int |
| --- |

SAR Multicast Retransmissions Interval state.

## [◆ ](#aa491eda390c1b9532e968ed566ec23c2)seg\_int\_step

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::seg\_int\_step |
| --- |

SAR Segment Interval Step state.

## [◆ ](#adaa856b561ac24c07706a04eea157183)unicast\_retrans\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::unicast\_retrans\_count |
| --- |

SAR Unicast Retransmissions Count state.

## [◆ ](#a40a96d401f44345397bd605d6f25e04a)unicast\_retrans\_int\_inc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::unicast\_retrans\_int\_inc |
| --- |

SAR Unicast Retransmissions Interval Increment state.

## [◆ ](#a8e0ad5b5977bd4aad20bd79977a0342d)unicast\_retrans\_int\_step

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::unicast\_retrans\_int\_step |
| --- |

## [◆ ](#a1893bbeb473ebcf99db633e7f979b376)unicast\_retrans\_without\_prog\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_sar\_tx::unicast\_retrans\_without\_prog\_count |
| --- |

SAR Unicast Retransmissions Without Progress Count state.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[sar\_cfg.h](sar__cfg_8h_source.md)

- [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
