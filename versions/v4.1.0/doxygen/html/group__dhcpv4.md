---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__dhcpv4.html
original_path: doxygen/html/group__dhcpv4.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DHCPv4

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DHCPv4.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_dhcpv4\_option\_callback\_handler\_t](#ga75caf142c6c4e058f78c7be0a4a35a9d)) (struct net\_dhcpv4\_option\_callback \*cb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, enum [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type, struct [net\_if](structnet__if.md) \*iface) |
|  | Define the application callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) {     [NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) = 1 , [NET\_DHCPV4\_MSG\_TYPE\_OFFER](#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) = 2 , [NET\_DHCPV4\_MSG\_TYPE\_REQUEST](#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) = 3 , [NET\_DHCPV4\_MSG\_TYPE\_DECLINE](#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) = 4 ,     [NET\_DHCPV4\_MSG\_TYPE\_ACK](#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) = 5 , [NET\_DHCPV4\_MSG\_TYPE\_NAK](#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) = 6 , [NET\_DHCPV4\_MSG\_TYPE\_RELEASE](#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) = 7 , [NET\_DHCPV4\_MSG\_TYPE\_INFORM](#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) = 8   } |
|  | DHCPv4 message types. [More...](#gacc66584b0776e5a79b1f4ceea479a7f8) |

| Functions | |
| --- | --- |
| static void | [net\_dhcpv4\_init\_option\_callback](#ga84df76c84de248a43e3e26d422cdfc2f) (struct net\_dhcpv4\_option\_callback \*callback, [net\_dhcpv4\_option\_callback\_handler\_t](#ga75caf142c6c4e058f78c7be0a4a35a9d) handler, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_length) |
|  | Helper to initialize a struct net\_dhcpv4\_option\_callback properly. |
| int | [net\_dhcpv4\_add\_option\_callback](#gaf073157fcd5cb2d18c40b8697d724a7c) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Add an application callback. |
| int | [net\_dhcpv4\_remove\_option\_callback](#gaa90c4ba8010bcd2079512afe5f288dbb) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Remove an application callback. |
| static void | [net\_dhcpv4\_init\_option\_vendor\_callback](#gaec0f1c87f5093767a4bb1c43b8e18e72) (struct net\_dhcpv4\_option\_callback \*callback, [net\_dhcpv4\_option\_callback\_handler\_t](#ga75caf142c6c4e058f78c7be0a4a35a9d) handler, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_length) |
|  | Helper to initialize a struct net\_dhcpv4\_option\_callback for encapsulated vendor-specific options properly. |
| int | [net\_dhcpv4\_add\_option\_vendor\_callback](#gabf3d97139fc4f7122c1bdee52cb003cb) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Add an application callback for encapsulated vendor-specific options. |
| int | [net\_dhcpv4\_remove\_option\_vendor\_callback](#ga1f362cce448226447d892f5ed8401db5) (struct net\_dhcpv4\_option\_callback \*cb) |
|  | Remove an application callback for encapsulated vendor-specific options. |
| void | [net\_dhcpv4\_start](#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start DHCPv4 client on an iface. |
| void | [net\_dhcpv4\_stop](#ga910a416e25c2878b84319f6884883d8e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop DHCPv4 client on an iface. |
| void | [net\_dhcpv4\_restart](#ga57979593bfb87d006e634b88a64bdf1a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Restart DHCPv4 client on an iface. |
| const char \* | [net\_dhcpv4\_msg\_type\_name](#ga571124b93b5dfdf3377877aded0c374c) (enum [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type) |
|  | Return a text representation of the msg\_type. |

## Detailed Description

DHCPv4.

Since
:   1.7

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#ga75caf142c6c4e058f78c7be0a4a35a9d)net\_dhcpv4\_option\_callback\_handler\_t

| typedef void(\* net\_dhcpv4\_option\_callback\_handler\_t) (struct net\_dhcpv4\_option\_callback \*cb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, enum [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type, struct [net\_if](structnet__if.md) \*iface) |
| --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Define the application callback handler function signature.

Parameters
:   | cb | Original struct net\_dhcpv4\_option\_callback owning this handler |
    | --- | --- |
    | length | The length of data returned by the server. If this is greater than cb->max\_length, only cb->max\_length bytes will be available in cb->data |
    | msg\_type | Type of DHCP message that triggered the callback |
    | iface | The interface on which the DHCP message was received |

Note: cb pointer can be used to retrieve private data through [CONTAINER\_OF()](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f "Get a pointer to a structure containing the element.") if original struct net\_dhcpv4\_option\_callback is stored in another private structure.

## Enumeration Type Documentation

## [◆ ](#gacc66584b0776e5a79b1f4ceea479a7f8)net\_dhcpv4\_msg\_type

| enum [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) |
| --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

DHCPv4 message types.

These enumerations represent RFC2131 defined msy type codes, hence they should not be renumbered.

Additions, removald and reorders in this definition must be reflected within corresponding changes to net\_dhcpv4\_msg\_type\_name.

| Enumerator | |
| --- | --- |
| NET\_DHCPV4\_MSG\_TYPE\_DISCOVER | Discover message. |
| NET\_DHCPV4\_MSG\_TYPE\_OFFER | Offer message. |
| NET\_DHCPV4\_MSG\_TYPE\_REQUEST | Request message. |
| NET\_DHCPV4\_MSG\_TYPE\_DECLINE | Decline message. |
| NET\_DHCPV4\_MSG\_TYPE\_ACK | Acknowledge message. |
| NET\_DHCPV4\_MSG\_TYPE\_NAK | Negative acknowledge message. |
| NET\_DHCPV4\_MSG\_TYPE\_RELEASE | Release message. |
| NET\_DHCPV4\_MSG\_TYPE\_INFORM | Inform message. |

## Function Documentation

## [◆ ](#gaf073157fcd5cb2d18c40b8697d724a7c)net\_dhcpv4\_add\_option\_callback()

| int net\_dhcpv4\_add\_option\_callback | ( | struct net\_dhcpv4\_option\_callback \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Add an application callback.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#gabf3d97139fc4f7122c1bdee52cb003cb)net\_dhcpv4\_add\_option\_vendor\_callback()

| int net\_dhcpv4\_add\_option\_vendor\_callback | ( | struct net\_dhcpv4\_option\_callback \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Add an application callback for encapsulated vendor-specific options.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#ga84df76c84de248a43e3e26d422cdfc2f)net\_dhcpv4\_init\_option\_callback()

| | void net\_dhcpv4\_init\_option\_callback | ( | struct net\_dhcpv4\_option\_callback \* | *callback*, | | --- | --- | --- | --- | |  |  | [net\_dhcpv4\_option\_callback\_handler\_t](#ga75caf142c6c4e058f78c7be0a4a35a9d) | *handler*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *option*, | |  |  | void \* | *data*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Helper to initialize a struct net\_dhcpv4\_option\_callback properly.

Parameters
:   | callback | A valid Application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | option | The DHCP option the callback responds to. |
    | data | A pointer to a buffer for max\_length bytes. |
    | max\_length | The maximum length of the data returned. |

## [◆ ](#gaec0f1c87f5093767a4bb1c43b8e18e72)net\_dhcpv4\_init\_option\_vendor\_callback()

| | void net\_dhcpv4\_init\_option\_vendor\_callback | ( | struct net\_dhcpv4\_option\_callback \* | *callback*, | | --- | --- | --- | --- | |  |  | [net\_dhcpv4\_option\_callback\_handler\_t](#ga75caf142c6c4e058f78c7be0a4a35a9d) | *handler*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *option*, | |  |  | void \* | *data*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Helper to initialize a struct net\_dhcpv4\_option\_callback for encapsulated vendor-specific options properly.

Parameters
:   | callback | A valid Application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | option | The DHCP encapsulated vendor-specific option the callback responds to. |
    | data | A pointer to a buffer for max\_length bytes. |
    | max\_length | The maximum length of the data returned. |

## [◆ ](#ga571124b93b5dfdf3377877aded0c374c)net\_dhcpv4\_msg\_type\_name()

| const char \* net\_dhcpv4\_msg\_type\_name | ( | enum [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) | *msg\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Return a text representation of the msg\_type.

Parameters
:   | msg\_type | The msg\_type to be converted to text |
    | --- | --- |

Returns
:   A text representation of msg\_type

## [◆ ](#gaa90c4ba8010bcd2079512afe5f288dbb)net\_dhcpv4\_remove\_option\_callback()

| int net\_dhcpv4\_remove\_option\_callback | ( | struct net\_dhcpv4\_option\_callback \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Remove an application callback.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#ga1f362cce448226447d892f5ed8401db5)net\_dhcpv4\_remove\_option\_vendor\_callback()

| int net\_dhcpv4\_remove\_option\_vendor\_callback | ( | struct net\_dhcpv4\_option\_callback \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Remove an application callback for encapsulated vendor-specific options.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#ga57979593bfb87d006e634b88a64bdf1a)net\_dhcpv4\_restart()

| void net\_dhcpv4\_restart | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Restart DHCPv4 client on an iface.

Restart DHCPv4 client on a given interface. DHCPv4 client will restart the state machine without any of the initial delays used in start.

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |

## [◆ ](#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)net\_dhcpv4\_start()

| void net\_dhcpv4\_start | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Start DHCPv4 client on an iface.

Start DHCPv4 client on a given interface. DHCPv4 client will start negotiation for IPv4 address. Once the negotiation is success IPv4 address details will be added to interface.

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |

## [◆ ](#ga910a416e25c2878b84319f6884883d8e)net\_dhcpv4\_stop()

| void net\_dhcpv4\_stop | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4.h](dhcpv4_8h.md)>`

Stop DHCPv4 client on an iface.

Stop DHCPv4 client on a given interface. DHCPv4 client will remove all configuration obtained from a DHCP server from the interface and stop any further negotiation with the server.

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
