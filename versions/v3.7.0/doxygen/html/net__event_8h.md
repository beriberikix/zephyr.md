---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__event_8h.html
original_path: doxygen/html/net__event_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event.h File Reference

Network Events code public header.
[More...](#details)

`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/hostname.h](hostname_8h_source.md)>`

[Go to the source code of this file.](net__event_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ADDR\_ADD, NET\_EVENT\_IPV6\_ADDR\_DEL, NET\_EVENT\_IPV6\_MADDR\_ADD and NET\_EVENT\_IPV6\_MADDR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__addr.md#details) |
| struct | [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_NBR\_ADD and NET\_EVENT\_IPV6\_NBR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__nbr.md#details) |
| struct | [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ROUTE\_ADD and NET\_EVENT\_IPV6\_ROUTE\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__route.md#details) |
| struct | [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PREFIX\_ADD and NET\_EVENT\_IPV6\_PREFIX\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__ipv6__prefix.md#details) |
| struct | [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) |
|  | Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED event when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__l4__hostname.md#details) |
| struct | [net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PE\_FILTER\_ADD and NET\_EVENT\_IPV6\_PE\_FILTER\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__ipv6__pe__filter.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_EVENT\_IF\_DOWN](group__net__mgmt.md#gac43a928bce3feb217b37ff7eb205e71b)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN) |
|  | Event emitted when the network interface goes down. |
| #define | [NET\_EVENT\_IF\_UP](group__net__mgmt.md#gaddc84a60607bb27048397e29eb9107f5)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP) |
|  | Event emitted when the network interface goes up. |
| #define | [NET\_EVENT\_IF\_ADMIN\_DOWN](group__net__mgmt.md#gacb6ac7a4579be883abc9aa638299b0cd)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN) |
|  | Event emitted when the network interface is taken down manually. |
| #define | [NET\_EVENT\_IF\_ADMIN\_UP](group__net__mgmt.md#ga94a52eb94cc2189919ade9c8c8f239bd)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP) |
|  | Event emitted when the network interface goes up manually. |
| #define | [NET\_EVENT\_IPV6\_ADDR\_ADD](group__net__mgmt.md#ga20125c6148169a91fbebab1ebba17be3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD) |
|  | Event emitted when an IPv6 address is added to the system. |
| #define | [NET\_EVENT\_IPV6\_ADDR\_DEL](group__net__mgmt.md#ga61f243efbc25928815ec78305b4f000e)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL) |
|  | Event emitted when an IPv6 address is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_MADDR\_ADD](group__net__mgmt.md#gadda9dccf913a4dcb4d12b2b1fe5d403c)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD) |
|  | Event emitted when an IPv6 multicast address is added to the system. |
| #define | [NET\_EVENT\_IPV6\_MADDR\_DEL](group__net__mgmt.md#ga035db32f66effd2407e0cca4b1fd9ea3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL) |
|  | Event emitted when an IPv6 multicast address is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_PREFIX\_ADD](group__net__mgmt.md#ga392414b95838bca1e55e4342870a8333)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD) |
|  | Event emitted when an IPv6 prefix is added to the system. |
| #define | [NET\_EVENT\_IPV6\_PREFIX\_DEL](group__net__mgmt.md#gab06f93335938a635966e85a18b5b0cf6)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL) |
|  | Event emitted when an IPv6 prefix is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_MCAST\_JOIN](group__net__mgmt.md#ga287d37bae2d74e0c85de59c5e23d409a)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN) |
|  | Event emitted when an IPv6 multicast group is joined. |
| #define | [NET\_EVENT\_IPV6\_MCAST\_LEAVE](group__net__mgmt.md#ga862d1b2ce9b65c0806ef77909364a58d)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE) |
|  | Event emitted when an IPv6 multicast group is left. |
| #define | [NET\_EVENT\_IPV6\_ROUTER\_ADD](group__net__mgmt.md#gaae932293528aa40127a906c3dbd45e31)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD) |
|  | Event emitted when an IPv6 router is added to the system. |
| #define | [NET\_EVENT\_IPV6\_ROUTER\_DEL](group__net__mgmt.md#ga8d4b7798981aaaf3aea2b793739143b7)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL) |
|  | Event emitted when an IPv6 router is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_ROUTE\_ADD](group__net__mgmt.md#gad19b5e742ded9b3ed673d8f7985100fd)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD) |
|  | Event emitted when an IPv6 route is added to the system. |
| #define | [NET\_EVENT\_IPV6\_ROUTE\_DEL](group__net__mgmt.md#gae6f68ec69032ac049f072d6ed164987c)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL) |
|  | Event emitted when an IPv6 route is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_DAD\_SUCCEED](group__net__mgmt.md#ga8711b4b1e88c897196b982e4d56968f1)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED) |
|  | Event emitted when an IPv6 duplicate address detection succeeds. |
| #define | [NET\_EVENT\_IPV6\_DAD\_FAILED](group__net__mgmt.md#ga0d5013ea3a6fa3bddd5cb182dd616151)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED) |
|  | Event emitted when an IPv6 duplicate address detection fails. |
| #define | [NET\_EVENT\_IPV6\_NBR\_ADD](group__net__mgmt.md#ga96fe7da048fe4d59435b7337626d4af7)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD) |
|  | Event emitted when an IPv6 neighbor is added to the system. |
| #define | [NET\_EVENT\_IPV6\_NBR\_DEL](group__net__mgmt.md#ga5be1cdfeb1b8da485b1042a7b2dc14e4)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL) |
|  | Event emitted when an IPv6 neighbor is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_DHCP\_START](group__net__mgmt.md#gaa07a5e8779ec24e5ab883970bcec6c5e)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START) |
|  | Event emitted when an IPv6 DHCP client starts. |
| #define | [NET\_EVENT\_IPV6\_DHCP\_BOUND](group__net__mgmt.md#gaff89dbc7562a85e9ff073b507bdf06e3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND) |
|  | Event emitted when an IPv6 DHCP client address is bound. |
| #define | [NET\_EVENT\_IPV6\_DHCP\_STOP](group__net__mgmt.md#gaab05d5a65ef5f9ed147e32ce380f7de4)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP) |
|  | Event emitted when an IPv6 DHCP client is stopped. |
| #define | [NET\_EVENT\_IPV6\_ADDR\_DEPRECATED](group__net__mgmt.md#ga6cc42e3ca8197e46809de6082602ab98)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED) |
|  | IPv6 address is deprecated. |
| #define | [NET\_EVENT\_IPV6\_PE\_ENABLED](group__net__mgmt.md#ga95f7a737a39fb655d3577405e70e04ba)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED) |
|  | IPv6 Privacy extension is enabled. |
| #define | [NET\_EVENT\_IPV6\_PE\_DISABLED](group__net__mgmt.md#gaba20579e42c4cebc8c3ac9a40ff384f3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED) |
|  | IPv6 Privacy extension is disabled. |
| #define | [NET\_EVENT\_IPV6\_PE\_FILTER\_ADD](group__net__mgmt.md#ga19d671971cf07e76580db8098ab32971)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD) |
|  | IPv6 Privacy extension filter is added. |
| #define | [NET\_EVENT\_IPV6\_PE\_FILTER\_DEL](group__net__mgmt.md#gaf2f1c4b8dc5b9b07985265cee6a90f70)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL) |
|  | IPv6 Privacy extension filter is removed. |
| #define | [NET\_EVENT\_IPV4\_ADDR\_ADD](group__net__mgmt.md#gad422365df617ce1473412908738048f0)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD) |
|  | Event emitted when an IPv4 address is added to the system. |
| #define | [NET\_EVENT\_IPV4\_ADDR\_DEL](group__net__mgmt.md#ga0d78644f799d1d8f5c18ec9860582817)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL) |
|  | Event emitted when an IPv4 address is removed from the system. |
| #define | [NET\_EVENT\_IPV4\_MADDR\_ADD](group__net__mgmt.md#ga854e897d09eecccc83d04d86fbba5b64)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD) |
|  | Event emitted when an IPv4 multicast address is added to the system. |
| #define | [NET\_EVENT\_IPV4\_MADDR\_DEL](group__net__mgmt.md#ga303824277664ee64674b7c93ff865bb4)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL) |
|  | Event emitted when an IPv4 multicast address is removed from the system. |
| #define | [NET\_EVENT\_IPV4\_ROUTER\_ADD](group__net__mgmt.md#ga740c97a7e94181ad734888bbe7b0a3d0)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD) |
|  | Event emitted when an IPv4 router is added to the system. |
| #define | [NET\_EVENT\_IPV4\_ROUTER\_DEL](group__net__mgmt.md#gae45a3b6a5f4b72edc51e06a22b88239a)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL) |
|  | Event emitted when an IPv4 router is removed from the system. |
| #define | [NET\_EVENT\_IPV4\_DHCP\_START](group__net__mgmt.md#ga2d3a9351c226b1542d1b2f469b77233a)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START) |
|  | Event emitted when an IPv4 DHCP client is started. |
| #define | [NET\_EVENT\_IPV4\_DHCP\_BOUND](group__net__mgmt.md#ga7461ef85f4f8433851cb7583468c00cb)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND) |
|  | Event emitted when an IPv4 DHCP client address is bound. |
| #define | [NET\_EVENT\_IPV4\_DHCP\_STOP](group__net__mgmt.md#gabc06b6010780ab2d1e4f88227965b4e7)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP) |
|  | Event emitted when an IPv4 DHCP client is stopped. |
| #define | [NET\_EVENT\_IPV4\_MCAST\_JOIN](group__net__mgmt.md#ga17ad57d81f3046555f94f75dc6d31ec1)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN) |
|  | Event emitted when an IPv4 multicast group is joined. |
| #define | [NET\_EVENT\_IPV4\_MCAST\_LEAVE](group__net__mgmt.md#ga3cbb8a9dfec8435b93d908171ab944c9)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE) |
|  | Event emitted when an IPv4 multicast group is left. |
| #define | [NET\_EVENT\_IPV4\_ACD\_SUCCEED](group__net__mgmt.md#ga5293377de1fdc79e7564f4e5104a07c2)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED) |
|  | Event emitted when an IPv4 address conflict detection succeeds. |
| #define | [NET\_EVENT\_IPV4\_ACD\_FAILED](group__net__mgmt.md#ga3de741f5732473a1f49d9d0b93183549)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED) |
|  | Event emitted when an IPv4 address conflict detection fails. |
| #define | [NET\_EVENT\_IPV4\_ACD\_CONFLICT](group__net__mgmt.md#ga9af1f8f4ba965e6d6e82a190ab4748a1)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT) |
|  | Event emitted when an IPv4 address conflict was detected after the address was confirmed as safe to use. |
| #define | [NET\_EVENT\_L4\_CONNECTED](group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED) |
|  | Event emitted when the system is considered to be connected. |
| #define | [NET\_EVENT\_L4\_DISCONNECTED](group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED) |
|  | Event emitted when the system is no longer connected. |
| #define | [NET\_EVENT\_L4\_IPV4\_CONNECTED](group__net__mgmt.md#ga532fdc2f199e047a5d17e325cee12cf1)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED) |
|  | Event raised when IPv4 network connectivity is available. |
| #define | [NET\_EVENT\_L4\_IPV4\_DISCONNECTED](group__net__mgmt.md#gaa92cc806d93446d548a05edb8e0074c2)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED) |
|  | Event emitted when IPv4 network connectivity is lost. |
| #define | [NET\_EVENT\_L4\_IPV6\_CONNECTED](group__net__mgmt.md#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED) |
|  | Event emitted when IPv6 network connectivity is available. |
| #define | [NET\_EVENT\_L4\_IPV6\_DISCONNECTED](group__net__mgmt.md#gac81abeab44fbf2b6f29d4e11a1e1bd17)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED) |
|  | Event emitted when IPv6 network connectivity is lost. |
| #define | [NET\_EVENT\_DNS\_SERVER\_ADD](group__net__mgmt.md#ga5735d13f24c974ad6d4038c93edf05e0)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD) |
|  | Event emitted when a DNS server is added to the system. |
| #define | [NET\_EVENT\_DNS\_SERVER\_DEL](group__net__mgmt.md#ga9d406772e5d1ad2952b2a2e0fed05c73)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL) |
|  | Event emitted when a DNS server is removed from the system. |
| #define | [NET\_EVENT\_HOSTNAME\_CHANGED](group__net__mgmt.md#gac5a7458d89e4a95564999dca3c1b9f1e)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED) |
|  | Event emitted when the system hostname is changed. |
| #define | [NET\_EVENT\_CAPTURE\_STARTED](group__net__mgmt.md#gaa89b82a1890c55775f8c3c24e11f40e2)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED) |
|  | Network packet capture is started. |
| #define | [NET\_EVENT\_CAPTURE\_STOPPED](group__net__mgmt.md#gaa2b655aedd597636790409539b1f86cd)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED) |
|  | Network packet capture is stopped. |

## Detailed Description

Network Events code public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_event.h](net__event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
