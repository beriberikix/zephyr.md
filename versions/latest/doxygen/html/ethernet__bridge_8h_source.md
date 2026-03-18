---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ethernet__bridge_8h_source.html
original_path: doxygen/html/ethernet__bridge_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_bridge.h

[Go to the documentation of this file.](ethernet__bridge_8h.md)

1

8

9/\*

10 \* Copyright (c) 2021 BayLibre SAS

11 \*

12 \* SPDX-License-Identifier: Apache-2.0

13 \*/

14

15#ifndef ZEPHYR\_INCLUDE\_NET\_ETHERNET\_BRIDGE\_H\_

16#define ZEPHYR\_INCLUDE\_NET\_ETHERNET\_BRIDGE\_H\_

17

18#include <[zephyr/sys/slist.h](slist_8h.md)>

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

31

33

34struct eth\_bridge {

35 struct k\_mutex lock;

36 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) interfaces;

37 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) listeners;

38 bool initialized;

39};

40

41#define ETH\_BRIDGE\_INITIALIZER(obj) \

42 { \

43 .lock = { }, \

44 .interfaces = SYS\_SLIST\_STATIC\_INIT(&obj.interfaces), \

45 .listeners = SYS\_SLIST\_STATIC\_INIT(&obj.listeners), \

46 }

47

49

[ 55](group__eth__bridge.md#gaeafd2e30e2f484117797570dd5834de0)#define ETH\_BRIDGE\_INIT(name) \

56 STRUCT\_SECTION\_ITERABLE(eth\_bridge, name) = \

57 ETH\_BRIDGE\_INITIALIZER(name)

58

[ 59](structeth__bridge__iface__context.md)struct [eth\_bridge\_iface\_context](structeth__bridge__iface__context.md) {

[ 60](structeth__bridge__iface__context.md#ad88d752c988d4a7be637b4f682db589f) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structeth__bridge__iface__context.md#ad88d752c988d4a7be637b4f682db589f);

[ 61](structeth__bridge__iface__context.md#a5825456106f3df291a623c249cc7144c) struct eth\_bridge \*[instance](structeth__bridge__iface__context.md#a5825456106f3df291a623c249cc7144c);

[ 62](structeth__bridge__iface__context.md#a278c0a37617e9e5639f28220dc9ef7a0) bool [allow\_tx](structeth__bridge__iface__context.md#a278c0a37617e9e5639f28220dc9ef7a0);

63};

64

[ 65](structeth__bridge__listener.md)struct [eth\_bridge\_listener](structeth__bridge__listener.md) {

[ 66](structeth__bridge__listener.md#a4f76bce3bba51650278950c706924fa4) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structeth__bridge__listener.md#a4f76bce3bba51650278950c706924fa4);

[ 67](structeth__bridge__listener.md#a47da5284374203f242df88fac1c4a428) struct [k\_fifo](structk__fifo.md) [pkt\_queue](structeth__bridge__listener.md#a47da5284374203f242df88fac1c4a428);

68};

69

[ 91](group__eth__bridge.md#ga2a2f2fad28df21210bed17ef2a38fb00)int [eth\_bridge\_iface\_add](group__eth__bridge.md#ga2a2f2fad28df21210bed17ef2a38fb00)(struct eth\_bridge \*br, struct [net\_if](structnet__if.md) \*iface);

92

[ 101](group__eth__bridge.md#ga08a44cd033b2b3aa565bbec4d815fdd3)int [eth\_bridge\_iface\_remove](group__eth__bridge.md#ga08a44cd033b2b3aa565bbec4d815fdd3)(struct eth\_bridge \*br, struct [net\_if](structnet__if.md) \*iface);

102

[ 116](group__eth__bridge.md#gac7124d2ab5bbd11908a86709ba0e85ce)int [eth\_bridge\_iface\_allow\_tx](group__eth__bridge.md#gac7124d2ab5bbd11908a86709ba0e85ce)(struct [net\_if](structnet__if.md) \*iface, bool allow);

117

[ 134](group__eth__bridge.md#ga06ff0ece90f1aee17e4fa448ccfa44a0)int [eth\_bridge\_listener\_add](group__eth__bridge.md#ga06ff0ece90f1aee17e4fa448ccfa44a0)(struct eth\_bridge \*br, struct [eth\_bridge\_listener](structeth__bridge__listener.md) \*l);

135

[ 144](group__eth__bridge.md#gafe7ea985453c51223d62f5e84509ef59)int [eth\_bridge\_listener\_remove](group__eth__bridge.md#gafe7ea985453c51223d62f5e84509ef59)(struct eth\_bridge \*br, struct [eth\_bridge\_listener](structeth__bridge__listener.md) \*l);

145

[ 153](group__eth__bridge.md#gaaec8cb29a13b3a439b0f9d7cef358bb2)int [eth\_bridge\_get\_index](group__eth__bridge.md#gaaec8cb29a13b3a439b0f9d7cef358bb2)(struct eth\_bridge \*br);

154

[ 162](group__eth__bridge.md#ga94bd48c3f6ff6e51dcb4d194515db8b6)struct eth\_bridge \*[eth\_bridge\_get\_by\_index](group__eth__bridge.md#ga94bd48c3f6ff6e51dcb4d194515db8b6)(int index);

163

[ 171](group__eth__bridge.md#gad9ace58ad82de9c0778b083fe50eb7a8)typedef void (\*[eth\_bridge\_cb\_t](group__eth__bridge.md#gad9ace58ad82de9c0778b083fe50eb7a8))(struct eth\_bridge \*br, void \*user\_data);

172

[ 181](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31)void [net\_eth\_bridge\_foreach](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31)([eth\_bridge\_cb\_t](group__eth__bridge.md#gad9ace58ad82de9c0778b083fe50eb7a8) cb, void \*user\_data);

182

186

187#ifdef \_\_cplusplus

188}

189#endif

190

191#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_BRIDGE\_H\_ \*/

[eth\_bridge\_listener\_add](group__eth__bridge.md#ga06ff0ece90f1aee17e4fa448ccfa44a0)

int eth\_bridge\_listener\_add(struct eth\_bridge \*br, struct eth\_bridge\_listener \*l)

Add (register) a listener to the bridge.

[eth\_bridge\_iface\_remove](group__eth__bridge.md#ga08a44cd033b2b3aa565bbec4d815fdd3)

int eth\_bridge\_iface\_remove(struct eth\_bridge \*br, struct net\_if \*iface)

Remove an Ethernet network interface from a bridge.

[eth\_bridge\_iface\_add](group__eth__bridge.md#ga2a2f2fad28df21210bed17ef2a38fb00)

int eth\_bridge\_iface\_add(struct eth\_bridge \*br, struct net\_if \*iface)

Add an Ethernet network interface to a bridge.

[net\_eth\_bridge\_foreach](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31)

void net\_eth\_bridge\_foreach(eth\_bridge\_cb\_t cb, void \*user\_data)

Go through all the bridge instances in order to get information about them.

[eth\_bridge\_get\_by\_index](group__eth__bridge.md#ga94bd48c3f6ff6e51dcb4d194515db8b6)

struct eth\_bridge \* eth\_bridge\_get\_by\_index(int index)

Get bridge instance according to index.

[eth\_bridge\_get\_index](group__eth__bridge.md#gaaec8cb29a13b3a439b0f9d7cef358bb2)

int eth\_bridge\_get\_index(struct eth\_bridge \*br)

Get bridge index according to pointer.

[eth\_bridge\_iface\_allow\_tx](group__eth__bridge.md#gac7124d2ab5bbd11908a86709ba0e85ce)

int eth\_bridge\_iface\_allow\_tx(struct net\_if \*iface, bool allow)

Enable/disable transmission mode for a bridged interface.

[eth\_bridge\_cb\_t](group__eth__bridge.md#gad9ace58ad82de9c0778b083fe50eb7a8)

void(\* eth\_bridge\_cb\_t)(struct eth\_bridge \*br, void \*user\_data)

Callback used while iterating over bridge instances.

**Definition** ethernet\_bridge.h:171

[eth\_bridge\_listener\_remove](group__eth__bridge.md#gafe7ea985453c51223d62f5e84509ef59)

int eth\_bridge\_listener\_remove(struct eth\_bridge \*br, struct eth\_bridge\_listener \*l)

Remove (unregister) a listener from the bridge.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[eth\_bridge\_iface\_context](structeth__bridge__iface__context.md)

**Definition** ethernet\_bridge.h:59

[eth\_bridge\_iface\_context::allow\_tx](structeth__bridge__iface__context.md#a278c0a37617e9e5639f28220dc9ef7a0)

bool allow\_tx

**Definition** ethernet\_bridge.h:62

[eth\_bridge\_iface\_context::instance](structeth__bridge__iface__context.md#a5825456106f3df291a623c249cc7144c)

struct eth\_bridge \* instance

**Definition** ethernet\_bridge.h:61

[eth\_bridge\_iface\_context::node](structeth__bridge__iface__context.md#ad88d752c988d4a7be637b4f682db589f)

sys\_snode\_t node

**Definition** ethernet\_bridge.h:60

[eth\_bridge\_listener](structeth__bridge__listener.md)

**Definition** ethernet\_bridge.h:65

[eth\_bridge\_listener::pkt\_queue](structeth__bridge__listener.md#a47da5284374203f242df88fac1c4a428)

struct k\_fifo pkt\_queue

**Definition** ethernet\_bridge.h:67

[eth\_bridge\_listener::node](structeth__bridge__listener.md#a4f76bce3bba51650278950c706924fa4)

sys\_snode\_t node

**Definition** ethernet\_bridge.h:66

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_bridge.h](ethernet__bridge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
