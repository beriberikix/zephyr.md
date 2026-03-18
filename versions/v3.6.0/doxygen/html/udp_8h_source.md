---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/udp_8h_source.html
original_path: doxygen/html/udp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udp.h

[Go to the documentation of this file.](udp_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_UDP\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_UDP\_H\_

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

16#include <[zephyr/net/net\_core.h](net__core_8h.md)>

17#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

18#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

24/\* These APIs are mostly meant for Zephyr internal use so do not generate

25 \* documentation for them.

26 \*/

28

35

53#if defined(CONFIG\_NET\_UDP)

54struct net\_udp\_hdr \*net\_udp\_get\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

55 struct net\_udp\_hdr \*hdr);

56#else

57static inline struct net\_udp\_hdr \*net\_udp\_get\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

58 struct net\_udp\_hdr \*hdr)

59{

60 return NULL;

61}

62#endif /\* CONFIG\_NET\_UDP \*/

63

79#if defined(CONFIG\_NET\_UDP)

80struct net\_udp\_hdr \*net\_udp\_set\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

81 struct net\_udp\_hdr \*hdr);

82#else

83static inline struct net\_udp\_hdr \*net\_udp\_set\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

84 struct net\_udp\_hdr \*hdr)

85{

86 return NULL;

87}

88#endif /\* CONFIG\_NET\_UDP \*/

89

93

95

96#ifdef \_\_cplusplus

97}

98#endif

99

100#endif /\* ZEPHYR\_INCLUDE\_NET\_UDP\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [udp.h](udp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
