---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dhcpv4_8h_source.html
original_path: doxygen/html/dhcpv4_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dhcpv4.h

[Go to the documentation of this file.](dhcpv4_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_DHCPV4\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_DHCPV4\_H\_

13

14#include <[zephyr/sys/slist.h](slist_8h.md)>

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

29

35enum net\_dhcpv4\_state {

36 NET\_DHCPV4\_DISABLED,

37 NET\_DHCPV4\_INIT,

38 NET\_DHCPV4\_SELECTING,

39 NET\_DHCPV4\_REQUESTING,

40 NET\_DHCPV4\_RENEWING,

41 NET\_DHCPV4\_REBINDING,

42 NET\_DHCPV4\_BOUND,

43} \_\_packed;

44

46

[ 56](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8)enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) {

[ 57](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) [NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) = 1,

[ 58](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) [NET\_DHCPV4\_MSG\_TYPE\_OFFER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) = 2,

[ 59](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) [NET\_DHCPV4\_MSG\_TYPE\_REQUEST](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) = 3,

[ 60](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) [NET\_DHCPV4\_MSG\_TYPE\_DECLINE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) = 4,

[ 61](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) [NET\_DHCPV4\_MSG\_TYPE\_ACK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) = 5,

[ 62](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) [NET\_DHCPV4\_MSG\_TYPE\_NAK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) = 6,

[ 63](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) [NET\_DHCPV4\_MSG\_TYPE\_RELEASE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) = 7,

[ 64](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) [NET\_DHCPV4\_MSG\_TYPE\_INFORM](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) = 8,

65};

66

67#ifdef CONFIG\_NET\_DHCPV4\_OPTION\_CALLBACKS

68

69struct net\_dhcpv4\_option\_callback;

70

86typedef void (\*net\_dhcpv4\_option\_callback\_handler\_t)(struct net\_dhcpv4\_option\_callback \*cb,

87 size\_t length,

88 enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type,

89 struct [net\_if](structnet__if.md) \*iface);

90

92

103struct net\_dhcpv4\_option\_callback {

107 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

108

110 net\_dhcpv4\_option\_callback\_handler\_t handler;

111

113 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option;

114

116 size\_t max\_length;

117

121 void \*data;

122};

123

125

134static inline void net\_dhcpv4\_init\_option\_callback(struct net\_dhcpv4\_option\_callback \*callback,

135 net\_dhcpv4\_option\_callback\_handler\_t handler,

136 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option,

137 void \*data,

138 size\_t max\_length)

139{

140 \_\_ASSERT(callback, "Callback pointer should not be NULL");

141 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

142 \_\_ASSERT(data, "Data pointer should not be NULL");

143

144 callback->handler = handler;

145 callback->option = option;

146 callback->data = data;

147 callback->max\_length = max\_length;

148}

149

155int net\_dhcpv4\_add\_option\_callback(struct net\_dhcpv4\_option\_callback \*cb);

156

162int net\_dhcpv4\_remove\_option\_callback(struct net\_dhcpv4\_option\_callback \*cb);

163

164#endif /\* CONFIG\_NET\_DHCPV4\_OPTION\_CALLBACKS \*/

165

[ 175](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)void [net\_dhcpv4\_start](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)(struct [net\_if](structnet__if.md) \*iface);

176

[ 186](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e)void [net\_dhcpv4\_stop](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e)(struct [net\_if](structnet__if.md) \*iface);

187

[ 197](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a)void [net\_dhcpv4\_restart](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a)(struct [net\_if](structnet__if.md) \*iface);

198

200

206const char \*net\_dhcpv4\_state\_name(enum net\_dhcpv4\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

207

209

[ 216](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c)const char \*[net\_dhcpv4\_msg\_type\_name](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c)(enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type);

217

221

222#ifdef \_\_cplusplus

223}

224#endif

225

226#endif /\* ZEPHYR\_INCLUDE\_NET\_DHCPV4\_H\_ \*/

[net\_dhcpv4\_msg\_type\_name](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c)

const char \* net\_dhcpv4\_msg\_type\_name(enum net\_dhcpv4\_msg\_type msg\_type)

Return a text representation of the msg\_type.

[net\_dhcpv4\_restart](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a)

void net\_dhcpv4\_restart(struct net\_if \*iface)

Restart DHCPv4 client on an iface.

[net\_dhcpv4\_stop](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e)

void net\_dhcpv4\_stop(struct net\_if \*iface)

Stop DHCPv4 client on an iface.

[net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8)

net\_dhcpv4\_msg\_type

DHCPv4 message types.

**Definition** dhcpv4.h:56

[net\_dhcpv4\_start](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)

void net\_dhcpv4\_start(struct net\_if \*iface)

Start DHCPv4 client on an iface.

[NET\_DHCPV4\_MSG\_TYPE\_REQUEST](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e)

@ NET\_DHCPV4\_MSG\_TYPE\_REQUEST

**Definition** dhcpv4.h:59

[NET\_DHCPV4\_MSG\_TYPE\_ACK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925)

@ NET\_DHCPV4\_MSG\_TYPE\_ACK

**Definition** dhcpv4.h:61

[NET\_DHCPV4\_MSG\_TYPE\_OFFER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a)

@ NET\_DHCPV4\_MSG\_TYPE\_OFFER

**Definition** dhcpv4.h:58

[NET\_DHCPV4\_MSG\_TYPE\_RELEASE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5)

@ NET\_DHCPV4\_MSG\_TYPE\_RELEASE

**Definition** dhcpv4.h:63

[NET\_DHCPV4\_MSG\_TYPE\_NAK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4)

@ NET\_DHCPV4\_MSG\_TYPE\_NAK

**Definition** dhcpv4.h:62

[NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d)

@ NET\_DHCPV4\_MSG\_TYPE\_DISCOVER

**Definition** dhcpv4.h:57

[NET\_DHCPV4\_MSG\_TYPE\_INFORM](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866)

@ NET\_DHCPV4\_MSG\_TYPE\_INFORM

**Definition** dhcpv4.h:64

[NET\_DHCPV4\_MSG\_TYPE\_DECLINE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f)

@ NET\_DHCPV4\_MSG\_TYPE\_DECLINE

**Definition** dhcpv4.h:60

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv4.h](dhcpv4_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
