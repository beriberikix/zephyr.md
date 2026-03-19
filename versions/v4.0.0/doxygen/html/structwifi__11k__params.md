---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__11k__params.html
original_path: doxygen/html/structwifi__11k__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_11k\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi 11k parameters.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) | [oper](#ae6029ed4bada41f18df0329d0da7401e) |
|  | 11k command operation |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_11k](#a739c3e94b025aae2fcf5680aecf3d646) |
|  | 11k enable/disable |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ssid](#a64ace23c71837417678ceb9cc8d5f216) [[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)+1] |
|  | SSID. |

## Detailed Description

Wi-Fi 11k parameters.

## Field Documentation

## [◆ ](#a739c3e94b025aae2fcf5680aecf3d646)enable\_11k

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_11k\_params::enable\_11k |
| --- |

11k enable/disable

## [◆ ](#ae6029ed4bada41f18df0329d0da7401e)oper

| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) wifi\_11k\_params::oper |
| --- |

11k command operation

## [◆ ](#a64ace23c71837417678ceb9cc8d5f216)ssid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_11k\_params::ssid[[WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)+1] |
| --- |

SSID.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_11k\_params](structwifi__11k__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
