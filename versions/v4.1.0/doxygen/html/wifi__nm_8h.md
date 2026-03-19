---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wifi__nm_8h.html
original_path: doxygen/html/wifi__nm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_nm.h File Reference

Wi-Fi Network manager API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

[Go to the source code of this file.](wifi__nm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md) |
|  | WiFi Network Managed interfaces. [More...](structwifi__nm__mgd__iface.md#details) |
| struct | [wifi\_nm\_instance](structwifi__nm__instance.md) |
|  | WiFi Network manager instance. [More...](structwifi__nm__instance.md#details) |

| Enumerations | |
| --- | --- |
| enum | [wifi\_nm\_iface\_type](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1) { [WIFI\_TYPE\_STA](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468) = 0 , [WIFI\_TYPE\_SAP](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345) } |
|  | Types of Wi-Fi interface. [More...](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1) |

| Functions | |
| --- | --- |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed) (const char \*name) |
|  | Get a Network manager instance for a given name. |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance\_iface](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a Network manager instance for a given interface. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [wifi\_nm\_get\_type\_iface](group__wifi__nm.md#ga6a598af94e36a1f4ade05d7a18c019f5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a Wi-Fi type for a given interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_nm\_iface\_is\_sta](group__wifi__nm.md#gaa89e5acfa5eebc9267aa7ed2ce3adc39) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the interface is a Wi-Fi station interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_nm\_iface\_is\_sap](group__wifi__nm.md#ga963f646981e9a64c9e61659e40c9880e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the interface is a Wi-Fi Soft AP interface. |
| int | [wifi\_nm\_register\_mgd\_iface](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
|  | Register a managed interface. |
| int | [wifi\_nm\_register\_mgd\_type\_iface](group__wifi__nm.md#gafea087a6c50d6ad05933ef62546868d6) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, enum [wifi\_nm\_iface\_type](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1) type, struct [net\_if](structnet__if.md) \*iface) |
|  | Register a managed interface. |
| int | [wifi\_nm\_unregister\_mgd\_iface](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
|  | Unregister managed interface. |

## Detailed Description

Wi-Fi Network manager API.

This file contains the Wi-Fi network manager API. These APIs are used by the any network management application to register as a Wi-Fi network manager.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_nm.h](wifi__nm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
