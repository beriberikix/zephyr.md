---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__event_8h_source.html
original_path: doxygen/html/net__event_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

16#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

17#include <[zephyr/net/hostname.h](hostname_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

27

29

30/\* Network Interface events \*/

31#define NET\_IF\_LAYER NET\_MGMT\_LAYER\_L2

32#define NET\_IF\_CORE\_CODE NET\_MGMT\_LAYER\_CODE\_IFACE

33#define NET\_EVENT\_IF\_BASE (NET\_MGMT\_EVENT\_BIT | \

34 NET\_MGMT\_IFACE\_BIT | \

35 NET\_MGMT\_LAYER(NET\_IF\_LAYER) | \

36 NET\_MGMT\_LAYER\_CODE(NET\_IF\_CORE\_CODE))

37

38enum {

39 NET\_EVENT\_IF\_CMD\_DOWN\_VAL,

40 NET\_EVENT\_IF\_CMD\_UP\_VAL,

41 NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN\_VAL,

42 NET\_EVENT\_IF\_CMD\_ADMIN\_UP\_VAL,

43

44 NET\_EVENT\_IF\_CMD\_MAX

45};

46

47BUILD\_ASSERT(NET\_EVENT\_IF\_CMD\_MAX <= NET\_MGMT\_MAX\_COMMANDS,

48 "Number of events in net\_event\_if\_cmd exceeds the limit");

49

50enum net\_event\_if\_cmd {

51 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IF\_CMD\_DOWN),

52 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IF\_CMD\_UP),

53 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN),

54 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IF\_CMD\_ADMIN\_UP),

55};

56

57/\* IPv6 Events \*/

58#define NET\_IPV6\_LAYER NET\_MGMT\_LAYER\_L3

59#define NET\_IPV6\_CORE\_CODE NET\_MGMT\_LAYER\_CODE\_IPV6

60#define NET\_EVENT\_IPV6\_BASE (NET\_MGMT\_EVENT\_BIT | \

61 NET\_MGMT\_IFACE\_BIT | \

62 NET\_MGMT\_LAYER(NET\_IPV6\_LAYER) | \

63 NET\_MGMT\_LAYER\_CODE(NET\_IPV6\_CORE\_CODE))

64

65enum {

66 NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD\_VAL,

67 NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL\_VAL,

68 NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD\_VAL,

69 NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL\_VAL,

70 NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD\_VAL,

71 NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL\_VAL,

72 NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN\_VAL,

73 NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE\_VAL,

74 NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD\_VAL,

75 NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL\_VAL,

76 NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD\_VAL,

77 NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL\_VAL,

78 NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED\_VAL,

79 NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED\_VAL,

80 NET\_EVENT\_IPV6\_CMD\_NBR\_ADD\_VAL,

81 NET\_EVENT\_IPV6\_CMD\_NBR\_DEL\_VAL,

82 NET\_EVENT\_IPV6\_CMD\_DHCP\_START\_VAL,

83 NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND\_VAL,

84 NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP\_VAL,

85 NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED\_VAL,

86 NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED\_VAL,

87 NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED\_VAL,

88 NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD\_VAL,

89 NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL\_VAL,

90 NET\_EVENT\_IPV6\_CMD\_PMTU\_CHANGED\_VAL,

91

92 NET\_EVENT\_IPV6\_CMD\_MAX

93};

94

95BUILD\_ASSERT(NET\_EVENT\_IPV6\_CMD\_MAX <= NET\_MGMT\_MAX\_COMMANDS,

96 "Number of events in net\_event\_ipv6\_cmd exceeds the limit");

97

98enum net\_event\_ipv6\_cmd {

99 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD),

100 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL),

101 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD),

102 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL),

103 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD),

104 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL),

105 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN),

106 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE),

107 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD),

108 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL),

109 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD),

110 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL),

111 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED),

112 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED),

113 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_NBR\_ADD),

114 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_NBR\_DEL),

115 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_DHCP\_START),

116 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND),

117 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP),

118 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED),

119 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED),

120 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED),

121 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD),

122 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL),

123 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV6\_CMD\_PMTU\_CHANGED),

124};

125

126/\* IPv4 Events\*/

127#define NET\_IPV4\_LAYER NET\_MGMT\_LAYER\_L3

128#define NET\_IPV4\_CORE\_CODE NET\_MGMT\_LAYER\_CODE\_IPV4

129#define NET\_EVENT\_IPV4\_BASE (NET\_MGMT\_EVENT\_BIT | \

130 NET\_MGMT\_IFACE\_BIT | \

131 NET\_MGMT\_LAYER(NET\_IPV4\_LAYER) | \

132 NET\_MGMT\_LAYER\_CODE(NET\_IPV4\_CORE\_CODE))

133

134enum {

135 NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD\_VAL,

136 NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL\_VAL,

137 NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD\_VAL,

138 NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL\_VAL,

139 NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD\_VAL,

140 NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL\_VAL,

141 NET\_EVENT\_IPV4\_CMD\_DHCP\_START\_VAL,

142 NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND\_VAL,

143 NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP\_VAL,

144 NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN\_VAL,

145 NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE\_VAL,

146 NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED\_VAL,

147 NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED\_VAL,

148 NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT\_VAL,

149 NET\_EVENT\_IPV4\_CMD\_PMTU\_CHANGED\_VAL,

150

151 NET\_EVENT\_IPV4\_CMD\_MAX

152};

153

154BUILD\_ASSERT(NET\_EVENT\_IPV4\_CMD\_MAX <= NET\_MGMT\_MAX\_COMMANDS,

155 "Number of events in net\_event\_ipv4\_cmd exceeds the limit");

156

157enum net\_event\_ipv4\_cmd {

158 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD),

159 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL),

160 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD),

161 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL),

162 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD),

163 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL),

164 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_DHCP\_START),

165 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND),

166 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP),

167 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN),

168 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE),

169 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED),

170 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED),

171 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT),

172 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_IPV4\_CMD\_PMTU\_CHANGED),

173};

174

175/\* L4 network events \*/

176#define NET\_L4\_LAYER NET\_MGMT\_LAYER\_L4

177#define NET\_L4\_CORE\_CODE NET\_MGMT\_LAYER\_CODE\_L4

178#define NET\_EVENT\_L4\_BASE (NET\_MGMT\_EVENT\_BIT | \

179 NET\_MGMT\_IFACE\_BIT | \

180 NET\_MGMT\_LAYER(NET\_L4\_LAYER) | \

181 NET\_MGMT\_LAYER\_CODE(NET\_L4\_CORE\_CODE))

182

183enum {

184 NET\_EVENT\_L4\_CMD\_CONNECTED\_VAL,

185 NET\_EVENT\_L4\_CMD\_DISCONNECTED\_VAL,

186 NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED\_VAL,

187 NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED\_VAL,

188 NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED\_VAL,

189 NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED\_VAL,

190 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD\_VAL,

191 NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL\_VAL,

192 NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED\_VAL,

193 NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED\_VAL,

194 NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED\_VAL,

195 NET\_EVENT\_L4\_CMD\_VPN\_CONNECTED\_VAL,

196 NET\_EVENT\_L4\_CMD\_VPN\_DISCONNECTED\_VAL,

197 NET\_EVENT\_L4\_CMD\_VPN\_PEER\_ADD\_VAL,

198 NET\_EVENT\_L4\_CMD\_VPN\_PEER\_DEL\_VAL,

199

200 NET\_EVENT\_L4\_CMD\_MAX

201};

202

203BUILD\_ASSERT(NET\_EVENT\_L4\_CMD\_MAX <= NET\_MGMT\_MAX\_COMMANDS,

204 "Number of events in net\_event\_l4\_cmd exceeds the limit");

205

206enum net\_event\_l4\_cmd {

207 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_CONNECTED),

208 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_DISCONNECTED),

209 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED),

210 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED),

211 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED),

212 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED),

213 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD),

214 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL),

215 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED),

216 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED),

217 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED),

218 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_VPN\_CONNECTED),

219 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_VPN\_DISCONNECTED),

220 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_VPN\_PEER\_ADD),

221 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_L4\_CMD\_VPN\_PEER\_DEL),

222};

223

225

[ 227](group__net__mgmt.md#gac43a928bce3feb217b37ff7eb205e71b)#define NET\_EVENT\_IF\_DOWN \

228 (NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_DOWN)

229

[ 231](group__net__mgmt.md#gaddc84a60607bb27048397e29eb9107f5)#define NET\_EVENT\_IF\_UP \

232 (NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_UP)

233

[ 235](group__net__mgmt.md#gacb6ac7a4579be883abc9aa638299b0cd)#define NET\_EVENT\_IF\_ADMIN\_DOWN \

236 (NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_DOWN)

237

[ 239](group__net__mgmt.md#ga94a52eb94cc2189919ade9c8c8f239bd)#define NET\_EVENT\_IF\_ADMIN\_UP \

240 (NET\_EVENT\_IF\_BASE | NET\_EVENT\_IF\_CMD\_ADMIN\_UP)

241

[ 243](group__net__mgmt.md#ga20125c6148169a91fbebab1ebba17be3)#define NET\_EVENT\_IPV6\_ADDR\_ADD \

244 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_ADD)

245

[ 247](group__net__mgmt.md#ga61f243efbc25928815ec78305b4f000e)#define NET\_EVENT\_IPV6\_ADDR\_DEL \

248 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEL)

249

[ 251](group__net__mgmt.md#gadda9dccf913a4dcb4d12b2b1fe5d403c)#define NET\_EVENT\_IPV6\_MADDR\_ADD \

252 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_ADD)

253

[ 255](group__net__mgmt.md#ga035db32f66effd2407e0cca4b1fd9ea3)#define NET\_EVENT\_IPV6\_MADDR\_DEL \

256 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MADDR\_DEL)

257

[ 259](group__net__mgmt.md#ga392414b95838bca1e55e4342870a8333)#define NET\_EVENT\_IPV6\_PREFIX\_ADD \

260 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_ADD)

261

[ 263](group__net__mgmt.md#gab06f93335938a635966e85a18b5b0cf6)#define NET\_EVENT\_IPV6\_PREFIX\_DEL \

264 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PREFIX\_DEL)

265

[ 267](group__net__mgmt.md#ga287d37bae2d74e0c85de59c5e23d409a)#define NET\_EVENT\_IPV6\_MCAST\_JOIN \

268 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_JOIN)

269

[ 271](group__net__mgmt.md#ga862d1b2ce9b65c0806ef77909364a58d)#define NET\_EVENT\_IPV6\_MCAST\_LEAVE \

272 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_MCAST\_LEAVE)

273

[ 275](group__net__mgmt.md#gaae932293528aa40127a906c3dbd45e31)#define NET\_EVENT\_IPV6\_ROUTER\_ADD \

276 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_ADD)

277

[ 279](group__net__mgmt.md#ga8d4b7798981aaaf3aea2b793739143b7)#define NET\_EVENT\_IPV6\_ROUTER\_DEL \

280 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTER\_DEL)

281

[ 283](group__net__mgmt.md#gad19b5e742ded9b3ed673d8f7985100fd)#define NET\_EVENT\_IPV6\_ROUTE\_ADD \

284 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_ADD)

285

[ 287](group__net__mgmt.md#gae6f68ec69032ac049f072d6ed164987c)#define NET\_EVENT\_IPV6\_ROUTE\_DEL \

288 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ROUTE\_DEL)

289

[ 291](group__net__mgmt.md#ga8711b4b1e88c897196b982e4d56968f1)#define NET\_EVENT\_IPV6\_DAD\_SUCCEED \

292 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_SUCCEED)

293

[ 295](group__net__mgmt.md#ga0d5013ea3a6fa3bddd5cb182dd616151)#define NET\_EVENT\_IPV6\_DAD\_FAILED \

296 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DAD\_FAILED)

297

[ 299](group__net__mgmt.md#ga96fe7da048fe4d59435b7337626d4af7)#define NET\_EVENT\_IPV6\_NBR\_ADD \

300 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_ADD)

301

[ 303](group__net__mgmt.md#ga5be1cdfeb1b8da485b1042a7b2dc14e4)#define NET\_EVENT\_IPV6\_NBR\_DEL \

304 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_NBR\_DEL)

305

[ 307](group__net__mgmt.md#gaa07a5e8779ec24e5ab883970bcec6c5e)#define NET\_EVENT\_IPV6\_DHCP\_START \

308 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_START)

309

[ 311](group__net__mgmt.md#gaff89dbc7562a85e9ff073b507bdf06e3)#define NET\_EVENT\_IPV6\_DHCP\_BOUND \

312 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_BOUND)

313

[ 315](group__net__mgmt.md#gaab05d5a65ef5f9ed147e32ce380f7de4)#define NET\_EVENT\_IPV6\_DHCP\_STOP \

316 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_DHCP\_STOP)

317

[ 319](group__net__mgmt.md#ga6cc42e3ca8197e46809de6082602ab98)#define NET\_EVENT\_IPV6\_ADDR\_DEPRECATED \

320 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_ADDR\_DEPRECATED)

321

[ 323](group__net__mgmt.md#ga95f7a737a39fb655d3577405e70e04ba)#define NET\_EVENT\_IPV6\_PE\_ENABLED \

324 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_ENABLED)

325

[ 327](group__net__mgmt.md#gaba20579e42c4cebc8c3ac9a40ff384f3)#define NET\_EVENT\_IPV6\_PE\_DISABLED \

328 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_DISABLED)

329

[ 331](group__net__mgmt.md#ga19d671971cf07e76580db8098ab32971)#define NET\_EVENT\_IPV6\_PE\_FILTER\_ADD \

332 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_ADD)

333

[ 335](group__net__mgmt.md#gaf2f1c4b8dc5b9b07985265cee6a90f70)#define NET\_EVENT\_IPV6\_PE\_FILTER\_DEL \

336 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PE\_FILTER\_DEL)

337

[ 339](group__net__mgmt.md#gae0e1924aa8c8f6dc47582883528df185)#define NET\_EVENT\_IPV6\_PMTU\_CHANGED \

340 (NET\_EVENT\_IPV6\_BASE | NET\_EVENT\_IPV6\_CMD\_PMTU\_CHANGED)

341

[ 343](group__net__mgmt.md#gad422365df617ce1473412908738048f0)#define NET\_EVENT\_IPV4\_ADDR\_ADD \

344 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_ADD)

345

[ 347](group__net__mgmt.md#ga0d78644f799d1d8f5c18ec9860582817)#define NET\_EVENT\_IPV4\_ADDR\_DEL \

348 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ADDR\_DEL)

349

[ 351](group__net__mgmt.md#ga854e897d09eecccc83d04d86fbba5b64)#define NET\_EVENT\_IPV4\_MADDR\_ADD \

352 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_ADD)

353

[ 355](group__net__mgmt.md#ga303824277664ee64674b7c93ff865bb4)#define NET\_EVENT\_IPV4\_MADDR\_DEL \

356 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MADDR\_DEL)

357

[ 359](group__net__mgmt.md#ga740c97a7e94181ad734888bbe7b0a3d0)#define NET\_EVENT\_IPV4\_ROUTER\_ADD \

360 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_ADD)

361

[ 363](group__net__mgmt.md#gae45a3b6a5f4b72edc51e06a22b88239a)#define NET\_EVENT\_IPV4\_ROUTER\_DEL \

364 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ROUTER\_DEL)

365

[ 367](group__net__mgmt.md#ga2d3a9351c226b1542d1b2f469b77233a)#define NET\_EVENT\_IPV4\_DHCP\_START \

368 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_START)

369

[ 371](group__net__mgmt.md#ga7461ef85f4f8433851cb7583468c00cb)#define NET\_EVENT\_IPV4\_DHCP\_BOUND \

372 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_BOUND)

373

[ 375](group__net__mgmt.md#gabc06b6010780ab2d1e4f88227965b4e7)#define NET\_EVENT\_IPV4\_DHCP\_STOP \

376 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_DHCP\_STOP)

377

[ 379](group__net__mgmt.md#ga17ad57d81f3046555f94f75dc6d31ec1)#define NET\_EVENT\_IPV4\_MCAST\_JOIN \

380 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_JOIN)

381

[ 383](group__net__mgmt.md#ga3cbb8a9dfec8435b93d908171ab944c9)#define NET\_EVENT\_IPV4\_MCAST\_LEAVE \

384 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_MCAST\_LEAVE)

385

[ 387](group__net__mgmt.md#ga5293377de1fdc79e7564f4e5104a07c2)#define NET\_EVENT\_IPV4\_ACD\_SUCCEED \

388 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_SUCCEED)

389

[ 391](group__net__mgmt.md#ga3de741f5732473a1f49d9d0b93183549)#define NET\_EVENT\_IPV4\_ACD\_FAILED \

392 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_FAILED)

393

[ 398](group__net__mgmt.md#ga9af1f8f4ba965e6d6e82a190ab4748a1)#define NET\_EVENT\_IPV4\_ACD\_CONFLICT \

399 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_ACD\_CONFLICT)

400

[ 402](group__net__mgmt.md#ga24766ef249022c198299d38e95f400b9)#define NET\_EVENT\_IPV4\_PMTU\_CHANGED \

403 (NET\_EVENT\_IPV4\_BASE | NET\_EVENT\_IPV4\_CMD\_PMTU\_CHANGED)

404

[ 409](group__net__mgmt.md#gacbd2b10cc345359c07de4a62eb172a09)#define NET\_EVENT\_L4\_CONNECTED \

410 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CONNECTED)

411

[ 417](group__net__mgmt.md#gacd9e0b5e2f540794b20f11b070ffbd65)#define NET\_EVENT\_L4\_DISCONNECTED \

418 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DISCONNECTED)

419

420

[ 422](group__net__mgmt.md#ga532fdc2f199e047a5d17e325cee12cf1)#define NET\_EVENT\_L4\_IPV4\_CONNECTED \

423 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_CONNECTED)

424

[ 426](group__net__mgmt.md#gaa92cc806d93446d548a05edb8e0074c2)#define NET\_EVENT\_L4\_IPV4\_DISCONNECTED \

427 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV4\_DISCONNECTED)

428

[ 430](group__net__mgmt.md#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)#define NET\_EVENT\_L4\_IPV6\_CONNECTED \

431 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_CONNECTED)

432

[ 434](group__net__mgmt.md#gac81abeab44fbf2b6f29d4e11a1e1bd17)#define NET\_EVENT\_L4\_IPV6\_DISCONNECTED \

435 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_IPV6\_DISCONNECTED)

436

[ 438](group__net__mgmt.md#ga5735d13f24c974ad6d4038c93edf05e0)#define NET\_EVENT\_DNS\_SERVER\_ADD \

439 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_ADD)

440

[ 442](group__net__mgmt.md#ga9d406772e5d1ad2952b2a2e0fed05c73)#define NET\_EVENT\_DNS\_SERVER\_DEL \

443 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_DNS\_SERVER\_DEL)

444

[ 446](group__net__mgmt.md#gac5a7458d89e4a95564999dca3c1b9f1e)#define NET\_EVENT\_HOSTNAME\_CHANGED \

447 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_HOSTNAME\_CHANGED)

448

[ 450](group__net__mgmt.md#gaa89b82a1890c55775f8c3c24e11f40e2)#define NET\_EVENT\_CAPTURE\_STARTED \

451 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STARTED)

452

[ 454](group__net__mgmt.md#gaa2b655aedd597636790409539b1f86cd)#define NET\_EVENT\_CAPTURE\_STOPPED \

455 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_CAPTURE\_STOPPED)

456

[ 458](group__net__mgmt.md#ga8084de14ebd35b4d32075642e952ca4d)#define NET\_EVENT\_VPN\_CONNECTED \

459 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_VPN\_CONNECTED)

460

[ 462](group__net__mgmt.md#ga74e837120225c10f0ccfa38696051cb8)#define NET\_EVENT\_VPN\_DISCONNECTED \

463 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_VPN\_DISCONNECTED)

464

[ 466](group__net__mgmt.md#gace9ee5cff7234717a9f183b89dcd28a3)#define NET\_EVENT\_VPN\_PEER\_ADD \

467 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_VPN\_PEER\_ADD)

468

[ 470](group__net__mgmt.md#ga03f4fcb1977379401e2b6ea83ad37883)#define NET\_EVENT\_VPN\_PEER\_DEL \

471 (NET\_EVENT\_L4\_BASE | NET\_EVENT\_L4\_CMD\_VPN\_PEER\_DEL)

472

[ 483](structnet__event__ipv6__addr.md)struct [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) {

[ 485](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43);

486};

487

[ 497](structnet__event__ipv6__nbr.md)struct [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) {

[ 499](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289);

[ 501](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee) int [idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee);

502};

503

[ 512](structnet__event__ipv6__route.md)struct [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) {

[ 514](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829) struct [in6\_addr](structin6__addr.md) [nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829);

[ 516](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c);

[ 518](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f);

519};

520

[ 529](structnet__event__ipv6__prefix.md)struct [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) {

[ 531](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb) struct [in6\_addr](structin6__addr.md) [addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb);

[ 533](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace);

[ 535](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4);

536};

537

[ 544](structnet__event__l4__hostname.md)struct [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) {

[ 546](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245) char [hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)[NET\_HOSTNAME\_SIZE];

547};

548

[ 559](structnet__event__ipv6__pe__filter.md)struct [net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md) {

[ 561](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc) struct [in6\_addr](structin6__addr.md) [prefix](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc);

[ 563](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a) bool [is\_deny\_list](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a);

564};

565

[ 573](structnet__event__ipv4__pmtu__info.md)struct [net\_event\_ipv4\_pmtu\_info](structnet__event__ipv4__pmtu__info.md) {

[ 575](structnet__event__ipv4__pmtu__info.md#a9779ec9487b5dde4d5df1d0aeef82ebf) struct [in\_addr](structin__addr.md) [dst](structnet__event__ipv4__pmtu__info.md#a9779ec9487b5dde4d5df1d0aeef82ebf);

[ 577](structnet__event__ipv4__pmtu__info.md#ae4f6951aed4253428a7ac4273b8b43fe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structnet__event__ipv4__pmtu__info.md#ae4f6951aed4253428a7ac4273b8b43fe);

578};

579

[ 587](structnet__event__ipv6__pmtu__info.md)struct [net\_event\_ipv6\_pmtu\_info](structnet__event__ipv6__pmtu__info.md) {

[ 589](structnet__event__ipv6__pmtu__info.md#aa9398dc7f56432b7489bcba7e9a6803c) struct [in6\_addr](structin6__addr.md) [dst](structnet__event__ipv6__pmtu__info.md#aa9398dc7f56432b7489bcba7e9a6803c);

[ 591](structnet__event__ipv6__pmtu__info.md#a52e5078e0f39cb5e95d4e5bc42674480) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mtu](structnet__event__ipv6__pmtu__info.md#a52e5078e0f39cb5e95d4e5bc42674480);

592};

593

594#ifdef \_\_cplusplus

595}

596#endif

597

601

602#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_EVENT\_H\_ \*/

[NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)

@ NET\_MGMT\_CMD

Scan results available.

**Definition** wifi\_mgmt.h:352

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[net\_event\_ipv4\_pmtu\_info](structnet__event__ipv4__pmtu__info.md)

Network Management event information structure Used to pass information on network event NET\_EVENT\_IP...

**Definition** net\_event.h:573

[net\_event\_ipv4\_pmtu\_info::dst](structnet__event__ipv4__pmtu__info.md#a9779ec9487b5dde4d5df1d0aeef82ebf)

struct in\_addr dst

IPv4 address.

**Definition** net\_event.h:575

[net\_event\_ipv4\_pmtu\_info::mtu](structnet__event__ipv4__pmtu__info.md#ae4f6951aed4253428a7ac4273b8b43fe)

uint16\_t mtu

New MTU.

**Definition** net\_event.h:577

[net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:483

[net\_event\_ipv6\_addr::addr](structnet__event__ipv6__addr.md#a3cb4dd6d1e33ef2769cd64fa27c69b43)

struct in6\_addr addr

IPv6 address related to this event.

**Definition** net\_event.h:485

[net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:497

[net\_event\_ipv6\_nbr::addr](structnet__event__ipv6__nbr.md#a75653facd98b568c300395c45191b289)

struct in6\_addr addr

Neighbor IPv6 address.

**Definition** net\_event.h:499

[net\_event\_ipv6\_nbr::idx](structnet__event__ipv6__nbr.md#adeb139ad70e794d1a805315ffd1fcbee)

int idx

Neighbor index in cache.

**Definition** net\_event.h:501

[net\_event\_ipv6\_pe\_filter](structnet__event__ipv6__pe__filter.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:559

[net\_event\_ipv6\_pe\_filter::is\_deny\_list](structnet__event__ipv6__pe__filter.md#a07961a42f5ff8ca98615164192b8ca5a)

bool is\_deny\_list

IPv6 filter deny or allow list.

**Definition** net\_event.h:563

[net\_event\_ipv6\_pe\_filter::prefix](structnet__event__ipv6__pe__filter.md#a2c0b6477f021e32bae98916f74e6affc)

struct in6\_addr prefix

IPv6 address of privacy extension filter.

**Definition** net\_event.h:561

[net\_event\_ipv6\_pmtu\_info](structnet__event__ipv6__pmtu__info.md)

Network Management event information structure Used to pass information on network event NET\_EVENT\_IP...

**Definition** net\_event.h:587

[net\_event\_ipv6\_pmtu\_info::mtu](structnet__event__ipv6__pmtu__info.md#a52e5078e0f39cb5e95d4e5bc42674480)

uint32\_t mtu

New MTU.

**Definition** net\_event.h:591

[net\_event\_ipv6\_pmtu\_info::dst](structnet__event__ipv6__pmtu__info.md#aa9398dc7f56432b7489bcba7e9a6803c)

struct in6\_addr dst

IPv6 address.

**Definition** net\_event.h:589

[net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:529

[net\_event\_ipv6\_prefix::len](structnet__event__ipv6__prefix.md#a3d70216e13fc0f78e08eb27f34fe8ace)

uint8\_t len

IPv6 prefix length.

**Definition** net\_event.h:533

[net\_event\_ipv6\_prefix::addr](structnet__event__ipv6__prefix.md#a5ccae593ce7678fcdd91a4d0eaf142fb)

struct in6\_addr addr

IPv6 prefix.

**Definition** net\_event.h:531

[net\_event\_ipv6\_prefix::lifetime](structnet__event__ipv6__prefix.md#a6d7b0323896e43a04931ece4daaa09c4)

uint32\_t lifetime

IPv6 prefix lifetime in seconds.

**Definition** net\_event.h:535

[net\_event\_ipv6\_route](structnet__event__ipv6__route.md)

Network Management event information structure Used to pass information on network events like NET\_EV...

**Definition** net\_event.h:512

[net\_event\_ipv6\_route::addr](structnet__event__ipv6__route.md#a42bb70c6b92841e5a77c80a3a193178c)

struct in6\_addr addr

IPv6 address or prefix of the route.

**Definition** net\_event.h:516

[net\_event\_ipv6\_route::prefix\_len](structnet__event__ipv6__route.md#aa1f21f6963befb3f94183d02c6d2d23f)

uint8\_t prefix\_len

IPv6 prefix length.

**Definition** net\_event.h:518

[net\_event\_ipv6\_route::nexthop](structnet__event__ipv6__route.md#ad8772d7949fa8b7e7217324acbda6829)

struct in6\_addr nexthop

IPv6 address of the next hop.

**Definition** net\_event.h:514

[net\_event\_l4\_hostname](structnet__event__l4__hostname.md)

Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED...

**Definition** net\_event.h:544

[net\_event\_l4\_hostname::hostname](structnet__event__l4__hostname.md#a8e04c33dfb1c251a0deaa29081283245)

char hostname[NET\_HOSTNAME\_SIZE]

New hostname.

**Definition** net\_event.h:546

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_event.h](net__event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
