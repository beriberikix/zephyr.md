---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structwifi__reg__domain.html
original_path: doxygen/html/structwifi__reg__domain.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_reg\_domain Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Regulatory domain information or configuration.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) | [oper](#a3bbfdf1497a87bbb6b6211c7035e1002) |
|  | Regulatory domain operation. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [force](#a567c6fcae8032567aea83c18cd211c33) |
|  | Ignore all other regulatory hints over this one, the behavior is implementation specific. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [country\_code](#abf191495814c227fbbfaccb2f727762e) [[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)] |
|  | Country code: ISO/IEC 3166-1 alpha-2. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [num\_channels](#a3278e9f43893f49ab9f9d0d7f24009c1) |
|  | Number of channels supported. |
| struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) \* | [chan\_info](#a4c8c9c11e41123cd7738fdb0d33ae5fb) |
|  | Channels information. |

## Detailed Description

Regulatory domain information or configuration.

## Field Documentation

## [◆ ](#a4c8c9c11e41123cd7738fdb0d33ae5fb)chan\_info

| struct [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)\* wifi\_reg\_domain::chan\_info |
| --- |

Channels information.

## [◆ ](#abf191495814c227fbbfaccb2f727762e)country\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_reg\_domain::country\_code[[WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)] |
| --- |

Country code: ISO/IEC 3166-1 alpha-2.

## [◆ ](#a567c6fcae8032567aea83c18cd211c33)force

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_reg\_domain::force |
| --- |

Ignore all other regulatory hints over this one, the behavior is implementation specific.

## [◆ ](#a3278e9f43893f49ab9f9d0d7f24009c1)num\_channels

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int wifi\_reg\_domain::num\_channels |
| --- |

Number of channels supported.

## [◆ ](#a3bbfdf1497a87bbb6b6211c7035e1002)oper

| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) wifi\_reg\_domain::oper |
| --- |

Regulatory domain operation.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_reg\_domain](structwifi__reg__domain.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
