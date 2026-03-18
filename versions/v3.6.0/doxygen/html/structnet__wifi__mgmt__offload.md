---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__wifi__mgmt__offload.html
original_path: doxygen/html/structnet__wifi__mgmt__offload.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_wifi\_mgmt\_offload Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi management offload API.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [ethernet\_api](structethernet__api.md) | [wifi\_iface](#a1d34a954a2f16d29f51dc51dd6fbb845) |
|  | Mandatory to get in first position. |
| const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*const | [wifi\_mgmt\_api](#a98fcc053d9820d2d981ed659520c9b3b) |
|  | Wi-Fi management API. |
| void \* | [wifi\_drv\_ops](#a0b50b958d9d9bcba029a0859304dd84f) |
|  | Wi-Fi supplicant driver API. |

## Detailed Description

Wi-Fi management offload API.

## Field Documentation

## [◆ ](#a0b50b958d9d9bcba029a0859304dd84f)wifi\_drv\_ops

| void\* net\_wifi\_mgmt\_offload::wifi\_drv\_ops |
| --- |

Wi-Fi supplicant driver API.

## [◆ ](#a1d34a954a2f16d29f51dc51dd6fbb845)wifi\_iface

| struct [ethernet\_api](structethernet__api.md) net\_wifi\_mgmt\_offload::wifi\_iface |
| --- |

Mandatory to get in first position.

A network device should indeed provide a pointer on such net\_if\_api structure. So we make current structure pointer that can be casted to a net\_if\_api structure pointer. Ethernet API

## [◆ ](#a98fcc053d9820d2d981ed659520c9b3b)wifi\_mgmt\_api

| const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md)\* const net\_wifi\_mgmt\_offload::wifi\_mgmt\_api |
| --- |

Wi-Fi management API.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
