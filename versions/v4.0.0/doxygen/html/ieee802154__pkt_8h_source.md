---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ieee802154__pkt_8h_source.html
original_path: doxygen/html/ieee802154__pkt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

62 struct {

63#if defined(CONFIG\_IEEE802154\_SELECTIVE\_TXCHANNEL)

64 /\* The channel used for timed transmissions.

65 \*

66 \* Please refer to `ieee802154\_radio\_api::tx` documentation for

67 \* details.

68 \*/

69 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) txchannel;

70#endif /\* CONFIG\_IEEE802154\_SELECTIVE\_TXCHANNEL \*/

71 };

72 };

73

74 /\* Flags \*/

75 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack\_fpb : 1; /\* Frame Pending Bit was set in the ACK \*/

76 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_secured : 1; /\* Frame is authenticated and

77 \* encrypted according to its

78 \* Auxiliary Security Header

79 \*/

80 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mac\_hdr\_rdy : 1; /\* Indicates if frame's MAC header

81 \* is ready to be transmitted or if

82 \* it requires further modifications,

83 \* e.g. Frame Counter injection.

84 \*/

85#if defined(CONFIG\_NET\_L2\_OPENTHREAD)

86 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ack\_seb : 1; /\* Security Enabled Bit was set in the ACK \*/

87#endif

88};

89

90struct [net\_pkt](structnet__pkt.md);

91static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt);

92

93static inline struct net\_pkt\_cb\_ieee802154 \*net\_pkt\_cb\_ieee802154(struct [net\_pkt](structnet__pkt.md) \*pkt)

94{

95 return (struct net\_pkt\_cb\_ieee802154 \*)net\_pkt\_cb(pkt);

96};

97

98static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_lqi(struct [net\_pkt](structnet__pkt.md) \*pkt)

99{

100 return net\_pkt\_cb\_ieee802154(pkt)->lqi;

101}

102

103static inline void net\_pkt\_set\_ieee802154\_lqi(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lqi)

104{

105 net\_pkt\_cb\_ieee802154(pkt)->lqi = lqi;

106}

107

120static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_rssi(struct [net\_pkt](structnet__pkt.md) \*pkt)

121{

122 return net\_pkt\_cb\_ieee802154(pkt)->rssi;

123}

124

137static inline void net\_pkt\_set\_ieee802154\_rssi(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rssi)

138{

139 net\_pkt\_cb\_ieee802154(pkt)->rssi = rssi;

140}

141

153static inline [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) net\_pkt\_ieee802154\_rssi\_dbm(struct [net\_pkt](structnet__pkt.md) \*pkt)

154{

155 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi = net\_pkt\_cb\_ieee802154(pkt)->rssi;

156 return rssi == IEEE802154\_MAC\_RSSI\_UNDEFINED ? IEEE802154\_MAC\_RSSI\_DBM\_UNDEFINED

157 : rssi + IEEE802154\_MAC\_RSSI\_DBM\_MIN;

158}

159

171static inline void net\_pkt\_set\_ieee802154\_rssi\_dbm(struct [net\_pkt](structnet__pkt.md) \*pkt, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi)

172{

173 if (likely(rssi >= IEEE802154\_MAC\_RSSI\_DBM\_MIN && rssi <= IEEE802154\_MAC\_RSSI\_DBM\_MAX)) {

174 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) unsigned\_rssi = rssi - IEEE802154\_MAC\_RSSI\_DBM\_MIN;

175

176 net\_pkt\_cb\_ieee802154(pkt)->rssi = unsigned\_rssi;

177 return;

178 } else if (rssi == IEEE802154\_MAC\_RSSI\_DBM\_UNDEFINED) {

179 net\_pkt\_cb\_ieee802154(pkt)->rssi = IEEE802154\_MAC\_RSSI\_UNDEFINED;

180 return;

181 } else if (rssi < IEEE802154\_MAC\_RSSI\_DBM\_MIN) {

182 net\_pkt\_cb\_ieee802154(pkt)->rssi = IEEE802154\_MAC\_RSSI\_MIN;

183 return;

184 } else if (rssi > IEEE802154\_MAC\_RSSI\_DBM\_MAX) {

185 net\_pkt\_cb\_ieee802154(pkt)->rssi = IEEE802154\_MAC\_RSSI\_MAX;

186 return;

187 }

188

189 CODE\_UNREACHABLE;

190}

191

192#if defined(CONFIG\_IEEE802154\_SELECTIVE\_TXCHANNEL)

193static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_txchannel(struct [net\_pkt](structnet__pkt.md) \*pkt)

194{

195 return net\_pkt\_cb\_ieee802154(pkt)->txchannel;

196}

197

198static inline void net\_pkt\_set\_ieee802154\_txchannel(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel)

199{

200 net\_pkt\_cb\_ieee802154(pkt)->txchannel = channel;

201}

202#endif /\* CONFIG\_IEEE802154\_SELECTIVE\_TXCHANNEL \*/

203

204static inline bool net\_pkt\_ieee802154\_ack\_fpb(struct [net\_pkt](structnet__pkt.md) \*pkt)

205{

206 return net\_pkt\_cb\_ieee802154(pkt)->ack\_fpb;

207}

208

209static inline void net\_pkt\_set\_ieee802154\_ack\_fpb(struct [net\_pkt](structnet__pkt.md) \*pkt, bool fpb)

210{

211 net\_pkt\_cb\_ieee802154(pkt)->ack\_fpb = fpb;

212}

213

214static inline bool net\_pkt\_ieee802154\_frame\_secured(struct [net\_pkt](structnet__pkt.md) \*pkt)

215{

216 return net\_pkt\_cb\_ieee802154(pkt)->frame\_secured;

217}

218

219static inline void net\_pkt\_set\_ieee802154\_frame\_secured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool secured)

220{

221 net\_pkt\_cb\_ieee802154(pkt)->frame\_secured = secured;

222}

223

224static inline bool net\_pkt\_ieee802154\_mac\_hdr\_rdy(struct [net\_pkt](structnet__pkt.md) \*pkt)

225{

226 return net\_pkt\_cb\_ieee802154(pkt)->mac\_hdr\_rdy;

227}

228

229static inline void net\_pkt\_set\_ieee802154\_mac\_hdr\_rdy(struct [net\_pkt](structnet__pkt.md) \*pkt, bool rdy)

230{

231 net\_pkt\_cb\_ieee802154(pkt)->mac\_hdr\_rdy = rdy;

232}

233

234#if defined(CONFIG\_NET\_L2\_OPENTHREAD)

235static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ieee802154\_ack\_fc(struct [net\_pkt](structnet__pkt.md) \*pkt)

236{

237 return net\_pkt\_cb\_ieee802154(pkt)->ack\_fc;

238}

239

240static inline void net\_pkt\_set\_ieee802154\_ack\_fc(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fc)

241{

242 net\_pkt\_cb\_ieee802154(pkt)->ack\_fc = fc;

243}

244

245static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ieee802154\_ack\_keyid(struct [net\_pkt](structnet__pkt.md) \*pkt)

246{

247 return net\_pkt\_cb\_ieee802154(pkt)->ack\_keyid;

248}

249

250static inline void net\_pkt\_set\_ieee802154\_ack\_keyid(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) keyid)

251{

252 net\_pkt\_cb\_ieee802154(pkt)->ack\_keyid = keyid;

253}

254

255static inline bool net\_pkt\_ieee802154\_ack\_seb(struct [net\_pkt](structnet__pkt.md) \*pkt)

256{

257 return net\_pkt\_cb\_ieee802154(pkt)->ack\_seb;

258}

259

260static inline void net\_pkt\_set\_ieee802154\_ack\_seb(struct [net\_pkt](structnet__pkt.md) \*pkt, bool seb)

261{

262 net\_pkt\_cb\_ieee802154(pkt)->ack\_seb = seb;

263}

264#endif /\* CONFIG\_NET\_L2\_OPENTHREAD \*/

265

267

268#ifdef \_\_cplusplus

269}

270#endif

271

272#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_PKT\_H\_ \*/

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

**Definition** net\_pkt.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_pkt.h](ieee802154__pkt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
