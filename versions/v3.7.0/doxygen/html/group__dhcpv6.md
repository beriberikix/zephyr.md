---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__dhcpv6.html
original_path: doxygen/html/group__dhcpv6.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DHCPv6

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DHCPv6.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_dhcpv6\_params](structnet__dhcpv6__params.md) |
|  | DHCPv6 client configuration parameters. [More...](structnet__dhcpv6__params.md#details) |

| Functions | |
| --- | --- |
| void | [net\_dhcpv6\_start](#gab607a476c947d0335a254304e5dc2a24) (struct [net\_if](structnet__if.md) \*iface, struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) \*params) |
|  | Start DHCPv6 client on an iface. |
| void | [net\_dhcpv6\_stop](#gaf0b903bdcd0becf06ed6b212c74097a0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop DHCPv6 client on an iface. |
| void | [net\_dhcpv6\_restart](#ga99642b89c14cb17f35b45a03a2286441) (struct [net\_if](structnet__if.md) \*iface) |
|  | Restart DHCPv6 client on an iface. |

## Detailed Description

DHCPv6.

## Function Documentation

## [◆ ](#ga99642b89c14cb17f35b45a03a2286441)net\_dhcpv6\_restart()

| void net\_dhcpv6\_restart | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv6.h](dhcpv6_8h.md)>`

Restart DHCPv6 client on an iface.

Restart DHCPv6 client on a given interface. DHCPv6 client will restart the state machine without any of the initial delays.

Parameters
:   | iface | A valid pointer to a network interface |
    | --- | --- |

## [◆ ](#gab607a476c947d0335a254304e5dc2a24)net\_dhcpv6\_start()

| void net\_dhcpv6\_start | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) \* | *params* ) |

`#include <[dhcpv6.h](dhcpv6_8h.md)>`

Start DHCPv6 client on an iface.

Start DHCPv6 client on a given interface. DHCPv6 client will start negotiation for IPv6 address and/or prefix, depending on the configuration. Once the negotiation is complete, IPv6 address/prefix details will be added to the interface.

Parameters
:   | iface | A valid pointer to a network interface |
    | --- | --- |
    | params | DHCPv6 client configuration parameters. |

## [◆ ](#gaf0b903bdcd0becf06ed6b212c74097a0)net\_dhcpv6\_stop()

| void net\_dhcpv6\_stop | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv6.h](dhcpv6_8h.md)>`

Stop DHCPv6 client on an iface.

Stop DHCPv6 client on a given interface. DHCPv6 client will remove all configuration obtained from a DHCP server from the interface and stop any further negotiation with the server.

Parameters
:   | iface | A valid pointer to a network interface |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
