---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__ps__params.html
original_path: doxygen/html/structwifi__ps__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_ps\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi power save parameters.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) | [enabled](#abb22aaa45833ac130922204bd2fe841b) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [listen\_interval](#a8510c799ab0c5825f1c6349f9799c62f) |
| enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) | [wakeup\_mode](#a7cb3e7fb7d9f8bd7c2cab41f879b3b66) |
|  | Wi-Fi power save wakeup mode. |
| enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) | [mode](#a5a022d89d43ecf2cd1f15fc72c0f2bed) |
|  | Wi-Fi power save mode. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [timeout\_ms](#ad963f1bf78dc271f08b73f3aadb36a91) |
|  | Wi-Fi power save timeout. |
| enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) | [type](#aef62e5bf6216bf4dc461efe71735c4bd) |
|  | Wi-Fi power save type. |
| enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) | [fail\_reason](#a63fa2ee03bc4aefada61c298ee14336c) |
|  | Wi-Fi power save fail reason. |

## Detailed Description

Wi-Fi power save parameters.

## Field Documentation

## [◆ ](#abb22aaa45833ac130922204bd2fe841b)enabled

| enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) wifi\_ps\_params::enabled |
| --- |

## [◆ ](#a63fa2ee03bc4aefada61c298ee14336c)fail\_reason

| enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) wifi\_ps\_params::fail\_reason |
| --- |

Wi-Fi power save fail reason.

## [◆ ](#a8510c799ab0c5825f1c6349f9799c62f)listen\_interval

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_ps\_params::listen\_interval |
| --- |

## [◆ ](#a5a022d89d43ecf2cd1f15fc72c0f2bed)mode

| enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) wifi\_ps\_params::mode |
| --- |

Wi-Fi power save mode.

## [◆ ](#ad963f1bf78dc271f08b73f3aadb36a91)timeout\_ms

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int wifi\_ps\_params::timeout\_ms |
| --- |

Wi-Fi power save timeout.

This is the time out to wait after sending a TX packet before going back to power save (in ms) to receive any replies from the AP. Zero means this feature is disabled.

It's a tradeoff between power consumption and latency.

## [◆ ](#aef62e5bf6216bf4dc461efe71735c4bd)type

| enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) wifi\_ps\_params::type |
| --- |

Wi-Fi power save type.

## [◆ ](#a7cb3e7fb7d9f8bd7c2cab41f879b3b66)wakeup\_mode

| enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) wifi\_ps\_params::wakeup\_mode |
| --- |

Wi-Fi power save wakeup mode.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_ps\_params](structwifi__ps__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
