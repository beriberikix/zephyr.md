---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structwifi__eap__config.html
original_path: doxygen/html/structwifi__eap__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_eap\_config Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

`#include <[wifi.h](wifi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | [type](#a031a5c86551f90130ff74ed53977c49d) |
|  | Security type. |
| enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) | [eap\_type\_phase1](#ab44893426c89416ab24e3bfb57bf49ad) |
|  | EAP method type of phase1. |
| enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) | [eap\_type\_phase2](#aaf73f2f986d56f95d196d02dcecbaff1) |
|  | EAP method type of phase2. |
| char \* | [method](#aa7a42a1256ef26562e83f47498d87113) |
|  | EAP method string. |
| char \* | [phase2](#abeed60cdf6c01751a4bb3c7ab67ea4e6) |
|  | Phase2 setting string. |

## Field Documentation

## [◆ ](#ab44893426c89416ab24e3bfb57bf49ad)eap\_type\_phase1

| enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) wifi\_eap\_config::eap\_type\_phase1 |
| --- |

EAP method type of phase1.

## [◆ ](#aaf73f2f986d56f95d196d02dcecbaff1)eap\_type\_phase2

| enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) wifi\_eap\_config::eap\_type\_phase2 |
| --- |

EAP method type of phase2.

## [◆ ](#aa7a42a1256ef26562e83f47498d87113)method

| char\* wifi\_eap\_config::method |
| --- |

EAP method string.

## [◆ ](#abeed60cdf6c01751a4bb3c7ab67ea4e6)phase2

| char\* wifi\_eap\_config::phase2 |
| --- |

Phase2 setting string.

## [◆ ](#a031a5c86551f90130ff74ed53977c49d)type

| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) wifi\_eap\_config::type |
| --- |

Security type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi.h](wifi_8h_source.md)

- [wifi\_eap\_config](structwifi__eap__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
