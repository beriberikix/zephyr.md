---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__eth__bridge.html
original_path: doxygen/html/group__eth__bridge.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet Bridging API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Ethernet Bridging API.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [eth\_bridge\_cb\_t](#gac7d0b995294279cc35408c69ee437778)) (struct eth\_bridge\_iface\_context \*br, void \*user\_data) |
|  | Callback used while iterating over bridge instances. |

| Functions | |
| --- | --- |
| int | [eth\_bridge\_iface\_add](#ga19756a715b210181001b04987a5e23a5) (struct [net\_if](structnet__if.md) \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Add an Ethernet network interface to a bridge. |
| int | [eth\_bridge\_iface\_remove](#ga671496bc299581b8d4d3ec9fd2ff1991) (struct [net\_if](structnet__if.md) \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Remove an Ethernet network interface from a bridge. |
| int | [eth\_bridge\_get\_index](#gafd194ba73599d0e37c8302e25d8208e4) (struct [net\_if](structnet__if.md) \*br) |
|  | Get bridge index according to pointer. |
| struct [net\_if](structnet__if.md) \* | [eth\_bridge\_get\_by\_index](#ga6b88a47138b199e65da602e0e63f13d1) (int index) |
|  | Get bridge instance according to index. |
| void | [net\_eth\_bridge\_foreach](#ga5bb8dba7fbde9f2095e19f1912855d31) ([eth\_bridge\_cb\_t](#gac7d0b995294279cc35408c69ee437778) cb, void \*user\_data) |
|  | Go through all the bridge context instances in order to get information about them. |

## Detailed Description

Ethernet Bridging API.

Since
:   2.7

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#gac7d0b995294279cc35408c69ee437778)eth\_bridge\_cb\_t

| typedef void(\* eth\_bridge\_cb\_t) (struct eth\_bridge\_iface\_context \*br, void \*user\_data) |
| --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Callback used while iterating over bridge instances.

Parameters
:   | br | Pointer to bridge context instance |
    | --- | --- |
    | user\_data | User supplied data |

## Function Documentation

## [◆ ](#ga6b88a47138b199e65da602e0e63f13d1)eth\_bridge\_get\_by\_index()

| struct [net\_if](structnet__if.md) \* eth\_bridge\_get\_by\_index | ( | int | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Get bridge instance according to index.

Parameters
:   | index | Bridge instance index |
    | --- | --- |

Returns
:   Pointer to bridge interface or NULL if not found.

## [◆ ](#gafd194ba73599d0e37c8302e25d8208e4)eth\_bridge\_get\_index()

| int eth\_bridge\_get\_index | ( | struct [net\_if](structnet__if.md) \* | *br* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Get bridge index according to pointer.

Parameters
:   | br | Pointer to bridge instance |
    | --- | --- |

Returns
:   Bridge index

## [◆ ](#ga19756a715b210181001b04987a5e23a5)eth\_bridge\_iface\_add()

| int eth\_bridge\_iface\_add | ( | struct [net\_if](structnet__if.md) \* | *br*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Add an Ethernet network interface to a bridge.

This adds a network interface to a bridge. The interface is then put into promiscuous mode. After more than one Ethernet interfaces are added to the bridge interface, the bridge interface is setup. After the setup is done, the bridge interface can be brought up so that it can start bridging L2 traffic.

Parameters
:   | br | A pointer to a bridge interface |
    | --- | --- |
    | iface | Interface to add |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#ga671496bc299581b8d4d3ec9fd2ff1991)eth\_bridge\_iface\_remove()

| int eth\_bridge\_iface\_remove | ( | struct [net\_if](structnet__if.md) \* | *br*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Remove an Ethernet network interface from a bridge.

If the bridge interface setup has only one Ethernet interface left after this function call, the bridge is disabled as it cannot bridge the L2 traffic any more. The bridge interface is left in UP state if this case.

Parameters
:   | br | A pointer to a bridge interface |
    | --- | --- |
    | iface | Interface to remove |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#ga5bb8dba7fbde9f2095e19f1912855d31)net\_eth\_bridge\_foreach()

| void net\_eth\_bridge\_foreach | ( | [eth\_bridge\_cb\_t](#gac7d0b995294279cc35408c69ee437778) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Go through all the bridge context instances in order to get information about them.

This is mainly useful in net-shell to print data about currently active bridges.

Parameters
:   | cb | Callback to call for each bridge instance |
    | --- | --- |
    | user\_data | User supplied data |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
