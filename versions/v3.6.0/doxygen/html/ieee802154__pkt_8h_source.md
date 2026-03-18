---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ieee802154__pkt_8h_source.html
original_path: doxygen/html/ieee802154__pkt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_pkt.h

[Go to the documentation of this file.](ieee802154__pkt_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \* Copyright (c) 2022 Florian Grandel.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_NET\_IEEE802154\_PKT\_H\_

16#define ZEPHYR\_INCLUDE\_NET\_IEEE802154\_PKT\_H\_

17

18#include <[string.h](string_8h.md)>

19

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

27

28#ifndef NET\_PKT\_HAS\_CONTROL\_BLOCK

29#define NET\_PKT\_HAS\_CONTROL\_BLOCK

30#endif

31

32/\* See section 6.16.2.8 - Received Signal Strength Indicator (RSSI) \*/

33#define IEEE802154\_MAC\_RSSI\_MIN 0U /\* corresponds to -174 dBm \*/

34#define IEEE802154\_MAC\_RSSI\_MAX 254U /\* corresponds to 80 dBm \*/

35#define IEEE802154\_MAC\_RSSI\_UNDEFINED 255U /\* used by us to indicate an undefined RSSI value \*/

36

37#define IEEE802154\_MAC\_RSSI\_DBM\_MIN -174 /\* in dBm \*/

38#define IEEE802154\_MAC\_RSSI\_DBM\_MAX 80 /\* in dBm \*/

39#define IEEE802154\_MAC\_RSSI\_DBM\_UNDEFINED INT16\_MIN /\* represents an undefined RSSI value \*/

40

41struct net\_pkt\_cb\_ieee802154 {

42#if defined(CONFIG\_NET\_L2\_OPENTHREAD)

43 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ack\_fc; /\* Frame counter set in the ACK \*/

44 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack\_keyid; /\* Key index set in the ACK \*/

45#endif

46 union {

47 /\* RX packets \*/

48 struct {

49 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lqi; /\* Link Quality Indicator \*/

50 /\* See section 6.16.2.8 - Received Signal Strength Indicator (RSSI)

51 \* "RSSI is represented as one octet of integer [...]; therefore,

52 \* the minimum and maximum values are 0 (–174 dBm) and 254 (80 dBm),

53 \* respectively. 255 is reserved." (MAC PIB attribute macRssi, see

54 \* section 8.4.3.10, table 8-108)

55 \*

56 \* TX packets will show zero for this value. Drivers may set the

57 \* field to the reserved value 255 (0xff) to indicate that an RSSI

58 \* value is not available for this packet.

59 \*/

60 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rssi;

61 };

62 };

63

64 /\* Flags \*/

65 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack\_fpb : 1; /\* Frame Pending Bit was set in the ACK \*/

66 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_secured : 1; /\* Frame is authenticated and

67 \* encrypted according to its

68 \* Auxiliary Security Header

69 \*/

70 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mac\_hdr\_rdy : 1; /\* Indicates if frame's MAC header

71 \* is ready to be transmitted or if

72 \* it requires further modifications,

73 \* e.g. Frame Counter injection.

74 \*/

75#if defined(CONFIG\_NET\_L2\_OPENTHREAD)

76 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack\_seb : 1; /\* Security Enabled Bit was set in the ACK \*/

77#endif

78};

79

80struct [net\_pkt](structnet__pkt.md);

81static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt);

82

83static inline struct net\_pkt\_cb\_ieee802154 \*net\_pkt\_cb\_ieee802154(struct [net\_pkt](structnet__pkt.md) \*pkt)

84{

85 return (struct net\_pkt\_cb\_ieee802154 \*)net\_pkt\_cb(pkt);

86};

87

88static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_lqi(struct [net\_pkt](structnet__pkt.md) \*pkt)

89{

90 return net\_pkt\_cb\_ieee802154(pkt)->lqi;

91}

92

93static inline void net\_pkt\_set\_ieee802154\_lqi(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lqi)

94{

95 net\_pkt\_cb\_ieee802154(pkt)->lqi = lqi;

96}

97

110static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_rssi(struct [net\_pkt](structnet__pkt.md) \*pkt)

111{

112 return net\_pkt\_cb\_ieee802154(pkt)->rssi;

113}

114

127static inline void net\_pkt\_set\_ieee802154\_rssi(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rssi)

128{

129 net\_pkt\_cb\_ieee802154(pkt)->rssi = rssi;

130}

131

143static inline [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) net\_pkt\_ieee802154\_rssi\_dbm(struct [net\_pkt](structnet__pkt.md) \*pkt)

144{

145 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi = net\_pkt\_cb\_ieee802154(pkt)->rssi;

146 return rssi == IEEE802154\_MAC\_RSSI\_UNDEFINED ? IEEE802154\_MAC\_RSSI\_DBM\_UNDEFINED

147 : rssi + IEEE802154\_MAC\_RSSI\_DBM\_MIN;

148}

149

161static inline void net\_pkt\_set\_ieee802154\_rssi\_dbm(struct [net\_pkt](structnet__pkt.md) \*pkt, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi)

162{

163 if (likely(rssi >= IEEE802154\_MAC\_RSSI\_DBM\_MIN && rssi <= IEEE802154\_MAC\_RSSI\_DBM\_MAX)) {

164 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) unsigned\_rssi = rssi - IEEE802154\_MAC\_RSSI\_DBM\_MIN;

165

166 net\_pkt\_cb\_ieee802154(pkt)->rssi = unsigned\_rssi;

167 return;

168 } else if (rssi == IEEE802154\_MAC\_RSSI\_DBM\_UNDEFINED) {

169 net\_pkt\_cb\_ieee802154(pkt)->rssi = IEEE802154\_MAC\_RSSI\_UNDEFINED;

170 return;

171 } else if (rssi < IEEE802154\_MAC\_RSSI\_DBM\_MIN) {

172 net\_pkt\_cb\_ieee802154(pkt)->rssi = IEEE802154\_MAC\_RSSI\_MIN;

173 return;

174 } else if (rssi > IEEE802154\_MAC\_RSSI\_DBM\_MAX) {

175 net\_pkt\_cb\_ieee802154(pkt)->rssi = IEEE802154\_MAC\_RSSI\_MAX;

176 return;

177 }

178

179 CODE\_UNREACHABLE;

180}

181

182static inline bool net\_pkt\_ieee802154\_ack\_fpb(struct [net\_pkt](structnet__pkt.md) \*pkt)

183{

184 return net\_pkt\_cb\_ieee802154(pkt)->ack\_fpb;

185}

186

187static inline void net\_pkt\_set\_ieee802154\_ack\_fpb(struct [net\_pkt](structnet__pkt.md) \*pkt, bool fpb)

188{

189 net\_pkt\_cb\_ieee802154(pkt)->ack\_fpb = fpb;

190}

191

192static inline bool net\_pkt\_ieee802154\_frame\_secured(struct [net\_pkt](structnet__pkt.md) \*pkt)

193{

194 return net\_pkt\_cb\_ieee802154(pkt)->frame\_secured;

195}

196

197static inline void net\_pkt\_set\_ieee802154\_frame\_secured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool secured)

198{

199 net\_pkt\_cb\_ieee802154(pkt)->frame\_secured = secured;

200}

201

202static inline bool net\_pkt\_ieee802154\_mac\_hdr\_rdy(struct [net\_pkt](structnet__pkt.md) \*pkt)

203{

204 return net\_pkt\_cb\_ieee802154(pkt)->mac\_hdr\_rdy;

205}

206

207static inline void net\_pkt\_set\_ieee802154\_mac\_hdr\_rdy(struct [net\_pkt](structnet__pkt.md) \*pkt, bool rdy)

208{

209 net\_pkt\_cb\_ieee802154(pkt)->mac\_hdr\_rdy = rdy;

210}

211

212#if defined(CONFIG\_NET\_L2\_OPENTHREAD)

213static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ieee802154\_ack\_fc(struct [net\_pkt](structnet__pkt.md) \*pkt)

214{

215 return net\_pkt\_cb\_ieee802154(pkt)->ack\_fc;

216}

217

218static inline void net\_pkt\_set\_ieee802154\_ack\_fc(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fc)

219{

220 net\_pkt\_cb\_ieee802154(pkt)->ack\_fc = fc;

221}

222

223static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_ack\_keyid(struct [net\_pkt](structnet__pkt.md) \*pkt)

224{

225 return net\_pkt\_cb\_ieee802154(pkt)->ack\_keyid;

226}

227

228static inline void net\_pkt\_set\_ieee802154\_ack\_keyid(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) keyid)

229{

230 net\_pkt\_cb\_ieee802154(pkt)->ack\_keyid = keyid;

231}

232

233static inline bool net\_pkt\_ieee802154\_ack\_seb(struct [net\_pkt](structnet__pkt.md) \*pkt)

234{

235 return net\_pkt\_cb\_ieee802154(pkt)->ack\_seb;

236}

237

238static inline void net\_pkt\_set\_ieee802154\_ack\_seb(struct [net\_pkt](structnet__pkt.md) \*pkt, bool seb)

239{

240 net\_pkt\_cb\_ieee802154(pkt)->ack\_seb = seb;

241}

242#endif /\* CONFIG\_NET\_L2\_OPENTHREAD \*/

243

245

246#ifdef \_\_cplusplus

247}

248#endif

249

250#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_PKT\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[string.h](string_8h.md)

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_pkt.h](ieee802154__pkt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
