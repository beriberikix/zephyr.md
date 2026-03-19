---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__l2_8h_source.html
original_path: doxygen/html/net__l2_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_l2.h

[Go to the documentation of this file.](net__l2_8h.md)

[ 1](structnet__l2.md#a1faa6e5b0c9228dd52c64fc7f2fd8036)/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_L2\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_L2\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/net\_buf.h](net__buf_8h.md)>

17#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

18#include <[zephyr/net/capture.h](capture_8h.md)>

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

33

34struct [net\_if](structnet__if.md);

35

[ 37](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) {

[ 39](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231) [NET\_L2\_MULTICAST](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

40

[ 42](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1) [NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

43

[ 45](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8) [NET\_L2\_PROMISC\_MODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

46

[ 50](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1) [NET\_L2\_POINT\_TO\_POINT](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

51} \_\_packed;

52

[ 58](structnet__l2.md)struct [net\_l2](structnet__l2.md) {

63 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[recv](structnet__l2.md#a1faa6e5b0c9228dd52c64fc7f2fd8036))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

64

[ 71](structnet__l2.md#a17d649732c3bb6bf9cc77a4939eb8801) int (\*[send](structnet__l2.md#a17d649732c3bb6bf9cc77a4939eb8801))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

72

[ 77](structnet__l2.md#a5d42c51eb8dc4d6a990aa9ff88a66b94) int (\*[enable](structnet__l2.md#a5d42c51eb8dc4d6a990aa9ff88a66b94))(struct [net\_if](structnet__if.md) \*iface, bool [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

78

82 enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) (\*[get\_flags](structnet__l2.md#a492c5c75801b9c8784c9322805869334))(struct [net\_if](structnet__if.md) \*iface);

83

[ 87](structnet__l2.md#a9aed44777aa01efcd45874679c6ea1c2) int (\*[alloc](structnet__l2.md#a9aed44777aa01efcd45874679c6ea1c2))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt,

88 size\_t size, enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

89 [k\_timeout\_t](structk__timeout__t.md) timeout);

90};

91

93#define NET\_L2\_GET\_NAME(\_name) \_net\_l2\_##\_name

94#define NET\_L2\_DECLARE\_PUBLIC(\_name) \

95 extern const struct net\_l2 NET\_L2\_GET\_NAME(\_name)

96#define NET\_L2\_GET\_CTX\_TYPE(\_name) \_name##\_CTX\_TYPE

97

98#define VIRTUAL\_L2 VIRTUAL

99NET\_L2\_DECLARE\_PUBLIC(VIRTUAL\_L2);

100

101#define DUMMY\_L2 DUMMY

102#define DUMMY\_L2\_CTX\_TYPE void\*

103NET\_L2\_DECLARE\_PUBLIC(DUMMY\_L2);

104

105#define OFFLOADED\_NETDEV\_L2 OFFLOADED\_NETDEV

106NET\_L2\_DECLARE\_PUBLIC(OFFLOADED\_NETDEV\_L2);

107

108#define ETHERNET\_L2 ETHERNET

109NET\_L2\_DECLARE\_PUBLIC(ETHERNET\_L2);

110

111#define PPP\_L2 PPP

112NET\_L2\_DECLARE\_PUBLIC(PPP\_L2);

113

114#define IEEE802154\_L2 IEEE802154

115NET\_L2\_DECLARE\_PUBLIC(IEEE802154\_L2);

116

117#define OPENTHREAD\_L2 OPENTHREAD

118NET\_L2\_DECLARE\_PUBLIC(OPENTHREAD\_L2);

119

120#define CANBUS\_RAW\_L2 CANBUS\_RAW

121#define CANBUS\_RAW\_L2\_CTX\_TYPE void\*

122NET\_L2\_DECLARE\_PUBLIC(CANBUS\_RAW\_L2);

123

124#ifdef CONFIG\_NET\_L2\_CUSTOM\_IEEE802154

125#ifndef CUSTOM\_IEEE802154\_L2

126#define CUSTOM\_IEEE802154\_L2 CUSTOM\_IEEE802154

127#endif

128#define CUSTOM\_IEEE802154\_L2\_CTX\_TYPE void\*

129NET\_L2\_DECLARE\_PUBLIC(CUSTOM\_IEEE802154\_L2);

130#endif /\* CONFIG\_NET\_L2\_CUSTOM\_IEEE802154 \*/

131

132#define NET\_L2\_INIT(\_name, \_recv\_fn, \_send\_fn, \_enable\_fn, \_get\_flags\_fn, ...) \

133 const STRUCT\_SECTION\_ITERABLE(net\_l2, \

134 NET\_L2\_GET\_NAME(\_name)) = { \

135 .recv = (\_recv\_fn), \

136 .send = (\_send\_fn), \

137 .enable = (\_enable\_fn), \

138 .get\_flags = (\_get\_flags\_fn), \

139 .alloc = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

140 (NULL), \

141 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

142 }

143

144#define NET\_L2\_GET\_DATA(name, sfx) \_net\_l2\_data\_##name##sfx

145

146#define NET\_L2\_DATA\_INIT(name, sfx, ctx\_type) \

147 static ctx\_type NET\_L2\_GET\_DATA(name, sfx) \_\_used;

148

149typedef int (\*net\_l2\_send\_t)(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

150

151static inline int net\_l2\_send(net\_l2\_send\_t send\_fn,

152 const struct [device](structdevice.md) \*dev,

153 struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

154 struct [net\_pkt](structnet__pkt.md) \*pkt)

155{

156 net\_capture\_pkt([iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), pkt);

157

158 return send\_fn(dev, pkt);

159}

160

162

166

167#ifdef \_\_cplusplus

168}

169#endif

170

171#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_L2\_H\_ \*/

[capture.h](capture_8h.md)

Network packet capture definitions.

[device.h](device_8h.md)

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:103

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:37

[NET\_L2\_POINT\_TO\_POINT](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1)

@ NET\_L2\_POINT\_TO\_POINT

Is this L2 point-to-point with tunneling so no need to have IP address etc to network interface.

**Definition** net\_l2.h:50

[NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1)

@ NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE

Do not join solicited node multicast group.

**Definition** net\_l2.h:42

[NET\_L2\_PROMISC\_MODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8)

@ NET\_L2\_PROMISC\_MODE

Is promiscuous mode supported.

**Definition** net\_l2.h:45

[NET\_L2\_MULTICAST](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231)

@ NET\_L2\_MULTICAST

IP multicast supported.

**Definition** net\_l2.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[net\_buf.h](net__buf_8h.md)

Buffer management.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:58

[net\_l2::send](structnet__l2.md#a17d649732c3bb6bf9cc77a4939eb8801)

int(\* send)(struct net\_if \*iface, struct net\_pkt \*pkt)

This function is used by net core to push a packet to lower layer (interface's L2),...

**Definition** net\_l2.h:71

[net\_l2::recv](structnet__l2.md#a1faa6e5b0c9228dd52c64fc7f2fd8036)

enum net\_verdict(\* recv)(struct net\_if \*iface, struct net\_pkt \*pkt)

This function is used by net core to get iface's L2 layer parsing what's relevant to itself.

**Definition** net\_l2.h:63

[net\_l2::get\_flags](structnet__l2.md#a492c5c75801b9c8784c9322805869334)

enum net\_l2\_flags(\* get\_flags)(struct net\_if \*iface)

Return L2 flags for the network interface.

**Definition** net\_l2.h:82

[net\_l2::enable](structnet__l2.md#a5d42c51eb8dc4d6a990aa9ff88a66b94)

int(\* enable)(struct net\_if \*iface, bool state)

This function is used to enable/disable traffic over a network interface.

**Definition** net\_l2.h:77

[net\_l2::alloc](structnet__l2.md#a9aed44777aa01efcd45874679c6ea1c2)

int(\* alloc)(struct net\_if \*iface, struct net\_pkt \*pkt, size\_t size, enum net\_ip\_protocol proto, k\_timeout\_t timeout)

Optional function for reserving L2 header space for this technology.

**Definition** net\_l2.h:87

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:114

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_l2.h](net__l2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
