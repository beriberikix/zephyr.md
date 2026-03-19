---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mld_8h_source.html
original_path: doxygen/html/mld_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mld.h

[Go to the documentation of this file.](mld_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \* Copyright (c) 2024 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_MLD\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_MLD\_H\_

14

23

24#include <[errno.h](errno_8h.md)>

25

26#include <[zephyr/net/net\_if.h](net__if_8h.md)>

27#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

28#include <[zephyr/toolchain.h](toolchain_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

42#if defined(CONFIG\_NET\_IPV6\_MLD)

43int [net\_ipv6\_mld\_join](group__mld.md#ga53af11b1107b0375d219f2a3f517fcce)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

44#else

45static inline int

[ 46](group__mld.md#ga53af11b1107b0375d219f2a3f517fcce)[net\_ipv6\_mld\_join](group__mld.md#ga53af11b1107b0375d219f2a3f517fcce)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr)

47{

48 ARG\_UNUSED(addr);

49 ARG\_UNUSED(iface);

50

51 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

52}

53#endif /\* CONFIG\_NET\_IPV6\_MLD \*/

54

63#if defined(CONFIG\_NET\_IPV6\_MLD)

64int [net\_ipv6\_mld\_leave](group__mld.md#gaa1ccc2b362787fe28fb118af51b49465)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr);

65#else

66static inline int

[ 67](group__mld.md#gaa1ccc2b362787fe28fb118af51b49465)[net\_ipv6\_mld\_leave](group__mld.md#gaa1ccc2b362787fe28fb118af51b49465)(struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr)

68{

69 ARG\_UNUSED(iface);

70 ARG\_UNUSED(addr);

71

72 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

73}

74#endif /\* CONFIG\_NET\_IPV6\_MLD \*/

75

76#ifdef \_\_cplusplus

77}

78#endif

79

83

84#endif /\* ZEPHYR\_INCLUDE\_NET\_MLD\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[net\_ipv6\_mld\_join](group__mld.md#ga53af11b1107b0375d219f2a3f517fcce)

static int net\_ipv6\_mld\_join(struct net\_if \*iface, const struct in6\_addr \*addr)

Join a given multicast group.

**Definition** mld.h:46

[net\_ipv6\_mld\_leave](group__mld.md#gaa1ccc2b362787fe28fb118af51b49465)

static int net\_ipv6\_mld\_leave(struct net\_if \*iface, const struct in6\_addr \*addr)

Leave a given multicast group.

**Definition** mld.h:67

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:142

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mld.h](mld_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
