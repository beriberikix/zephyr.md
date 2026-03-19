---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ipv4__autoconf_8h_source.html
original_path: doxygen/html/ipv4__autoconf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipv4\_autoconf.h

[Go to the documentation of this file.](ipv4__autoconf_8h.md)

1/\*

2 \* Copyright (c) 2017 Matthias Boesl

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_IPV4\_AUTOCONF\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_IPV4\_AUTOCONF\_H\_

13

[ 15](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899)enum [net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899) {

[ 16](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b) [NET\_IPV4\_AUTOCONF\_INIT](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b),

[ 17](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2) [NET\_IPV4\_AUTOCONF\_ASSIGNED](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2),

[ 18](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674) [NET\_IPV4\_AUTOCONF\_RENEW](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674),

19};

20

21struct [net\_if](structnet__if.md);

22

30#if defined(CONFIG\_NET\_IPV4\_AUTO)

31void [net\_ipv4\_autoconf\_start](ipv4__autoconf_8h.md#a5cbac9cab526f57c9b4a8ec141dbfb99)(struct [net\_if](structnet__if.md) \*iface);

32#else

[ 33](ipv4__autoconf_8h.md#a5cbac9cab526f57c9b4a8ec141dbfb99)static inline void [net\_ipv4\_autoconf\_start](ipv4__autoconf_8h.md#a5cbac9cab526f57c9b4a8ec141dbfb99)(struct [net\_if](structnet__if.md) \*iface)

34{

35 ARG\_UNUSED(iface);

36}

37#endif

38

46#if defined(CONFIG\_NET\_IPV4\_AUTO)

47void [net\_ipv4\_autoconf\_reset](ipv4__autoconf_8h.md#a4845fd81288d96d72bbf7e8001fd31a5)(struct [net\_if](structnet__if.md) \*iface);

48#else

[ 49](ipv4__autoconf_8h.md#a4845fd81288d96d72bbf7e8001fd31a5)static inline void [net\_ipv4\_autoconf\_reset](ipv4__autoconf_8h.md#a4845fd81288d96d72bbf7e8001fd31a5)(struct [net\_if](structnet__if.md) \*iface)

50{

51 ARG\_UNUSED(iface);

52}

53#endif

54

56

60#if defined(CONFIG\_NET\_IPV4\_AUTO)

61void net\_ipv4\_autoconf\_init(void);

62#else

63static inline void net\_ipv4\_autoconf\_init(void) { }

64#endif

65

67

68#endif /\* ZEPHYR\_INCLUDE\_NET\_IPV4\_AUTOCONF\_H\_ \*/

[net\_ipv4\_autoconf\_reset](ipv4__autoconf_8h.md#a4845fd81288d96d72bbf7e8001fd31a5)

static void net\_ipv4\_autoconf\_reset(struct net\_if \*iface)

Reset autoconf process.

**Definition** ipv4\_autoconf.h:49

[net\_ipv4\_autoconf\_start](ipv4__autoconf_8h.md#a5cbac9cab526f57c9b4a8ec141dbfb99)

static void net\_ipv4\_autoconf\_start(struct net\_if \*iface)

Start IPv4 autoconfiguration RFC 3927: IPv4 Link Local.

**Definition** ipv4\_autoconf.h:33

[net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899)

net\_ipv4\_autoconf\_state

Current state of IPv4 Autoconfiguration.

**Definition** ipv4\_autoconf.h:15

[NET\_IPV4\_AUTOCONF\_ASSIGNED](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2)

@ NET\_IPV4\_AUTOCONF\_ASSIGNED

Assigned state.

**Definition** ipv4\_autoconf.h:17

[NET\_IPV4\_AUTOCONF\_INIT](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b)

@ NET\_IPV4\_AUTOCONF\_INIT

Initialization state.

**Definition** ipv4\_autoconf.h:16

[NET\_IPV4\_AUTOCONF\_RENEW](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674)

@ NET\_IPV4\_AUTOCONF\_RENEW

Renew state.

**Definition** ipv4\_autoconf.h:18

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ipv4\_autoconf.h](ipv4__autoconf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
