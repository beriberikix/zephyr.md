---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dhcpv6_8h.html
original_path: doxygen/html/dhcpv6_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dhcpv6.h File Reference

DHCPv6 client.
[More...](#details)

[Go to the source code of this file.](dhcpv6_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_dhcpv6\_params](structnet__dhcpv6__params.md) |
|  | DHCPv6 client configuration parameters. [More...](structnet__dhcpv6__params.md#details) |

| Functions | |
| --- | --- |
| void | [net\_dhcpv6\_start](group__dhcpv6.md#gab607a476c947d0335a254304e5dc2a24) (struct [net\_if](structnet__if.md) \*iface, struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) \*params) |
|  | Start DHCPv6 client on an iface. |
| void | [net\_dhcpv6\_stop](group__dhcpv6.md#gaf0b903bdcd0becf06ed6b212c74097a0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop DHCPv6 client on an iface. |
| void | [net\_dhcpv6\_restart](group__dhcpv6.md#ga99642b89c14cb17f35b45a03a2286441) (struct [net\_if](structnet__if.md) \*iface) |
|  | Restart DHCPv6 client on an iface. |

## Detailed Description

DHCPv6 client.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv6.h](dhcpv6_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
