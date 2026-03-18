---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structwifi__nm__mgd__iface.html
original_path: doxygen/html/structwifi__nm__mgd__iface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_nm\_mgd\_iface Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Network Manager API](group__wifi__nm.md)

WiFi Network Managed interfaces.
[More...](#details)

`#include <[wifi_nm.h](wifi__nm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [type](#adf401562151097f8be118fc609e7f86a) |
|  | Wi-Fi interface type. |
| struct [net\_if](structnet__if.md) \* | [iface](#abd10caf51a7890d24af51c91a58f1e4d) |
|  | Managed net interfaces. |

## Detailed Description

WiFi Network Managed interfaces.

## Field Documentation

## [◆ ](#abd10caf51a7890d24af51c91a58f1e4d)iface

| struct [net\_if](structnet__if.md)\* wifi\_nm\_mgd\_iface::iface |
| --- |

Managed net interfaces.

## [◆ ](#adf401562151097f8be118fc609e7f86a)type

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char wifi\_nm\_mgd\_iface::type |
| --- |

Wi-Fi interface type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_nm.h](wifi__nm_8h_source.md)

- [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
