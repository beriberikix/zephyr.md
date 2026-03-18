---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/coap__mgmt_8h_source.html
original_path: doxygen/html/coap__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_mgmt.h

[Go to the documentation of this file.](coap__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2023 Basalte bv

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_COAP\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_COAP\_MGMT\_H\_

14

15#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

29

30/\* CoAP events \*/

31#define \_NET\_COAP\_LAYER NET\_MGMT\_LAYER\_L4

32#define \_NET\_COAP\_CODE 0x1c0

33#define \_NET\_COAP\_IF\_BASE (NET\_MGMT\_EVENT\_BIT | \

34 NET\_MGMT\_LAYER(\_NET\_COAP\_LAYER) | \

35 NET\_MGMT\_LAYER\_CODE(\_NET\_COAP\_CODE))

36

37struct coap\_service;

38struct [coap\_resource](structcoap__resource.md);

39struct [coap\_observer](structcoap__observer.md);

40

41enum net\_event\_coap\_cmd {

42 /\* Service events \*/

43 NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED = 1,

44 NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED,

45 /\* Observer events \*/

46 NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED,

47 NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED,

48};

49

51

[ 55](group__coap__mgmt.md#ga3b46cdbe035664256827049e4913643d)#define NET\_EVENT\_COAP\_SERVICE\_STARTED \

56 (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED)

57

[ 61](group__coap__mgmt.md#ga9a43c93ef72e152b17992af238507b9d)#define NET\_EVENT\_COAP\_SERVICE\_STOPPED \

62 (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED)

63

[ 67](group__coap__mgmt.md#gaf29083f98f6aa9e7f5192ee7f0504959)#define NET\_EVENT\_COAP\_OBSERVER\_ADDED \

68 (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED)

69

[ 73](group__coap__mgmt.md#ga6b56912cf30fa27cc2ccf27805274c69)#define NET\_EVENT\_COAP\_OBSERVER\_REMOVED \

74 (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED)

75

[ 79](structnet__event__coap__service.md)struct [net\_event\_coap\_service](structnet__event__coap__service.md) {

[ 81](structnet__event__coap__service.md#a66ad94d50eaf25c3dd3fa5f989a08392) const struct coap\_service \*[service](structnet__event__coap__service.md#a66ad94d50eaf25c3dd3fa5f989a08392);

82};

83

[ 87](structnet__event__coap__observer.md)struct [net\_event\_coap\_observer](structnet__event__coap__observer.md) {

[ 89](structnet__event__coap__observer.md#a4522acf85fff0a65def80f3a7d794d2b) struct [coap\_resource](structcoap__resource.md) \*[resource](structnet__event__coap__observer.md#a4522acf85fff0a65def80f3a7d794d2b);

[ 91](structnet__event__coap__observer.md#af15a9f085271fdc5e88180980013bfd2) struct [coap\_observer](structcoap__observer.md) \*[observer](structnet__event__coap__observer.md#af15a9f085271fdc5e88180980013bfd2);

92};

93

94#ifdef \_\_cplusplus

95}

96#endif

97

101

102#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_MGMT\_H\_ \*/

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[coap\_observer](structcoap__observer.md)

Represents a remote device that is observing a local resource.

**Definition** coap.h:281

[coap\_resource](structcoap__resource.md)

Description of CoAP resource.

**Definition** coap.h:263

[net\_event\_coap\_observer](structnet__event__coap__observer.md)

CoAP Observer event structure.

**Definition** coap\_mgmt.h:87

[net\_event\_coap\_observer::resource](structnet__event__coap__observer.md#a4522acf85fff0a65def80f3a7d794d2b)

struct coap\_resource \* resource

The CoAP resource for which the event is emitted.

**Definition** coap\_mgmt.h:89

[net\_event\_coap\_observer::observer](structnet__event__coap__observer.md#af15a9f085271fdc5e88180980013bfd2)

struct coap\_observer \* observer

The observer that is added/removed.

**Definition** coap\_mgmt.h:91

[net\_event\_coap\_service](structnet__event__coap__service.md)

CoAP Service event structure.

**Definition** coap\_mgmt.h:79

[net\_event\_coap\_service::service](structnet__event__coap__service.md#a66ad94d50eaf25c3dd3fa5f989a08392)

const struct coap\_service \* service

The CoAP service for which the event is emitted.

**Definition** coap\_mgmt.h:81

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_mgmt.h](coap__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
