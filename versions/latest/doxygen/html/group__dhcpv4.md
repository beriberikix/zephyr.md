---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__dhcpv4.html
original_path: doxygen/html/group__dhcpv4.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DHCPv4

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DHCPv4.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [net\_dhcpv4\_msg\_type](#gacc66584b0776e5a79b1f4ceea479a7f8) {     [NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) = 1 , [NET\_DHCPV4\_MSG\_TYPE\_OFFER](#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) = 2 , [NET\_DHCPV4\_MSG\_TYPE\_REQUEST](#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) = 3 , [NET\_DHCPV4\_MSG\_TYPE\_DECLINE](#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) = 4 ,     [NET\_DHCPV4\_MSG\_TYPE\_ACK](#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) = 5 , [NET\_DHCPV4\_MSG\_TYPE\_NAK](#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) = 6 , [NET\_DHCPV4\_MSG\_TYPE\_RELEASE](#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) = 7 , [NET\_DHCPV4\_MSG\_TYPE\_INFORM](#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) = 8   } |
|  | DHCPv4 message types. [More...](#gacc66584b0776e5a79b1f4ceea479a7f8) |

| Functions | |
| --- | --- |
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
| NET\_DHCPV4\_MSG\_TYPE\_DISCOVER |  |
| NET\_DHCPV4\_MSG\_TYPE\_OFFER |  |
| NET\_DHCPV4\_MSG\_TYPE\_REQUEST |  |
| NET\_DHCPV4\_MSG\_TYPE\_DECLINE |  |
| NET\_DHCPV4\_MSG\_TYPE\_ACK |  |
| NET\_DHCPV4\_MSG\_TYPE\_NAK |  |
| NET\_DHCPV4\_MSG\_TYPE\_RELEASE |  |
| NET\_DHCPV4\_MSG\_TYPE\_INFORM |  |

## Function Documentation

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
