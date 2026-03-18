---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__eth__bridge.html
original_path: doxygen/html/group__eth__bridge.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet Bridging API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Ethernet Bridging API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [eth\_bridge\_iface\_context](structeth__bridge__iface__context.md) |
| struct | [eth\_bridge\_listener](structeth__bridge__listener.md) |

| Macros | |
| --- | --- |
| #define | [ETH\_BRIDGE\_INIT](#gaeafd2e30e2f484117797570dd5834de0)(name) |
|  | Statically define and initialize a bridge instance. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [eth\_bridge\_cb\_t](#gad9ace58ad82de9c0778b083fe50eb7a8)) (struct eth\_bridge \*br, void \*user\_data) |
|  | Callback used while iterating over bridge instances. |

| Functions | |
| --- | --- |
| int | [eth\_bridge\_iface\_add](#ga2a2f2fad28df21210bed17ef2a38fb00) (struct eth\_bridge \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Add an Ethernet network interface to a bridge. |
| int | [eth\_bridge\_iface\_remove](#ga08a44cd033b2b3aa565bbec4d815fdd3) (struct eth\_bridge \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Remove an Ethernet network interface from a bridge. |
| int | [eth\_bridge\_iface\_allow\_tx](#gac7124d2ab5bbd11908a86709ba0e85ce) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) allow) |
|  | Enable/disable transmission mode for a bridged interface. |
| int | [eth\_bridge\_listener\_add](#ga06ff0ece90f1aee17e4fa448ccfa44a0) (struct eth\_bridge \*br, struct [eth\_bridge\_listener](structeth__bridge__listener.md) \*l) |
|  | Add (register) a listener to the bridge. |
| int | [eth\_bridge\_listener\_remove](#gafe7ea985453c51223d62f5e84509ef59) (struct eth\_bridge \*br, struct [eth\_bridge\_listener](structeth__bridge__listener.md) \*l) |
|  | Remove (unregister) a listener from the bridge. |
| int | [eth\_bridge\_get\_index](#gaaec8cb29a13b3a439b0f9d7cef358bb2) (struct eth\_bridge \*br) |
|  | Get bridge index according to pointer. |
| struct eth\_bridge \* | [eth\_bridge\_get\_by\_index](#ga94bd48c3f6ff6e51dcb4d194515db8b6) (int index) |
|  | Get bridge instance according to index. |
| void | [net\_eth\_bridge\_foreach](#ga5bb8dba7fbde9f2095e19f1912855d31) ([eth\_bridge\_cb\_t](#gad9ace58ad82de9c0778b083fe50eb7a8) cb, void \*user\_data) |
|  | Go through all the bridge instances in order to get information about them. |

## Detailed Description

Ethernet Bridging API.

## Macro Definition Documentation

## [◆ ](#gaeafd2e30e2f484117797570dd5834de0)ETH\_BRIDGE\_INIT

| #define ETH\_BRIDGE\_INIT | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(eth\_bridge, name) = \

ETH\_BRIDGE\_INITIALIZER(name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Statically define and initialize a bridge instance.

Parameters
:   | name | Name of the bridge object |
    | --- | --- |

## Typedef Documentation

## [◆ ](#gad9ace58ad82de9c0778b083fe50eb7a8)eth\_bridge\_cb\_t

| typedef void(\* eth\_bridge\_cb\_t) (struct eth\_bridge \*br, void \*user\_data) |
| --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Callback used while iterating over bridge instances.

Parameters
:   | br | Pointer to bridge instance |
    | --- | --- |
    | user\_data | User supplied data |

## Function Documentation

## [◆ ](#ga94bd48c3f6ff6e51dcb4d194515db8b6)eth\_bridge\_get\_by\_index()

| struct eth\_bridge \* eth\_bridge\_get\_by\_index | ( | int | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Get bridge instance according to index.

Parameters
:   | index | Bridge instance index |
    | --- | --- |

Returns
:   Pointer to bridge instance or NULL if not found.

## [◆ ](#gaaec8cb29a13b3a439b0f9d7cef358bb2)eth\_bridge\_get\_index()

| int eth\_bridge\_get\_index | ( | struct eth\_bridge \* | *br* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Get bridge index according to pointer.

Parameters
:   | br | Pointer to bridge instance |
    | --- | --- |

Returns
:   Bridge index

## [◆ ](#ga2a2f2fad28df21210bed17ef2a38fb00)eth\_bridge\_iface\_add()

| int eth\_bridge\_iface\_add | ( | struct eth\_bridge \* | *br*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Add an Ethernet network interface to a bridge.

This adds a network interface to a bridge. The interface is then put into promiscuous mode, all packets received by this interface are sent to the bridge, and any other packets sent to the bridge (with some exceptions) are transmitted via this interface.

For transmission from the bridge to occur via this interface, it is necessary to enable TX mode with eth\_bridge\_iface\_tx(). TX mode is initially disabled.

Once an interface is added to a bridge, all its incoming traffic is diverted to the bridge. However, packets sent out with [net\_if\_queue\_tx()](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed "Queue a packet to the net interface TX queue.") via this interface are not subjected to the bridge.

Parameters
:   | br | A pointer to an initialized bridge object |
    | --- | --- |
    | iface | Interface to add |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#gac7124d2ab5bbd11908a86709ba0e85ce)eth\_bridge\_iface\_allow\_tx()

| int eth\_bridge\_iface\_allow\_tx | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *allow* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Enable/disable transmission mode for a bridged interface.

When TX mode is off, the interface may receive packets and send them to the bridge but no packets coming from the bridge will be sent through this interface. When TX mode is on, both incoming and outgoing packets are allowed.

Parameters
:   | iface | Interface to configure |
    | --- | --- |
    | allow | true to activate TX mode, false otherwise |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#ga08a44cd033b2b3aa565bbec4d815fdd3)eth\_bridge\_iface\_remove()

| int eth\_bridge\_iface\_remove | ( | struct eth\_bridge \* | *br*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Remove an Ethernet network interface from a bridge.

Parameters
:   | br | A pointer to an initialized bridge object |
    | --- | --- |
    | iface | Interface to remove |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#ga06ff0ece90f1aee17e4fa448ccfa44a0)eth\_bridge\_listener\_add()

| int eth\_bridge\_listener\_add | ( | struct eth\_bridge \* | *br*, |
| --- | --- | --- | --- |
|  |  | struct [eth\_bridge\_listener](structeth__bridge__listener.md) \* | *l* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Add (register) a listener to the bridge.

This lets a software listener register a pointer to a provided FIFO for receiving packets sent to the bridge. The listener is responsible for emptying the FIFO with [k\_fifo\_get()](group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6 "Get an element from a FIFO queue.") which will return a struct [net\_pkt](structnet__pkt.md "Network packet.") pointer, and releasing the packet with [net\_pkt\_unref()](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099 "Place packet back into the available packets slab.") when done with it.

The listener wishing not to receive any more packets should simply unregister itself with [eth\_bridge\_listener\_remove()](#gafe7ea985453c51223d62f5e84509ef59).

Parameters
:   | br | A pointer to an initialized bridge object |
    | --- | --- |
    | l | A pointer to an initialized listener instance. |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#gafe7ea985453c51223d62f5e84509ef59)eth\_bridge\_listener\_remove()

| int eth\_bridge\_listener\_remove | ( | struct eth\_bridge \* | *br*, |
| --- | --- | --- | --- |
|  |  | struct [eth\_bridge\_listener](structeth__bridge__listener.md) \* | *l* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Remove (unregister) a listener from the bridge.

Parameters
:   | br | A pointer to an initialized bridge object |
    | --- | --- |
    | l | A pointer to the listener instance to be removed. |

Returns
:   0 if OK, negative error code otherwise.

## [◆ ](#ga5bb8dba7fbde9f2095e19f1912855d31)net\_eth\_bridge\_foreach()

| void net\_eth\_bridge\_foreach | ( | [eth\_bridge\_cb\_t](#gad9ace58ad82de9c0778b083fe50eb7a8) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[ethernet_bridge.h](ethernet__bridge_8h.md)>`

Go through all the bridge instances in order to get information about them.

This is mainly useful in net-shell to print data about currently active bridges.

Parameters
:   | cb | Callback to call for each bridge instance |
    | --- | --- |
    | user\_data | User supplied data |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
