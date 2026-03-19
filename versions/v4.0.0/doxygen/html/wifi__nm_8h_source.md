---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/wifi__nm_8h_source.html
original_path: doxygen/html/wifi__nm_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_nm.h

[Go to the documentation of this file.](wifi__nm_8h.md)

1

7

8/\*

9 \* Copyright (c) 2023 Nordic Semiconductor ASA.

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_NET\_WIFI\_NM\_H\_

15#define ZEPHYR\_INCLUDE\_ZEPHYR\_NET\_WIFI\_NM\_H\_

16

17#include <[zephyr/kernel.h](kernel_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/net/net\_if.h](net__if_8h.md)>

21#include <[zephyr/net/wifi\_mgmt.h](wifi__mgmt_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 36](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1)enum [wifi\_nm\_iface\_type](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1) {

[ 38](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468) [WIFI\_TYPE\_STA](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468) = 0,

[ 40](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345) [WIFI\_TYPE\_SAP](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345),

41};

42

[ 46](structwifi__nm__mgd__iface.md)struct [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md) {

[ 48](structwifi__nm__mgd__iface.md#adf401562151097f8be118fc609e7f86a) unsigned char [type](structwifi__nm__mgd__iface.md#adf401562151097f8be118fc609e7f86a);

[ 50](structwifi__nm__mgd__iface.md#abd10caf51a7890d24af51c91a58f1e4d) struct [net\_if](structnet__if.md) \*[iface](structwifi__nm__mgd__iface.md#abd10caf51a7890d24af51c91a58f1e4d);

51};

52

[ 56](structwifi__nm__instance.md)struct [wifi\_nm\_instance](structwifi__nm__instance.md) {

[ 58](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af) const char \*[name](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af);

[ 60](structwifi__nm__instance.md#a65e73ea84dfd64dc17f0af03477362ae) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*[ops](structwifi__nm__instance.md#a65e73ea84dfd64dc17f0af03477362ae);

[ 62](structwifi__nm__instance.md#a02184a7739d4b9a31b6142df3e0463c0) struct [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md) [mgd\_ifaces](structwifi__nm__instance.md#a02184a7739d4b9a31b6142df3e0463c0)[CONFIG\_WIFI\_NM\_MAX\_MANAGED\_INTERFACES];

63};

64

66

67#define WIFI\_NM\_NAME(name) wifi\_nm\_##name

68

69#define DEFINE\_WIFI\_NM\_INSTANCE(\_name, \_ops) \

70 static STRUCT\_SECTION\_ITERABLE(wifi\_nm\_instance, WIFI\_NM\_NAME(\_name)) = { \

71 .name = STRINGIFY(\_name), \

72 .ops = \_ops, \

73 .mgd\_ifaces = {}, \

74 }

75

77

[ 84](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed)struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*[wifi\_nm\_get\_instance](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed)(const char \*[name](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af));

85

[ 92](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3)struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*[wifi\_nm\_get\_instance\_iface](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3)(struct [net\_if](structnet__if.md) \*iface);

93

[ 100](group__wifi__nm.md#ga6a598af94e36a1f4ade05d7a18c019f5)unsigned char [wifi\_nm\_get\_type\_iface](group__wifi__nm.md#ga6a598af94e36a1f4ade05d7a18c019f5)(struct [net\_if](structnet__if.md) \*iface);

101

[ 110](group__wifi__nm.md#gaa89e5acfa5eebc9267aa7ed2ce3adc39)bool [wifi\_nm\_iface\_is\_sta](group__wifi__nm.md#gaa89e5acfa5eebc9267aa7ed2ce3adc39)(struct [net\_if](structnet__if.md) \*iface);

111

[ 120](group__wifi__nm.md#ga963f646981e9a64c9e61659e40c9880e)bool [wifi\_nm\_iface\_is\_sap](group__wifi__nm.md#ga963f646981e9a64c9e61659e40c9880e)(struct [net\_if](structnet__if.md) \*iface);

121

[ 133](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb)int [wifi\_nm\_register\_mgd\_iface](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb)(struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface);

134

[ 147](group__wifi__nm.md#gafea087a6c50d6ad05933ef62546868d6)int [wifi\_nm\_register\_mgd\_type\_iface](group__wifi__nm.md#gafea087a6c50d6ad05933ef62546868d6)(struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm,

148 enum [wifi\_nm\_iface\_type](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1) type, struct [net\_if](structnet__if.md) \*iface);

149

[ 158](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff)int [wifi\_nm\_unregister\_mgd\_iface](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff)(struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface);

159

163

164#ifdef \_\_cplusplus

165}

166#endif

167#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_NET\_WIFI\_NM\_H\_ \*/

[wifi\_nm\_register\_mgd\_iface](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb)

int wifi\_nm\_register\_mgd\_iface(struct wifi\_nm\_instance \*nm, struct net\_if \*iface)

Register a managed interface.

[wifi\_nm\_unregister\_mgd\_iface](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff)

int wifi\_nm\_unregister\_mgd\_iface(struct wifi\_nm\_instance \*nm, struct net\_if \*iface)

Unregister managed interface.

[wifi\_nm\_get\_type\_iface](group__wifi__nm.md#ga6a598af94e36a1f4ade05d7a18c019f5)

unsigned char wifi\_nm\_get\_type\_iface(struct net\_if \*iface)

Get a Wi-Fi type for a given interface.

[wifi\_nm\_get\_instance](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed)

struct wifi\_nm\_instance \* wifi\_nm\_get\_instance(const char \*name)

Get a Network manager instance for a given name.

[wifi\_nm\_get\_instance\_iface](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3)

struct wifi\_nm\_instance \* wifi\_nm\_get\_instance\_iface(struct net\_if \*iface)

Get a Network manager instance for a given interface.

[wifi\_nm\_iface\_is\_sap](group__wifi__nm.md#ga963f646981e9a64c9e61659e40c9880e)

bool wifi\_nm\_iface\_is\_sap(struct net\_if \*iface)

Check if the interface is a Wi-Fi Soft AP interface.

[wifi\_nm\_iface\_is\_sta](group__wifi__nm.md#gaa89e5acfa5eebc9267aa7ed2ce3adc39)

bool wifi\_nm\_iface\_is\_sta(struct net\_if \*iface)

Check if the interface is a Wi-Fi station interface.

[wifi\_nm\_iface\_type](group__wifi__nm.md#gadba91c7f3ef5027f7d2a01229372a1a1)

wifi\_nm\_iface\_type

Types of Wi-Fi interface.

**Definition** wifi\_nm.h:36

[wifi\_nm\_register\_mgd\_type\_iface](group__wifi__nm.md#gafea087a6c50d6ad05933ef62546868d6)

int wifi\_nm\_register\_mgd\_type\_iface(struct wifi\_nm\_instance \*nm, enum wifi\_nm\_iface\_type type, struct net\_if \*iface)

Register a managed interface.

[WIFI\_TYPE\_STA](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468)

@ WIFI\_TYPE\_STA

IEEE 802.11 Wi-Fi Station.

**Definition** wifi\_nm.h:38

[WIFI\_TYPE\_SAP](group__wifi__nm.md#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345)

@ WIFI\_TYPE\_SAP

IEEE 802.11 Wi-Fi Soft AP.

**Definition** wifi\_nm.h:40

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:1206

[wifi\_nm\_instance](structwifi__nm__instance.md)

WiFi Network manager instance.

**Definition** wifi\_nm.h:56

[wifi\_nm\_instance::mgd\_ifaces](structwifi__nm__instance.md#a02184a7739d4b9a31b6142df3e0463c0)

struct wifi\_nm\_mgd\_iface mgd\_ifaces[CONFIG\_WIFI\_NM\_MAX\_MANAGED\_INTERFACES]

List of Managed interfaces.

**Definition** wifi\_nm.h:62

[wifi\_nm\_instance::ops](structwifi__nm__instance.md#a65e73ea84dfd64dc17f0af03477362ae)

const struct wifi\_mgmt\_ops \* ops

Wi-Fi Management operations.

**Definition** wifi\_nm.h:60

[wifi\_nm\_instance::name](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af)

const char \* name

Name of the Network manager instance.

**Definition** wifi\_nm.h:58

[wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md)

WiFi Network Managed interfaces.

**Definition** wifi\_nm.h:46

[wifi\_nm\_mgd\_iface::iface](structwifi__nm__mgd__iface.md#abd10caf51a7890d24af51c91a58f1e4d)

struct net\_if \* iface

Managed net interfaces.

**Definition** wifi\_nm.h:50

[wifi\_nm\_mgd\_iface::type](structwifi__nm__mgd__iface.md#adf401562151097f8be118fc609e7f86a)

unsigned char type

Wi-Fi interface type.

**Definition** wifi\_nm.h:48

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[wifi\_mgmt.h](wifi__mgmt_8h.md)

WiFi L2 stack public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_nm.h](wifi__nm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
