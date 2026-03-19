---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dummy_8h_source.html
original_path: doxygen/html/dummy_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dummy.h

[Go to the documentation of this file.](dummy_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_DUMMY\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_DUMMY\_H\_

15

16#include <[zephyr/net/net\_if.h](net__if_8h.md)>

17#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

[ 33](structdummy__api.md)struct [dummy\_api](structdummy__api.md) {

[ 38](structdummy__api.md#ade5d5f20076909da1e9ea7a819192cf1) struct net\_if\_api [iface\_api](structdummy__api.md#ade5d5f20076909da1e9ea7a819192cf1);

39

[ 41](structdummy__api.md#a35fcbed7d17542ef32c80a09177cb1b5) int (\*[send](structdummy__api.md#a3a6110e3de2300931ac5e0aeabbd7311))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

42

47 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[recv](structdummy__api.md#a35fcbed7d17542ef32c80a09177cb1b5))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

48

[ 50](structdummy__api.md#a9f535aaf72c9e6781cceffdd019b3f85) int (\*[start](structdummy__api.md#a9f535aaf72c9e6781cceffdd019b3f85))(const struct [device](structdevice.md) \*dev);

51

[ 53](structdummy__api.md#a092fe1f0d12b091dad21e6dd7c717aa3) int (\*[stop](structdummy__api.md#a092fe1f0d12b091dad21e6dd7c717aa3))(const struct [device](structdevice.md) \*dev);

54};

55

56/\* Make sure that the network interface API is properly setup inside

57 \* dummy API struct (it is the first one).

58 \*/

59BUILD\_ASSERT(offsetof(struct [dummy\_api](structdummy__api.md), iface\_api) == 0);

60

61#ifdef \_\_cplusplus

62}

63#endif

64

68

69#endif /\* ZEPHYR\_INCLUDE\_NET\_DUMMY\_H\_ \*/

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:103

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[dummy\_api](structdummy__api.md)

Dummy L2 API operations.

**Definition** dummy.h:33

[dummy\_api::stop](structdummy__api.md#a092fe1f0d12b091dad21e6dd7c717aa3)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** dummy.h:53

[dummy\_api::recv](structdummy__api.md#a35fcbed7d17542ef32c80a09177cb1b5)

enum net\_verdict(\* recv)(struct net\_if \*iface, struct net\_pkt \*pkt)

Receive a network packet (only limited use for this, for example receiving capturing packets and post...

**Definition** dummy.h:47

[dummy\_api::send](structdummy__api.md#a3a6110e3de2300931ac5e0aeabbd7311)

int(\* send)(const struct device \*dev, struct net\_pkt \*pkt)

Send a network packet.

**Definition** dummy.h:41

[dummy\_api::start](structdummy__api.md#a9f535aaf72c9e6781cceffdd019b3f85)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** dummy.h:50

[dummy\_api::iface\_api](structdummy__api.md#ade5d5f20076909da1e9ea7a819192cf1)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** dummy.h:38

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dummy.h](dummy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
