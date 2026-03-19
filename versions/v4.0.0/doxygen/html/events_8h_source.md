---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/events_8h_source.html
original_path: doxygen/html/events_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

events.h

[Go to the documentation of this file.](events_8h.md)

1/\*

2 \* Copyright (c) 2021 EPAM Systems

3 \* Copyright (c) 2022 Arm Limited (or its affiliates). All rights reserved.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef \_\_XEN\_EVENTS\_H\_\_

8#define \_\_XEN\_EVENTS\_H\_\_

9

10#include <[zephyr/xen/public/event\_channel.h](event__channel_8h.md)>

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

[ 14](events_8h.md#a1e631dcb6d0ab84d2b63cced85f28d47)typedef void (\*[evtchn\_cb\_t](events_8h.md#a1e631dcb6d0ab84d2b63cced85f28d47))(void \*priv);

15

[ 16](structevent__channel__handle.md)struct [event\_channel\_handle](structevent__channel__handle.md) {

[ 17](structevent__channel__handle.md#ae9cd87fb197df9586dbf6f59978719a9) [evtchn\_cb\_t](events_8h.md#a1e631dcb6d0ab84d2b63cced85f28d47) [cb](structevent__channel__handle.md#ae9cd87fb197df9586dbf6f59978719a9);

[ 18](structevent__channel__handle.md#a251f0bf5106c1b7384418c08b032c6c6) void \*[priv](structevent__channel__handle.md#a251f0bf5106c1b7384418c08b032c6c6);

19};

[ 20](events_8h.md#a057cac7f834e8352d4b8b48d5ae22fcb)typedef struct [event\_channel\_handle](structevent__channel__handle.md) [evtchn\_handle\_t](events_8h.md#a057cac7f834e8352d4b8b48d5ae22fcb);

21

22/\*

23 \* Following functions just wrap Xen hypercalls, detailed description

24 \* of parameters and return values are located in include/xen/public/event\_channel.h

25 \*/

[ 26](events_8h.md#ae5391f2b67ddbd598f33d796ba591568)int [evtchn\_status](events_8h.md#ae5391f2b67ddbd598f33d796ba591568)([evtchn\_status\_t](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9) \*status);

[ 27](events_8h.md#abed06147ec0c0f9650ac7348a04ee430)int [evtchn\_close](events_8h.md#abed06147ec0c0f9650ac7348a04ee430)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port);

[ 28](events_8h.md#a761efce6eab19f91b33391d4bf516fff)int [evtchn\_set\_priority](events_8h.md#a761efce6eab19f91b33391d4bf516fff)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) priority);

[ 29](events_8h.md#a050856eda5a9c15075b3bc5314658d3a)void [notify\_evtchn](events_8h.md#a050856eda5a9c15075b3bc5314658d3a)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port);

30

31/\*

32 \* Allocate event-channel between caller and remote domain

33 \*

34 \* @param remote\_dom - remote domain domid

35 \* @return - local event channel port on success, negative on error

36 \*/

[ 37](events_8h.md#a46ba842a0e4f518d03683253d35b7126)int [alloc\_unbound\_event\_channel](events_8h.md#a46ba842a0e4f518d03683253d35b7126)([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) remote\_dom);

38

39#ifdef CONFIG\_XEN\_DOM0

40/\*

41 \* Allocate event-channel between remote domains. Can be used only from Dom0.

42 \*

43 \* @param dom - first remote domain domid (may be DOMID\_SELF)

44 \* @param remote\_dom - second remote domain domid

45 \* @return - local event channel port on success, negative on error

46 \*/

47int alloc\_unbound\_event\_channel\_dom0([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) dom, [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) remote\_dom);

48#endif /\* CONFIG\_XEN\_DOM0 \*/

49

50/\*

51 \* Allocate local event channel, binded to remote port and attach specified callback

52 \* to it

53 \*

54 \* @param remote\_dom - remote domain domid

55 \* @param remote\_port - remote domain event channel port number

56 \* @param cb - callback, attached to locat port

57 \* @param data - private data, that will be passed to cb

58 \* @return - local event channel port on success, negative on error

59 \*/

[ 60](events_8h.md#adc0a69c0205307e86458ada50aa0302d)int [bind\_interdomain\_event\_channel](events_8h.md#adc0a69c0205307e86458ada50aa0302d)([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) remote\_dom, [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) remote\_port,

61 [evtchn\_cb\_t](events_8h.md#a1e631dcb6d0ab84d2b63cced85f28d47) [cb](structevent__channel__handle.md#ae9cd87fb197df9586dbf6f59978719a9), void \*data);

62

63/\*

64 \* Bind user-defined handler to specified event-channel

65 \*

66 \* @param port - event channel number

67 \* @param cb - pointer to event channel handler

68 \* @param data - private data, that will be passed to handler as parameter

69 \* @return - zero on success

70 \*/

[ 71](events_8h.md#a74e60b33dd93a62835e86b251a9cd43c)int [bind\_event\_channel](events_8h.md#a74e60b33dd93a62835e86b251a9cd43c)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port, [evtchn\_cb\_t](events_8h.md#a1e631dcb6d0ab84d2b63cced85f28d47) [cb](structevent__channel__handle.md#ae9cd87fb197df9586dbf6f59978719a9), void \*data);

72

73/\*

74 \* Unbind handler from event channel, substitute it with empty callback

75 \*

76 \* @param port - event channel number to unbind

77 \* @return - zero on success

78 \*/

[ 79](events_8h.md#abad4417540bf329eca43842bf83549e9)int [unbind\_event\_channel](events_8h.md#abad4417540bf329eca43842bf83549e9)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port);

[ 80](events_8h.md#a2ac07d6eff7d3406716917578b5f7daf)int [get\_missed\_events](events_8h.md#a2ac07d6eff7d3406716917578b5f7daf)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port);

81

[ 82](events_8h.md#af6542be4472fb2d1dc17deca6c323972)int [xen\_events\_init](events_8h.md#af6542be4472fb2d1dc17deca6c323972)(void);

83

84#endif /\* \_\_XEN\_EVENTS\_H\_\_ \*/

[event\_channel.h](event__channel_8h.md)

[evtchn\_status\_t](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9)

struct evtchn\_status evtchn\_status\_t

**Definition** event\_channel.h:176

[evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)

uint32\_t evtchn\_port\_t

**Definition** event\_channel.h:74

[notify\_evtchn](events_8h.md#a050856eda5a9c15075b3bc5314658d3a)

void notify\_evtchn(evtchn\_port\_t port)

[evtchn\_handle\_t](events_8h.md#a057cac7f834e8352d4b8b48d5ae22fcb)

struct event\_channel\_handle evtchn\_handle\_t

**Definition** events.h:20

[evtchn\_cb\_t](events_8h.md#a1e631dcb6d0ab84d2b63cced85f28d47)

void(\* evtchn\_cb\_t)(void \*priv)

**Definition** events.h:14

[get\_missed\_events](events_8h.md#a2ac07d6eff7d3406716917578b5f7daf)

int get\_missed\_events(evtchn\_port\_t port)

[alloc\_unbound\_event\_channel](events_8h.md#a46ba842a0e4f518d03683253d35b7126)

int alloc\_unbound\_event\_channel(domid\_t remote\_dom)

[bind\_event\_channel](events_8h.md#a74e60b33dd93a62835e86b251a9cd43c)

int bind\_event\_channel(evtchn\_port\_t port, evtchn\_cb\_t cb, void \*data)

[evtchn\_set\_priority](events_8h.md#a761efce6eab19f91b33391d4bf516fff)

int evtchn\_set\_priority(evtchn\_port\_t port, uint32\_t priority)

[unbind\_event\_channel](events_8h.md#abad4417540bf329eca43842bf83549e9)

int unbind\_event\_channel(evtchn\_port\_t port)

[evtchn\_close](events_8h.md#abed06147ec0c0f9650ac7348a04ee430)

int evtchn\_close(evtchn\_port\_t port)

[bind\_interdomain\_event\_channel](events_8h.md#adc0a69c0205307e86458ada50aa0302d)

int bind\_interdomain\_event\_channel(domid\_t remote\_dom, evtchn\_port\_t remote\_port, evtchn\_cb\_t cb, void \*data)

[evtchn\_status](events_8h.md#ae5391f2b67ddbd598f33d796ba591568)

int evtchn\_status(evtchn\_status\_t \*status)

[xen\_events\_init](events_8h.md#af6542be4472fb2d1dc17deca6c323972)

int xen\_events\_init(void)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[event\_channel\_handle](structevent__channel__handle.md)

**Definition** events.h:16

[event\_channel\_handle::priv](structevent__channel__handle.md#a251f0bf5106c1b7384418c08b032c6c6)

void \* priv

**Definition** events.h:18

[event\_channel\_handle::cb](structevent__channel__handle.md#ae9cd87fb197df9586dbf6f59978719a9)

evtchn\_cb\_t cb

**Definition** events.h:17

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [events.h](events_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
