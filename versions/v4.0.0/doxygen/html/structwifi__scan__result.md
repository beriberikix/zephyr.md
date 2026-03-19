---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__scan__result.html
original_path: doxygen/html/structwifi__scan__result.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_scan\_result Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi scan result, each result is provided to the [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") via its info attribute (see [net\_mgmt.h](net__mgmt_8h.md "Network Management API public header.")).
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ssid](#aaefb8f5c9510e4f5002ae306d853ade8) [[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)+1] |
|  | SSID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ssid\_length](#a2c1c2f4265b914df08fc75deb8b69d39) |
|  | SSID length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [band](#a38201c9dd798dc11b5bda3ce97b02e92) |
|  | Frequency band. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#adbbfd7692ee5ffd6344fe78b9d91c840) |
|  | Channel. |
| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | [security](#af2d3dc5d115e3db76d3bc115510b0a5a) |
|  | Security type. |
| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) | [mfp](#acaa3fb30ebf6df22bfac6380698ed28e) |
|  | MFP options. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a76aa012136e3721fd4a482a22b93546f) |
|  | RSSI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mac](#a4fdbc4dc4d5c8b279223e8c06624f434) [[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)] |
|  | BSSID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mac\_length](#a8fca0dabec00ebd7ed4800098ec9d451) |
|  | BSSID length. |

## Detailed Description

Wi-Fi scan result, each result is provided to the [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") via its info attribute (see [net\_mgmt.h](net__mgmt_8h.md "Network Management API public header.")).

## Field Documentation

## [◆ ](#a38201c9dd798dc11b5bda3ce97b02e92)band

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_result::band |
| --- |

Frequency band.

## [◆ ](#adbbfd7692ee5ffd6344fe78b9d91c840)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_result::channel |
| --- |

Channel.

## [◆ ](#a4fdbc4dc4d5c8b279223e8c06624f434)mac

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_result::mac[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)] |
| --- |

BSSID.

## [◆ ](#a8fca0dabec00ebd7ed4800098ec9d451)mac\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_result::mac\_length |
| --- |

BSSID length.

## [◆ ](#acaa3fb30ebf6df22bfac6380698ed28e)mfp

| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) wifi\_scan\_result::mfp |
| --- |

MFP options.

## [◆ ](#a76aa012136e3721fd4a482a22b93546f)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) wifi\_scan\_result::rssi |
| --- |

RSSI.

## [◆ ](#af2d3dc5d115e3db76d3bc115510b0a5a)security

| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) wifi\_scan\_result::security |
| --- |

Security type.

## [◆ ](#aaefb8f5c9510e4f5002ae306d853ade8)ssid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_result::ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)+1] |
| --- |

SSID.

## [◆ ](#a2c1c2f4265b914df08fc75deb8b69d39)ssid\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_scan\_result::ssid\_length |
| --- |

SSID length.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_scan\_result](structwifi__scan__result.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
