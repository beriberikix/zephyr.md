---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/virtual_8h.html
original_path: doxygen/html/virtual_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtual.h File Reference

Virtual Network Interface.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](virtual_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [virtual\_interface\_api](structvirtual__interface__api.md) |
|  | Virtual L2 API operations. [More...](structvirtual__interface__api.md#details) |
| struct | [virtual\_interface\_context](structvirtual__interface__context.md) |
|  | Virtual L2 context that is needed to binding to the real network interface. [More...](structvirtual__interface__context.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_VIRTUAL\_INTERFACE\_INIT](group__virtual.md#ga74a5c258a08397f881a8922516ac5d3a)(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create a virtual network interface. |
| #define | [NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE](group__virtual.md#ga1846d4173bcd4b40a05b70c5fde18f91)(dev\_id, name, inst, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create a virtual network interface. |

| Enumerations | |
| --- | --- |
| enum | [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091) { [VIRTUAL\_INTERFACE\_IPIP](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071) = BIT(1) , [VIRTUAL\_INTERFACE\_VLAN](group__virtual.md#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b) = BIT(2) } |
|  | Virtual interface capabilities. [More...](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091) |

| Functions | |
| --- | --- |
| int | [net\_virtual\_interface\_attach](group__virtual.md#ga5cba6ff65402b591a0e42d05f258671f) (struct [net\_if](structnet__if.md) \*virtual\_iface, struct [net\_if](structnet__if.md) \*iface) |
|  | Attach virtual network interface to the given network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_virtual\_get\_iface](group__virtual.md#gabadf14eaa02978cde7030c99ddd3e279) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return network interface related to this virtual network interface. |
| char \* | [net\_virtual\_get\_name](group__virtual.md#gaa7ff8ebb83fe98a1dfd23f319317a8de) (struct [net\_if](structnet__if.md) \*iface, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Return the name of the virtual network interface L2. |
| void | [net\_virtual\_set\_name](group__virtual.md#ga2aaba616ed4fecc27138d5aae58a634f) (struct [net\_if](structnet__if.md) \*iface, const char \*name) |
|  | Set the name of the virtual network interface L2. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | [net\_virtual\_set\_flags](group__virtual.md#ga30f92f519a6f204ebeccd6053f17eaf0) (struct [net\_if](structnet__if.md) \*iface, enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set the L2 flags of the virtual network interface. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_virtual\_input](group__virtual.md#ga6c63773925ef7d96b0ba03d8978fd499) (struct [net\_if](structnet__if.md) \*input\_iface, struct net\_addr \*remote\_addr, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Feed the IP pkt to stack if tunneling is enabled. |

## Detailed Description

Virtual Network Interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [virtual.h](virtual_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
