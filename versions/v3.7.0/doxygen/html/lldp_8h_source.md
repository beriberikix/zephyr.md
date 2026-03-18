---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lldp_8h_source.html
original_path: doxygen/html/lldp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lldp.h

[Go to the documentation of this file.](lldp_8h.md)

1

6

7/\*

8 \* Copyright (c) 2017 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_LLDP\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_LLDP\_H\_

15

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

28

29#define LLDP\_TLV\_GET\_LENGTH(type\_length) (type\_length & BIT\_MASK(9))

30#define LLDP\_TLV\_GET\_TYPE(type\_length) ((uint8\_t)(type\_length >> 9))

31

32/\* LLDP Definitions \*/

33

34/\* According to the spec, End of LLDPDU TLV value is constant. \*/

35#define NET\_LLDP\_END\_LLDPDU\_VALUE 0x0000

36

37/\*

38 \* For the Chassis ID TLV Value, if subtype is a MAC address then we must

39 \* use values from CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC0 through

40 \* CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC5. If not, we use CONFIG\_NET\_LLDP\_CHASSIS\_ID.

41 \*

42 \* FIXME: implement a similar scheme for subtype 5 (network address).

43 \*/

44#if defined(CONFIG\_NET\_LLDP\_CHASSIS\_ID\_SUBTYPE)

45#if (CONFIG\_NET\_LLDP\_CHASSIS\_ID\_SUBTYPE == 4)

46#define NET\_LLDP\_CHASSIS\_ID\_VALUE \

47 { \

48 CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC0, \

49 CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC1, \

50 CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC2, \

51 CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC3, \

52 CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC4, \

53 CONFIG\_NET\_LLDP\_CHASSIS\_ID\_MAC5 \

54 }

55

56#define NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN (6)

57#else

58#define NET\_LLDP\_CHASSIS\_ID\_VALUE CONFIG\_NET\_LLDP\_CHASSIS\_ID

59#define NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN (sizeof(CONFIG\_NET\_LLDP\_CHASSIS\_ID) - 1)

60#endif

61#else

62#define NET\_LLDP\_CHASSIS\_ID\_VALUE 0

63#define NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN 0

64#endif

65

66/\*

67 \* For the Port ID TLV Value, if subtype is a MAC address then we must

68 \* use values from CONFIG\_NET\_LLDP\_PORT\_ID\_MAC0 through

69 \* CONFIG\_NET\_LLDP\_PORT\_ID\_MAC5. If not, we use CONFIG\_NET\_LLDP\_PORT\_ID.

70 \*

71 \* FIXME: implement a similar scheme for subtype 4 (network address).

72 \*/

73#if defined(CONFIG\_NET\_LLDP\_PORT\_ID\_SUBTYPE)

74#if (CONFIG\_NET\_LLDP\_PORT\_ID\_SUBTYPE == 3)

75#define NET\_LLDP\_PORT\_ID\_VALUE \

76 { \

77 CONFIG\_NET\_LLDP\_PORT\_ID\_MAC0, \

78 CONFIG\_NET\_LLDP\_PORT\_ID\_MAC1, \

79 CONFIG\_NET\_LLDP\_PORT\_ID\_MAC2, \

80 CONFIG\_NET\_LLDP\_PORT\_ID\_MAC3, \

81 CONFIG\_NET\_LLDP\_PORT\_ID\_MAC4, \

82 CONFIG\_NET\_LLDP\_PORT\_ID\_MAC5 \

83 }

84

85#define NET\_LLDP\_PORT\_ID\_VALUE\_LEN (6)

86#else

87#define NET\_LLDP\_PORT\_ID\_VALUE CONFIG\_NET\_LLDP\_PORT\_ID

88#define NET\_LLDP\_PORT\_ID\_VALUE\_LEN (sizeof(CONFIG\_NET\_LLDP\_PORT\_ID) - 1)

89#endif

90#else

91#define NET\_LLDP\_PORT\_ID\_VALUE 0

92#define NET\_LLDP\_PORT\_ID\_VALUE\_LEN 0

93#endif

94

95/\*

96 \* TLVs Length.

97 \* Note that TLVs that have a subtype must have a byte added to their length.

98 \*/

99#define NET\_LLDP\_CHASSIS\_ID\_TLV\_LEN (NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN + 1)

100#define NET\_LLDP\_PORT\_ID\_TLV\_LEN (NET\_LLDP\_PORT\_ID\_VALUE\_LEN + 1)

101#define NET\_LLDP\_TTL\_TLV\_LEN (2)

102

103/\*

104 \* Time to Live value.

105 \* Calculate based on section 9.2.5.22 from LLDP spec.

106 \*

107 \* FIXME: when the network interface is about to be ‘disabled’ TTL shall be set

108 \* to zero so LLDP Rx agents can invalidate the entry related to this node.

109 \*/

110#if defined(CONFIG\_NET\_LLDP\_TX\_INTERVAL) && defined(CONFIG\_NET\_LLDP\_TX\_HOLD)

111#define NET\_LLDP\_TTL \

112 MIN((CONFIG\_NET\_LLDP\_TX\_INTERVAL \* CONFIG\_NET\_LLDP\_TX\_HOLD) + 1, 65535)

113#endif

114

115

116struct [net\_if](structnet__if.md);

117

119

[ 121](group__lldp.md#gadd4273e4fe55757729008ce081771899)enum [net\_lldp\_tlv\_type](group__lldp.md#gadd4273e4fe55757729008ce081771899) {

[ 122](group__lldp.md#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a) [LLDP\_TLV\_END\_LLDPDU](group__lldp.md#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a) = 0,

[ 123](group__lldp.md#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6) [LLDP\_TLV\_CHASSIS\_ID](group__lldp.md#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6) = 1,

[ 124](group__lldp.md#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45) [LLDP\_TLV\_PORT\_ID](group__lldp.md#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45) = 2,

[ 125](group__lldp.md#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c) [LLDP\_TLV\_TTL](group__lldp.md#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c) = 3,

[ 126](group__lldp.md#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0) [LLDP\_TLV\_PORT\_DESC](group__lldp.md#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0) = 4,

[ 127](group__lldp.md#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9) [LLDP\_TLV\_SYSTEM\_NAME](group__lldp.md#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9) = 5,

[ 128](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782) [LLDP\_TLV\_SYSTEM\_DESC](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782) = 6,

[ 129](group__lldp.md#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521) [LLDP\_TLV\_SYSTEM\_CAPABILITIES](group__lldp.md#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521) = 7,

[ 130](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5) [LLDP\_TLV\_MANAGEMENT\_ADDR](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5) = 8,

131 /\* Types 9 - 126 are reserved. \*/

[ 132](group__lldp.md#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad) [LLDP\_TLV\_ORG\_SPECIFIC](group__lldp.md#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad) = 127,

133};

134

[ 136](structnet__lldp__chassis__tlv.md)struct [net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md) {

[ 138](structnet__lldp__chassis__tlv.md#af81d3102ad0ec1f7ef76bb1533dcc7cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type\_length](structnet__lldp__chassis__tlv.md#af81d3102ad0ec1f7ef76bb1533dcc7cd);

[ 140](structnet__lldp__chassis__tlv.md#ad9d415f6a1e9018953728de1b529fd98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subtype](structnet__lldp__chassis__tlv.md#ad9d415f6a1e9018953728de1b529fd98);

[ 142](structnet__lldp__chassis__tlv.md#a37b7e81a670595d1c6c77a45bf9cfc73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structnet__lldp__chassis__tlv.md#a37b7e81a670595d1c6c77a45bf9cfc73)[NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN];

143} \_\_packed;

144

[ 146](structnet__lldp__port__tlv.md)struct [net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md) {

[ 148](structnet__lldp__port__tlv.md#a710beaeda2ddd7933464e07cb87a2bfe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type\_length](structnet__lldp__port__tlv.md#a710beaeda2ddd7933464e07cb87a2bfe);

[ 150](structnet__lldp__port__tlv.md#a572a6fd721c68796a572410ac62f2f93) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subtype](structnet__lldp__port__tlv.md#a572a6fd721c68796a572410ac62f2f93);

[ 152](structnet__lldp__port__tlv.md#aecc83eaec39284b33c2e7cf07f0ffa05) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structnet__lldp__port__tlv.md#aecc83eaec39284b33c2e7cf07f0ffa05)[NET\_LLDP\_PORT\_ID\_VALUE\_LEN];

153} \_\_packed;

154

[ 156](structnet__lldp__time__to__live__tlv.md)struct [net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md) {

[ 158](structnet__lldp__time__to__live__tlv.md#a78b88d66184a0d25c413baf2fec495ab) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type\_length](structnet__lldp__time__to__live__tlv.md#a78b88d66184a0d25c413baf2fec495ab);

[ 160](structnet__lldp__time__to__live__tlv.md#ab967792a938a5d67f744e53be8d5f0fd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ttl](structnet__lldp__time__to__live__tlv.md#ab967792a938a5d67f744e53be8d5f0fd);

161} \_\_packed;

162

[ 167](structnet__lldpdu.md)struct [net\_lldpdu](structnet__lldpdu.md) {

[ 168](structnet__lldpdu.md#a1a1c80fe7462ddbfd84289735013834c) struct [net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md) [chassis\_id](structnet__lldpdu.md#a1a1c80fe7462ddbfd84289735013834c);

[ 169](structnet__lldpdu.md#aa55adafc5528576017c37a28413bdaf9) struct [net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md) [port\_id](structnet__lldpdu.md#aa55adafc5528576017c37a28413bdaf9);

[ 170](structnet__lldpdu.md#afbe0618b6d849b8ee7b225844ac399df) struct [net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md) [ttl](structnet__lldpdu.md#afbe0618b6d849b8ee7b225844ac399df);

171} \_\_packed;

172

[ 181](group__lldp.md#ga0efa1813c537dcf02e021db60049c284)int [net\_lldp\_config](group__lldp.md#ga0efa1813c537dcf02e021db60049c284)(struct [net\_if](structnet__if.md) \*iface, const struct [net\_lldpdu](structnet__lldpdu.md) \*lldpdu);

182

[ 192](group__lldp.md#ga9702175375a71eaab20f450291cb51ad)int [net\_lldp\_config\_optional](group__lldp.md#ga9702175375a71eaab20f450291cb51ad)(struct [net\_if](structnet__if.md) \*iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tlv,

193 size\_t len);

194

[ 198](group__lldp.md#ga38f3eff9da2f06e10defddb1776cdb37)void [net\_lldp\_init](group__lldp.md#ga38f3eff9da2f06e10defddb1776cdb37)(void);

199

213typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf))(struct [net\_if](structnet__if.md) \*iface,

214 struct [net\_pkt](structnet__pkt.md) \*pkt);

215

[ 224](group__lldp.md#ga61845c96c65d6df83f422a68e31162cf)int [net\_lldp\_register\_callback](group__lldp.md#ga61845c96c65d6df83f422a68e31162cf)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf) cb);

225

[ 234](group__lldp.md#gafde82841435942b1ce7cc91083c9a06f)enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [net\_lldp\_recv](group__lldp.md#gafde82841435942b1ce7cc91083c9a06f)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), struct [net\_pkt](structnet__pkt.md) \*pkt);

235

243#if defined(CONFIG\_NET\_LLDP)

244int [net\_lldp\_set\_lldpdu](group__lldp.md#ga961bc59567ffa2d5a4d21290d1d78407)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

245#else

[ 246](group__lldp.md#ga961bc59567ffa2d5a4d21290d1d78407)#define net\_lldp\_set\_lldpdu(iface)

247#endif

248

254#if defined(CONFIG\_NET\_LLDP)

255void [net\_lldp\_unset\_lldpdu](group__lldp.md#gafdd1b4cea9f560597c31a0e42d5341e0)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

256#else

[ 257](group__lldp.md#gafdd1b4cea9f560597c31a0e42d5341e0)#define net\_lldp\_unset\_lldpdu(iface)

258#endif

259

260#ifdef \_\_cplusplus

261}

262#endif

263

267

268#endif /\* ZEPHYR\_INCLUDE\_NET\_LLDP\_H\_ \*/

[net\_lldp\_config](group__lldp.md#ga0efa1813c537dcf02e021db60049c284)

int net\_lldp\_config(struct net\_if \*iface, const struct net\_lldpdu \*lldpdu)

Set the LLDP data unit for a network interface.

[net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf)

enum net\_verdict(\* net\_lldp\_recv\_cb\_t)(struct net\_if \*iface, struct net\_pkt \*pkt)

LLDP Receive packet callback.

**Definition** lldp.h:213

[net\_lldp\_init](group__lldp.md#ga38f3eff9da2f06e10defddb1776cdb37)

void net\_lldp\_init(void)

Initialize LLDP engine.

[net\_lldp\_register\_callback](group__lldp.md#ga61845c96c65d6df83f422a68e31162cf)

int net\_lldp\_register\_callback(struct net\_if \*iface, net\_lldp\_recv\_cb\_t cb)

Register LLDP Rx callback function.

[net\_lldp\_set\_lldpdu](group__lldp.md#ga961bc59567ffa2d5a4d21290d1d78407)

#define net\_lldp\_set\_lldpdu(iface)

Set LLDP protocol data unit (LLDPDU) for the network interface.

**Definition** lldp.h:246

[net\_lldp\_config\_optional](group__lldp.md#ga9702175375a71eaab20f450291cb51ad)

int net\_lldp\_config\_optional(struct net\_if \*iface, const uint8\_t \*tlv, size\_t len)

Set the Optional LLDP TLVs for a network interface.

[net\_lldp\_tlv\_type](group__lldp.md#gadd4273e4fe55757729008ce081771899)

net\_lldp\_tlv\_type

TLV Types.

**Definition** lldp.h:121

[net\_lldp\_unset\_lldpdu](group__lldp.md#gafdd1b4cea9f560597c31a0e42d5341e0)

#define net\_lldp\_unset\_lldpdu(iface)

Unset LLDP protocol data unit (LLDPDU) for the network interface.

**Definition** lldp.h:257

[net\_lldp\_recv](group__lldp.md#gafde82841435942b1ce7cc91083c9a06f)

enum net\_verdict net\_lldp\_recv(struct net\_if \*iface, struct net\_pkt \*pkt)

Parse LLDP packet.

[LLDP\_TLV\_ORG\_SPECIFIC](group__lldp.md#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad)

@ LLDP\_TLV\_ORG\_SPECIFIC

Org specific TLVs (optional).

**Definition** lldp.h:132

[LLDP\_TLV\_PORT\_ID](group__lldp.md#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45)

@ LLDP\_TLV\_PORT\_ID

Port ID (mandatory).

**Definition** lldp.h:124

[LLDP\_TLV\_END\_LLDPDU](group__lldp.md#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a)

@ LLDP\_TLV\_END\_LLDPDU

End Of LLDPDU (optional).

**Definition** lldp.h:122

[LLDP\_TLV\_PORT\_DESC](group__lldp.md#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0)

@ LLDP\_TLV\_PORT\_DESC

Port Description (optional).

**Definition** lldp.h:126

[LLDP\_TLV\_SYSTEM\_CAPABILITIES](group__lldp.md#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521)

@ LLDP\_TLV\_SYSTEM\_CAPABILITIES

System Capability (optional).

**Definition** lldp.h:129

[LLDP\_TLV\_MANAGEMENT\_ADDR](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5)

@ LLDP\_TLV\_MANAGEMENT\_ADDR

Management Address (optional).

**Definition** lldp.h:130

[LLDP\_TLV\_SYSTEM\_DESC](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782)

@ LLDP\_TLV\_SYSTEM\_DESC

System Description (optional).

**Definition** lldp.h:128

[LLDP\_TLV\_SYSTEM\_NAME](group__lldp.md#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9)

@ LLDP\_TLV\_SYSTEM\_NAME

System Name (optional).

**Definition** lldp.h:127

[LLDP\_TLV\_CHASSIS\_ID](group__lldp.md#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6)

@ LLDP\_TLV\_CHASSIS\_ID

Chassis ID (mandatory).

**Definition** lldp.h:123

[LLDP\_TLV\_TTL](group__lldp.md#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c)

@ LLDP\_TLV\_TTL

Time To Live (mandatory).

**Definition** lldp.h:125

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:100

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md)

Chassis ID TLV, see chapter 8.5.2 in IEEE 802.1AB.

**Definition** lldp.h:136

[net\_lldp\_chassis\_tlv::value](structnet__lldp__chassis__tlv.md#a37b7e81a670595d1c6c77a45bf9cfc73)

uint8\_t value[NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN]

Chassis ID value.

**Definition** lldp.h:142

[net\_lldp\_chassis\_tlv::subtype](structnet__lldp__chassis__tlv.md#ad9d415f6a1e9018953728de1b529fd98)

uint8\_t subtype

ID subtype.

**Definition** lldp.h:140

[net\_lldp\_chassis\_tlv::type\_length](structnet__lldp__chassis__tlv.md#af81d3102ad0ec1f7ef76bb1533dcc7cd)

uint16\_t type\_length

7 bits for type, 9 bits for length

**Definition** lldp.h:138

[net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md)

Port ID TLV, see chapter 8.5.3 in IEEE 802.1AB.

**Definition** lldp.h:146

[net\_lldp\_port\_tlv::subtype](structnet__lldp__port__tlv.md#a572a6fd721c68796a572410ac62f2f93)

uint8\_t subtype

ID subtype.

**Definition** lldp.h:150

[net\_lldp\_port\_tlv::type\_length](structnet__lldp__port__tlv.md#a710beaeda2ddd7933464e07cb87a2bfe)

uint16\_t type\_length

7 bits for type, 9 bits for length

**Definition** lldp.h:148

[net\_lldp\_port\_tlv::value](structnet__lldp__port__tlv.md#aecc83eaec39284b33c2e7cf07f0ffa05)

uint8\_t value[NET\_LLDP\_PORT\_ID\_VALUE\_LEN]

Port ID value.

**Definition** lldp.h:152

[net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md)

Time To Live TLV, see chapter 8.5.4 in IEEE 802.1AB.

**Definition** lldp.h:156

[net\_lldp\_time\_to\_live\_tlv::type\_length](structnet__lldp__time__to__live__tlv.md#a78b88d66184a0d25c413baf2fec495ab)

uint16\_t type\_length

7 bits for type, 9 bits for length

**Definition** lldp.h:158

[net\_lldp\_time\_to\_live\_tlv::ttl](structnet__lldp__time__to__live__tlv.md#ab967792a938a5d67f744e53be8d5f0fd)

uint16\_t ttl

Time To Live (TTL) value.

**Definition** lldp.h:160

[net\_lldpdu](structnet__lldpdu.md)

LLDP Data Unit (LLDPDU) shall contain the following ordered TLVs as stated in "8.2 LLDPDU format" fro...

**Definition** lldp.h:167

[net\_lldpdu::chassis\_id](structnet__lldpdu.md#a1a1c80fe7462ddbfd84289735013834c)

struct net\_lldp\_chassis\_tlv chassis\_id

Mandatory Chassis TLV.

**Definition** lldp.h:168

[net\_lldpdu::port\_id](structnet__lldpdu.md#aa55adafc5528576017c37a28413bdaf9)

struct net\_lldp\_port\_tlv port\_id

Mandatory Port TLV.

**Definition** lldp.h:169

[net\_lldpdu::ttl](structnet__lldpdu.md#afbe0618b6d849b8ee7b225844ac399df)

struct net\_lldp\_time\_to\_live\_tlv ttl

Mandatory TTL TLV.

**Definition** lldp.h:170

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [lldp.h](lldp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
