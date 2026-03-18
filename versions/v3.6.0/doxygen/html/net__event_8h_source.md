---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__event_8h_source.html
original_path: doxygen/html/net__event_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event.h

[Go to the documentation of this file.](net__event_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_

14

15#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

16#include <[zephyr/net/hostname.h](hostname_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

26

28

29/\* Network Interface events \*/

30#define \_NET\_IF\_LAYER NET\_MGMT\_LAYER\_L2

31#define \_NET\_IF\_CORE\_CODE 0x001

32#define \_NET\_EVENT\_IF\_BASE (NET\_MGMT\_EVENT\_BIT | \

33 NET\_MGMT\_IFACE\_BIT | \

34 NET\_MGMT\_LAYER(\_NET\_IF\_LAYER) | \

35 NET\_MGMT\_LAYER\_CODE(\_NET\_IF\_CORE\_CODE))

36

37enum net\_event\_if\_cmd {

38 NET\_EVENT\_IF\_CMD\_DOWN = 1,

39 NET\_EVENT\_IF\_CMD\_UP,

40 NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN,

41 NET\_EVENT\_IF\_CMD\_ADMIN\_UP,

42};

43

44#define NET\_EVENT\_IF\_DOWN \

45 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN)

46

47#define NET\_EVENT\_IF\_UP \

48 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP)

49

50#define NET\_EVENT\_IF\_ADMIN\_DOWN \

51 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN)

52

53#define NET\_EVENT\_IF\_ADMIN\_UP \

54 (\_NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP)

55

56/\* IPv6 Events \*/

57#define \_NET\_IPV6\_LAYER NET\_MGMT\_LAYER\_L3

58#define \_NET\_IPV6\_CORE\_CODE 0x060

59#define \_NET\_EVENT\_IPV6\_BASE (NET\_MGMT\_EVENT\_BIT | \

60 NET\_MGMT\_IFACE\_BIT | \

61 NET\_MGMT\_LAYER(\_NET\_IPV6\_LAYER) | \

62 NET\_MGMT\_LAYER\_CODE(\_NET\_IPV6\_CORE\_CODE))

63

64enum net\_event\_ipv6\_cmd {

65 NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD = 1,

66 NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL,

67 NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD,

68 NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL,

69 NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD,

70 NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL,

71 NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN,

72 NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE,

73 NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD,

74 NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL,

75 NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD,

76 NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL,

77 NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED,

78 NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED,

79 NET\_EVENT\_IPV6\_CMD\_NBR\_ADD,

80 NET\_EVENT\_IPV6\_CMD\_NBR\_DEL,

81 NET\_EVENT\_IPV6\_CMD\_DHCP\_START,

82 NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND,

83 NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP,

84};

85

86#define NET\_EVENT\_IPV6\_ADDR\_ADD \

87 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD)

88

89#define NET\_EVENT\_IPV6\_ADDR\_DEL \

90 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL)

91

92#define NET\_EVENT\_IPV6\_MADDR\_ADD \

93 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD)

94

95#define NET\_EVENT\_IPV6\_MADDR\_DEL \

96 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL)

97

98#define NET\_EVENT\_IPV6\_PREFIX\_ADD \

99 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD)

100

101#define NET\_EVENT\_IPV6\_PREFIX\_DEL \

102 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL)

103

104#define NET\_EVENT\_IPV6\_MCAST\_JOIN \

105 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN)

106

107#define NET\_EVENT\_IPV6\_MCAST\_LEAVE \

108 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE)

109

110#define NET\_EVENT\_IPV6\_ROUTER\_ADD \

111 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD)

112

113#define NET\_EVENT\_IPV6\_ROUTER\_DEL \

114 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL)

115

116#define NET\_EVENT\_IPV6\_ROUTE\_ADD \

117 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD)

118

119#define NET\_EVENT\_IPV6\_ROUTE\_DEL \

120 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL)

121

122#define NET\_EVENT\_IPV6\_DAD\_SUCCEED \

123 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED)

124

125#define NET\_EVENT\_IPV6\_DAD\_FAILED \

126 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED)

127

128#define NET\_EVENT\_IPV6\_NBR\_ADD \

129 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD)

130

131#define NET\_EVENT\_IPV6\_NBR\_DEL \

132 (\_NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL)

133

134#define NET\_EVENT\_IPV6\_DHCP\_START \

135 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START)

136

137#define NET\_EVENT\_IPV6\_DHCP\_BOUND \

138 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND)

139

140#define NET\_EVENT\_IPV6\_DHCP\_STOP \

141 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP)

142

143/\* IPv4 Events\*/

144#define \_NET\_IPV4\_LAYER NET\_MGMT\_LAYER\_L3

145#define \_NET\_IPV4\_CORE\_CODE 0x004

146#define \_NET\_EVENT\_IPV4\_BASE (NET\_MGMT\_EVENT\_BIT | \

147 NET\_MGMT\_IFACE\_BIT | \

148 NET\_MGMT\_LAYER(\_NET\_IPV4\_LAYER) | \

149 NET\_MGMT\_LAYER\_CODE(\_NET\_IPV4\_CORE\_CODE))

150

151enum net\_event\_ipv4\_cmd {

152 NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD = 1,

153 NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL,

154 NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD,

155 NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL,

156 NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD,

157 NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL,

158 NET\_EVENT\_IPV4\_CMD\_DHCP\_START,

159 NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND,

160 NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP,

161 NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN,

162 NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE,

163};

164

165#define NET\_EVENT\_IPV4\_ADDR\_ADD \

166 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD)

167

168#define NET\_EVENT\_IPV4\_ADDR\_DEL \

169 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL)

170

171#define NET\_EVENT\_IPV4\_MADDR\_ADD \

172 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD)

173

174#define NET\_EVENT\_IPV4\_MADDR\_DEL \

175 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL)

176

177#define NET\_EVENT\_IPV4\_ROUTER\_ADD \

178 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD)

179

180#define NET\_EVENT\_IPV4\_ROUTER\_DEL \

181 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL)

182

183#define NET\_EVENT\_IPV4\_DHCP\_START \

184 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START)

185

186#define NET\_EVENT\_IPV4\_DHCP\_BOUND \

187 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND)

188

189#define NET\_EVENT\_IPV4\_DHCP\_STOP \

190 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP)

191

192#define NET\_EVENT\_IPV4\_MCAST\_JOIN \

193 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN)

194

195#define NET\_EVENT\_IPV4\_MCAST\_LEAVE \

196 (\_NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE)

197

198

199/\* L4 network events \*/

200#define \_NET\_L4\_LAYER NET\_MGMT\_LAYER\_L4

201#define \_NET\_L4\_CORE\_CODE 0x114

202#define \_NET\_EVENT\_L4\_BASE (NET\_MGMT\_EVENT\_BIT | \

203 NET\_MGMT\_IFACE\_BIT | \

204 NET\_MGMT\_LAYER(\_NET\_L4\_LAYER) | \

205 NET\_MGMT\_LAYER\_CODE(\_NET\_L4\_CORE\_CODE))

206

207enum net\_event\_l4\_cmd {

208 NET\_EVENT\_L4\_CMD\_CONNECTED = 1,

209 NET\_EVENT\_L4\_CMD\_DISCONNECTED,

210 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD,

211 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL,

212 NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED,

213};

214

215#define NET\_EVENT\_L4\_CONNECTED \

216 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED)

217

218#define NET\_EVENT\_L4\_DISCONNECTED \

219 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED)

220

221#define NET\_EVENT\_DNS\_SERVER\_ADD \

222 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD)

223

224#define NET\_EVENT\_DNS\_SERVER\_DEL \

225 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL)

226

227#define NET\_EVENT\_HOSTNAME\_CHANGED \

228 (\_NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED)

229

231

[ 242](structnet__event__ipv6__addr.md)struct [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) {

[ 243](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43);

244};

245

[ 255](structnet__event__ipv6__nbr.md)struct [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) {

[ 256](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289);

[ 257](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee) int [idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee); /\* NBR index\*/

258};

259

[ 268](structnet__event__ipv6__route.md)struct [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) {

[ 269](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829) struct [in6\_addr](structin6__addr.md) [nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829);

[ 270](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c); /\* addr/prefix \*/

[ 271](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f);

272};

273

[ 282](structnet__event__ipv6__prefix.md)struct [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) {

[ 283](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb); /\* prefix \*/

[ 284](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace);

[ 285](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4);

286};

287

[ 294](structnet__event__l4__hostname.md)struct [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) {

[ 295](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245) char [hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)[[NET\_HOSTNAME\_SIZE](group__net__hostname.md#gabd1224299a2d7f1b81d1025bf9d9731f)];

296};

297

298#ifdef \_\_cplusplus

299}

300#endif

301

305

306#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_ \*/

[NET\_HOSTNAME\_SIZE](group__net__hostname.md#gabd1224299a2d7f1b81d1025bf9d9731f)

#define NET\_HOSTNAME\_SIZE

**Definition** hostname.h:39

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:242

[net\_event\_ipv6\_addr::addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43)

struct in6\_addr addr

**Definition** net\_event.h:243

[net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:255

[net\_event\_ipv6\_nbr::addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289)

struct in6\_addr addr

**Definition** net\_event.h:256

[net\_event\_ipv6\_nbr::idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee)

int idx

**Definition** net\_event.h:257

[net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:282

[net\_event\_ipv6\_prefix::len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace)

uint8\_t len

**Definition** net\_event.h:284

[net\_event\_ipv6\_prefix::addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb)

struct in6\_addr addr

**Definition** net\_event.h:283

[net\_event\_ipv6\_prefix::lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4)

uint32\_t lifetime

**Definition** net\_event.h:285

[net\_event\_ipv6\_route](structnet__event__ipv6__route.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:268

[net\_event\_ipv6\_route::addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c)

struct in6\_addr addr

**Definition** net\_event.h:270

[net\_event\_ipv6\_route::prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f)

uint8\_t prefix\_len

**Definition** net\_event.h:271

[net\_event\_ipv6\_route::nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829)

struct in6\_addr nexthop

**Definition** net\_event.h:269

[net\_event\_l4\_hostname](structnet__event__l4__hostname.md)

Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED...

**Definition** net\_event.h:294

[net\_event\_l4\_hostname::hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)

char hostname[NET\_HOSTNAME\_SIZE]

**Definition** net\_event.h:295

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_event.h](net__event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
