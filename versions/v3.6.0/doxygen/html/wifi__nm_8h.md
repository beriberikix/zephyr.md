---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/wifi__nm_8h.html
original_path: doxygen/html/wifi__nm_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_nm.h File Reference

Wi-Fi Network manager API.
[More...](#details)

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

[Go to the source code of this file.](wifi__nm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [wifi\_nm\_instance](structwifi__nm__instance.md) |
|  | WiFi Network manager instance. [More...](structwifi__nm__instance.md#details) |

| Macros | |
| --- | --- |
| #define | [WIFI\_NM\_NAME](group__wifi__nm.md#ga476afa0a50621396bc959d9cc7eca19f)(name) |
| #define | [DEFINE\_WIFI\_NM\_INSTANCE](group__wifi__nm.md#ga618fa06395943215db2fa96cbfa3fc99)(\_name, \_ops) |

| Functions | |
| --- | --- |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed) (const char \*name) |
|  | Get a Network manager instance for a given name. |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance\_iface](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a Network manager instance for a given interface. |
| int | [wifi\_nm\_register\_mgd\_iface](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
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
