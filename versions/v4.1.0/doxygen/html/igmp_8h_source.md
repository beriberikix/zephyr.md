---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/igmp_8h_source.html
original_path: doxygen/html/igmp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25#include <[zephyr/net/net\_if.h](net__if_8h.md)>

26#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 33](structigmp__param.md)struct [igmp\_param](structigmp__param.md) {

[ 34](structigmp__param.md#ab64622c259c381d4c1ae3e3c0497b2b7) struct [in\_addr](structin__addr.md) \*[source\_list](structigmp__param.md#ab64622c259c381d4c1ae3e3c0497b2b7);

[ 35](structigmp__param.md#acb8f39f66f0c11733cf855f4303b0495) size\_t [sources\_len](structigmp__param.md#acb8f39f66f0c11733cf855f4303b0495);

[ 36](structigmp__param.md#a2b60c5de6e21371dacc7f7f34ba6904b) bool [include](structigmp__param.md#a2b60c5de6e21371dacc7f7f34ba6904b);

37};

38

48#if defined(CONFIG\_NET\_IPV4\_IGMP)

49int [net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr,

50 const struct [igmp\_param](structigmp__param.md) \*param);

51#else

[ 52](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)static inline int [net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr,

53 const struct [igmp\_param](structigmp__param.md) \*param)

54{

55 ARG\_UNUSED(iface);

56 ARG\_UNUSED(addr);

57 ARG\_UNUSED(param);

58

59 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

60}

61#endif

62

71#if defined(CONFIG\_NET\_IPV4\_IGMP)

72int [net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b)(struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr);

73#else

[ 74](group__igmp.md#gae92a971ee047049e05a16779100cb08b)static inline int [net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b)(struct [net\_if](structnet__if.md) \*iface,

75 const struct [in\_addr](structin__addr.md) \*addr)

76{

77 ARG\_UNUSED(iface);

78 ARG\_UNUSED(addr);

79

80 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

81}

82#endif

83

84#ifdef \_\_cplusplus

85}

86#endif

87

91

92#endif /\* ZEPHYR\_INCLUDE\_NET\_IGMP\_H\_ \*/

[net\_ipv4\_igmp\_join](group__igmp.md#ga39227f2f4c2f0e7b0be8ac3cff080df0)

static int net\_ipv4\_igmp\_join(struct net\_if \*iface, const struct in\_addr \*addr, const struct igmp\_param \*param)

Join a given multicast group.

**Definition** igmp.h:52

[net\_ipv4\_igmp\_leave](group__igmp.md#gae92a971ee047049e05a16779100cb08b)

static int net\_ipv4\_igmp\_leave(struct net\_if \*iface, const struct in\_addr \*addr)

Leave a given multicast group.

**Definition** igmp.h:74

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[igmp\_param](structigmp__param.md)

IGMP parameters.

**Definition** igmp.h:33

[igmp\_param::include](structigmp__param.md#a2b60c5de6e21371dacc7f7f34ba6904b)

bool include

Source list filter type.

**Definition** igmp.h:36

[igmp\_param::source\_list](structigmp__param.md#ab64622c259c381d4c1ae3e3c0497b2b7)

struct in\_addr \* source\_list

List of sources to include or exclude.

**Definition** igmp.h:34

[igmp\_param::sources\_len](structigmp__param.md#acb8f39f66f0c11733cf855f4303b0495)

size\_t sources\_len

Length of source list.

**Definition** igmp.h:35

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [igmp.h](igmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
