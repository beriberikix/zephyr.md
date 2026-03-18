---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structlorawan__join__config.html
original_path: doxygen/html/structlorawan__join__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lorawan\_join\_config Struct Reference

[Connectivity](group__connectivity.md) » [LoRaWAN APIs](group__lorawan__api.md)

LoRaWAN join parameters.
[More...](#details)

`#include <[lorawan.h](lorawan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [lorawan\_join\_otaa](structlorawan__join__otaa.md)   [otaa](#a7e2db9310308b59f652d72a3d7b3f7ff) |  |
|  | OTAA join parameters. [More...](#a7e2db9310308b59f652d72a3d7b3f7ff) |
| struct [lorawan\_join\_abp](structlorawan__join__abp.md)   [abp](#a0b44703df9ebe466ccf1d7744138daee) |  |
|  | ABP join parameters. [More...](#a0b44703df9ebe466ccf1d7744138daee) |
| }; |  |
|  | Join parameters. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [dev\_eui](#af5c973ed774255858b2219f737a3fe0a) |
|  | Device EUI. |
| enum [lorawan\_act\_type](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338) | [mode](#a9dbe39641f878e4c997a16711fdb5585) |
|  | Activation mode. |

## Detailed Description

LoRaWAN join parameters.

## Field Documentation

## [◆ ](#ab359c2a358c27c620d40ed92559d13da)[union]

| union { ... } [lorawan\_join\_config](structlorawan__join__config.md) |
| --- |

Join parameters.

## [◆ ](#a0b44703df9ebe466ccf1d7744138daee)abp

| struct [lorawan\_join\_abp](structlorawan__join__abp.md) lorawan\_join\_config::abp |
| --- |

ABP join parameters.

## [◆ ](#af5c973ed774255858b2219f737a3fe0a)dev\_eui

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_config::dev\_eui |
| --- |

Device EUI.

Optional if a secure element is present.

## [◆ ](#a9dbe39641f878e4c997a16711fdb5585)mode

| enum [lorawan\_act\_type](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338) lorawan\_join\_config::mode |
| --- |

Activation mode.

## [◆ ](#a7e2db9310308b59f652d72a3d7b3f7ff)otaa

| struct [lorawan\_join\_otaa](structlorawan__join__otaa.md) lorawan\_join\_config::otaa |
| --- |

OTAA join parameters.

---

The documentation for this struct was generated from the following file:

- zephyr/lorawan/[lorawan.h](lorawan_8h_source.md)

- [lorawan\_join\_config](structlorawan__join__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
