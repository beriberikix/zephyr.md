---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/igmp_8h.html
original_path: doxygen/html/igmp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

igmp.h File Reference

IGMP API.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`

[Go to the source code of this file.](igmp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [igmp\_param](structigmp__param.md) |
|  | IGMP parameters. [More...](structigmp__param.md#details) |

| Functions | |
| --- | --- |
| static int | [net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr, const struct [igmp\_param](structigmp__param.md) \*param) |
|  | Join a given multicast group. |
| static int | [net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Leave a given multicast group. |

## Detailed Description

IGMP API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [igmp.h](igmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
