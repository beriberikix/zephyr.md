---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dhcpv4__server_8h.html
original_path: doxygen/html/dhcpv4__server_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dhcpv4\_server.h File Reference

DHCPv4 Server API.
[More...](#details)

`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`

[Go to the source code of this file.](dhcpv4__server_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_dhcpv4\_lease\_cb\_t](group__dhcpv4__server.md#gabd37fd84bc25525d4f1aec4df8aef8b6)) (struct [net\_if](structnet__if.md) \*iface, struct dhcpv4\_addr\_slot \*lease, void \*user\_data) |
|  | Callback used while iterating over active DHCPv4 address leases. |
| typedef int(\* | [net\_dhcpv4\_server\_provider\_cb\_t](group__dhcpv4__server.md#ga416f4c6f173622d602aa122c5d3ca55e)) (struct [net\_if](structnet__if.md) \*iface, const struct dhcpv4\_client\_id \*client\_id, struct [in\_addr](structin__addr.md) \*addr, void \*user\_data) |
|  | Callback used to let application provide an address for a given client ID. |

| Functions | |
| --- | --- |
| int | [net\_dhcpv4\_server\_start](group__dhcpv4__server.md#ga2f3cc50c9428fe45540535fc66bec052) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*base\_addr) |
|  | Start DHCPv4 server instance on an iface. |
| int | [net\_dhcpv4\_server\_stop](group__dhcpv4__server.md#ga7955e5f3ff357c292a8641c0385f34e4) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop DHCPv4 server instance on an iface. |
| int | [net\_dhcpv4\_server\_foreach\_lease](group__dhcpv4__server.md#ga636b2c71a7d5f00997cba946c31c0c00) (struct [net\_if](structnet__if.md) \*iface, [net\_dhcpv4\_lease\_cb\_t](group__dhcpv4__server.md#gabd37fd84bc25525d4f1aec4df8aef8b6) cb, void \*user\_data) |
|  | Iterate over all DHCPv4 address leases on a given network interface and call callback for each lease. |
| void | [net\_dhcpv4\_server\_set\_provider\_cb](group__dhcpv4__server.md#ga1db06c0bf6a5f79334c81472b0a37bb7) ([net\_dhcpv4\_server\_provider\_cb\_t](group__dhcpv4__server.md#ga416f4c6f173622d602aa122c5d3ca55e) cb, void \*user\_data) |
|  | Set the callback used to provide addresses to the DHCP server. |

## Detailed Description

DHCPv4 Server API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv4\_server.h](dhcpv4__server_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
