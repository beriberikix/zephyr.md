---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ethernet__bridge_8h.html
original_path: doxygen/html/ethernet__bridge_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_bridge.h File Reference

Ethernet Bridge public header file.
[More...](#details)

`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](ethernet__bridge_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ETH\_BRIDGE\_INIT](group__eth__bridge.md#gaeafd2e30e2f484117797570dd5834de0)(name) |
|  | Statically define and initialize a bridge instance. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [eth\_bridge\_cb\_t](group__eth__bridge.md#gad9ace58ad82de9c0778b083fe50eb7a8)) (struct eth\_bridge \*br, void \*user\_data) |
|  | Callback used while iterating over bridge instances. |

| Functions | |
| --- | --- |
| int | [eth\_bridge\_iface\_add](group__eth__bridge.md#ga2a2f2fad28df21210bed17ef2a38fb00) (struct eth\_bridge \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Add an Ethernet network interface to a bridge. |
| int | [eth\_bridge\_iface\_remove](group__eth__bridge.md#ga08a44cd033b2b3aa565bbec4d815fdd3) (struct eth\_bridge \*br, struct [net\_if](structnet__if.md) \*iface) |
|  | Remove an Ethernet network interface from a bridge. |
| int | [eth\_bridge\_iface\_allow\_tx](group__eth__bridge.md#gac7124d2ab5bbd11908a86709ba0e85ce) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) allow) |
|  | Enable/disable transmission mode for a bridged interface. |
| int | [eth\_bridge\_listener\_add](group__eth__bridge.md#ga06ff0ece90f1aee17e4fa448ccfa44a0) (struct eth\_bridge \*br, struct eth\_bridge\_listener \*l) |
|  | Add (register) a listener to the bridge. |
| int | [eth\_bridge\_listener\_remove](group__eth__bridge.md#gafe7ea985453c51223d62f5e84509ef59) (struct eth\_bridge \*br, struct eth\_bridge\_listener \*l) |
|  | Remove (unregister) a listener from the bridge. |
| int | [eth\_bridge\_get\_index](group__eth__bridge.md#gaaec8cb29a13b3a439b0f9d7cef358bb2) (struct eth\_bridge \*br) |
|  | Get bridge index according to pointer. |
| struct eth\_bridge \* | [eth\_bridge\_get\_by\_index](group__eth__bridge.md#ga94bd48c3f6ff6e51dcb4d194515db8b6) (int index) |
|  | Get bridge instance according to index. |
| void | [net\_eth\_bridge\_foreach](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31) ([eth\_bridge\_cb\_t](group__eth__bridge.md#gad9ace58ad82de9c0778b083fe50eb7a8) cb, void \*user\_data) |
|  | Go through all the bridge instances in order to get information about them. |

## Detailed Description

Ethernet Bridge public header file.

Ethernet Bridges connect two or more Ethernet networks together and transparently forward packets from one network to the others as if they were part of the same network.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_bridge.h](ethernet__bridge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
