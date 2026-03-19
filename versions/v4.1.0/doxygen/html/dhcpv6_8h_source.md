---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dhcpv6_8h_source.html
original_path: doxygen/html/dhcpv6_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dhcpv6.h

[Go to the documentation of this file.](dhcpv6_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_DHCPV6\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_DHCPV6\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

26

28

30enum net\_dhcpv6\_state {

31 NET\_DHCPV6\_DISABLED,

32 NET\_DHCPV6\_INIT,

33 NET\_DHCPV6\_SOLICITING,

34 NET\_DHCPV6\_REQUESTING,

35 NET\_DHCPV6\_CONFIRMING,

36 NET\_DHCPV6\_RENEWING,

37 NET\_DHCPV6\_REBINDING,

38 NET\_DHCPV6\_INFO\_REQUESTING,

39 NET\_DHCPV6\_BOUND,

40} \_\_packed;

41

42#define DHCPV6\_TID\_SIZE 3

43

44#ifndef CONFIG\_NET\_DHCPV6\_DUID\_MAX\_LEN

45#define CONFIG\_NET\_DHCPV6\_DUID\_MAX\_LEN 22

46#endif

47

48struct net\_dhcpv6\_duid\_raw {

49 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type;

50 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[CONFIG\_NET\_DHCPV6\_DUID\_MAX\_LEN];

51} \_\_packed;

52

53struct net\_dhcpv6\_duid\_storage {

54 struct net\_dhcpv6\_duid\_raw duid;

55 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) length;

56};

57

58struct [net\_if](structnet__if.md);

59

61

[ 63](structnet__dhcpv6__params.md)struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) {

[ 64](structnet__dhcpv6__params.md#a4bc3655ee2a830879667cdb554883573) bool [request\_addr](structnet__dhcpv6__params.md#a4bc3655ee2a830879667cdb554883573) : 1;

[ 65](structnet__dhcpv6__params.md#afd290d92fcc5ae3bac9a9c7030910e6b) bool [request\_prefix](structnet__dhcpv6__params.md#afd290d92fcc5ae3bac9a9c7030910e6b) : 1;

66};

67

[ 79](group__dhcpv6.md#gab607a476c947d0335a254304e5dc2a24)void [net\_dhcpv6\_start](group__dhcpv6.md#gab607a476c947d0335a254304e5dc2a24)(struct [net\_if](structnet__if.md) \*iface, struct [net\_dhcpv6\_params](structnet__dhcpv6__params.md) \*params);

80

[ 90](group__dhcpv6.md#gaf0b903bdcd0becf06ed6b212c74097a0)void [net\_dhcpv6\_stop](group__dhcpv6.md#gaf0b903bdcd0becf06ed6b212c74097a0)(struct [net\_if](structnet__if.md) \*iface);

91

[ 100](group__dhcpv6.md#ga99642b89c14cb17f35b45a03a2286441)void [net\_dhcpv6\_restart](group__dhcpv6.md#ga99642b89c14cb17f35b45a03a2286441)(struct [net\_if](structnet__if.md) \*iface);

101

103

109const char \*net\_dhcpv6\_state\_name(enum net\_dhcpv6\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

110

112

116

117#ifdef \_\_cplusplus

118}

119#endif

120

121#endif /\* ZEPHYR\_INCLUDE\_NET\_DHCPV6\_H\_ \*/

[net\_dhcpv6\_restart](group__dhcpv6.md#ga99642b89c14cb17f35b45a03a2286441)

void net\_dhcpv6\_restart(struct net\_if \*iface)

Restart DHCPv6 client on an iface.

[net\_dhcpv6\_start](group__dhcpv6.md#gab607a476c947d0335a254304e5dc2a24)

void net\_dhcpv6\_start(struct net\_if \*iface, struct net\_dhcpv6\_params \*params)

Start DHCPv6 client on an iface.

[net\_dhcpv6\_stop](group__dhcpv6.md#gaf0b903bdcd0becf06ed6b212c74097a0)

void net\_dhcpv6\_stop(struct net\_if \*iface)

Stop DHCPv6 client on an iface.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[net\_dhcpv6\_params](structnet__dhcpv6__params.md)

DHCPv6 client configuration parameters.

**Definition** dhcpv6.h:63

[net\_dhcpv6\_params::request\_addr](structnet__dhcpv6__params.md#a4bc3655ee2a830879667cdb554883573)

bool request\_addr

Request IPv6 address.

**Definition** dhcpv6.h:64

[net\_dhcpv6\_params::request\_prefix](structnet__dhcpv6__params.md#afd290d92fcc5ae3bac9a9c7030910e6b)

bool request\_prefix

Request IPv6 prefix.

**Definition** dhcpv6.h:65

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv6.h](dhcpv6_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
