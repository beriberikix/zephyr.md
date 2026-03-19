---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/conn_8h_source.html
original_path: doxygen/html/conn_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn.h

[Go to the documentation of this file.](conn_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_CONN\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_CONN\_H\_

12

19

20#include <[stdbool.h](stdbool_8h.md)>

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

24#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

25#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

26#include <[zephyr/bluetooth/gap.h](gap_8h.md)>

27#include <[zephyr/bluetooth/direction.h](direction_8h.md)>

28#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

35struct bt\_conn;

36

[ 38](structbt__le__conn__param.md)struct [bt\_le\_conn\_param](structbt__le__conn__param.md) {

[ 39](structbt__le__conn__param.md#acd3b0a74402ca45402bab9ff54763e8d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__le__conn__param.md#acd3b0a74402ca45402bab9ff54763e8d);

[ 40](structbt__le__conn__param.md#a6d5a2662a5f22ccc26c992829d21f22d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__le__conn__param.md#a6d5a2662a5f22ccc26c992829d21f22d);

[ 41](structbt__le__conn__param.md#a3d21bd8363fa77dab83468ea319fef7d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__le__conn__param.md#a3d21bd8363fa77dab83468ea319fef7d);

[ 42](structbt__le__conn__param.md#ac06c16eb02e7a9d8b414db07e829178a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__conn__param.md#ac06c16eb02e7a9d8b414db07e829178a);

43};

44

[ 52](group__bt__conn.md#ga81de567c4c8cb691ef8b02633b42e342)#define BT\_LE\_CONN\_PARAM\_INIT(int\_min, int\_max, lat, to) \

53{ \

54 .interval\_min = (int\_min), \

55 .interval\_max = (int\_max), \

56 .latency = (lat), \

57 .timeout = (to), \

58}

59

[ 67](group__bt__conn.md#ga940d55c0d84c0cb8f09bc41074ae50d0)#define BT\_LE\_CONN\_PARAM(int\_min, int\_max, lat, to) \

68 ((struct bt\_le\_conn\_param[]) { \

69 BT\_LE\_CONN\_PARAM\_INIT(int\_min, int\_max, lat, to) \

70 })

71

[ 77](group__bt__conn.md#ga82df8f439aeb3a156f4238deb085534a)#define BT\_LE\_CONN\_PARAM\_DEFAULT BT\_LE\_CONN\_PARAM(BT\_GAP\_INIT\_CONN\_INT\_MIN, \

78 BT\_GAP\_INIT\_CONN\_INT\_MAX, \

79 0, 400)

80

[ 82](structbt__conn__le__phy__info.md)struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) {

[ 83](structbt__conn__le__phy__info.md#ac65912cc2a7997c0f886886783ea5b11) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_phy](structbt__conn__le__phy__info.md#ac65912cc2a7997c0f886886783ea5b11);

[ 84](structbt__conn__le__phy__info.md#abf029b63958d86eef7bf15218238783b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__conn__le__phy__info.md#abf029b63958d86eef7bf15218238783b);

85};

86

88enum {

[ 90](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98) [BT\_CONN\_LE\_PHY\_OPT\_NONE](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98) = 0,

91

[ 93](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34) [BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

94

[ 96](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0) [BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

97};

98

[ 100](structbt__conn__le__phy__param.md)struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) {

[ 101](structbt__conn__le__phy__param.md#a889dae2cdc2fba43f9f1194d26c4b737) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [options](structbt__conn__le__phy__param.md#a889dae2cdc2fba43f9f1194d26c4b737);

[ 102](structbt__conn__le__phy__param.md#ace64d2181ecc25ecdfa374f7f4bcf664) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pref\_tx\_phy](structbt__conn__le__phy__param.md#ace64d2181ecc25ecdfa374f7f4bcf664);

[ 103](structbt__conn__le__phy__param.md#a8d576bed5d9dfe9ca9a694d6d295afbc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pref\_rx\_phy](structbt__conn__le__phy__param.md#a8d576bed5d9dfe9ca9a694d6d295afbc);

104};

105

[ 111](group__bt__conn.md#gabca56de0c82c14995738952dafb1fe2d)#define BT\_CONN\_LE\_PHY\_PARAM\_INIT(\_pref\_tx\_phy, \_pref\_rx\_phy) \

112{ \

113 .options = BT\_CONN\_LE\_PHY\_OPT\_NONE, \

114 .pref\_tx\_phy = (\_pref\_tx\_phy), \

115 .pref\_rx\_phy = (\_pref\_rx\_phy), \

116}

117

[ 123](group__bt__conn.md#ga39b69f0978f74b5f13f829e908b7cebb)#define BT\_CONN\_LE\_PHY\_PARAM(\_pref\_tx\_phy, \_pref\_rx\_phy) \

124 ((struct bt\_conn\_le\_phy\_param []) { \

125 BT\_CONN\_LE\_PHY\_PARAM\_INIT(\_pref\_tx\_phy, \_pref\_rx\_phy) \

126 })

127

[ 129](group__bt__conn.md#ga3ec555bb4ace5e9c7c13735820fd31de)#define BT\_CONN\_LE\_PHY\_PARAM\_1M BT\_CONN\_LE\_PHY\_PARAM(BT\_GAP\_LE\_PHY\_1M, \

130 BT\_GAP\_LE\_PHY\_1M)

131

[ 133](group__bt__conn.md#ga633126e356658886e9fa3f3217cb4e2c)#define BT\_CONN\_LE\_PHY\_PARAM\_2M BT\_CONN\_LE\_PHY\_PARAM(BT\_GAP\_LE\_PHY\_2M, \

134 BT\_GAP\_LE\_PHY\_2M)

135

[ 137](group__bt__conn.md#ga4915244a6cd70995514d6dde1ee0b45f)#define BT\_CONN\_LE\_PHY\_PARAM\_CODED BT\_CONN\_LE\_PHY\_PARAM(BT\_GAP\_LE\_PHY\_CODED, \

138 BT\_GAP\_LE\_PHY\_CODED)

139

[ 141](group__bt__conn.md#ga02c9d7a04ccf2f043293aed7a7f767a7)#define BT\_CONN\_LE\_PHY\_PARAM\_ALL BT\_CONN\_LE\_PHY\_PARAM(BT\_GAP\_LE\_PHY\_1M | \

142 BT\_GAP\_LE\_PHY\_2M | \

143 BT\_GAP\_LE\_PHY\_CODED, \

144 BT\_GAP\_LE\_PHY\_1M | \

145 BT\_GAP\_LE\_PHY\_2M | \

146 BT\_GAP\_LE\_PHY\_CODED)

147

[ 149](structbt__conn__le__data__len__info.md)struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) {

[ 151](structbt__conn__le__data__len__info.md#a48d175f3c4b03dbdee129feae3edab23) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_max\_len](structbt__conn__le__data__len__info.md#a48d175f3c4b03dbdee129feae3edab23);

[ 153](structbt__conn__le__data__len__info.md#a14288429cbbcce2ef34580a581815eb7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_max\_time](structbt__conn__le__data__len__info.md#a14288429cbbcce2ef34580a581815eb7);

[ 155](structbt__conn__le__data__len__info.md#a18ddc603e922586e331187c9b29f2908) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_max\_len](structbt__conn__le__data__len__info.md#a18ddc603e922586e331187c9b29f2908);

[ 157](structbt__conn__le__data__len__info.md#af2316cdc921e9ec19491501e15248f73) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_max\_time](structbt__conn__le__data__len__info.md#af2316cdc921e9ec19491501e15248f73);

158};

159

[ 161](structbt__conn__le__data__len__param.md)struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) {

[ 163](structbt__conn__le__data__len__param.md#a8b279a0dc72c70aaf5205558fd4b4c4a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_max\_len](structbt__conn__le__data__len__param.md#a8b279a0dc72c70aaf5205558fd4b4c4a);

[ 165](structbt__conn__le__data__len__param.md#a9046542952fa822b944602b398562e6e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_max\_time](structbt__conn__le__data__len__param.md#a9046542952fa822b944602b398562e6e);

166};

167

[ 173](group__bt__conn.md#ga98f9dab71897382cf1187259a3b5660e)#define BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT(\_tx\_max\_len, \_tx\_max\_time) \

174{ \

175 .tx\_max\_len = (\_tx\_max\_len), \

176 .tx\_max\_time = (\_tx\_max\_time), \

177}

178

[ 184](group__bt__conn.md#ga102b97de8689fe3fb53f9691009de87f)#define BT\_CONN\_LE\_DATA\_LEN\_PARAM(\_tx\_max\_len, \_tx\_max\_time) \

185 ((struct bt\_conn\_le\_data\_len\_param[]) { \

186 BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT(\_tx\_max\_len, \_tx\_max\_time) \

187 })

188

[ 190](group__bt__conn.md#gaf66746d834f7556dc77659741e27e0c9)#define BT\_LE\_DATA\_LEN\_PARAM\_DEFAULT \

191 BT\_CONN\_LE\_DATA\_LEN\_PARAM(BT\_GAP\_DATA\_LEN\_DEFAULT, \

192 BT\_GAP\_DATA\_TIME\_DEFAULT)

193

[ 195](group__bt__conn.md#ga9cc26afda3c507cb5439184fedcd61ba)#define BT\_LE\_DATA\_LEN\_PARAM\_MAX \

196 BT\_CONN\_LE\_DATA\_LEN\_PARAM(BT\_GAP\_DATA\_LEN\_MAX, \

197 BT\_GAP\_DATA\_TIME\_MAX)

198

[ 200](structbt__conn__le__subrate__param.md)struct [bt\_conn\_le\_subrate\_param](structbt__conn__le__subrate__param.md) {

[ 202](structbt__conn__le__subrate__param.md#aef75fec8ba8c9987d55e81aa2539b96e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_min](structbt__conn__le__subrate__param.md#aef75fec8ba8c9987d55e81aa2539b96e);

[ 204](structbt__conn__le__subrate__param.md#a59d2d244e3568b8f97ce936121d41b1a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subrate\_max](structbt__conn__le__subrate__param.md#a59d2d244e3568b8f97ce936121d41b1a);

[ 206](structbt__conn__le__subrate__param.md#a15d05324708ddeea8d2f3515eea396bb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_latency](structbt__conn__le__subrate__param.md#a15d05324708ddeea8d2f3515eea396bb);

[ 211](structbt__conn__le__subrate__param.md#a978cef5f2f14a5a7fe7ded09c6fdf2d9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [continuation\_number](structbt__conn__le__subrate__param.md#a978cef5f2f14a5a7fe7ded09c6fdf2d9);

[ 216](structbt__conn__le__subrate__param.md#aca0897d00a1dd1735dbbaf5bfde711ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__conn__le__subrate__param.md#aca0897d00a1dd1735dbbaf5bfde711ed);

217};

218

[ 220](structbt__conn__le__subrating__info.md)struct [bt\_conn\_le\_subrating\_info](structbt__conn__le__subrating__info.md) {

[ 222](structbt__conn__le__subrating__info.md#a23736535309f38695a2e432c5c80bbe1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [factor](structbt__conn__le__subrating__info.md#a23736535309f38695a2e432c5c80bbe1);

[ 227](structbt__conn__le__subrating__info.md#a0a6d1eae73f76382f1a9415c01761c19) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [continuation\_number](structbt__conn__le__subrating__info.md#a0a6d1eae73f76382f1a9415c01761c19);

228};

229

[ 231](structbt__conn__le__subrate__changed.md)struct [bt\_conn\_le\_subrate\_changed](structbt__conn__le__subrate__changed.md) {

[ 236](structbt__conn__le__subrate__changed.md#afc5a577dadf41819e89bc3af016ce258) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__conn__le__subrate__changed.md#afc5a577dadf41819e89bc3af016ce258);

[ 238](structbt__conn__le__subrate__changed.md#a0c3e3dc41ca4dec92740c920e959060b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [factor](structbt__conn__le__subrate__changed.md#a0c3e3dc41ca4dec92740c920e959060b);

[ 243](structbt__conn__le__subrate__changed.md#a2420a0a3145471c6a1a618bea8d1d7c6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [continuation\_number](structbt__conn__le__subrate__changed.md#a2420a0a3145471c6a1a618bea8d1d7c6);

[ 245](structbt__conn__le__subrate__changed.md#aa0bab070bc43972dfb3a5259934b4931) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [peripheral\_latency](structbt__conn__le__subrate__changed.md#aa0bab070bc43972dfb3a5259934b4931);

[ 247](structbt__conn__le__subrate__changed.md#aab0cb08a7549401684bcab3c291dc192) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [supervision\_timeout](structbt__conn__le__subrate__changed.md#aab0cb08a7549401684bcab3c291dc192);

248};

249

[ 251](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20)enum \_\_packed [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) {

[ 253](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) [BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 255](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) [BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 257](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) [BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 259](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee) [BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 261](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836) [BT\_CONN\_TYPE\_ALL](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836) = [BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) | [BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) |

262 [BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) | [BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee),

263};

264

[ 266](group__bt__conn.md#gafe14d64a64383b097760764697b035e2)enum [bt\_conn\_le\_cs\_capability\_rtt\_aa\_only](group__bt__conn.md#gafe14d64a64383b097760764697b035e2) {

[ 268](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94) [BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_NOT\_SUPP](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94) = 0,

[ 270](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a) [BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_10NS](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a),

[ 272](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6) [BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_150NS](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6),

273};

274

[ 276](group__bt__conn.md#ga1892ec23ca3b1818287a9d7dafc16433)enum [bt\_conn\_le\_cs\_capability\_rtt\_sounding](group__bt__conn.md#ga1892ec23ca3b1818287a9d7dafc16433) {

[ 278](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14) [BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_NOT\_SUPP](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14) = 0,

[ 280](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb) [BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_10NS](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb),

[ 282](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584) [BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_150NS](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584),

283};

284

[ 286](group__bt__conn.md#ga5568443825fc1ce9534753d8918aa813)enum [bt\_conn\_le\_cs\_capability\_rtt\_random\_payload](group__bt__conn.md#ga5568443825fc1ce9534753d8918aa813) {

[ 288](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d) [BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_NOT\_SUPP](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d) = 0,

[ 290](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741) [BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_10NS](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741),

[ 292](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db) [BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_150NS](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db),

293};

294

[ 296](structbt__conn__le__cs__capabilities.md)struct [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md) {

[ 298](structbt__conn__le__cs__capabilities.md#a77aacfd02b354e04d4cc29cc1bf4b779) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_config\_supported](structbt__conn__le__cs__capabilities.md#a77aacfd02b354e04d4cc29cc1bf4b779);

[ 304](structbt__conn__le__cs__capabilities.md#ae76fbc0f88525e83717e1d8ef5acae59) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_consecutive\_procedures\_supported](structbt__conn__le__cs__capabilities.md#ae76fbc0f88525e83717e1d8ef5acae59);

[ 306](structbt__conn__le__cs__capabilities.md#a4e4c56c5066d02b2a0cd59c067f1e4b9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antennas\_supported](structbt__conn__le__cs__capabilities.md#a4e4c56c5066d02b2a0cd59c067f1e4b9);

[ 308](structbt__conn__le__cs__capabilities.md#ac842e123166008ad1ad663f827937a3b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_antenna\_paths\_supported](structbt__conn__le__cs__capabilities.md#ac842e123166008ad1ad663f827937a3b);

[ 310](structbt__conn__le__cs__capabilities.md#a6530d2a3fb66d498711856b723acecb7) bool [initiator\_supported](structbt__conn__le__cs__capabilities.md#a6530d2a3fb66d498711856b723acecb7);

[ 312](structbt__conn__le__cs__capabilities.md#a694119619d359d0b7e298edf6201ee20) bool [reflector\_supported](structbt__conn__le__cs__capabilities.md#a694119619d359d0b7e298edf6201ee20);

[ 314](structbt__conn__le__cs__capabilities.md#aa1616417e6183cf283cf96efc9a92b8e) bool [mode\_3\_supported](structbt__conn__le__cs__capabilities.md#aa1616417e6183cf283cf96efc9a92b8e);

[ 316](structbt__conn__le__cs__capabilities.md#a46c9168328d3fbc98a2625799c733818) enum [bt\_conn\_le\_cs\_capability\_rtt\_aa\_only](group__bt__conn.md#gafe14d64a64383b097760764697b035e2) [rtt\_aa\_only\_precision](structbt__conn__le__cs__capabilities.md#a46c9168328d3fbc98a2625799c733818);

[ 318](structbt__conn__le__cs__capabilities.md#acef0d65ed55ae304fea47006bfb0076f) enum [bt\_conn\_le\_cs\_capability\_rtt\_sounding](group__bt__conn.md#ga1892ec23ca3b1818287a9d7dafc16433) [rtt\_sounding\_precision](structbt__conn__le__cs__capabilities.md#acef0d65ed55ae304fea47006bfb0076f);

[ 320](structbt__conn__le__cs__capabilities.md#abbefdc0268a775712c7abd664adcb6b2) enum [bt\_conn\_le\_cs\_capability\_rtt\_random\_payload](group__bt__conn.md#ga5568443825fc1ce9534753d8918aa813) [rtt\_random\_payload\_precision](structbt__conn__le__cs__capabilities.md#abbefdc0268a775712c7abd664adcb6b2);

[ 326](structbt__conn__le__cs__capabilities.md#abe3c611316bb5f710f355846ee9ec437) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_aa\_only\_n](structbt__conn__le__cs__capabilities.md#abe3c611316bb5f710f355846ee9ec437);

[ 332](structbt__conn__le__cs__capabilities.md#a7f35343a1572800850e791ba3ff5ffb1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_sounding\_n](structbt__conn__le__cs__capabilities.md#a7f35343a1572800850e791ba3ff5ffb1);

[ 338](structbt__conn__le__cs__capabilities.md#a345d9e43222d77024a8f4283b274b48f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtt\_random\_payload\_n](structbt__conn__le__cs__capabilities.md#a345d9e43222d77024a8f4283b274b48f);

[ 342](structbt__conn__le__cs__capabilities.md#a94fd00a7a9b22d649f75c7fdd17590a9) bool [phase\_based\_nadm\_sounding\_supported](structbt__conn__le__cs__capabilities.md#a94fd00a7a9b22d649f75c7fdd17590a9);

[ 346](structbt__conn__le__cs__capabilities.md#a1a0076a0c97317803976f4aca86afc0d) bool [phase\_based\_nadm\_random\_supported](structbt__conn__le__cs__capabilities.md#a1a0076a0c97317803976f4aca86afc0d);

[ 348](structbt__conn__le__cs__capabilities.md#a3fd09db5fae9c5e307994a78131199c6) bool [cs\_sync\_2m\_phy\_supported](structbt__conn__le__cs__capabilities.md#a3fd09db5fae9c5e307994a78131199c6);

[ 350](structbt__conn__le__cs__capabilities.md#a6513d8ffe7d168441205f6dd656dcbbc) bool [cs\_sync\_2m\_2bt\_phy\_supported](structbt__conn__le__cs__capabilities.md#a6513d8ffe7d168441205f6dd656dcbbc);

[ 352](structbt__conn__le__cs__capabilities.md#a22604c052da2f8ccf77c81a0a5c628b7) bool [cs\_without\_fae\_supported](structbt__conn__le__cs__capabilities.md#a22604c052da2f8ccf77c81a0a5c628b7);

[ 354](structbt__conn__le__cs__capabilities.md#aba0db15183d4fa4ae0e3f1333202e55e) bool [chsel\_alg\_3c\_supported](structbt__conn__le__cs__capabilities.md#aba0db15183d4fa4ae0e3f1333202e55e);

[ 356](structbt__conn__le__cs__capabilities.md#ad57f15b4dda88e2b747f30451601c923) bool [pbr\_from\_rtt\_sounding\_seq\_supported](structbt__conn__le__cs__capabilities.md#ad57f15b4dda88e2b747f30451601c923);

[ 367](structbt__conn__le__cs__capabilities.md#a090f869cfe7e39a70cea94afbd5ac376) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip1\_times\_supported](structbt__conn__le__cs__capabilities.md#a090f869cfe7e39a70cea94afbd5ac376);

[ 378](structbt__conn__le__cs__capabilities.md#ae93594f360430e9c0c80cf3edcf570f6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ip2\_times\_supported](structbt__conn__le__cs__capabilities.md#ae93594f360430e9c0c80cf3edcf570f6);

[ 391](structbt__conn__le__cs__capabilities.md#a1ff1d7d769e3ba915f91bf672a6f8a61) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_fcs\_times\_supported](structbt__conn__le__cs__capabilities.md#a1ff1d7d769e3ba915f91bf672a6f8a61);

[ 397](structbt__conn__le__cs__capabilities.md#a6e92391b21d4acaebba8a171643f572f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_pm\_times\_supported](structbt__conn__le__cs__capabilities.md#a6e92391b21d4acaebba8a171643f572f);

[ 399](structbt__conn__le__cs__capabilities.md#a5a86629a5ad4203b5efe3802cd8b6ae7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_sw\_time](structbt__conn__le__cs__capabilities.md#a5a86629a5ad4203b5efe3802cd8b6ae7);

[ 408](structbt__conn__le__cs__capabilities.md#ad58deea7a825bb5f0bc2ca0034183948) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_snr\_capability](structbt__conn__le__cs__capabilities.md#ad58deea7a825bb5f0bc2ca0034183948);

409};

410

[ 412](structbt__conn__le__cs__fae__table.md)struct [bt\_conn\_le\_cs\_fae\_table](structbt__conn__le__cs__fae__table.md) {

[ 413](structbt__conn__le__cs__fae__table.md#a88edb4769f68966347b08afa354d9d41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[remote\_fae\_table](structbt__conn__le__cs__fae__table.md#a88edb4769f68966347b08afa354d9d41);

414};

415

[ 417](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f)enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) {

[ 419](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fa206d9eebf020d9743767b66a5f5a023d) [BT\_CONN\_LE\_CS\_MAIN\_MODE\_1](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fa206d9eebf020d9743767b66a5f5a023d) = [BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1](hci__types_8h.md#af1b7924e50ba017e59d697fd8814d491),

[ 421](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fa5a60c772a06c6f8925344dac63f592c6) [BT\_CONN\_LE\_CS\_MAIN\_MODE\_2](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fa5a60c772a06c6f8925344dac63f592c6) = [BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2](hci__types_8h.md#a714152a085bbc317b539d6e973ccffc6),

[ 423](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fafebd88560cfcce6ba2eb48976e220c4a) [BT\_CONN\_LE\_CS\_MAIN\_MODE\_3](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fafebd88560cfcce6ba2eb48976e220c4a) = [BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3](hci__types_8h.md#a5d2af0ed5e0cc5cf7d9f0baae512ff68),

424};

425

[ 427](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf)enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) {

[ 429](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafac1b24ef35efc9222771f45422b2e8f24) [BT\_CONN\_LE\_CS\_SUB\_MODE\_UNUSED](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafac1b24ef35efc9222771f45422b2e8f24) = [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED](hci__types_8h.md#ab3fce1eb448b0ade581e4e12b2d56039),

[ 431](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafaf23b70be00b04f15fe9b38190e26b49c) [BT\_CONN\_LE\_CS\_SUB\_MODE\_1](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafaf23b70be00b04f15fe9b38190e26b49c) = [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1](hci__types_8h.md#a219243d501bbcb6d62668398cde79fca),

[ 433](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafaf894463ad77a424ddba3d5f4edfdd3e8) [BT\_CONN\_LE\_CS\_SUB\_MODE\_2](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafaf894463ad77a424ddba3d5f4edfdd3e8) = [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2](hci__types_8h.md#ada09c787fca0a1d54bb754635489b51e),

[ 435](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafa132f05ddbf885086e7bee500608d8797) [BT\_CONN\_LE\_CS\_SUB\_MODE\_3](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafa132f05ddbf885086e7bee500608d8797) = [BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3](hci__types_8h.md#a4b48c199b6b75e9dd62ec36883b40aa4),

436};

437

[ 439](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f)enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) {

[ 441](group__bt__conn.md#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4) [BT\_CONN\_LE\_CS\_ROLE\_INITIATOR](group__bt__conn.md#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4),

[ 443](group__bt__conn.md#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968) [BT\_CONN\_LE\_CS\_ROLE\_REFLECTOR](group__bt__conn.md#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968),

444};

445

[ 447](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51)enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) {

[ 449](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_AA\_ONLY](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY](hci__types_8h.md#a759eb7a8e43ee7cf1ea88ddd3e69feb5),

[ 451](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_SOUNDING](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND](hci__types_8h.md#aa2ae18252a20ef3481d2402f8924cdda),

[ 453](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_SOUNDING](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND](hci__types_8h.md#a73cbfe2a942b684ac0b5b50d900fb83f),

[ 455](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND](hci__types_8h.md#abe4efee7cf9371129f4b5bd650b0d64a),

[ 457](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_64\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND](hci__types_8h.md#a77e56fd5302673f6ef295c0cceabdc9f),

[ 459](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND](hci__types_8h.md#aa60f64ff7259fd79fb1da2c063530348),

[ 461](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5) [BT\_CONN\_LE\_CS\_RTT\_TYPE\_128\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5) = [BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND](hci__types_8h.md#a1fe5e94fbd1156c8196c8e1ab9816bac),

462};

463

[ 465](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb)enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) {

[ 467](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95) [BT\_CONN\_LE\_CS\_SYNC\_1M\_PHY](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95) = [BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M](hci__types_8h.md#a7baf90f5bf691ce6b650677e6c2a9600),

[ 469](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6) [BT\_CONN\_LE\_CS\_SYNC\_2M\_PHY](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6) = [BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M](hci__types_8h.md#ae49d35db87532e06ea685a63eb89177a),

[ 471](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b) [BT\_CONN\_LE\_CS\_SYNC\_2M\_2BT\_PHY](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b) = [BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT](hci__types_8h.md#ac34716156b071e06eb454f091a63216c),

472};

473

[ 475](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0)enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) {

[ 477](group__bt__conn.md#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1) [BT\_CONN\_LE\_CS\_CHSEL\_TYPE\_3B](group__bt__conn.md#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1) = [BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B](hci__types_8h.md#a77d27762b9faa7743a55d822a1839eac),

[ 479](group__bt__conn.md#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6) [BT\_CONN\_LE\_CS\_CHSEL\_TYPE\_3C](group__bt__conn.md#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6) = [BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C](hci__types_8h.md#af17f867204bc7cf99e5d530c39302be0),

480};

481

[ 483](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b)enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) {

[ 485](group__bt__conn.md#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea) [BT\_CONN\_LE\_CS\_CH3C\_SHAPE\_HAT](group__bt__conn.md#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea) = [BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT](hci__types_8h.md#acd33fc2eb3f5ebe10cbe4c5060f8336b),

[ 487](group__bt__conn.md#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622) [BT\_CONN\_LE\_CS\_CH3C\_SHAPE\_X](group__bt__conn.md#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622) = [BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X](hci__types_8h.md#ad09c735ab352d7a546cade296e915e85),

488};

489

[ 491](structbt__conn__le__cs__config.md)struct [bt\_conn\_le\_cs\_config](structbt__conn__le__cs__config.md) {

[ 493](structbt__conn__le__cs__config.md#aaf8f1ce04fd22b4ca4728bdcfce8bd4a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__conn__le__cs__config.md#aaf8f1ce04fd22b4ca4728bdcfce8bd4a);

[ 495](structbt__conn__le__cs__config.md#a02b942d1def46476160ba8839ca9690f) enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) [main\_mode\_type](structbt__conn__le__cs__config.md#a02b942d1def46476160ba8839ca9690f);

[ 497](structbt__conn__le__cs__config.md#a4ee4bf79283686e16d4737f546718c44) enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) [sub\_mode\_type](structbt__conn__le__cs__config.md#a4ee4bf79283686e16d4737f546718c44);

[ 499](structbt__conn__le__cs__config.md#a2e59fb17cd932b7670b3e915684c2107) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_main\_mode\_steps](structbt__conn__le__cs__config.md#a2e59fb17cd932b7670b3e915684c2107);

[ 501](structbt__conn__le__cs__config.md#aff70b37fac8a3bd94acb25d7bd06989b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_main\_mode\_steps](structbt__conn__le__cs__config.md#aff70b37fac8a3bd94acb25d7bd06989b);

[ 506](structbt__conn__le__cs__config.md#a2e904438c579870ed96b5dccff239c18) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [main\_mode\_repetition](structbt__conn__le__cs__config.md#a2e904438c579870ed96b5dccff239c18);

[ 508](structbt__conn__le__cs__config.md#a8eea68bffef759b4532b68a1ecbdd4f1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode\_0\_steps](structbt__conn__le__cs__config.md#a8eea68bffef759b4532b68a1ecbdd4f1);

[ 510](structbt__conn__le__cs__config.md#ad11f8bee028ad3eb59008d46dce2d5bd) enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) [role](structbt__conn__le__cs__config.md#ad11f8bee028ad3eb59008d46dce2d5bd);

[ 512](structbt__conn__le__cs__config.md#a194e3844373c57e714917d03ac82666d) enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) [rtt\_type](structbt__conn__le__cs__config.md#a194e3844373c57e714917d03ac82666d);

[ 514](structbt__conn__le__cs__config.md#a2051f559b41085c4b41743aaaaecf3a1) enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) [cs\_sync\_phy](structbt__conn__le__cs__config.md#a2051f559b41085c4b41743aaaaecf3a1);

[ 518](structbt__conn__le__cs__config.md#a971ff7ba734dd71512af7f3850de364d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map\_repetition](structbt__conn__le__cs__config.md#a971ff7ba734dd71512af7f3850de364d);

[ 520](structbt__conn__le__cs__config.md#a63b7027929a5c3ec7fd68f35343262ee) enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) [channel\_selection\_type](structbt__conn__le__cs__config.md#a63b7027929a5c3ec7fd68f35343262ee);

[ 522](structbt__conn__le__cs__config.md#a9b64ecb0986e7e9995c29feaf105eeaa) enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) [ch3c\_shape](structbt__conn__le__cs__config.md#a9b64ecb0986e7e9995c29feaf105eeaa);

[ 524](structbt__conn__le__cs__config.md#afa2846689f1a9d5b9e124b1c9095154f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch3c\_jump](structbt__conn__le__cs__config.md#afa2846689f1a9d5b9e124b1c9095154f);

[ 526](structbt__conn__le__cs__config.md#aab9a1d8d09d7a439f1c4dd28b9dd05c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip1\_time\_us](structbt__conn__le__cs__config.md#aab9a1d8d09d7a439f1c4dd28b9dd05c4);

[ 528](structbt__conn__le__cs__config.md#a8e650b50400a45040c02a88dfb30683c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_ip2\_time\_us](structbt__conn__le__cs__config.md#a8e650b50400a45040c02a88dfb30683c);

[ 530](structbt__conn__le__cs__config.md#a29912bd291fa4da09bb5b196d747ca6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_fcs\_time\_us](structbt__conn__le__cs__config.md#a29912bd291fa4da09bb5b196d747ca6b);

[ 532](structbt__conn__le__cs__config.md#ae7f1cc232df00b4543fdb2b2596b9bbf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t\_pm\_time\_us](structbt__conn__le__cs__config.md#ae7f1cc232df00b4543fdb2b2596b9bbf);

[ 538](structbt__conn__le__cs__config.md#a60f9d21629554d47556d0fe8d63dcae3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_map](structbt__conn__le__cs__config.md#a60f9d21629554d47556d0fe8d63dcae3)[10];

539};

540

[ 542](group__bt__conn.md#ga9a1dc2010c5237466de87160944630d3)enum [bt\_conn\_le\_cs\_procedure\_done\_status](group__bt__conn.md#ga9a1dc2010c5237466de87160944630d3) {

[ 543](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f) [BT\_CONN\_LE\_CS\_PROCEDURE\_COMPLETE](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f) = [BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE](hci__types_8h.md#ace872d54fba6d94d62b59a2373c7d0d5),

[ 544](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82) [BT\_CONN\_LE\_CS\_PROCEDURE\_INCOMPLETE](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82) = [BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL](hci__types_8h.md#af057e8492e52d0c8763d4a2e969d949d),

[ 545](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b) [BT\_CONN\_LE\_CS\_PROCEDURE\_ABORTED](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b) = [BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED](hci__types_8h.md#a821a29dacea9867e4e576f916cf7be3d),

546};

547

[ 549](group__bt__conn.md#ga8e54a191b889b1d5ed3e1fbb648d9bc7)enum [bt\_conn\_le\_cs\_subevent\_done\_status](group__bt__conn.md#ga8e54a191b889b1d5ed3e1fbb648d9bc7) {

[ 550](group__bt__conn.md#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146) [BT\_CONN\_LE\_CS\_SUBEVENT\_COMPLETE](group__bt__conn.md#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146) = [BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE](hci__types_8h.md#aee251ce3c46dc0404d880be7d4550fa6),

[ 551](group__bt__conn.md#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202) [BT\_CONN\_LE\_CS\_SUBEVENT\_ABORTED](group__bt__conn.md#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202) = [BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED](hci__types_8h.md#af1907f8ae481a08c674d86e689826f49),

552};

553

[ 555](group__bt__conn.md#ga3196a0eb1c7497e93d7c646713d2fc79)enum [bt\_conn\_le\_cs\_procedure\_abort\_reason](group__bt__conn.md#ga3196a0eb1c7497e93d7c646713d2fc79) {

[ 556](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d) [BT\_CONN\_LE\_CS\_PROCEDURE\_NOT\_ABORTED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d) = [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT](hci__types_8h.md#a056a67d663cfdc2189b480fc79946c74),

[ 557](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0) [BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_REQUESTED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0) =

558 [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST](hci__types_8h.md#a21eb191c5d99f902c7a244cad685995f),

[ 559](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02) [BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_TOO\_FEW\_CHANNELS](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02) =

560 [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS](hci__types_8h.md#a6dc3f766ce40bbd0ddb7af3cf85677b1),

[ 561](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744) [BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_CHMAP\_INSTANT\_PASSED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744) =

562 [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED](hci__types_8h.md#ae8446a2638bd4009b7dee725bb54c883),

[ 563](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886) [BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_UNSPECIFIED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886) = [BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED](hci__types_8h.md#a1e92177f7be3c6a6be00f97fbfc17dcf),

564};

565

[ 567](group__bt__conn.md#ga6394906c6da40c9bebfaeb05de9fd5be)enum [bt\_conn\_le\_cs\_subevent\_abort\_reason](group__bt__conn.md#ga6394906c6da40c9bebfaeb05de9fd5be) {

[ 568](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c) [BT\_CONN\_LE\_CS\_SUBEVENT\_NOT\_ABORTED](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c) = [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT](hci__types_8h.md#a095b6061c31229b951b6b96e5d02381f),

[ 569](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d) [BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_REQUESTED](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d) =

570 [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST](hci__types_8h.md#a41bbe08db99fb0a2ef77f4f3103f9b6c),

[ 571](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d) [BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_NO\_CS\_SYNC](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d) =

572 [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED](hci__types_8h.md#ac4817c265c50019d8f74146f7477bf58),

[ 573](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd) [BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_SCHED\_CONFLICT](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd) =

574 [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT](hci__types_8h.md#a31cb520a05fe31313bacf8b021da468c),

[ 575](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3) [BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_UNSPECIFIED](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3) = [BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED](hci__types_8h.md#abfdca3ae615e19c8e24c098ba8349618),

576};

577

[ 579](structbt__conn__le__cs__subevent__result.md)struct [bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md) {

580 struct {

[ 588](structbt__conn__le__cs__subevent__result.md#aa4c770ab2db8d4ab665ad50f7edd5bfa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__conn__le__cs__subevent__result.md#aa4c770ab2db8d4ab665ad50f7edd5bfa);

[ 594](structbt__conn__le__cs__subevent__result.md#a7706d0dfd7246d4cf193a8a9e7b6305d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_acl\_conn\_event](structbt__conn__le__cs__subevent__result.md#a7706d0dfd7246d4cf193a8a9e7b6305d);

[ 600](structbt__conn__le__cs__subevent__result.md#a0f8fc918f8eb31c47acf51885c7add08) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [procedure\_counter](structbt__conn__le__cs__subevent__result.md#a0f8fc918f8eb31c47acf51885c7add08);

[ 609](structbt__conn__le__cs__subevent__result.md#a967d37f37d0e1596984fdda34609a3b3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [frequency\_compensation](structbt__conn__le__cs__subevent__result.md#a967d37f37d0e1596984fdda34609a3b3);

[ 617](structbt__conn__le__cs__subevent__result.md#acbfc5e80a2fb82072d9376e996f7969f) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [reference\_power\_level](structbt__conn__le__cs__subevent__result.md#acbfc5e80a2fb82072d9376e996f7969f);

[ 619](structbt__conn__le__cs__subevent__result.md#adf60893d9229003d1eefc552a4957b65) enum [bt\_conn\_le\_cs\_procedure\_done\_status](group__bt__conn.md#ga9a1dc2010c5237466de87160944630d3) [procedure\_done\_status](structbt__conn__le__cs__subevent__result.md#adf60893d9229003d1eefc552a4957b65);

[ 633](structbt__conn__le__cs__subevent__result.md#a45b22c6c2252e2afa28ee8b1bfed3ecf) enum [bt\_conn\_le\_cs\_subevent\_done\_status](group__bt__conn.md#ga8e54a191b889b1d5ed3e1fbb648d9bc7) [subevent\_done\_status](structbt__conn__le__cs__subevent__result.md#a45b22c6c2252e2afa28ee8b1bfed3ecf);

[ 640](structbt__conn__le__cs__subevent__result.md#a778c89f57ef50f612654243ba673ba3f) enum [bt\_conn\_le\_cs\_procedure\_abort\_reason](group__bt__conn.md#ga3196a0eb1c7497e93d7c646713d2fc79) [procedure\_abort\_reason](structbt__conn__le__cs__subevent__result.md#a778c89f57ef50f612654243ba673ba3f);

[ 647](structbt__conn__le__cs__subevent__result.md#aef5ba53497c4d1576c9ecec1b5dea289) enum [bt\_conn\_le\_cs\_subevent\_abort\_reason](group__bt__conn.md#ga6394906c6da40c9bebfaeb05de9fd5be) [subevent\_abort\_reason](structbt__conn__le__cs__subevent__result.md#aef5ba53497c4d1576c9ecec1b5dea289);

[ 650](structbt__conn__le__cs__subevent__result.md#a3597697ae4acdd8f7c009bececab6a65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_antenna\_paths](structbt__conn__le__cs__subevent__result.md#a3597697ae4acdd8f7c009bececab6a65);

[ 653](structbt__conn__le__cs__subevent__result.md#a3bffc0935a5410d75d0050337e4fad27) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_steps\_reported](structbt__conn__le__cs__subevent__result.md#a3bffc0935a5410d75d0050337e4fad27);

[ 658](structbt__conn__le__cs__subevent__result.md#a9bfcc6dcaa191c7f56958ef88926b51e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [abort\_step](structbt__conn__le__cs__subevent__result.md#a9bfcc6dcaa191c7f56958ef88926b51e);

[ 659](structbt__conn__le__cs__subevent__result.md#a1a90563a8c93f9b309e88fd771a7cec4) } [header](structbt__conn__le__cs__subevent__result.md#a1a90563a8c93f9b309e88fd771a7cec4);

[ 660](structbt__conn__le__cs__subevent__result.md#a6948c4a8c5882cb1d1b04a2b390fda8c) struct [net\_buf\_simple](structnet__buf__simple.md) \*[step\_data\_buf](structbt__conn__le__cs__subevent__result.md#a6948c4a8c5882cb1d1b04a2b390fda8c);

661};

662

[ 674](group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c)struct bt\_conn \*[bt\_conn\_ref](group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c)(struct bt\_conn \*conn);

675

[ 682](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6)void [bt\_conn\_unref](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6)(struct bt\_conn \*conn);

683

[ 700](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916)void [bt\_conn\_foreach](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916)(enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) type,

701 void (\*func)(struct bt\_conn \*conn, void \*data),

702 void \*data);

703

[ 716](group__bt__conn.md#ga1bfe349efd8a7de31e9457fe439d746a)struct bt\_conn \*[bt\_conn\_lookup\_addr\_le](group__bt__conn.md#ga1bfe349efd8a7de31e9457fe439d746a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer);

717

[ 724](group__bt__conn.md#ga77108581b8f61485ca840e4bf7a17087)const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[bt\_conn\_get\_dst](group__bt__conn.md#ga77108581b8f61485ca840e4bf7a17087)(const struct bt\_conn \*conn);

725

[ 736](group__bt__conn.md#gad4aed76b80cc815f748ad0e84ae3d87c)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_conn\_index](group__bt__conn.md#gad4aed76b80cc815f748ad0e84ae3d87c)(const struct bt\_conn \*conn);

737

[ 739](structbt__conn__le__info.md)struct [bt\_conn\_le\_info](structbt__conn__le__info.md) {

[ 741](structbt__conn__le__info.md#a5f1eacec82f31182460d6d5359a8b295) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[src](structbt__conn__le__info.md#a5f1eacec82f31182460d6d5359a8b295);

[ 745](structbt__conn__le__info.md#a1f78e1c0ed3482ce6eec9ce6eeda4769) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[dst](structbt__conn__le__info.md#a1f78e1c0ed3482ce6eec9ce6eeda4769);

[ 747](structbt__conn__le__info.md#a3be5df0deb0af08f84843eb3c6a5e5ae) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[local](structbt__conn__le__info.md#a3be5df0deb0af08f84843eb3c6a5e5ae);

[ 749](structbt__conn__le__info.md#a236d1c97c735c7cfaead0b1a3672d512) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[remote](structbt__conn__le__info.md#a236d1c97c735c7cfaead0b1a3672d512);

[ 750](structbt__conn__le__info.md#a95a1f635e53f16d5839cdd58f4bda962) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__conn__le__info.md#a95a1f635e53f16d5839cdd58f4bda962);

[ 751](structbt__conn__le__info.md#acd83835fe5ec0878fd653b87cb570a49) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__conn__le__info.md#acd83835fe5ec0878fd653b87cb570a49);

[ 752](structbt__conn__le__info.md#afb4dc594d063fbbad2bcd4acf047f716) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__conn__le__info.md#afb4dc594d063fbbad2bcd4acf047f716);

753

754#if defined(CONFIG\_BT\_USER\_PHY\_UPDATE)

[ 755](structbt__conn__le__info.md#a215d39c6cd7da1ac033529b5541cbfc1) const struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \*[phy](structbt__conn__le__info.md#a215d39c6cd7da1ac033529b5541cbfc1);

756#endif /\* defined(CONFIG\_BT\_USER\_PHY\_UPDATE) \*/

757

758#if defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE)

759 /\* Connection maximum single fragment parameters \*/

[ 760](structbt__conn__le__info.md#ae309f390c8d7b33a4de55791af235ab0) const struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \*[data\_len](structbt__conn__le__info.md#ae309f390c8d7b33a4de55791af235ab0);

761#endif /\* defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE) \*/

762

763#if defined(CONFIG\_BT\_SUBRATING)

764 /\* Connection subrating parameters \*/

765 const struct [bt\_conn\_le\_subrating\_info](structbt__conn__le__subrating__info.md) \*subrate;

766#endif /\* defined(CONFIG\_BT\_SUBRATING) \*/

767};

768

[ 776](group__bt__conn.md#ga707cc62b12c89478aebd0488a464a776)#define BT\_CONN\_INTERVAL\_TO\_MS(interval) ((interval) \* 5U / 4U)

777

[ 782](group__bt__conn.md#ga0a5fac126005684847ee7509bb98e382)#define BT\_CONN\_INTERVAL\_TO\_US(interval) ((interval) \* 1250U)

783

[ 785](structbt__conn__br__info.md)struct [bt\_conn\_br\_info](structbt__conn__br__info.md) {

[ 786](structbt__conn__br__info.md#aeef49f711872ccfec5dd558c4552b71e) const [bt\_addr\_t](structbt__addr__t.md) \*[dst](structbt__conn__br__info.md#aeef49f711872ccfec5dd558c4552b71e);

787};

788

789enum {

[ 790](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) [BT\_CONN\_ROLE\_CENTRAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) = 0,

[ 791](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) [BT\_CONN\_ROLE\_PERIPHERAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) = 1,

792};

793

[ 794](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282)enum [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) {

[ 796](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587) [BT\_CONN\_STATE\_DISCONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587),

[ 798](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd) [BT\_CONN\_STATE\_CONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd),

[ 800](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f) [BT\_CONN\_STATE\_CONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f),

[ 802](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f) [BT\_CONN\_STATE\_DISCONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f),

803};

804

[ 806](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)typedef enum \_\_packed {

[ 808](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e) [BT\_SECURITY\_L0](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e),

[ 810](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b) [BT\_SECURITY\_L1](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b),

[ 812](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a) [BT\_SECURITY\_L2](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a),

[ 814](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631) [BT\_SECURITY\_L3](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631),

[ 816](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81) [BT\_SECURITY\_L4](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81),

[ 820](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) [BT\_SECURITY\_FORCE\_PAIR](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

821} [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783);

822

[ 824](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e)enum [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) {

[ 826](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6) [BT\_SECURITY\_FLAG\_SC](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 828](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198) [BT\_SECURITY\_FLAG\_OOB](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

829};

830

[ 832](structbt__security__info.md)struct [bt\_security\_info](structbt__security__info.md) {

[ 834](structbt__security__info.md#a7b18849fad25b3f2da6b8c85a56d86e1) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [level](structbt__security__info.md#a7b18849fad25b3f2da6b8c85a56d86e1);

[ 836](structbt__security__info.md#a6567ffb82b7fa8093cc57ef4662873ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enc\_key\_size](structbt__security__info.md#a6567ffb82b7fa8093cc57ef4662873ba);

[ 838](structbt__security__info.md#a99cb4af08bfa1dab182821d956368526) enum [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) [flags](structbt__security__info.md#a99cb4af08bfa1dab182821d956368526);

839};

840

[ 842](structbt__conn__info.md)struct [bt\_conn\_info](structbt__conn__info.md) {

[ 844](structbt__conn__info.md#a7995e1291be494b5bdf860eceea0cad1) enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) [type](structbt__conn__info.md#a7995e1291be494b5bdf860eceea0cad1);

[ 846](structbt__conn__info.md#a8237b8c1bb9a97a174d04cbe13dca7c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__conn__info.md#a8237b8c1bb9a97a174d04cbe13dca7c7);

[ 848](structbt__conn__info.md#a3a4e24519b5d3ba547423e53c4d92a5c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__conn__info.md#a3a4e24519b5d3ba547423e53c4d92a5c);

850 union {

[ 852](structbt__conn__info.md#a6b536e7732dcf7b77a7bc05116dca548) struct [bt\_conn\_le\_info](structbt__conn__le__info.md) [le](structbt__conn__info.md#a6b536e7732dcf7b77a7bc05116dca548);

[ 854](structbt__conn__info.md#a799e59d3a85625799a32ac3f0b3d67d1) struct [bt\_conn\_br\_info](structbt__conn__br__info.md) [br](structbt__conn__info.md#a799e59d3a85625799a32ac3f0b3d67d1);

855 };

[ 857](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc) enum [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) [state](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc);

[ 859](structbt__conn__info.md#ae4405f1b4f3fe2ff6253453964860931) struct [bt\_security\_info](structbt__security__info.md) [security](structbt__conn__info.md#ae4405f1b4f3fe2ff6253453964860931);

860};

861

[ 863](structbt__conn__le__remote__info.md)struct [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md) {

864

[ 866](structbt__conn__le__remote__info.md#a4ff434f6c501dc60db5c4b776be46b3b) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[features](structbt__conn__le__remote__info.md#a4ff434f6c501dc60db5c4b776be46b3b);

867};

868

[ 870](structbt__conn__br__remote__info.md)struct [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md) {

871

[ 873](structbt__conn__br__remote__info.md#afa19f7db400bb0de234e8cda61f3deaf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[features](structbt__conn__br__remote__info.md#afa19f7db400bb0de234e8cda61f3deaf);

874

[ 876](structbt__conn__br__remote__info.md#a798c179c803e709182a1b0c3594f4a0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_pages](structbt__conn__br__remote__info.md#a798c179c803e709182a1b0c3594f4a0a);

877};

878

[ 884](structbt__conn__remote__info.md)struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) {

[ 886](structbt__conn__remote__info.md#a8bb514196bde5df561dbf76b68060729) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__conn__remote__info.md#a8bb514196bde5df561dbf76b68060729);

887

[ 889](structbt__conn__remote__info.md#a2664f6ed3bd22f9a011126daf5d81376) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structbt__conn__remote__info.md#a2664f6ed3bd22f9a011126daf5d81376);

890

[ 892](structbt__conn__remote__info.md#a47cc5a4b8888a0b8faaf6880c37418b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manufacturer](structbt__conn__remote__info.md#a47cc5a4b8888a0b8faaf6880c37418b8);

893

[ 895](structbt__conn__remote__info.md#a360979a15c958706157fc630fd55cbca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subversion](structbt__conn__remote__info.md#a360979a15c958706157fc630fd55cbca);

896

897 union {

[ 899](structbt__conn__remote__info.md#ae75530b09c6dea416630a4a19a1d64cc) struct [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md) [le](structbt__conn__remote__info.md#ae75530b09c6dea416630a4a19a1d64cc);

900

[ 902](structbt__conn__remote__info.md#ab73365f09cdb5ce870272546543bcfeb) struct [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md) [br](structbt__conn__remote__info.md#ab73365f09cdb5ce870272546543bcfeb);

903 };

904};

905

[ 906](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190)enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) {

[ 908](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a) [BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a),

[ 910](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046) [BT\_CONN\_LE\_TX\_POWER\_PHY\_1M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046),

[ 912](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800) [BT\_CONN\_LE\_TX\_POWER\_PHY\_2M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800),

[ 914](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2) [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2),

[ 916](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296) [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296),

917};

918

[ 920](structbt__conn__le__tx__power.md)struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) {

921

[ 923](structbt__conn__le__tx__power.md#a8702c4ff5082b8f90decdfabfb8253fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__conn__le__tx__power.md#a8702c4ff5082b8f90decdfabfb8253fe);

924

[ 926](structbt__conn__le__tx__power.md#a6d2e5a5215fa5d60630e74928a67fc04) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [current\_level](structbt__conn__le__tx__power.md#a6d2e5a5215fa5d60630e74928a67fc04);

927

[ 929](structbt__conn__le__tx__power.md#a1674247c511906fa6f0193653ed0b71a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_level](structbt__conn__le__tx__power.md#a1674247c511906fa6f0193653ed0b71a);

930};

931

932

[ 934](structbt__conn__le__tx__power__report.md)struct [bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md) {

935

[ 939](structbt__conn__le__tx__power__report.md#aa5606925229784af8ae90542432cf200) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__conn__le__tx__power__report.md#aa5606925229784af8ae90542432cf200);

940

[ 942](structbt__conn__le__tx__power__report.md#a5b1f67537fbe945f2f258b47082723b4) enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) [phy](structbt__conn__le__tx__power__report.md#a5b1f67537fbe945f2f258b47082723b4);

943

[ 952](structbt__conn__le__tx__power__report.md#ace830ddb7ae662c9759babed87f1b6f3) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__conn__le__tx__power__report.md#ace830ddb7ae662c9759babed87f1b6f3);

953

[ 957](structbt__conn__le__tx__power__report.md#ae7a4f77c6f7af1a459896d25cf661eb8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_power\_level\_flag](structbt__conn__le__tx__power__report.md#ae7a4f77c6f7af1a459896d25cf661eb8);

958

[ 965](structbt__conn__le__tx__power__report.md#a7c681c7b9f77d994b2de1febea7c5dc9) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [delta](structbt__conn__le__tx__power__report.md#a7c681c7b9f77d994b2de1febea7c5dc9);

966};

967

[ 976](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)enum [bt\_conn\_le\_path\_loss\_zone](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e) {

[ 978](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8) [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_LOW](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8),

[ 980](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec) [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_MIDDLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec),

[ 982](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705) [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_HIGH](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705),

[ 984](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942) [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_UNAVAILABLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942),

985};

986

987BUILD\_ASSERT([BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_LOW](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8) == [BT\_HCI\_LE\_ZONE\_ENTERED\_LOW](hci__types_8h.md#aff1538e314a97aa4910d4f7066dc4d55));

988BUILD\_ASSERT([BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_MIDDLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec) == [BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE](hci__types_8h.md#ab88f3d713f6862c08b73752436ca8b1b));

989BUILD\_ASSERT([BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_HIGH](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705) == [BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH](hci__types_8h.md#af7cc15be8165315ee0358ebb517b5e33));

990

[ 992](structbt__conn__le__path__loss__threshold__report.md)struct [bt\_conn\_le\_path\_loss\_threshold\_report](structbt__conn__le__path__loss__threshold__report.md) {

993

[ 995](structbt__conn__le__path__loss__threshold__report.md#ab2b71b7ddccc40ced56657a548b98e77) enum [bt\_conn\_le\_path\_loss\_zone](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e) [zone](structbt__conn__le__path__loss__threshold__report.md#ab2b71b7ddccc40ced56657a548b98e77);

996

[ 998](structbt__conn__le__path__loss__threshold__report.md#abe631b07816d6c18bacba64bfbd1e844) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_loss](structbt__conn__le__path__loss__threshold__report.md#abe631b07816d6c18bacba64bfbd1e844);

999};

1000

[ 1004](structbt__conn__le__path__loss__reporting__param.md)struct [bt\_conn\_le\_path\_loss\_reporting\_param](structbt__conn__le__path__loss__reporting__param.md) {

[ 1006](structbt__conn__le__path__loss__reporting__param.md#a5cc7a17efee69d61b8f8d0c242321054) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [high\_threshold](structbt__conn__le__path__loss__reporting__param.md#a5cc7a17efee69d61b8f8d0c242321054);

[ 1008](structbt__conn__le__path__loss__reporting__param.md#aec49adc896604d878060b03bd40ab0f4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [high\_hysteresis](structbt__conn__le__path__loss__reporting__param.md#aec49adc896604d878060b03bd40ab0f4);

[ 1010](structbt__conn__le__path__loss__reporting__param.md#a634c08e573cffd97a94ad681bed9239e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [low\_threshold](structbt__conn__le__path__loss__reporting__param.md#a634c08e573cffd97a94ad681bed9239e);

[ 1012](structbt__conn__le__path__loss__reporting__param.md#af8e70508a39ee73b75a4769769aa303f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [low\_hysteresis](structbt__conn__le__path__loss__reporting__param.md#af8e70508a39ee73b75a4769769aa303f);

[ 1016](structbt__conn__le__path__loss__reporting__param.md#a6fec4497c6fd95fa6f265bd859976c9d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_time\_spent](structbt__conn__le__path__loss__reporting__param.md#a6fec4497c6fd95fa6f265bd859976c9d);

1017};

1018

[ 1024](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043)enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) {

[ 1025](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6) [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6) = 0x00,

[ 1026](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1) [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1) = 0x01,

[ 1027](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529) [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529) = 0x02,

[ 1028](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da) [BT\_CONN\_AUTH\_KEYPRESS\_CLEARED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da) = 0x03,

[ 1029](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8) [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8) = 0x04,

1030};

1031

[ 1039](group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)int [bt\_conn\_get\_info](group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)(const struct bt\_conn \*conn, struct [bt\_conn\_info](structbt__conn__info.md) \*info);

1040

[ 1056](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92)int [bt\_conn\_get\_remote\_info](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92)(struct bt\_conn \*conn,

1057 struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info);

1058

[ 1067](group__bt__conn.md#gaa5289154bc508444f68df7abcef18aca)int [bt\_conn\_le\_get\_tx\_power\_level](group__bt__conn.md#gaa5289154bc508444f68df7abcef18aca)(struct bt\_conn \*conn,

1068 struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power\_level);

1069

[ 1078](group__bt__conn.md#gaa79eada87d698f4998af876d03d7e92b)int [bt\_conn\_le\_enhanced\_get\_tx\_power\_level](group__bt__conn.md#gaa79eada87d698f4998af876d03d7e92b)(struct bt\_conn \*conn,

1079 struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power);

1080

[ 1089](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4)int [bt\_conn\_le\_get\_remote\_tx\_power\_level](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4)(struct bt\_conn \*conn,

1090 enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) phy);

1091

[ 1101](group__bt__conn.md#gaa1f38911acee0534a8a6e414018c6fb6)int [bt\_conn\_le\_set\_tx\_power\_report\_enable](group__bt__conn.md#gaa1f38911acee0534a8a6e414018c6fb6)(struct bt\_conn \*conn,

1102 bool local\_enable,

1103 bool remote\_enable);

1104

[ 1116](group__bt__conn.md#ga6be5f3bf064ba03dc2307fdd2b634637)int [bt\_conn\_le\_set\_path\_loss\_mon\_param](group__bt__conn.md#ga6be5f3bf064ba03dc2307fdd2b634637)(struct bt\_conn \*conn,

1117 const struct [bt\_conn\_le\_path\_loss\_reporting\_param](structbt__conn__le__path__loss__reporting__param.md) \*param);

1118

[ 1131](group__bt__conn.md#ga90ae27bcc6f71f32be56efe8ecbc165d)int [bt\_conn\_le\_set\_path\_loss\_mon\_enable](group__bt__conn.md#ga90ae27bcc6f71f32be56efe8ecbc165d)(struct bt\_conn \*conn, bool enable);

1132

[ 1147](group__bt__conn.md#gac7bb456c530c7e08b4fa9f4d478fdaf9)int [bt\_conn\_le\_subrate\_set\_defaults](group__bt__conn.md#gac7bb456c530c7e08b4fa9f4d478fdaf9)(const struct [bt\_conn\_le\_subrate\_param](structbt__conn__le__subrate__param.md) \*params);

1148

[ 1160](group__bt__conn.md#ga754ed218fe9577f2d0ef6d508cfc5a0b)int [bt\_conn\_le\_subrate\_request](group__bt__conn.md#ga754ed218fe9577f2d0ef6d508cfc5a0b)(struct bt\_conn \*conn,

1161 const struct [bt\_conn\_le\_subrate\_param](structbt__conn__le__subrate__param.md) \*params);

1162

[ 1174](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb)int [bt\_conn\_le\_param\_update](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb)(struct bt\_conn \*conn,

1175 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param);

1176

[ 1184](group__bt__conn.md#ga8a2006f6e34b20c7e8ef65a73f431a57)int [bt\_conn\_le\_data\_len\_update](group__bt__conn.md#ga8a2006f6e34b20c7e8ef65a73f431a57)(struct bt\_conn \*conn,

1185 const struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) \*param);

1186

[ 1197](group__bt__conn.md#gae13ed81b1e7928f44b8fdf85995b3e58)int [bt\_conn\_le\_phy\_update](group__bt__conn.md#gae13ed81b1e7928f44b8fdf85995b3e58)(struct bt\_conn \*conn,

1198 const struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) \*param);

1199

[ 1222](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3)int [bt\_conn\_disconnect](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

1223

1224enum {

[ 1226](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9) [BT\_CONN\_LE\_OPT\_NONE](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9) = 0,

1227

[ 1232](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b) [BT\_CONN\_LE\_OPT\_CODED](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

1233

[ 1240](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9) [BT\_CONN\_LE\_OPT\_NO\_1M](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1241};

1242

[ 1243](structbt__conn__le__create__param.md)struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) {

1244

[ 1246](structbt__conn__le__create__param.md#a4b1e26c0976d9c900b831c886c77b055) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__conn__le__create__param.md#a4b1e26c0976d9c900b831c886c77b055);

1247

[ 1256](structbt__conn__le__create__param.md#a5cfae677f924534dc5bc7b38c457a7af) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__conn__le__create__param.md#a5cfae677f924534dc5bc7b38c457a7af);

1257

[ 1266](structbt__conn__le__create__param.md#a339b99f65c5029ada6cdf453ab1f258e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__conn__le__create__param.md#a339b99f65c5029ada6cdf453ab1f258e);

1267

[ 1272](structbt__conn__le__create__param.md#a2bc978ac97435fe5f87c6e01692f2910) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_coded](structbt__conn__le__create__param.md#a2bc978ac97435fe5f87c6e01692f2910);

1273

[ 1278](structbt__conn__le__create__param.md#ae62491837d35d95e32016b793edf8c96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window\_coded](structbt__conn__le__create__param.md#ae62491837d35d95e32016b793edf8c96);

1279

[ 1287](structbt__conn__le__create__param.md#a59f05bfb9468779d02f8d0beeb7a35c1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__conn__le__create__param.md#a59f05bfb9468779d02f8d0beeb7a35c1);

1288};

1289

[ 1296](group__bt__conn.md#ga8ac93a19c34d2821c158f310879fe00d)#define BT\_CONN\_LE\_CREATE\_PARAM\_INIT(\_options, \_interval, \_window) \

1297{ \

1298 .options = (\_options), \

1299 .interval = (\_interval), \

1300 .window = (\_window), \

1301 .interval\_coded = 0, \

1302 .window\_coded = 0, \

1303 .timeout = 0, \

1304}

1305

[ 1312](group__bt__conn.md#gae86425d432078e2ddca260eebc2802f1)#define BT\_CONN\_LE\_CREATE\_PARAM(\_options, \_interval, \_window) \

1313 ((struct bt\_conn\_le\_create\_param[]) { \

1314 BT\_CONN\_LE\_CREATE\_PARAM\_INIT(\_options, \_interval, \_window) \

1315 })

1316

[ 1320](group__bt__conn.md#gab4203c55c20d83256ca036148c14a00d)#define BT\_CONN\_LE\_CREATE\_CONN \

1321 BT\_CONN\_LE\_CREATE\_PARAM(BT\_CONN\_LE\_OPT\_NONE, \

1322 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

1323 BT\_GAP\_SCAN\_FAST\_INTERVAL)

1324

[ 1329](group__bt__conn.md#gaaba7c37a5c6e98e7b62ac12bde814d5d)#define BT\_CONN\_LE\_CREATE\_CONN\_AUTO \

1330 BT\_CONN\_LE\_CREATE\_PARAM(BT\_CONN\_LE\_OPT\_NONE, \

1331 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

1332 BT\_GAP\_SCAN\_FAST\_WINDOW)

1333

[ 1356](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6)int [bt\_conn\_le\_create](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer,

1357 const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param,

1358 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param,

1359 struct bt\_conn \*\*conn);

1360

[ 1361](structbt__conn__le__create__synced__param.md)struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) {

1362

[ 1368](structbt__conn__le__create__synced__param.md#ac5872dda4042e3ba6c161dce60784b70) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[peer](structbt__conn__le__create__synced__param.md#ac5872dda4042e3ba6c161dce60784b70);

1369

[ 1371](structbt__conn__le__create__synced__param.md#ac7b4e4144aaf914bdef1dc305b5e297f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__conn__le__create__synced__param.md#ac7b4e4144aaf914bdef1dc305b5e297f);

1372};

1373

[ 1393](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1)int [bt\_conn\_le\_create\_synced](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1)(const struct bt\_le\_ext\_adv \*adv,

1394 const struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) \*synced\_param,

1395 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param, struct bt\_conn \*\*conn);

1396

[ 1412](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b)int [bt\_conn\_le\_create\_auto](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b)(const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param,

1413 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param);

1414

[ 1419](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4)int [bt\_conn\_create\_auto\_stop](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4)(void);

1420

[ 1435](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a)int [bt\_le\_set\_auto\_conn](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr,

1436 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param);

1437

[ 1474](group__bt__conn.md#gae001f1268e1ff42c3c974c95dcb6735d)int [bt\_conn\_set\_security](group__bt__conn.md#gae001f1268e1ff42c3c974c95dcb6735d)(struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) sec);

1475

[ 1480](group__bt__conn.md#ga4b43ef0f30146808e560991a302e88ad)[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [bt\_conn\_get\_security](group__bt__conn.md#ga4b43ef0f30146808e560991a302e88ad)(const struct bt\_conn \*conn);

1481

[ 1491](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_conn\_enc\_key\_size](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e)(const struct bt\_conn \*conn);

1492

[ 1493](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff)enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) {

[ 1495](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05) [BT\_SECURITY\_ERR\_SUCCESS](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05),

1496

[ 1498](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7) [BT\_SECURITY\_ERR\_AUTH\_FAIL](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7),

1499

[ 1501](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171) [BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171),

1502

[ 1504](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7) [BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7),

1505

[ 1507](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae) [BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae),

1508

[ 1510](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6) [BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6),

1511

[ 1513](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f) [BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f),

1514

[ 1516](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5) [BT\_SECURITY\_ERR\_INVALID\_PARAM](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5),

1517

[ 1519](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216) [BT\_SECURITY\_ERR\_KEY\_REJECTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216),

1520

[ 1522](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242) [BT\_SECURITY\_ERR\_UNSPECIFIED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242),

1523};

1524

[ 1525](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2)enum [bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2) {

[ 1526](group__bt__conn.md#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83) [BT\_CONN\_LE\_CS\_PROCEDURES\_DISABLED](group__bt__conn.md#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83) = [BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED](hci__types_8h.md#a3e01bbe3a72c946015a288ee49d3cbdd),

[ 1527](group__bt__conn.md#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac) [BT\_CONN\_LE\_CS\_PROCEDURES\_ENABLED](group__bt__conn.md#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac) = [BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED](hci__types_8h.md#a4a88120ae7e83fd791012c913315d14f),

1528};

1529

[ 1557](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c)enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) {

[ 1558](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591cac8e353ad7af2b410aebf02aaa5d5f2c4) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_ONE](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591cac8e353ad7af2b410aebf02aaa5d5f2c4) = [BT\_HCI\_OP\_LE\_CS\_ACI\_0](hci__types_8h.md#a92e1ec21014999f40172fa1812c36575),

[ 1559](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca172dde37f3e1368fd00d2bed86c4ae7b) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_TWO](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca172dde37f3e1368fd00d2bed86c4ae7b) = [BT\_HCI\_OP\_LE\_CS\_ACI\_1](hci__types_8h.md#a5b082fa5b8ba11a651468cc516d067fe),

[ 1560](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591caf6bd13c55ac53af42ff9035221a91fc4) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_THREE](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591caf6bd13c55ac53af42ff9035221a91fc4) = [BT\_HCI\_OP\_LE\_CS\_ACI\_2](hci__types_8h.md#ab30a4e55002080394c39fb885eba36e4),

[ 1561](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca967ebe063b0ae1d4249e67fcbea9fa18) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_FOUR](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca967ebe063b0ae1d4249e67fcbea9fa18) = [BT\_HCI\_OP\_LE\_CS\_ACI\_3](hci__types_8h.md#a76d1452003c0bd3b688765aa2d25047f),

[ 1562](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca6256d88a5a4c8b9c63625dfc0e251da0) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_FIVE](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca6256d88a5a4c8b9c63625dfc0e251da0) = [BT\_HCI\_OP\_LE\_CS\_ACI\_4](hci__types_8h.md#af16c4c79e602e6da833b8aa3e0c4bf64),

[ 1563](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591cab26feeda58c2275dd857c10a7029dc83) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_SIX](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591cab26feeda58c2275dd857c10a7029dc83) = [BT\_HCI\_OP\_LE\_CS\_ACI\_5](hci__types_8h.md#ad980d8f134d940b80dc9b0e3a570ac06),

[ 1564](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca6aac8dc77fccbc6a89226341a85bbdcc) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_SEVEN](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca6aac8dc77fccbc6a89226341a85bbdcc) = [BT\_HCI\_OP\_LE\_CS\_ACI\_6](hci__types_8h.md#a4c7ff3c949023f4544bf50353a0f082b),

[ 1565](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591caae7087f9165279af27e64676a54eaea3) [BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_EIGHT](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591caae7087f9165279af27e64676a54eaea3) = [BT\_HCI\_OP\_LE\_CS\_ACI\_7](hci__types_8h.md#acabccf9f5893324dcb6acc0769ab8417),

1566};

1567

[ 1568](structbt__conn__le__cs__procedure__enable__complete.md)struct [bt\_conn\_le\_cs\_procedure\_enable\_complete](structbt__conn__le__cs__procedure__enable__complete.md) {

1569 /\* The ID associated with the desired configuration (0 to 3) \*/

[ 1570](structbt__conn__le__cs__procedure__enable__complete.md#a2e290c25ec5af8b0259d45f04d6c543d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config\_id](structbt__conn__le__cs__procedure__enable__complete.md#a2e290c25ec5af8b0259d45f04d6c543d);

1571

1572 /\* State of the CS procedure \*/

[ 1573](structbt__conn__le__cs__procedure__enable__complete.md#acc1d12d347e1b02b2eea562ea064a40b) enum [bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2) [state](structbt__conn__le__cs__procedure__enable__complete.md#acc1d12d347e1b02b2eea562ea064a40b);

1574

1575 /\* Antenna configuration index \*/

[ 1576](structbt__conn__le__cs__procedure__enable__complete.md#a3fa8ad4dd264eb4e2489dea9c1048d22) enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) [tone\_antenna\_config\_selection](structbt__conn__le__cs__procedure__enable__complete.md#a3fa8ad4dd264eb4e2489dea9c1048d22);

1577

1578 /\* Transmit power level used for CS procedures (-127 to 20 dB; 0x7F if unavailable) \*/

[ 1579](structbt__conn__le__cs__procedure__enable__complete.md#aeb918e438cd02296c7f693757268f6bf) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [selected\_tx\_power](structbt__conn__le__cs__procedure__enable__complete.md#aeb918e438cd02296c7f693757268f6bf);

1580

1581 /\* Duration of each CS subevent in microseconds (1250 us to 4 s) \*/

[ 1582](structbt__conn__le__cs__procedure__enable__complete.md#ae990a10c468ec62fbaf9325c94733c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [subevent\_len](structbt__conn__le__cs__procedure__enable__complete.md#ae990a10c468ec62fbaf9325c94733c7c);

1583

1584 /\* Number of CS subevents anchored off the same ACL connection event (0x01 to 0x20) \*/

[ 1585](structbt__conn__le__cs__procedure__enable__complete.md#a40b03220932852b6b51d65f557c21f17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevents\_per\_event](structbt__conn__le__cs__procedure__enable__complete.md#a40b03220932852b6b51d65f557c21f17);

1586

1587 /\* Time between consecutive CS subevents anchored off the same ACL connection event in

1588 \* units of 0.625 ms

1589 \*/

[ 1590](structbt__conn__le__cs__procedure__enable__complete.md#a77a2bd8ee384c4567321a09f6b64782c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subevent\_interval](structbt__conn__le__cs__procedure__enable__complete.md#a77a2bd8ee384c4567321a09f6b64782c);

1591

1592 /\* Number of ACL connection events between consecutive CS event anchor points \*/

[ 1593](structbt__conn__le__cs__procedure__enable__complete.md#a4129ab9519ba140ffb198aa9a5cde6ac) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [event\_interval](structbt__conn__le__cs__procedure__enable__complete.md#a4129ab9519ba140ffb198aa9a5cde6ac);

1594

1595 /\* Number of ACL connection events between consecutive CS procedure anchor points \*/

[ 1596](structbt__conn__le__cs__procedure__enable__complete.md#a8511deef97f19c53ddaa4dec8492658f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [procedure\_interval](structbt__conn__le__cs__procedure__enable__complete.md#a8511deef97f19c53ddaa4dec8492658f);

1597

1598 /\* Number of CS procedures to be scheduled (0 if procedures to continue until disabled) \*/

[ 1599](structbt__conn__le__cs__procedure__enable__complete.md#ab83778fe2d1274e5658fd5f5f867314f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [procedure\_count](structbt__conn__le__cs__procedure__enable__complete.md#ab83778fe2d1274e5658fd5f5f867314f);

1600

1601 /\* Maximum duration for each procedure in units of 0.625 ms (0x0001 to 0xFFFF) \*/

[ 1602](structbt__conn__le__cs__procedure__enable__complete.md#ad71825d71ab89baea138e41f9a3ff57e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_procedure\_len](structbt__conn__le__cs__procedure__enable__complete.md#ad71825d71ab89baea138e41f9a3ff57e);

1603};

1604

[ 1615](structbt__conn__cb.md)struct [bt\_conn\_cb](structbt__conn__cb.md) {

[ 1640](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69) void (\*[connected](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err);

1641

[ 1659](structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914) void (\*[disconnected](structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

1660

[ 1673](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b) void (\*[recycled](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b))(void);

1674

[ 1699](structbt__conn__cb.md#a2c52c2e2798062708c373fae9610fadd) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[le\_param\_req](structbt__conn__cb.md#a2c52c2e2798062708c373fae9610fadd))(struct bt\_conn \*conn,

1700 struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param);

1701

[ 1712](structbt__conn__cb.md#a01582ed3e3801e10c665534eaa991454) void (\*[le\_param\_updated](structbt__conn__cb.md#a01582ed3e3801e10c665534eaa991454))(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) interval,

1713 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) latency, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout);

1714#if defined(CONFIG\_BT\_SMP)

[ 1724](structbt__conn__cb.md#aea9b62ab1a1469be97a207a8e07d2f14) void (\*[identity\_resolved](structbt__conn__cb.md#aea9b62ab1a1469be97a207a8e07d2f14))(struct bt\_conn \*conn,

1725 const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*rpa,

1726 const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*identity);

1727#endif /\* CONFIG\_BT\_SMP \*/

1728#if defined(CONFIG\_BT\_SMP) || defined(CONFIG\_BT\_CLASSIC)

[ 1745](structbt__conn__cb.md#ae454d5bc2664e90ba2b1e0c867db374e) void (\*[security\_changed](structbt__conn__cb.md#ae454d5bc2664e90ba2b1e0c867db374e))(struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) level,

1746 enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err);

1747#endif /\* defined(CONFIG\_BT\_SMP) || defined(CONFIG\_BT\_CLASSIC) \*/

1748

1749#if defined(CONFIG\_BT\_REMOTE\_INFO)

[ 1758](structbt__conn__cb.md#af726f004c06b86f770ece263ed6c9ca4) void (\*[remote\_info\_available](structbt__conn__cb.md#af726f004c06b86f770ece263ed6c9ca4))(struct bt\_conn \*conn,

1759 struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info);

1760#endif /\* defined(CONFIG\_BT\_REMOTE\_INFO) \*/

1761

1762#if defined(CONFIG\_BT\_USER\_PHY\_UPDATE)

[ 1771](structbt__conn__cb.md#ae02a23d823954a747f8f474fb19276d7) void (\*[le\_phy\_updated](structbt__conn__cb.md#ae02a23d823954a747f8f474fb19276d7))(struct bt\_conn \*conn,

1772 struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \*param);

1773#endif /\* defined(CONFIG\_BT\_USER\_PHY\_UPDATE) \*/

1774

1775#if defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE)

[ 1784](structbt__conn__cb.md#a1142d1861cc0b0058f68ecf537d0cec3) void (\*[le\_data\_len\_updated](structbt__conn__cb.md#a1142d1861cc0b0058f68ecf537d0cec3))(struct bt\_conn \*conn,

1785 struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \*info);

1786#endif /\* defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE) \*/

1787

1788#if defined(CONFIG\_BT\_DF\_CONNECTION\_CTE\_RX)

1795 void (\*cte\_report\_cb)(struct bt\_conn \*conn,

1796 const struct [bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md) \*iq\_report);

1797#endif /\* CONFIG\_BT\_DF\_CONNECTION\_CTE\_RX \*/

1798

1799#if defined(CONFIG\_BT\_TRANSMIT\_POWER\_CONTROL)

1811 void (\*tx\_power\_report)(struct bt\_conn \*conn,

1812 const struct [bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md) \*report);

1813#endif /\* CONFIG\_BT\_TRANSMIT\_POWER\_CONTROL \*/

1814

1815#if defined(CONFIG\_BT\_PATH\_LOSS\_MONITORING)

1825 void (\*path\_loss\_threshold\_report)(struct bt\_conn \*conn,

1826 const struct [bt\_conn\_le\_path\_loss\_threshold\_report](structbt__conn__le__path__loss__threshold__report.md) \*report);

1827#endif /\* CONFIG\_BT\_PATH\_LOSS\_MONITORING \*/

1828

1829#if defined(CONFIG\_BT\_SUBRATING)

1840 void (\*subrate\_changed)(struct bt\_conn \*conn,

1841 const struct [bt\_conn\_le\_subrate\_changed](structbt__conn__le__subrate__changed.md) \*params);

1842#endif /\* CONFIG\_BT\_SUBRATING \*/

1843

1844#if defined(CONFIG\_BT\_CHANNEL\_SOUNDING)

1853 void (\*le\_cs\_remote\_capabilities\_available)(struct bt\_conn \*conn,

1854 struct [bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md) \*params);

1855

1864 void (\*le\_cs\_remote\_fae\_table\_available)(struct bt\_conn \*conn,

1865 struct [bt\_conn\_le\_cs\_fae\_table](structbt__conn__le__cs__fae__table.md) \*params);

1866

1875 void (\*le\_cs\_config\_created)(struct bt\_conn \*conn, struct [bt\_conn\_le\_cs\_config](structbt__conn__le__cs__config.md) \*config);

1876

1885 void (\*le\_cs\_config\_removed)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) config\_id);

1886

1895 void (\*le\_cs\_subevent\_data\_available)(struct bt\_conn \*conn,

1896 struct [bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md) \*result);

1897

1905 void (\*le\_cs\_security\_enabled)(struct bt\_conn \*conn);

1906

1915 void (\*le\_cs\_procedure\_enabled)(

1916 struct bt\_conn \*conn, struct [bt\_conn\_le\_cs\_procedure\_enable\_complete](structbt__conn__le__cs__procedure__enable__complete.md) \*params);

1917

1918#endif

1919

1921 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

1922};

1923

[ 1933](group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b)int [bt\_conn\_cb\_register](group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b)(struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb);

1934

[ 1946](group__bt__conn.md#gad2f90b34390e3c3697fd455ae4ef5f31)int [bt\_conn\_cb\_unregister](group__bt__conn.md#gad2f90b34390e3c3697fd455ae4ef5f31)(struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb);

1947

[ 1953](group__bt__conn.md#ga9227880a1ae5fc373d334171e1450f00)#define BT\_CONN\_CB\_DEFINE(\_name) \

1954 static const STRUCT\_SECTION\_ITERABLE(bt\_conn\_cb, \

1955 \_CONCAT(bt\_conn\_cb\_, \

1956 \_name))

1957

1964#if defined(CONFIG\_BT\_SECURITY\_ERR\_TO\_STR)

1965const char \*[bt\_security\_err\_to\_str](group__bt__conn.md#ga327444a6987b8e0b573fe758d2f75886)(enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err);

1966#else

[ 1967](group__bt__conn.md#ga327444a6987b8e0b573fe758d2f75886)static inline const char \*[bt\_security\_err\_to\_str](group__bt__conn.md#ga327444a6987b8e0b573fe758d2f75886)(enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err)

1968{

1969 ARG\_UNUSED(err);

1970

1971 return "";

1972}

1973#endif

1974

[ 1985](group__bt__conn.md#ga014db594b17a3b5d7d954e64ad8de759)void [bt\_set\_bondable](group__bt__conn.md#ga014db594b17a3b5d7d954e64ad8de759)(bool enable);

1986

[ 1996](group__bt__conn.md#ga0c84d5597a71fe38788a88063fd19a2d)bool [bt\_get\_bondable](group__bt__conn.md#ga0c84d5597a71fe38788a88063fd19a2d)(void);

1997

[ 2016](group__bt__conn.md#ga4165819d12dd96e00dfa2fd6f4b95669)int [bt\_conn\_set\_bondable](group__bt__conn.md#ga4165819d12dd96e00dfa2fd6f4b95669)(struct bt\_conn \*conn, bool enable);

2017

[ 2024](group__bt__conn.md#gad02f8fe587efd543c0c81cace3f63d63)void [bt\_le\_oob\_set\_sc\_flag](group__bt__conn.md#gad02f8fe587efd543c0c81cace3f63d63)(bool enable);

2025

[ 2032](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892)void [bt\_le\_oob\_set\_legacy\_flag](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892)(bool enable);

2033

[ 2045](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba)int [bt\_le\_oob\_set\_legacy\_tk](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba)(struct bt\_conn \*conn, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tk);

2046

[ 2065](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503)int [bt\_le\_oob\_set\_sc\_data](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503)(struct bt\_conn \*conn,

2066 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_local,

2067 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_remote);

2068

[ 2084](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee)int [bt\_le\_oob\_get\_sc\_data](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee)(struct bt\_conn \*conn,

2085 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_local,

2086 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_remote);

2087

[ 2092](group__bt__conn.md#gaf638077430b418f9879ac4ddf58ef17a)#define BT\_PASSKEY\_INVALID 0xffffffff

2093

[ 2107](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1)int [bt\_passkey\_set](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1)(unsigned int passkey);

2108

[ 2110](structbt__conn__oob__info.md)struct [bt\_conn\_oob\_info](structbt__conn__oob__info.md) {

2112 enum {

[ 2114](structbt__conn__oob__info.md#a318a663619f0bbbb90a849fd5e16c37ea4c33ea839306256a198c29ea783c659b) [BT\_CONN\_OOB\_LE\_LEGACY](structbt__conn__oob__info.md#a318a663619f0bbbb90a849fd5e16c37ea4c33ea839306256a198c29ea783c659b),

2115

[ 2117](structbt__conn__oob__info.md#a318a663619f0bbbb90a849fd5e16c37eacd02773beb42df3fb6cbaa2fa2abda1e) [BT\_CONN\_OOB\_LE\_SC](structbt__conn__oob__info.md#a318a663619f0bbbb90a849fd5e16c37eacd02773beb42df3fb6cbaa2fa2abda1e),

[ 2118](structbt__conn__oob__info.md#a9923119f8a145066408d9e46d6993026) } [type](structbt__conn__oob__info.md#a9923119f8a145066408d9e46d6993026);

2119

2120 union {

2122 struct {

2124 enum {

[ 2126](structbt__conn__oob__info.md#a72a749120c0a55a8dc9bd078921277e5) [BT\_CONN\_OOB\_LOCAL\_ONLY](structbt__conn__oob__info.md#a72a749120c0a55a8dc9bd078921277e5),

2127

[ 2129](structbt__conn__oob__info.md#a7506049b35ac63602452b087d1d60fa2) [BT\_CONN\_OOB\_REMOTE\_ONLY](structbt__conn__oob__info.md#a7506049b35ac63602452b087d1d60fa2),

2130

[ 2132](structbt__conn__oob__info.md#a99685ad84ac991e0540855cab5546ff8) [BT\_CONN\_OOB\_BOTH\_PEERS](structbt__conn__oob__info.md#a99685ad84ac991e0540855cab5546ff8),

2133

[ 2135](structbt__conn__oob__info.md#a71bf295d82fbc647b3816bfba6fa0ae7) [BT\_CONN\_OOB\_NO\_DATA](structbt__conn__oob__info.md#a71bf295d82fbc647b3816bfba6fa0ae7),

[ 2136](structbt__conn__oob__info.md#a96f2cf2f20d9890b833949b2183a029c) } [oob\_config](structbt__conn__oob__info.md#a96f2cf2f20d9890b833949b2183a029c);

[ 2137](structbt__conn__oob__info.md#a59febda99e1ad78321fe2da07f98322b) } [lesc](structbt__conn__oob__info.md#a59febda99e1ad78321fe2da07f98322b);

2138 };

2139};

2140

2141#if defined(CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT)

[ 2148](structbt__conn__pairing__feat.md)struct [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) {

[ 2150](structbt__conn__pairing__feat.md#a68005cea273c8e76c086502001b258b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [io\_capability](structbt__conn__pairing__feat.md#a68005cea273c8e76c086502001b258b0);

2151

[ 2153](structbt__conn__pairing__feat.md#afb03164960db62b4b4cf70d3f0134099) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_data\_flag](structbt__conn__pairing__feat.md#afb03164960db62b4b4cf70d3f0134099);

2154

[ 2156](structbt__conn__pairing__feat.md#af9a977b1e0f9d4eada26a82d92eaec54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [auth\_req](structbt__conn__pairing__feat.md#af9a977b1e0f9d4eada26a82d92eaec54);

2157

[ 2159](structbt__conn__pairing__feat.md#abe1d7d4bd9f4b551a2d0c69adc75bd40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_enc\_key\_size](structbt__conn__pairing__feat.md#abe1d7d4bd9f4b551a2d0c69adc75bd40);

2160

[ 2164](structbt__conn__pairing__feat.md#a70adc125b875348ec8d273dea3b470d8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_key\_dist](structbt__conn__pairing__feat.md#a70adc125b875348ec8d273dea3b470d8);

2165

[ 2169](structbt__conn__auth__cb.md#a92391a172e158a42966f410d732424a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [resp\_key\_dist](structbt__conn__pairing__feat.md#a49f9f02e232e91f7f7a530aa7f226cba);

2170};

2171#endif /\* CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT \*/

2172

[ 2174](structbt__conn__auth__cb.md)struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) {

2175#if defined(CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT)

2203 enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) (\*[pairing\_accept](structbt__conn__auth__cb.md#a92391a172e158a42966f410d732424a7))(struct bt\_conn \*conn,

2204 const struct [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) \*const feat);

2205#endif /\* CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT \*/

2206

[ 2225](structbt__conn__auth__cb.md#a14074ca97fad6af4c58c43a00c503104) void (\*[passkey\_display](structbt__conn__auth__cb.md#a14074ca97fad6af4c58c43a00c503104))(struct bt\_conn \*conn, unsigned int passkey);

2226

2227#if defined(CONFIG\_BT\_PASSKEY\_KEYPRESS)

2249 void (\*passkey\_display\_keypress)(struct bt\_conn \*conn,

2250 enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) type);

2251#endif

2252

[ 2271](structbt__conn__auth__cb.md#a10f9d22c89c95a6f3ffe0016f92445c0) void (\*[passkey\_entry](structbt__conn__auth__cb.md#a10f9d22c89c95a6f3ffe0016f92445c0))(struct bt\_conn \*conn);

2272

[ 2294](structbt__conn__auth__cb.md#a2bb6c10666d111f675fd6de5ff51410a) void (\*[passkey\_confirm](structbt__conn__auth__cb.md#a2bb6c10666d111f675fd6de5ff51410a))(struct bt\_conn \*conn, unsigned int passkey);

2295

[ 2312](structbt__conn__auth__cb.md#aec9f6256607ea2cd1ce1b4cdb3052b42) void (\*[oob\_data\_request](structbt__conn__auth__cb.md#aec9f6256607ea2cd1ce1b4cdb3052b42))(struct bt\_conn \*conn,

2313 struct [bt\_conn\_oob\_info](structbt__conn__oob__info.md) \*info);

2314

[ 2327](structbt__conn__auth__cb.md#af6eb01c252ba3e32ff8bf583aa6ca0a4) void (\*[cancel](structbt__conn__auth__cb.md#af6eb01c252ba3e32ff8bf583aa6ca0a4))(struct bt\_conn \*conn);

2328

[ 2347](structbt__conn__auth__cb.md#af4f7d3ee570b3472ee79b014be01f76e) void (\*[pairing\_confirm](structbt__conn__auth__cb.md#af4f7d3ee570b3472ee79b014be01f76e))(struct bt\_conn \*conn);

2348

2349#if defined(CONFIG\_BT\_CLASSIC)

[ 2368](structbt__conn__auth__cb.md#ab6df1b1505dc22dd8dae0e946546c8bb) void (\*[pincode\_entry](structbt__conn__auth__cb.md#ab6df1b1505dc22dd8dae0e946546c8bb))(struct bt\_conn \*conn, bool highsec);

2369#endif

2370};

2371

[ 2373](structbt__conn__auth__info__cb.md)struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) {

[ 2383](structbt__conn__auth__info__cb.md#aea737700f2760de1ed26a721b5e860d2) void (\*[pairing\_complete](structbt__conn__auth__info__cb.md#aea737700f2760de1ed26a721b5e860d2))(struct bt\_conn \*conn, bool bonded);

2384

[ 2390](structbt__conn__auth__info__cb.md#ae7228bb82889eacebf67e1d4b3b23375) void (\*[pairing\_failed](structbt__conn__auth__info__cb.md#ae7228bb82889eacebf67e1d4b3b23375))(struct bt\_conn \*conn,

2391 enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) reason);

2392

[ 2401](structbt__conn__auth__info__cb.md#af20b0d7fc5fd8399ad9368b3ef7067f8) void (\*[bond\_deleted](structbt__conn__auth__info__cb.md#af20b0d7fc5fd8399ad9368b3ef7067f8))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer);

2402

[ 2404](structbt__conn__auth__info__cb.md#afde62f2cdfb40b4154208f3c1c3dadc1) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__conn__auth__info__cb.md#afde62f2cdfb40b4154208f3c1c3dadc1);

2405};

2406

[ 2416](group__bt__conn.md#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)int [bt\_conn\_auth\_cb\_register](group__bt__conn.md#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)(const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb);

2417

[ 2432](group__bt__conn.md#ga81077385583d71c248a1eb6aab9ee86e)int [bt\_conn\_auth\_cb\_overlay](group__bt__conn.md#ga81077385583d71c248a1eb6aab9ee86e)(struct bt\_conn \*conn, const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb);

2433

[ 2443](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f)int [bt\_conn\_auth\_info\_cb\_register](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f)(struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb);

2444

[ 2453](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37)int [bt\_conn\_auth\_info\_cb\_unregister](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37)(struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb);

2454

[ 2465](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)int [bt\_conn\_auth\_passkey\_entry](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)(struct bt\_conn \*conn, unsigned int passkey);

2466

[ 2482](group__bt__conn.md#ga2987a902da4f5cfe3671c60d154ced7e)int [bt\_conn\_auth\_keypress\_notify](group__bt__conn.md#ga2987a902da4f5cfe3671c60d154ced7e)(struct bt\_conn \*conn, enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) type);

2483

[ 2492](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59)int [bt\_conn\_auth\_cancel](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59)(struct bt\_conn \*conn);

2493

[ 2503](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995)int [bt\_conn\_auth\_passkey\_confirm](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995)(struct bt\_conn \*conn);

2504

[ 2514](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d)int [bt\_conn\_auth\_pairing\_confirm](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d)(struct bt\_conn \*conn);

2515

[ 2526](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98)int [bt\_conn\_auth\_pincode\_entry](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98)(struct bt\_conn \*conn, const char \*pin);

2527

[ 2529](structbt__br__conn__param.md)struct [bt\_br\_conn\_param](structbt__br__conn__param.md) {

[ 2530](structbt__br__conn__param.md#a95454a74932a14b4137c3fe82821be49) bool [allow\_role\_switch](structbt__br__conn__param.md#a95454a74932a14b4137c3fe82821be49);

2531};

2532

[ 2537](group__bt__conn.md#ga986f563bfb741c70fbee39b3948d9d8d)#define BT\_BR\_CONN\_PARAM\_INIT(role\_switch) \

2538{ \

2539 .allow\_role\_switch = (role\_switch), \

2540}

2541

[ 2546](group__bt__conn.md#ga6f99f4adfcef36a4d738783921965ca6)#define BT\_BR\_CONN\_PARAM(role\_switch) \

2547 ((struct bt\_br\_conn\_param[]) { \

2548 BT\_BR\_CONN\_PARAM\_INIT(role\_switch) \

2549 })

2550

[ 2554](group__bt__conn.md#ga5ccdbff63a430a37a8a8077d8792f706)#define BT\_BR\_CONN\_PARAM\_DEFAULT BT\_BR\_CONN\_PARAM(true)

2555

2556

[ 2569](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9)struct bt\_conn \*[bt\_conn\_create\_br](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9)(const [bt\_addr\_t](structbt__addr__t.md) \*peer,

2570 const struct [bt\_br\_conn\_param](structbt__br__conn__param.md) \*param);

2571

2572#ifdef \_\_cplusplus

2573}

2574#endif

2575

2579

2580#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_CONN\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[direction.h](direction_8h.md)

[gap.h](gap_8h.md)

Bluetooth Generic Access Profile defines and Assigned Numbers.

[bt\_set\_bondable](group__bt__conn.md#ga014db594b17a3b5d7d954e64ad8de759)

void bt\_set\_bondable(bool enable)

Enable/disable bonding.

[bt\_conn\_ref](group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c)

struct bt\_conn \* bt\_conn\_ref(struct bt\_conn \*conn)

Increment a connection's reference count.

[bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf)

bt\_conn\_le\_cs\_sub\_mode

Channel sounding sub mode.

**Definition** conn.h:427

[bt\_conn\_le\_get\_remote\_tx\_power\_level](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4)

int bt\_conn\_le\_get\_remote\_tx\_power\_level(struct bt\_conn \*conn, enum bt\_conn\_le\_tx\_power\_phy phy)

Get remote (peer) transmit power level.

[bt\_le\_oob\_get\_sc\_data](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee)

int bt\_le\_oob\_get\_sc\_data(struct bt\_conn \*conn, const struct bt\_le\_oob\_sc\_data \*\*oobd\_local, const struct bt\_le\_oob\_sc\_data \*\*oobd\_remote)

Get OOB data used for LE Secure Connections (SC) pairing procedure.

[bt\_get\_bondable](group__bt__conn.md#ga0c84d5597a71fe38788a88063fd19a2d)

bool bt\_get\_bondable(void)

Get bonding flag.

[bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f)

bt\_conn\_le\_cs\_role

Channel sounding role.

**Definition** conn.h:439

[bt\_le\_oob\_set\_legacy\_tk](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba)

int bt\_le\_oob\_set\_legacy\_tk(struct bt\_conn \*conn, const uint8\_t \*tk)

Set OOB Temporary Key to be used for pairing.

[bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f)

bt\_conn\_le\_cs\_main\_mode

Channel sounding main mode.

**Definition** conn.h:417

[bt\_conn\_disconnect](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3)

int bt\_conn\_disconnect(struct bt\_conn \*conn, uint8\_t reason)

Disconnect from a remote device or cancel pending connection.

[bt\_conn\_le\_cs\_capability\_rtt\_sounding](group__bt__conn.md#ga1892ec23ca3b1818287a9d7dafc16433)

bt\_conn\_le\_cs\_capability\_rtt\_sounding

Supported Sounding Sequence RTT precision.

**Definition** conn.h:276

[bt\_conn\_auth\_cb\_register](group__bt__conn.md#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)

int bt\_conn\_auth\_cb\_register(const struct bt\_conn\_auth\_cb \*cb)

Register authentication callbacks.

[bt\_conn\_lookup\_addr\_le](group__bt__conn.md#ga1bfe349efd8a7de31e9457fe439d746a)

struct bt\_conn \* bt\_conn\_lookup\_addr\_le(uint8\_t id, const bt\_addr\_le\_t \*peer)

Look up an existing connection by address.

[bt\_conn\_auth\_keypress\_notify](group__bt__conn.md#ga2987a902da4f5cfe3671c60d154ced7e)

int bt\_conn\_auth\_keypress\_notify(struct bt\_conn \*conn, enum bt\_conn\_auth\_keypress type)

Send Passkey Keypress Notification during pairing.

[bt\_conn\_get\_info](group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)

int bt\_conn\_get\_info(const struct bt\_conn \*conn, struct bt\_conn\_info \*info)

Get connection info.

[bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e)

bt\_security\_flag

Security Info Flags.

**Definition** conn.h:824

[bt\_conn\_le\_cs\_procedure\_abort\_reason](group__bt__conn.md#ga3196a0eb1c7497e93d7c646713d2fc79)

bt\_conn\_le\_cs\_procedure\_abort\_reason

Procedure abort reason.

**Definition** conn.h:555

[bt\_security\_err\_to\_str](group__bt__conn.md#ga327444a6987b8e0b573fe758d2f75886)

static const char \* bt\_security\_err\_to\_str(enum bt\_security\_err err)

Converts a security error to string.

**Definition** conn.h:1967

[bt\_passkey\_set](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1)

int bt\_passkey\_set(unsigned int passkey)

Set a fixed passkey to be used for pairing.

[bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0)

bt\_conn\_le\_cs\_chsel\_type

Channel sounding channel selection type.

**Definition** conn.h:475

[bt\_conn\_auth\_passkey\_entry](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)

int bt\_conn\_auth\_passkey\_entry(struct bt\_conn \*conn, unsigned int passkey)

Reply with entered passkey.

[bt\_conn\_auth\_pairing\_confirm](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d)

int bt\_conn\_auth\_pairing\_confirm(struct bt\_conn \*conn)

Reply if incoming pairing was confirmed by user.

[bt\_conn\_auth\_pincode\_entry](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98)

int bt\_conn\_auth\_pincode\_entry(struct bt\_conn \*conn, const char \*pin)

Reply with entered PIN code.

[bt\_conn\_set\_bondable](group__bt__conn.md#ga4165819d12dd96e00dfa2fd6f4b95669)

int bt\_conn\_set\_bondable(struct bt\_conn \*conn, bool enable)

Set/clear the bonding flag for a given connection.

[bt\_conn\_unref](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6)

void bt\_conn\_unref(struct bt\_conn \*conn)

Decrement a connection's reference count.

[bt\_conn\_get\_security](group__bt__conn.md#ga4b43ef0f30146808e560991a302e88ad)

bt\_security\_t bt\_conn\_get\_security(const struct bt\_conn \*conn)

Get security level for a connection.

[bt\_conn\_le\_cs\_capability\_rtt\_random\_payload](group__bt__conn.md#ga5568443825fc1ce9534753d8918aa813)

bt\_conn\_le\_cs\_capability\_rtt\_random\_payload

Supported Random Payload RTT precision.

**Definition** conn.h:286

[bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043)

bt\_conn\_auth\_keypress

Passkey Keypress Notification type.

**Definition** conn.h:1024

[bt\_conn\_foreach](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916)

void bt\_conn\_foreach(enum bt\_conn\_type type, void(\*func)(struct bt\_conn \*conn, void \*data), void \*data)

Iterate through all bt\_conn objects.

[bt\_conn\_create\_auto\_stop](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4)

int bt\_conn\_create\_auto\_stop(void)

Stop automatic connect creation.

[bt\_conn\_le\_cs\_subevent\_abort\_reason](group__bt__conn.md#ga6394906c6da40c9bebfaeb05de9fd5be)

bt\_conn\_le\_cs\_subevent\_abort\_reason

Subevent abort reason.

**Definition** conn.h:567

[bt\_conn\_le\_set\_path\_loss\_mon\_param](group__bt__conn.md#ga6be5f3bf064ba03dc2307fdd2b634637)

int bt\_conn\_le\_set\_path\_loss\_mon\_param(struct bt\_conn \*conn, const struct bt\_conn\_le\_path\_loss\_reporting\_param \*param)

Set Path Loss Monitoring Parameters.

[bt\_conn\_get\_remote\_info](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92)

int bt\_conn\_get\_remote\_info(struct bt\_conn \*conn, struct bt\_conn\_remote\_info \*remote\_info)

Get connection info for the remote device.

[bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190)

bt\_conn\_le\_tx\_power\_phy

**Definition** conn.h:906

[bt\_conn\_le\_subrate\_request](group__bt__conn.md#ga754ed218fe9577f2d0ef6d508cfc5a0b)

int bt\_conn\_le\_subrate\_request(struct bt\_conn \*conn, const struct bt\_conn\_le\_subrate\_param \*params)

Request New Subrating Parameters.

[bt\_conn\_get\_dst](group__bt__conn.md#ga77108581b8f61485ca840e4bf7a17087)

const bt\_addr\_le\_t \* bt\_conn\_get\_dst(const struct bt\_conn \*conn)

Get destination (peer) address of a connection.

[bt\_conn\_auth\_cb\_overlay](group__bt__conn.md#ga81077385583d71c248a1eb6aab9ee86e)

int bt\_conn\_auth\_cb\_overlay(struct bt\_conn \*conn, const struct bt\_conn\_auth\_cb \*cb)

Overlay authentication callbacks used for a given connection.

[bt\_conn\_auth\_cancel](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59)

int bt\_conn\_auth\_cancel(struct bt\_conn \*conn)

Cancel ongoing authenticated pairing.

[bt\_conn\_le\_data\_len\_update](group__bt__conn.md#ga8a2006f6e34b20c7e8ef65a73f431a57)

int bt\_conn\_le\_data\_len\_update(struct bt\_conn \*conn, const struct bt\_conn\_le\_data\_len\_param \*param)

Update the connection transmit data length parameters.

[bt\_conn\_le\_create](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6)

int bt\_conn\_le\_create(const bt\_addr\_le\_t \*peer, const struct bt\_conn\_le\_create\_param \*create\_param, const struct bt\_le\_conn\_param \*conn\_param, struct bt\_conn \*\*conn)

Initiate an LE connection to a remote device.

[bt\_conn\_le\_cs\_subevent\_done\_status](group__bt__conn.md#ga8e54a191b889b1d5ed3e1fbb648d9bc7)

bt\_conn\_le\_cs\_subevent\_done\_status

Subevent done status.

**Definition** conn.h:549

[bt\_le\_set\_auto\_conn](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a)

int bt\_le\_set\_auto\_conn(const bt\_addr\_le\_t \*addr, const struct bt\_le\_conn\_param \*param)

Automatically connect to remote device if it's in range.

[bt\_conn\_le\_set\_path\_loss\_mon\_enable](group__bt__conn.md#ga90ae27bcc6f71f32be56efe8ecbc165d)

int bt\_conn\_le\_set\_path\_loss\_mon\_enable(struct bt\_conn \*conn, bool enable)

Enable or Disable Path Loss Monitoring.

[bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282)

bt\_conn\_state

**Definition** conn.h:794

[bt\_le\_oob\_set\_legacy\_flag](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892)

void bt\_le\_oob\_set\_legacy\_flag(bool enable)

Allow/disallow remote legacy OOB data to be used for pairing.

[bt\_conn\_le\_create\_synced](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1)

int bt\_conn\_le\_create\_synced(const struct bt\_le\_ext\_adv \*adv, const struct bt\_conn\_le\_create\_synced\_param \*synced\_param, const struct bt\_le\_conn\_param \*conn\_param, struct bt\_conn \*\*conn)

Create a connection to a synced device.

[bt\_conn\_le\_cs\_procedure\_done\_status](group__bt__conn.md#ga9a1dc2010c5237466de87160944630d3)

bt\_conn\_le\_cs\_procedure\_done\_status

Procedure done status.

**Definition** conn.h:542

[bt\_conn\_le\_set\_tx\_power\_report\_enable](group__bt__conn.md#gaa1f38911acee0534a8a6e414018c6fb6)

int bt\_conn\_le\_set\_tx\_power\_report\_enable(struct bt\_conn \*conn, bool local\_enable, bool remote\_enable)

Enable transmit power reporting.

[bt\_conn\_le\_get\_tx\_power\_level](group__bt__conn.md#gaa5289154bc508444f68df7abcef18aca)

int bt\_conn\_le\_get\_tx\_power\_level(struct bt\_conn \*conn, struct bt\_conn\_le\_tx\_power \*tx\_power\_level)

Get connection transmit power level.

[bt\_conn\_le\_enhanced\_get\_tx\_power\_level](group__bt__conn.md#gaa79eada87d698f4998af876d03d7e92b)

int bt\_conn\_le\_enhanced\_get\_tx\_power\_level(struct bt\_conn \*conn, struct bt\_conn\_le\_tx\_power \*tx\_power)

Get local enhanced connection transmit power level.

[bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff)

bt\_security\_err

**Definition** conn.h:1493

[bt\_conn\_cb\_register](group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b)

int bt\_conn\_cb\_register(struct bt\_conn\_cb \*cb)

Register connection callbacks.

[bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb)

bt\_conn\_le\_cs\_sync\_phy

Channel sounding PHY used for CS sync.

**Definition** conn.h:465

[bt\_conn\_le\_param\_update](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb)

int bt\_conn\_le\_param\_update(struct bt\_conn \*conn, const struct bt\_le\_conn\_param \*param)

Update the connection parameters.

[bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c)

bt\_conn\_le\_cs\_tone\_antenna\_config\_selection

CS Test Tone Antennna Config Selection.

**Definition** conn.h:1557

[bt\_conn\_auth\_passkey\_confirm](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995)

int bt\_conn\_auth\_passkey\_confirm(struct bt\_conn \*conn)

Reply if passkey was confirmed to match by user.

[bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20)

bt\_conn\_type

Connection Type.

**Definition** conn.h:251

[bt\_le\_oob\_set\_sc\_data](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503)

int bt\_le\_oob\_set\_sc\_data(struct bt\_conn \*conn, const struct bt\_le\_oob\_sc\_data \*oobd\_local, const struct bt\_le\_oob\_sc\_data \*oobd\_remote)

Set OOB data during LE Secure Connections (SC) pairing procedure.

[bt\_conn\_auth\_info\_cb\_register](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f)

int bt\_conn\_auth\_info\_cb\_register(struct bt\_conn\_auth\_info\_cb \*cb)

Register authentication information callbacks.

[bt\_conn\_auth\_info\_cb\_unregister](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37)

int bt\_conn\_auth\_info\_cb\_unregister(struct bt\_conn\_auth\_info\_cb \*cb)

Unregister authentication information callbacks.

[bt\_conn\_le\_subrate\_set\_defaults](group__bt__conn.md#gac7bb456c530c7e08b4fa9f4d478fdaf9)

int bt\_conn\_le\_subrate\_set\_defaults(const struct bt\_conn\_le\_subrate\_param \*params)

Set Default Connection Subrating Parameters.

[bt\_le\_oob\_set\_sc\_flag](group__bt__conn.md#gad02f8fe587efd543c0c81cace3f63d63)

void bt\_le\_oob\_set\_sc\_flag(bool enable)

Allow/disallow remote LE SC OOB data to be used for pairing.

[bt\_conn\_cb\_unregister](group__bt__conn.md#gad2f90b34390e3c3697fd455ae4ef5f31)

int bt\_conn\_cb\_unregister(struct bt\_conn\_cb \*cb)

Unregister connection callbacks.

[bt\_conn\_index](group__bt__conn.md#gad4aed76b80cc815f748ad0e84ae3d87c)

uint8\_t bt\_conn\_index(const struct bt\_conn \*conn)

Get array index of a connection.

[bt\_conn\_set\_security](group__bt__conn.md#gae001f1268e1ff42c3c974c95dcb6735d)

int bt\_conn\_set\_security(struct bt\_conn \*conn, bt\_security\_t sec)

Set security level for a connection.

[bt\_conn\_le\_phy\_update](group__bt__conn.md#gae13ed81b1e7928f44b8fdf85995b3e58)

int bt\_conn\_le\_phy\_update(struct bt\_conn \*conn, const struct bt\_conn\_le\_phy\_param \*param)

Update the connection PHY parameters.

[bt\_conn\_le\_create\_auto](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b)

int bt\_conn\_le\_create\_auto(const struct bt\_conn\_le\_create\_param \*create\_param, const struct bt\_le\_conn\_param \*conn\_param)

Automatically connect to remote devices in the filter accept list.

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:806

[bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b)

bt\_conn\_le\_cs\_ch3c\_shape

Channel sounding channel sequence shape.

**Definition** conn.h:483

[bt\_conn\_le\_cs\_procedure\_enable\_state](group__bt__conn.md#gaf3653de72793f775e33fd9eb04c3e7a2)

bt\_conn\_le\_cs\_procedure\_enable\_state

**Definition** conn.h:1525

[bt\_conn\_le\_path\_loss\_zone](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)

bt\_conn\_le\_path\_loss\_zone

Path Loss zone that has been entered.

**Definition** conn.h:976

[bt\_conn\_create\_br](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9)

struct bt\_conn \* bt\_conn\_create\_br(const bt\_addr\_t \*peer, const struct bt\_br\_conn\_param \*param)

Initiate an BR/EDR connection to a remote device.

[bt\_conn\_le\_cs\_capability\_rtt\_aa\_only](group__bt__conn.md#gafe14d64a64383b097760764697b035e2)

bt\_conn\_le\_cs\_capability\_rtt\_aa\_only

Supported AA-Only RTT precision.

**Definition** conn.h:266

[bt\_conn\_enc\_key\_size](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e)

uint8\_t bt\_conn\_enc\_key\_size(const struct bt\_conn \*conn)

Get encryption key size.

[bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51)

bt\_conn\_le\_cs\_rtt\_type

Channel sounding RTT type.

**Definition** conn.h:447

[BT\_CONN\_LE\_CS\_SUB\_MODE\_3](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafa132f05ddbf885086e7bee500608d8797)

@ BT\_CONN\_LE\_CS\_SUB\_MODE\_3

Mode-3 (RTT and PBR).

**Definition** conn.h:435

[BT\_CONN\_LE\_CS\_SUB\_MODE\_UNUSED](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafac1b24ef35efc9222771f45422b2e8f24)

@ BT\_CONN\_LE\_CS\_SUB\_MODE\_UNUSED

Unused.

**Definition** conn.h:429

[BT\_CONN\_LE\_CS\_SUB\_MODE\_1](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafaf23b70be00b04f15fe9b38190e26b49c)

@ BT\_CONN\_LE\_CS\_SUB\_MODE\_1

Mode-1 (RTT).

**Definition** conn.h:431

[BT\_CONN\_LE\_CS\_SUB\_MODE\_2](group__bt__conn.md#gga07c6f1248c9a6da0168bd3d398925dafaf894463ad77a424ddba3d5f4edfdd3e8)

@ BT\_CONN\_LE\_CS\_SUB\_MODE\_2

Mode-2 (PBR).

**Definition** conn.h:433

[BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34)

@ BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2

LE Coded using S=2 coding preferred when transmitting.

**Definition** conn.h:93

[BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0)

@ BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8

LE Coded using S=8 coding preferred when transmitting.

**Definition** conn.h:96

[BT\_CONN\_LE\_PHY\_OPT\_NONE](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98)

@ BT\_CONN\_LE\_PHY\_OPT\_NONE

Convenience value when no options are specified.

**Definition** conn.h:90

[BT\_CONN\_LE\_CS\_ROLE\_REFLECTOR](group__bt__conn.md#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968)

@ BT\_CONN\_LE\_CS\_ROLE\_REFLECTOR

CS reflector role.

**Definition** conn.h:443

[BT\_CONN\_LE\_CS\_ROLE\_INITIATOR](group__bt__conn.md#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4)

@ BT\_CONN\_LE\_CS\_ROLE\_INITIATOR

CS initiator role.

**Definition** conn.h:441

[BT\_CONN\_LE\_CS\_MAIN\_MODE\_1](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fa206d9eebf020d9743767b66a5f5a023d)

@ BT\_CONN\_LE\_CS\_MAIN\_MODE\_1

Mode-1 (RTT).

**Definition** conn.h:419

[BT\_CONN\_LE\_CS\_MAIN\_MODE\_2](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fa5a60c772a06c6f8925344dac63f592c6)

@ BT\_CONN\_LE\_CS\_MAIN\_MODE\_2

Mode-2 (PBR).

**Definition** conn.h:421

[BT\_CONN\_LE\_CS\_MAIN\_MODE\_3](group__bt__conn.md#gga133504278b6e01993ff36e96a238484fafebd88560cfcce6ba2eb48976e220c4a)

@ BT\_CONN\_LE\_CS\_MAIN\_MODE\_3

Mode-3 (RTT and PBR).

**Definition** conn.h:423

[BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_150NS](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584)

@ BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_150NS

150ns time-of-flight accuracy.

**Definition** conn.h:282

[BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_NOT\_SUPP](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14)

@ BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_NOT\_SUPP

Sounding Sequence RTT variant is not supported.

**Definition** conn.h:278

[BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_10NS](group__bt__conn.md#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb)

@ BT\_CONN\_LE\_CS\_RTT\_SOUNDING\_10NS

10ns time-of-flight accuracy.

**Definition** conn.h:280

[BT\_SECURITY\_FLAG\_OOB](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198)

@ BT\_SECURITY\_FLAG\_OOB

Paired with Out of Band method.

**Definition** conn.h:828

[BT\_SECURITY\_FLAG\_SC](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6)

@ BT\_SECURITY\_FLAG\_SC

Paired with Secure Connections.

**Definition** conn.h:826

[BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_REQUESTED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_REQUESTED

**Definition** conn.h:557

[BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_TOO\_FEW\_CHANNELS](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_TOO\_FEW\_CHANNELS

**Definition** conn.h:559

[BT\_CONN\_LE\_CS\_PROCEDURE\_NOT\_ABORTED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_NOT\_ABORTED

**Definition** conn.h:556

[BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_UNSPECIFIED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_UNSPECIFIED

**Definition** conn.h:563

[BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_CHMAP\_INSTANT\_PASSED](group__bt__conn.md#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_ABORT\_CHMAP\_INSTANT\_PASSED

**Definition** conn.h:561

[BT\_CONN\_LE\_CS\_CHSEL\_TYPE\_3C](group__bt__conn.md#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6)

@ BT\_CONN\_LE\_CS\_CHSEL\_TYPE\_3C

Use Channel Selection Algorithm #3c for non-mode-0 CS steps.

**Definition** conn.h:479

[BT\_CONN\_LE\_CS\_CHSEL\_TYPE\_3B](group__bt__conn.md#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1)

@ BT\_CONN\_LE\_CS\_CHSEL\_TYPE\_3B

Use Channel Selection Algorithm #3b for non-mode-0 CS steps.

**Definition** conn.h:477

[BT\_CONN\_LE\_OPT\_NONE](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)

@ BT\_CONN\_LE\_OPT\_NONE

Convenience value when no options are specified.

**Definition** conn.h:1226

[BT\_CONN\_LE\_OPT\_NO\_1M](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9)

@ BT\_CONN\_LE\_OPT\_NO\_1M

Disable LE 1M PHY.

**Definition** conn.h:1240

[BT\_CONN\_LE\_OPT\_CODED](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b)

@ BT\_CONN\_LE\_OPT\_CODED

Enable LE Coded PHY.

**Definition** conn.h:1232

[BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_10NS](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741)

@ BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_10NS

10ns time-of-flight accuracy.

**Definition** conn.h:290

[BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_NOT\_SUPP](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d)

@ BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_NOT\_SUPP

Random Payload RTT variant is not supported.

**Definition** conn.h:288

[BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_150NS](group__bt__conn.md#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db)

@ BT\_CONN\_LE\_CS\_RTT\_RANDOM\_PAYLOAD\_150NS

150ns time-of-flight accuracy.

**Definition** conn.h:292

[BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529)

@ BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED

**Definition** conn.h:1027

[BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1)

@ BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED

**Definition** conn.h:1026

[BT\_CONN\_AUTH\_KEYPRESS\_CLEARED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da)

@ BT\_CONN\_AUTH\_KEYPRESS\_CLEARED

**Definition** conn.h:1028

[BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6)

@ BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED

**Definition** conn.h:1025

[BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8)

@ BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED

**Definition** conn.h:1029

[BT\_CONN\_LE\_CS\_SUBEVENT\_NOT\_ABORTED](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_NOT\_ABORTED

**Definition** conn.h:568

[BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_UNSPECIFIED](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_UNSPECIFIED

**Definition** conn.h:575

[BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_REQUESTED](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_REQUESTED

**Definition** conn.h:569

[BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_SCHED\_CONFLICT](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_SCHED\_CONFLICT

**Definition** conn.h:573

[BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_NO\_CS\_SYNC](group__bt__conn.md#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_ABORT\_NO\_CS\_SYNC

**Definition** conn.h:571

[BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE

Convenience macro for when no PHY is set.

**Definition** conn.h:908

[BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2

LE Coded PHY using S=2 coding.

**Definition** conn.h:916

[BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8

LE Coded PHY using S=8 coding.

**Definition** conn.h:914

[BT\_CONN\_LE\_TX\_POWER\_PHY\_1M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_1M

LE 1M PHY.

**Definition** conn.h:910

[BT\_CONN\_LE\_TX\_POWER\_PHY\_2M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_2M

LE 2M PHY.

**Definition** conn.h:912

[BT\_CONN\_LE\_CS\_SUBEVENT\_ABORTED](group__bt__conn.md#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_ABORTED

**Definition** conn.h:551

[BT\_CONN\_LE\_CS\_SUBEVENT\_COMPLETE](group__bt__conn.md#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146)

@ BT\_CONN\_LE\_CS\_SUBEVENT\_COMPLETE

**Definition** conn.h:550

[BT\_CONN\_STATE\_CONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd)

@ BT\_CONN\_STATE\_CONNECTING

Channel in connecting state.

**Definition** conn.h:798

[BT\_CONN\_STATE\_CONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f)

@ BT\_CONN\_STATE\_CONNECTED

Channel connected and ready for upper layer traffic on it.

**Definition** conn.h:800

[BT\_CONN\_STATE\_DISCONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587)

@ BT\_CONN\_STATE\_DISCONNECTED

Channel disconnected.

**Definition** conn.h:796

[BT\_CONN\_STATE\_DISCONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f)

@ BT\_CONN\_STATE\_DISCONNECTING

Channel in disconnecting state.

**Definition** conn.h:802

[BT\_CONN\_LE\_CS\_PROCEDURE\_ABORTED](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_ABORTED

**Definition** conn.h:545

[BT\_CONN\_LE\_CS\_PROCEDURE\_COMPLETE](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_COMPLETE

**Definition** conn.h:543

[BT\_CONN\_LE\_CS\_PROCEDURE\_INCOMPLETE](group__bt__conn.md#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82)

@ BT\_CONN\_LE\_CS\_PROCEDURE\_INCOMPLETE

**Definition** conn.h:544

[BT\_CONN\_ROLE\_PERIPHERAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0)

@ BT\_CONN\_ROLE\_PERIPHERAL

**Definition** conn.h:791

[BT\_CONN\_ROLE\_CENTRAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)

@ BT\_CONN\_ROLE\_CENTRAL

**Definition** conn.h:790

[BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7)

@ BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE

OOB data is not available.

**Definition** conn.h:1504

[BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae)

@ BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT

The requested security level could not be reached.

**Definition** conn.h:1507

[BT\_SECURITY\_ERR\_KEY\_REJECTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216)

@ BT\_SECURITY\_ERR\_KEY\_REJECTED

Distributed Key Rejected.

**Definition** conn.h:1519

[BT\_SECURITY\_ERR\_UNSPECIFIED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)

@ BT\_SECURITY\_ERR\_UNSPECIFIED

Pairing failed but the exact reason could not be specified.

**Definition** conn.h:1522

[BT\_SECURITY\_ERR\_INVALID\_PARAM](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5)

@ BT\_SECURITY\_ERR\_INVALID\_PARAM

Invalid parameters.

**Definition** conn.h:1516

[BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6)

@ BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED

Pairing is not supported.

**Definition** conn.h:1510

[BT\_SECURITY\_ERR\_AUTH\_FAIL](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7)

@ BT\_SECURITY\_ERR\_AUTH\_FAIL

Authentication failed.

**Definition** conn.h:1498

[BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171)

@ BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING

PIN or encryption key is missing.

**Definition** conn.h:1501

[BT\_SECURITY\_ERR\_SUCCESS](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05)

@ BT\_SECURITY\_ERR\_SUCCESS

Security procedure successful.

**Definition** conn.h:1495

[BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f)

@ BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED

Pairing is not allowed.

**Definition** conn.h:1513

[BT\_CONN\_LE\_CS\_SYNC\_1M\_PHY](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95)

@ BT\_CONN\_LE\_CS\_SYNC\_1M\_PHY

LE 1M PHY.

**Definition** conn.h:467

[BT\_CONN\_LE\_CS\_SYNC\_2M\_PHY](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6)

@ BT\_CONN\_LE\_CS\_SYNC\_2M\_PHY

LE 2M PHY.

**Definition** conn.h:469

[BT\_CONN\_LE\_CS\_SYNC\_2M\_2BT\_PHY](group__bt__conn.md#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b)

@ BT\_CONN\_LE\_CS\_SYNC\_2M\_2BT\_PHY

LE 2M 2BT PHY.

**Definition** conn.h:471

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_TWO](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca172dde37f3e1368fd00d2bed86c4ae7b)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_TWO

**Definition** conn.h:1559

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_FIVE](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca6256d88a5a4c8b9c63625dfc0e251da0)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_FIVE

**Definition** conn.h:1562

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_SEVEN](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca6aac8dc77fccbc6a89226341a85bbdcc)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_SEVEN

**Definition** conn.h:1564

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_FOUR](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591ca967ebe063b0ae1d4249e67fcbea9fa18)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_FOUR

**Definition** conn.h:1561

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_EIGHT](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591caae7087f9165279af27e64676a54eaea3)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_EIGHT

**Definition** conn.h:1565

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_SIX](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591cab26feeda58c2275dd857c10a7029dc83)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_SIX

**Definition** conn.h:1563

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_ONE](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591cac8e353ad7af2b410aebf02aaa5d5f2c4)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_ONE

**Definition** conn.h:1558

[BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_THREE](group__bt__conn.md#ggab7acdbdf273fc760799cf0d8cf71591caf6bd13c55ac53af42ff9035221a91fc4)

@ BT\_LE\_CS\_TONE\_ANTENNA\_CONFIGURATION\_INDEX\_THREE

**Definition** conn.h:1560

[BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)

@ BT\_CONN\_TYPE\_LE

LE Connection Type.

**Definition** conn.h:253

[BT\_CONN\_TYPE\_ALL](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)

@ BT\_CONN\_TYPE\_ALL

All Connection Type.

**Definition** conn.h:261

[BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)

@ BT\_CONN\_TYPE\_BR

BR/EDR Connection Type.

**Definition** conn.h:255

[BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)

@ BT\_CONN\_TYPE\_ISO

ISO Connection Type.

**Definition** conn.h:259

[BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953)

@ BT\_CONN\_TYPE\_SCO

SCO Connection Type.

**Definition** conn.h:257

[BT\_SECURITY\_L4](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81)

@ BT\_SECURITY\_L4

Level 4: Authenticated Secure Connections and 128-bit key.

**Definition** conn.h:816

[BT\_SECURITY\_L0](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e)

@ BT\_SECURITY\_L0

Level 0: Only for BR/EDR special cases, like SDP.

**Definition** conn.h:808

[BT\_SECURITY\_L3](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631)

@ BT\_SECURITY\_L3

Level 3: Encryption and authentication (MITM).

**Definition** conn.h:814

[BT\_SECURITY\_FORCE\_PAIR](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae)

@ BT\_SECURITY\_FORCE\_PAIR

Bit to force new pairing procedure, bit-wise OR with requested security level.

**Definition** conn.h:820

[BT\_SECURITY\_L1](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b)

@ BT\_SECURITY\_L1

Level 1: No encryption and no authentication.

**Definition** conn.h:810

[BT\_SECURITY\_L2](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a)

@ BT\_SECURITY\_L2

Level 2: Encryption and no authentication (no MITM).

**Definition** conn.h:812

[BT\_CONN\_LE\_CS\_CH3C\_SHAPE\_HAT](group__bt__conn.md#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea)

@ BT\_CONN\_LE\_CS\_CH3C\_SHAPE\_HAT

Use Hat shape for user-specified channel sequence.

**Definition** conn.h:485

[BT\_CONN\_LE\_CS\_CH3C\_SHAPE\_X](group__bt__conn.md#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622)

@ BT\_CONN\_LE\_CS\_CH3C\_SHAPE\_X

Use X shape for user-specified channel sequence.

**Definition** conn.h:487

[BT\_CONN\_LE\_CS\_PROCEDURES\_ENABLED](group__bt__conn.md#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac)

@ BT\_CONN\_LE\_CS\_PROCEDURES\_ENABLED

**Definition** conn.h:1527

[BT\_CONN\_LE\_CS\_PROCEDURES\_DISABLED](group__bt__conn.md#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83)

@ BT\_CONN\_LE\_CS\_PROCEDURES\_DISABLED

**Definition** conn.h:1526

[BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_MIDDLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec)

@ BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_MIDDLE

Middle path loss zone entered.

**Definition** conn.h:980

[BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_LOW](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8)

@ BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_LOW

Low path loss zone entered.

**Definition** conn.h:978

[BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_HIGH](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705)

@ BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_HIGH

High path loss zone entered.

**Definition** conn.h:982

[BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_UNAVAILABLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942)

@ BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_UNAVAILABLE

Path loss has become unavailable.

**Definition** conn.h:984

[BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_NOT\_SUPP](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94)

@ BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_NOT\_SUPP

AA-Only RTT variant is not supported.

**Definition** conn.h:268

[BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_150NS](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6)

@ BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_150NS

150ns time-of-flight accuracy.

**Definition** conn.h:272

[BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_10NS](group__bt__conn.md#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a)

@ BT\_CONN\_LE\_CS\_RTT\_AA\_ONLY\_10NS

10ns time-of-flight accuracy.

**Definition** conn.h:270

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_SOUNDING](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_SOUNDING

RTT with 96-bit sounding sequence.

**Definition** conn.h:453

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_SOUNDING](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_SOUNDING

RTT with 32-bit sounding sequence.

**Definition** conn.h:451

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_128\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_128\_BIT\_RANDOM

RTT with 128-bit random sequence.

**Definition** conn.h:461

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_AA\_ONLY](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_AA\_ONLY

RTT AA only.

**Definition** conn.h:449

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_96\_BIT\_RANDOM

RTT with 96-bit random sequence.

**Definition** conn.h:459

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_32\_BIT\_RANDOM

RTT with 32-bit random sequence.

**Definition** conn.h:455

[BT\_CONN\_LE\_CS\_RTT\_TYPE\_64\_BIT\_RANDOM](group__bt__conn.md#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91)

@ BT\_CONN\_LE\_CS\_RTT\_TYPE\_64\_BIT\_RANDOM

RTT with 64-bit random sequence.

**Definition** conn.h:457

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[hci\_types.h](hci__types_8h.md)

[BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT](hci__types_8h.md#a056a67d663cfdc2189b480fc79946c74)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_NO\_ABORT

**Definition** hci\_types.h:3599

[BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT](hci__types_8h.md#a095b6061c31229b951b6b96e5d02381f)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_ABORT

**Definition** hci\_types.h:3605

[BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED](hci__types_8h.md#a1e92177f7be3c6a6be00f97fbfc17dcf)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_UNSPECIFIED

**Definition** hci\_types.h:3603

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND](hci__types_8h.md#a1fe5e94fbd1156c8196c8e1ab9816bac)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_128BIT\_RAND

**Definition** hci\_types.h:2563

[BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1](hci__types_8h.md#a219243d501bbcb6d62668398cde79fca)

#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_1

**Definition** hci\_types.h:2549

[BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST](hci__types_8h.md#a21eb191c5d99f902c7a244cad685995f)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST

**Definition** hci\_types.h:3600

[BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT](hci__types_8h.md#a31cb520a05fe31313bacf8b021da468c)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_SCHED\_CONFLICT

**Definition** hci\_types.h:3608

[BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED](hci__types_8h.md#a3e01bbe3a72c946015a288ee49d3cbdd)

#define BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_DISABLED

**Definition** hci\_types.h:2534

[BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST](hci__types_8h.md#a41bbe08db99fb0a2ef77f4f3103f9b6c)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_LOCAL\_HOST\_OR\_REMOTE\_REQUEST

**Definition** hci\_types.h:3606

[BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED](hci__types_8h.md#a4a88120ae7e83fd791012c913315d14f)

#define BT\_HCI\_OP\_LE\_CS\_PROCEDURES\_ENABLED

**Definition** hci\_types.h:2535

[BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3](hci__types_8h.md#a4b48c199b6b75e9dd62ec36883b40aa4)

#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_3

**Definition** hci\_types.h:2551

[BT\_HCI\_OP\_LE\_CS\_ACI\_6](hci__types_8h.md#a4c7ff3c949023f4544bf50353a0f082b)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_6

**Definition** hci\_types.h:2578

[BT\_HCI\_OP\_LE\_CS\_ACI\_1](hci__types_8h.md#a5b082fa5b8ba11a651468cc516d067fe)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_1

**Definition** hci\_types.h:2573

[BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3](hci__types_8h.md#a5d2af0ed5e0cc5cf7d9f0baae512ff68)

#define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_3

**Definition** hci\_types.h:2547

[BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS](hci__types_8h.md#a6dc3f766ce40bbd0ddb7af3cf85677b1)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_TOO\_FEW\_CHANNELS

**Definition** hci\_types.h:3601

[BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2](hci__types_8h.md#a714152a085bbc317b539d6e973ccffc6)

#define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_2

**Definition** hci\_types.h:2546

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND](hci__types_8h.md#a73cbfe2a942b684ac0b5b50d900fb83f)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_SOUND

**Definition** hci\_types.h:2559

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY](hci__types_8h.md#a759eb7a8e43ee7cf1ea88ddd3e69feb5)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_AA\_ONLY

**Definition** hci\_types.h:2557

[BT\_HCI\_OP\_LE\_CS\_ACI\_3](hci__types_8h.md#a76d1452003c0bd3b688765aa2d25047f)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_3

**Definition** hci\_types.h:2575

[BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B](hci__types_8h.md#a77d27762b9faa7743a55d822a1839eac)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3B

**Definition** hci\_types.h:2605

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND](hci__types_8h.md#a77e56fd5302673f6ef295c0cceabdc9f)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_64BIT\_RAND

**Definition** hci\_types.h:2561

[BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M](hci__types_8h.md#a7baf90f5bf691ce6b650677e6c2a9600)

#define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_1M

**Definition** hci\_types.h:2565

[BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED](hci__types_8h.md#a821a29dacea9867e4e576f916cf7be3d)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_ABORTED

**Definition** hci\_types.h:3593

[BT\_HCI\_OP\_LE\_CS\_ACI\_0](hci__types_8h.md#a92e1ec21014999f40172fa1812c36575)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_0

**Definition** hci\_types.h:2572

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND](hci__types_8h.md#aa2ae18252a20ef3481d2402f8924cdda)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_SOUND

**Definition** hci\_types.h:2558

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND](hci__types_8h.md#aa60f64ff7259fd79fb1da2c063530348)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_96BIT\_RAND

**Definition** hci\_types.h:2562

[BT\_HCI\_OP\_LE\_CS\_ACI\_2](hci__types_8h.md#ab30a4e55002080394c39fb885eba36e4)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_2

**Definition** hci\_types.h:2574

[BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED](hci__types_8h.md#ab3fce1eb448b0ade581e4e12b2d56039)

#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_UNUSED

**Definition** hci\_types.h:2552

[BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE](hci__types_8h.md#ab88f3d713f6862c08b73752436ca8b1b)

#define BT\_HCI\_LE\_ZONE\_ENTERED\_MIDDLE

**Definition** hci\_types.h:3403

[BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND](hci__types_8h.md#abe4efee7cf9371129f4b5bd650b0d64a)

#define BT\_HCI\_OP\_LE\_CS\_RTT\_TYPE\_32BIT\_RAND

**Definition** hci\_types.h:2560

[BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED](hci__types_8h.md#abfdca3ae615e19c8e24c098ba8349618)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_UNSPECIFIED

**Definition** hci\_types.h:3609

[BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT](hci__types_8h.md#ac34716156b071e06eb454f091a63216c)

#define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M\_2BT

**Definition** hci\_types.h:2567

[BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED](hci__types_8h.md#ac4817c265c50019d8f74146f7477bf58)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_ABORT\_REASON\_NO\_CS\_SYNC\_RECEIVED

**Definition** hci\_types.h:3607

[BT\_HCI\_OP\_LE\_CS\_ACI\_7](hci__types_8h.md#acabccf9f5893324dcb6acc0769ab8417)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_7

**Definition** hci\_types.h:2579

[BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT](hci__types_8h.md#acd33fc2eb3f5ebe10cbe4c5060f8336b)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_HAT

**Definition** hci\_types.h:2608

[BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE](hci__types_8h.md#ace872d54fba6d94d62b59a2373c7d0d5)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_COMPLETE

**Definition** hci\_types.h:3591

[BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X](hci__types_8h.md#ad09c735ab352d7a546cade296e915e85)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_CH3C\_SHAPE\_X

**Definition** hci\_types.h:2609

[BT\_HCI\_OP\_LE\_CS\_ACI\_5](hci__types_8h.md#ad980d8f134d940b80dc9b0e3a570ac06)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_5

**Definition** hci\_types.h:2577

[BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2](hci__types_8h.md#ada09c787fca0a1d54bb754635489b51e)

#define BT\_HCI\_OP\_LE\_CS\_SUB\_MODE\_2

**Definition** hci\_types.h:2550

[BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M](hci__types_8h.md#ae49d35db87532e06ea685a63eb89177a)

#define BT\_HCI\_OP\_LE\_CS\_CS\_SYNC\_2M

**Definition** hci\_types.h:2566

[BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED](hci__types_8h.md#ae8446a2638bd4009b7dee725bb54c883)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_ABORT\_REASON\_CHMAP\_INSTANT\_PASSED

**Definition** hci\_types.h:3602

[BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE](hci__types_8h.md#aee251ce3c46dc0404d880be7d4550fa6)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_COMPLETE

**Definition** hci\_types.h:3595

[BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL](hci__types_8h.md#af057e8492e52d0c8763d4a2e969d949d)

#define BT\_HCI\_LE\_CS\_PROCEDURE\_DONE\_STATUS\_PARTIAL

**Definition** hci\_types.h:3592

[BT\_HCI\_OP\_LE\_CS\_ACI\_4](hci__types_8h.md#af16c4c79e602e6da833b8aa3e0c4bf64)

#define BT\_HCI\_OP\_LE\_CS\_ACI\_4

**Definition** hci\_types.h:2576

[BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C](hci__types_8h.md#af17f867204bc7cf99e5d530c39302be0)

#define BT\_HCI\_OP\_LE\_CS\_TEST\_CHSEL\_TYPE\_3C

**Definition** hci\_types.h:2606

[BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED](hci__types_8h.md#af1907f8ae481a08c674d86e689826f49)

#define BT\_HCI\_LE\_CS\_SUBEVENT\_DONE\_STATUS\_ABORTED

**Definition** hci\_types.h:3597

[BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1](hci__types_8h.md#af1b7924e50ba017e59d697fd8814d491)

#define BT\_HCI\_OP\_LE\_CS\_MAIN\_MODE\_1

**Definition** hci\_types.h:2545

[BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH](hci__types_8h.md#af7cc15be8165315ee0358ebb517b5e33)

#define BT\_HCI\_LE\_ZONE\_ENTERED\_HIGH

**Definition** hci\_types.h:3404

[BT\_HCI\_LE\_ZONE\_ENTERED\_LOW](hci__types_8h.md#aff1538e314a97aa4910d4f7066dc4d55)

#define BT\_HCI\_LE\_ZONE\_ENTERED\_LOW

**Definition** hci\_types.h:3402

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_br\_conn\_param](structbt__br__conn__param.md)

Connection parameters for BR/EDR connections.

**Definition** conn.h:2529

[bt\_br\_conn\_param::allow\_role\_switch](structbt__br__conn__param.md#a95454a74932a14b4137c3fe82821be49)

bool allow\_role\_switch

**Definition** conn.h:2530

[bt\_conn\_auth\_cb](structbt__conn__auth__cb.md)

Authenticated pairing callback structure.

**Definition** conn.h:2174

[bt\_conn\_auth\_cb::passkey\_entry](structbt__conn__auth__cb.md#a10f9d22c89c95a6f3ffe0016f92445c0)

void(\* passkey\_entry)(struct bt\_conn \*conn)

Request the user to enter a passkey.

**Definition** conn.h:2271

[bt\_conn\_auth\_cb::passkey\_display](structbt__conn__auth__cb.md#a14074ca97fad6af4c58c43a00c503104)

void(\* passkey\_display)(struct bt\_conn \*conn, unsigned int passkey)

Display a passkey to the user.

**Definition** conn.h:2225

[bt\_conn\_auth\_cb::passkey\_confirm](structbt__conn__auth__cb.md#a2bb6c10666d111f675fd6de5ff51410a)

void(\* passkey\_confirm)(struct bt\_conn \*conn, unsigned int passkey)

Request the user to confirm a passkey.

**Definition** conn.h:2294

[bt\_conn\_auth\_cb::pairing\_accept](structbt__conn__auth__cb.md#a92391a172e158a42966f410d732424a7)

enum bt\_security\_err(\* pairing\_accept)(struct bt\_conn \*conn, const struct bt\_conn\_pairing\_feat \*const feat)

Query to proceed incoming pairing or not.

**Definition** conn.h:2203

[bt\_conn\_auth\_cb::pincode\_entry](structbt__conn__auth__cb.md#ab6df1b1505dc22dd8dae0e946546c8bb)

void(\* pincode\_entry)(struct bt\_conn \*conn, bool highsec)

Request the user to enter a passkey.

**Definition** conn.h:2368

[bt\_conn\_auth\_cb::oob\_data\_request](structbt__conn__auth__cb.md#aec9f6256607ea2cd1ce1b4cdb3052b42)

void(\* oob\_data\_request)(struct bt\_conn \*conn, struct bt\_conn\_oob\_info \*info)

Request the user to provide Out of Band (OOB) data.

**Definition** conn.h:2312

[bt\_conn\_auth\_cb::pairing\_confirm](structbt__conn__auth__cb.md#af4f7d3ee570b3472ee79b014be01f76e)

void(\* pairing\_confirm)(struct bt\_conn \*conn)

Request confirmation for an incoming pairing.

**Definition** conn.h:2347

[bt\_conn\_auth\_cb::cancel](structbt__conn__auth__cb.md#af6eb01c252ba3e32ff8bf583aa6ca0a4)

void(\* cancel)(struct bt\_conn \*conn)

Cancel the ongoing user request.

**Definition** conn.h:2327

[bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md)

Authenticated pairing information callback structure.

**Definition** conn.h:2373

[bt\_conn\_auth\_info\_cb::pairing\_failed](structbt__conn__auth__info__cb.md#ae7228bb82889eacebf67e1d4b3b23375)

void(\* pairing\_failed)(struct bt\_conn \*conn, enum bt\_security\_err reason)

notify that pairing process has failed.

**Definition** conn.h:2390

[bt\_conn\_auth\_info\_cb::pairing\_complete](structbt__conn__auth__info__cb.md#aea737700f2760de1ed26a721b5e860d2)

void(\* pairing\_complete)(struct bt\_conn \*conn, bool bonded)

notify that pairing procedure was complete.

**Definition** conn.h:2383

[bt\_conn\_auth\_info\_cb::bond\_deleted](structbt__conn__auth__info__cb.md#af20b0d7fc5fd8399ad9368b3ef7067f8)

void(\* bond\_deleted)(uint8\_t id, const bt\_addr\_le\_t \*peer)

Notify that bond has been deleted.

**Definition** conn.h:2401

[bt\_conn\_auth\_info\_cb::node](structbt__conn__auth__info__cb.md#afde62f2cdfb40b4154208f3c1c3dadc1)

sys\_snode\_t node

Internally used field for list handling.

**Definition** conn.h:2404

[bt\_conn\_br\_info](structbt__conn__br__info.md)

BR/EDR Connection Info Structure.

**Definition** conn.h:785

[bt\_conn\_br\_info::dst](structbt__conn__br__info.md#aeef49f711872ccfec5dd558c4552b71e)

const bt\_addr\_t \* dst

Destination (Remote) BR/EDR address.

**Definition** conn.h:786

[bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md)

BR/EDR Connection Remote Info structure.

**Definition** conn.h:870

[bt\_conn\_br\_remote\_info::num\_pages](structbt__conn__br__remote__info.md#a798c179c803e709182a1b0c3594f4a0a)

uint8\_t num\_pages

Number of pages in the remote feature set.

**Definition** conn.h:876

[bt\_conn\_br\_remote\_info::features](structbt__conn__br__remote__info.md#afa19f7db400bb0de234e8cda61f3deaf)

const uint8\_t \* features

Remote feature set (pages of bitmasks).

**Definition** conn.h:873

[bt\_conn\_cb](structbt__conn__cb.md)

Connection callback structure.

**Definition** conn.h:1615

[bt\_conn\_cb::le\_param\_updated](structbt__conn__cb.md#a01582ed3e3801e10c665534eaa991454)

void(\* le\_param\_updated)(struct bt\_conn \*conn, uint16\_t interval, uint16\_t latency, uint16\_t timeout)

The parameters for an LE connection have been updated.

**Definition** conn.h:1712

[bt\_conn\_cb::le\_data\_len\_updated](structbt__conn__cb.md#a1142d1861cc0b0058f68ecf537d0cec3)

void(\* le\_data\_len\_updated)(struct bt\_conn \*conn, struct bt\_conn\_le\_data\_len\_info \*info)

The data length parameters of the connection has changed.

**Definition** conn.h:1784

[bt\_conn\_cb::recycled](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b)

void(\* recycled)(void)

A connection object has been returned to the pool.

**Definition** conn.h:1673

[bt\_conn\_cb::le\_param\_req](structbt__conn__cb.md#a2c52c2e2798062708c373fae9610fadd)

bool(\* le\_param\_req)(struct bt\_conn \*conn, struct bt\_le\_conn\_param \*param)

LE connection parameter update request.

**Definition** conn.h:1699

[bt\_conn\_cb::disconnected](structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914)

void(\* disconnected)(struct bt\_conn \*conn, uint8\_t reason)

A connection has been disconnected.

**Definition** conn.h:1659

[bt\_conn\_cb::connected](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69)

void(\* connected)(struct bt\_conn \*conn, uint8\_t err)

A new connection has been established.

**Definition** conn.h:1640

[bt\_conn\_cb::le\_phy\_updated](structbt__conn__cb.md#ae02a23d823954a747f8f474fb19276d7)

void(\* le\_phy\_updated)(struct bt\_conn \*conn, struct bt\_conn\_le\_phy\_info \*param)

The PHY of the connection has changed.

**Definition** conn.h:1771

[bt\_conn\_cb::security\_changed](structbt__conn__cb.md#ae454d5bc2664e90ba2b1e0c867db374e)

void(\* security\_changed)(struct bt\_conn \*conn, bt\_security\_t level, enum bt\_security\_err err)

The security level of a connection has changed.

**Definition** conn.h:1745

[bt\_conn\_cb::identity\_resolved](structbt__conn__cb.md#aea9b62ab1a1469be97a207a8e07d2f14)

void(\* identity\_resolved)(struct bt\_conn \*conn, const bt\_addr\_le\_t \*rpa, const bt\_addr\_le\_t \*identity)

Remote Identity Address has been resolved.

**Definition** conn.h:1724

[bt\_conn\_cb::remote\_info\_available](structbt__conn__cb.md#af726f004c06b86f770ece263ed6c9ca4)

void(\* remote\_info\_available)(struct bt\_conn \*conn, struct bt\_conn\_remote\_info \*remote\_info)

Remote information procedures has completed.

**Definition** conn.h:1758

[bt\_conn\_info](structbt__conn__info.md)

Connection Info Structure.

**Definition** conn.h:842

[bt\_conn\_info::id](structbt__conn__info.md#a3a4e24519b5d3ba547423e53c4d92a5c)

uint8\_t id

Which local identity the connection was created with.

**Definition** conn.h:848

[bt\_conn\_info::le](structbt__conn__info.md#a6b536e7732dcf7b77a7bc05116dca548)

struct bt\_conn\_le\_info le

LE Connection specific Info.

**Definition** conn.h:852

[bt\_conn\_info::type](structbt__conn__info.md#a7995e1291be494b5bdf860eceea0cad1)

enum bt\_conn\_type type

Connection Type.

**Definition** conn.h:844

[bt\_conn\_info::br](structbt__conn__info.md#a799e59d3a85625799a32ac3f0b3d67d1)

struct bt\_conn\_br\_info br

BR/EDR Connection specific Info.

**Definition** conn.h:854

[bt\_conn\_info::role](structbt__conn__info.md#a8237b8c1bb9a97a174d04cbe13dca7c7)

uint8\_t role

Connection Role.

**Definition** conn.h:846

[bt\_conn\_info::security](structbt__conn__info.md#ae4405f1b4f3fe2ff6253453964860931)

struct bt\_security\_info security

Security specific info.

**Definition** conn.h:859

[bt\_conn\_info::state](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc)

enum bt\_conn\_state state

Connection state.

**Definition** conn.h:857

[bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md)

**Definition** conn.h:1243

[bt\_conn\_le\_create\_param::interval\_coded](structbt__conn__le__create__param.md#a2bc978ac97435fe5f87c6e01692f2910)

uint16\_t interval\_coded

Scan interval LE Coded PHY (N \* 0.625 MS).

**Definition** conn.h:1272

[bt\_conn\_le\_create\_param::window](structbt__conn__le__create__param.md#a339b99f65c5029ada6cdf453ab1f258e)

uint16\_t window

Scan window (N \* 0.625 ms).

**Definition** conn.h:1266

[bt\_conn\_le\_create\_param::options](structbt__conn__le__create__param.md#a4b1e26c0976d9c900b831c886c77b055)

uint32\_t options

Bit-field of create connection options.

**Definition** conn.h:1246

[bt\_conn\_le\_create\_param::timeout](structbt__conn__le__create__param.md#a59f05bfb9468779d02f8d0beeb7a35c1)

uint16\_t timeout

Connection initiation timeout (N \* 10 MS).

**Definition** conn.h:1287

[bt\_conn\_le\_create\_param::interval](structbt__conn__le__create__param.md#a5cfae677f924534dc5bc7b38c457a7af)

uint16\_t interval

Scan interval (N \* 0.625 ms).

**Definition** conn.h:1256

[bt\_conn\_le\_create\_param::window\_coded](structbt__conn__le__create__param.md#ae62491837d35d95e32016b793edf8c96)

uint16\_t window\_coded

Scan window LE Coded PHY (N \* 0.625 MS).

**Definition** conn.h:1278

[bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md)

**Definition** conn.h:1361

[bt\_conn\_le\_create\_synced\_param::peer](structbt__conn__le__create__synced__param.md#ac5872dda4042e3ba6c161dce60784b70)

const bt\_addr\_le\_t \* peer

Remote address.

**Definition** conn.h:1368

[bt\_conn\_le\_create\_synced\_param::subevent](structbt__conn__le__create__synced__param.md#ac7b4e4144aaf914bdef1dc305b5e297f)

uint8\_t subevent

The subevent where the connection will be initiated.

**Definition** conn.h:1371

[bt\_conn\_le\_cs\_capabilities](structbt__conn__le__cs__capabilities.md)

Remote channel sounding capabilities for LE connections supporting CS.

**Definition** conn.h:296

[bt\_conn\_le\_cs\_capabilities::t\_ip1\_times\_supported](structbt__conn__le__cs__capabilities.md#a090f869cfe7e39a70cea94afbd5ac376)

uint16\_t t\_ip1\_times\_supported

Optional T\_IP1 time durations during CS steps.

**Definition** conn.h:367

[bt\_conn\_le\_cs\_capabilities::phase\_based\_nadm\_random\_supported](structbt__conn__le__cs__capabilities.md#a1a0076a0c97317803976f4aca86afc0d)

bool phase\_based\_nadm\_random\_supported

Phase-based normalized attack detector metric when a CS\_SYNC with random sequence is received.

**Definition** conn.h:346

[bt\_conn\_le\_cs\_capabilities::t\_fcs\_times\_supported](structbt__conn__le__cs__capabilities.md#a1ff1d7d769e3ba915f91bf672a6f8a61)

uint16\_t t\_fcs\_times\_supported

Optional T\_FCS time durations during CS steps.

**Definition** conn.h:391

[bt\_conn\_le\_cs\_capabilities::cs\_without\_fae\_supported](structbt__conn__le__cs__capabilities.md#a22604c052da2f8ccf77c81a0a5c628b7)

bool cs\_without\_fae\_supported

Subfeature: CS with no Frequency Actuation Error.

**Definition** conn.h:352

[bt\_conn\_le\_cs\_capabilities::rtt\_random\_payload\_n](structbt__conn__le__cs__capabilities.md#a345d9e43222d77024a8f4283b274b48f)

uint8\_t rtt\_random\_payload\_n

Number of CS steps needed to achieve the accuracy requirements for RTT Random Payload.

**Definition** conn.h:338

[bt\_conn\_le\_cs\_capabilities::cs\_sync\_2m\_phy\_supported](structbt__conn__le__cs__capabilities.md#a3fd09db5fae9c5e307994a78131199c6)

bool cs\_sync\_2m\_phy\_supported

CS\_SYNC LE 2M PHY.

**Definition** conn.h:348

[bt\_conn\_le\_cs\_capabilities::rtt\_aa\_only\_precision](structbt__conn__le__cs__capabilities.md#a46c9168328d3fbc98a2625799c733818)

enum bt\_conn\_le\_cs\_capability\_rtt\_aa\_only rtt\_aa\_only\_precision

RTT AA-Only.

**Definition** conn.h:316

[bt\_conn\_le\_cs\_capabilities::num\_antennas\_supported](structbt__conn__le__cs__capabilities.md#a4e4c56c5066d02b2a0cd59c067f1e4b9)

uint8\_t num\_antennas\_supported

Number of antennas.

**Definition** conn.h:306

[bt\_conn\_le\_cs\_capabilities::t\_sw\_time](structbt__conn__le__cs__capabilities.md#a5a86629a5ad4203b5efe3802cd8b6ae7)

uint8\_t t\_sw\_time

Time in microseconds for the antenna switch period of the CS tones.

**Definition** conn.h:399

[bt\_conn\_le\_cs\_capabilities::cs\_sync\_2m\_2bt\_phy\_supported](structbt__conn__le__cs__capabilities.md#a6513d8ffe7d168441205f6dd656dcbbc)

bool cs\_sync\_2m\_2bt\_phy\_supported

CS\_SYNC LE 2M 2BT PHY.

**Definition** conn.h:350

[bt\_conn\_le\_cs\_capabilities::initiator\_supported](structbt__conn__le__cs__capabilities.md#a6530d2a3fb66d498711856b723acecb7)

bool initiator\_supported

Initiator role.

**Definition** conn.h:310

[bt\_conn\_le\_cs\_capabilities::reflector\_supported](structbt__conn__le__cs__capabilities.md#a694119619d359d0b7e298edf6201ee20)

bool reflector\_supported

Reflector role.

**Definition** conn.h:312

[bt\_conn\_le\_cs\_capabilities::t\_pm\_times\_supported](structbt__conn__le__cs__capabilities.md#a6e92391b21d4acaebba8a171643f572f)

uint16\_t t\_pm\_times\_supported

Optional T\_PM time durations during CS steps.

**Definition** conn.h:397

[bt\_conn\_le\_cs\_capabilities::num\_config\_supported](structbt__conn__le__cs__capabilities.md#a77aacfd02b354e04d4cc29cc1bf4b779)

uint8\_t num\_config\_supported

Number of CS configurations.

**Definition** conn.h:298

[bt\_conn\_le\_cs\_capabilities::rtt\_sounding\_n](structbt__conn__le__cs__capabilities.md#a7f35343a1572800850e791ba3ff5ffb1)

uint8\_t rtt\_sounding\_n

Number of CS steps needed to achieve the accuracy requirements for RTT Sounding.

**Definition** conn.h:332

[bt\_conn\_le\_cs\_capabilities::phase\_based\_nadm\_sounding\_supported](structbt__conn__le__cs__capabilities.md#a94fd00a7a9b22d649f75c7fdd17590a9)

bool phase\_based\_nadm\_sounding\_supported

Phase-based normalized attack detector metric when a CS\_SYNC with sounding sequence is received.

**Definition** conn.h:342

[bt\_conn\_le\_cs\_capabilities::mode\_3\_supported](structbt__conn__le__cs__capabilities.md#aa1616417e6183cf283cf96efc9a92b8e)

bool mode\_3\_supported

Mode-3.

**Definition** conn.h:314

[bt\_conn\_le\_cs\_capabilities::chsel\_alg\_3c\_supported](structbt__conn__le__cs__capabilities.md#aba0db15183d4fa4ae0e3f1333202e55e)

bool chsel\_alg\_3c\_supported

Subfeature: Channel Selection Algorithm #3c.

**Definition** conn.h:354

[bt\_conn\_le\_cs\_capabilities::rtt\_random\_payload\_precision](structbt__conn__le__cs__capabilities.md#abbefdc0268a775712c7abd664adcb6b2)

enum bt\_conn\_le\_cs\_capability\_rtt\_random\_payload rtt\_random\_payload\_precision

RTT Random Payload.

**Definition** conn.h:320

[bt\_conn\_le\_cs\_capabilities::rtt\_aa\_only\_n](structbt__conn__le__cs__capabilities.md#abe3c611316bb5f710f355846ee9ec437)

uint8\_t rtt\_aa\_only\_n

Number of CS steps needed to achieve the accuracy requirements for RTT AA Only.

**Definition** conn.h:326

[bt\_conn\_le\_cs\_capabilities::max\_antenna\_paths\_supported](structbt__conn__le__cs__capabilities.md#ac842e123166008ad1ad663f827937a3b)

uint8\_t max\_antenna\_paths\_supported

Maximum number of antenna paths.

**Definition** conn.h:308

[bt\_conn\_le\_cs\_capabilities::rtt\_sounding\_precision](structbt__conn__le__cs__capabilities.md#acef0d65ed55ae304fea47006bfb0076f)

enum bt\_conn\_le\_cs\_capability\_rtt\_sounding rtt\_sounding\_precision

RTT Sounding.

**Definition** conn.h:318

[bt\_conn\_le\_cs\_capabilities::pbr\_from\_rtt\_sounding\_seq\_supported](structbt__conn__le__cs__capabilities.md#ad57f15b4dda88e2b747f30451601c923)

bool pbr\_from\_rtt\_sounding\_seq\_supported

Subfeature: Phase-based Ranging from RTT sounding sequence.

**Definition** conn.h:356

[bt\_conn\_le\_cs\_capabilities::tx\_snr\_capability](structbt__conn__le__cs__capabilities.md#ad58deea7a825bb5f0bc2ca0034183948)

uint8\_t tx\_snr\_capability

Supported SNR levels used in RTT packets.

**Definition** conn.h:408

[bt\_conn\_le\_cs\_capabilities::max\_consecutive\_procedures\_supported](structbt__conn__le__cs__capabilities.md#ae76fbc0f88525e83717e1d8ef5acae59)

uint16\_t max\_consecutive\_procedures\_supported

Maximum number of consecutive CS procedures.

**Definition** conn.h:304

[bt\_conn\_le\_cs\_capabilities::t\_ip2\_times\_supported](structbt__conn__le__cs__capabilities.md#ae93594f360430e9c0c80cf3edcf570f6)

uint16\_t t\_ip2\_times\_supported

Optional T\_IP2 time durations during CS steps.

**Definition** conn.h:378

[bt\_conn\_le\_cs\_config](structbt__conn__le__cs__config.md)

Channel sounding configuration.

**Definition** conn.h:491

[bt\_conn\_le\_cs\_config::main\_mode\_type](structbt__conn__le__cs__config.md#a02b942d1def46476160ba8839ca9690f)

enum bt\_conn\_le\_cs\_main\_mode main\_mode\_type

Main CS mode type.

**Definition** conn.h:495

[bt\_conn\_le\_cs\_config::rtt\_type](structbt__conn__le__cs__config.md#a194e3844373c57e714917d03ac82666d)

enum bt\_conn\_le\_cs\_rtt\_type rtt\_type

RTT type.

**Definition** conn.h:512

[bt\_conn\_le\_cs\_config::cs\_sync\_phy](structbt__conn__le__cs__config.md#a2051f559b41085c4b41743aaaaecf3a1)

enum bt\_conn\_le\_cs\_sync\_phy cs\_sync\_phy

CS Sync PHY.

**Definition** conn.h:514

[bt\_conn\_le\_cs\_config::t\_fcs\_time\_us](structbt__conn__le__cs__config.md#a29912bd291fa4da09bb5b196d747ca6b)

uint8\_t t\_fcs\_time\_us

Time in microseconds for frequency changes.

**Definition** conn.h:530

[bt\_conn\_le\_cs\_config::min\_main\_mode\_steps](structbt__conn__le__cs__config.md#a2e59fb17cd932b7670b3e915684c2107)

uint8\_t min\_main\_mode\_steps

Minimum number of CS main mode steps to be executed before a submode step is executed.

**Definition** conn.h:499

[bt\_conn\_le\_cs\_config::main\_mode\_repetition](structbt__conn__le__cs__config.md#a2e904438c579870ed96b5dccff239c18)

uint8\_t main\_mode\_repetition

Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning ...

**Definition** conn.h:506

[bt\_conn\_le\_cs\_config::sub\_mode\_type](structbt__conn__le__cs__config.md#a4ee4bf79283686e16d4737f546718c44)

enum bt\_conn\_le\_cs\_sub\_mode sub\_mode\_type

Sub CS mode type.

**Definition** conn.h:497

[bt\_conn\_le\_cs\_config::channel\_map](structbt__conn__le__cs__config.md#a60f9d21629554d47556d0fe8d63dcae3)

uint8\_t channel\_map[10]

Channel map used for CS procedure Channels n = 0, 1, 23, 24, 25, 77, and 78 are not allowed and shall...

**Definition** conn.h:538

[bt\_conn\_le\_cs\_config::channel\_selection\_type](structbt__conn__le__cs__config.md#a63b7027929a5c3ec7fd68f35343262ee)

enum bt\_conn\_le\_cs\_chsel\_type channel\_selection\_type

Channel selection type.

**Definition** conn.h:520

[bt\_conn\_le\_cs\_config::t\_ip2\_time\_us](structbt__conn__le__cs__config.md#a8e650b50400a45040c02a88dfb30683c)

uint8\_t t\_ip2\_time\_us

Interlude time in microseconds between the CS tones.

**Definition** conn.h:528

[bt\_conn\_le\_cs\_config::mode\_0\_steps](structbt__conn__le__cs__config.md#a8eea68bffef759b4532b68a1ecbdd4f1)

uint8\_t mode\_0\_steps

Number of CS mode-0 steps to be included at the beginning of each CS subevent.

**Definition** conn.h:508

[bt\_conn\_le\_cs\_config::channel\_map\_repetition](structbt__conn__le__cs__config.md#a971ff7ba734dd71512af7f3850de364d)

uint8\_t channel\_map\_repetition

The number of times the Channel\_Map field will be cycled through for non-mode-0 steps within a CS pro...

**Definition** conn.h:518

[bt\_conn\_le\_cs\_config::ch3c\_shape](structbt__conn__le__cs__config.md#a9b64ecb0986e7e9995c29feaf105eeaa)

enum bt\_conn\_le\_cs\_ch3c\_shape ch3c\_shape

User-specified channel sequence shape.

**Definition** conn.h:522

[bt\_conn\_le\_cs\_config::t\_ip1\_time\_us](structbt__conn__le__cs__config.md#aab9a1d8d09d7a439f1c4dd28b9dd05c4)

uint8\_t t\_ip1\_time\_us

Interlude time in microseconds between the RTT packets.

**Definition** conn.h:526

[bt\_conn\_le\_cs\_config::id](structbt__conn__le__cs__config.md#aaf8f1ce04fd22b4ca4728bdcfce8bd4a)

uint8\_t id

CS configuration ID.

**Definition** conn.h:493

[bt\_conn\_le\_cs\_config::role](structbt__conn__le__cs__config.md#ad11f8bee028ad3eb59008d46dce2d5bd)

enum bt\_conn\_le\_cs\_role role

CS role.

**Definition** conn.h:510

[bt\_conn\_le\_cs\_config::t\_pm\_time\_us](structbt__conn__le__cs__config.md#ae7f1cc232df00b4543fdb2b2596b9bbf)

uint8\_t t\_pm\_time\_us

Time in microseconds for the phase measurement period of the CS tones.

**Definition** conn.h:532

[bt\_conn\_le\_cs\_config::ch3c\_jump](structbt__conn__le__cs__config.md#afa2846689f1a9d5b9e124b1c9095154f)

uint8\_t ch3c\_jump

Number of channels skipped in each rising and falling sequence.

**Definition** conn.h:524

[bt\_conn\_le\_cs\_config::max\_main\_mode\_steps](structbt__conn__le__cs__config.md#aff70b37fac8a3bd94acb25d7bd06989b)

uint8\_t max\_main\_mode\_steps

Maximum number of CS main mode steps to be executed before a submode step is executed.

**Definition** conn.h:501

[bt\_conn\_le\_cs\_fae\_table](structbt__conn__le__cs__fae__table.md)

Remote FAE Table for LE connections supporting CS.

**Definition** conn.h:412

[bt\_conn\_le\_cs\_fae\_table::remote\_fae\_table](structbt__conn__le__cs__fae__table.md#a88edb4769f68966347b08afa354d9d41)

uint8\_t \* remote\_fae\_table

**Definition** conn.h:413

[bt\_conn\_le\_cs\_procedure\_enable\_complete](structbt__conn__le__cs__procedure__enable__complete.md)

**Definition** conn.h:1568

[bt\_conn\_le\_cs\_procedure\_enable\_complete::config\_id](structbt__conn__le__cs__procedure__enable__complete.md#a2e290c25ec5af8b0259d45f04d6c543d)

uint8\_t config\_id

**Definition** conn.h:1570

[bt\_conn\_le\_cs\_procedure\_enable\_complete::tone\_antenna\_config\_selection](structbt__conn__le__cs__procedure__enable__complete.md#a3fa8ad4dd264eb4e2489dea9c1048d22)

enum bt\_conn\_le\_cs\_tone\_antenna\_config\_selection tone\_antenna\_config\_selection

**Definition** conn.h:1576

[bt\_conn\_le\_cs\_procedure\_enable\_complete::subevents\_per\_event](structbt__conn__le__cs__procedure__enable__complete.md#a40b03220932852b6b51d65f557c21f17)

uint8\_t subevents\_per\_event

**Definition** conn.h:1585

[bt\_conn\_le\_cs\_procedure\_enable\_complete::event\_interval](structbt__conn__le__cs__procedure__enable__complete.md#a4129ab9519ba140ffb198aa9a5cde6ac)

uint16\_t event\_interval

**Definition** conn.h:1593

[bt\_conn\_le\_cs\_procedure\_enable\_complete::subevent\_interval](structbt__conn__le__cs__procedure__enable__complete.md#a77a2bd8ee384c4567321a09f6b64782c)

uint16\_t subevent\_interval

**Definition** conn.h:1590

[bt\_conn\_le\_cs\_procedure\_enable\_complete::procedure\_interval](structbt__conn__le__cs__procedure__enable__complete.md#a8511deef97f19c53ddaa4dec8492658f)

uint16\_t procedure\_interval

**Definition** conn.h:1596

[bt\_conn\_le\_cs\_procedure\_enable\_complete::procedure\_count](structbt__conn__le__cs__procedure__enable__complete.md#ab83778fe2d1274e5658fd5f5f867314f)

uint16\_t procedure\_count

**Definition** conn.h:1599

[bt\_conn\_le\_cs\_procedure\_enable\_complete::state](structbt__conn__le__cs__procedure__enable__complete.md#acc1d12d347e1b02b2eea562ea064a40b)

enum bt\_conn\_le\_cs\_procedure\_enable\_state state

**Definition** conn.h:1573

[bt\_conn\_le\_cs\_procedure\_enable\_complete::max\_procedure\_len](structbt__conn__le__cs__procedure__enable__complete.md#ad71825d71ab89baea138e41f9a3ff57e)

uint16\_t max\_procedure\_len

**Definition** conn.h:1602

[bt\_conn\_le\_cs\_procedure\_enable\_complete::subevent\_len](structbt__conn__le__cs__procedure__enable__complete.md#ae990a10c468ec62fbaf9325c94733c7c)

uint32\_t subevent\_len

**Definition** conn.h:1582

[bt\_conn\_le\_cs\_procedure\_enable\_complete::selected\_tx\_power](structbt__conn__le__cs__procedure__enable__complete.md#aeb918e438cd02296c7f693757268f6bf)

int8\_t selected\_tx\_power

**Definition** conn.h:1579

[bt\_conn\_le\_cs\_subevent\_result](structbt__conn__le__cs__subevent__result.md)

Subevent data for LE connections supporting CS.

**Definition** conn.h:579

[bt\_conn\_le\_cs\_subevent\_result::procedure\_counter](structbt__conn__le__cs__subevent__result.md#a0f8fc918f8eb31c47acf51885c7add08)

uint16\_t procedure\_counter

CS procedure count associated with these results.

**Definition** conn.h:600

[bt\_conn\_le\_cs\_subevent\_result::header](structbt__conn__le__cs__subevent__result.md#a1a90563a8c93f9b309e88fd771a7cec4)

struct bt\_conn\_le\_cs\_subevent\_result::@320060245020174255122267056204140154173252004243 header

[bt\_conn\_le\_cs\_subevent\_result::num\_antenna\_paths](structbt__conn__le__cs__subevent__result.md#a3597697ae4acdd8f7c009bececab6a65)

uint8\_t num\_antenna\_paths

Number of antenna paths used during the phase measurement stage.

**Definition** conn.h:650

[bt\_conn\_le\_cs\_subevent\_result::num\_steps\_reported](structbt__conn__le__cs__subevent__result.md#a3bffc0935a5410d75d0050337e4fad27)

uint8\_t num\_steps\_reported

Number of CS steps in the subevent.

**Definition** conn.h:653

[bt\_conn\_le\_cs\_subevent\_result::subevent\_done\_status](structbt__conn__le__cs__subevent__result.md#a45b22c6c2252e2afa28ee8b1bfed3ecf)

enum bt\_conn\_le\_cs\_subevent\_done\_status subevent\_done\_status

Subevent status.

**Definition** conn.h:633

[bt\_conn\_le\_cs\_subevent\_result::step\_data\_buf](structbt__conn__le__cs__subevent__result.md#a6948c4a8c5882cb1d1b04a2b390fda8c)

struct net\_buf\_simple \* step\_data\_buf

**Definition** conn.h:660

[bt\_conn\_le\_cs\_subevent\_result::start\_acl\_conn\_event](structbt__conn__le__cs__subevent__result.md#a7706d0dfd7246d4cf193a8a9e7b6305d)

uint16\_t start\_acl\_conn\_event

Starting ACL connection event counter.

**Definition** conn.h:594

[bt\_conn\_le\_cs\_subevent\_result::procedure\_abort\_reason](structbt__conn__le__cs__subevent__result.md#a778c89f57ef50f612654243ba673ba3f)

enum bt\_conn\_le\_cs\_procedure\_abort\_reason procedure\_abort\_reason

Abort reason.

**Definition** conn.h:640

[bt\_conn\_le\_cs\_subevent\_result::frequency\_compensation](structbt__conn__le__cs__subevent__result.md#a967d37f37d0e1596984fdda34609a3b3)

uint16\_t frequency\_compensation

Frequency compensation value in units of 0.01 ppm.

**Definition** conn.h:609

[bt\_conn\_le\_cs\_subevent\_result::abort\_step](structbt__conn__le__cs__subevent__result.md#a9bfcc6dcaa191c7f56958ef88926b51e)

uint8\_t abort\_step

Step number, on which the subevent was aborted if subevent\_done\_status is BT\_CONN\_LE\_CS\_SUBEVENT\_COMP...

**Definition** conn.h:658

[bt\_conn\_le\_cs\_subevent\_result::config\_id](structbt__conn__le__cs__subevent__result.md#aa4c770ab2db8d4ab665ad50f7edd5bfa)

uint8\_t config\_id

CS configuration identifier.

**Definition** conn.h:588

[bt\_conn\_le\_cs\_subevent\_result::reference\_power\_level](structbt__conn__le__cs__subevent__result.md#acbfc5e80a2fb82072d9376e996f7969f)

int8\_t reference\_power\_level

Reference power level in dBm.

**Definition** conn.h:617

[bt\_conn\_le\_cs\_subevent\_result::procedure\_done\_status](structbt__conn__le__cs__subevent__result.md#adf60893d9229003d1eefc552a4957b65)

enum bt\_conn\_le\_cs\_procedure\_done\_status procedure\_done\_status

Procedure status.

**Definition** conn.h:619

[bt\_conn\_le\_cs\_subevent\_result::subevent\_abort\_reason](structbt__conn__le__cs__subevent__result.md#aef5ba53497c4d1576c9ecec1b5dea289)

enum bt\_conn\_le\_cs\_subevent\_abort\_reason subevent\_abort\_reason

Abort reason.

**Definition** conn.h:647

[bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md)

Connection data length information for LE connections.

**Definition** conn.h:149

[bt\_conn\_le\_data\_len\_info::tx\_max\_time](structbt__conn__le__data__len__info.md#a14288429cbbcce2ef34580a581815eb7)

uint16\_t tx\_max\_time

Maximum Link Layer transmission payload time in us.

**Definition** conn.h:153

[bt\_conn\_le\_data\_len\_info::rx\_max\_len](structbt__conn__le__data__len__info.md#a18ddc603e922586e331187c9b29f2908)

uint16\_t rx\_max\_len

Maximum Link Layer reception payload size in bytes.

**Definition** conn.h:155

[bt\_conn\_le\_data\_len\_info::tx\_max\_len](structbt__conn__le__data__len__info.md#a48d175f3c4b03dbdee129feae3edab23)

uint16\_t tx\_max\_len

Maximum Link Layer transmission payload size in bytes.

**Definition** conn.h:151

[bt\_conn\_le\_data\_len\_info::rx\_max\_time](structbt__conn__le__data__len__info.md#af2316cdc921e9ec19491501e15248f73)

uint16\_t rx\_max\_time

Maximum Link Layer reception payload time in us.

**Definition** conn.h:157

[bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md)

Connection data length parameters for LE connections.

**Definition** conn.h:161

[bt\_conn\_le\_data\_len\_param::tx\_max\_len](structbt__conn__le__data__len__param.md#a8b279a0dc72c70aaf5205558fd4b4c4a)

uint16\_t tx\_max\_len

Maximum Link Layer transmission payload size in bytes.

**Definition** conn.h:163

[bt\_conn\_le\_data\_len\_param::tx\_max\_time](structbt__conn__le__data__len__param.md#a9046542952fa822b944602b398562e6e)

uint16\_t tx\_max\_time

Maximum Link Layer transmission payload time in us.

**Definition** conn.h:165

[bt\_conn\_le\_info](structbt__conn__le__info.md)

LE Connection Info Structure.

**Definition** conn.h:739

[bt\_conn\_le\_info::dst](structbt__conn__le__info.md#a1f78e1c0ed3482ce6eec9ce6eeda4769)

const bt\_addr\_le\_t \* dst

Destination (Remote) Identity Address or remote Resolvable Private Address (RPA) before identity has ...

**Definition** conn.h:745

[bt\_conn\_le\_info::phy](structbt__conn__le__info.md#a215d39c6cd7da1ac033529b5541cbfc1)

const struct bt\_conn\_le\_phy\_info \* phy

**Definition** conn.h:755

[bt\_conn\_le\_info::remote](structbt__conn__le__info.md#a236d1c97c735c7cfaead0b1a3672d512)

const bt\_addr\_le\_t \* remote

Remote device address used during connection setup.

**Definition** conn.h:749

[bt\_conn\_le\_info::local](structbt__conn__le__info.md#a3be5df0deb0af08f84843eb3c6a5e5ae)

const bt\_addr\_le\_t \* local

Local device address used during connection setup.

**Definition** conn.h:747

[bt\_conn\_le\_info::src](structbt__conn__le__info.md#a5f1eacec82f31182460d6d5359a8b295)

const bt\_addr\_le\_t \* src

Source (Local) Identity Address.

**Definition** conn.h:741

[bt\_conn\_le\_info::interval](structbt__conn__le__info.md#a95a1f635e53f16d5839cdd58f4bda962)

uint16\_t interval

Connection interval.

**Definition** conn.h:750

[bt\_conn\_le\_info::latency](structbt__conn__le__info.md#acd83835fe5ec0878fd653b87cb570a49)

uint16\_t latency

Connection peripheral latency.

**Definition** conn.h:751

[bt\_conn\_le\_info::data\_len](structbt__conn__le__info.md#ae309f390c8d7b33a4de55791af235ab0)

const struct bt\_conn\_le\_data\_len\_info \* data\_len

**Definition** conn.h:760

[bt\_conn\_le\_info::timeout](structbt__conn__le__info.md#afb4dc594d063fbbad2bcd4acf047f716)

uint16\_t timeout

Connection supervision timeout.

**Definition** conn.h:752

[bt\_conn\_le\_path\_loss\_reporting\_param](structbt__conn__le__path__loss__reporting__param.md)

LE Path Loss Monitoring Parameters Structure as defined in Core Spec.

**Definition** conn.h:1004

[bt\_conn\_le\_path\_loss\_reporting\_param::high\_threshold](structbt__conn__le__path__loss__reporting__param.md#a5cc7a17efee69d61b8f8d0c242321054)

uint8\_t high\_threshold

High threshold for the path loss (dB).

**Definition** conn.h:1006

[bt\_conn\_le\_path\_loss\_reporting\_param::low\_threshold](structbt__conn__le__path__loss__reporting__param.md#a634c08e573cffd97a94ad681bed9239e)

uint8\_t low\_threshold

Low threshold for the path loss (dB).

**Definition** conn.h:1010

[bt\_conn\_le\_path\_loss\_reporting\_param::min\_time\_spent](structbt__conn__le__path__loss__reporting__param.md#a6fec4497c6fd95fa6f265bd859976c9d)

uint16\_t min\_time\_spent

Minimum time in number of connection events to be observed once the path loss crosses the threshold b...

**Definition** conn.h:1016

[bt\_conn\_le\_path\_loss\_reporting\_param::high\_hysteresis](structbt__conn__le__path__loss__reporting__param.md#aec49adc896604d878060b03bd40ab0f4)

uint8\_t high\_hysteresis

Hysteresis value for the high threshold (dB).

**Definition** conn.h:1008

[bt\_conn\_le\_path\_loss\_reporting\_param::low\_hysteresis](structbt__conn__le__path__loss__reporting__param.md#af8e70508a39ee73b75a4769769aa303f)

uint8\_t low\_hysteresis

Hysteresis value for the low threshold (dB).

**Definition** conn.h:1012

[bt\_conn\_le\_path\_loss\_threshold\_report](structbt__conn__le__path__loss__threshold__report.md)

LE Path Loss Monitoring Threshold Change Report Structure.

**Definition** conn.h:992

[bt\_conn\_le\_path\_loss\_threshold\_report::zone](structbt__conn__le__path__loss__threshold__report.md#ab2b71b7ddccc40ced56657a548b98e77)

enum bt\_conn\_le\_path\_loss\_zone zone

Path Loss zone as documented in Core Spec.

**Definition** conn.h:995

[bt\_conn\_le\_path\_loss\_threshold\_report::path\_loss](structbt__conn__le__path__loss__threshold__report.md#abe631b07816d6c18bacba64bfbd1e844)

uint8\_t path\_loss

Current path loss (dB).

**Definition** conn.h:998

[bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md)

Connection PHY information for LE connections.

**Definition** conn.h:82

[bt\_conn\_le\_phy\_info::rx\_phy](structbt__conn__le__phy__info.md#abf029b63958d86eef7bf15218238783b)

uint8\_t rx\_phy

Connection transmit PHY.

**Definition** conn.h:84

[bt\_conn\_le\_phy\_info::tx\_phy](structbt__conn__le__phy__info.md#ac65912cc2a7997c0f886886783ea5b11)

uint8\_t tx\_phy

**Definition** conn.h:83

[bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md)

Preferred PHY parameters for LE connections.

**Definition** conn.h:100

[bt\_conn\_le\_phy\_param::options](structbt__conn__le__phy__param.md#a889dae2cdc2fba43f9f1194d26c4b737)

uint16\_t options

Connection PHY options.

**Definition** conn.h:101

[bt\_conn\_le\_phy\_param::pref\_rx\_phy](structbt__conn__le__phy__param.md#a8d576bed5d9dfe9ca9a694d6d295afbc)

uint8\_t pref\_rx\_phy

Bitmask of preferred receive PHYs.

**Definition** conn.h:103

[bt\_conn\_le\_phy\_param::pref\_tx\_phy](structbt__conn__le__phy__param.md#ace64d2181ecc25ecdfa374f7f4bcf664)

uint8\_t pref\_tx\_phy

Bitmask of preferred transmit PHYs.

**Definition** conn.h:102

[bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md)

LE Connection Remote Info Structure.

**Definition** conn.h:863

[bt\_conn\_le\_remote\_info::features](structbt__conn__le__remote__info.md#a4ff434f6c501dc60db5c4b776be46b3b)

const uint8\_t \* features

Remote LE feature set (bitmask).

**Definition** conn.h:866

[bt\_conn\_le\_subrate\_changed](structbt__conn__le__subrate__changed.md)

Updated subrating connection parameters for LE connections.

**Definition** conn.h:231

[bt\_conn\_le\_subrate\_changed::factor](structbt__conn__le__subrate__changed.md#a0c3e3dc41ca4dec92740c920e959060b)

uint16\_t factor

Connection subrate factor.

**Definition** conn.h:238

[bt\_conn\_le\_subrate\_changed::continuation\_number](structbt__conn__le__subrate__changed.md#a2420a0a3145471c6a1a618bea8d1d7c6)

uint16\_t continuation\_number

Number of underlying connection events to remain active after a packet containing a Link Layer PDU wi...

**Definition** conn.h:243

[bt\_conn\_le\_subrate\_changed::peripheral\_latency](structbt__conn__le__subrate__changed.md#aa0bab070bc43972dfb3a5259934b4931)

uint16\_t peripheral\_latency

Peripheral latency in units of subrated connection intervals.

**Definition** conn.h:245

[bt\_conn\_le\_subrate\_changed::supervision\_timeout](structbt__conn__le__subrate__changed.md#aab0cb08a7549401684bcab3c291dc192)

uint16\_t supervision\_timeout

Connection Supervision timeout (N \* 10 ms).

**Definition** conn.h:247

[bt\_conn\_le\_subrate\_changed::status](structbt__conn__le__subrate__changed.md#afc5a577dadf41819e89bc3af016ce258)

uint8\_t status

HCI Status from LE Subrate Changed event.

**Definition** conn.h:236

[bt\_conn\_le\_subrate\_param](structbt__conn__le__subrate__param.md)

Connection subrating parameters for LE connections.

**Definition** conn.h:200

[bt\_conn\_le\_subrate\_param::max\_latency](structbt__conn__le__subrate__param.md#a15d05324708ddeea8d2f3515eea396bb)

uint16\_t max\_latency

Maximum Peripheral latency in units of subrated connection intervals.

**Definition** conn.h:206

[bt\_conn\_le\_subrate\_param::subrate\_max](structbt__conn__le__subrate__param.md#a59d2d244e3568b8f97ce936121d41b1a)

uint16\_t subrate\_max

Maximum subrate factor.

**Definition** conn.h:204

[bt\_conn\_le\_subrate\_param::continuation\_number](structbt__conn__le__subrate__param.md#a978cef5f2f14a5a7fe7ded09c6fdf2d9)

uint16\_t continuation\_number

Minimum number of underlying connection events to remain active after a packet containing a Link Laye...

**Definition** conn.h:211

[bt\_conn\_le\_subrate\_param::supervision\_timeout](structbt__conn__le__subrate__param.md#aca0897d00a1dd1735dbbaf5bfde711ed)

uint16\_t supervision\_timeout

Connection Supervision timeout (N \* 10 ms).

**Definition** conn.h:216

[bt\_conn\_le\_subrate\_param::subrate\_min](structbt__conn__le__subrate__param.md#aef75fec8ba8c9987d55e81aa2539b96e)

uint16\_t subrate\_min

Minimum subrate factor.

**Definition** conn.h:202

[bt\_conn\_le\_subrating\_info](structbt__conn__le__subrating__info.md)

Subrating information for LE connections.

**Definition** conn.h:220

[bt\_conn\_le\_subrating\_info::continuation\_number](structbt__conn__le__subrating__info.md#a0a6d1eae73f76382f1a9415c01761c19)

uint16\_t continuation\_number

Number of underlying connection events to remain active after a packet containing a Link Layer PDU wi...

**Definition** conn.h:227

[bt\_conn\_le\_subrating\_info::factor](structbt__conn__le__subrating__info.md#a23736535309f38695a2e432c5c80bbe1)

uint16\_t factor

Connection subrate factor.

**Definition** conn.h:222

[bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md)

LE Transmit Power Reporting Structure.

**Definition** conn.h:934

[bt\_conn\_le\_tx\_power\_report::phy](structbt__conn__le__tx__power__report.md#a5b1f67537fbe945f2f258b47082723b4)

enum bt\_conn\_le\_tx\_power\_phy phy

Phy of Transmit power reporting.

**Definition** conn.h:942

[bt\_conn\_le\_tx\_power\_report::delta](structbt__conn__le__tx__power__report.md#a7c681c7b9f77d994b2de1febea7c5dc9)

int8\_t delta

Change in transmit power level.

**Definition** conn.h:965

[bt\_conn\_le\_tx\_power\_report::reason](structbt__conn__le__tx__power__report.md#aa5606925229784af8ae90542432cf200)

uint8\_t reason

Reason for Transmit power reporting, as documented in Core Spec.

**Definition** conn.h:939

[bt\_conn\_le\_tx\_power\_report::tx\_power\_level](structbt__conn__le__tx__power__report.md#ace830ddb7ae662c9759babed87f1b6f3)

int8\_t tx\_power\_level

Transmit power level.

**Definition** conn.h:952

[bt\_conn\_le\_tx\_power\_report::tx\_power\_level\_flag](structbt__conn__le__tx__power__report.md#ae7a4f77c6f7af1a459896d25cf661eb8)

uint8\_t tx\_power\_level\_flag

Bit 0: Transmit power level is at minimum level.

**Definition** conn.h:957

[bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md)

LE Transmit Power Level Structure.

**Definition** conn.h:920

[bt\_conn\_le\_tx\_power::max\_level](structbt__conn__le__tx__power.md#a1674247c511906fa6f0193653ed0b71a)

int8\_t max\_level

Output: maximum transmit power level.

**Definition** conn.h:929

[bt\_conn\_le\_tx\_power::current\_level](structbt__conn__le__tx__power.md#a6d2e5a5215fa5d60630e74928a67fc04)

int8\_t current\_level

Output: current transmit power level.

**Definition** conn.h:926

[bt\_conn\_le\_tx\_power::phy](structbt__conn__le__tx__power.md#a8702c4ff5082b8f90decdfabfb8253fe)

uint8\_t phy

Input: 1M, 2M, Coded S2 or Coded S8.

**Definition** conn.h:923

[bt\_conn\_oob\_info](structbt__conn__oob__info.md)

Info Structure for OOB pairing.

**Definition** conn.h:2110

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_LE\_LEGACY](structbt__conn__oob__info.md#a318a663619f0bbbb90a849fd5e16c37ea4c33ea839306256a198c29ea783c659b)

@ BT\_CONN\_OOB\_LE\_LEGACY

LE legacy pairing.

**Definition** conn.h:2114

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_LE\_SC](structbt__conn__oob__info.md#a318a663619f0bbbb90a849fd5e16c37eacd02773beb42df3fb6cbaa2fa2abda1e)

@ BT\_CONN\_OOB\_LE\_SC

LE SC pairing.

**Definition** conn.h:2117

[bt\_conn\_oob\_info::lesc](structbt__conn__oob__info.md#a59febda99e1ad78321fe2da07f98322b)

struct bt\_conn\_oob\_info::@224236016370304343054103074037006351074263006352::@130100253371055064164065265224242172250032310014 lesc

LE Secure Connections OOB pairing parameters.

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_NO\_DATA](structbt__conn__oob__info.md#a71bf295d82fbc647b3816bfba6fa0ae7)

@ BT\_CONN\_OOB\_NO\_DATA

No OOB data requested.

**Definition** conn.h:2135

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_LOCAL\_ONLY](structbt__conn__oob__info.md#a72a749120c0a55a8dc9bd078921277e5)

@ BT\_CONN\_OOB\_LOCAL\_ONLY

Local OOB data requested.

**Definition** conn.h:2126

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_REMOTE\_ONLY](structbt__conn__oob__info.md#a7506049b35ac63602452b087d1d60fa2)

@ BT\_CONN\_OOB\_REMOTE\_ONLY

Remote OOB data requested.

**Definition** conn.h:2129

[bt\_conn\_oob\_info::oob\_config](structbt__conn__oob__info.md#a96f2cf2f20d9890b833949b2183a029c)

enum bt\_conn\_oob\_info::@224236016370304343054103074037006351074263006352::@130100253371055064164065265224242172250032310014::@174114057350366013042053070360265151016144152040 oob\_config

OOB data configuration.

[bt\_conn\_oob\_info::type](structbt__conn__oob__info.md#a9923119f8a145066408d9e46d6993026)

enum bt\_conn\_oob\_info::@143143115062310336126347360141254141124170204126 type

Type of OOB pairing method.

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_BOTH\_PEERS](structbt__conn__oob__info.md#a99685ad84ac991e0540855cab5546ff8)

@ BT\_CONN\_OOB\_BOTH\_PEERS

Both local and remote OOB data requested.

**Definition** conn.h:2132

[bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md)

Pairing request and pairing response info structure.

**Definition** conn.h:2148

[bt\_conn\_pairing\_feat::resp\_key\_dist](structbt__conn__pairing__feat.md#a49f9f02e232e91f7f7a530aa7f226cba)

uint8\_t resp\_key\_dist

Responder Key Distribution/Generation, Core Spec.

**Definition** conn.h:2169

[bt\_conn\_pairing\_feat::io\_capability](structbt__conn__pairing__feat.md#a68005cea273c8e76c086502001b258b0)

uint8\_t io\_capability

IO Capability, Core Spec.

**Definition** conn.h:2150

[bt\_conn\_pairing\_feat::init\_key\_dist](structbt__conn__pairing__feat.md#a70adc125b875348ec8d273dea3b470d8)

uint8\_t init\_key\_dist

Initiator Key Distribution/Generation, Core Spec.

**Definition** conn.h:2164

[bt\_conn\_pairing\_feat::max\_enc\_key\_size](structbt__conn__pairing__feat.md#abe1d7d4bd9f4b551a2d0c69adc75bd40)

uint8\_t max\_enc\_key\_size

Maximum Encryption Key Size, Core Spec.

**Definition** conn.h:2159

[bt\_conn\_pairing\_feat::auth\_req](structbt__conn__pairing__feat.md#af9a977b1e0f9d4eada26a82d92eaec54)

uint8\_t auth\_req

AuthReq, Core Spec.

**Definition** conn.h:2156

[bt\_conn\_pairing\_feat::oob\_data\_flag](structbt__conn__pairing__feat.md#afb03164960db62b4b4cf70d3f0134099)

uint8\_t oob\_data\_flag

OOB data flag, Core Spec.

**Definition** conn.h:2153

[bt\_conn\_remote\_info](structbt__conn__remote__info.md)

Connection Remote Info Structure.

**Definition** conn.h:884

[bt\_conn\_remote\_info::version](structbt__conn__remote__info.md#a2664f6ed3bd22f9a011126daf5d81376)

uint8\_t version

Remote Link Layer version.

**Definition** conn.h:889

[bt\_conn\_remote\_info::subversion](structbt__conn__remote__info.md#a360979a15c958706157fc630fd55cbca)

uint16\_t subversion

Per-manufacturer unique revision.

**Definition** conn.h:895

[bt\_conn\_remote\_info::manufacturer](structbt__conn__remote__info.md#a47cc5a4b8888a0b8faaf6880c37418b8)

uint16\_t manufacturer

Remote manufacturer identifier.

**Definition** conn.h:892

[bt\_conn\_remote\_info::type](structbt__conn__remote__info.md#a8bb514196bde5df561dbf76b68060729)

uint8\_t type

Connection Type.

**Definition** conn.h:886

[bt\_conn\_remote\_info::br](structbt__conn__remote__info.md#ab73365f09cdb5ce870272546543bcfeb)

struct bt\_conn\_br\_remote\_info br

BR/EDR connection remote info.

**Definition** conn.h:902

[bt\_conn\_remote\_info::le](structbt__conn__remote__info.md#ae75530b09c6dea416630a4a19a1d64cc)

struct bt\_conn\_le\_remote\_info le

LE connection remote info.

**Definition** conn.h:899

[bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md)

**Definition** direction.h:165

[bt\_le\_conn\_param](structbt__le__conn__param.md)

Connection parameters for LE connections.

**Definition** conn.h:38

[bt\_le\_conn\_param::latency](structbt__le__conn__param.md#a3d21bd8363fa77dab83468ea319fef7d)

uint16\_t latency

**Definition** conn.h:41

[bt\_le\_conn\_param::interval\_max](structbt__le__conn__param.md#a6d5a2662a5f22ccc26c992829d21f22d)

uint16\_t interval\_max

**Definition** conn.h:40

[bt\_le\_conn\_param::timeout](structbt__le__conn__param.md#ac06c16eb02e7a9d8b414db07e829178a)

uint16\_t timeout

**Definition** conn.h:42

[bt\_le\_conn\_param::interval\_min](structbt__le__conn__param.md#acd3b0a74402ca45402bab9ff54763e8d)

uint16\_t interval\_min

**Definition** conn.h:39

[bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md)

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2540

[bt\_security\_info](structbt__security__info.md)

Security Info Structure.

**Definition** conn.h:832

[bt\_security\_info::enc\_key\_size](structbt__security__info.md#a6567ffb82b7fa8093cc57ef4662873ba)

uint8\_t enc\_key\_size

Encryption Key Size.

**Definition** conn.h:836

[bt\_security\_info::level](structbt__security__info.md#a7b18849fad25b3f2da6b8c85a56d86e1)

bt\_security\_t level

Security Level.

**Definition** conn.h:834

[bt\_security\_info::flags](structbt__security__info.md#a99cb4af08bfa1dab182821d956368526)

enum bt\_security\_flag flags

Flags.

**Definition** conn.h:838

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [conn.h](conn_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
