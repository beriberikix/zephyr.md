---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__filter__info.html
original_path: doxygen/html/structwifi__filter__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_filter\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [filter](#ad9560be814299055cfa11b995a7dcf42) |
|  | Filter setting. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [if\_index](#af9ea91e31e78afcb7ffe1ff9a04277a3) |
|  | Interface index. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [buffer\_size](#a1b2d0448fc7f62654e3f5aacfba62f8f) |
|  | Filter buffer size. |
| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) | [oper](#aedd5e220cdde5768cb0f4aff920971cd) |
|  | Get or set operation. |

## Detailed Description

Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes.

## Field Documentation

## [◆ ](#a1b2d0448fc7f62654e3f5aacfba62f8f)buffer\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_filter\_info::buffer\_size |
| --- |

Filter buffer size.

## [◆ ](#ad9560be814299055cfa11b995a7dcf42)filter

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_filter\_info::filter |
| --- |

Filter setting.

## [◆ ](#af9ea91e31e78afcb7ffe1ff9a04277a3)if\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_filter\_info::if\_index |
| --- |

Interface index.

## [◆ ](#aedd5e220cdde5768cb0f4aff920971cd)oper

| enum [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) wifi\_filter\_info::oper |
| --- |

Get or set operation.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_filter\_info](structwifi__filter__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
