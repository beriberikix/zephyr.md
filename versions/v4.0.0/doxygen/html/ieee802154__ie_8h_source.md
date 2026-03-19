---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ieee802154__ie_8h_source.html
original_path: doxygen/html/ieee802154__ie_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_ie.h

[Go to the documentation of this file.](ieee802154__ie_8h.md)

1/\*

2 \* Copyright (c) 2023 Florian Grandel, Zephyr Project.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

22

23#ifndef ZEPHYR\_INCLUDE\_NET\_IEEE802154\_IE\_H\_

24#define ZEPHYR\_INCLUDE\_NET\_IEEE802154\_IE\_H\_

25

26#include <[zephyr/net\_buf.h](net__buf_8h.md)>

27#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

28

36

[ 42](group__ieee802154__driver.md#ga207e3aa0454f9e4173c809cfe7ff32cd)enum [ieee802154\_ie\_type](group__ieee802154__driver.md#ga207e3aa0454f9e4173c809cfe7ff32cd) {

[ 43](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a) [IEEE802154\_IE\_TYPE\_HEADER](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a) = 0x0,

[ 44](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7) [IEEE802154\_IE\_TYPE\_PAYLOAD](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7),

45};

46

[ 53](group__ieee802154__driver.md#ga0de396c2c2c781ff85b94ebf577f15ce)enum [ieee802154\_header\_ie\_element\_id](group__ieee802154__driver.md#ga0de396c2c2c781ff85b94ebf577f15ce) {

[ 54](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14) = 0x00,

[ 55](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb) = 0x1a,

[ 56](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021) = 0x1b,

[ 57](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e) = 0x1d,

[ 58](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330) = 0x1e,

[ 59](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3) = 0x7e,

[ 60](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941) [IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941) = 0x7f,

61 /\* partial list, add additional ids as needed \*/

62};

63

65#define IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN 3

67

[ 69](structieee802154__header__ie__vendor__specific.md)struct [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md) {

[ 71](structieee802154__header__ie__vendor__specific.md#a52d5ef47cbf674438bdc59aff40d0cbe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vendor\_oui](structieee802154__header__ie__vendor__specific.md#a52d5ef47cbf674438bdc59aff40d0cbe)[IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN];

[ 73](structieee802154__header__ie__vendor__specific.md#a7227c96e07f5cd26353d10710d5a8db1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[vendor\_specific\_info](structieee802154__header__ie__vendor__specific.md#a7227c96e07f5cd26353d10710d5a8db1);

74} \_\_packed;

75

[ 77](structieee802154__header__ie__csl__full.md)struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md) {

[ 78](structieee802154__header__ie__csl__full.md#a27089bfc19fbef2e79c5dce1a300a7b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_phase](structieee802154__header__ie__csl__full.md#a27089bfc19fbef2e79c5dce1a300a7b6);

[ 79](structieee802154__header__ie__csl__full.md#a6633583d786b2935e27a9feb8918227d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_period](structieee802154__header__ie__csl__full.md#a6633583d786b2935e27a9feb8918227d);

[ 80](structieee802154__header__ie__csl__full.md#aec452cd03e9baa50253aaafd2232a011) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_rendezvous\_time](structieee802154__header__ie__csl__full.md#aec452cd03e9baa50253aaafd2232a011);

81} \_\_packed;

82

[ 84](structieee802154__header__ie__csl__reduced.md)struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md) {

[ 85](structieee802154__header__ie__csl__reduced.md#a6fb0873938f857263280286c7aedda11) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_phase](structieee802154__header__ie__csl__reduced.md#a6fb0873938f857263280286c7aedda11);

[ 86](structieee802154__header__ie__csl__reduced.md#a967fe59ea8da123bf07d9184195d00d3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_period](structieee802154__header__ie__csl__reduced.md#a967fe59ea8da123bf07d9184195d00d3);

87} \_\_packed;

88

[ 90](structieee802154__header__ie__csl.md)struct [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) {

91 union {

[ 93](structieee802154__header__ie__csl.md#abb040a32c97c219ae0674a30ce3c916b) struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md) [full](structieee802154__header__ie__csl.md#abb040a32c97c219ae0674a30ce3c916b);

[ 95](structieee802154__header__ie__csl.md#a8373e14f7c6cd1dfe8cd214dfa5d0676) struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md) [reduced](structieee802154__header__ie__csl.md#a8373e14f7c6cd1dfe8cd214dfa5d0676);

96 };

97} \_\_packed;

98

[ 100](structieee802154__header__ie__rit.md)struct [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md) {

[ 101](structieee802154__header__ie__rit.md#a94efc1605d6799a9d88e6cb801f7ec0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [time\_to\_first\_listen](structieee802154__header__ie__rit.md#a94efc1605d6799a9d88e6cb801f7ec0b);

[ 102](structieee802154__header__ie__rit.md#a5eaca9e09ebdbb933b4324c899c248b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [number\_of\_repeat\_listen](structieee802154__header__ie__rit.md#a5eaca9e09ebdbb933b4324c899c248b4);

[ 103](structieee802154__header__ie__rit.md#a73cd396d5e98799b655242f525ccf42b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [repeat\_listen\_interval](structieee802154__header__ie__rit.md#a73cd396d5e98799b655242f525ccf42b);

104} \_\_packed;

105

[ 110](structieee802154__header__ie__rendezvous__time__full.md)struct [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md) {

[ 111](structieee802154__header__ie__rendezvous__time__full.md#a57a0ae2de948d7890ef61e3e245c24cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rendezvous\_time](structieee802154__header__ie__rendezvous__time__full.md#a57a0ae2de948d7890ef61e3e245c24cd);

[ 112](structieee802154__header__ie__rendezvous__time__full.md#a77a83a45e1292ee4dfc99d388ec8b305) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wakeup\_interval](structieee802154__header__ie__rendezvous__time__full.md#a77a83a45e1292ee4dfc99d388ec8b305);

113} \_\_packed;

114

[ 119](structieee802154__header__ie__rendezvous__time__reduced.md)struct [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md) {

[ 120](structieee802154__header__ie__rendezvous__time__reduced.md#ac5691bb2f16feb4b51d7992a3f875b83) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rendezvous\_time](structieee802154__header__ie__rendezvous__time__reduced.md#ac5691bb2f16feb4b51d7992a3f875b83);

121} \_\_packed;

122

[ 124](structieee802154__header__ie__rendezvous__time.md)struct [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) {

125 union {

[ 127](structieee802154__header__ie__rendezvous__time.md#ad977678922a3cecd1159a9089c5d41b5) struct [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md) [full](structieee802154__header__ie__rendezvous__time.md#ad977678922a3cecd1159a9089c5d41b5);

[ 129](structieee802154__header__ie__rendezvous__time.md#a620857d35fb7dd3a56d193c7f056e4b5) struct [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md) [reduced](structieee802154__header__ie__rendezvous__time.md#a620857d35fb7dd3a56d193c7f056e4b5);

130 };

131} \_\_packed;

132

[ 134](structieee802154__header__ie__time__correction.md)struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) {

[ 135](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880);

136} \_\_packed;

137

139

140/\* @brief Generic Header IE, see section 7.4.2.1. \*/

141struct ieee802154\_header\_ie {

142#if CONFIG\_LITTLE\_ENDIAN

143 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length : 7;

144 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) element\_id\_low : 1; /\* see enum ieee802154\_header\_ie\_element\_id \*/

145 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) element\_id\_high : 7;

146 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type : 1; /\* always 0 \*/

147#else

148 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) element\_id\_low : 1; /\* see enum ieee802154\_header\_ie\_element\_id \*/

149 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length : 7;

150 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type : 1; /\* always 0 \*/

151 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) element\_id\_high : 7;

152#endif

153 union {

154 struct [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md) vendor\_specific;

155 struct [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) csl;

156 struct [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md) rit;

157 struct [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) rendezvous\_time;

158 struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) time\_correction;

159 /\* add additional supported header IEs here \*/

160 } content;

161} \_\_packed;

162

164

[ 166](group__ieee802154__driver.md#ga4f66344126179e2c98a17f19f6db516b)#define IEEE802154\_HEADER\_IE\_HEADER\_LENGTH sizeof(uint16\_t)

167

168

170#define IEEE802154\_DEFINE\_HEADER\_IE(\_element\_id, \_length, \_content, \_content\_type) \

171 (struct ieee802154\_header\_ie) { \

172 .length = (\_length), \

173 .element\_id\_high = (\_element\_id) >> 1U, .element\_id\_low = (\_element\_id) & 0x01, \

174 .type = IEEE802154\_IE\_TYPE\_HEADER, \

175 .content.\_content\_type = \_content, \

176 }

177

178#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT\_LEN(\_vendor\_specific\_info\_len) \

179 (IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN + (\_vendor\_specific\_info\_len))

180

181#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT(\_vendor\_oui, \_vendor\_specific\_info) \

182 (struct ieee802154\_header\_ie\_vendor\_specific) { \

183 .vendor\_oui = \_vendor\_oui, .vendor\_specific\_info = (\_vendor\_specific\_info), \

184 }

185

186#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED\_CONTENT(\_csl\_phase, \_csl\_period) \

187 (struct ieee802154\_header\_ie\_csl\_reduced) { \

188 .csl\_phase = sys\_cpu\_to\_le16(\_csl\_phase), \

189 .csl\_period = sys\_cpu\_to\_le16(\_csl\_period), \

190 }

191

192#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL\_CONTENT(\_csl\_phase, \_csl\_period, \

193 \_csl\_rendezvous\_time) \

194 (struct ieee802154\_header\_ie\_csl\_full) { \

195 .csl\_phase = sys\_cpu\_to\_le16(\_csl\_phase), \

196 .csl\_period = sys\_cpu\_to\_le16(\_csl\_period), \

197 .csl\_rendezvous\_time = sys\_cpu\_to\_le16(\_csl\_rendezvous\_time), \

198 }

199

200#define IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_NACK 0x8000

201#define IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK 0x0fff

202#define IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_SIGN\_BIT\_MASK 0x0800

203

204#define IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION\_CONTENT(\_ack, \_time\_correction\_us) \

205 (struct ieee802154\_header\_ie\_time\_correction) { \

206 .time\_sync\_info = sys\_cpu\_to\_le16( \

207 (!(\_ack) \* IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_NACK) | \

208 ((\_time\_correction\_us) & IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK)), \

209 }

211

[ 230](group__ieee802154__driver.md#gafc449a0c9d4ce8f128fd716b2a537f68)#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC(\_vendor\_oui, \_vendor\_specific\_info, \

231 \_vendor\_specific\_info\_len) \

232 IEEE802154\_DEFINE\_HEADER\_IE(IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE, \

233 IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT\_LEN( \

234 \_vendor\_specific\_info\_len), \

235 IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT( \

236 \_vendor\_oui, \_vendor\_specific\_info), \

237 vendor\_specific)

238

[ 254](group__ieee802154__driver.md#ga382debc13f36ee16e0c015a2c2555c8f)#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED(\_csl\_phase, \_csl\_period) \

255 IEEE802154\_DEFINE\_HEADER\_IE( \

256 IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE, \

257 sizeof(struct ieee802154\_header\_ie\_csl\_reduced), \

258 IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED\_CONTENT(\_csl\_phase, \_csl\_period), \

259 csl.reduced)

260

[ 278](group__ieee802154__driver.md#ga3392a33334814ae63e212491ea90ae74)#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL(\_csl\_phase, \_csl\_period, \_csl\_rendezvous\_time) \

279 IEEE802154\_DEFINE\_HEADER\_IE(IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE, \

280 sizeof(struct ieee802154\_header\_ie\_csl\_full), \

281 IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL\_CONTENT( \

282 \_csl\_phase, \_csl\_period, \_csl\_rendezvous\_time), \

283 csl.full)

284

[ 301](group__ieee802154__driver.md#gac2549865f529b5aff1653c80ceda9650)#define IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION(\_ack, \_time\_correction\_us) \

302 IEEE802154\_DEFINE\_HEADER\_IE( \

303 IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE, \

304 sizeof(struct ieee802154\_header\_ie\_time\_correction), \

305 IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION\_CONTENT(\_ack, \_time\_correction\_us), \

306 time\_correction)

307

316static inline [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

[ 317](group__ieee802154__driver.md#gaaae70f7d15135b2e77369cef3c61ba62)[ieee802154\_header\_ie\_get\_time\_correction\_us](group__ieee802154__driver.md#gaaae70f7d15135b2e77369cef3c61ba62)(struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) \*ie)

318{

319 if (ie->[time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) & IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_SIGN\_BIT\_MASK) {

320 /\* Negative integer \*/

321 return ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))ie->[time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) | ~IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK;

322 }

323

324 /\* Positive integer \*/

325 return ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))ie->[time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) & IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK;

326}

327

[ 334](group__ieee802154__driver.md#gaef81648e58dc4fbdfd942a1d856952fa)static inline void [ieee802154\_header\_ie\_set\_element\_id](group__ieee802154__driver.md#gaef81648e58dc4fbdfd942a1d856952fa)(struct ieee802154\_header\_ie \*ie,

335 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) element\_id)

336{

337 ie->element\_id\_high = element\_id >> 1U;

338 ie->element\_id\_low = element\_id & 0x01;

339}

340

[ 348](group__ieee802154__driver.md#gaec7f06d8bf0b44c3350d1d07a65c6cb4)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ieee802154\_header\_ie\_get\_element\_id](group__ieee802154__driver.md#gaec7f06d8bf0b44c3350d1d07a65c6cb4)(struct ieee802154\_header\_ie \*ie)

349{

350 return (ie->element\_id\_high << 1U) | ie->element\_id\_low;

351}

352

[ 354](group__ieee802154__driver.md#gaaaf32be17c41497c8d3be48292ad1374)#define IEEE802154\_TIME\_CORRECTION\_HEADER\_IE\_LEN \

355 (IEEE802154\_HEADER\_IE\_HEADER\_LENGTH + sizeof(struct ieee802154\_header\_ie\_time\_correction))

356

[ 358](group__ieee802154__driver.md#gae16b5d403da141b0f9d9279817703677)#define IEEE802154\_HEADER\_TERMINATION\_1\_HEADER\_IE\_LEN IEEE802154\_HEADER\_IE\_HEADER\_LENGTH

359

365

366#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_IE\_H\_ \*/

[ieee802154\_header\_ie\_element\_id](group__ieee802154__driver.md#ga0de396c2c2c781ff85b94ebf577f15ce)

ieee802154\_header\_ie\_element\_id

Header Information Element IDs.

**Definition** ieee802154\_ie.h:53

[ieee802154\_ie\_type](group__ieee802154__driver.md#ga207e3aa0454f9e4173c809cfe7ff32cd)

ieee802154\_ie\_type

Information Element Types.

**Definition** ieee802154\_ie.h:42

[ieee802154\_header\_ie\_get\_time\_correction\_us](group__ieee802154__driver.md#gaaae70f7d15135b2e77369cef3c61ba62)

static int16\_t ieee802154\_header\_ie\_get\_time\_correction\_us(struct ieee802154\_header\_ie\_time\_correction \*ie)

Retrieve the time correction value in microseconds from a Time Correction IE, see section 7....

**Definition** ieee802154\_ie.h:317

[ieee802154\_header\_ie\_get\_element\_id](group__ieee802154__driver.md#gaec7f06d8bf0b44c3350d1d07a65c6cb4)

static uint8\_t ieee802154\_header\_ie\_get\_element\_id(struct ieee802154\_header\_ie \*ie)

Get the element ID of a header IE.

**Definition** ieee802154\_ie.h:348

[ieee802154\_header\_ie\_set\_element\_id](group__ieee802154__driver.md#gaef81648e58dc4fbdfd942a1d856952fa)

static void ieee802154\_header\_ie\_set\_element\_id(struct ieee802154\_header\_ie \*ie, uint8\_t element\_id)

Set the element ID of a header IE.

**Definition** ieee802154\_ie.h:334

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE

Rendezvous time IE.

**Definition** ieee802154\_ie.h:57

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE

Time correction IE.

**Definition** ieee802154\_ie.h:58

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1

Header termination 1.

**Definition** ieee802154\_ie.h:59

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE

CSL IE.

**Definition** ieee802154\_ie.h:55

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2

Header termination 2.

**Definition** ieee802154\_ie.h:60

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE

Vendor specific IE.

**Definition** ieee802154\_ie.h:54

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE

RIT IE.

**Definition** ieee802154\_ie.h:56

[IEEE802154\_IE\_TYPE\_HEADER](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a)

@ IEEE802154\_IE\_TYPE\_HEADER

Header type.

**Definition** ieee802154\_ie.h:43

[IEEE802154\_IE\_TYPE\_PAYLOAD](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7)

@ IEEE802154\_IE\_TYPE\_PAYLOAD

Payload type.

**Definition** ieee802154\_ie.h:44

[net\_buf.h](net__buf_8h.md)

Buffer management.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md)

Full CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:77

[ieee802154\_header\_ie\_csl\_full::csl\_phase](structieee802154__header__ie__csl__full.md#a27089bfc19fbef2e79c5dce1a300a7b6)

uint16\_t csl\_phase

CSL phase.

**Definition** ieee802154\_ie.h:78

[ieee802154\_header\_ie\_csl\_full::csl\_period](structieee802154__header__ie__csl__full.md#a6633583d786b2935e27a9feb8918227d)

uint16\_t csl\_period

CSL period.

**Definition** ieee802154\_ie.h:79

[ieee802154\_header\_ie\_csl\_full::csl\_rendezvous\_time](structieee802154__header__ie__csl__full.md#aec452cd03e9baa50253aaafd2232a011)

uint16\_t csl\_rendezvous\_time

Rendezvous time.

**Definition** ieee802154\_ie.h:80

[ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md)

Reduced CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:84

[ieee802154\_header\_ie\_csl\_reduced::csl\_phase](structieee802154__header__ie__csl__reduced.md#a6fb0873938f857263280286c7aedda11)

uint16\_t csl\_phase

CSL phase.

**Definition** ieee802154\_ie.h:85

[ieee802154\_header\_ie\_csl\_reduced::csl\_period](structieee802154__header__ie__csl__reduced.md#a967fe59ea8da123bf07d9184195d00d3)

uint16\_t csl\_period

CSL period.

**Definition** ieee802154\_ie.h:86

[ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md)

Generic CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:90

[ieee802154\_header\_ie\_csl::reduced](structieee802154__header__ie__csl.md#a8373e14f7c6cd1dfe8cd214dfa5d0676)

struct ieee802154\_header\_ie\_csl\_reduced reduced

CSL reduced information.

**Definition** ieee802154\_ie.h:95

[ieee802154\_header\_ie\_csl::full](structieee802154__header__ie__csl.md#abb040a32c97c219ae0674a30ce3c916b)

struct ieee802154\_header\_ie\_csl\_full full

CSL full information.

**Definition** ieee802154\_ie.h:93

[ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md)

Full Rendezvous Time IE, see section 7.4.2.6 (macCslInterval is nonzero).

**Definition** ieee802154\_ie.h:110

[ieee802154\_header\_ie\_rendezvous\_time\_full::rendezvous\_time](structieee802154__header__ie__rendezvous__time__full.md#a57a0ae2de948d7890ef61e3e245c24cd)

uint16\_t rendezvous\_time

Rendezvous time.

**Definition** ieee802154\_ie.h:111

[ieee802154\_header\_ie\_rendezvous\_time\_full::wakeup\_interval](structieee802154__header__ie__rendezvous__time__full.md#a77a83a45e1292ee4dfc99d388ec8b305)

uint16\_t wakeup\_interval

Wakeup interval.

**Definition** ieee802154\_ie.h:112

[ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md)

Reduced Rendezvous Time IE, see section 7.4.2.6 (macCslInterval is zero).

**Definition** ieee802154\_ie.h:119

[ieee802154\_header\_ie\_rendezvous\_time\_reduced::rendezvous\_time](structieee802154__header__ie__rendezvous__time__reduced.md#ac5691bb2f16feb4b51d7992a3f875b83)

uint16\_t rendezvous\_time

Rendezvous time.

**Definition** ieee802154\_ie.h:120

[ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md)

Rendezvous Time IE, see section 7.4.2.6.

**Definition** ieee802154\_ie.h:124

[ieee802154\_header\_ie\_rendezvous\_time::reduced](structieee802154__header__ie__rendezvous__time.md#a620857d35fb7dd3a56d193c7f056e4b5)

struct ieee802154\_header\_ie\_rendezvous\_time\_reduced reduced

Rendezvous time reduced information.

**Definition** ieee802154\_ie.h:129

[ieee802154\_header\_ie\_rendezvous\_time::full](structieee802154__header__ie__rendezvous__time.md#ad977678922a3cecd1159a9089c5d41b5)

struct ieee802154\_header\_ie\_rendezvous\_time\_full full

Rendezvous time full information.

**Definition** ieee802154\_ie.h:127

[ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md)

RIT IE, see section 7.4.2.4.

**Definition** ieee802154\_ie.h:100

[ieee802154\_header\_ie\_rit::number\_of\_repeat\_listen](structieee802154__header__ie__rit.md#a5eaca9e09ebdbb933b4324c899c248b4)

uint8\_t number\_of\_repeat\_listen

Number of Repeat Listen.

**Definition** ieee802154\_ie.h:102

[ieee802154\_header\_ie\_rit::repeat\_listen\_interval](structieee802154__header__ie__rit.md#a73cd396d5e98799b655242f525ccf42b)

uint16\_t repeat\_listen\_interval

Repeat listen interval.

**Definition** ieee802154\_ie.h:103

[ieee802154\_header\_ie\_rit::time\_to\_first\_listen](structieee802154__header__ie__rit.md#a94efc1605d6799a9d88e6cb801f7ec0b)

uint8\_t time\_to\_first\_listen

Time to First Listen.

**Definition** ieee802154\_ie.h:101

[ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md)

Time Correction IE, see section 7.4.2.7.

**Definition** ieee802154\_ie.h:134

[ieee802154\_header\_ie\_time\_correction::time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880)

uint16\_t time\_sync\_info

Time synchronization information.

**Definition** ieee802154\_ie.h:135

[ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md)

Vendor Specific Header IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:69

[ieee802154\_header\_ie\_vendor\_specific::vendor\_oui](structieee802154__header__ie__vendor__specific.md#a52d5ef47cbf674438bdc59aff40d0cbe)

uint8\_t vendor\_oui[IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN]

Vendor OUI.

**Definition** ieee802154\_ie.h:71

[ieee802154\_header\_ie\_vendor\_specific::vendor\_specific\_info](structieee802154__header__ie__vendor__specific.md#a7227c96e07f5cd26353d10710d5a8db1)

uint8\_t \* vendor\_specific\_info

Vendor specific information.

**Definition** ieee802154\_ie.h:73

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_ie.h](ieee802154__ie_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
