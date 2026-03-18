---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__l2_8h_source.html
original_path: doxygen/html/net__l2_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

16#include <[zephyr/net/buf.h](net_2buf_8h.md)>

17#include <[zephyr/net/capture.h](capture_8h.md)>

18#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

30

31struct [net\_if](structnet__if.md);

32

[ 34](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) {

[ 36](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231) [NET\_L2\_MULTICAST](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

37

[ 39](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1) [NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

40

[ 42](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8) [NET\_L2\_PROMISC\_MODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

43

[ 47](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1) [NET\_L2\_POINT\_TO\_POINT](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

48} \_\_packed;

49

[ 55](structnet__l2.md)struct [net\_l2](structnet__l2.md) {

60 enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) (\*[recv](structnet__l2.md#a1faa6e5b0c9228dd52c64fc7f2fd8036))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

61

[ 68](structnet__l2.md#a17d649732c3bb6bf9cc77a4939eb8801) int (\*[send](structnet__l2.md#a17d649732c3bb6bf9cc77a4939eb8801))(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

69

[ 74](structnet__l2.md#a5d42c51eb8dc4d6a990aa9ff88a66b94) int (\*[enable](structnet__l2.md#a5d42c51eb8dc4d6a990aa9ff88a66b94))(struct [net\_if](structnet__if.md) \*iface, bool [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

75

79 enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) (\*[get\_flags](structnet__l2.md#a492c5c75801b9c8784c9322805869334))(struct [net\_if](structnet__if.md) \*iface);

80};

81

83#define NET\_L2\_GET\_NAME(\_name) \_net\_l2\_##\_name

84#define NET\_L2\_DECLARE\_PUBLIC(\_name) \

85 extern const struct net\_l2 NET\_L2\_GET\_NAME(\_name)

86#define NET\_L2\_GET\_CTX\_TYPE(\_name) \_name##\_CTX\_TYPE

87

88#ifdef CONFIG\_NET\_L2\_VIRTUAL

89#define VIRTUAL\_L2 VIRTUAL

90NET\_L2\_DECLARE\_PUBLIC(VIRTUAL\_L2);

91#endif /\* CONFIG\_NET\_L2\_DUMMY \*/

92

93#ifdef CONFIG\_NET\_L2\_DUMMY

94#define DUMMY\_L2 DUMMY

95#define DUMMY\_L2\_CTX\_TYPE void\*

96NET\_L2\_DECLARE\_PUBLIC(DUMMY\_L2);

97#endif /\* CONFIG\_NET\_L2\_DUMMY \*/

98

99#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

100#define OFFLOADED\_NETDEV\_L2 OFFLOADED\_NETDEV

101NET\_L2\_DECLARE\_PUBLIC(OFFLOADED\_NETDEV\_L2);

102#endif /\* CONFIG\_NET\_OFFLOAD || CONFIG\_NET\_SOCKETS\_OFFLOAD \*/

103

104#ifdef CONFIG\_NET\_L2\_ETHERNET

105#define ETHERNET\_L2 ETHERNET

106NET\_L2\_DECLARE\_PUBLIC(ETHERNET\_L2);

107#endif /\* CONFIG\_NET\_L2\_ETHERNET \*/

108

109#ifdef CONFIG\_NET\_L2\_PPP

110#define PPP\_L2 PPP

111NET\_L2\_DECLARE\_PUBLIC(PPP\_L2);

112#endif /\* CONFIG\_NET\_L2\_PPP \*/

113

114#ifdef CONFIG\_NET\_L2\_IEEE802154

115#define IEEE802154\_L2 IEEE802154

116NET\_L2\_DECLARE\_PUBLIC(IEEE802154\_L2);

117#endif /\* CONFIG\_NET\_L2\_IEEE802154 \*/

118

119#ifdef CONFIG\_NET\_L2\_OPENTHREAD

120#define OPENTHREAD\_L2 OPENTHREAD

121NET\_L2\_DECLARE\_PUBLIC(OPENTHREAD\_L2);

122#endif /\* CONFIG\_NET\_L2\_OPENTHREAD \*/

123

124#ifdef CONFIG\_NET\_L2\_CANBUS\_RAW

125#define CANBUS\_RAW\_L2 CANBUS\_RAW

126#define CANBUS\_RAW\_L2\_CTX\_TYPE void\*

127NET\_L2\_DECLARE\_PUBLIC(CANBUS\_RAW\_L2);

128#endif /\* CONFIG\_NET\_L2\_CANBUS\_RAW \*/

129

130#ifdef CONFIG\_NET\_L2\_CUSTOM\_IEEE802154

131#ifndef CUSTOM\_IEEE802154\_L2

132#define CUSTOM\_IEEE802154\_L2 CUSTOM\_IEEE802154

133#endif

134#define CUSTOM\_IEEE802154\_L2\_CTX\_TYPE void\*

135NET\_L2\_DECLARE\_PUBLIC(CUSTOM\_IEEE802154\_L2);

136#endif /\* CONFIG\_NET\_L2\_CUSTOM\_IEEE802154 \*/

137

138#define NET\_L2\_INIT(\_name, \_recv\_fn, \_send\_fn, \_enable\_fn, \_get\_flags\_fn) \

139 const STRUCT\_SECTION\_ITERABLE(net\_l2, \

140 NET\_L2\_GET\_NAME(\_name)) = { \

141 .recv = (\_recv\_fn), \

142 .send = (\_send\_fn), \

143 .enable = (\_enable\_fn), \

144 .get\_flags = (\_get\_flags\_fn), \

145 }

146

147#define NET\_L2\_GET\_DATA(name, sfx) \_net\_l2\_data\_##name##sfx

148

149#define NET\_L2\_DATA\_INIT(name, sfx, ctx\_type) \

150 static ctx\_type NET\_L2\_GET\_DATA(name, sfx) \_\_used;

151

152typedef int (\*net\_l2\_send\_t)(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt);

153

154static inline int net\_l2\_send(net\_l2\_send\_t send\_fn,

155 const struct [device](structdevice.md) \*dev,

156 struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

157 struct [net\_pkt](structnet__pkt.md) \*pkt)

158{

159 net\_capture\_pkt([iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2), pkt);

160

161 return send\_fn(dev, pkt);

162}

163

165

169

170#ifdef \_\_cplusplus

171}

172#endif

173

174#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_L2\_H\_ \*/

[capture.h](capture_8h.md)

Network packet capture definitions.

[device.h](device_8h.md)

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:100

[net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)

net\_l2\_flags

L2 flags.

**Definition** net\_l2.h:34

[NET\_L2\_POINT\_TO\_POINT](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1)

@ NET\_L2\_POINT\_TO\_POINT

Is this L2 point-to-point with tunneling so no need to have IP address etc to network interface.

**Definition** net\_l2.h:47

[NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1)

@ NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE

Do not join solicited node multicast group.

**Definition** net\_l2.h:39

[NET\_L2\_PROMISC\_MODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8)

@ NET\_L2\_PROMISC\_MODE

Is promiscuous mode supported.

**Definition** net\_l2.h:42

[NET\_L2\_MULTICAST](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231)

@ NET\_L2\_MULTICAST

IP multicast supported.

**Definition** net\_l2.h:36

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[buf.h](net_2buf_8h.md)

Buffer management.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:55

[net\_l2::send](structnet__l2.md#a17d649732c3bb6bf9cc77a4939eb8801)

int(\* send)(struct net\_if \*iface, struct net\_pkt \*pkt)

This function is used by net core to push a packet to lower layer (interface's L2),...

**Definition** net\_l2.h:68

[net\_l2::recv](structnet__l2.md#a1faa6e5b0c9228dd52c64fc7f2fd8036)

enum net\_verdict(\* recv)(struct net\_if \*iface, struct net\_pkt \*pkt)

This function is used by net core to get iface's L2 layer parsing what's relevant to itself.

**Definition** net\_l2.h:60

[net\_l2::get\_flags](structnet__l2.md#a492c5c75801b9c8784c9322805869334)

enum net\_l2\_flags(\* get\_flags)(struct net\_if \*iface)

Return L2 flags for the network interface.

**Definition** net\_l2.h:79

[net\_l2::enable](structnet__l2.md#a5d42c51eb8dc4d6a990aa9ff88a66b94)

int(\* enable)(struct net\_if \*iface, bool state)

This function is used to enable/disable traffic over a network interface.

**Definition** net\_l2.h:74

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:90

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_l2.h](net__l2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
