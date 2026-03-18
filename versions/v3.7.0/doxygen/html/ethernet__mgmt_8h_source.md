---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ethernet__mgmt_8h_source.html
original_path: doxygen/html/ethernet__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_mgmt.h

[Go to the documentation of this file.](ethernet__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_ETHERNET\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_ETHERNET\_MGMT\_H\_

14

15#include <[zephyr/net/ethernet.h](ethernet_8h.md)>

16#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

30

31#define \_NET\_ETHERNET\_LAYER NET\_MGMT\_LAYER\_L2

32#define \_NET\_ETHERNET\_CODE 0x208

33#define \_NET\_ETHERNET\_BASE (NET\_MGMT\_IFACE\_BIT | \

34 NET\_MGMT\_LAYER(\_NET\_ETHERNET\_LAYER) | \

35 NET\_MGMT\_LAYER\_CODE(\_NET\_ETHERNET\_CODE))

36#define \_NET\_ETHERNET\_EVENT (\_NET\_ETHERNET\_BASE | NET\_MGMT\_EVENT\_BIT)

37

38enum net\_request\_ethernet\_cmd {

39 NET\_REQUEST\_ETHERNET\_CMD\_SET\_AUTO\_NEGOTIATION = 1,

40 NET\_REQUEST\_ETHERNET\_CMD\_SET\_LINK,

41 NET\_REQUEST\_ETHERNET\_CMD\_SET\_DUPLEX,

42 NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS,

43 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM,

44 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM,

45 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM,

46 NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM,

47 NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE,

48 NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM,

49 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM,

50 NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM,

51 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM,

52 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM,

53 NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM,

54 NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM,

55 NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE,

56 NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE,

57 NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_FILTER,

58};

59

60#define NET\_REQUEST\_ETHERNET\_SET\_AUTO\_NEGOTIATION \

61 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_AUTO\_NEGOTIATION)

62

63[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_AUTO\_NEGOTIATION);

64

65#define NET\_REQUEST\_ETHERNET\_SET\_LINK \

66 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_LINK)

67

68[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_LINK);

69

70#define NET\_REQUEST\_ETHERNET\_SET\_DUPLEX \

71 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_DUPLEX)

72

73[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_DUPLEX);

74

75#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS \

76 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS)

77

78[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS);

79

80#define NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM \

81 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM)

82

83[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM);

84

85#define NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM \

86 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM)

87

88[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM);

89

90#define NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM \

91 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM)

92

93[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM);

94

95#define NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM \

96 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM)

97

98[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM);

99

100#define NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM \

101 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM)

102

103[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM);

104

105#define NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE \

106 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE)

107

108[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE);

109

110#define NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM \

111 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM)

112

113[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM);

114

115#define NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM \

116 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM)

117

118[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM);

119

120#define NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM \

121 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM)

122

123[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM);

124

125#define NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM \

126 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM)

127

128[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM);

129

130#define NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM \

131 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM)

132

133[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM);

134

135#define NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM \

136 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM)

137

138[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM);

139

140#define NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE \

141 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE)

142

143[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE);

144

145#define NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE \

146 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE)

147

148[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE);

149

150#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_FILTER \

151 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_FILTER)

152

153[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_FILTER);

154

155struct [net\_eth\_addr](structnet__eth__addr.md);

156struct [ethernet\_qav\_param](structethernet__qav__param.md);

157struct [ethernet\_qbv\_param](structethernet__qbv__param.md);

158struct [ethernet\_qbu\_param](structethernet__qbu__param.md);

159struct [ethernet\_txtime\_param](structethernet__txtime__param.md);

160

161struct ethernet\_req\_params {

162 union {

163 bool auto\_negotiation;

164 bool full\_duplex;

165 bool promisc\_mode;

166 bool txinjection\_mode;

167

168 struct {

169 bool link\_10bt;

170 bool link\_100bt;

171 bool link\_1000bt;

172 } l;

173

174 struct net\_eth\_addr mac\_address;

175

176 struct ethernet\_qav\_param qav\_param;

177 struct ethernet\_qbv\_param qbv\_param;

178 struct ethernet\_qbu\_param qbu\_param;

179 struct ethernet\_txtime\_param txtime\_param;

180 struct ethernet\_t1s\_param t1s\_param;

181

182 struct ethernet\_filter filter;

183

184 int priority\_queues\_num;

185 int ports\_num;

186 };

187};

188

189enum net\_event\_ethernet\_cmd {

190 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON = 1,

191 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF,

192 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED,

193 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED,

194};

195

196#define NET\_EVENT\_ETHERNET\_CARRIER\_ON \

197 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON)

198

199#define NET\_EVENT\_ETHERNET\_CARRIER\_OFF \

200 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF)

201

202#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_ENABLED \

203 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED)

204

205#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_DISABLED \

206 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED)

207

208struct [net\_if](structnet__if.md);

209

211

217#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 218](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface);

219#else

220static inline void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface)

221{

222 ARG\_UNUSED(iface);

223}

224#endif

225

231#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 232](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface);

233#else

234static inline void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface)

235{

236 ARG\_UNUSED(iface);

237}

238#endif

239

246#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 247](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

248#else

249static inline void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface,

250 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

251{

252 ARG\_UNUSED(iface);

253 ARG\_UNUSED(tag);

254}

255#endif

256

263#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 264](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

265 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

266#else

267static inline void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

268 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

269{

270 ARG\_UNUSED(iface);

271 ARG\_UNUSED(tag);

272}

273#endif

274

278

279#ifdef \_\_cplusplus

280}

281#endif

282

283#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_MGMT\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)

void ethernet\_mgmt\_raise\_carrier\_off\_event(struct net\_if \*iface)

Raise CARRIER\_OFF event when Ethernet is disconnected.

[ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)

void ethernet\_mgmt\_raise\_carrier\_on\_event(struct net\_if \*iface)

Raise CARRIER\_ON event when Ethernet is connected.

[ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)

void ethernet\_mgmt\_raise\_vlan\_disabled\_event(struct net\_if \*iface, uint16\_t tag)

Raise VLAN\_DISABLED event when VLAN is disabled.

[ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)

void ethernet\_mgmt\_raise\_vlan\_enabled\_event(struct net\_if \*iface, uint16\_t tag)

Raise VLAN\_ENABLED event when VLAN is enabled.

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:109

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ethernet\_qav\_param](structethernet__qav__param.md)

Ethernet Qav specific parameters.

**Definition** ethernet.h:288

[ethernet\_qbu\_param](structethernet__qbu__param.md)

Ethernet Qbu specific parameters.

**Definition** ethernet.h:397

[ethernet\_qbv\_param](structethernet__qbv__param.md)

Ethernet Qbv specific parameters.

**Definition** ethernet.h:330

[ethernet\_txtime\_param](structethernet__txtime__param.md)

Ethernet TXTIME specific parameters.

**Definition** ethernet.h:464

[net\_eth\_addr](structnet__eth__addr.md)

Ethernet address.

**Definition** ethernet.h:51

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_mgmt.h](ethernet__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
