---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/wifi__nm_8h_source.html
original_path: doxygen/html/wifi__nm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

17#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/net/net\_if.h](net__if_8h.md)>

21#include <[zephyr/net/wifi\_mgmt.h](wifi__mgmt_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 36](structwifi__nm__instance.md)struct [wifi\_nm\_instance](structwifi__nm__instance.md) {

[ 38](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af) const char \*[name](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af);

[ 40](structwifi__nm__instance.md#a65e73ea84dfd64dc17f0af03477362ae) const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \*[ops](structwifi__nm__instance.md#a65e73ea84dfd64dc17f0af03477362ae);

[ 42](structwifi__nm__instance.md#a1a2a156fa39e1d09b6b9a1422f6097ac) struct [net\_if](structnet__if.md) \*[mgd\_ifaces](structwifi__nm__instance.md#a1a2a156fa39e1d09b6b9a1422f6097ac)[CONFIG\_WIFI\_NM\_MAX\_MANAGED\_INTERFACES];

43};

44

[ 45](group__wifi__nm.md#ga476afa0a50621396bc959d9cc7eca19f)#define WIFI\_NM\_NAME(name) wifi\_nm\_##name

46

[ 47](group__wifi__nm.md#ga618fa06395943215db2fa96cbfa3fc99)#define DEFINE\_WIFI\_NM\_INSTANCE(\_name, \_ops) \

48 static STRUCT\_SECTION\_ITERABLE(wifi\_nm\_instance, WIFI\_NM\_NAME(\_name)) = { \

49 .name = STRINGIFY(\_name), \

50 .ops = \_ops, \

51 .mgd\_ifaces = { NULL }, \

52 }

53

[ 60](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed)struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*[wifi\_nm\_get\_instance](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed)(const char \*[name](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af));

61

[ 68](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3)struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*[wifi\_nm\_get\_instance\_iface](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3)(struct [net\_if](structnet__if.md) \*iface);

69

[ 81](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb)int [wifi\_nm\_register\_mgd\_iface](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb)(struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface);

82

[ 91](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff)int [wifi\_nm\_unregister\_mgd\_iface](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff)(struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface);

92

96

97#ifdef \_\_cplusplus

98}

99#endif

100#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_NET\_WIFI\_NM\_H\_ \*/

[wifi\_nm\_register\_mgd\_iface](group__wifi__nm.md#ga26edd4cbb045a87613b79f8edd8e9dbb)

int wifi\_nm\_register\_mgd\_iface(struct wifi\_nm\_instance \*nm, struct net\_if \*iface)

Register a managed interface.

[wifi\_nm\_unregister\_mgd\_iface](group__wifi__nm.md#ga467b630fa57bb5587c0237b9cdf403ff)

int wifi\_nm\_unregister\_mgd\_iface(struct wifi\_nm\_instance \*nm, struct net\_if \*iface)

Unregister managed interface.

[wifi\_nm\_get\_instance](group__wifi__nm.md#ga781238fda024558c8ccb4cd8877467ed)

struct wifi\_nm\_instance \* wifi\_nm\_get\_instance(const char \*name)

Get a Network manager instance for a given name.

[wifi\_nm\_get\_instance\_iface](group__wifi__nm.md#ga813b6b6cc227115e83b8e632dd39e6f3)

struct wifi\_nm\_instance \* wifi\_nm\_get\_instance\_iface(struct net\_if \*iface)

Get a Network manager instance for a given interface.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[wifi\_mgmt\_ops](structwifi__mgmt__ops.md)

Wi-Fi management API.

**Definition** wifi\_mgmt.h:713

[wifi\_nm\_instance](structwifi__nm__instance.md)

WiFi Network manager instance.

**Definition** wifi\_nm.h:36

[wifi\_nm\_instance::mgd\_ifaces](structwifi__nm__instance.md#a1a2a156fa39e1d09b6b9a1422f6097ac)

struct net\_if \* mgd\_ifaces[CONFIG\_WIFI\_NM\_MAX\_MANAGED\_INTERFACES]

List of Managed interfaces.

**Definition** wifi\_nm.h:42

[wifi\_nm\_instance::ops](structwifi__nm__instance.md#a65e73ea84dfd64dc17f0af03477362ae)

const struct wifi\_mgmt\_ops \* ops

Wi-Fi Management operations.

**Definition** wifi\_nm.h:40

[wifi\_nm\_instance::name](structwifi__nm__instance.md#a9789018a431b6c78bbbbed1bbaf634af)

const char \* name

Name of the Network manager instance.

**Definition** wifi\_nm.h:38

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[wifi\_mgmt.h](wifi__mgmt_8h.md)

WiFi L2 stack public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_nm.h](wifi__nm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
