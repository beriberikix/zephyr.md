---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ethernet__mgmt_8h_source.html
original_path: doxygen/html/ethernet__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

57};

58

59#define NET\_REQUEST\_ETHERNET\_SET\_AUTO\_NEGOTIATION \

60 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_AUTO\_NEGOTIATION)

61

62[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_AUTO\_NEGOTIATION);

63

64#define NET\_REQUEST\_ETHERNET\_SET\_LINK \

65 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_LINK)

66

67[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_LINK);

68

69#define NET\_REQUEST\_ETHERNET\_SET\_DUPLEX \

70 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_DUPLEX)

71

72[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_DUPLEX);

73

74#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS \

75 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS)

76

77[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS);

78

79#define NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM \

80 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM)

81

82[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM);

83

84#define NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM \

85 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM)

86

87[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM);

88

89#define NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM \

90 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM)

91

92[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM);

93

94#define NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM \

95 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM)

96

97[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM);

98

99#define NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM \

100 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM)

101

102[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM);

103

104#define NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE \

105 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE)

106

107[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE);

108

109#define NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM \

110 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM)

111

112[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM);

113

114#define NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM \

115 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM)

116

117[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM);

118

119#define NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM \

120 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM)

121

122[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM);

123

124#define NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM \

125 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM)

126

127[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM);

128

129#define NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM \

130 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM)

131

132[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM);

133

134#define NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM \

135 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM)

136

137[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM);

138

139#define NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE \

140 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE)

141

142[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE);

143

144#define NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE \

145 (\_NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE)

146

147[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE);

148

149struct net\_eth\_addr;

150struct [ethernet\_qav\_param](structethernet__qav__param.md);

151struct [ethernet\_qbv\_param](structethernet__qbv__param.md);

152struct [ethernet\_qbu\_param](structethernet__qbu__param.md);

153struct [ethernet\_txtime\_param](structethernet__txtime__param.md);

154

155struct ethernet\_req\_params {

156 union {

157 bool auto\_negotiation;

158 bool full\_duplex;

159 bool promisc\_mode;

160 bool txinjection\_mode;

161

162 struct {

163 bool link\_10bt;

164 bool link\_100bt;

165 bool link\_1000bt;

166 } l;

167

168 struct net\_eth\_addr mac\_address;

169

170 struct ethernet\_qav\_param qav\_param;

171 struct ethernet\_qbv\_param qbv\_param;

172 struct ethernet\_qbu\_param qbu\_param;

173 struct ethernet\_txtime\_param txtime\_param;

174 struct ethernet\_t1s\_param t1s\_param;

175

176 int priority\_queues\_num;

177 int ports\_num;

178 };

179};

180

181enum net\_event\_ethernet\_cmd {

182 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON = 1,

183 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF,

184 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED,

185 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED,

186};

187

188#define NET\_EVENT\_ETHERNET\_CARRIER\_ON \

189 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON)

190

191#define NET\_EVENT\_ETHERNET\_CARRIER\_OFF \

192 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF)

193

194#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_ENABLED \

195 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED)

196

197#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_DISABLED \

198 (\_NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED)

199

200struct [net\_if](structnet__if.md);

201

203

209#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 210](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface);

211#else

212static inline void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface)

213{

214 ARG\_UNUSED(iface);

215}

216#endif

217

223#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 224](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface);

225#else

226static inline void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface)

227{

228 ARG\_UNUSED(iface);

229}

230#endif

231

238#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 239](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

240#else

241static inline void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface,

242 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

243{

244 ARG\_UNUSED(iface);

245 ARG\_UNUSED(tag);

246}

247#endif

248

255#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 256](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

257 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

258#else

259static inline void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

260 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

261{

262 ARG\_UNUSED(iface);

263 ARG\_UNUSED(tag);

264}

265#endif

266

270

271#ifdef \_\_cplusplus

272}

273#endif

274

275#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_MGMT\_H\_ \*/

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

**Definition** net\_mgmt.h:96

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ethernet\_qav\_param](structethernet__qav__param.md)

**Definition** ethernet.h:262

[ethernet\_qbu\_param](structethernet__qbu__param.md)

**Definition** ethernet.h:367

[ethernet\_qbv\_param](structethernet__qbv__param.md)

**Definition** ethernet.h:303

[ethernet\_txtime\_param](structethernet__txtime__param.md)

**Definition** ethernet.h:434

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_mgmt.h](ethernet__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
