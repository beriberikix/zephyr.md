---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__credentials__header.html
original_path: doxygen/html/structwifi__credentials__header.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_credentials\_header Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi credentials library](group__wifi__credentials.md)

Wi-Fi credentials entry header.
[More...](#details)

`#include <[wifi_credentials.h](wifi__credentials_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | [type](#a5b873555b2154e22367644c2805c0494) |
|  | Wi-Fi security type. |
| char | [ssid](#a172c0a2052146ce1748e7ab4e0aa076f) [32] |
|  | SSID (Service Set Identifier). |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [ssid\_len](#ab5bfa4ac972a8ad1ba4b395fad48a923) |
|  | Length of the SSID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a59b8b99ad309c0cc2cb6c5438554fefe) |
|  | Flags for controlling detail settings. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timeout](#ab6b02e3c88ff13a323cbafdf9af9ba1f) |
|  | Timeout for connecting to the network. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bssid](#a18d7796039bcdec0ce611a7f2dfe5c63) [6] |
|  | BSSID (Basic Service Set Identifier). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#a9ab939e7cb212a85d2612d5582e2336d) |
|  | Channel on which the network operates. |

## Detailed Description

Wi-Fi credentials entry header.

Note
:   Every settings entry starts with this header. Depending on the [type](#a5b873555b2154e22367644c2805c0494) field, the header can be casted to a larger type. In addition to SSID (usually a string) and BSSID (a MAC address), a [flags](#a59b8b99ad309c0cc2cb6c5438554fefe) field can be used to control some detail settings.

## Field Documentation

## [◆ ](#a18d7796039bcdec0ce611a7f2dfe5c63)bssid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_credentials\_header::bssid[6] |
| --- |

BSSID (Basic Service Set Identifier).

## [◆ ](#a9ab939e7cb212a85d2612d5582e2336d)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_credentials\_header::channel |
| --- |

Channel on which the network operates.

## [◆ ](#a59b8b99ad309c0cc2cb6c5438554fefe)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_credentials\_header::flags |
| --- |

Flags for controlling detail settings.

## [◆ ](#a172c0a2052146ce1748e7ab4e0aa076f)ssid

| char wifi\_credentials\_header::ssid[32] |
| --- |

SSID (Service Set Identifier).

## [◆ ](#ab5bfa4ac972a8ad1ba4b395fad48a923)ssid\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_header::ssid\_len |
| --- |

Length of the SSID.

## [◆ ](#ab6b02e3c88ff13a323cbafdf9af9ba1f)timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_credentials\_header::timeout |
| --- |

Timeout for connecting to the network.

## [◆ ](#a5b873555b2154e22367644c2805c0494)type

| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) wifi\_credentials\_header::type |
| --- |

Wi-Fi security type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_credentials.h](wifi__credentials_8h_source.md)

- [wifi\_credentials\_header](structwifi__credentials__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
