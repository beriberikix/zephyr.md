---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dhcpv4_8h.html
original_path: doxygen/html/dhcpv4_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dhcpv4.h File Reference

DHCPv4 Client Handler.
[More...](#details)

`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](dhcpv4_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d)) (struct net\_dhcpv4\_option\_callback \*cb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type, struct [net\_if](structnet__if.md) \*iface) |
|  | Define the application callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) {     [NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) = 1 , [NET\_DHCPV4\_MSG\_TYPE\_OFFER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) = 2 , [NET\_DHCPV4\_MSG\_TYPE\_REQUEST](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) = 3 , [NET\_DHCPV4\_MSG\_TYPE\_DECLINE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) = 4 ,     [NET\_DHCPV4\_MSG\_TYPE\_ACK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) = 5 , [NET\_DHCPV4\_MSG\_TYPE\_NAK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) = 6 , [NET\_DHCPV4\_MSG\_TYPE\_RELEASE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) = 7 , [NET\_DHCPV4\_MSG\_TYPE\_INFORM](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) = 8   } |
|  | DHCPv4 message types. [More...](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) |

| Functions | |
| --- | --- |
| static void | [net\_dhcpv4\_init\_option\_callback](group__dhcpv4.md#ga84df76c84de248a43e3e26d422cdfc2f) (struct net\_dhcpv4\_option\_callback \*callback, [net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d) handler, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_length) |
|  | Helper to initialize a struct net\_dhcpv4\_option\_callback properly. |
| int | [net\_dhcpv4\_add\_option\_callback](group__dhcpv4.md#gaf073157fcd5cb2d18c40b8697d724a7c) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Add an application callback. |
| int | [net\_dhcpv4\_remove\_option\_callback](group__dhcpv4.md#gaa90c4ba8010bcd2079512afe5f288dbb) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Remove an application callback. |
| static void | [net\_dhcpv4\_init\_option\_vendor\_callback](group__dhcpv4.md#gaec0f1c87f5093767a4bb1c43b8e18e72) (struct net\_dhcpv4\_option\_callback \*callback, [net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d) handler, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_length) |
|  | Helper to initialize a struct net\_dhcpv4\_option\_callback for encapsulated vendor-specific options properly. |
| int | [net\_dhcpv4\_add\_option\_vendor\_callback](group__dhcpv4.md#gabf3d97139fc4f7122c1bdee52cb003cb) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Add an application callback for encapsulated vendor-specific options. |
| int | [net\_dhcpv4\_remove\_option\_vendor\_callback](group__dhcpv4.md#ga1f362cce448226447d892f5ed8401db5) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Remove an application callback for encapsulated vendor-specific options. |
| void | [net\_dhcpv4\_start](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start DHCPv4 client on an iface. |
| void | [net\_dhcpv4\_stop](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop DHCPv4 client on an iface. |
| void | [net\_dhcpv4\_restart](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Restart DHCPv4 client on an iface. |
| const char \* | [net\_dhcpv4\_msg\_type\_name](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c) (enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type) |
|  | Return a text representation of the msg\_type. |

## Detailed Description

DHCPv4 Client Handler.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv4.h](dhcpv4_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
