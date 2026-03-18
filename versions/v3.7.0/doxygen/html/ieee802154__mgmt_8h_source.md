---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ieee802154__mgmt_8h_source.html
original_path: doxygen/html/ieee802154__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_mgmt.h

[Go to the documentation of this file.](ieee802154__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_IEEE802154\_MGMT\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_IEEE802154\_MGMT\_H\_

16

17#include <[zephyr/net/ieee802154.h](ieee802154_8h.md)>

18#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

43

47

48#define \_NET\_IEEE802154\_LAYER NET\_MGMT\_LAYER\_L2

49#define \_NET\_IEEE802154\_CODE 0x154

50#define \_NET\_IEEE802154\_BASE (NET\_MGMT\_IFACE\_BIT | \

51 NET\_MGMT\_LAYER(\_NET\_IEEE802154\_LAYER) |\

52 NET\_MGMT\_LAYER\_CODE(\_NET\_IEEE802154\_CODE))

53#define \_NET\_IEEE802154\_EVENT (\_NET\_IEEE802154\_BASE | NET\_MGMT\_EVENT\_BIT)

54

55enum net\_request\_ieee802154\_cmd {

56 NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK = 1,

57 NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK,

58 NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN,

59 NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN,

60 NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN,

61 NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE,

62 NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE,

63 NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL,

64 NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL,

65 NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID,

66 NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID,

67 NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR,

68 NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR,

69 NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR,

70 NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR,

71 NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER,

72 NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER,

73 NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS,

74 NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS,

75};

76

80

109

[ 111](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da)#define NET\_REQUEST\_IEEE802154\_SET\_ACK (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK)

112

113[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_ACK](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da));

114

[ 116](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)#define NET\_REQUEST\_IEEE802154\_UNSET\_ACK \

117 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK)

118

119[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_UNSET\_ACK](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18));

120

[ 126](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9)#define NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN \

127 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN)

128

129[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9));

130

[ 136](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b)#define NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN \

137 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN)

138

139[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b));

140

[ 142](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe)#define NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN \

143 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN)

144

145[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe));

146

[ 148](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf)#define NET\_REQUEST\_IEEE802154\_ASSOCIATE \

149 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE)

150

151[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_ASSOCIATE](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf));

152

[ 154](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd)#define NET\_REQUEST\_IEEE802154\_DISASSOCIATE \

155 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE)

156

157[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_DISASSOCIATE](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd));

158

[ 160](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced)#define NET\_REQUEST\_IEEE802154\_SET\_CHANNEL \

161 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL)

162

163[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_CHANNEL](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced));

164

[ 166](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b)#define NET\_REQUEST\_IEEE802154\_GET\_CHANNEL \

167 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL)

168

169[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_CHANNEL](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b));

170

[ 172](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c)#define NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID \

173 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID)

174

175[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c));

176

[ 178](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f)#define NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID \

179 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID)

180

181[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f));

182

[ 187](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9)#define NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR \

188 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR)

189

190[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9));

191

[ 193](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66)#define NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR \

194 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR)

195

196[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66));

197

[ 199](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465)#define NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR \

200 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR)

201

202[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465));

203

[ 205](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241)#define NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR \

206 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR)

207

208[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241));

209

[ 214](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638)#define NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER \

215 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER)

216

217[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638));

218

[ 220](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4)#define NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER \

221 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER)

222

223[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4));

224

225#ifdef CONFIG\_NET\_L2\_IEEE802154\_SECURITY

226

[ 233](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654)#define NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS \

234 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS)

235

236[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654));

237

[ 243](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df)#define NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS \

244 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS)

245

246[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df));

247

248#endif /\* CONFIG\_NET\_L2\_IEEE802154\_SECURITY \*/

249

253

257

258enum net\_event\_ieee802154\_cmd {

259 NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT = 1,

260};

261

265

277

[ 284](group__ieee802154__mgmt.md#ga0442eaa04068a7b66f9b4ae40b570470)#define NET\_EVENT\_IEEE802154\_SCAN\_RESULT \

285 (\_NET\_IEEE802154\_EVENT | NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT)

286

290

294

295#define IEEE802154\_IS\_CHAN\_SCANNED(\_channel\_set, \_chan) \

296 (\_channel\_set & BIT(\_chan - 1))

297#define IEEE802154\_IS\_CHAN\_UNSCANNED(\_channel\_set, \_chan) \

298 (!IEEE802154\_IS\_CHAN\_SCANNED(\_channel\_set, \_chan))

299

300#define IEEE802154\_ALL\_CHANNELS UINT32\_MAX

301

305

[ 311](structieee802154__req__params.md)struct [ieee802154\_req\_params](structieee802154__req__params.md) {

[ 313](structieee802154__req__params.md#ad49071ae3c35a548f6894d32be017ad7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel\_set](structieee802154__req__params.md#ad49071ae3c35a548f6894d32be017ad7);

314

[ 316](structieee802154__req__params.md#a75b3e1658829dfa4970cef7267250c9b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duration](structieee802154__req__params.md#a75b3e1658829dfa4970cef7267250c9b);

317

[ 319](structieee802154__req__params.md#a78c9f6b62c7cfc51f514df09a2719441) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structieee802154__req__params.md#a78c9f6b62c7cfc51f514df09a2719441); /\* in CPU byte order \*/

[ 321](structieee802154__req__params.md#abde2cf05ea51cd0e024552aaf2414c86) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pan\_id](structieee802154__req__params.md#abde2cf05ea51cd0e024552aaf2414c86); /\* in CPU byte order \*/

322

324 union {

[ 325](structieee802154__req__params.md#a9cafc55c59dc4eff07bdf03e60da07ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [short\_addr](structieee802154__req__params.md#a9cafc55c59dc4eff07bdf03e60da07ec);

[ 326](structieee802154__req__params.md#aa1b2ea9ffb009a1b6255a9e57ddef9f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structieee802154__req__params.md#aa1b2ea9ffb009a1b6255a9e57ddef9f7)[[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)];

327 };

328

[ 330](structieee802154__req__params.md#a8c63caa3ae260f4c6f9bebe71677673b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structieee802154__req__params.md#a8c63caa3ae260f4c6f9bebe71677673b);

[ 332](structieee802154__req__params.md#af08c2fa32367340c54c8d8bf9c46f34a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lqi](structieee802154__req__params.md#af08c2fa32367340c54c8d8bf9c46f34a);

333};

334

[ 341](structieee802154__security__params.md)struct [ieee802154\_security\_params](structieee802154__security__params.md) {

[ 342](structieee802154__security__params.md#ae47ed5df4c70bfd4a28319d35f34c940) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structieee802154__security__params.md#ae47ed5df4c70bfd4a28319d35f34c940)[16];

[ 343](structieee802154__security__params.md#a03ba0953eaea5035346b35e0555beb9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_len](structieee802154__security__params.md#a03ba0953eaea5035346b35e0555beb9c);

[ 344](structieee802154__security__params.md#a5b6248a76d95ede67495f765d4d35b57) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_mode](structieee802154__security__params.md#a5b6248a76d95ede67495f765d4d35b57) : 2;

[ 345](structieee802154__security__params.md#a50b7b0cbb4151234747c41d41e6fd656) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structieee802154__security__params.md#a50b7b0cbb4151234747c41d41e6fd656) : 3;

348 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 3;

349};

350

351#ifdef \_\_cplusplus

352}

353#endif

354

358

359#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_MGMT\_H\_ \*/

[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)

#define IEEE802154\_MAX\_ADDR\_LENGTH

IEEE 802.15.4 maximum address length.

**Definition** ieee802154.h:147

[NET\_REQUEST\_IEEE802154\_ASSOCIATE](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf)

#define NET\_REQUEST\_IEEE802154\_ASSOCIATE

MLME-ASSOCIATE(...) request.

**Definition** ieee802154\_mgmt.h:148

[NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638)

#define NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER

MLME-SET(phyUnicastTxPower/phyBroadcastTxPower) request (currently not distinguished).

**Definition** ieee802154\_mgmt.h:214

[NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df)

#define NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS

Gets the configured sec\* attributes.

**Definition** ieee802154\_mgmt.h:243

[NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4)

#define NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER

MLME-GET(phyUnicastTxPower/phyBroadcastTxPower) request.

**Definition** ieee802154\_mgmt.h:220

[NET\_REQUEST\_IEEE802154\_SET\_CHANNEL](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced)

#define NET\_REQUEST\_IEEE802154\_SET\_CHANNEL

MLME-SET(phyCurrentChannel) request.

**Definition** ieee802154\_mgmt.h:160

[NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241)

#define NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR

MLME-GET(macShortAddress) request.

**Definition** ieee802154\_mgmt.h:205

[NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9)

#define NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN

MLME-SCAN(PASSIVE, ...) request.

**Definition** ieee802154\_mgmt.h:126

[NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f)

#define NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID

MLME-GET(macPanId) request.

**Definition** ieee802154\_mgmt.h:178

[NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654)

#define NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS

Configures basic sec\* MAC PIB attributes, implies macSecurityEnabled=true.

**Definition** ieee802154\_mgmt.h:233

[NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c)

#define NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID

MLME-SET(macPanId) request.

**Definition** ieee802154\_mgmt.h:172

[NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465)

#define NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR

MLME-SET(macShortAddress) request, only allowed for co-ordinators.

**Definition** ieee802154\_mgmt.h:199

[NET\_REQUEST\_IEEE802154\_SET\_ACK](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da)

#define NET\_REQUEST\_IEEE802154\_SET\_ACK

Sets AckTx for all subsequent MLME-DATA (aka TX) requests.

**Definition** ieee802154\_mgmt.h:111

[NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b)

#define NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN

MLME-SCAN(ACTIVE, ...) request.

**Definition** ieee802154\_mgmt.h:136

[NET\_REQUEST\_IEEE802154\_DISASSOCIATE](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd)

#define NET\_REQUEST\_IEEE802154\_DISASSOCIATE

MLME-DISASSOCIATE(...) request.

**Definition** ieee802154\_mgmt.h:154

[NET\_REQUEST\_IEEE802154\_GET\_CHANNEL](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b)

#define NET\_REQUEST\_IEEE802154\_GET\_CHANNEL

MLME-GET(phyCurrentChannel) request.

**Definition** ieee802154\_mgmt.h:166

[NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9)

#define NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR

Sets the extended interface address (non-standard), see sections 7.1 and 8.4.3.1, in big endian byte ...

**Definition** ieee802154\_mgmt.h:187

[NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe)

#define NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN

Cancels an ongoing MLME-SCAN(...) command (non-standard).

**Definition** ieee802154\_mgmt.h:142

[NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66)

#define NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR

like MLME-GET(macExtendedAddress) but in big endian byte order

**Definition** ieee802154\_mgmt.h:193

[NET\_REQUEST\_IEEE802154\_UNSET\_ACK](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)

#define NET\_REQUEST\_IEEE802154\_UNSET\_ACK

Unsets AckTx for all subsequent MLME-DATA requests.

**Definition** ieee802154\_mgmt.h:116

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

Declare a request handler function for the given network event.

**Definition** net\_mgmt.h:109

[ieee802154.h](ieee802154_8h.md)

IEEE 802.15.4 native L2 stack public header.

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

[ieee802154\_req\_params](structieee802154__req__params.md)

Scanning parameters.

**Definition** ieee802154\_mgmt.h:311

[ieee802154\_req\_params::duration](structieee802154__req__params.md#a75b3e1658829dfa4970cef7267250c9b)

uint32\_t duration

Duration of scan, per-channel, in milliseconds.

**Definition** ieee802154\_mgmt.h:316

[ieee802154\_req\_params::channel](structieee802154__req__params.md#a78c9f6b62c7cfc51f514df09a2719441)

uint16\_t channel

Current channel in use as a result.

**Definition** ieee802154\_mgmt.h:319

[ieee802154\_req\_params::len](structieee802154__req__params.md#a8c63caa3ae260f4c6f9bebe71677673b)

uint8\_t len

length of address

**Definition** ieee802154\_mgmt.h:330

[ieee802154\_req\_params::short\_addr](structieee802154__req__params.md#a9cafc55c59dc4eff07bdf03e60da07ec)

uint16\_t short\_addr

in CPU byte order

**Definition** ieee802154\_mgmt.h:325

[ieee802154\_req\_params::addr](structieee802154__req__params.md#aa1b2ea9ffb009a1b6255a9e57ddef9f7)

uint8\_t addr[8]

in big endian

**Definition** ieee802154\_mgmt.h:326

[ieee802154\_req\_params::pan\_id](structieee802154__req__params.md#abde2cf05ea51cd0e024552aaf2414c86)

uint16\_t pan\_id

Current pan\_id in use as a result.

**Definition** ieee802154\_mgmt.h:321

[ieee802154\_req\_params::channel\_set](structieee802154__req__params.md#ad49071ae3c35a548f6894d32be017ad7)

uint32\_t channel\_set

The set of channels to scan, use above macros to manage it.

**Definition** ieee802154\_mgmt.h:313

[ieee802154\_req\_params::lqi](structieee802154__req__params.md#af08c2fa32367340c54c8d8bf9c46f34a)

uint8\_t lqi

Link quality information, between 0 and 255.

**Definition** ieee802154\_mgmt.h:332

[ieee802154\_security\_params](structieee802154__security__params.md)

Security parameters.

**Definition** ieee802154\_mgmt.h:341

[ieee802154\_security\_params::key\_len](structieee802154__security__params.md#a03ba0953eaea5035346b35e0555beb9c)

uint8\_t key\_len

Key length of 16 bytes is mandatory for standards conformance.

**Definition** ieee802154\_mgmt.h:343

[ieee802154\_security\_params::level](structieee802154__security__params.md#a50b7b0cbb4151234747c41d41e6fd656)

uint8\_t level

Used instead of a frame-specific SecurityLevel parameter when constructing the auxiliary security hea...

**Definition** ieee802154\_mgmt.h:345

[ieee802154\_security\_params::key\_mode](structieee802154__security__params.md#a5b6248a76d95ede67495f765d4d35b57)

uint8\_t key\_mode

secKeyIdMode

**Definition** ieee802154\_mgmt.h:344

[ieee802154\_security\_params::key](structieee802154__security__params.md#ae47ed5df4c70bfd4a28319d35f34c940)

uint8\_t key[16]

secKeyDescriptor.secKey

**Definition** ieee802154\_mgmt.h:342

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_mgmt.h](ieee802154__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
