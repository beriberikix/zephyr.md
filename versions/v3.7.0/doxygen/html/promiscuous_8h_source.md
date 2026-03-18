---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/promiscuous_8h_source.html
original_path: doxygen/html/promiscuous_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

promiscuous.h

[Go to the documentation of this file.](promiscuous_8h.md)

1

7

8/\*

9 \* Copyright (c) 2018 Intel Corporation

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_PROMISCUOUS\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_PROMISCUOUS\_H\_

16

23

24#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

25#include <[zephyr/net/net\_if.h](net__if_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

38#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

39struct [net\_pkt](structnet__pkt.md) \*[net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)([k\_timeout\_t](structk__timeout__t.md) timeout);

40#else

[ 41](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)static inline struct [net\_pkt](structnet__pkt.md) \*[net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)([k\_timeout\_t](structk__timeout__t.md) timeout)

42{

43 ARG\_UNUSED(timeout);

44

45 return NULL;

46}

47#endif /\* CONFIG\_NET\_PROMISCUOUS\_MODE \*/

48

56#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

57int [net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

58#else

[ 59](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)static inline int [net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2))

60{

61 ARG\_UNUSED([iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

62

63 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

64}

65#endif /\* CONFIG\_NET\_PROMISCUOUS\_MODE \*/

66

74#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

75int [net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

76#else

[ 77](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)static inline int [net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2))

78{

79 ARG\_UNUSED([iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

80

81 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

82}

83#endif /\* CONFIG\_NET\_PROMISCUOUS\_MODE \*/

84

85#ifdef \_\_cplusplus

86}

87#endif

88

92

93#endif /\* ZEPHYR\_INCLUDE\_NET\_PROMISCUOUS\_H\_ \*/

[net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)

static int net\_promisc\_mode\_off(struct net\_if \*iface)

Disable promiscuous mode for a given network interface.

**Definition** promiscuous.h:77

[net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)

static struct net\_pkt \* net\_promisc\_mode\_wait\_data(k\_timeout\_t timeout)

Start to wait received network packets.

**Definition** promiscuous.h:41

[net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)

static int net\_promisc\_mode\_on(struct net\_if \*iface)

Enable promiscuous mode for a given network interface.

**Definition** promiscuous.h:59

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [promiscuous.h](promiscuous_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
