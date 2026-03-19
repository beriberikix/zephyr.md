---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__virtual.html
original_path: doxygen/html/group__virtual.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Virtual Network Interface Support Functions

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Virtual network interface support functions.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [virtual\_interface\_api](structvirtual__interface__api.md) |
|  | Virtual L2 API operations. [More...](structvirtual__interface__api.md#details) |
| struct | [virtual\_interface\_context](structvirtual__interface__context.md) |
|  | Virtual L2 context that is needed to binding to the real network interface. [More...](structvirtual__interface__context.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_VIRTUAL\_INTERFACE\_INIT](#ga74a5c258a08397f881a8922516ac5d3a)(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create a virtual network interface. |
| #define | [NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE](#ga1846d4173bcd4b40a05b70c5fde18f91)(dev\_id, name, inst, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create a virtual network interface. |

| Enumerations | |
| --- | --- |
| enum | [virtual\_interface\_caps](#ga8f188f5c2f19960d7113da52aefe8091) { [VIRTUAL\_INTERFACE\_IPIP](#gga8f188f5c2f19960d7113da52aefe8091a097c314c36dc5f7129f1c8bb1e110071) = BIT(1) , [VIRTUAL\_INTERFACE\_VLAN](#gga8f188f5c2f19960d7113da52aefe8091a5d496813292edfe8156484450fc7d83b) = BIT(2) , [VIRTUAL\_INTERFACE\_BRIDGE](#gga8f188f5c2f19960d7113da52aefe8091a1ce35cd2b3312437b51d7440da2efaed) = BIT(3) } |
|  | Virtual interface capabilities. [More...](#ga8f188f5c2f19960d7113da52aefe8091) |

| Functions | |
| --- | --- |
| int | [net\_virtual\_interface\_attach](#ga5cba6ff65402b591a0e42d05f258671f) (struct [net\_if](structnet__if.md) \*virtual\_iface, struct [net\_if](structnet__if.md) \*iface) |
|  | Attach virtual network interface to the given network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_virtual\_get\_iface](#gabadf14eaa02978cde7030c99ddd3e279) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return network interface related to this virtual network interface. |
| char \* | [net\_virtual\_get\_name](#gaa7ff8ebb83fe98a1dfd23f319317a8de) (struct [net\_if](structnet__if.md) \*iface, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Return the name of the virtual network interface L2. |
| void | [net\_virtual\_set\_name](#ga2aaba616ed4fecc27138d5aae58a634f) (struct [net\_if](structnet__if.md) \*iface, const char \*name) |
|  | Set the name of the virtual network interface L2. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | [net\_virtual\_set\_flags](#ga30f92f519a6f204ebeccd6053f17eaf0) (struct [net\_if](structnet__if.md) \*iface, enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set the L2 flags of the virtual network interface. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_virtual\_input](#ga6c63773925ef7d96b0ba03d8978fd499) (struct [net\_if](structnet__if.md) \*input\_iface, struct net\_addr \*remote\_addr, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Feed the IP pkt to stack if tunneling is enabled. |

## Detailed Description

Virtual network interface support functions.

Since
:   2.6

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga74a5c258a08397f881a8922516ac5d3a)NET\_VIRTUAL\_INTERFACE\_INIT

| #define NET\_VIRTUAL\_INTERFACE\_INIT | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *mtu* ) |

`#include <[virtual.h](virtual_8h.md)>`

**Value:**

Z\_NET\_VIRTUAL\_INTERFACE\_INIT([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, name, \

init\_fn, pm, data, config, prio, \

api, mtu)

[DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:83

Create a virtual network interface.

Binding to another interface is done at runtime by calling [net\_virtual\_interface\_attach()](#ga5cba6ff65402b591a0e42d05f258671f). The attaching is done automatically when setting up tunneling when peer IP address is set in IP tunneling driver.

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
    | mtu | Maximum transfer unit in bytes for this network interface. This is the default value and its value can be tweaked at runtime. |

## [◆ ](#ga1846d4173bcd4b40a05b70c5fde18f91)NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE

| #define NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *inst*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *mtu* ) |

`#include <[virtual.h](virtual_8h.md)>`

**Value:**

Z\_NET\_VIRTUAL\_INTERFACE\_INIT\_INSTANCE([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, \

name, inst, \

init\_fn, pm, data, config, \

prio, api, mtu)

Create a virtual network interface.

Binding to another interface is done at runtime by calling [net\_virtual\_interface\_attach()](#ga5cba6ff65402b591a0e42d05f258671f). The attaching is done automatically when setting up tunneling when peer IP address is set in IP tunneling driver.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | name | The name this instance of the driver exposes to the system. |
    | inst | instance number |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | mtu | Maximum transfer unit in bytes for this network interface. This is the default value and its value can be tweaked at runtime. |

## Enumeration Type Documentation

## [◆ ](#ga8f188f5c2f19960d7113da52aefe8091)virtual\_interface\_caps

| enum [virtual\_interface\_caps](#ga8f188f5c2f19960d7113da52aefe8091) |
| --- |

`#include <[virtual.h](virtual_8h.md)>`

Virtual interface capabilities.

| Enumerator | |
| --- | --- |
| VIRTUAL\_INTERFACE\_IPIP | IPIP tunnel. |
| VIRTUAL\_INTERFACE\_VLAN | Virtual LAN interface (VLAN). |
| VIRTUAL\_INTERFACE\_BRIDGE | Virtual Ethernet bridge interface. |

## Function Documentation

## [◆ ](#gabadf14eaa02978cde7030c99ddd3e279)net\_virtual\_get\_iface()

| struct [net\_if](structnet__if.md) \* net\_virtual\_get\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[virtual.h](virtual_8h.md)>`

Return network interface related to this virtual network interface.

The returned network interface is below this virtual network interface.

Parameters
:   | iface | Virtual network interface. |
    | --- | --- |

Returns
:   Network interface related to this virtual interface or NULL if no such interface exists.

## [◆ ](#gaa7ff8ebb83fe98a1dfd23f319317a8de)net\_virtual\_get\_name()

| char \* net\_virtual\_get\_name | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[virtual.h](virtual_8h.md)>`

Return the name of the virtual network interface L2.

Parameters
:   | iface | Virtual network interface. |
    | --- | --- |
    | buf | Buffer to store the name |
    | len | Max buffer length |

Returns
:   Name of the virtual network interface.

## [◆ ](#ga6c63773925ef7d96b0ba03d8978fd499)net\_virtual\_input()

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) net\_virtual\_input | ( | struct [net\_if](structnet__if.md) \* | *input\_iface*, |
| --- | --- | --- | --- |
|  |  | struct net\_addr \* | *remote\_addr*, |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[virtual.h](virtual_8h.md)>`

Feed the IP pkt to stack if tunneling is enabled.

Parameters
:   | input\_iface | Network interface receiving the pkt. |
    | --- | --- |
    | remote\_addr | IP address of the sender. |
    | pkt | Network packet. |

Returns
:   Verdict what to do with the packet.

## [◆ ](#ga5cba6ff65402b591a0e42d05f258671f)net\_virtual\_interface\_attach()

| int net\_virtual\_interface\_attach | ( | struct [net\_if](structnet__if.md) \* | *virtual\_iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[virtual.h](virtual_8h.md)>`

Attach virtual network interface to the given network interface.

Parameters
:   | virtual\_iface | Virtual network interface. |
    | --- | --- |
    | iface | Network interface we are attached to. This can be NULL, if we want to detach. |

Returns
:   0 if ok, <0 if attaching failed

## [◆ ](#ga30f92f519a6f204ebeccd6053f17eaf0)net\_virtual\_set\_flags()

| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) net\_virtual\_set\_flags | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | *flags* ) |

`#include <[virtual.h](virtual_8h.md)>`

Set the L2 flags of the virtual network interface.

Parameters
:   | iface | Virtual network interface. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | L2 flags to set. |

Returns
:   Previous flags that were set.

## [◆ ](#ga2aaba616ed4fecc27138d5aae58a634f)net\_virtual\_set\_name()

| void net\_virtual\_set\_name | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name* ) |

`#include <[virtual.h](virtual_8h.md)>`

Set the name of the virtual network interface L2.

Parameters
:   | iface | Virtual network interface. |
    | --- | --- |
    | name | Name of the virtual L2 layer. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
