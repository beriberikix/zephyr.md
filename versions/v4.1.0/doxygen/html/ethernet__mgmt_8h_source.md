---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ethernet__mgmt_8h_source.html
original_path: doxygen/html/ethernet__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

30

32

33#define \_NET\_ETHERNET\_LAYER NET\_MGMT\_LAYER\_L2

34#define \_NET\_ETHERNET\_CODE 0x208

35#define \_NET\_ETHERNET\_BASE (NET\_MGMT\_IFACE\_BIT | \

36 NET\_MGMT\_LAYER(\_NET\_ETHERNET\_LAYER) | \

37 NET\_MGMT\_LAYER\_CODE(\_NET\_ETHERNET\_CODE))

38#define \_NET\_ETHERNET\_EVENT (\_NET\_ETHERNET\_BASE | NET\_MGMT\_EVENT\_BIT)

39

40enum net\_request\_ethernet\_cmd {

41 NET\_REQUEST\_ETHERNET\_CMD\_SET\_AUTO\_NEGOTIATION = 1,

42 NET\_REQUEST\_ETHERNET\_CMD\_SET\_LINK,

43 NET\_REQUEST\_ETHERNET\_CMD\_SET\_DUPLEX,

44 NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS,

45 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM,

46 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM,

47 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM,

48 NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM,

49 NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE,

50 NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM,

51 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM,

52 NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM,

53 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM,

54 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM,

55 NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM,

56 NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM,

57 NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE,

58 NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE,

59 NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_FILTER,

60};

61

62#define NET\_REQUEST\_ETHERNET\_SET\_AUTO\_NEGOTIATION \

63 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_AUTO\_NEGOTIATION)

64

65[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_AUTO\_NEGOTIATION);

66

67#define NET\_REQUEST\_ETHERNET\_SET\_LINK \

68 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_LINK)

69

70[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_LINK);

71

72#define NET\_REQUEST\_ETHERNET\_SET\_DUPLEX \

73 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_DUPLEX)

74

75[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_DUPLEX);

76

77#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS \

78 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS)

79

80[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS);

81

82#define NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM \

83 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM)

84

85[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM);

86

87#define NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM \

88 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM)

89

90[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM);

91

92#define NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM \

93 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM)

94

95[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM);

96

97#define NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM \

98 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM)

99

100[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM);

101

102#define NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM \

103 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM)

104

105[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM);

106

107#define NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE \

108 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE)

109

110[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE);

111

112#define NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM \

113 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM)

114

115[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM);

116

117#define NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM \

118 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM)

119

120[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM);

121

122#define NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM \

123 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM)

124

125[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM);

126

127#define NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM \

128 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM)

129

130[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM);

131

132#define NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM \

133 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM)

134

135[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM);

136

137#define NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM \

138 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM)

139

140[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM);

141

142#define NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE \

143 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE)

144

145[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE);

146

147#define NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE \

148 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE)

149

150[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE);

151

152#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_FILTER \

153 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_FILTER)

154

155[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_FILTER);

156

157struct [net\_eth\_addr](structnet__eth__addr.md);

158struct [ethernet\_qav\_param](structethernet__qav__param.md);

159struct [ethernet\_qbv\_param](structethernet__qbv__param.md);

160struct [ethernet\_qbu\_param](structethernet__qbu__param.md);

161struct [ethernet\_txtime\_param](structethernet__txtime__param.md);

162

163struct ethernet\_req\_params {

164 union {

165 bool auto\_negotiation;

166 bool full\_duplex;

167 bool promisc\_mode;

168 bool txinjection\_mode;

169

170 struct {

171 bool link\_10bt;

172 bool link\_100bt;

173 bool link\_1000bt;

174 } l;

175

176 struct net\_eth\_addr mac\_address;

177

178 struct ethernet\_qav\_param qav\_param;

179 struct ethernet\_qbv\_param qbv\_param;

180 struct ethernet\_qbu\_param qbu\_param;

181 struct ethernet\_txtime\_param txtime\_param;

182 struct ethernet\_t1s\_param t1s\_param;

183

184 struct ethernet\_filter filter;

185

186 int priority\_queues\_num;

187 int ports\_num;

188 };

189};

190

191enum net\_event\_ethernet\_cmd {

192 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON = 1,

193 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF,

194 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED,

195 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED,

196};

197

198#define NET\_EVENT\_ETHERNET\_CARRIER\_ON \

199 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON)

200

201#define NET\_EVENT\_ETHERNET\_CARRIER\_OFF \

202 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF)

203

204#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_ENABLED \

205 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED)

206

207#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_DISABLED \

208 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED)

209

210struct [net\_if](structnet__if.md);

211

213

219#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 220](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface);

221#else

222static inline void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface)

223{

224 ARG\_UNUSED(iface);

225}

226#endif

227

233#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 234](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface);

235#else

236static inline void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface)

237{

238 ARG\_UNUSED(iface);

239}

240#endif

241

248#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 249](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

250#else

251static inline void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface,

252 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

253{

254 ARG\_UNUSED(iface);

255 ARG\_UNUSED(tag);

256}

257#endif

258

265#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 266](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

267 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

268#else

269static inline void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

270 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

271{

272 ARG\_UNUSED(iface);

273 ARG\_UNUSED(tag);

274}

275#endif

276

280

281#ifdef \_\_cplusplus

282}

283#endif

284

285#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_MGMT\_H\_ \*/

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

**Definition** net\_mgmt.h:111

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ethernet\_qav\_param](structethernet__qav__param.md)

Ethernet Qav specific parameters.

**Definition** ethernet.h:301

[ethernet\_qbu\_param](structethernet__qbu__param.md)

Ethernet Qbu specific parameters.

**Definition** ethernet.h:410

[ethernet\_qbv\_param](structethernet__qbv__param.md)

Ethernet Qbv specific parameters.

**Definition** ethernet.h:343

[ethernet\_txtime\_param](structethernet__txtime__param.md)

Ethernet TXTIME specific parameters.

**Definition** ethernet.h:477

[net\_eth\_addr](structnet__eth__addr.md)

Ethernet address.

**Definition** ethernet.h:53

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_mgmt.h](ethernet__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
