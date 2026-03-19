---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ethernet__bridge_8h.html
original_path: doxygen/html/ethernet__bridge_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_bridge.h File Reference

Ethernet Bridge public header file.
[More...](#details)

`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](ethernet__bridge_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [eth\_bridge\_cb\_t](group__eth__bridge.md#gac7d0b995294279cc35408c69ee437778)) (struct eth\_bridge\_iface\_context \*br, void \*user\_data) |
|  | Callback used while iterating over bridge instances. |

| Functions | |
| --- | --- |
| int | [eth\_bridge\_iface\_add](group__eth__bridge.md#ga19756a715b210181001b04987a5e23a5) (struct [net\_if](structnet__if.md) \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Add an Ethernet network interface to a bridge. |
| int | [eth\_bridge\_iface\_remove](group__eth__bridge.md#ga671496bc299581b8d4d3ec9fd2ff1991) (struct [net\_if](structnet__if.md) \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Remove an Ethernet network interface from a bridge. |
| int | [eth\_bridge\_get\_index](group__eth__bridge.md#gafd194ba73599d0e37c8302e25d8208e4) (struct [net\_if](structnet__if.md) \*br) |
|  | Get bridge index according to pointer. |
| struct [net\_if](structnet__if.md) \* | [eth\_bridge\_get\_by\_index](group__eth__bridge.md#ga6b88a47138b199e65da602e0e63f13d1) (int index) |
|  | Get bridge instance according to index. |
| void | [net\_eth\_bridge\_foreach](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31) ([eth\_bridge\_cb\_t](group__eth__bridge.md#gac7d0b995294279cc35408c69ee437778) cb, void \*user\_data) |
|  | Go through all the bridge context instances in order to get information about them. |

## Detailed Description

Ethernet Bridge public header file.

Ethernet Bridges connect two or more Ethernet networks together and transparently forward packets from one network to the others as if they were part of the same network.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_bridge.h](ethernet__bridge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
