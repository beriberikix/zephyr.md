---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__ethernet.html
original_path: doxygen/html/group__ethernet.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet Support Functions

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Ethernet support functions.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Ethernet MII Support Functions](group__ethernet__mii.md) |
|  | Ethernet MII (media independent interface) functions. |
|  | [IEEE 802.3 management interface](group__ethernet__mdio.md) |
|  | Definitions for IEEE 802.3 management interface. |

| Data Structures | |
| --- | --- |
| struct | [ethernet\_t1s\_param](structethernet__t1s__param.md) |
| struct | [ethernet\_qav\_param](structethernet__qav__param.md) |
| struct | [ethernet\_qbv\_param](structethernet__qbv__param.md) |
| struct | [ethernet\_qbu\_param](structethernet__qbu__param.md) |
| struct | [ethernet\_filter](structethernet__filter.md) |
| struct | [ethernet\_txtime\_param](structethernet__txtime__param.md) |
| struct | [ethernet\_api](structethernet__api.md) |
| struct | [ethernet\_context](structethernet__context.md) |
|  | Ethernet L2 context that is needed for VLAN. [More...](structethernet__context.md#details) |

| Macros | |
| --- | --- |
| #define | [ETH\_NET\_DEVICE\_INIT](#ga197e02748be8eaf410f7deb57c984642)(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create an Ethernet network interface and bind it to network device. |
| #define | [ETH\_NET\_DEVICE\_DT\_DEFINE](#ga9f67fee695953f24b1e5d9e49041aa99)(node\_id, init\_fn, pm, data, config, prio, api, mtu) |
|  | Like ETH\_NET\_DEVICE\_INIT but taking metadata from a devicetree. |
| #define | [ETH\_NET\_DEVICE\_DT\_INST\_DEFINE](#gaecf9f102108836ed9cf7e2cdb3c90579)(inst, ...) |
|  | Like ETH\_NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible. |

| Enumerations | |
| --- | --- |
| enum | [ethernet\_hw\_caps](#ga9162ff11d626813fc840df0b67820ac5) {     [ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD](#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861) = BIT(0) , [ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD](#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33) = BIT(1) , [ETHERNET\_HW\_VLAN](#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95) = BIT(2) , [ETHERNET\_AUTO\_NEGOTIATION\_SET](#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a) = BIT(3) ,     [ETHERNET\_LINK\_10BASE\_T](#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6) = BIT(4) , [ETHERNET\_LINK\_100BASE\_T](#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e) = BIT(5) , [ETHERNET\_LINK\_1000BASE\_T](#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8) = BIT(6) , [ETHERNET\_DUPLEX\_SET](#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc) = BIT(7) ,     [ETHERNET\_PTP](#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a) = BIT(8) , [ETHERNET\_QAV](#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42) = BIT(9) , [ETHERNET\_PROMISC\_MODE](#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d) = BIT(10) , [ETHERNET\_PRIORITY\_QUEUES](#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475) = BIT(11) ,     [ETHERNET\_HW\_FILTERING](#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe) = BIT(12) , [ETHERNET\_LLDP](#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2) = BIT(13) , [ETHERNET\_HW\_VLAN\_TAG\_STRIP](#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5) = BIT(14) , [ETHERNET\_DSA\_SLAVE\_PORT](#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7) = BIT(15) ,     [ETHERNET\_DSA\_MASTER\_PORT](#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883) = BIT(16) , [ETHERNET\_QBV](#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85) = BIT(17) , [ETHERNET\_QBU](#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08) = BIT(18) , [ETHERNET\_TXTIME](#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2) = BIT(19) ,     [ETHERNET\_TXINJECTION\_MODE](#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b) = BIT(20)   } |
|  | Ethernet hardware capabilities. [More...](#ga9162ff11d626813fc840df0b67820ac5) |
| enum | [ethernet\_if\_types](#ga139cc696837611a522b289f2ea7bf6fc) { [L2\_ETH\_IF\_TYPE\_ETHERNET](#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530) , [L2\_ETH\_IF\_TYPE\_WIFI](#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671) } |
|  | Types of Ethernet L2. [More...](#ga139cc696837611a522b289f2ea7bf6fc) |
| enum | [ethernet\_flags](#ga97d926fe9e96a1205b00b808120dda88) { [ETH\_CARRIER\_UP](#gga97d926fe9e96a1205b00b808120dda88ae630377e05a087a99649647593c38135) } |

| Functions | |
| --- | --- |
| void | [ethernet\_init](#gacd67360df806183cbc15159b0480bfa0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Initialize Ethernet L2 stack for a given interface. |
| void | [net\_eth\_ipv4\_mcast\_to\_mac\_addr](#gae3ce2bd669391071635f5709d1c3cd8e) (const struct [in\_addr](structin__addr.md) \*ipv4\_addr, struct net\_eth\_addr \*mac\_addr) |
|  | Convert IPv4 multicast address to Ethernet address. |
| void | [net\_eth\_ipv6\_mcast\_to\_mac\_addr](#gaa08d5237c26e8c05748d58eb65b15c2f) (const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr, struct net\_eth\_addr \*mac\_addr) |
|  | Convert IPv6 multicast address to Ethernet address. |
| static enum [ethernet\_hw\_caps](#ga9162ff11d626813fc840df0b67820ac5) | [net\_eth\_get\_hw\_capabilities](#gab0a3b4584bb6ce1d27b98b063fd3fcbd) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return ethernet device hardware capability information. |
| static int | [net\_eth\_vlan\_enable](#ga16cbc14e3a0a470bbbd5aeb5e73dc1de) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Add VLAN tag to the interface. |
| static int | [net\_eth\_vlan\_disable](#gab71a741cea5f645f4354a1abc9c95a50) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Remove VLAN tag from the interface. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_get\_vlan\_tag](#ga6184c43a62e4af9958412f99991358c9) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return VLAN tag specified to network interface. |
| static struct [net\_if](structnet__if.md) \* | [net\_eth\_get\_vlan\_iface](#gad9d890dcf7f5ee3659bf3bd5949faa4e) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Return network interface related to this VLAN tag. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_vlan\_enabled](#gac536aa7154c4a8d194ec67efb68e275c) (struct [ethernet\_context](structethernet__context.md) \*ctx, struct [net\_if](structnet__if.md) \*iface) |
|  | Check if VLAN is enabled for a specific network interface. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_get\_vlan\_status](#ga78aad58ec66710034cab8891ad638a2c) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get VLAN status for a given network interface (enabled or not). |
| void | [net\_eth\_carrier\_on](#gabeb21cb06b18674b73fbd0f42ee726f0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Inform ethernet L2 driver that ethernet carrier is detected. |
| void | [net\_eth\_carrier\_off](#ga4dcf5047108b509e349b02fe35c10d75) (struct [net\_if](structnet__if.md) \*iface) |
|  | Inform ethernet L2 driver that ethernet carrier was lost. |
| int | [net\_eth\_promisc\_mode](#ga42a3c6b04ef8827e3443c5aebe5541b9) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set promiscuous mode either ON or OFF. |
| int | [net\_eth\_txinjection\_mode](#gafbb76d53f9f80628d18d39368a28f984) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set TX-Injection mode either ON or OFF. |
| static const struct [device](structdevice.md) \* | [net\_eth\_get\_ptp\_clock](#ga37ff48434c56bbb24422dd805449b6f3) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return PTP clock that is tied to this ethernet network interface. |
| const struct [device](structdevice.md) \* | [net\_eth\_get\_ptp\_clock\_by\_index](#ga84c37db5687c5264bec99976a1108ab6) (int index) |
|  | Return PTP clock that is tied to this ethernet network interface index. |
| static int | [net\_eth\_get\_ptp\_port](#ga37c5d1d5d534c6d024b060ae54bbd82a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return PTP port number attached to this interface. |
| static void | [net\_eth\_set\_ptp\_port](#ga1424a7e54b8b439b7000dfb23f825231) (struct [net\_if](structnet__if.md) \*iface, int port) |
|  | Set PTP port number attached to this interface. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_type\_is\_wifi](#ga6e603f6f74e6d7e988e7119a6df2ab4d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the Ethernet L2 network interface can perform Wi-Fi. |

## Detailed Description

Ethernet support functions.

## Macro Definition Documentation

## [◆ ](#ga9f67fee695953f24b1e5d9e49041aa99)ETH\_NET\_DEVICE\_DT\_DEFINE

| #define ETH\_NET\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *mtu* ) |

`#include <[ethernet.h](ethernet_8h.md)>`

**Value:**

Z\_ETH\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), init\_fn, pm, \

data, config, prio, api, mtu)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:149

Like ETH\_NET\_DEVICE\_INIT but taking metadata from a devicetree.

Create an Ethernet network interface and bind it to network device.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#gaecf9f102108836ed9cf7e2cdb3c90579)ETH\_NET\_DEVICE\_DT\_INST\_DEFINE

| #define ETH\_NET\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ethernet.h](ethernet_8h.md)>`

**Value:**

[ETH\_NET\_DEVICE\_DT\_DEFINE](#ga9f67fee695953f24b1e5d9e49041aa99)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[ETH\_NET\_DEVICE\_DT\_DEFINE](#ga9f67fee695953f24b1e5d9e49041aa99)

#define ETH\_NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, prio, api, mtu)

Like ETH\_NET\_DEVICE\_INIT but taking metadata from a devicetree.

**Definition** ethernet.h:992

Like ETH\_NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to ETH\_NET\_DEVICE\_DT\_DEFINE. |
    | --- | --- |
    | ... | other parameters as expected by ETH\_NET\_DEVICE\_DT\_DEFINE. |

## [◆ ](#ga197e02748be8eaf410f7deb57c984642)ETH\_NET\_DEVICE\_INIT

| #define ETH\_NET\_DEVICE\_INIT | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *mtu* ) |

`#include <[ethernet.h](ethernet_8h.md)>`

**Value:**

Z\_ETH\_NET\_DEVICE\_INIT([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, name, init\_fn, \

pm, data, config, prio, api, mtu)

[DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:85

Create an Ethernet network interface and bind it to network device.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | name | The name this instance of the driver exposes to the system. |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## Enumeration Type Documentation

## [◆ ](#ga97d926fe9e96a1205b00b808120dda88)ethernet\_flags

| enum [ethernet\_flags](#ga97d926fe9e96a1205b00b808120dda88) |
| --- |

`#include <[ethernet.h](ethernet_8h.md)>`

| Enumerator | |
| --- | --- |
| ETH\_CARRIER\_UP |  |

## [◆ ](#ga9162ff11d626813fc840df0b67820ac5)ethernet\_hw\_caps

| enum [ethernet\_hw\_caps](#ga9162ff11d626813fc840df0b67820ac5) |
| --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Ethernet hardware capabilities.

| Enumerator | |
| --- | --- |
| ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD | TX Checksum offloading supported for all of IPv4, UDP, TCP. |
| ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD | RX Checksum offloading supported for all of IPv4, UDP, TCP. |
| ETHERNET\_HW\_VLAN | VLAN supported. |
| ETHERNET\_AUTO\_NEGOTIATION\_SET | Enabling/disabling auto negotiation supported. |
| ETHERNET\_LINK\_10BASE\_T | 10 Mbits link supported |
| ETHERNET\_LINK\_100BASE\_T | 100 Mbits link supported |
| ETHERNET\_LINK\_1000BASE\_T | 1 Gbits link supported |
| ETHERNET\_DUPLEX\_SET | Changing duplex (half/full) supported. |
| ETHERNET\_PTP | IEEE 802.1AS (gPTP) clock supported. |
| ETHERNET\_QAV | IEEE 802.1Qav (credit-based shaping) supported. |
| ETHERNET\_PROMISC\_MODE | Promiscuous mode supported. |
| ETHERNET\_PRIORITY\_QUEUES | Priority queues available. |
| ETHERNET\_HW\_FILTERING | MAC address filtering supported. |
| ETHERNET\_LLDP | Link Layer Discovery Protocol supported. |
| ETHERNET\_HW\_VLAN\_TAG\_STRIP | VLAN Tag stripping. |
| ETHERNET\_DSA\_SLAVE\_PORT | DSA switch. |
| ETHERNET\_DSA\_MASTER\_PORT |  |
| ETHERNET\_QBV | IEEE 802.1Qbv (scheduled traffic) supported. |
| ETHERNET\_QBU | IEEE 802.1Qbu (frame preemption) supported. |
| ETHERNET\_TXTIME | TXTIME supported. |
| ETHERNET\_TXINJECTION\_MODE | TX-Injection supported. |

## [◆ ](#ga139cc696837611a522b289f2ea7bf6fc)ethernet\_if\_types

| enum [ethernet\_if\_types](#ga139cc696837611a522b289f2ea7bf6fc) |
| --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Types of Ethernet L2.

| Enumerator | |
| --- | --- |
| L2\_ETH\_IF\_TYPE\_ETHERNET | IEEE 802.3 Ethernet (default). |
| L2\_ETH\_IF\_TYPE\_WIFI | IEEE 802.11 Wi-Fi. |

## Function Documentation

## [◆ ](#gacd67360df806183cbc15159b0480bfa0)ethernet\_init()

| void ethernet\_init | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Initialize Ethernet L2 stack for a given interface.

Parameters
:   | iface | A valid pointer to a network interface |
    | --- | --- |

## [◆ ](#ga4dcf5047108b509e349b02fe35c10d75)net\_eth\_carrier\_off()

| void net\_eth\_carrier\_off | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Inform ethernet L2 driver that ethernet carrier was lost.

This happens when cable is disconnected.

Parameters
:   | iface | Network interface |
    | --- | --- |

## [◆ ](#gabeb21cb06b18674b73fbd0f42ee726f0)net\_eth\_carrier\_on()

| void net\_eth\_carrier\_on | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Inform ethernet L2 driver that ethernet carrier is detected.

This happens when cable is connected.

Parameters
:   | iface | Network interface |
    | --- | --- |

## [◆ ](#gab0a3b4584bb6ce1d27b98b063fd3fcbd)net\_eth\_get\_hw\_capabilities()

| | enum [ethernet\_hw\_caps](#ga9162ff11d626813fc840df0b67820ac5) net\_eth\_get\_hw\_capabilities | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Return ethernet device hardware capability information.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Hardware capabilities

## [◆ ](#ga37ff48434c56bbb24422dd805449b6f3)net\_eth\_get\_ptp\_clock()

| | const struct [device](structdevice.md) \* net\_eth\_get\_ptp\_clock | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Return PTP clock that is tied to this ethernet network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Pointer to PTP clock if found, NULL if not found or if this ethernet interface does not support PTP.

## [◆ ](#ga84c37db5687c5264bec99976a1108ab6)net\_eth\_get\_ptp\_clock\_by\_index()

| const struct [device](structdevice.md) \* net\_eth\_get\_ptp\_clock\_by\_index | ( | int | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Return PTP clock that is tied to this ethernet network interface index.

Parameters
:   | index | Network interface index |
    | --- | --- |

Returns
:   Pointer to PTP clock if found, NULL if not found or if this ethernet interface index does not support PTP.

## [◆ ](#ga37c5d1d5d534c6d024b060ae54bbd82a)net\_eth\_get\_ptp\_port()

| | int net\_eth\_get\_ptp\_port | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Return PTP port number attached to this interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Port number, no such port if < 0

## [◆ ](#gad9d890dcf7f5ee3659bf3bd5949faa4e)net\_eth\_get\_vlan\_iface()

| | struct [net\_if](structnet__if.md) \* net\_eth\_get\_vlan\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tag* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Return network interface related to this VLAN tag.

Parameters
:   | iface | Master network interface. This is used to get the pointer to ethernet L2 context |
    | --- | --- |
    | tag | VLAN tag |

Returns
:   Network interface related to this tag or NULL if no such interface exists.

## [◆ ](#ga78aad58ec66710034cab8891ad638a2c)net\_eth\_get\_vlan\_status()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_eth\_get\_vlan\_status | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Get VLAN status for a given network interface (enabled or not).

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   True if VLAN is enabled for this network interface, false if not.

## [◆ ](#ga6184c43a62e4af9958412f99991358c9)net\_eth\_get\_vlan\_tag()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_eth\_get\_vlan\_tag | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Return VLAN tag specified to network interface.

Parameters
:   | iface | Network interface. |
    | --- | --- |

Returns
:   VLAN tag for this interface or NET\_VLAN\_TAG\_UNSPEC if VLAN is not configured for that interface.

## [◆ ](#gae3ce2bd669391071635f5709d1c3cd8e)net\_eth\_ipv4\_mcast\_to\_mac\_addr()

| void net\_eth\_ipv4\_mcast\_to\_mac\_addr | ( | const struct [in\_addr](structin__addr.md) \* | *ipv4\_addr*, |
| --- | --- | --- | --- |
|  |  | struct net\_eth\_addr \* | *mac\_addr* ) |

`#include <[ethernet.h](ethernet_8h.md)>`

Convert IPv4 multicast address to Ethernet address.

Parameters
:   | ipv4\_addr | IPv4 multicast address |
    | --- | --- |
    | mac\_addr | Output buffer for Ethernet address |

## [◆ ](#gaa08d5237c26e8c05748d58eb65b15c2f)net\_eth\_ipv6\_mcast\_to\_mac\_addr()

| void net\_eth\_ipv6\_mcast\_to\_mac\_addr | ( | const struct [in6\_addr](structin6__addr.md) \* | *ipv6\_addr*, |
| --- | --- | --- | --- |
|  |  | struct net\_eth\_addr \* | *mac\_addr* ) |

`#include <[ethernet.h](ethernet_8h.md)>`

Convert IPv6 multicast address to Ethernet address.

Parameters
:   | ipv6\_addr | IPv6 multicast address |
    | --- | --- |
    | mac\_addr | Output buffer for Ethernet address |

## [◆ ](#gac536aa7154c4a8d194ec67efb68e275c)net\_eth\_is\_vlan\_enabled()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_eth\_is\_vlan\_enabled | ( | struct [ethernet\_context](structethernet__context.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \* | *iface* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Check if VLAN is enabled for a specific network interface.

Parameters
:   | ctx | Ethernet context |
    | --- | --- |
    | iface | Network interface |

Returns
:   True if VLAN is enabled for this network interface, false if not.

## [◆ ](#ga42a3c6b04ef8827e3443c5aebe5541b9)net\_eth\_promisc\_mode()

| int net\_eth\_promisc\_mode | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[ethernet.h](ethernet_8h.md)>`

Set promiscuous mode either ON or OFF.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | enable | on (true) or off (false) |

Returns
:   0 if mode set or unset was successful, <0 otherwise.

## [◆ ](#ga1424a7e54b8b439b7000dfb23f825231)net\_eth\_set\_ptp\_port()

| | void net\_eth\_set\_ptp\_port | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | int | *port* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Set PTP port number attached to this interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | port | Port number to set |

## [◆ ](#gafbb76d53f9f80628d18d39368a28f984)net\_eth\_txinjection\_mode()

| int net\_eth\_txinjection\_mode | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[ethernet.h](ethernet_8h.md)>`

Set TX-Injection mode either ON or OFF.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | enable | on (true) or off (false) |

Returns
:   0 if mode set or unset was successful, <0 otherwise.

## [◆ ](#ga6e603f6f74e6d7e988e7119a6df2ab4d)net\_eth\_type\_is\_wifi()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_eth\_type\_is\_wifi | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Check if the Ethernet L2 network interface can perform Wi-Fi.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface supports Wi-Fi, False otherwise.

## [◆ ](#gab71a741cea5f645f4354a1abc9c95a50)net\_eth\_vlan\_disable()

| | int net\_eth\_vlan\_disable | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tag* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Remove VLAN tag from the interface.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | tag | VLAN tag to remove |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga16cbc14e3a0a470bbbd5aeb5e73dc1de)net\_eth\_vlan\_enable()

| | int net\_eth\_vlan\_enable | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tag* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet.h](ethernet_8h.md)>`

Add VLAN tag to the interface.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | tag | VLAN tag to add |

Returns
:   0 if ok, <0 if error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
