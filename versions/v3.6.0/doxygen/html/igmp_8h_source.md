---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/igmp_8h_source.html
original_path: doxygen/html/igmp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

igmp.h

[Go to the documentation of this file.](igmp_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_IGMP\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_IGMP\_H\_

13

20

21#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

22

23#include <[zephyr/net/net\_if.h](net__if_8h.md)>

24#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 30](structigmp__param.md)struct [igmp\_param](structigmp__param.md) {

[ 31](structigmp__param.md#ab64622c259c381d4c1ae3e3c0497b2b7) struct [in\_addr](structin__addr.md) \*[source\_list](structigmp__param.md#ab64622c259c381d4c1ae3e3c0497b2b7); /\* List of sources to include or exclude \*/

[ 32](structigmp__param.md#acb8f39f66f0c11733cf855f4303b0495) size\_t [sources\_len](structigmp__param.md#acb8f39f66f0c11733cf855f4303b0495); /\* Length of source list \*/

[ 33](structigmp__param.md#a2b60c5de6e21371dacc7f7f34ba6904b) bool [include](structigmp__param.md#a2b60c5de6e21371dacc7f7f34ba6904b); /\* Source list filter type \*/

34};

35

45#if defined(CONFIG\_NET\_IPV4\_IGMP)

46int [net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr,

47 const struct [igmp\_param](structigmp__param.md) \*param);

48#else

[ 49](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)static inline int [net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr,

50 const struct [igmp\_param](structigmp__param.md) \*param)

51{

52 ARG\_UNUSED(iface);

53 ARG\_UNUSED(addr);

54 ARG\_UNUSED(param);

55

56 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

57}

58#endif

59

68#if defined(CONFIG\_NET\_IPV4\_IGMP)

69int [net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

70#else

[ 71](group__igmp.md#gae92a971ee047049e05a16779100cb08b)static inline int [net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b)(struct [net\_if](structnet__if.md) \*iface,

72 const struct [in\_addr](structin__addr.md) \*addr)

73{

74 ARG\_UNUSED(iface);

75 ARG\_UNUSED(addr);

76

77 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

78}

79#endif

80

81#ifdef \_\_cplusplus

82}

83#endif

84

88

89#endif /\* ZEPHYR\_INCLUDE\_NET\_IGMP\_H\_ \*/

[net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)

static int net\_ipv4\_igmp\_join(struct net\_if \*iface, const struct in\_addr \*addr, const struct igmp\_param \*param)

Join a given multicast group.

**Definition** igmp.h:49

[net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b)

static int net\_ipv4\_igmp\_leave(struct net\_if \*iface, const struct in\_addr \*addr)

Leave a given multicast group.

**Definition** igmp.h:71

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[igmp\_param](structigmp__param.md)

**Definition** igmp.h:30

[igmp\_param::include](structigmp__param.md#a2b60c5de6e21371dacc7f7f34ba6904b)

bool include

**Definition** igmp.h:33

[igmp\_param::source\_list](structigmp__param.md#ab64622c259c381d4c1ae3e3c0497b2b7)

struct in\_addr \* source\_list

**Definition** igmp.h:31

[igmp\_param::sources\_len](structigmp__param.md#acb8f39f66f0c11733cf855f4303b0495)

size\_t sources\_len

**Definition** igmp.h:32

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [igmp.h](igmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
