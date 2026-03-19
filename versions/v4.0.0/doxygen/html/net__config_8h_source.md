---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__config_8h_source.html
original_path: doxygen/html/net__config_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_config.h

[Go to the documentation of this file.](net__config_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_CONFIG\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_NET\_CONFIG\_H\_

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/net/net\_if.h](net__if_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

30

31/\* Flags that tell what kind of functionality is needed by the client. \*/

[ 37](group__net__config.md#ga5c1a321477ce072a964bc610aef805f1)#define NET\_CONFIG\_NEED\_ROUTER 0x00000001

38

[ 43](group__net__config.md#ga469731c167f97b5df40b51ee0c87313c)#define NET\_CONFIG\_NEED\_IPV6 0x00000002

44

[ 49](group__net__config.md#ga4312efaa62093c93968c0ae81efc36dd)#define NET\_CONFIG\_NEED\_IPV4 0x00000004

50

[ 64](group__net__config.md#ga02a2b4fbac3eba68a175630293c91484)int [net\_config\_init](group__net__config.md#ga02a2b4fbac3eba68a175630293c91484)(const char \*app\_info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

65

[ 81](group__net__config.md#gab19ec1b3411f38d9bee5abcb25926ea0)int [net\_config\_init\_by\_iface](group__net__config.md#gab19ec1b3411f38d9bee5abcb25926ea0)(struct [net\_if](structnet__if.md) \*iface, const char \*app\_info,

82 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

83

[ 99](group__net__config.md#ga49c6b4cd9d338f1b3d76225a9872c84c)int [net\_config\_init\_app](group__net__config.md#ga49c6b4cd9d338f1b3d76225a9872c84c)(const struct [device](structdevice.md) \*dev, const char \*app\_info);

100

104

105#ifdef \_\_cplusplus

106}

107#endif

108

109#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CONFIG\_H\_ \*/

[device.h](device_8h.md)

[net\_config\_init](group__net__config.md#ga02a2b4fbac3eba68a175630293c91484)

int net\_config\_init(const char \*app\_info, uint32\_t flags, int32\_t timeout)

Initialize this network application.

[net\_config\_init\_app](group__net__config.md#ga49c6b4cd9d338f1b3d76225a9872c84c)

int net\_config\_init\_app(const struct device \*dev, const char \*app\_info)

Initialize this network application.

[net\_config\_init\_by\_iface](group__net__config.md#gab19ec1b3411f38d9bee5abcb25926ea0)

int net\_config\_init\_by\_iface(struct net\_if \*iface, const char \*app\_info, uint32\_t flags, int32\_t timeout)

Initialize this network application using a specific network interface.

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_config.h](net__config_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
