---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ipv4__autoconf_8h_source.html
original_path: doxygen/html/ipv4__autoconf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

[ 17](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a346aab74cb52d65887c523cf7d802765) [NET\_IPV4\_AUTOCONF\_PROBE](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a346aab74cb52d65887c523cf7d802765),

[ 18](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a1b050e88e0ad48c4a2f954e0995864c9) [NET\_IPV4\_AUTOCONF\_ANNOUNCE](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a1b050e88e0ad48c4a2f954e0995864c9),

[ 19](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2) [NET\_IPV4\_AUTOCONF\_ASSIGNED](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2),

[ 20](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674) [NET\_IPV4\_AUTOCONF\_RENEW](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674),

21};

22

26#if defined(CONFIG\_NET\_IPV4\_AUTO)

27void [net\_ipv4\_autoconf\_init](ipv4__autoconf_8h.md#a20d767a6d3b73cb9075384313e425e80)(void);

28#else

[ 29](ipv4__autoconf_8h.md#a20d767a6d3b73cb9075384313e425e80)#define net\_ipv4\_autoconf\_init(...)

30#endif

31

32#endif /\* ZEPHYR\_INCLUDE\_NET\_IPV4\_AUTOCONF\_H\_ \*/

[net\_ipv4\_autoconf\_init](ipv4__autoconf_8h.md#a20d767a6d3b73cb9075384313e425e80)

#define net\_ipv4\_autoconf\_init(...)

Initialize IPv4 auto configuration engine.

**Definition** ipv4\_autoconf.h:29

[net\_ipv4\_autoconf\_state](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899)

net\_ipv4\_autoconf\_state

Current state of IPv4 Autoconfiguration.

**Definition** ipv4\_autoconf.h:15

[NET\_IPV4\_AUTOCONF\_ANNOUNCE](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a1b050e88e0ad48c4a2f954e0995864c9)

@ NET\_IPV4\_AUTOCONF\_ANNOUNCE

**Definition** ipv4\_autoconf.h:18

[NET\_IPV4\_AUTOCONF\_PROBE](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a346aab74cb52d65887c523cf7d802765)

@ NET\_IPV4\_AUTOCONF\_PROBE

**Definition** ipv4\_autoconf.h:17

[NET\_IPV4\_AUTOCONF\_ASSIGNED](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2)

@ NET\_IPV4\_AUTOCONF\_ASSIGNED

**Definition** ipv4\_autoconf.h:19

[NET\_IPV4\_AUTOCONF\_INIT](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b)

@ NET\_IPV4\_AUTOCONF\_INIT

**Definition** ipv4\_autoconf.h:16

[NET\_IPV4\_AUTOCONF\_RENEW](ipv4__autoconf_8h.md#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674)

@ NET\_IPV4\_AUTOCONF\_RENEW

**Definition** ipv4\_autoconf.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ipv4\_autoconf.h](ipv4__autoconf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
