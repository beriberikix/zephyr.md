---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ethernet__mgmt_8h_source.html
original_path: doxygen/html/ethernet__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

33#define NET\_ETHERNET\_LAYER NET\_MGMT\_LAYER\_L2

34#define NET\_ETHERNET\_CODE NET\_MGMT\_LAYER\_CODE\_ETHERNET

35#define NET\_ETHERNET\_BASE (NET\_MGMT\_IFACE\_BIT | \

36 NET\_MGMT\_LAYER(NET\_ETHERNET\_LAYER) | \

37 NET\_MGMT\_LAYER\_CODE(NET\_ETHERNET\_CODE))

38#define NET\_ETHERNET\_EVENT (NET\_ETHERNET\_BASE | NET\_MGMT\_EVENT\_BIT)

39

40enum net\_request\_ethernet\_cmd {

41 NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS = 1,

42 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM,

43 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM,

44 NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM,

45 NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM,

46 NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE,

47 NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM,

48 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM,

49 NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM,

50 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM,

51 NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM,

52 NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM,

53 NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM,

54 NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE,

55 NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE,

56 NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_FILTER,

57};

58

59#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS \

60 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_ADDRESS)

61

62[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_ADDRESS);

63

64#define NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM \

65 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QAV\_PARAM)

66

67[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QAV\_PARAM);

68

69#define NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM \

70 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PORTS\_NUM)

71

72[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PORTS\_NUM);

73

74#define NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM \

75 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBV\_PARAM)

76

77[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBV\_PARAM);

78

79#define NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM \

80 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_QBU\_PARAM)

81

82[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_QBU\_PARAM);

83

84#define NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM \

85 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXTIME\_PARAM)

86

87[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXTIME\_PARAM);

88

89#define NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE \

90 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_PROMISC\_MODE)

91

92[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_PROMISC\_MODE);

93

94#define NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM \

95 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_PRIORITY\_QUEUES\_NUM)

96

97[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_PRIORITY\_QUEUES\_NUM);

98

99#define NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM \

100 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QAV\_PARAM)

101

102[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QAV\_PARAM);

103

104#define NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM \

105 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBV\_PARAM)

106

107[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBV\_PARAM);

108

109#define NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM \

110 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_QBU\_PARAM)

111

112[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_QBU\_PARAM);

113

114#define NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM \

115 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXTIME\_PARAM)

116

117[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXTIME\_PARAM);

118

119#define NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM \

120 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_T1S\_PARAM)

121

122[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_T1S\_PARAM);

123

124#define NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE \

125 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_TXINJECTION\_MODE)

126

127[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_TXINJECTION\_MODE);

128

129#define NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE \

130 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_GET\_TXINJECTION\_MODE)

131

132[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_GET\_TXINJECTION\_MODE);

133

134#define NET\_REQUEST\_ETHERNET\_SET\_MAC\_FILTER \

135 (NET\_ETHERNET\_BASE | NET\_REQUEST\_ETHERNET\_CMD\_SET\_MAC\_FILTER)

136

137[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(NET\_REQUEST\_ETHERNET\_SET\_MAC\_FILTER);

138

139struct [net\_eth\_addr](structnet__eth__addr.md);

140struct [ethernet\_qav\_param](structethernet__qav__param.md);

141struct [ethernet\_qbv\_param](structethernet__qbv__param.md);

142struct [ethernet\_qbu\_param](structethernet__qbu__param.md);

143struct [ethernet\_txtime\_param](structethernet__txtime__param.md);

144

145struct ethernet\_req\_params {

146 union {

147 bool promisc\_mode;

148 bool txinjection\_mode;

149

150 struct net\_eth\_addr mac\_address;

151

152 struct ethernet\_qav\_param qav\_param;

153 struct ethernet\_qbv\_param qbv\_param;

154 struct ethernet\_qbu\_param qbu\_param;

155 struct ethernet\_txtime\_param txtime\_param;

156 struct ethernet\_t1s\_param t1s\_param;

157

158 struct ethernet\_filter filter;

159

160 int priority\_queues\_num;

161 int ports\_num;

162 };

163};

164

165enum {

166 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON\_VAL,

167 NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF\_VAL,

168 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED\_VAL,

169 NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED\_VAL,

170

171 NET\_EVENT\_ETHERNET\_CMD\_MAX

172};

173

174BUILD\_ASSERT(NET\_EVENT\_ETHERNET\_CMD\_MAX <= NET\_MGMT\_MAX\_COMMANDS,

175 "Number of events in net\_event\_ethernet\_cmd exceeds the limit");

176

177enum net\_event\_ethernet\_cmd {

178 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON),

179 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF),

180 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED),

181 [NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)(NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED),

182};

183

184#define NET\_EVENT\_ETHERNET\_CARRIER\_ON \

185 (NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_ON)

186

187#define NET\_EVENT\_ETHERNET\_CARRIER\_OFF \

188 (NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_CARRIER\_OFF)

189

190#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_ENABLED \

191 (NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_ENABLED)

192

193#define NET\_EVENT\_ETHERNET\_VLAN\_TAG\_DISABLED \

194 (NET\_ETHERNET\_EVENT | NET\_EVENT\_ETHERNET\_CMD\_VLAN\_TAG\_DISABLED)

195

196struct [net\_if](structnet__if.md);

197

199

205#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 206](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface);

207#else

208static inline void [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad)(struct [net\_if](structnet__if.md) \*iface)

209{

210 ARG\_UNUSED(iface);

211}

212#endif

213

219#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 220](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface);

221#else

222static inline void [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d)(struct [net\_if](structnet__if.md) \*iface)

223{

224 ARG\_UNUSED(iface);

225}

226#endif

227

234#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 235](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

236#else

237static inline void [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536)(struct [net\_if](structnet__if.md) \*iface,

238 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

239{

240 ARG\_UNUSED(iface);

241 ARG\_UNUSED(tag);

242}

243#endif

244

251#if defined(CONFIG\_NET\_L2\_ETHERNET\_MGMT)

[ 252](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

253 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag);

254#else

255static inline void [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f)(struct [net\_if](structnet__if.md) \*iface,

256 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

257{

258 ARG\_UNUSED(iface);

259 ARG\_UNUSED(tag);

260}

261#endif

262

266

267#ifdef \_\_cplusplus

268}

269#endif

270

271#endif /\* ZEPHYR\_INCLUDE\_NET\_ETHERNET\_MGMT\_H\_ \*/

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

**Definition** net\_mgmt.h:129

[NET\_MGMT\_CMD](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)

@ NET\_MGMT\_CMD

Scan results available.

**Definition** wifi\_mgmt.h:352

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ethernet\_qav\_param](structethernet__qav__param.md)

Ethernet Qav specific parameters.

**Definition** ethernet.h:286

[ethernet\_qbu\_param](structethernet__qbu__param.md)

Ethernet Qbu specific parameters.

**Definition** ethernet.h:395

[ethernet\_qbv\_param](structethernet__qbv__param.md)

Ethernet Qbv specific parameters.

**Definition** ethernet.h:328

[ethernet\_txtime\_param](structethernet__txtime__param.md)

Ethernet TXTIME specific parameters.

**Definition** ethernet.h:462

[net\_eth\_addr](structnet__eth__addr.md)

Ethernet address.

**Definition** ethernet.h:55

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_mgmt.h](ethernet__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
