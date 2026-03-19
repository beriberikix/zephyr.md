---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/promiscuous_8h_source.html
original_path: doxygen/html/promiscuous_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

25

26#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

27#include <[zephyr/net/net\_if.h](net__if_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

40#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

41struct [net\_pkt](structnet__pkt.md) \*[net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)([k\_timeout\_t](structk__timeout__t.md) timeout);

42#else

[ 43](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)static inline struct [net\_pkt](structnet__pkt.md) \*[net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)([k\_timeout\_t](structk__timeout__t.md) timeout)

44{

45 ARG\_UNUSED(timeout);

46

47 return NULL;

48}

49#endif /\* CONFIG\_NET\_PROMISCUOUS\_MODE \*/

50

58#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

59int [net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

60#else

[ 61](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)static inline int [net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2))

62{

63 ARG\_UNUSED([iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

64

65 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

66}

67#endif /\* CONFIG\_NET\_PROMISCUOUS\_MODE \*/

68

76#if defined(CONFIG\_NET\_PROMISCUOUS\_MODE)

77int [net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

78#else

[ 79](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)static inline int [net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2))

80{

81 ARG\_UNUSED([iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

82

83 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

84}

85#endif /\* CONFIG\_NET\_PROMISCUOUS\_MODE \*/

86

87#ifdef \_\_cplusplus

88}

89#endif

90

94

95#endif /\* ZEPHYR\_INCLUDE\_NET\_PROMISCUOUS\_H\_ \*/

[net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a)

static int net\_promisc\_mode\_off(struct net\_if \*iface)

Disable promiscuous mode for a given network interface.

**Definition** promiscuous.h:79

[net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e)

static struct net\_pkt \* net\_promisc\_mode\_wait\_data(k\_timeout\_t timeout)

Start to wait received network packets.

**Definition** promiscuous.h:43

[net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926)

static int net\_promisc\_mode\_on(struct net\_if \*iface)

Enable promiscuous mode for a given network interface.

**Definition** promiscuous.h:61

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

**Definition** net\_if.h:680

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:114

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [promiscuous.h](promiscuous_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
