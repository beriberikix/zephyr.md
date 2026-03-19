---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/canbus_8h_source.html
original_path: doxygen/html/canbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

canbus.h

[Go to the documentation of this file.](canbus_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_CANBUS\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_CANBUS\_H\_

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

16#include <[zephyr/net/net\_if.h](net__if_8h.md)>

17#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 26](structcanbus__api.md)struct [canbus\_api](structcanbus__api.md) {

[ 31](structcanbus__api.md#af8f809bf252a5d261209af2b7b3096f7) struct net\_if\_api [iface\_api](structcanbus__api.md#af8f809bf252a5d261209af2b7b3096f7);

32

[ 34](structcanbus__api.md#a31fee4b60f4ab2f832e0599c23337b6c) int (\*[send](structcanbus__api.md#a31fee4b60f4ab2f832e0599c23337b6c))(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

35

[ 37](structcanbus__api.md#abff03e6144170f8f223e11a7f28b59b7) void (\*[close](structcanbus__api.md#abff03e6144170f8f223e11a7f28b59b7))(const struct [device](structdevice.md) \*dev, int filter\_id);

38

[ 40](structcanbus__api.md#aad0cbe71d16cec3c99c812ab324e5382) int (\*[setsockopt](structcanbus__api.md#aad0cbe71d16cec3c99c812ab324e5382))(const struct [device](structdevice.md) \*dev, void \*obj, int level,

41 int optname,

42 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

43

[ 45](structcanbus__api.md#a0d61e7052367475a10b8c72461f7361f) int (\*[getsockopt](structcanbus__api.md#a0d61e7052367475a10b8c72461f7361f))(const struct [device](structdevice.md) \*dev, void \*obj, int level,

46 int optname,

47 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

48};

49

50/\* Make sure that the network interface API is properly setup inside

51 \* CANBUS API struct (it is the first one).

52 \*/

53BUILD\_ASSERT(offsetof(struct [canbus\_api](structcanbus__api.md), iface\_api) == 0);

54

55#ifdef \_\_cplusplus

56}

57#endif

58

59#endif /\* ZEPHYR\_INCLUDE\_NET\_CANBUS\_H\_ \*/

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[canbus\_api](structcanbus__api.md)

CAN L2 network driver API.

**Definition** canbus.h:26

[canbus\_api::getsockopt](structcanbus__api.md#a0d61e7052367475a10b8c72461f7361f)

int(\* getsockopt)(const struct device \*dev, void \*obj, int level, int optname, const void \*optval, socklen\_t \*optlen)

Get socket CAN option.

**Definition** canbus.h:45

[canbus\_api::send](structcanbus__api.md#a31fee4b60f4ab2f832e0599c23337b6c)

int(\* send)(const struct device \*dev, struct net\_pkt \*pkt)

Send a CAN packet by socket.

**Definition** canbus.h:34

[canbus\_api::setsockopt](structcanbus__api.md#aad0cbe71d16cec3c99c812ab324e5382)

int(\* setsockopt)(const struct device \*dev, void \*obj, int level, int optname, const void \*optval, socklen\_t optlen)

Set socket CAN option.

**Definition** canbus.h:40

[canbus\_api::close](structcanbus__api.md#abff03e6144170f8f223e11a7f28b59b7)

void(\* close)(const struct device \*dev, int filter\_id)

Close the related CAN socket.

**Definition** canbus.h:37

[canbus\_api::iface\_api](structcanbus__api.md#af8f809bf252a5d261209af2b7b3096f7)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** canbus.h:31

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [canbus.h](canbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
