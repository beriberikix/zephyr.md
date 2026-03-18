---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__df__per__adv__sync__iq__samples__report.html
original_path: doxygen/html/structbt__df__per__adv__sync__iq__samples__report.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_df\_per\_adv\_sync\_iq\_samples\_report Struct Reference

`#include <[direction.h](direction_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [chan\_idx](#ad4d213aa20a0c2fe329606ed789436fd) |
|  | Channel index used to receive PDU with CTE that was sampled. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [rssi](#a48793aad0f603d1763f06453e837a9d9) |
|  | The RSSI of the PDU with CTE (excluding CTE). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rssi\_ant\_id](#a0b07042bad2a28065b8ea4def73c91d3) |
|  | Id of antenna used to measure the RSSI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#aa81e74769290f427b60398eb976b4a2a) |
|  | Type of CTE ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#ab256dc21c5d707a9195967caaa13e3e0) |
|  | Duration of slots when received CTE type is AoA ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_status](#a6fea28c1d3b00f1fd7bcb7264f4c3fc9) |
|  | Status of received PDU with CTE ([bt\_df\_packet\_status](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c "bt_df_packet_status")). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [per\_evt\_counter](#a1a9c763fa7dd445b5dea8c2bb7b82bc0) |
|  | Value of the paEventCounter of the AUX\_SYNC\_IND PDU. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sample\_count](#a4d1da7208e043f5ae015612cee16ee25) |
|  | Number of IQ samples in report. |
| enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) | [sample\_type](#a88d950cdaa4f08a0fa3eb26f1fed7982) |
|  | Type of IQ samples provided in a report. |
| union { |  |
| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) const \*   [sample](#a64c2936dc8180fc34651b18199241a9b) |  |
| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) const \*   [sample16](#ae0a28844a5588af05bbde046f6355ddf) |  |
| }; |  |
|  | Pointer to IQ samples data. |

## Field Documentation

## [◆ ](#a16a70bd3a0045227e6de26f86231243b)[union]

| union { ... } [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) |
| --- |

Pointer to IQ samples data.

## [◆ ](#ad4d213aa20a0c2fe329606ed789436fd)chan\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_iq\_samples\_report::chan\_idx |
| --- |

Channel index used to receive PDU with CTE that was sampled.

## [◆ ](#aa81e74769290f427b60398eb976b4a2a)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_iq\_samples\_report::cte\_type |
| --- |

Type of CTE ([bt\_df\_cte\_type](direction_8h.md#a64bf01dee8bc4bbc62e0dbc356726a05 "bt_df_cte_type")).

## [◆ ](#a6fea28c1d3b00f1fd7bcb7264f4c3fc9)packet\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_iq\_samples\_report::packet\_status |
| --- |

Status of received PDU with CTE ([bt\_df\_packet\_status](direction_8h.md#ab9acadbaf03dd976a2ee185574effb4c "bt_df_packet_status")).

## [◆ ](#a1a9c763fa7dd445b5dea8c2bb7b82bc0)per\_evt\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_df\_per\_adv\_sync\_iq\_samples\_report::per\_evt\_counter |
| --- |

Value of the paEventCounter of the AUX\_SYNC\_IND PDU.

## [◆ ](#a48793aad0f603d1763f06453e837a9d9)rssi

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_df\_per\_adv\_sync\_iq\_samples\_report::rssi |
| --- |

The RSSI of the PDU with CTE (excluding CTE).

Range: -1270 to +200. Units: 0.1 dBm.

## [◆ ](#a0b07042bad2a28065b8ea4def73c91d3)rssi\_ant\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_iq\_samples\_report::rssi\_ant\_id |
| --- |

Id of antenna used to measure the RSSI.

## [◆ ](#a64c2936dc8180fc34651b18199241a9b)sample

| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) const\* bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample |
| --- |

## [◆ ](#ae0a28844a5588af05bbde046f6355ddf)sample16

| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) const\* bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample16 |
| --- |

## [◆ ](#a4d1da7208e043f5ae015612cee16ee25)sample\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample\_count |
| --- |

Number of IQ samples in report.

## [◆ ](#a88d950cdaa4f08a0fa3eb26f1fed7982)sample\_type

| enum [bt\_df\_iq\_sample](direction_8h.md#a53df7da4b178b4a6e4dd68e9266c0771) bt\_df\_per\_adv\_sync\_iq\_samples\_report::sample\_type |
| --- |

Type of IQ samples provided in a report.

## [◆ ](#ab256dc21c5d707a9195967caaa13e3e0)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_df\_per\_adv\_sync\_iq\_samples\_report::slot\_durations |
| --- |

Duration of slots when received CTE type is AoA ([bt\_df\_antenna\_switching\_slot](direction_8h.md#a546598ce9a81161ad1ba098a7b1a8df4 "bt_df_antenna_switching_slot")).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[direction.h](direction_8h_source.md)

- [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
