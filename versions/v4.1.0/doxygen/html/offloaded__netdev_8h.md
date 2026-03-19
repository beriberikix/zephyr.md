---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/offloaded__netdev_8h.html
original_path: doxygen/html/offloaded__netdev_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

offloaded\_netdev.h File Reference

Offloaded network device iface API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](offloaded__netdev_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [offloaded\_if\_api](structoffloaded__if__api.md) |
|  | Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state changes. [More...](structoffloaded__if__api.md#details) |

| Enumerations | |
| --- | --- |
| enum | [offloaded\_net\_if\_types](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f) { [L2\_OFFLOADED\_NET\_IF\_TYPE\_UNKNOWN](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d) , [L2\_OFFLOADED\_NET\_IF\_TYPE\_ETHERNET](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a) , [L2\_OFFLOADED\_NET\_IF\_TYPE\_MODEM](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21) , [L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24) } |
|  | Types of offloaded netdev L2. [More...](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_off\_is\_wifi\_offloaded](group__offloaded__netdev.md#gad1076eacf1b1e82f70759f9b54937ced) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the offloaded network interface supports Wi-Fi. |

## Detailed Description

Offloaded network device iface API.

This is not to be included by the application.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [offloaded\_netdev.h](offloaded__netdev_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
