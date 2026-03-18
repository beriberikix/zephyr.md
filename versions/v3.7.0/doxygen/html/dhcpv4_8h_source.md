---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dhcpv4_8h_source.html
original_path: doxygen/html/dhcpv4_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

43 NET\_DHCPV4\_DECLINE,

44} \_\_packed;

45

47

[ 57](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8)enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) {

[ 58](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) [NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d) = 1,

[ 59](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) [NET\_DHCPV4\_MSG\_TYPE\_OFFER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a) = 2,

[ 60](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) [NET\_DHCPV4\_MSG\_TYPE\_REQUEST](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e) = 3,

[ 61](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) [NET\_DHCPV4\_MSG\_TYPE\_DECLINE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f) = 4,

[ 62](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) [NET\_DHCPV4\_MSG\_TYPE\_ACK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925) = 5,

[ 63](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) [NET\_DHCPV4\_MSG\_TYPE\_NAK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4) = 6,

[ 64](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) [NET\_DHCPV4\_MSG\_TYPE\_RELEASE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5) = 7,

[ 65](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) [NET\_DHCPV4\_MSG\_TYPE\_INFORM](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866) = 8,

66};

67

68struct net\_dhcpv4\_option\_callback;

69

[ 85](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d)typedef void (\*[net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d))(struct net\_dhcpv4\_option\_callback \*cb,

86 size\_t length,

87 enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type,

88 struct [net\_if](structnet__if.md) \*iface);

89

91

102struct net\_dhcpv4\_option\_callback {

106 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

107

109 [net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d) handler;

110

112 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option;

113

115 size\_t max\_length;

116

120 void \*data;

121};

122

124

[ 133](group__dhcpv4.md#ga84df76c84de248a43e3e26d422cdfc2f)static inline void [net\_dhcpv4\_init\_option\_callback](group__dhcpv4.md#ga84df76c84de248a43e3e26d422cdfc2f)(struct net\_dhcpv4\_option\_callback \*callback,

134 [net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d) handler,

135 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option,

136 void \*data,

137 size\_t max\_length)

138{

139 \_\_ASSERT(callback, "Callback pointer should not be NULL");

140 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

141 \_\_ASSERT(data, "Data pointer should not be NULL");

142

143 callback->handler = handler;

144 callback->option = option;

145 callback->data = data;

146 callback->max\_length = max\_length;

147}

148

[ 154](group__dhcpv4.md#gaf073157fcd5cb2d18c40b8697d724a7c)int [net\_dhcpv4\_add\_option\_callback](group__dhcpv4.md#gaf073157fcd5cb2d18c40b8697d724a7c)(struct net\_dhcpv4\_option\_callback \*cb);

155

[ 161](group__dhcpv4.md#gaa90c4ba8010bcd2079512afe5f288dbb)int [net\_dhcpv4\_remove\_option\_callback](group__dhcpv4.md#gaa90c4ba8010bcd2079512afe5f288dbb)(struct net\_dhcpv4\_option\_callback \*cb);

162

172static inline void

[ 173](group__dhcpv4.md#gaec0f1c87f5093767a4bb1c43b8e18e72)[net\_dhcpv4\_init\_option\_vendor\_callback](group__dhcpv4.md#gaec0f1c87f5093767a4bb1c43b8e18e72)(struct net\_dhcpv4\_option\_callback \*callback,

174 [net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d) handler, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) option,

175 void \*data, size\_t max\_length)

176{

177 \_\_ASSERT(callback, "Callback pointer should not be NULL");

178 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

179 \_\_ASSERT(data, "Data pointer should not be NULL");

180

181 callback->handler = handler;

182 callback->option = option;

183 callback->data = data;

184 callback->max\_length = max\_length;

185}

186

[ 192](group__dhcpv4.md#gabf3d97139fc4f7122c1bdee52cb003cb)int [net\_dhcpv4\_add\_option\_vendor\_callback](group__dhcpv4.md#gabf3d97139fc4f7122c1bdee52cb003cb)(struct net\_dhcpv4\_option\_callback \*cb);

193

[ 199](group__dhcpv4.md#ga1f362cce448226447d892f5ed8401db5)int [net\_dhcpv4\_remove\_option\_vendor\_callback](group__dhcpv4.md#ga1f362cce448226447d892f5ed8401db5)(struct net\_dhcpv4\_option\_callback \*cb);

200

[ 210](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)void [net\_dhcpv4\_start](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)(struct [net\_if](structnet__if.md) \*iface);

211

[ 221](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e)void [net\_dhcpv4\_stop](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e)(struct [net\_if](structnet__if.md) \*iface);

222

[ 232](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a)void [net\_dhcpv4\_restart](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a)(struct [net\_if](structnet__if.md) \*iface);

233

235

241const char \*net\_dhcpv4\_state\_name(enum net\_dhcpv4\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

242

244

[ 251](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c)const char \*[net\_dhcpv4\_msg\_type\_name](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c)(enum [net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8) msg\_type);

252

256

257#ifdef \_\_cplusplus

258}

259#endif

260

261#endif /\* ZEPHYR\_INCLUDE\_NET\_DHCPV4\_H\_ \*/

[net\_dhcpv4\_remove\_option\_vendor\_callback](group__dhcpv4.md#ga1f362cce448226447d892f5ed8401db5)

int net\_dhcpv4\_remove\_option\_vendor\_callback(struct net\_dhcpv4\_option\_callback \*cb)

Remove an application callback for encapsulated vendor-specific options.

[net\_dhcpv4\_msg\_type\_name](group__dhcpv4.md#ga571124b93b5dfdf3377877aded0c374c)

const char \* net\_dhcpv4\_msg\_type\_name(enum net\_dhcpv4\_msg\_type msg\_type)

Return a text representation of the msg\_type.

[net\_dhcpv4\_restart](group__dhcpv4.md#ga57979593bfb87d006e634b88a64bdf1a)

void net\_dhcpv4\_restart(struct net\_if \*iface)

Restart DHCPv4 client on an iface.

[net\_dhcpv4\_option\_callback\_handler\_t](group__dhcpv4.md#ga75caf142c6c4e058f78c7be0a4a35a9d)

void(\* net\_dhcpv4\_option\_callback\_handler\_t)(struct net\_dhcpv4\_option\_callback \*cb, size\_t length, enum net\_dhcpv4\_msg\_type msg\_type, struct net\_if \*iface)

Define the application callback handler function signature.

**Definition** dhcpv4.h:85

[net\_dhcpv4\_init\_option\_callback](group__dhcpv4.md#ga84df76c84de248a43e3e26d422cdfc2f)

static void net\_dhcpv4\_init\_option\_callback(struct net\_dhcpv4\_option\_callback \*callback, net\_dhcpv4\_option\_callback\_handler\_t handler, uint8\_t option, void \*data, size\_t max\_length)

Helper to initialize a struct net\_dhcpv4\_option\_callback properly.

**Definition** dhcpv4.h:133

[net\_dhcpv4\_stop](group__dhcpv4.md#ga910a416e25c2878b84319f6884883d8e)

void net\_dhcpv4\_stop(struct net\_if \*iface)

Stop DHCPv4 client on an iface.

[net\_dhcpv4\_remove\_option\_callback](group__dhcpv4.md#gaa90c4ba8010bcd2079512afe5f288dbb)

int net\_dhcpv4\_remove\_option\_callback(struct net\_dhcpv4\_option\_callback \*cb)

Remove an application callback.

[net\_dhcpv4\_add\_option\_vendor\_callback](group__dhcpv4.md#gabf3d97139fc4f7122c1bdee52cb003cb)

int net\_dhcpv4\_add\_option\_vendor\_callback(struct net\_dhcpv4\_option\_callback \*cb)

Add an application callback for encapsulated vendor-specific options.

[net\_dhcpv4\_msg\_type](group__dhcpv4.md#gacc66584b0776e5a79b1f4ceea479a7f8)

net\_dhcpv4\_msg\_type

DHCPv4 message types.

**Definition** dhcpv4.h:57

[net\_dhcpv4\_init\_option\_vendor\_callback](group__dhcpv4.md#gaec0f1c87f5093767a4bb1c43b8e18e72)

static void net\_dhcpv4\_init\_option\_vendor\_callback(struct net\_dhcpv4\_option\_callback \*callback, net\_dhcpv4\_option\_callback\_handler\_t handler, uint8\_t option, void \*data, size\_t max\_length)

Helper to initialize a struct net\_dhcpv4\_option\_callback for encapsulated vendor-specific options pro...

**Definition** dhcpv4.h:173

[net\_dhcpv4\_add\_option\_callback](group__dhcpv4.md#gaf073157fcd5cb2d18c40b8697d724a7c)

int net\_dhcpv4\_add\_option\_callback(struct net\_dhcpv4\_option\_callback \*cb)

Add an application callback.

[net\_dhcpv4\_start](group__dhcpv4.md#gafa2ddaa5cf17fbe5c4a3ca6fbf883cbe)

void net\_dhcpv4\_start(struct net\_if \*iface)

Start DHCPv4 client on an iface.

[NET\_DHCPV4\_MSG\_TYPE\_REQUEST](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a4ec90153e2775f013099541acc15b14e)

@ NET\_DHCPV4\_MSG\_TYPE\_REQUEST

Request message.

**Definition** dhcpv4.h:60

[NET\_DHCPV4\_MSG\_TYPE\_ACK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a77932735abd547927ed8eef61c9f4925)

@ NET\_DHCPV4\_MSG\_TYPE\_ACK

Acknowledge message.

**Definition** dhcpv4.h:62

[NET\_DHCPV4\_MSG\_TYPE\_OFFER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a7e2888c4bb7cd85e3fb99b72d1a90a4a)

@ NET\_DHCPV4\_MSG\_TYPE\_OFFER

Offer message.

**Definition** dhcpv4.h:59

[NET\_DHCPV4\_MSG\_TYPE\_RELEASE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a9255fce7b8a52f290f6406e039b298c5)

@ NET\_DHCPV4\_MSG\_TYPE\_RELEASE

Release message.

**Definition** dhcpv4.h:64

[NET\_DHCPV4\_MSG\_TYPE\_NAK](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8a95d3e660ab59bdfb9de09e95493055c4)

@ NET\_DHCPV4\_MSG\_TYPE\_NAK

Negative acknowledge message.

**Definition** dhcpv4.h:63

[NET\_DHCPV4\_MSG\_TYPE\_DISCOVER](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ab8cb4caf5ae9de5bf79f791630475f1d)

@ NET\_DHCPV4\_MSG\_TYPE\_DISCOVER

Discover message.

**Definition** dhcpv4.h:58

[NET\_DHCPV4\_MSG\_TYPE\_INFORM](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8aba941cf50fabac68e5d0e07fa923b866)

@ NET\_DHCPV4\_MSG\_TYPE\_INFORM

Inform message.

**Definition** dhcpv4.h:65

[NET\_DHCPV4\_MSG\_TYPE\_DECLINE](group__dhcpv4.md#ggacc66584b0776e5a79b1f4ceea479a7f8ad5e45accf00132a16a3c6042a21e7b9f)

@ NET\_DHCPV4\_MSG\_TYPE\_DECLINE

Decline message.

**Definition** dhcpv4.h:61

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

**Definition** net\_if.h:678

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv4.h](dhcpv4_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
