---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dummy_8h_source.html
original_path: doxygen/html/dummy_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

7

8#ifndef ZEPHYR\_INCLUDE\_NET\_DUMMY\_H\_

9#define ZEPHYR\_INCLUDE\_NET\_DUMMY\_H\_

10

11#include <[zephyr/net/net\_if.h](net__if_8h.md)>

12#include <[zephyr/net/net\_pkt.h](net__pkt_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 25](structdummy__api.md)struct [dummy\_api](structdummy__api.md) {

[ 30](structdummy__api.md#ade5d5f20076909da1e9ea7a819192cf1) struct net\_if\_api [iface\_api](structdummy__api.md#ade5d5f20076909da1e9ea7a819192cf1);

31

[ 33](structdummy__api.md#a3a6110e3de2300931ac5e0aeabbd7311) int (\*[send](structdummy__api.md#a3a6110e3de2300931ac5e0aeabbd7311))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

34

[ 36](structdummy__api.md#a9f535aaf72c9e6781cceffdd019b3f85) int (\*[start](structdummy__api.md#a9f535aaf72c9e6781cceffdd019b3f85))(const struct [device](structdevice.md) \*dev);

37

[ 39](structdummy__api.md#a092fe1f0d12b091dad21e6dd7c717aa3) int (\*[stop](structdummy__api.md#a092fe1f0d12b091dad21e6dd7c717aa3))(const struct [device](structdevice.md) \*dev);

40};

41

42/\* Make sure that the network interface API is properly setup inside

43 \* dummy API struct (it is the first one).

44 \*/

45BUILD\_ASSERT(offsetof(struct [dummy\_api](structdummy__api.md), iface\_api) == 0);

46

47#ifdef \_\_cplusplus

48}

49#endif

50

54

55#endif /\* ZEPHYR\_INCLUDE\_NET\_DUMMY\_H\_ \*/

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_pkt.h](net__pkt_8h.md)

Network packet buffer descriptor API.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[dummy\_api](structdummy__api.md)

**Definition** dummy.h:25

[dummy\_api::stop](structdummy__api.md#a092fe1f0d12b091dad21e6dd7c717aa3)

int(\* stop)(const struct device \*dev)

Stop the device.

**Definition** dummy.h:39

[dummy\_api::send](structdummy__api.md#a3a6110e3de2300931ac5e0aeabbd7311)

int(\* send)(const struct device \*dev, struct net\_pkt \*pkt)

Send a network packet.

**Definition** dummy.h:33

[dummy\_api::start](structdummy__api.md#a9f535aaf72c9e6781cceffdd019b3f85)

int(\* start)(const struct device \*dev)

Start the device.

**Definition** dummy.h:36

[dummy\_api::iface\_api](structdummy__api.md#ade5d5f20076909da1e9ea7a819192cf1)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** dummy.h:30

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dummy.h](dummy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
