---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structwifi__reg__chan__info.html
original_path: doxygen/html/structwifi__reg__chan__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_reg\_chan\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Per-channel regulatory attributes.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [center\_frequency](#a0addffc11ef29f50c01b700835e59930) |
|  | Center frequency in MHz. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [max\_power](#af9169ab4a41fac4c6f6766fc96799545):8 |
|  | Maximum transmission power (in dBm). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [supported](#aa044611e18b7332b8577e29f6a769e3f):1 |
|  | Is channel supported or not. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [passive\_only](#acc7a88b004c9a61c8bf9ee1a97f85928):1 |
|  | Passive transmissions only. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [dfs](#a1ab137c142902d2de7d6be2626d7ac1f):1 |
|  | Is a DFS channel. |

## Detailed Description

Per-channel regulatory attributes.

## Field Documentation

## [◆ ](#a0addffc11ef29f50c01b700835e59930)center\_frequency

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_reg\_chan\_info::center\_frequency |
| --- |

Center frequency in MHz.

## [◆ ](#a1ab137c142902d2de7d6be2626d7ac1f)dfs

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_reg\_chan\_info::dfs |
| --- |

Is a DFS channel.

## [◆ ](#af9169ab4a41fac4c6f6766fc96799545)max\_power

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_reg\_chan\_info::max\_power |
| --- |

Maximum transmission power (in dBm).

## [◆ ](#acc7a88b004c9a61c8bf9ee1a97f85928)passive\_only

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_reg\_chan\_info::passive\_only |
| --- |

Passive transmissions only.

## [◆ ](#aa044611e18b7332b8577e29f6a769e3f)supported

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_reg\_chan\_info::supported |
| --- |

Is channel supported or not.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
