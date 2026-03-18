---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__net__mgmt.html
original_path: doxygen/html/group__net__mgmt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Management

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network Management.
[More...](#details)

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
| struct | [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) |
|  | Network Management event callback structure Used to register a callback into the network management event part, in order to let the owner of this struct to get network event notification based on given event mask. [More...](structnet__mgmt__event__callback.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_EVENT\_IF\_DOWN](#gac43a928bce3feb217b37ff7eb205e71b)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN) |
|  | Event emitted when the network interface goes down. |
| #define | [NET\_EVENT\_IF\_UP](#gaddc84a60607bb27048397e29eb9107f5)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP) |
|  | Event emitted when the network interface goes up. |
| #define | [NET\_EVENT\_IF\_ADMIN\_DOWN](#gacb6ac7a4579be883abc9aa638299b0cd)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN) |
|  | Event emitted when the network interface is taken down manually. |
| #define | [NET\_EVENT\_IF\_ADMIN\_UP](#ga94a52eb94cc2189919ade9c8c8f239bd)   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP) |
|  | Event emitted when the network interface goes up manually. |
| #define | [NET\_EVENT\_IPV6\_ADDR\_ADD](#ga20125c6148169a91fbebab1ebba17be3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD) |
|  | Event emitted when an IPv6 address is added to the system. |
| #define | [NET\_EVENT\_IPV6\_ADDR\_DEL](#ga61f243efbc25928815ec78305b4f000e)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL) |
|  | Event emitted when an IPv6 address is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_MADDR\_ADD](#gadda9dccf913a4dcb4d12b2b1fe5d403c)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD) |
|  | Event emitted when an IPv6 multicast address is added to the system. |
| #define | [NET\_EVENT\_IPV6\_MADDR\_DEL](#ga035db32f66effd2407e0cca4b1fd9ea3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL) |
|  | Event emitted when an IPv6 multicast address is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_PREFIX\_ADD](#ga392414b95838bca1e55e4342870a8333)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD) |
|  | Event emitted when an IPv6 prefix is added to the system. |
| #define | [NET\_EVENT\_IPV6\_PREFIX\_DEL](#gab06f93335938a635966e85a18b5b0cf6)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL) |
|  | Event emitted when an IPv6 prefix is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_MCAST\_JOIN](#ga287d37bae2d74e0c85de59c5e23d409a)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN) |
|  | Event emitted when an IPv6 multicast group is joined. |
| #define | [NET\_EVENT\_IPV6\_MCAST\_LEAVE](#ga862d1b2ce9b65c0806ef77909364a58d)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE) |
|  | Event emitted when an IPv6 multicast group is left. |
| #define | [NET\_EVENT\_IPV6\_ROUTER\_ADD](#gaae932293528aa40127a906c3dbd45e31)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD) |
|  | Event emitted when an IPv6 router is added to the system. |
| #define | [NET\_EVENT\_IPV6\_ROUTER\_DEL](#ga8d4b7798981aaaf3aea2b793739143b7)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL) |
|  | Event emitted when an IPv6 router is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_ROUTE\_ADD](#gad19b5e742ded9b3ed673d8f7985100fd)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD) |
|  | Event emitted when an IPv6 route is added to the system. |
| #define | [NET\_EVENT\_IPV6\_ROUTE\_DEL](#gae6f68ec69032ac049f072d6ed164987c)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL) |
|  | Event emitted when an IPv6 route is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_DAD\_SUCCEED](#ga8711b4b1e88c897196b982e4d56968f1)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED) |
|  | Event emitted when an IPv6 duplicate address detection succeeds. |
| #define | [NET\_EVENT\_IPV6\_DAD\_FAILED](#ga0d5013ea3a6fa3bddd5cb182dd616151)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED) |
|  | Event emitted when an IPv6 duplicate address detection fails. |
| #define | [NET\_EVENT\_IPV6\_NBR\_ADD](#ga96fe7da048fe4d59435b7337626d4af7)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD) |
|  | Event emitted when an IPv6 neighbor is added to the system. |
| #define | [NET\_EVENT\_IPV6\_NBR\_DEL](#ga5be1cdfeb1b8da485b1042a7b2dc14e4)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL) |
|  | Event emitted when an IPv6 neighbor is removed from the system. |
| #define | [NET\_EVENT\_IPV6\_DHCP\_START](#gaa07a5e8779ec24e5ab883970bcec6c5e)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START) |
|  | Event emitted when an IPv6 DHCP client starts. |
| #define | [NET\_EVENT\_IPV6\_DHCP\_BOUND](#gaff89dbc7562a85e9ff073b507bdf06e3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND) |
|  | Event emitted when an IPv6 DHCP client address is bound. |
| #define | [NET\_EVENT\_IPV6\_DHCP\_STOP](#gaab05d5a65ef5f9ed147e32ce380f7de4)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP) |
|  | Event emitted when an IPv6 DHCP client is stopped. |
| #define | [NET\_EVENT\_IPV6\_ADDR\_DEPRECATED](#ga6cc42e3ca8197e46809de6082602ab98)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED) |
|  | IPv6 address is deprecated. |
| #define | [NET\_EVENT\_IPV6\_PE\_ENABLED](#ga95f7a737a39fb655d3577405e70e04ba)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED) |
|  | IPv6 Privacy extension is enabled. |
| #define | [NET\_EVENT\_IPV6\_PE\_DISABLED](#gaba20579e42c4cebc8c3ac9a40ff384f3)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED) |
|  | IPv6 Privacy extension is disabled. |
| #define | [NET\_EVENT\_IPV6\_PE\_FILTER\_ADD](#ga19d671971cf07e76580db8098ab32971)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD) |
|  | IPv6 Privacy extension filter is added. |
| #define | [NET\_EVENT\_IPV6\_PE\_FILTER\_DEL](#gaf2f1c4b8dc5b9b07985265cee6a90f70)   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL) |
|  | IPv6 Privacy extension filter is removed. |
| #define | [NET\_EVENT\_IPV4\_ADDR\_ADD](#gad422365df617ce1473412908738048f0)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD) |
|  | Event emitted when an IPv4 address is added to the system. |
| #define | [NET\_EVENT\_IPV4\_ADDR\_DEL](#ga0d78644f799d1d8f5c18ec9860582817)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL) |
|  | Event emitted when an IPv4 address is removed from the system. |
| #define | [NET\_EVENT\_IPV4\_MADDR\_ADD](#ga854e897d09eecccc83d04d86fbba5b64)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD) |
|  | Event emitted when an IPv4 multicast address is added to the system. |
| #define | [NET\_EVENT\_IPV4\_MADDR\_DEL](#ga303824277664ee64674b7c93ff865bb4)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL) |
|  | Event emitted when an IPv4 multicast address is removed from the system. |
| #define | [NET\_EVENT\_IPV4\_ROUTER\_ADD](#ga740c97a7e94181ad734888bbe7b0a3d0)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD) |
|  | Event emitted when an IPv4 router is added to the system. |
| #define | [NET\_EVENT\_IPV4\_ROUTER\_DEL](#gae45a3b6a5f4b72edc51e06a22b88239a)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL) |
|  | Event emitted when an IPv4 router is removed from the system. |
| #define | [NET\_EVENT\_IPV4\_DHCP\_START](#ga2d3a9351c226b1542d1b2f469b77233a)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START) |
|  | Event emitted when an IPv4 DHCP client is started. |
| #define | [NET\_EVENT\_IPV4\_DHCP\_BOUND](#ga7461ef85f4f8433851cb7583468c00cb)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND) |
|  | Event emitted when an IPv4 DHCP client address is bound. |
| #define | [NET\_EVENT\_IPV4\_DHCP\_STOP](#gabc06b6010780ab2d1e4f88227965b4e7)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP) |
|  | Event emitted when an IPv4 DHCP client is stopped. |
| #define | [NET\_EVENT\_IPV4\_MCAST\_JOIN](#ga17ad57d81f3046555f94f75dc6d31ec1)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN) |
|  | Event emitted when an IPv4 multicast group is joined. |
| #define | [NET\_EVENT\_IPV4\_MCAST\_LEAVE](#ga3cbb8a9dfec8435b93d908171ab944c9)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE) |
|  | Event emitted when an IPv4 multicast group is left. |
| #define | [NET\_EVENT\_IPV4\_ACD\_SUCCEED](#ga5293377de1fdc79e7564f4e5104a07c2)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED) |
|  | Event emitted when an IPv4 address conflict detection succeeds. |
| #define | [NET\_EVENT\_IPV4\_ACD\_FAILED](#ga3de741f5732473a1f49d9d0b93183549)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED) |
|  | Event emitted when an IPv4 address conflict detection fails. |
| #define | [NET\_EVENT\_IPV4\_ACD\_CONFLICT](#ga9af1f8f4ba965e6d6e82a190ab4748a1)   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT) |
|  | Event emitted when an IPv4 address conflict was detected after the address was confirmed as safe to use. |
| #define | [NET\_EVENT\_L4\_CONNECTED](#gacbd2b10cc345359c07de4a62eb172a09)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED) |
|  | Event emitted when the system is considered to be connected. |
| #define | [NET\_EVENT\_L4\_DISCONNECTED](#gacd9e0b5e2f540794b20f11b070ffbd65)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED) |
|  | Event emitted when the system is no longer connected. |
| #define | [NET\_EVENT\_L4\_IPV4\_CONNECTED](#ga532fdc2f199e047a5d17e325cee12cf1)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED) |
|  | Event raised when IPv4 network connectivity is available. |
| #define | [NET\_EVENT\_L4\_IPV4\_DISCONNECTED](#gaa92cc806d93446d548a05edb8e0074c2)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED) |
|  | Event emitted when IPv4 network connectivity is lost. |
| #define | [NET\_EVENT\_L4\_IPV6\_CONNECTED](#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED) |
|  | Event emitted when IPv6 network connectivity is available. |
| #define | [NET\_EVENT\_L4\_IPV6\_DISCONNECTED](#gac81abeab44fbf2b6f29d4e11a1e1bd17)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED) |
|  | Event emitted when IPv6 network connectivity is lost. |
| #define | [NET\_EVENT\_DNS\_SERVER\_ADD](#ga5735d13f24c974ad6d4038c93edf05e0)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD) |
|  | Event emitted when a DNS server is added to the system. |
| #define | [NET\_EVENT\_DNS\_SERVER\_DEL](#ga9d406772e5d1ad2952b2a2e0fed05c73)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL) |
|  | Event emitted when a DNS server is removed from the system. |
| #define | [NET\_EVENT\_HOSTNAME\_CHANGED](#gac5a7458d89e4a95564999dca3c1b9f1e)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED) |
|  | Event emitted when the system hostname is changed. |
| #define | [NET\_EVENT\_CAPTURE\_STARTED](#gaa89b82a1890c55775f8c3c24e11f40e2)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED) |
|  | Network packet capture is started. |
| #define | [NET\_EVENT\_CAPTURE\_STOPPED](#gaa2b655aedd597636790409539b1f86cd)   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED) |
|  | Network packet capture is stopped. |
| #define | [net\_mgmt](#ga40e0f9fc86812ad9f6fe174b4c3804e6)(\_mgmt\_request, \_iface, \_data, \_len) |
|  | Generate a network management event. |
| #define | [NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](#ga08bde8717fd8e12a338c517b22b87776)(\_mgmt\_request) |
|  | Declare a request handler function for the given network event. |
| #define | [NET\_MGMT\_REGISTER\_REQUEST\_HANDLER](#gab67d09d1e65b806ec1957451cbf60501)(\_mgmt\_request, \_func) |
|  | Create a request handler function for the given network event. |
| #define | [NET\_MGMT\_REGISTER\_EVENT\_HANDLER](#ga3a6ca8a72ab12afd4f9b0461253eaa12)(\_name, \_event\_mask, \_func, \_user\_data) |
|  | Define a static network event handler. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_mgmt\_request\_handler\_t](#gae288951a34f7810c291986046ebe4056)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, struct [net\_if](structnet__if.md) \*iface, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Signature which all Net MGMT request handler need to follow. |
| typedef void(\* | [net\_mgmt\_event\_handler\_t](#gadb876a681fe7f5fb6d2709015625a67f)) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Define the user's callback handler function signature. |
| typedef void(\* | [net\_mgmt\_event\_static\_handler\_t](#ga14c81781b5bb1e6675e78a249a69357c)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) info\_length, void \*user\_data) |
|  | Define the user's callback handler function signature. |

| Functions | |
| --- | --- |
| static void | [net\_mgmt\_init\_event\_callback](#gaa1d086dcdeb54412073e287129bc50e0) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [net\_mgmt\_event\_handler\_t](#gadb876a681fe7f5fb6d2709015625a67f) handler, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask) |
|  | Helper to initialize a struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") properly. |
| void | [net\_mgmt\_add\_event\_callback](#gae53f5bbc973b0f414107eca75ac0c26f) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Add a user callback. |
| void | [net\_mgmt\_del\_event\_callback](#ga4960bfb01ecd891da72c57f17587f946) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Delete a user callback. |
| void | [net\_mgmt\_event\_notify\_with\_info](#ga10882f80c53400b94401a2a08d31697d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, const void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Used by the system to notify an event. |
| static void | [net\_mgmt\_event\_notify](#ga0648b82762467395b98a3bc13ab451d0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Used by the system to notify an event without any additional information. |
| int | [net\_mgmt\_event\_wait](#gacbaa95c65717747d802dc80eb745aa17) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event, struct [net\_if](structnet__if.md) \*\*iface, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask. |
| int | [net\_mgmt\_event\_wait\_on\_iface](#ga03c39d5f2af3f2d7a633513fb5ec8a7d) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask for a specific iface. |
| void | [net\_mgmt\_event\_init](#gaab4fe2e9ea0657bf91fb1910af6729cc) (void) |
|  | Used by the core of the network stack to initialize the network event processing. |

## Detailed Description

Network Management.

## Macro Definition Documentation

## [◆ ](#gaa89b82a1890c55775f8c3c24e11f40e2)NET\_EVENT\_CAPTURE\_STARTED

| #define NET\_EVENT\_CAPTURE\_STARTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Network packet capture is started.

## [◆ ](#gaa2b655aedd597636790409539b1f86cd)NET\_EVENT\_CAPTURE\_STOPPED

| #define NET\_EVENT\_CAPTURE\_STOPPED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Network packet capture is stopped.

## [◆ ](#ga5735d13f24c974ad6d4038c93edf05e0)NET\_EVENT\_DNS\_SERVER\_ADD

| #define NET\_EVENT\_DNS\_SERVER\_ADD   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when a DNS server is added to the system.

## [◆ ](#ga9d406772e5d1ad2952b2a2e0fed05c73)NET\_EVENT\_DNS\_SERVER\_DEL

| #define NET\_EVENT\_DNS\_SERVER\_DEL   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when a DNS server is removed from the system.

## [◆ ](#gac5a7458d89e4a95564999dca3c1b9f1e)NET\_EVENT\_HOSTNAME\_CHANGED

| #define NET\_EVENT\_HOSTNAME\_CHANGED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the system hostname is changed.

## [◆ ](#gacb6ac7a4579be883abc9aa638299b0cd)NET\_EVENT\_IF\_ADMIN\_DOWN

| #define NET\_EVENT\_IF\_ADMIN\_DOWN   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the network interface is taken down manually.

## [◆ ](#ga94a52eb94cc2189919ade9c8c8f239bd)NET\_EVENT\_IF\_ADMIN\_UP

| #define NET\_EVENT\_IF\_ADMIN\_UP   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the network interface goes up manually.

## [◆ ](#gac43a928bce3feb217b37ff7eb205e71b)NET\_EVENT\_IF\_DOWN

| #define NET\_EVENT\_IF\_DOWN   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the network interface goes down.

## [◆ ](#gaddc84a60607bb27048397e29eb9107f5)NET\_EVENT\_IF\_UP

| #define NET\_EVENT\_IF\_UP   (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the network interface goes up.

## [◆ ](#ga9af1f8f4ba965e6d6e82a190ab4748a1)NET\_EVENT\_IPV4\_ACD\_CONFLICT

| #define NET\_EVENT\_IPV4\_ACD\_CONFLICT   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 address conflict was detected after the address was confirmed as safe to use.

It's up to the application to determine on how to act in such case.

## [◆ ](#ga3de741f5732473a1f49d9d0b93183549)NET\_EVENT\_IPV4\_ACD\_FAILED

| #define NET\_EVENT\_IPV4\_ACD\_FAILED   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 address conflict detection fails.

## [◆ ](#ga5293377de1fdc79e7564f4e5104a07c2)NET\_EVENT\_IPV4\_ACD\_SUCCEED

| #define NET\_EVENT\_IPV4\_ACD\_SUCCEED   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 address conflict detection succeeds.

## [◆ ](#gad422365df617ce1473412908738048f0)NET\_EVENT\_IPV4\_ADDR\_ADD

| #define NET\_EVENT\_IPV4\_ADDR\_ADD   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 address is added to the system.

## [◆ ](#ga0d78644f799d1d8f5c18ec9860582817)NET\_EVENT\_IPV4\_ADDR\_DEL

| #define NET\_EVENT\_IPV4\_ADDR\_DEL   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 address is removed from the system.

## [◆ ](#ga7461ef85f4f8433851cb7583468c00cb)NET\_EVENT\_IPV4\_DHCP\_BOUND

| #define NET\_EVENT\_IPV4\_DHCP\_BOUND   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 DHCP client address is bound.

## [◆ ](#ga2d3a9351c226b1542d1b2f469b77233a)NET\_EVENT\_IPV4\_DHCP\_START

| #define NET\_EVENT\_IPV4\_DHCP\_START   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 DHCP client is started.

## [◆ ](#gabc06b6010780ab2d1e4f88227965b4e7)NET\_EVENT\_IPV4\_DHCP\_STOP

| #define NET\_EVENT\_IPV4\_DHCP\_STOP   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 DHCP client is stopped.

## [◆ ](#ga854e897d09eecccc83d04d86fbba5b64)NET\_EVENT\_IPV4\_MADDR\_ADD

| #define NET\_EVENT\_IPV4\_MADDR\_ADD   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 multicast address is added to the system.

## [◆ ](#ga303824277664ee64674b7c93ff865bb4)NET\_EVENT\_IPV4\_MADDR\_DEL

| #define NET\_EVENT\_IPV4\_MADDR\_DEL   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 multicast address is removed from the system.

## [◆ ](#ga17ad57d81f3046555f94f75dc6d31ec1)NET\_EVENT\_IPV4\_MCAST\_JOIN

| #define NET\_EVENT\_IPV4\_MCAST\_JOIN   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 multicast group is joined.

## [◆ ](#ga3cbb8a9dfec8435b93d908171ab944c9)NET\_EVENT\_IPV4\_MCAST\_LEAVE

| #define NET\_EVENT\_IPV4\_MCAST\_LEAVE   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 multicast group is left.

## [◆ ](#ga740c97a7e94181ad734888bbe7b0a3d0)NET\_EVENT\_IPV4\_ROUTER\_ADD

| #define NET\_EVENT\_IPV4\_ROUTER\_ADD   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 router is added to the system.

## [◆ ](#gae45a3b6a5f4b72edc51e06a22b88239a)NET\_EVENT\_IPV4\_ROUTER\_DEL

| #define NET\_EVENT\_IPV4\_ROUTER\_DEL   (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv4 router is removed from the system.

## [◆ ](#ga20125c6148169a91fbebab1ebba17be3)NET\_EVENT\_IPV6\_ADDR\_ADD

| #define NET\_EVENT\_IPV6\_ADDR\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 address is added to the system.

## [◆ ](#ga61f243efbc25928815ec78305b4f000e)NET\_EVENT\_IPV6\_ADDR\_DEL

| #define NET\_EVENT\_IPV6\_ADDR\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 address is removed from the system.

## [◆ ](#ga6cc42e3ca8197e46809de6082602ab98)NET\_EVENT\_IPV6\_ADDR\_DEPRECATED

| #define NET\_EVENT\_IPV6\_ADDR\_DEPRECATED   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

IPv6 address is deprecated.

## [◆ ](#ga0d5013ea3a6fa3bddd5cb182dd616151)NET\_EVENT\_IPV6\_DAD\_FAILED

| #define NET\_EVENT\_IPV6\_DAD\_FAILED   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 duplicate address detection fails.

## [◆ ](#ga8711b4b1e88c897196b982e4d56968f1)NET\_EVENT\_IPV6\_DAD\_SUCCEED

| #define NET\_EVENT\_IPV6\_DAD\_SUCCEED   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 duplicate address detection succeeds.

## [◆ ](#gaff89dbc7562a85e9ff073b507bdf06e3)NET\_EVENT\_IPV6\_DHCP\_BOUND

| #define NET\_EVENT\_IPV6\_DHCP\_BOUND   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 DHCP client address is bound.

## [◆ ](#gaa07a5e8779ec24e5ab883970bcec6c5e)NET\_EVENT\_IPV6\_DHCP\_START

| #define NET\_EVENT\_IPV6\_DHCP\_START   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 DHCP client starts.

## [◆ ](#gaab05d5a65ef5f9ed147e32ce380f7de4)NET\_EVENT\_IPV6\_DHCP\_STOP

| #define NET\_EVENT\_IPV6\_DHCP\_STOP   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 DHCP client is stopped.

## [◆ ](#gadda9dccf913a4dcb4d12b2b1fe5d403c)NET\_EVENT\_IPV6\_MADDR\_ADD

| #define NET\_EVENT\_IPV6\_MADDR\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 multicast address is added to the system.

## [◆ ](#ga035db32f66effd2407e0cca4b1fd9ea3)NET\_EVENT\_IPV6\_MADDR\_DEL

| #define NET\_EVENT\_IPV6\_MADDR\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 multicast address is removed from the system.

## [◆ ](#ga287d37bae2d74e0c85de59c5e23d409a)NET\_EVENT\_IPV6\_MCAST\_JOIN

| #define NET\_EVENT\_IPV6\_MCAST\_JOIN   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 multicast group is joined.

## [◆ ](#ga862d1b2ce9b65c0806ef77909364a58d)NET\_EVENT\_IPV6\_MCAST\_LEAVE

| #define NET\_EVENT\_IPV6\_MCAST\_LEAVE   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 multicast group is left.

## [◆ ](#ga96fe7da048fe4d59435b7337626d4af7)NET\_EVENT\_IPV6\_NBR\_ADD

| #define NET\_EVENT\_IPV6\_NBR\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 neighbor is added to the system.

## [◆ ](#ga5be1cdfeb1b8da485b1042a7b2dc14e4)NET\_EVENT\_IPV6\_NBR\_DEL

| #define NET\_EVENT\_IPV6\_NBR\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 neighbor is removed from the system.

## [◆ ](#gaba20579e42c4cebc8c3ac9a40ff384f3)NET\_EVENT\_IPV6\_PE\_DISABLED

| #define NET\_EVENT\_IPV6\_PE\_DISABLED   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

IPv6 Privacy extension is disabled.

## [◆ ](#ga95f7a737a39fb655d3577405e70e04ba)NET\_EVENT\_IPV6\_PE\_ENABLED

| #define NET\_EVENT\_IPV6\_PE\_ENABLED   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

IPv6 Privacy extension is enabled.

## [◆ ](#ga19d671971cf07e76580db8098ab32971)NET\_EVENT\_IPV6\_PE\_FILTER\_ADD

| #define NET\_EVENT\_IPV6\_PE\_FILTER\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

IPv6 Privacy extension filter is added.

## [◆ ](#gaf2f1c4b8dc5b9b07985265cee6a90f70)NET\_EVENT\_IPV6\_PE\_FILTER\_DEL

| #define NET\_EVENT\_IPV6\_PE\_FILTER\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

IPv6 Privacy extension filter is removed.

## [◆ ](#ga392414b95838bca1e55e4342870a8333)NET\_EVENT\_IPV6\_PREFIX\_ADD

| #define NET\_EVENT\_IPV6\_PREFIX\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 prefix is added to the system.

## [◆ ](#gab06f93335938a635966e85a18b5b0cf6)NET\_EVENT\_IPV6\_PREFIX\_DEL

| #define NET\_EVENT\_IPV6\_PREFIX\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 prefix is removed from the system.

## [◆ ](#gad19b5e742ded9b3ed673d8f7985100fd)NET\_EVENT\_IPV6\_ROUTE\_ADD

| #define NET\_EVENT\_IPV6\_ROUTE\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 route is added to the system.

## [◆ ](#gae6f68ec69032ac049f072d6ed164987c)NET\_EVENT\_IPV6\_ROUTE\_DEL

| #define NET\_EVENT\_IPV6\_ROUTE\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 route is removed from the system.

## [◆ ](#gaae932293528aa40127a906c3dbd45e31)NET\_EVENT\_IPV6\_ROUTER\_ADD

| #define NET\_EVENT\_IPV6\_ROUTER\_ADD   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 router is added to the system.

## [◆ ](#ga8d4b7798981aaaf3aea2b793739143b7)NET\_EVENT\_IPV6\_ROUTER\_DEL

| #define NET\_EVENT\_IPV6\_ROUTER\_DEL   (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when an IPv6 router is removed from the system.

## [◆ ](#gacbd2b10cc345359c07de4a62eb172a09)NET\_EVENT\_L4\_CONNECTED

| #define NET\_EVENT\_L4\_CONNECTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the system is considered to be connected.

The connected in this context means that the network interface is up, and the interface has either IPv4 or IPv6 address assigned to it.

## [◆ ](#gacd9e0b5e2f540794b20f11b070ffbd65)NET\_EVENT\_L4\_DISCONNECTED

| #define NET\_EVENT\_L4\_DISCONNECTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when the system is no longer connected.

Typically this means that network connectivity is lost either by the network interface is going down, or the interface has no longer an IP address etc.

## [◆ ](#ga532fdc2f199e047a5d17e325cee12cf1)NET\_EVENT\_L4\_IPV4\_CONNECTED

| #define NET\_EVENT\_L4\_IPV4\_CONNECTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event raised when IPv4 network connectivity is available.

## [◆ ](#gaa92cc806d93446d548a05edb8e0074c2)NET\_EVENT\_L4\_IPV4\_DISCONNECTED

| #define NET\_EVENT\_L4\_IPV4\_DISCONNECTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when IPv4 network connectivity is lost.

## [◆ ](#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)NET\_EVENT\_L4\_IPV6\_CONNECTED

| #define NET\_EVENT\_L4\_IPV6\_CONNECTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when IPv6 network connectivity is available.

## [◆ ](#gac81abeab44fbf2b6f29d4e11a1e1bd17)NET\_EVENT\_L4\_IPV6\_DISCONNECTED

| #define NET\_EVENT\_L4\_IPV6\_DISCONNECTED   (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED) |
| --- |

`#include <[net_event.h](net__event_8h.md)>`

Event emitted when IPv6 network connectivity is lost.

## [◆ ](#ga40e0f9fc86812ad9f6fe174b4c3804e6)net\_mgmt

| #define net\_mgmt | ( |  | *\_mgmt\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_iface*, |
|  |  |  | *\_data*, |
|  |  |  | *\_len* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

net\_mgmt\_##\_mgmt\_request(\_mgmt\_request, \_iface, \_data, \_len)

Generate a network management event.

Parameters
:   | \_mgmt\_request | Management event identifier |
    | --- | --- |
    | \_iface | Network interface |
    | \_data | Any additional data for the event |
    | \_len | Length of the additional data. |

## [◆ ](#ga08bde8717fd8e12a338c517b22b87776)NET\_MGMT\_DEFINE\_REQUEST\_HANDLER

| #define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER | ( |  | *\_mgmt\_request* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

extern int net\_mgmt\_##\_mgmt\_request([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, \

struct [net\_if](structnet__if.md) \*iface, \

void \*data, size\_t len)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

Declare a request handler function for the given network event.

Parameters
:   | \_mgmt\_request | Management event identifier |
    | --- | --- |

## [◆ ](#ga3a6ca8a72ab12afd4f9b0461253eaa12)NET\_MGMT\_REGISTER\_EVENT\_HANDLER

| #define NET\_MGMT\_REGISTER\_EVENT\_HANDLER | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_event\_mask*, |
|  |  |  | *\_func*, |
|  |  |  | *\_user\_data* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(net\_mgmt\_event\_static\_handler, \_name) = { \

.event\_mask = \_event\_mask, \

.handler = \_func, \

.user\_data = (void \*)\_user\_data, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Define a static network event handler.

Parameters
:   | \_name | Name of the event handler. |
    | --- | --- |
    | \_event\_mask | A mask of network events on which the passed handler should be called in case those events come. Note that only the command part is treated as a mask, matching one to several commands. Layer and layer code will be made of an exact match. This means that in order to receive events from multiple layers, one must have multiple listeners registered, one for each layer being listened. |
    | \_func | The function to be called upon network events being emitted. |
    | \_user\_data | User data passed to the handler being called on network events. |

## [◆ ](#gab67d09d1e65b806ec1957451cbf60501)NET\_MGMT\_REGISTER\_REQUEST\_HANDLER

| #define NET\_MGMT\_REGISTER\_REQUEST\_HANDLER | ( |  | *\_mgmt\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_func* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

FUNC\_ALIAS(\_func, net\_mgmt\_##\_mgmt\_request, int)

Create a request handler function for the given network event.

Parameters
:   | \_mgmt\_request | Management event identifier |
    | --- | --- |
    | \_func | Function for handling this event |

## Typedef Documentation

## [◆ ](#gadb876a681fe7f5fb6d2709015625a67f)net\_mgmt\_event\_handler\_t

| typedef void(\* net\_mgmt\_event\_handler\_t) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
| --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Define the user's callback handler function signature.

Parameters
:   | cb | Original struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") owning this handler. |
    | --- | --- |
    | mgmt\_event | The network event being notified. |
    | iface | A pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") to which the event belongs to, if it's an event on an iface. NULL otherwise. |

## [◆ ](#ga14c81781b5bb1e6675e78a249a69357c)net\_mgmt\_event\_static\_handler\_t

| typedef void(\* net\_mgmt\_event\_static\_handler\_t) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) info\_length, void \*user\_data) |
| --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Define the user's callback handler function signature.

Parameters
:   | mgmt\_event | The network event being notified. |
    | --- | --- |
    | iface | A pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") to which the event belongs to, if it's an event on an iface. NULL otherwise. |
    | info | A valid pointer on a data understood by the handler. NULL otherwise. |
    | info\_length | Length in bytes of the memory pointed by `info`. |
    | user\_data | Data provided by the user to the handler. |

## [◆ ](#gae288951a34f7810c291986046ebe4056)net\_mgmt\_request\_handler\_t

| typedef int(\* net\_mgmt\_request\_handler\_t) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, struct [net\_if](structnet__if.md) \*iface, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Signature which all Net MGMT request handler need to follow.

Parameters
:   | mgmt\_request | The exact request value the handler is being called through |
    | --- | --- |
    | iface | A valid pointer on struct [net\_if](structnet__if.md "Network Interface structure.") if the request is meant to be tied to a network interface. NULL otherwise. |
    | data | A valid pointer on a data understood by the handler. NULL otherwise. |
    | len | Length in byte of the memory pointed by data. |

## Function Documentation

## [◆ ](#gae53f5bbc973b0f414107eca75ac0c26f)net\_mgmt\_add\_event\_callback()

| void net\_mgmt\_add\_event\_callback | ( | struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Add a user callback.

Parameters
:   | cb | A valid pointer on user's callback to add. |
    | --- | --- |

## [◆ ](#ga4960bfb01ecd891da72c57f17587f946)net\_mgmt\_del\_event\_callback()

| void net\_mgmt\_del\_event\_callback | ( | struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Delete a user callback.

Parameters
:   | cb | A valid pointer on user's callback to delete. |
    | --- | --- |

## [◆ ](#gaab4fe2e9ea0657bf91fb1910af6729cc)net\_mgmt\_event\_init()

| void net\_mgmt\_event\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used by the core of the network stack to initialize the network event processing.

## [◆ ](#ga0648b82762467395b98a3bc13ab451d0)net\_mgmt\_event\_notify()

| | void net\_mgmt\_event\_notify | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \* | *iface* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used by the system to notify an event without any additional information.

Parameters
:   | mgmt\_event | The actual network event code to notify |
    | --- | --- |
    | iface | A valid pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") if only the event is based on an iface. NULL otherwise. |

## [◆ ](#ga10882f80c53400b94401a2a08d31697d)net\_mgmt\_event\_notify\_with\_info()

| void net\_mgmt\_event\_notify\_with\_info | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface*, |
|  |  | const void \* | *info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used by the system to notify an event.

Parameters
:   | mgmt\_event | The actual network event code to notify |
    | --- | --- |
    | iface | a valid pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") if only the event is based on an iface. NULL otherwise. |
    | info | A valid pointer on the information you want to pass along with the event. NULL otherwise. Note the data pointed there is normalized by the related event. |
    | length | size of the data pointed by info pointer. |

Note: info and length are disabled if CONFIG\_NET\_MGMT\_EVENT\_INFO is not defined.

## [◆ ](#gacbaa95c65717747d802dc80eb745aa17)net\_mgmt\_event\_wait()

| int net\_mgmt\_event\_wait | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event\_mask*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *raised\_event*, |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface*, |
|  |  | const void \*\* | *info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *info\_length*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used to wait synchronously on an event mask.

Parameters
:   | mgmt\_event\_mask | A mask of relevant events to wait on. |
    | --- | --- |
    | raised\_event | a pointer on a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) to get which event from the mask generated the event. Can be NULL if the caller is not interested in that information. |
    | iface | a pointer on a place holder for the iface on which the event has originated from. This is valid if only the event mask has bit NET\_MGMT\_IFACE\_BIT set relevantly, depending on events the caller wants to listen to. |
    | info | a valid pointer if user wants to get the information the event might bring along. NULL otherwise. |
    | info\_length | tells how long the info memory area is. Only valid if the info is not NULL. |
    | timeout | A timeout delay. K\_FOREVER can be used to wait indefinitely. |

Returns
:   0 on success, a negative error code otherwise. -ETIMEDOUT will be specifically returned if the timeout kick-in instead of an actual event.

## [◆ ](#ga03c39d5f2af3f2d7a633513fb5ec8a7d)net\_mgmt\_event\_wait\_on\_iface()

| int net\_mgmt\_event\_wait\_on\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event\_mask*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *raised\_event*, |
|  |  | const void \*\* | *info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *info\_length*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used to wait synchronously on an event mask for a specific iface.

Parameters
:   | iface | a pointer on a valid network interface to listen event to |
    | --- | --- |
    | mgmt\_event\_mask | A mask of relevant events to wait on. Listened to events should be relevant to iface events and thus have the bit NET\_MGMT\_IFACE\_BIT set. |
    | raised\_event | a pointer on a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) to get which event from the mask generated the event. Can be NULL if the caller is not interested in that information. |
    | info | a valid pointer if user wants to get the information the event might bring along. NULL otherwise. |
    | info\_length | tells how long the info memory area is. Only valid if the info is not NULL. |
    | timeout | A timeout delay. K\_FOREVER can be used to wait indefinitely. |

Returns
:   0 on success, a negative error code otherwise. -ETIMEDOUT will be specifically returned if the timeout kick-in instead of an actual event.

## [◆ ](#gaa1d086dcdeb54412073e287129bc50e0)net\_mgmt\_init\_event\_callback()

| | void net\_mgmt\_init\_event\_callback | ( | struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \* | *cb*, | | --- | --- | --- | --- | |  |  | [net\_mgmt\_event\_handler\_t](#gadb876a681fe7f5fb6d2709015625a67f) | *handler*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event\_mask* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Helper to initialize a struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") properly.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | mgmt\_event\_mask | A mask of relevant events for the handler |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
