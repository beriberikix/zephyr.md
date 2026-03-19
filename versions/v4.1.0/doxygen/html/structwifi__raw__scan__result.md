---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structwifi__raw__scan__result.html
original_path: doxygen/html/structwifi__raw__scan__result.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_raw\_scan\_result Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi raw scan result.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a3f08580c6448a5fa28dd8a594fa7dad6) |
|  | RSSI. |
| int | [frame\_length](#a876966f469714eb481b42ccc8a63945c) |
|  | Frame length. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [frequency](#aa2c7781882c6775616cbc8016b0842f6) |
|  | Frequency. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a5710e89199c147ce898602795f00aba3) [CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH] |
|  | Raw scan data. |

## Detailed Description

Wi-Fi raw scan result.

## Field Documentation

## [◆ ](#a5710e89199c147ce898602795f00aba3)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_raw\_scan\_result::data[CONFIG\_WIFI\_MGMT\_RAW\_SCAN\_RESULT\_LENGTH] |
| --- |

Raw scan data.

## [◆ ](#a876966f469714eb481b42ccc8a63945c)frame\_length

| int wifi\_raw\_scan\_result::frame\_length |
| --- |

Frame length.

## [◆ ](#aa2c7781882c6775616cbc8016b0842f6)frequency

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_raw\_scan\_result::frequency |
| --- |

Frequency.

## [◆ ](#a3f08580c6448a5fa28dd8a594fa7dad6)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) wifi\_raw\_scan\_result::rssi |
| --- |

RSSI.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
