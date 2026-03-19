---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__df__conn__iq__samples__report.html
original_path: doxygen/html/structbt__df__conn__iq__samples__report.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_conn\_iq\_samples\_report Struct Reference

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_df\_conn\_iq\_report\_err](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6) | [err](#ab6e31e979bba969a18804cf8c9b88f03) |
|  | Report receive failed reason. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_phy](#ac14e792a3ce2f3297ddab49e801ba640) |
|  | PHY that was used to receive PDU with CTE that was sampled. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [chan\_idx](#a9374ecd1437f532dec863c527d22348d) |
|  | Channel index used to receive PDU with CTE that was sampled. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [rssi](#aac825fbdecd6a5a82da0097a8694fb65) |
|  | The RSSI of the PDU with CTE (excluding CTE). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rssi\_ant\_id](#a7c5147b426bb87f9d11c8bdffb91ff02) |
|  | Id of antenna used to measure the RSSI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a4d467a7ac76dc9ed6331c10172895097) |
|  | Type of CTE ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#a578132e4a88e739451cf80eba7345094) |
|  | Duration of slots when received CTE type is AoA ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_status](#afdc456a8af5a31ee62c489534af3ecdb) |
|  | Status of received PDU with CTE ([bt\_df\_packet\_status](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c "bt_df_packet_status")). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_evt\_counter](#ac7f3993bd20bd44354f15f098e423c33) |
|  | Value of connection event counter when the CTE was received and sampled. |
| enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) | [sample\_type](#a1e7901b81c8618e4515cd22a681b4d43) |
|  | Type of IQ samples provided in a report. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sample\_count](#a60500e954e2694a209c2d103887b2685) |
|  | Number of IQ samples in report. |
| union { |  |
| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) const \*   [sample](#aa9b177817075e3781256ec2c7d5ac0ce) |  |
| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) const \*   [sample16](#a55e1d7d31557f0e1f59ad91834460b78) |  |
| }; |  |
|  | Pointer to IQ samples data. |

## Field Documentation

## [◆ ](#af3635455cf6b195ba28afd7c1464829a)[union]

| union { ... } [bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md) |
| --- |

Pointer to IQ samples data.

## [◆ ](#a9374ecd1437f532dec863c527d22348d)chan\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::chan\_idx |
| --- |

Channel index used to receive PDU with CTE that was sampled.

## [◆ ](#ac7f3993bd20bd44354f15f098e423c33)conn\_evt\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_df\_conn\_iq\_samples\_report::conn\_evt\_counter |
| --- |

Value of connection event counter when the CTE was received and sampled.

## [◆ ](#a4d467a7ac76dc9ed6331c10172895097)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::cte\_type |
| --- |

Type of CTE ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")).

## [◆ ](#ab6e31e979bba969a18804cf8c9b88f03)err

| enum [bt\_df\_conn\_iq\_report\_err](direction_8h.md#a953634e6a88617a8729541d6b5bd0dd6) bt\_df\_conn\_iq\_samples\_report::err |
| --- |

Report receive failed reason.

## [◆ ](#afdc456a8af5a31ee62c489534af3ecdb)packet\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::packet\_status |
| --- |

Status of received PDU with CTE ([bt\_df\_packet\_status](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c "bt_df_packet_status")).

## [◆ ](#aac825fbdecd6a5a82da0097a8694fb65)rssi

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_df\_conn\_iq\_samples\_report::rssi |
| --- |

The RSSI of the PDU with CTE (excluding CTE).

Range: -1270 to +200. Units: 0.1 dBm.

## [◆ ](#a7c5147b426bb87f9d11c8bdffb91ff02)rssi\_ant\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::rssi\_ant\_id |
| --- |

Id of antenna used to measure the RSSI.

## [◆ ](#ac14e792a3ce2f3297ddab49e801ba640)rx\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::rx\_phy |
| --- |

PHY that was used to receive PDU with CTE that was sampled.

## [◆ ](#aa9b177817075e3781256ec2c7d5ac0ce)sample

| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) const\* bt\_df\_conn\_iq\_samples\_report::sample |
| --- |

## [◆ ](#a55e1d7d31557f0e1f59ad91834460b78)sample16

| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) const\* bt\_df\_conn\_iq\_samples\_report::sample16 |
| --- |

## [◆ ](#a60500e954e2694a209c2d103887b2685)sample\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::sample\_count |
| --- |

Number of IQ samples in report.

## [◆ ](#a1e7901b81c8618e4515cd22a681b4d43)sample\_type

| enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) bt\_df\_conn\_iq\_samples\_report::sample\_type |
| --- |

Type of IQ samples provided in a report.

## [◆ ](#a578132e4a88e739451cf80eba7345094)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_conn\_iq\_samples\_report::slot\_durations |
| --- |

Duration of slots when received CTE type is AoA ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
