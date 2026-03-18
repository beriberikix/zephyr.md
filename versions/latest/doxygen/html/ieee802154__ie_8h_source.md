---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ieee802154__ie_8h_source.html
original_path: doxygen/html/ieee802154__ie_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

26#include <[zephyr/net/buf.h](net_2buf_8h.md)>

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

[ 70](structieee802154__header__ie__vendor__specific.md#a52d5ef47cbf674438bdc59aff40d0cbe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vendor\_oui](structieee802154__header__ie__vendor__specific.md#a52d5ef47cbf674438bdc59aff40d0cbe)[IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN];

[ 71](structieee802154__header__ie__vendor__specific.md#a7227c96e07f5cd26353d10710d5a8db1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[vendor\_specific\_info](structieee802154__header__ie__vendor__specific.md#a7227c96e07f5cd26353d10710d5a8db1);

72} \_\_packed;

73

[ 75](structieee802154__header__ie__csl__full.md)struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md) {

[ 76](structieee802154__header__ie__csl__full.md#a27089bfc19fbef2e79c5dce1a300a7b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_phase](structieee802154__header__ie__csl__full.md#a27089bfc19fbef2e79c5dce1a300a7b6);

[ 77](structieee802154__header__ie__csl__full.md#a6633583d786b2935e27a9feb8918227d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_period](structieee802154__header__ie__csl__full.md#a6633583d786b2935e27a9feb8918227d);

[ 78](structieee802154__header__ie__csl__full.md#aec452cd03e9baa50253aaafd2232a011) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_rendezvous\_time](structieee802154__header__ie__csl__full.md#aec452cd03e9baa50253aaafd2232a011);

79} \_\_packed;

80

[ 82](structieee802154__header__ie__csl__reduced.md)struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md) {

[ 83](structieee802154__header__ie__csl__reduced.md#a6fb0873938f857263280286c7aedda11) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_phase](structieee802154__header__ie__csl__reduced.md#a6fb0873938f857263280286c7aedda11);

[ 84](structieee802154__header__ie__csl__reduced.md#a967fe59ea8da123bf07d9184195d00d3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [csl\_period](structieee802154__header__ie__csl__reduced.md#a967fe59ea8da123bf07d9184195d00d3);

85} \_\_packed;

86

[ 88](structieee802154__header__ie__csl.md)struct [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) {

89 union {

[ 90](structieee802154__header__ie__csl.md#abb040a32c97c219ae0674a30ce3c916b) struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md) [full](structieee802154__header__ie__csl.md#abb040a32c97c219ae0674a30ce3c916b);

[ 91](structieee802154__header__ie__csl.md#a8373e14f7c6cd1dfe8cd214dfa5d0676) struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md) [reduced](structieee802154__header__ie__csl.md#a8373e14f7c6cd1dfe8cd214dfa5d0676);

92 };

93} \_\_packed;

94

[ 96](structieee802154__header__ie__rit.md)struct [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md) {

[ 97](structieee802154__header__ie__rit.md#a94efc1605d6799a9d88e6cb801f7ec0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [time\_to\_first\_listen](structieee802154__header__ie__rit.md#a94efc1605d6799a9d88e6cb801f7ec0b);

[ 98](structieee802154__header__ie__rit.md#a5eaca9e09ebdbb933b4324c899c248b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [number\_of\_repeat\_listen](structieee802154__header__ie__rit.md#a5eaca9e09ebdbb933b4324c899c248b4);

[ 99](structieee802154__header__ie__rit.md#a73cd396d5e98799b655242f525ccf42b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [repeat\_listen\_interval](structieee802154__header__ie__rit.md#a73cd396d5e98799b655242f525ccf42b);

100} \_\_packed;

101

[ 106](structieee802154__header__ie__rendezvous__time__full.md)struct [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md) {

[ 107](structieee802154__header__ie__rendezvous__time__full.md#a57a0ae2de948d7890ef61e3e245c24cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rendezvous\_time](structieee802154__header__ie__rendezvous__time__full.md#a57a0ae2de948d7890ef61e3e245c24cd);

[ 108](structieee802154__header__ie__rendezvous__time__full.md#a77a83a45e1292ee4dfc99d388ec8b305) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wakeup\_interval](structieee802154__header__ie__rendezvous__time__full.md#a77a83a45e1292ee4dfc99d388ec8b305);

109} \_\_packed;

110

[ 115](structieee802154__header__ie__rendezvous__time__reduced.md)struct [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md) {

[ 116](structieee802154__header__ie__rendezvous__time__reduced.md#ac5691bb2f16feb4b51d7992a3f875b83) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rendezvous\_time](structieee802154__header__ie__rendezvous__time__reduced.md#ac5691bb2f16feb4b51d7992a3f875b83);

117} \_\_packed;

118

[ 120](structieee802154__header__ie__rendezvous__time.md)struct [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) {

121 union {

[ 122](structieee802154__header__ie__rendezvous__time.md#ad977678922a3cecd1159a9089c5d41b5) struct [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md) [full](structieee802154__header__ie__rendezvous__time.md#ad977678922a3cecd1159a9089c5d41b5);

[ 123](structieee802154__header__ie__rendezvous__time.md#a620857d35fb7dd3a56d193c7f056e4b5) struct [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md) [reduced](structieee802154__header__ie__rendezvous__time.md#a620857d35fb7dd3a56d193c7f056e4b5);

124 };

125} \_\_packed;

126

[ 128](structieee802154__header__ie__time__correction.md)struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) {

[ 129](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880);

130} \_\_packed;

131

132/\* @brief Generic Header IE, see section 7.4.2.1. \*/

[ 133](structieee802154__header__ie.md)struct [ieee802154\_header\_ie](structieee802154__header__ie.md) {

134#if CONFIG\_LITTLE\_ENDIAN

135 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [length](structieee802154__header__ie.md#a9c1632eac7955370784445f5571d337d) : 7;

136 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [element\_id\_low](structieee802154__header__ie.md#ab389f739b6e6f77add4f77786f8c0577) : 1; /\* see enum ieee802154\_header\_ie\_element\_id \*/

137 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [element\_id\_high](structieee802154__header__ie.md#a8521084dddda0853d3711d5b0dc1eada) : 7;

138 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structieee802154__header__ie.md#aa2c087927391e811437028c55141ce94) : 1; /\* always 0 \*/

139#else

[ 140](structieee802154__header__ie.md#ab389f739b6e6f77add4f77786f8c0577) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [element\_id\_low](structieee802154__header__ie.md#ab389f739b6e6f77add4f77786f8c0577) : 1; /\* see enum ieee802154\_header\_ie\_element\_id \*/

[ 141](structieee802154__header__ie.md#a9c1632eac7955370784445f5571d337d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [length](structieee802154__header__ie.md#a9c1632eac7955370784445f5571d337d) : 7;

[ 142](structieee802154__header__ie.md#aa2c087927391e811437028c55141ce94) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structieee802154__header__ie.md#aa2c087927391e811437028c55141ce94) : 1; /\* always 0 \*/

[ 143](structieee802154__header__ie.md#a8521084dddda0853d3711d5b0dc1eada) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [element\_id\_high](structieee802154__header__ie.md#a8521084dddda0853d3711d5b0dc1eada) : 7;

144#endif

145 union {

[ 146](structieee802154__header__ie.md#ac932f99fb3b93debde45e1f82d059cf8) struct [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md) [vendor\_specific](structieee802154__header__ie.md#ac932f99fb3b93debde45e1f82d059cf8);

[ 147](structieee802154__header__ie.md#af73871d2a4c26d6e3cde0c18a74e7006) struct [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) [csl](structieee802154__header__ie.md#af73871d2a4c26d6e3cde0c18a74e7006);

[ 148](structieee802154__header__ie.md#a0950703553d298a6af00cdb11012146c) struct [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md) [rit](structieee802154__header__ie.md#a0950703553d298a6af00cdb11012146c);

[ 149](structieee802154__header__ie.md#aecf96d749b103c1c5f702da675bacb26) struct [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) [rendezvous\_time](structieee802154__header__ie.md#aecf96d749b103c1c5f702da675bacb26);

[ 150](structieee802154__header__ie.md#a6a9c76df7d1e7b082642f10eeb4875af) struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) [time\_correction](structieee802154__header__ie.md#a6a9c76df7d1e7b082642f10eeb4875af);

151 /\* add additional supported header IEs here \*/

[ 152](structieee802154__header__ie.md#ac2d67fc001eddde667f25ebbf5ef5ce1) } [content](structieee802154__header__ie.md#ac2d67fc001eddde667f25ebbf5ef5ce1);

153} \_\_packed;

154

[ 156](group__ieee802154__driver.md#ga4f66344126179e2c98a17f19f6db516b)#define IEEE802154\_HEADER\_IE\_HEADER\_LENGTH sizeof(uint16\_t)

157

158

160#define IEEE802154\_DEFINE\_HEADER\_IE(\_element\_id, \_length, \_content, \_content\_type) \

161 (struct ieee802154\_header\_ie) { \

162 .length = (\_length), \

163 .element\_id\_high = (\_element\_id) >> 1U, .element\_id\_low = (\_element\_id) & 0x01, \

164 .type = IEEE802154\_IE\_TYPE\_HEADER, \

165 .content.\_content\_type = \_content, \

166 }

167

168#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT\_LEN(\_vendor\_specific\_info\_len) \

169 (IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN + (\_vendor\_specific\_info\_len))

170

171#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT(\_vendor\_oui, \_vendor\_specific\_info) \

172 (struct ieee802154\_header\_ie\_vendor\_specific) { \

173 .vendor\_oui = \_vendor\_oui, .vendor\_specific\_info = (\_vendor\_specific\_info), \

174 }

175

176#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED\_CONTENT(\_csl\_phase, \_csl\_period) \

177 (struct ieee802154\_header\_ie\_csl\_reduced) { \

178 .csl\_phase = sys\_cpu\_to\_le16(\_csl\_phase), \

179 .csl\_period = sys\_cpu\_to\_le16(\_csl\_period), \

180 }

181

182#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL\_CONTENT(\_csl\_phase, \_csl\_period, \

183 \_csl\_rendezvous\_time) \

184 (struct ieee802154\_header\_ie\_csl\_full) { \

185 .csl\_phase = sys\_cpu\_to\_le16(\_csl\_phase), \

186 .csl\_period = sys\_cpu\_to\_le16(\_csl\_period), \

187 .csl\_rendezvous\_time = sys\_cpu\_to\_le16(\_csl\_rendezvous\_time), \

188 }

189

190#define IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_NACK 0x8000

191#define IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK 0x0fff

192#define IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_SIGN\_BIT\_MASK 0x0800

193

194#define IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION\_CONTENT(\_ack, \_time\_correction\_us) \

195 (struct ieee802154\_header\_ie\_time\_correction) { \

196 .time\_sync\_info = sys\_cpu\_to\_le16( \

197 (!(\_ack) \* IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_NACK) | \

198 ((\_time\_correction\_us) & IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK)), \

199 }

201

[ 220](group__ieee802154__driver.md#gafc449a0c9d4ce8f128fd716b2a537f68)#define IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC(\_vendor\_oui, \_vendor\_specific\_info, \

221 \_vendor\_specific\_info\_len) \

222 IEEE802154\_DEFINE\_HEADER\_IE(IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE, \

223 IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT\_LEN( \

224 \_vendor\_specific\_info\_len), \

225 IEEE802154\_DEFINE\_HEADER\_IE\_VENDOR\_SPECIFIC\_CONTENT( \

226 \_vendor\_oui, \_vendor\_specific\_info), \

227 vendor\_specific)

228

[ 244](group__ieee802154__driver.md#ga382debc13f36ee16e0c015a2c2555c8f)#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED(\_csl\_phase, \_csl\_period) \

245 IEEE802154\_DEFINE\_HEADER\_IE( \

246 IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE, \

247 sizeof(struct ieee802154\_header\_ie\_csl\_reduced), \

248 IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_REDUCED\_CONTENT(\_csl\_phase, \_csl\_period), \

249 csl.reduced)

250

[ 268](group__ieee802154__driver.md#ga3392a33334814ae63e212491ea90ae74)#define IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL(\_csl\_phase, \_csl\_period, \_csl\_rendezvous\_time) \

269 IEEE802154\_DEFINE\_HEADER\_IE(IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE, \

270 sizeof(struct ieee802154\_header\_ie\_csl\_full), \

271 IEEE802154\_DEFINE\_HEADER\_IE\_CSL\_FULL\_CONTENT( \

272 \_csl\_phase, \_csl\_period, \_csl\_rendezvous\_time), \

273 csl.full)

274

[ 291](group__ieee802154__driver.md#gac2549865f529b5aff1653c80ceda9650)#define IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION(\_ack, \_time\_correction\_us) \

292 IEEE802154\_DEFINE\_HEADER\_IE( \

293 IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE, \

294 sizeof(struct ieee802154\_header\_ie\_time\_correction), \

295 IEEE802154\_DEFINE\_HEADER\_IE\_TIME\_CORRECTION\_CONTENT(\_ack, \_time\_correction\_us), \

296 time\_correction)

297

306static inline [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

[ 307](group__ieee802154__driver.md#gaaae70f7d15135b2e77369cef3c61ba62)[ieee802154\_header\_ie\_get\_time\_correction\_us](group__ieee802154__driver.md#gaaae70f7d15135b2e77369cef3c61ba62)(struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) \*ie)

308{

309 if (ie->[time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) & IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_SIGN\_BIT\_MASK) {

310 /\* Negative integer \*/

311 return ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))ie->[time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) | ~IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK;

312 }

313

314 /\* Positive integer \*/

315 return ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))ie->[time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880) & IEEE802154\_HEADER\_IE\_TIME\_CORRECTION\_MASK;

316}

317

[ 324](group__ieee802154__driver.md#gaef81648e58dc4fbdfd942a1d856952fa)static inline void [ieee802154\_header\_ie\_set\_element\_id](group__ieee802154__driver.md#gaef81648e58dc4fbdfd942a1d856952fa)(struct [ieee802154\_header\_ie](structieee802154__header__ie.md) \*ie,

325 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) element\_id)

326{

327 ie->[element\_id\_high](structieee802154__header__ie.md#a8521084dddda0853d3711d5b0dc1eada) = element\_id >> 1U;

328 ie->[element\_id\_low](structieee802154__header__ie.md#ab389f739b6e6f77add4f77786f8c0577) = element\_id & 0x01;

329}

330

[ 338](group__ieee802154__driver.md#gaec7f06d8bf0b44c3350d1d07a65c6cb4)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ieee802154\_header\_ie\_get\_element\_id](group__ieee802154__driver.md#gaec7f06d8bf0b44c3350d1d07a65c6cb4)(struct [ieee802154\_header\_ie](structieee802154__header__ie.md) \*ie)

339{

340 return (ie->[element\_id\_high](structieee802154__header__ie.md#a8521084dddda0853d3711d5b0dc1eada) << 1U) | ie->[element\_id\_low](structieee802154__header__ie.md#ab389f739b6e6f77add4f77786f8c0577);

341}

342

[ 344](group__ieee802154__driver.md#gaaaf32be17c41497c8d3be48292ad1374)#define IEEE802154\_TIME\_CORRECTION\_HEADER\_IE\_LEN \

345 (IEEE802154\_HEADER\_IE\_HEADER\_LENGTH + sizeof(struct ieee802154\_header\_ie\_time\_correction))

346

[ 348](group__ieee802154__driver.md#gae16b5d403da141b0f9d9279817703677)#define IEEE802154\_HEADER\_TERMINATION\_1\_HEADER\_IE\_LEN IEEE802154\_HEADER\_IE\_HEADER\_LENGTH

349

355

356#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_IE\_H\_ \*/

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

**Definition** ieee802154\_ie.h:307

[ieee802154\_header\_ie\_get\_element\_id](group__ieee802154__driver.md#gaec7f06d8bf0b44c3350d1d07a65c6cb4)

static uint8\_t ieee802154\_header\_ie\_get\_element\_id(struct ieee802154\_header\_ie \*ie)

Get the element ID of a header IE.

**Definition** ieee802154\_ie.h:338

[ieee802154\_header\_ie\_set\_element\_id](group__ieee802154__driver.md#gaef81648e58dc4fbdfd942a1d856952fa)

static void ieee802154\_header\_ie\_set\_element\_id(struct ieee802154\_header\_ie \*ie, uint8\_t element\_id)

Set the element ID of a header IE.

**Definition** ieee802154\_ie.h:324

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RENDEZVOUS\_TIME\_IE

**Definition** ieee802154\_ie.h:57

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_TIME\_CORRECTION\_IE

**Definition** ieee802154\_ie.h:58

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_1

**Definition** ieee802154\_ie.h:59

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_CSL\_IE

**Definition** ieee802154\_ie.h:55

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_HEADER\_TERMINATION\_2

**Definition** ieee802154\_ie.h:60

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_VENDOR\_SPECIFIC\_IE

**Definition** ieee802154\_ie.h:54

[IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE](group__ieee802154__driver.md#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021)

@ IEEE802154\_HEADER\_IE\_ELEMENT\_ID\_RIT\_IE

**Definition** ieee802154\_ie.h:56

[IEEE802154\_IE\_TYPE\_HEADER](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a)

@ IEEE802154\_IE\_TYPE\_HEADER

**Definition** ieee802154\_ie.h:43

[IEEE802154\_IE\_TYPE\_PAYLOAD](group__ieee802154__driver.md#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7)

@ IEEE802154\_IE\_TYPE\_PAYLOAD

**Definition** ieee802154\_ie.h:44

[buf.h](net_2buf_8h.md)

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

**Definition** ieee802154\_ie.h:75

[ieee802154\_header\_ie\_csl\_full::csl\_phase](structieee802154__header__ie__csl__full.md#a27089bfc19fbef2e79c5dce1a300a7b6)

uint16\_t csl\_phase

**Definition** ieee802154\_ie.h:76

[ieee802154\_header\_ie\_csl\_full::csl\_period](structieee802154__header__ie__csl__full.md#a6633583d786b2935e27a9feb8918227d)

uint16\_t csl\_period

**Definition** ieee802154\_ie.h:77

[ieee802154\_header\_ie\_csl\_full::csl\_rendezvous\_time](structieee802154__header__ie__csl__full.md#aec452cd03e9baa50253aaafd2232a011)

uint16\_t csl\_rendezvous\_time

**Definition** ieee802154\_ie.h:78

[ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md)

Reduced CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:82

[ieee802154\_header\_ie\_csl\_reduced::csl\_phase](structieee802154__header__ie__csl__reduced.md#a6fb0873938f857263280286c7aedda11)

uint16\_t csl\_phase

**Definition** ieee802154\_ie.h:83

[ieee802154\_header\_ie\_csl\_reduced::csl\_period](structieee802154__header__ie__csl__reduced.md#a967fe59ea8da123bf07d9184195d00d3)

uint16\_t csl\_period

**Definition** ieee802154\_ie.h:84

[ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md)

Generic CSL IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:88

[ieee802154\_header\_ie\_csl::reduced](structieee802154__header__ie__csl.md#a8373e14f7c6cd1dfe8cd214dfa5d0676)

struct ieee802154\_header\_ie\_csl\_reduced reduced

**Definition** ieee802154\_ie.h:91

[ieee802154\_header\_ie\_csl::full](structieee802154__header__ie__csl.md#abb040a32c97c219ae0674a30ce3c916b)

struct ieee802154\_header\_ie\_csl\_full full

**Definition** ieee802154\_ie.h:90

[ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md)

Full Rendezvous Time IE, see section 7.4.2.6 (macCslInterval is nonzero).

**Definition** ieee802154\_ie.h:106

[ieee802154\_header\_ie\_rendezvous\_time\_full::rendezvous\_time](structieee802154__header__ie__rendezvous__time__full.md#a57a0ae2de948d7890ef61e3e245c24cd)

uint16\_t rendezvous\_time

**Definition** ieee802154\_ie.h:107

[ieee802154\_header\_ie\_rendezvous\_time\_full::wakeup\_interval](structieee802154__header__ie__rendezvous__time__full.md#a77a83a45e1292ee4dfc99d388ec8b305)

uint16\_t wakeup\_interval

**Definition** ieee802154\_ie.h:108

[ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md)

Reduced Rendezvous Time IE, see section 7.4.2.6 (macCslInterval is zero).

**Definition** ieee802154\_ie.h:115

[ieee802154\_header\_ie\_rendezvous\_time\_reduced::rendezvous\_time](structieee802154__header__ie__rendezvous__time__reduced.md#ac5691bb2f16feb4b51d7992a3f875b83)

uint16\_t rendezvous\_time

**Definition** ieee802154\_ie.h:116

[ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md)

Rendezvous Time IE, see section 7.4.2.6.

**Definition** ieee802154\_ie.h:120

[ieee802154\_header\_ie\_rendezvous\_time::reduced](structieee802154__header__ie__rendezvous__time.md#a620857d35fb7dd3a56d193c7f056e4b5)

struct ieee802154\_header\_ie\_rendezvous\_time\_reduced reduced

**Definition** ieee802154\_ie.h:123

[ieee802154\_header\_ie\_rendezvous\_time::full](structieee802154__header__ie__rendezvous__time.md#ad977678922a3cecd1159a9089c5d41b5)

struct ieee802154\_header\_ie\_rendezvous\_time\_full full

**Definition** ieee802154\_ie.h:122

[ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md)

RIT IE, see section 7.4.2.4.

**Definition** ieee802154\_ie.h:96

[ieee802154\_header\_ie\_rit::number\_of\_repeat\_listen](structieee802154__header__ie__rit.md#a5eaca9e09ebdbb933b4324c899c248b4)

uint8\_t number\_of\_repeat\_listen

**Definition** ieee802154\_ie.h:98

[ieee802154\_header\_ie\_rit::repeat\_listen\_interval](structieee802154__header__ie__rit.md#a73cd396d5e98799b655242f525ccf42b)

uint16\_t repeat\_listen\_interval

**Definition** ieee802154\_ie.h:99

[ieee802154\_header\_ie\_rit::time\_to\_first\_listen](structieee802154__header__ie__rit.md#a94efc1605d6799a9d88e6cb801f7ec0b)

uint8\_t time\_to\_first\_listen

**Definition** ieee802154\_ie.h:97

[ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md)

Time Correction IE, see section 7.4.2.7.

**Definition** ieee802154\_ie.h:128

[ieee802154\_header\_ie\_time\_correction::time\_sync\_info](structieee802154__header__ie__time__correction.md#a9ee84948740e66d1ee16786de5f38880)

uint16\_t time\_sync\_info

**Definition** ieee802154\_ie.h:129

[ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md)

Vendor Specific Header IE, see section 7.4.2.3.

**Definition** ieee802154\_ie.h:69

[ieee802154\_header\_ie\_vendor\_specific::vendor\_oui](structieee802154__header__ie__vendor__specific.md#a52d5ef47cbf674438bdc59aff40d0cbe)

uint8\_t vendor\_oui[IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN]

**Definition** ieee802154\_ie.h:70

[ieee802154\_header\_ie\_vendor\_specific::vendor\_specific\_info](structieee802154__header__ie__vendor__specific.md#a7227c96e07f5cd26353d10710d5a8db1)

uint8\_t \* vendor\_specific\_info

**Definition** ieee802154\_ie.h:71

[ieee802154\_header\_ie](structieee802154__header__ie.md)

**Definition** ieee802154\_ie.h:133

[ieee802154\_header\_ie::rit](structieee802154__header__ie.md#a0950703553d298a6af00cdb11012146c)

struct ieee802154\_header\_ie\_rit rit

**Definition** ieee802154\_ie.h:148

[ieee802154\_header\_ie::time\_correction](structieee802154__header__ie.md#a6a9c76df7d1e7b082642f10eeb4875af)

struct ieee802154\_header\_ie\_time\_correction time\_correction

**Definition** ieee802154\_ie.h:150

[ieee802154\_header\_ie::element\_id\_high](structieee802154__header__ie.md#a8521084dddda0853d3711d5b0dc1eada)

uint16\_t element\_id\_high

**Definition** ieee802154\_ie.h:143

[ieee802154\_header\_ie::length](structieee802154__header__ie.md#a9c1632eac7955370784445f5571d337d)

uint16\_t length

**Definition** ieee802154\_ie.h:141

[ieee802154\_header\_ie::type](structieee802154__header__ie.md#aa2c087927391e811437028c55141ce94)

uint16\_t type

**Definition** ieee802154\_ie.h:142

[ieee802154\_header\_ie::element\_id\_low](structieee802154__header__ie.md#ab389f739b6e6f77add4f77786f8c0577)

uint16\_t element\_id\_low

**Definition** ieee802154\_ie.h:140

[ieee802154\_header\_ie::content](structieee802154__header__ie.md#ac2d67fc001eddde667f25ebbf5ef5ce1)

union ieee802154\_header\_ie::@344013326214031274271343116205025343131166276172 content

[ieee802154\_header\_ie::vendor\_specific](structieee802154__header__ie.md#ac932f99fb3b93debde45e1f82d059cf8)

struct ieee802154\_header\_ie\_vendor\_specific vendor\_specific

**Definition** ieee802154\_ie.h:146

[ieee802154\_header\_ie::rendezvous\_time](structieee802154__header__ie.md#aecf96d749b103c1c5f702da675bacb26)

struct ieee802154\_header\_ie\_rendezvous\_time rendezvous\_time

**Definition** ieee802154\_ie.h:149

[ieee802154\_header\_ie::csl](structieee802154__header__ie.md#af73871d2a4c26d6e3cde0c18a74e7006)

struct ieee802154\_header\_ie\_csl csl

**Definition** ieee802154\_ie.h:147

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_ie.h](ieee802154__ie_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
