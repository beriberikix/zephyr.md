---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__dhcpv4__server.html
original_path: doxygen/html/group__dhcpv4__server.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DHCPv4 server

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DHCPv4 server.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_dhcpv4\_lease\_cb\_t](#gabd37fd84bc25525d4f1aec4df8aef8b6)) (struct [net\_if](structnet__if.md) \*iface, struct dhcpv4\_addr\_slot \*lease, void \*user\_data) |
|  | Callback used while iterating over active DHCPv4 address leases. |
| typedef int(\* | [net\_dhcpv4\_server\_provider\_cb\_t](#ga416f4c6f173622d602aa122c5d3ca55e)) (struct [net\_if](structnet__if.md) \*iface, const struct dhcpv4\_client\_id \*client\_id, struct [in\_addr](structin__addr.md) \*addr, void \*user\_data) |
|  | Callback used to let application provide an address for a given client ID. |

| Functions | |
| --- | --- |
| int | [net\_dhcpv4\_server\_start](#ga2f3cc50c9428fe45540535fc66bec052) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*base\_addr) |
|  | Start DHCPv4 server instance on an iface. |
| int | [net\_dhcpv4\_server\_stop](#ga7955e5f3ff357c292a8641c0385f34e4) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop DHCPv4 server instance on an iface. |
| int | [net\_dhcpv4\_server\_foreach\_lease](#ga636b2c71a7d5f00997cba946c31c0c00) (struct [net\_if](structnet__if.md) \*iface, [net\_dhcpv4\_lease\_cb\_t](#gabd37fd84bc25525d4f1aec4df8aef8b6) cb, void \*user\_data) |
|  | Iterate over all DHCPv4 address leases on a given network interface and call callback for each lease. |
| void | [net\_dhcpv4\_server\_set\_provider\_cb](#ga1db06c0bf6a5f79334c81472b0a37bb7) ([net\_dhcpv4\_server\_provider\_cb\_t](#ga416f4c6f173622d602aa122c5d3ca55e) cb, void \*user\_data) |
|  | Set the callback used to provide addresses to the DHCP server. |

## Detailed Description

DHCPv4 server.

Since
:   3.6

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#gabd37fd84bc25525d4f1aec4df8aef8b6)net\_dhcpv4\_lease\_cb\_t

| typedef void(\* net\_dhcpv4\_lease\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, struct dhcpv4\_addr\_slot \*lease, void \*user\_data) |
| --- |

`#include <[dhcpv4_server.h](dhcpv4__server_8h.md)>`

Callback used while iterating over active DHCPv4 address leases.

Parameters
:   | iface | Pointer to the network interface |
    | --- | --- |
    | lease | Pointer to the DHPCv4 address lease slot |
    | user\_data | A valid pointer to user data or NULL |

## [◆ ](#ga416f4c6f173622d602aa122c5d3ca55e)net\_dhcpv4\_server\_provider\_cb\_t

| typedef int(\* net\_dhcpv4\_server\_provider\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, const struct dhcpv4\_client\_id \*client\_id, struct [in\_addr](structin__addr.md) \*addr, void \*user\_data) |
| --- |

`#include <[dhcpv4_server.h](dhcpv4__server_8h.md)>`

Callback used to let application provide an address for a given client ID.

This function is called before assigning an address to a client, and lets the application override the address for a given client. If the callback returns 0, addr needs to be a valid address and will be assigned to the client. If the callback returns anything non-zero, the client will be assigned an address from the pool.

Parameters
:   | iface | Pointer to the network interface |
    | --- | --- |
    | client\_id | Pointer to client requesting an address |
    | addr | Address to be assigned to client |
    | user\_data | A valid pointer to user data or NULL |

## Function Documentation

## [◆ ](#ga636b2c71a7d5f00997cba946c31c0c00)net\_dhcpv4\_server\_foreach\_lease()

| int net\_dhcpv4\_server\_foreach\_lease | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [net\_dhcpv4\_lease\_cb\_t](#gabd37fd84bc25525d4f1aec4df8aef8b6) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[dhcpv4_server.h](dhcpv4__server_8h.md)>`

Iterate over all DHCPv4 address leases on a given network interface and call callback for each lease.

In case no network interface is provided (NULL interface pointer), will iterate over all interfaces running DHCPv4 server instance.

Parameters
:   | iface | Pointer to the network interface, can be NULL |
    | --- | --- |
    | cb | User-supplied callback function to call |
    | user\_data | User specified data |

## [◆ ](#ga1db06c0bf6a5f79334c81472b0a37bb7)net\_dhcpv4\_server\_set\_provider\_cb()

| void net\_dhcpv4\_server\_set\_provider\_cb | ( | [net\_dhcpv4\_server\_provider\_cb\_t](#ga416f4c6f173622d602aa122c5d3ca55e) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[dhcpv4_server.h](dhcpv4__server_8h.md)>`

Set the callback used to provide addresses to the DHCP server.

Parameters
:   | cb | User-supplied callback function to call |
    | --- | --- |
    | user\_data | A valid pointer to user data or NULL |

## [◆ ](#ga2f3cc50c9428fe45540535fc66bec052)net\_dhcpv4\_server\_start()

| int net\_dhcpv4\_server\_start | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in\_addr](structin__addr.md) \* | *base\_addr* ) |

`#include <[dhcpv4_server.h](dhcpv4__server_8h.md)>`

Start DHCPv4 server instance on an iface.

Start DHCPv4 server on a given interface. The server will start listening for DHCPv4 Discover/Request messages on the interface and assign IPv4 addresses from the configured address pool accordingly.

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |
    | base\_addr | First IPv4 address from the DHCPv4 address pool. The number of addresses in the pool is configured statically with Kconfig (CONFIG\_NET\_DHCPV4\_SERVER\_ADDR\_COUNT). |

Returns
:   0 on success, a negative error code otherwise.

## [◆ ](#ga7955e5f3ff357c292a8641c0385f34e4)net\_dhcpv4\_server\_stop()

| int net\_dhcpv4\_server\_stop | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dhcpv4_server.h](dhcpv4__server_8h.md)>`

Stop DHCPv4 server instance on an iface.

Stop DHCPv4 server on a given interface. DHCPv4 requests will no longer be handled on the interface, and all of the allocations are cleared.

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |

Returns
:   0 on success, a negative error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
