---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ethernet__bridge_8h_source.html
original_path: doxygen/html/ethernet__bridge_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

11 \* Copyright (c) 2024 Nordic Semiconductor

12 \*

13 \* SPDX-License-Identifier: Apache-2.0

14 \*/

15

16#ifndef ZEPHYR\_INCLUDE\_NET\_ETHERNET\_BRIDGE\_H\_

17#define ZEPHYR\_INCLUDE\_NET\_ETHERNET\_BRIDGE\_H\_

18

19#include <[zephyr/sys/slist.h](slist_8h.md)>

20#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

34

36

37#if defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

38#define NET\_ETHERNET\_BRIDGE\_ETH\_INTERFACE\_COUNT CONFIG\_NET\_ETHERNET\_BRIDGE\_ETH\_INTERFACE\_COUNT

39#else

40#define NET\_ETHERNET\_BRIDGE\_ETH\_INTERFACE\_COUNT 1

41#endif

42

43struct eth\_bridge\_iface\_context {

44 /\* Lock to protect access to interface array below \*/

45 struct k\_mutex lock;

46

47 /\* The actual bridge virtual interface \*/

48 struct net\_if \*iface;

49

50 /\* What Ethernet interfaces are bridged together \*/

51 struct net\_if \*eth\_iface[NET\_ETHERNET\_BRIDGE\_ETH\_INTERFACE\_COUNT];

52

53 /\* How many interfaces are bridged atm \*/

54 size\_t count;

55

56 /\* Bridge instance id \*/

57 int id;

58

59 /\* Is the bridge interface initialized \*/

60 bool is\_init : 1;

61

62 /\* Has user configured the bridge \*/

63 bool is\_setup : 1;

64

65 /\* Is the interface enabled or not \*/

66 bool status : 1;

67};

68

70

[ 85](group__eth__bridge.md#ga19756a715b210181001b04987a5e23a5)int [eth\_bridge\_iface\_add](group__eth__bridge.md#ga19756a715b210181001b04987a5e23a5)(struct [net\_if](structnet__if.md) \*br, struct [net\_if](structnet__if.md) \*iface);

86

[ 100](group__eth__bridge.md#ga671496bc299581b8d4d3ec9fd2ff1991)int [eth\_bridge\_iface\_remove](group__eth__bridge.md#ga671496bc299581b8d4d3ec9fd2ff1991)(struct [net\_if](structnet__if.md) \*br, struct [net\_if](structnet__if.md) \*iface);

101

[ 109](group__eth__bridge.md#gafd194ba73599d0e37c8302e25d8208e4)int [eth\_bridge\_get\_index](group__eth__bridge.md#gafd194ba73599d0e37c8302e25d8208e4)(struct [net\_if](structnet__if.md) \*br);

110

[ 118](group__eth__bridge.md#ga6b88a47138b199e65da602e0e63f13d1)struct [net\_if](structnet__if.md) \*[eth\_bridge\_get\_by\_index](group__eth__bridge.md#ga6b88a47138b199e65da602e0e63f13d1)(int index);

119

[ 127](group__eth__bridge.md#gac7d0b995294279cc35408c69ee437778)typedef void (\*[eth\_bridge\_cb\_t](group__eth__bridge.md#gac7d0b995294279cc35408c69ee437778))(struct eth\_bridge\_iface\_context \*br, void \*user\_data);

128

[ 137](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31)void [net\_eth\_bridge\_foreach](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31)([eth\_bridge\_cb\_t](group__eth__bridge.md#gac7d0b995294279cc35408c69ee437778) cb, void \*user\_data);

138

142

143#ifdef \_\_cplusplus

144}

145#endif

146

147#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_BRIDGE\_H\_ \*/

[eth\_bridge\_iface\_add](group__eth__bridge.md#ga19756a715b210181001b04987a5e23a5)

int eth\_bridge\_iface\_add(struct net\_if \*br, struct net\_if \*iface)

Add an Ethernet network interface to a bridge.

[net\_eth\_bridge\_foreach](group__eth__bridge.md#ga5bb8dba7fbde9f2095e19f1912855d31)

void net\_eth\_bridge\_foreach(eth\_bridge\_cb\_t cb, void \*user\_data)

Go through all the bridge context instances in order to get information about them.

[eth\_bridge\_iface\_remove](group__eth__bridge.md#ga671496bc299581b8d4d3ec9fd2ff1991)

int eth\_bridge\_iface\_remove(struct net\_if \*br, struct net\_if \*iface)

Remove an Ethernet network interface from a bridge.

[eth\_bridge\_get\_by\_index](group__eth__bridge.md#ga6b88a47138b199e65da602e0e63f13d1)

struct net\_if \* eth\_bridge\_get\_by\_index(int index)

Get bridge instance according to index.

[eth\_bridge\_cb\_t](group__eth__bridge.md#gac7d0b995294279cc35408c69ee437778)

void(\* eth\_bridge\_cb\_t)(struct eth\_bridge\_iface\_context \*br, void \*user\_data)

Callback used while iterating over bridge instances.

**Definition** ethernet\_bridge.h:127

[eth\_bridge\_get\_index](group__eth__bridge.md#gafd194ba73599d0e37c8302e25d8208e4)

int eth\_bridge\_get\_index(struct net\_if \*br)

Get bridge index according to pointer.

[slist.h](slist_8h.md)

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_bridge.h](ethernet__bridge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
