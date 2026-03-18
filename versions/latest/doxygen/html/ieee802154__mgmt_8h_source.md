---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ieee802154__mgmt_8h_source.html
original_path: doxygen/html/ieee802154__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

41

45

46#define \_NET\_IEEE802154\_LAYER NET\_MGMT\_LAYER\_L2

47#define \_NET\_IEEE802154\_CODE 0x154

48#define \_NET\_IEEE802154\_BASE (NET\_MGMT\_IFACE\_BIT | \

49 NET\_MGMT\_LAYER(\_NET\_IEEE802154\_LAYER) |\

50 NET\_MGMT\_LAYER\_CODE(\_NET\_IEEE802154\_CODE))

51#define \_NET\_IEEE802154\_EVENT (\_NET\_IEEE802154\_BASE | NET\_MGMT\_EVENT\_BIT)

52

53enum net\_request\_ieee802154\_cmd {

54 NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK = 1,

55 NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK,

56 NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN,

57 NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN,

58 NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN,

59 NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE,

60 NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE,

61 NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL,

62 NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL,

63 NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID,

64 NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID,

65 NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR,

66 NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR,

67 NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR,

68 NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR,

69 NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER,

70 NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER,

71 NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS,

72 NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS,

73};

74

78

107

[ 109](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da)#define NET\_REQUEST\_IEEE802154\_SET\_ACK (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK)

110

111[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_ACK](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da));

112

[ 114](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)#define NET\_REQUEST\_IEEE802154\_UNSET\_ACK \

115 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK)

116

117[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_UNSET\_ACK](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18));

118

[ 124](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9)#define NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN \

125 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN)

126

127[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9));

128

[ 134](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b)#define NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN \

135 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN)

136

137[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b));

138

[ 140](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe)#define NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN \

141 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN)

142

143[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe));

144

[ 146](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf)#define NET\_REQUEST\_IEEE802154\_ASSOCIATE \

147 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE)

148

149[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_ASSOCIATE](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf));

150

[ 152](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd)#define NET\_REQUEST\_IEEE802154\_DISASSOCIATE \

153 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE)

154

155[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_DISASSOCIATE](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd));

156

[ 158](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced)#define NET\_REQUEST\_IEEE802154\_SET\_CHANNEL \

159 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL)

160

161[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_CHANNEL](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced));

162

[ 164](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b)#define NET\_REQUEST\_IEEE802154\_GET\_CHANNEL \

165 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL)

166

167[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_CHANNEL](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b));

168

[ 170](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c)#define NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID \

171 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID)

172

173[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c));

174

[ 176](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f)#define NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID \

177 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID)

178

179[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f));

180

[ 185](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9)#define NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR \

186 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR)

187

188[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9));

189

[ 191](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66)#define NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR \

192 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR)

193

194[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66));

195

[ 197](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465)#define NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR \

198 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR)

199

200[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465));

201

[ 203](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241)#define NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR \

204 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR)

205

206[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241));

207

[ 212](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638)#define NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER \

213 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER)

214

215[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638));

216

[ 218](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4)#define NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER \

219 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER)

220

221[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4));

222

223#ifdef CONFIG\_NET\_L2\_IEEE802154\_SECURITY

224

[ 231](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654)#define NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS \

232 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS)

233

234[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654));

235

[ 241](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df)#define NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS \

242 (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS)

243

244[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df));

245

246#endif /\* CONFIG\_NET\_L2\_IEEE802154\_SECURITY \*/

247

251

255

256enum net\_event\_ieee802154\_cmd {

257 NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT = 1,

258};

259

263

275

[ 282](group__ieee802154__mgmt.md#ga0442eaa04068a7b66f9b4ae40b570470)#define NET\_EVENT\_IEEE802154\_SCAN\_RESULT \

283 (\_NET\_IEEE802154\_EVENT | NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT)

284

288

292

293#define IEEE802154\_IS\_CHAN\_SCANNED(\_channel\_set, \_chan) \

294 (\_channel\_set & BIT(\_chan - 1))

295#define IEEE802154\_IS\_CHAN\_UNSCANNED(\_channel\_set, \_chan) \

296 (!IEEE802154\_IS\_CHAN\_SCANNED(\_channel\_set, \_chan))

297

298#define IEEE802154\_ALL\_CHANNELS UINT32\_MAX

299

303

[ 309](structieee802154__req__params.md)struct [ieee802154\_req\_params](structieee802154__req__params.md) {

[ 311](structieee802154__req__params.md#ad49071ae3c35a548f6894d32be017ad7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [channel\_set](structieee802154__req__params.md#ad49071ae3c35a548f6894d32be017ad7);

312

[ 314](structieee802154__req__params.md#a75b3e1658829dfa4970cef7267250c9b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duration](structieee802154__req__params.md#a75b3e1658829dfa4970cef7267250c9b);

315

[ 317](structieee802154__req__params.md#a78c9f6b62c7cfc51f514df09a2719441) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel](structieee802154__req__params.md#a78c9f6b62c7cfc51f514df09a2719441); /\* in CPU byte order \*/

[ 319](structieee802154__req__params.md#abde2cf05ea51cd0e024552aaf2414c86) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pan\_id](structieee802154__req__params.md#abde2cf05ea51cd0e024552aaf2414c86); /\* in CPU byte order \*/

320

322 union {

[ 323](structieee802154__req__params.md#a9cafc55c59dc4eff07bdf03e60da07ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [short\_addr](structieee802154__req__params.md#a9cafc55c59dc4eff07bdf03e60da07ec); /\* in CPU byte order \*/

[ 324](structieee802154__req__params.md#aa1b2ea9ffb009a1b6255a9e57ddef9f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structieee802154__req__params.md#aa1b2ea9ffb009a1b6255a9e57ddef9f7)[[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)]; /\* in big endian \*/

325 };

326

[ 328](structieee802154__req__params.md#a8c63caa3ae260f4c6f9bebe71677673b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structieee802154__req__params.md#a8c63caa3ae260f4c6f9bebe71677673b);

[ 330](structieee802154__req__params.md#af08c2fa32367340c54c8d8bf9c46f34a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lqi](structieee802154__req__params.md#af08c2fa32367340c54c8d8bf9c46f34a);

331};

332

[ 339](structieee802154__security__params.md)struct [ieee802154\_security\_params](structieee802154__security__params.md) {

[ 340](structieee802154__security__params.md#ae47ed5df4c70bfd4a28319d35f34c940) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key](structieee802154__security__params.md#ae47ed5df4c70bfd4a28319d35f34c940)[16]; /\* secKeyDescriptor.secKey \*/

[ 341](structieee802154__security__params.md#a03ba0953eaea5035346b35e0555beb9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_len](structieee802154__security__params.md#a03ba0953eaea5035346b35e0555beb9c); /\* a key length of 16 bytes is mandatory for standards conformance \*/

[ 342](structieee802154__security__params.md#a5b6248a76d95ede67495f765d4d35b57) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [key\_mode](structieee802154__security__params.md#a5b6248a76d95ede67495f765d4d35b57) : 2; /\* secKeyIdMode \*/

[ 343](structieee802154__security__params.md#a50b7b0cbb4151234747c41d41e6fd656) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structieee802154__security__params.md#a50b7b0cbb4151234747c41d41e6fd656) : 3; /\* Used instead of a frame-specific SecurityLevel parameter when

344 \* constructing the auxiliary security header

345 \*/

346 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_unused : 3;

347};

348

349#ifdef \_\_cplusplus

350}

351#endif

352

356

357#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_MGMT\_H\_ \*/

[IEEE802154\_MAX\_ADDR\_LENGTH](group__ieee802154__l2.md#gae405ed23baf91fa3d96c81d5121faa1a)

#define IEEE802154\_MAX\_ADDR\_LENGTH

IEEE 802.15.4 maximum address length.

**Definition** ieee802154.h:143

[NET\_REQUEST\_IEEE802154\_ASSOCIATE](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf)

#define NET\_REQUEST\_IEEE802154\_ASSOCIATE

MLME-ASSOCIATE(...) request.

**Definition** ieee802154\_mgmt.h:146

[NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638)

#define NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER

MLME-SET(phyUnicastTxPower/phyBroadcastTxPower) request (currently not distinguished).

**Definition** ieee802154\_mgmt.h:212

[NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df)

#define NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS

Gets the configured sec\* attributes.

**Definition** ieee802154\_mgmt.h:241

[NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4)

#define NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER

MLME-GET(phyUnicastTxPower/phyBroadcastTxPower) request.

**Definition** ieee802154\_mgmt.h:218

[NET\_REQUEST\_IEEE802154\_SET\_CHANNEL](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced)

#define NET\_REQUEST\_IEEE802154\_SET\_CHANNEL

MLME-SET(phyCurrentChannel) request.

**Definition** ieee802154\_mgmt.h:158

[NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241)

#define NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR

MLME-GET(macShortAddress) request.

**Definition** ieee802154\_mgmt.h:203

[NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9)

#define NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN

MLME-SCAN(PASSIVE, ...) request.

**Definition** ieee802154\_mgmt.h:124

[NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f)

#define NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID

MLME-GET(macPanId) request.

**Definition** ieee802154\_mgmt.h:176

[NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654)

#define NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS

Configures basic sec\* MAC PIB attributes, implies macSecurityEnabled=true.

**Definition** ieee802154\_mgmt.h:231

[NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c)

#define NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID

MLME-SET(macPanId) request.

**Definition** ieee802154\_mgmt.h:170

[NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465)

#define NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR

MLME-SET(macShortAddress) request, only allowed for co-ordinators.

**Definition** ieee802154\_mgmt.h:197

[NET\_REQUEST\_IEEE802154\_SET\_ACK](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da)

#define NET\_REQUEST\_IEEE802154\_SET\_ACK

Sets AckTx for all subsequent MLME-DATA (aka TX) requests.

**Definition** ieee802154\_mgmt.h:109

[NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b)

#define NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN

MLME-SCAN(ACTIVE, ...) request.

**Definition** ieee802154\_mgmt.h:134

[NET\_REQUEST\_IEEE802154\_DISASSOCIATE](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd)

#define NET\_REQUEST\_IEEE802154\_DISASSOCIATE

MLME-DISASSOCIATE(...) request.

**Definition** ieee802154\_mgmt.h:152

[NET\_REQUEST\_IEEE802154\_GET\_CHANNEL](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b)

#define NET\_REQUEST\_IEEE802154\_GET\_CHANNEL

MLME-GET(phyCurrentChannel) request.

**Definition** ieee802154\_mgmt.h:164

[NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9)

#define NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR

Sets the extended interface address (non-standard), see sections 7.1 and 8.4.3.1, in big endian byte ...

**Definition** ieee802154\_mgmt.h:185

[NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe)

#define NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN

Cancels an ongoing MLME-SCAN(...) command (non-standard).

**Definition** ieee802154\_mgmt.h:140

[NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66)

#define NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR

like MLME-GET(macExtendedAddress) but in big endian byte order

**Definition** ieee802154\_mgmt.h:191

[NET\_REQUEST\_IEEE802154\_UNSET\_ACK](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)

#define NET\_REQUEST\_IEEE802154\_UNSET\_ACK

Unsets AckTx for all subsequent MLME-DATA requests.

**Definition** ieee802154\_mgmt.h:114

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

**Definition** net\_mgmt.h:96

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

**Definition** ieee802154\_mgmt.h:309

[ieee802154\_req\_params::duration](structieee802154__req__params.md#a75b3e1658829dfa4970cef7267250c9b)

uint32\_t duration

Duration of scan, per-channel, in milliseconds.

**Definition** ieee802154\_mgmt.h:314

[ieee802154\_req\_params::channel](structieee802154__req__params.md#a78c9f6b62c7cfc51f514df09a2719441)

uint16\_t channel

Current channel in use as a result.

**Definition** ieee802154\_mgmt.h:317

[ieee802154\_req\_params::len](structieee802154__req__params.md#a8c63caa3ae260f4c6f9bebe71677673b)

uint8\_t len

length of address

**Definition** ieee802154\_mgmt.h:328

[ieee802154\_req\_params::short\_addr](structieee802154__req__params.md#a9cafc55c59dc4eff07bdf03e60da07ec)

uint16\_t short\_addr

**Definition** ieee802154\_mgmt.h:323

[ieee802154\_req\_params::addr](structieee802154__req__params.md#aa1b2ea9ffb009a1b6255a9e57ddef9f7)

uint8\_t addr[8]

**Definition** ieee802154\_mgmt.h:324

[ieee802154\_req\_params::pan\_id](structieee802154__req__params.md#abde2cf05ea51cd0e024552aaf2414c86)

uint16\_t pan\_id

Current pan\_id in use as a result.

**Definition** ieee802154\_mgmt.h:319

[ieee802154\_req\_params::channel\_set](structieee802154__req__params.md#ad49071ae3c35a548f6894d32be017ad7)

uint32\_t channel\_set

The set of channels to scan, use above macros to manage it.

**Definition** ieee802154\_mgmt.h:311

[ieee802154\_req\_params::lqi](structieee802154__req__params.md#af08c2fa32367340c54c8d8bf9c46f34a)

uint8\_t lqi

Link quality information, between 0 and 255.

**Definition** ieee802154\_mgmt.h:330

[ieee802154\_security\_params](structieee802154__security__params.md)

Security parameters.

**Definition** ieee802154\_mgmt.h:339

[ieee802154\_security\_params::key\_len](structieee802154__security__params.md#a03ba0953eaea5035346b35e0555beb9c)

uint8\_t key\_len

**Definition** ieee802154\_mgmt.h:341

[ieee802154\_security\_params::level](structieee802154__security__params.md#a50b7b0cbb4151234747c41d41e6fd656)

uint8\_t level

**Definition** ieee802154\_mgmt.h:343

[ieee802154\_security\_params::key\_mode](structieee802154__security__params.md#a5b6248a76d95ede67495f765d4d35b57)

uint8\_t key\_mode

**Definition** ieee802154\_mgmt.h:342

[ieee802154\_security\_params::key](structieee802154__security__params.md#ae47ed5df4c70bfd4a28319d35f34c940)

uint8\_t key[16]

**Definition** ieee802154\_mgmt.h:340

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_mgmt.h](ieee802154__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
