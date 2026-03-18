---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__connect__req__params.html
original_path: doxygen/html/structwifi__connect__req__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_connect\_req\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi connect request parameters.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ssid](#ac260c2cd17a3f36ea101edaf23d41083) |
|  | SSID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ssid\_length](#a547dddf6be5dd77eda74b1085a798400) |
|  | SSID length. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [psk](#aa7743f0ecbc27a9595720ce13ce57c1d) |
|  | Pre-shared key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [psk\_length](#aaf7455a65590d19f047214b459a2dcb9) |
|  | Pre-shared key length. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [sae\_password](#a469fac5758b78fc425911837930b2060) |
|  | SAE password (same as PSK but with no length restrictions), optional. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sae\_password\_length](#a74f0819e7a546ffb8bfb0ec587eccf20) |
|  | SAE password length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [band](#aa2fea1881a8ffdf5d7093ae295867f3e) |
|  | Frequency band. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#a52b6d0323c35d03ec239f40be35cae72) |
|  | Channel. |
| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | [security](#a18dce6bb021086877a30e7a04f5b24b9) |
|  | Security type. |
| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) | [mfp](#a745b3416172672a7e5b12bcc5b55e88c) |
|  | MFP options. |
| int | [timeout](#a56183ba7f4d8eaf5fc5b495856adecfd) |
|  | Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout. |

## Detailed Description

Wi-Fi connect request parameters.

## Field Documentation

## [◆ ](#aa2fea1881a8ffdf5d7093ae295867f3e)band

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::band |
| --- |

Frequency band.

## [◆ ](#a52b6d0323c35d03ec239f40be35cae72)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::channel |
| --- |

Channel.

## [◆ ](#a745b3416172672a7e5b12bcc5b55e88c)mfp

| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) wifi\_connect\_req\_params::mfp |
| --- |

MFP options.

## [◆ ](#aa7743f0ecbc27a9595720ce13ce57c1d)psk

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::psk |
| --- |

Pre-shared key.

## [◆ ](#aaf7455a65590d19f047214b459a2dcb9)psk\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::psk\_length |
| --- |

Pre-shared key length.

## [◆ ](#a469fac5758b78fc425911837930b2060)sae\_password

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::sae\_password |
| --- |

SAE password (same as PSK but with no length restrictions), optional.

## [◆ ](#a74f0819e7a546ffb8bfb0ec587eccf20)sae\_password\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::sae\_password\_length |
| --- |

SAE password length.

## [◆ ](#a18dce6bb021086877a30e7a04f5b24b9)security

| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) wifi\_connect\_req\_params::security |
| --- |

Security type.

## [◆ ](#ac260c2cd17a3f36ea101edaf23d41083)ssid

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::ssid |
| --- |

SSID.

## [◆ ](#a547dddf6be5dd77eda74b1085a798400)ssid\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::ssid\_length |
| --- |

SSID length.

## [◆ ](#a56183ba7f4d8eaf5fc5b495856adecfd)timeout

| int wifi\_connect\_req\_params::timeout |
| --- |

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_connect\_req\_params](structwifi__connect__req__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
