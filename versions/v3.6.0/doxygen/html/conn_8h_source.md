---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/conn_8h_source.html
original_path: doxygen/html/conn_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

23#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h.md)>

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

[ 200](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20)enum \_\_packed [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) {

[ 202](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) [BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 204](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) [BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 206](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) [BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 208](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee) [BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 210](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836) [BT\_CONN\_TYPE\_ALL](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836) = [BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) | [BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) |

211 [BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) | [BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee),

212};

213

[ 225](group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c)struct bt\_conn \*[bt\_conn\_ref](group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c)(struct bt\_conn \*conn);

226

[ 233](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6)void [bt\_conn\_unref](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6)(struct bt\_conn \*conn);

234

[ 251](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916)void [bt\_conn\_foreach](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916)(enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) type,

252 void (\*func)(struct bt\_conn \*conn, void \*data),

253 void \*data);

254

[ 267](group__bt__conn.md#ga1bfe349efd8a7de31e9457fe439d746a)struct bt\_conn \*[bt\_conn\_lookup\_addr\_le](group__bt__conn.md#ga1bfe349efd8a7de31e9457fe439d746a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer);

268

[ 275](group__bt__conn.md#ga77108581b8f61485ca840e4bf7a17087)const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[bt\_conn\_get\_dst](group__bt__conn.md#ga77108581b8f61485ca840e4bf7a17087)(const struct bt\_conn \*conn);

276

[ 287](group__bt__conn.md#gad4aed76b80cc815f748ad0e84ae3d87c)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_conn\_index](group__bt__conn.md#gad4aed76b80cc815f748ad0e84ae3d87c)(const struct bt\_conn \*conn);

288

[ 290](structbt__conn__le__info.md)struct [bt\_conn\_le\_info](structbt__conn__le__info.md) {

[ 292](structbt__conn__le__info.md#a5f1eacec82f31182460d6d5359a8b295) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[src](structbt__conn__le__info.md#a5f1eacec82f31182460d6d5359a8b295);

[ 296](structbt__conn__le__info.md#a1f78e1c0ed3482ce6eec9ce6eeda4769) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[dst](structbt__conn__le__info.md#a1f78e1c0ed3482ce6eec9ce6eeda4769);

[ 298](structbt__conn__le__info.md#a3be5df0deb0af08f84843eb3c6a5e5ae) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[local](structbt__conn__le__info.md#a3be5df0deb0af08f84843eb3c6a5e5ae);

[ 300](structbt__conn__le__info.md#a236d1c97c735c7cfaead0b1a3672d512) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[remote](structbt__conn__le__info.md#a236d1c97c735c7cfaead0b1a3672d512);

[ 301](structbt__conn__le__info.md#a95a1f635e53f16d5839cdd58f4bda962) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__conn__le__info.md#a95a1f635e53f16d5839cdd58f4bda962);

[ 302](structbt__conn__le__info.md#acd83835fe5ec0878fd653b87cb570a49) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__conn__le__info.md#acd83835fe5ec0878fd653b87cb570a49);

[ 303](structbt__conn__le__info.md#afb4dc594d063fbbad2bcd4acf047f716) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__conn__le__info.md#afb4dc594d063fbbad2bcd4acf047f716);

304

305#if defined(CONFIG\_BT\_USER\_PHY\_UPDATE)

[ 306](structbt__conn__le__info.md#a215d39c6cd7da1ac033529b5541cbfc1) const struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \*[phy](structbt__conn__le__info.md#a215d39c6cd7da1ac033529b5541cbfc1);

307#endif /\* defined(CONFIG\_BT\_USER\_PHY\_UPDATE) \*/

308

309#if defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE)

310 /\* Connection maximum single fragment parameters \*/

[ 311](structbt__conn__le__info.md#ae309f390c8d7b33a4de55791af235ab0) const struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \*[data\_len](structbt__conn__le__info.md#ae309f390c8d7b33a4de55791af235ab0);

312#endif /\* defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE) \*/

313};

314

[ 322](group__bt__conn.md#ga707cc62b12c89478aebd0488a464a776)#define BT\_CONN\_INTERVAL\_TO\_MS(interval) ((interval) \* 5U / 4U)

323

[ 328](group__bt__conn.md#ga0a5fac126005684847ee7509bb98e382)#define BT\_CONN\_INTERVAL\_TO\_US(interval) ((interval) \* 1250U)

329

[ 331](structbt__conn__br__info.md)struct [bt\_conn\_br\_info](structbt__conn__br__info.md) {

[ 332](structbt__conn__br__info.md#aeef49f711872ccfec5dd558c4552b71e) const [bt\_addr\_t](structbt__addr__t.md) \*[dst](structbt__conn__br__info.md#aeef49f711872ccfec5dd558c4552b71e);

333};

334

335enum {

[ 336](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) [BT\_CONN\_ROLE\_CENTRAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) = 0,

[ 337](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) [BT\_CONN\_ROLE\_PERIPHERAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) = 1,

338};

339

[ 340](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282)enum [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) {

[ 342](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587) [BT\_CONN\_STATE\_DISCONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587),

[ 344](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd) [BT\_CONN\_STATE\_CONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd),

[ 346](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f) [BT\_CONN\_STATE\_CONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f),

[ 348](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f) [BT\_CONN\_STATE\_DISCONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f),

349};

350

[ 352](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)typedef enum \_\_packed {

[ 354](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e) [BT\_SECURITY\_L0](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e),

[ 356](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b) [BT\_SECURITY\_L1](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b),

[ 358](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a) [BT\_SECURITY\_L2](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a),

[ 360](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631) [BT\_SECURITY\_L3](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631),

[ 362](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81) [BT\_SECURITY\_L4](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81),

[ 366](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) [BT\_SECURITY\_FORCE\_PAIR](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

367} [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783);

368

[ 370](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e)enum [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) {

[ 372](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6) [BT\_SECURITY\_FLAG\_SC](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 374](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198) [BT\_SECURITY\_FLAG\_OOB](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

375};

376

[ 378](structbt__security__info.md)struct [bt\_security\_info](structbt__security__info.md) {

[ 380](structbt__security__info.md#a7b18849fad25b3f2da6b8c85a56d86e1) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [level](structbt__security__info.md#a7b18849fad25b3f2da6b8c85a56d86e1);

[ 382](structbt__security__info.md#a6567ffb82b7fa8093cc57ef4662873ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enc\_key\_size](structbt__security__info.md#a6567ffb82b7fa8093cc57ef4662873ba);

[ 384](structbt__security__info.md#a99cb4af08bfa1dab182821d956368526) enum [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) [flags](structbt__security__info.md#a99cb4af08bfa1dab182821d956368526);

385};

386

[ 388](group__bt__conn.md#ga047061be4b45bcdd5c84114b01567592)#define BT\_CONN\_ROLE\_MASTER \_\_DEPRECATED\_MACRO BT\_CONN\_ROLE\_CENTRAL

[ 389](group__bt__conn.md#ga65a7e3af728d3d60f484b4f166ac9882)#define BT\_CONN\_ROLE\_SLAVE \_\_DEPRECATED\_MACRO BT\_CONN\_ROLE\_PERIPHERAL

390

[ 392](structbt__conn__info.md)struct [bt\_conn\_info](structbt__conn__info.md) {

[ 394](structbt__conn__info.md#a7995e1291be494b5bdf860eceea0cad1) enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) [type](structbt__conn__info.md#a7995e1291be494b5bdf860eceea0cad1);

[ 396](structbt__conn__info.md#a8237b8c1bb9a97a174d04cbe13dca7c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [role](structbt__conn__info.md#a8237b8c1bb9a97a174d04cbe13dca7c7);

[ 398](structbt__conn__info.md#a3a4e24519b5d3ba547423e53c4d92a5c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__conn__info.md#a3a4e24519b5d3ba547423e53c4d92a5c);

400 union {

[ 402](structbt__conn__info.md#a6b536e7732dcf7b77a7bc05116dca548) struct [bt\_conn\_le\_info](structbt__conn__le__info.md) [le](structbt__conn__info.md#a6b536e7732dcf7b77a7bc05116dca548);

[ 404](structbt__conn__info.md#a799e59d3a85625799a32ac3f0b3d67d1) struct [bt\_conn\_br\_info](structbt__conn__br__info.md) [br](structbt__conn__info.md#a799e59d3a85625799a32ac3f0b3d67d1);

405 };

[ 407](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc) enum [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) [state](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc);

[ 409](structbt__conn__info.md#ae4405f1b4f3fe2ff6253453964860931) struct [bt\_security\_info](structbt__security__info.md) [security](structbt__conn__info.md#ae4405f1b4f3fe2ff6253453964860931);

410};

411

[ 413](structbt__conn__le__remote__info.md)struct [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md) {

414

[ 416](structbt__conn__le__remote__info.md#a4ff434f6c501dc60db5c4b776be46b3b) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[features](structbt__conn__le__remote__info.md#a4ff434f6c501dc60db5c4b776be46b3b);

417};

418

[ 420](structbt__conn__br__remote__info.md)struct [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md) {

421

[ 423](structbt__conn__br__remote__info.md#afa19f7db400bb0de234e8cda61f3deaf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[features](structbt__conn__br__remote__info.md#afa19f7db400bb0de234e8cda61f3deaf);

424

[ 426](structbt__conn__br__remote__info.md#a798c179c803e709182a1b0c3594f4a0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_pages](structbt__conn__br__remote__info.md#a798c179c803e709182a1b0c3594f4a0a);

427};

428

[ 434](structbt__conn__remote__info.md)struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) {

[ 436](structbt__conn__remote__info.md#a8bb514196bde5df561dbf76b68060729) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__conn__remote__info.md#a8bb514196bde5df561dbf76b68060729);

437

[ 439](structbt__conn__remote__info.md#a2664f6ed3bd22f9a011126daf5d81376) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structbt__conn__remote__info.md#a2664f6ed3bd22f9a011126daf5d81376);

440

[ 442](structbt__conn__remote__info.md#a47cc5a4b8888a0b8faaf6880c37418b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manufacturer](structbt__conn__remote__info.md#a47cc5a4b8888a0b8faaf6880c37418b8);

443

[ 445](structbt__conn__remote__info.md#a360979a15c958706157fc630fd55cbca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [subversion](structbt__conn__remote__info.md#a360979a15c958706157fc630fd55cbca);

446

447 union {

[ 449](structbt__conn__remote__info.md#ae75530b09c6dea416630a4a19a1d64cc) struct [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md) [le](structbt__conn__remote__info.md#ae75530b09c6dea416630a4a19a1d64cc);

450

[ 452](structbt__conn__remote__info.md#ab73365f09cdb5ce870272546543bcfeb) struct [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md) [br](structbt__conn__remote__info.md#ab73365f09cdb5ce870272546543bcfeb);

453 };

454};

455

[ 456](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190)enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) {

[ 458](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a) [BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a),

[ 460](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046) [BT\_CONN\_LE\_TX\_POWER\_PHY\_1M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046),

[ 462](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800) [BT\_CONN\_LE\_TX\_POWER\_PHY\_2M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800),

[ 464](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2) [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2),

[ 466](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296) [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296),

467};

468

[ 470](structbt__conn__le__tx__power.md)struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) {

471

[ 473](structbt__conn__le__tx__power.md#a8702c4ff5082b8f90decdfabfb8253fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__conn__le__tx__power.md#a8702c4ff5082b8f90decdfabfb8253fe);

474

[ 476](structbt__conn__le__tx__power.md#a6d2e5a5215fa5d60630e74928a67fc04) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [current\_level](structbt__conn__le__tx__power.md#a6d2e5a5215fa5d60630e74928a67fc04);

477

[ 479](structbt__conn__le__tx__power.md#a1674247c511906fa6f0193653ed0b71a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_level](structbt__conn__le__tx__power.md#a1674247c511906fa6f0193653ed0b71a);

480};

481

482

[ 484](structbt__conn__le__tx__power__report.md)struct [bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md) {

485

[ 489](structbt__conn__le__tx__power__report.md#aa5606925229784af8ae90542432cf200) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__conn__le__tx__power__report.md#aa5606925229784af8ae90542432cf200);

490

[ 492](structbt__conn__le__tx__power__report.md#a5b1f67537fbe945f2f258b47082723b4) enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) [phy](structbt__conn__le__tx__power__report.md#a5b1f67537fbe945f2f258b47082723b4);

493

[ 502](structbt__conn__le__tx__power__report.md#ace830ddb7ae662c9759babed87f1b6f3) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__conn__le__tx__power__report.md#ace830ddb7ae662c9759babed87f1b6f3);

503

[ 507](structbt__conn__le__tx__power__report.md#ae7a4f77c6f7af1a459896d25cf661eb8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_power\_level\_flag](structbt__conn__le__tx__power__report.md#ae7a4f77c6f7af1a459896d25cf661eb8);

508

[ 515](structbt__conn__le__tx__power__report.md#a7c681c7b9f77d994b2de1febea7c5dc9) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [delta](structbt__conn__le__tx__power__report.md#a7c681c7b9f77d994b2de1febea7c5dc9);

516};

517

[ 523](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043)enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) {

[ 524](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6) [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6) = 0x00,

[ 525](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1) [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1) = 0x01,

[ 526](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529) [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529) = 0x02,

[ 527](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da) [BT\_CONN\_AUTH\_KEYPRESS\_CLEARED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da) = 0x03,

[ 528](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8) [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8) = 0x04,

529};

530

[ 538](group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)int [bt\_conn\_get\_info](group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)(const struct bt\_conn \*conn, struct [bt\_conn\_info](structbt__conn__info.md) \*info);

539

[ 555](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92)int [bt\_conn\_get\_remote\_info](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92)(struct bt\_conn \*conn,

556 struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info);

557

[ 566](group__bt__conn.md#gaa5289154bc508444f68df7abcef18aca)int [bt\_conn\_le\_get\_tx\_power\_level](group__bt__conn.md#gaa5289154bc508444f68df7abcef18aca)(struct bt\_conn \*conn,

567 struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power\_level);

568

[ 577](group__bt__conn.md#gaa79eada87d698f4998af876d03d7e92b)int [bt\_conn\_le\_enhanced\_get\_tx\_power\_level](group__bt__conn.md#gaa79eada87d698f4998af876d03d7e92b)(struct bt\_conn \*conn,

578 struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power);

579

[ 588](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4)int [bt\_conn\_le\_get\_remote\_tx\_power\_level](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4)(struct bt\_conn \*conn,

589 enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) phy);

590

[ 600](group__bt__conn.md#gaa1f38911acee0534a8a6e414018c6fb6)int [bt\_conn\_le\_set\_tx\_power\_report\_enable](group__bt__conn.md#gaa1f38911acee0534a8a6e414018c6fb6)(struct bt\_conn \*conn,

601 bool local\_enable,

602 bool remote\_enable);

603

[ 615](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb)int [bt\_conn\_le\_param\_update](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb)(struct bt\_conn \*conn,

616 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param);

617

[ 625](group__bt__conn.md#ga8a2006f6e34b20c7e8ef65a73f431a57)int [bt\_conn\_le\_data\_len\_update](group__bt__conn.md#ga8a2006f6e34b20c7e8ef65a73f431a57)(struct bt\_conn \*conn,

626 const struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) \*param);

627

[ 638](group__bt__conn.md#gae13ed81b1e7928f44b8fdf85995b3e58)int [bt\_conn\_le\_phy\_update](group__bt__conn.md#gae13ed81b1e7928f44b8fdf85995b3e58)(struct bt\_conn \*conn,

639 const struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) \*param);

640

[ 663](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3)int [bt\_conn\_disconnect](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

664

665enum {

[ 667](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9) [BT\_CONN\_LE\_OPT\_NONE](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9) = 0,

668

[ 673](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b) [BT\_CONN\_LE\_OPT\_CODED](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

674

[ 681](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9) [BT\_CONN\_LE\_OPT\_NO\_1M](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

682};

683

[ 684](structbt__conn__le__create__param.md)struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) {

685

[ 687](structbt__conn__le__create__param.md#a4b1e26c0976d9c900b831c886c77b055) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__conn__le__create__param.md#a4b1e26c0976d9c900b831c886c77b055);

688

[ 690](structbt__conn__le__create__param.md#a5cfae677f924534dc5bc7b38c457a7af) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__conn__le__create__param.md#a5cfae677f924534dc5bc7b38c457a7af);

691

[ 693](structbt__conn__le__create__param.md#a339b99f65c5029ada6cdf453ab1f258e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__conn__le__create__param.md#a339b99f65c5029ada6cdf453ab1f258e);

694

[ 699](structbt__conn__le__create__param.md#a2bc978ac97435fe5f87c6e01692f2910) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_coded](structbt__conn__le__create__param.md#a2bc978ac97435fe5f87c6e01692f2910);

700

[ 705](structbt__conn__le__create__param.md#ae62491837d35d95e32016b793edf8c96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window\_coded](structbt__conn__le__create__param.md#ae62491837d35d95e32016b793edf8c96);

706

[ 714](structbt__conn__le__create__param.md#a59f05bfb9468779d02f8d0beeb7a35c1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__conn__le__create__param.md#a59f05bfb9468779d02f8d0beeb7a35c1);

715};

716

[ 723](group__bt__conn.md#ga8ac93a19c34d2821c158f310879fe00d)#define BT\_CONN\_LE\_CREATE\_PARAM\_INIT(\_options, \_interval, \_window) \

724{ \

725 .options = (\_options), \

726 .interval = (\_interval), \

727 .window = (\_window), \

728 .interval\_coded = 0, \

729 .window\_coded = 0, \

730 .timeout = 0, \

731}

732

[ 739](group__bt__conn.md#gae86425d432078e2ddca260eebc2802f1)#define BT\_CONN\_LE\_CREATE\_PARAM(\_options, \_interval, \_window) \

740 ((struct bt\_conn\_le\_create\_param[]) { \

741 BT\_CONN\_LE\_CREATE\_PARAM\_INIT(\_options, \_interval, \_window) \

742 })

743

[ 747](group__bt__conn.md#gab4203c55c20d83256ca036148c14a00d)#define BT\_CONN\_LE\_CREATE\_CONN \

748 BT\_CONN\_LE\_CREATE\_PARAM(BT\_CONN\_LE\_OPT\_NONE, \

749 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

750 BT\_GAP\_SCAN\_FAST\_INTERVAL)

751

[ 756](group__bt__conn.md#gaaba7c37a5c6e98e7b62ac12bde814d5d)#define BT\_CONN\_LE\_CREATE\_CONN\_AUTO \

757 BT\_CONN\_LE\_CREATE\_PARAM(BT\_CONN\_LE\_OPT\_NONE, \

758 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

759 BT\_GAP\_SCAN\_FAST\_WINDOW)

760

[ 780](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6)int [bt\_conn\_le\_create](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer,

781 const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param,

782 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param,

783 struct bt\_conn \*\*conn);

784

[ 785](structbt__conn__le__create__synced__param.md)struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) {

786

[ 792](structbt__conn__le__create__synced__param.md#ac5872dda4042e3ba6c161dce60784b70) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[peer](structbt__conn__le__create__synced__param.md#ac5872dda4042e3ba6c161dce60784b70);

793

[ 795](structbt__conn__le__create__synced__param.md#ac7b4e4144aaf914bdef1dc305b5e297f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__conn__le__create__synced__param.md#ac7b4e4144aaf914bdef1dc305b5e297f);

796};

797

[ 815](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1)int [bt\_conn\_le\_create\_synced](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1)(const struct bt\_le\_ext\_adv \*adv,

816 const struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) \*synced\_param,

817 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param, struct bt\_conn \*\*conn);

818

[ 834](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b)int [bt\_conn\_le\_create\_auto](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b)(const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param,

835 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param);

836

[ 841](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4)int [bt\_conn\_create\_auto\_stop](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4)(void);

842

[ 857](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a)int [bt\_le\_set\_auto\_conn](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr,

858 const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param);

859

[ 896](group__bt__conn.md#gae001f1268e1ff42c3c974c95dcb6735d)int [bt\_conn\_set\_security](group__bt__conn.md#gae001f1268e1ff42c3c974c95dcb6735d)(struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) sec);

897

[ 902](group__bt__conn.md#ga4b43ef0f30146808e560991a302e88ad)[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [bt\_conn\_get\_security](group__bt__conn.md#ga4b43ef0f30146808e560991a302e88ad)(const struct bt\_conn \*conn);

903

[ 913](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_conn\_enc\_key\_size](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e)(const struct bt\_conn \*conn);

914

[ 915](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff)enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) {

[ 917](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05) [BT\_SECURITY\_ERR\_SUCCESS](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05),

918

[ 920](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7) [BT\_SECURITY\_ERR\_AUTH\_FAIL](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7),

921

[ 923](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171) [BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171),

924

[ 926](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7) [BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7),

927

[ 929](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae) [BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae),

930

[ 932](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6) [BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6),

933

[ 935](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f) [BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f),

936

[ 938](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5) [BT\_SECURITY\_ERR\_INVALID\_PARAM](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5),

939

[ 941](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216) [BT\_SECURITY\_ERR\_KEY\_REJECTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216),

942

[ 944](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242) [BT\_SECURITY\_ERR\_UNSPECIFIED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242),

945};

946

[ 957](structbt__conn__cb.md)struct [bt\_conn\_cb](structbt__conn__cb.md) {

[ 982](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69) void (\*[connected](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err);

983

[ 1001](structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914) void (\*[disconnected](structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

1002

[ 1015](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b) void (\*[recycled](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b))(void);

1016

[ 1041](structbt__conn__cb.md#a2c52c2e2798062708c373fae9610fadd) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[le\_param\_req](structbt__conn__cb.md#a2c52c2e2798062708c373fae9610fadd))(struct bt\_conn \*conn,

1042 struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param);

1043

[ 1054](structbt__conn__cb.md#a01582ed3e3801e10c665534eaa991454) void (\*[le\_param\_updated](structbt__conn__cb.md#a01582ed3e3801e10c665534eaa991454))(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) interval,

1055 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) latency, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout);

1056#if defined(CONFIG\_BT\_SMP)

[ 1066](structbt__conn__cb.md#aea9b62ab1a1469be97a207a8e07d2f14) void (\*[identity\_resolved](structbt__conn__cb.md#aea9b62ab1a1469be97a207a8e07d2f14))(struct bt\_conn \*conn,

1067 const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*rpa,

1068 const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*identity);

1069#endif /\* CONFIG\_BT\_SMP \*/

1070#if defined(CONFIG\_BT\_SMP) || defined(CONFIG\_BT\_BREDR)

[ 1087](structbt__conn__cb.md#ae454d5bc2664e90ba2b1e0c867db374e) void (\*[security\_changed](structbt__conn__cb.md#ae454d5bc2664e90ba2b1e0c867db374e))(struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) level,

1088 enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err);

1089#endif /\* defined(CONFIG\_BT\_SMP) || defined(CONFIG\_BT\_BREDR) \*/

1090

1091#if defined(CONFIG\_BT\_REMOTE\_INFO)

[ 1100](structbt__conn__cb.md#af726f004c06b86f770ece263ed6c9ca4) void (\*[remote\_info\_available](structbt__conn__cb.md#af726f004c06b86f770ece263ed6c9ca4))(struct bt\_conn \*conn,

1101 struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info);

1102#endif /\* defined(CONFIG\_BT\_REMOTE\_INFO) \*/

1103

1104#if defined(CONFIG\_BT\_USER\_PHY\_UPDATE)

[ 1113](structbt__conn__cb.md#ae02a23d823954a747f8f474fb19276d7) void (\*[le\_phy\_updated](structbt__conn__cb.md#ae02a23d823954a747f8f474fb19276d7))(struct bt\_conn \*conn,

1114 struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \*param);

1115#endif /\* defined(CONFIG\_BT\_USER\_PHY\_UPDATE) \*/

1116

1117#if defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE)

[ 1126](structbt__conn__cb.md#a1142d1861cc0b0058f68ecf537d0cec3) void (\*[le\_data\_len\_updated](structbt__conn__cb.md#a1142d1861cc0b0058f68ecf537d0cec3))(struct bt\_conn \*conn,

1127 struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \*info);

1128#endif /\* defined(CONFIG\_BT\_USER\_DATA\_LEN\_UPDATE) \*/

1129

1130#if defined(CONFIG\_BT\_DF\_CONNECTION\_CTE\_RX)

1137 void (\*cte\_report\_cb)(struct bt\_conn \*conn,

1138 const struct [bt\_df\_conn\_iq\_samples\_report](structbt__df__conn__iq__samples__report.md) \*iq\_report);

1139#endif /\* CONFIG\_BT\_DF\_CONNECTION\_CTE\_RX \*/

1140

1141#if defined(CONFIG\_BT\_TRANSMIT\_POWER\_CONTROL)

1153 void (\*tx\_power\_report)(struct bt\_conn \*conn,

1154 const struct [bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md) \*report);

1155#endif /\* CONFIG\_BT\_TRANSMIT\_POWER\_CONTROL \*/

1156

1157 struct [bt\_conn\_cb](structbt__conn__cb.md) \*\_next;

1158};

1159

[ 1166](group__bt__conn.md#ga33b35e6457af183e059078aead4562b4)void [bt\_conn\_cb\_register](group__bt__conn.md#ga33b35e6457af183e059078aead4562b4)(struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb);

1167

[ 1179](group__bt__conn.md#gad2f90b34390e3c3697fd455ae4ef5f31)int [bt\_conn\_cb\_unregister](group__bt__conn.md#gad2f90b34390e3c3697fd455ae4ef5f31)(struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb);

1180

[ 1186](group__bt__conn.md#ga9227880a1ae5fc373d334171e1450f00)#define BT\_CONN\_CB\_DEFINE(\_name) \

1187 static const STRUCT\_SECTION\_ITERABLE(bt\_conn\_cb, \

1188 \_CONCAT(bt\_conn\_cb\_, \

1189 \_name))

1190

[ 1201](group__bt__conn.md#ga014db594b17a3b5d7d954e64ad8de759)void [bt\_set\_bondable](group__bt__conn.md#ga014db594b17a3b5d7d954e64ad8de759)(bool enable);

1202

[ 1221](group__bt__conn.md#ga4165819d12dd96e00dfa2fd6f4b95669)int [bt\_conn\_set\_bondable](group__bt__conn.md#ga4165819d12dd96e00dfa2fd6f4b95669)(struct bt\_conn \*conn, bool enable);

1222

[ 1229](group__bt__conn.md#gad02f8fe587efd543c0c81cace3f63d63)void [bt\_le\_oob\_set\_sc\_flag](group__bt__conn.md#gad02f8fe587efd543c0c81cace3f63d63)(bool enable);

1230

[ 1237](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892)void [bt\_le\_oob\_set\_legacy\_flag](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892)(bool enable);

1238

[ 1250](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba)int [bt\_le\_oob\_set\_legacy\_tk](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba)(struct bt\_conn \*conn, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tk);

1251

[ 1270](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503)int [bt\_le\_oob\_set\_sc\_data](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503)(struct bt\_conn \*conn,

1271 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_local,

1272 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_remote);

1273

[ 1289](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee)int [bt\_le\_oob\_get\_sc\_data](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee)(struct bt\_conn \*conn,

1290 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_local,

1291 const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_remote);

1292

[ 1297](group__bt__conn.md#gaf638077430b418f9879ac4ddf58ef17a)#define BT\_PASSKEY\_INVALID 0xffffffff

1298

[ 1312](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1)int [bt\_passkey\_set](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1)(unsigned int passkey);

1313

[ 1315](structbt__conn__oob__info.md)struct [bt\_conn\_oob\_info](structbt__conn__oob__info.md) {

1317 enum {

[ 1319](structbt__conn__oob__info.md#a433c4a8e1efcb663ad369d018d999b0ea4c33ea839306256a198c29ea783c659b) [BT\_CONN\_OOB\_LE\_LEGACY](structbt__conn__oob__info.md#a433c4a8e1efcb663ad369d018d999b0ea4c33ea839306256a198c29ea783c659b),

1320

[ 1322](structbt__conn__oob__info.md#a433c4a8e1efcb663ad369d018d999b0eacd02773beb42df3fb6cbaa2fa2abda1e) [BT\_CONN\_OOB\_LE\_SC](structbt__conn__oob__info.md#a433c4a8e1efcb663ad369d018d999b0eacd02773beb42df3fb6cbaa2fa2abda1e),

[ 1323](structbt__conn__oob__info.md#aa793302d7c6c41a1b714ab219a1f14c9) } [type](structbt__conn__oob__info.md#aa793302d7c6c41a1b714ab219a1f14c9);

1324

1325 union {

1327 struct {

1329 enum {

[ 1331](structbt__conn__oob__info.md#a72a749120c0a55a8dc9bd078921277e5) [BT\_CONN\_OOB\_LOCAL\_ONLY](structbt__conn__oob__info.md#a72a749120c0a55a8dc9bd078921277e5),

1332

[ 1334](structbt__conn__oob__info.md#a7506049b35ac63602452b087d1d60fa2) [BT\_CONN\_OOB\_REMOTE\_ONLY](structbt__conn__oob__info.md#a7506049b35ac63602452b087d1d60fa2),

1335

[ 1337](structbt__conn__oob__info.md#a99685ad84ac991e0540855cab5546ff8) [BT\_CONN\_OOB\_BOTH\_PEERS](structbt__conn__oob__info.md#a99685ad84ac991e0540855cab5546ff8),

1338

[ 1340](structbt__conn__oob__info.md#a71bf295d82fbc647b3816bfba6fa0ae7) [BT\_CONN\_OOB\_NO\_DATA](structbt__conn__oob__info.md#a71bf295d82fbc647b3816bfba6fa0ae7),

[ 1341](structbt__conn__oob__info.md#aa20bbff037e6878216d7dd45938bca76) } [oob\_config](structbt__conn__oob__info.md#aa20bbff037e6878216d7dd45938bca76);

[ 1342](structbt__conn__oob__info.md#ad721c4bbe51bec994362b35944579240) } [lesc](structbt__conn__oob__info.md#ad721c4bbe51bec994362b35944579240);

1343 };

1344};

1345

1346#if defined(CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT)

[ 1353](structbt__conn__pairing__feat.md)struct [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) {

[ 1355](structbt__conn__pairing__feat.md#a68005cea273c8e76c086502001b258b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [io\_capability](structbt__conn__pairing__feat.md#a68005cea273c8e76c086502001b258b0);

1356

[ 1358](structbt__conn__pairing__feat.md#afb03164960db62b4b4cf70d3f0134099) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [oob\_data\_flag](structbt__conn__pairing__feat.md#afb03164960db62b4b4cf70d3f0134099);

1359

[ 1361](structbt__conn__pairing__feat.md#af9a977b1e0f9d4eada26a82d92eaec54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [auth\_req](structbt__conn__pairing__feat.md#af9a977b1e0f9d4eada26a82d92eaec54);

1362

[ 1364](structbt__conn__pairing__feat.md#abe1d7d4bd9f4b551a2d0c69adc75bd40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_enc\_key\_size](structbt__conn__pairing__feat.md#abe1d7d4bd9f4b551a2d0c69adc75bd40);

1365

[ 1369](structbt__conn__pairing__feat.md#a70adc125b875348ec8d273dea3b470d8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_key\_dist](structbt__conn__pairing__feat.md#a70adc125b875348ec8d273dea3b470d8);

1370

[ 1374](structbt__conn__auth__cb.md#a92391a172e158a42966f410d732424a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [resp\_key\_dist](structbt__conn__pairing__feat.md#a49f9f02e232e91f7f7a530aa7f226cba);

1375};

1376#endif /\* CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT \*/

1377

[ 1379](structbt__conn__auth__cb.md)struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) {

1380#if defined(CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT)

1408 enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) (\*[pairing\_accept](structbt__conn__auth__cb.md#a92391a172e158a42966f410d732424a7))(struct bt\_conn \*conn,

1409 const struct [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) \*const feat);

1410#endif /\* CONFIG\_BT\_SMP\_APP\_PAIRING\_ACCEPT \*/

1411

[ 1430](structbt__conn__auth__cb.md#a14074ca97fad6af4c58c43a00c503104) void (\*[passkey\_display](structbt__conn__auth__cb.md#a14074ca97fad6af4c58c43a00c503104))(struct bt\_conn \*conn, unsigned int passkey);

1431

1432#if defined(CONFIG\_BT\_PASSKEY\_KEYPRESS)

1454 void (\*passkey\_display\_keypress)(struct bt\_conn \*conn,

1455 enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) type);

1456#endif

1457

[ 1476](structbt__conn__auth__cb.md#a10f9d22c89c95a6f3ffe0016f92445c0) void (\*[passkey\_entry](structbt__conn__auth__cb.md#a10f9d22c89c95a6f3ffe0016f92445c0))(struct bt\_conn \*conn);

1477

[ 1499](structbt__conn__auth__cb.md#a2bb6c10666d111f675fd6de5ff51410a) void (\*[passkey\_confirm](structbt__conn__auth__cb.md#a2bb6c10666d111f675fd6de5ff51410a))(struct bt\_conn \*conn, unsigned int passkey);

1500

[ 1517](structbt__conn__auth__cb.md#aec9f6256607ea2cd1ce1b4cdb3052b42) void (\*[oob\_data\_request](structbt__conn__auth__cb.md#aec9f6256607ea2cd1ce1b4cdb3052b42))(struct bt\_conn \*conn,

1518 struct [bt\_conn\_oob\_info](structbt__conn__oob__info.md) \*info);

1519

[ 1532](structbt__conn__auth__cb.md#af6eb01c252ba3e32ff8bf583aa6ca0a4) void (\*[cancel](structbt__conn__auth__cb.md#af6eb01c252ba3e32ff8bf583aa6ca0a4))(struct bt\_conn \*conn);

1533

[ 1552](structbt__conn__auth__cb.md#af4f7d3ee570b3472ee79b014be01f76e) void (\*[pairing\_confirm](structbt__conn__auth__cb.md#af4f7d3ee570b3472ee79b014be01f76e))(struct bt\_conn \*conn);

1553

1554#if defined(CONFIG\_BT\_BREDR)

[ 1573](structbt__conn__auth__cb.md#ab6df1b1505dc22dd8dae0e946546c8bb) void (\*[pincode\_entry](structbt__conn__auth__cb.md#ab6df1b1505dc22dd8dae0e946546c8bb))(struct bt\_conn \*conn, bool highsec);

1574#endif

1575};

1576

[ 1578](structbt__conn__auth__info__cb.md)struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) {

[ 1588](structbt__conn__auth__info__cb.md#aea737700f2760de1ed26a721b5e860d2) void (\*[pairing\_complete](structbt__conn__auth__info__cb.md#aea737700f2760de1ed26a721b5e860d2))(struct bt\_conn \*conn, bool bonded);

1589

[ 1595](structbt__conn__auth__info__cb.md#ae7228bb82889eacebf67e1d4b3b23375) void (\*[pairing\_failed](structbt__conn__auth__info__cb.md#ae7228bb82889eacebf67e1d4b3b23375))(struct bt\_conn \*conn,

1596 enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) reason);

1597

[ 1606](structbt__conn__auth__info__cb.md#af20b0d7fc5fd8399ad9368b3ef7067f8) void (\*[bond\_deleted](structbt__conn__auth__info__cb.md#af20b0d7fc5fd8399ad9368b3ef7067f8))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer);

1607

[ 1609](structbt__conn__auth__info__cb.md#afde62f2cdfb40b4154208f3c1c3dadc1) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__conn__auth__info__cb.md#afde62f2cdfb40b4154208f3c1c3dadc1);

1610};

1611

[ 1621](group__bt__conn.md#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)int [bt\_conn\_auth\_cb\_register](group__bt__conn.md#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)(const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb);

1622

[ 1637](group__bt__conn.md#ga81077385583d71c248a1eb6aab9ee86e)int [bt\_conn\_auth\_cb\_overlay](group__bt__conn.md#ga81077385583d71c248a1eb6aab9ee86e)(struct bt\_conn \*conn, const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb);

1638

[ 1648](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f)int [bt\_conn\_auth\_info\_cb\_register](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f)(struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb);

1649

[ 1658](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37)int [bt\_conn\_auth\_info\_cb\_unregister](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37)(struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb);

1659

[ 1670](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)int [bt\_conn\_auth\_passkey\_entry](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)(struct bt\_conn \*conn, unsigned int passkey);

1671

[ 1687](group__bt__conn.md#ga2987a902da4f5cfe3671c60d154ced7e)int [bt\_conn\_auth\_keypress\_notify](group__bt__conn.md#ga2987a902da4f5cfe3671c60d154ced7e)(struct bt\_conn \*conn, enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) type);

1688

[ 1697](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59)int [bt\_conn\_auth\_cancel](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59)(struct bt\_conn \*conn);

1698

[ 1708](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995)int [bt\_conn\_auth\_passkey\_confirm](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995)(struct bt\_conn \*conn);

1709

[ 1719](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d)int [bt\_conn\_auth\_pairing\_confirm](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d)(struct bt\_conn \*conn);

1720

[ 1731](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98)int [bt\_conn\_auth\_pincode\_entry](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98)(struct bt\_conn \*conn, const char \*pin);

1732

[ 1734](structbt__br__conn__param.md)struct [bt\_br\_conn\_param](structbt__br__conn__param.md) {

[ 1735](structbt__br__conn__param.md#a95454a74932a14b4137c3fe82821be49) bool [allow\_role\_switch](structbt__br__conn__param.md#a95454a74932a14b4137c3fe82821be49);

1736};

1737

[ 1742](group__bt__conn.md#ga986f563bfb741c70fbee39b3948d9d8d)#define BT\_BR\_CONN\_PARAM\_INIT(role\_switch) \

1743{ \

1744 .allow\_role\_switch = (role\_switch), \

1745}

1746

[ 1751](group__bt__conn.md#ga6f99f4adfcef36a4d738783921965ca6)#define BT\_BR\_CONN\_PARAM(role\_switch) \

1752 ((struct bt\_br\_conn\_param[]) { \

1753 BT\_BR\_CONN\_PARAM\_INIT(role\_switch) \

1754 })

1755

[ 1759](group__bt__conn.md#ga5ccdbff63a430a37a8a8077d8792f706)#define BT\_BR\_CONN\_PARAM\_DEFAULT BT\_BR\_CONN\_PARAM(true)

1760

1761

[ 1774](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9)struct bt\_conn \*[bt\_conn\_create\_br](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9)(const [bt\_addr\_t](structbt__addr__t.md) \*peer,

1775 const struct [bt\_br\_conn\_param](structbt__br__conn__param.md) \*param);

1776

[ 1788](group__bt__conn.md#gac270287d6764dff1963f859a51a438e4)struct bt\_conn \*[bt\_conn\_create\_sco](group__bt__conn.md#gac270287d6764dff1963f859a51a438e4)(const [bt\_addr\_t](structbt__addr__t.md) \*peer);

1789

1790#ifdef \_\_cplusplus

1791}

1792#endif

1793

1797

1798#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_CONN\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[bluetooth.h](bluetooth_8h.md)

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

[bt\_conn\_le\_get\_remote\_tx\_power\_level](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4)

int bt\_conn\_le\_get\_remote\_tx\_power\_level(struct bt\_conn \*conn, enum bt\_conn\_le\_tx\_power\_phy phy)

Get remote (peer) transmit power level.

[bt\_le\_oob\_get\_sc\_data](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee)

int bt\_le\_oob\_get\_sc\_data(struct bt\_conn \*conn, const struct bt\_le\_oob\_sc\_data \*\*oobd\_local, const struct bt\_le\_oob\_sc\_data \*\*oobd\_remote)

Get OOB data used for LE Secure Connections (SC) pairing procedure.

[bt\_le\_oob\_set\_legacy\_tk](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba)

int bt\_le\_oob\_set\_legacy\_tk(struct bt\_conn \*conn, const uint8\_t \*tk)

Set OOB Temporary Key to be used for pairing.

[bt\_conn\_disconnect](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3)

int bt\_conn\_disconnect(struct bt\_conn \*conn, uint8\_t reason)

Disconnect from a remote device or cancel pending connection.

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

**Definition** conn.h:370

[bt\_passkey\_set](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1)

int bt\_passkey\_set(unsigned int passkey)

Set a fixed passkey to be used for pairing.

[bt\_conn\_cb\_register](group__bt__conn.md#ga33b35e6457af183e059078aead4562b4)

void bt\_conn\_cb\_register(struct bt\_conn\_cb \*cb)

Register connection callbacks.

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

[bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043)

bt\_conn\_auth\_keypress

Passkey Keypress Notification type.

**Definition** conn.h:523

[bt\_conn\_foreach](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916)

void bt\_conn\_foreach(enum bt\_conn\_type type, void(\*func)(struct bt\_conn \*conn, void \*data), void \*data)

Iterate through all bt\_conn objects.

[bt\_conn\_create\_auto\_stop](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4)

int bt\_conn\_create\_auto\_stop(void)

Stop automatic connect creation.

[bt\_conn\_get\_remote\_info](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92)

int bt\_conn\_get\_remote\_info(struct bt\_conn \*conn, struct bt\_conn\_remote\_info \*remote\_info)

Get connection info for the remote device.

[bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190)

bt\_conn\_le\_tx\_power\_phy

**Definition** conn.h:456

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

[bt\_le\_set\_auto\_conn](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a)

int bt\_le\_set\_auto\_conn(const bt\_addr\_le\_t \*addr, const struct bt\_le\_conn\_param \*param)

Automatically connect to remote device if it's in range.

[bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282)

bt\_conn\_state

**Definition** conn.h:340

[bt\_le\_oob\_set\_legacy\_flag](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892)

void bt\_le\_oob\_set\_legacy\_flag(bool enable)

Allow/disallow remote legacy OOB data to be used for pairing.

[bt\_conn\_le\_create\_synced](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1)

int bt\_conn\_le\_create\_synced(const struct bt\_le\_ext\_adv \*adv, const struct bt\_conn\_le\_create\_synced\_param \*synced\_param, const struct bt\_le\_conn\_param \*conn\_param, struct bt\_conn \*\*conn)

Create a connection to a synced device.

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

**Definition** conn.h:915

[bt\_conn\_le\_param\_update](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb)

int bt\_conn\_le\_param\_update(struct bt\_conn \*conn, const struct bt\_le\_conn\_param \*param)

Update the connection parameters.

[bt\_conn\_auth\_passkey\_confirm](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995)

int bt\_conn\_auth\_passkey\_confirm(struct bt\_conn \*conn)

Reply if passkey was confirmed to match by user.

[bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20)

bt\_conn\_type

Connection Type.

**Definition** conn.h:200

[bt\_conn\_create\_sco](group__bt__conn.md#gac270287d6764dff1963f859a51a438e4)

struct bt\_conn \* bt\_conn\_create\_sco(const bt\_addr\_t \*peer)

Initiate an SCO connection to a remote device.

[bt\_le\_oob\_set\_sc\_data](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503)

int bt\_le\_oob\_set\_sc\_data(struct bt\_conn \*conn, const struct bt\_le\_oob\_sc\_data \*oobd\_local, const struct bt\_le\_oob\_sc\_data \*oobd\_remote)

Set OOB data during LE Secure Connections (SC) pairing procedure.

[bt\_conn\_auth\_info\_cb\_register](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f)

int bt\_conn\_auth\_info\_cb\_register(struct bt\_conn\_auth\_info\_cb \*cb)

Register authentication information callbacks.

[bt\_conn\_auth\_info\_cb\_unregister](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37)

int bt\_conn\_auth\_info\_cb\_unregister(struct bt\_conn\_auth\_info\_cb \*cb)

Unregister authentication information callbacks.

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

**Definition** conn.h:352

[bt\_conn\_create\_br](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9)

struct bt\_conn \* bt\_conn\_create\_br(const bt\_addr\_t \*peer, const struct bt\_br\_conn\_param \*param)

Initiate an BR/EDR connection to a remote device.

[bt\_conn\_enc\_key\_size](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e)

uint8\_t bt\_conn\_enc\_key\_size(const struct bt\_conn \*conn)

Get encryption key size.

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

[BT\_SECURITY\_FLAG\_OOB](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198)

@ BT\_SECURITY\_FLAG\_OOB

Paired with Out of Band method.

**Definition** conn.h:374

[BT\_SECURITY\_FLAG\_SC](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6)

@ BT\_SECURITY\_FLAG\_SC

Paired with Secure Connections.

**Definition** conn.h:372

[BT\_CONN\_LE\_OPT\_NONE](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)

@ BT\_CONN\_LE\_OPT\_NONE

Convenience value when no options are specified.

**Definition** conn.h:667

[BT\_CONN\_LE\_OPT\_NO\_1M](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9)

@ BT\_CONN\_LE\_OPT\_NO\_1M

Disable LE 1M PHY.

**Definition** conn.h:681

[BT\_CONN\_LE\_OPT\_CODED](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b)

@ BT\_CONN\_LE\_OPT\_CODED

Enable LE Coded PHY.

**Definition** conn.h:673

[BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529)

@ BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED

**Definition** conn.h:526

[BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1)

@ BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED

**Definition** conn.h:525

[BT\_CONN\_AUTH\_KEYPRESS\_CLEARED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da)

@ BT\_CONN\_AUTH\_KEYPRESS\_CLEARED

**Definition** conn.h:527

[BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6)

@ BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED

**Definition** conn.h:524

[BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8)

@ BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED

**Definition** conn.h:528

[BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE

Convenience macro for when no PHY is set.

**Definition** conn.h:458

[BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2

LE Coded PHY using S=2 coding.

**Definition** conn.h:466

[BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8

LE Coded PHY using S=8 coding.

**Definition** conn.h:464

[BT\_CONN\_LE\_TX\_POWER\_PHY\_1M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_1M

LE 1M PHY.

**Definition** conn.h:460

[BT\_CONN\_LE\_TX\_POWER\_PHY\_2M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800)

@ BT\_CONN\_LE\_TX\_POWER\_PHY\_2M

LE 2M PHY.

**Definition** conn.h:462

[BT\_CONN\_STATE\_CONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd)

@ BT\_CONN\_STATE\_CONNECTING

Channel in connecting state.

**Definition** conn.h:344

[BT\_CONN\_STATE\_CONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f)

@ BT\_CONN\_STATE\_CONNECTED

Channel connected and ready for upper layer traffic on it.

**Definition** conn.h:346

[BT\_CONN\_STATE\_DISCONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587)

@ BT\_CONN\_STATE\_DISCONNECTED

Channel disconnected.

**Definition** conn.h:342

[BT\_CONN\_STATE\_DISCONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f)

@ BT\_CONN\_STATE\_DISCONNECTING

Channel in disconnecting state.

**Definition** conn.h:348

[BT\_CONN\_ROLE\_PERIPHERAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0)

@ BT\_CONN\_ROLE\_PERIPHERAL

**Definition** conn.h:337

[BT\_CONN\_ROLE\_CENTRAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)

@ BT\_CONN\_ROLE\_CENTRAL

**Definition** conn.h:336

[BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7)

@ BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE

OOB data is not available.

**Definition** conn.h:926

[BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae)

@ BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT

The requested security level could not be reached.

**Definition** conn.h:929

[BT\_SECURITY\_ERR\_KEY\_REJECTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216)

@ BT\_SECURITY\_ERR\_KEY\_REJECTED

Distributed Key Rejected.

**Definition** conn.h:941

[BT\_SECURITY\_ERR\_UNSPECIFIED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)

@ BT\_SECURITY\_ERR\_UNSPECIFIED

Pairing failed but the exact reason could not be specified.

**Definition** conn.h:944

[BT\_SECURITY\_ERR\_INVALID\_PARAM](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5)

@ BT\_SECURITY\_ERR\_INVALID\_PARAM

Invalid parameters.

**Definition** conn.h:938

[BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6)

@ BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED

Pairing is not supported.

**Definition** conn.h:932

[BT\_SECURITY\_ERR\_AUTH\_FAIL](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7)

@ BT\_SECURITY\_ERR\_AUTH\_FAIL

Authentication failed.

**Definition** conn.h:920

[BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171)

@ BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING

PIN or encryption key is missing.

**Definition** conn.h:923

[BT\_SECURITY\_ERR\_SUCCESS](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05)

@ BT\_SECURITY\_ERR\_SUCCESS

Security procedure successful.

**Definition** conn.h:917

[BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f)

@ BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED

Pairing is not allowed.

**Definition** conn.h:935

[BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)

@ BT\_CONN\_TYPE\_LE

LE Connection Type.

**Definition** conn.h:202

[BT\_CONN\_TYPE\_ALL](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)

@ BT\_CONN\_TYPE\_ALL

All Connection Type.

**Definition** conn.h:210

[BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)

@ BT\_CONN\_TYPE\_BR

BR/EDR Connection Type.

**Definition** conn.h:204

[BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)

@ BT\_CONN\_TYPE\_ISO

ISO Connection Type.

**Definition** conn.h:208

[BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953)

@ BT\_CONN\_TYPE\_SCO

SCO Connection Type.

**Definition** conn.h:206

[BT\_SECURITY\_L4](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81)

@ BT\_SECURITY\_L4

Level 4: Authenticated Secure Connections and 128-bit key.

**Definition** conn.h:362

[BT\_SECURITY\_L0](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e)

@ BT\_SECURITY\_L0

Level 0: Only for BR/EDR special cases, like SDP.

**Definition** conn.h:354

[BT\_SECURITY\_L3](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631)

@ BT\_SECURITY\_L3

Level 3: Encryption and authentication (MITM).

**Definition** conn.h:360

[BT\_SECURITY\_FORCE\_PAIR](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae)

@ BT\_SECURITY\_FORCE\_PAIR

Bit to force new pairing procedure, bit-wise OR with requested security level.

**Definition** conn.h:366

[BT\_SECURITY\_L1](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b)

@ BT\_SECURITY\_L1

Level 1: No encryption and no authentication.

**Definition** conn.h:356

[BT\_SECURITY\_L2](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a)

@ BT\_SECURITY\_L2

Level 2: Encryption and no authentication (no MITM).

**Definition** conn.h:358

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[hci\_types.h](hci__types_8h.md)

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

**Definition** conn.h:1734

[bt\_br\_conn\_param::allow\_role\_switch](structbt__br__conn__param.md#a95454a74932a14b4137c3fe82821be49)

bool allow\_role\_switch

**Definition** conn.h:1735

[bt\_conn\_auth\_cb](structbt__conn__auth__cb.md)

Authenticated pairing callback structure.

**Definition** conn.h:1379

[bt\_conn\_auth\_cb::passkey\_entry](structbt__conn__auth__cb.md#a10f9d22c89c95a6f3ffe0016f92445c0)

void(\* passkey\_entry)(struct bt\_conn \*conn)

Request the user to enter a passkey.

**Definition** conn.h:1476

[bt\_conn\_auth\_cb::passkey\_display](structbt__conn__auth__cb.md#a14074ca97fad6af4c58c43a00c503104)

void(\* passkey\_display)(struct bt\_conn \*conn, unsigned int passkey)

Display a passkey to the user.

**Definition** conn.h:1430

[bt\_conn\_auth\_cb::passkey\_confirm](structbt__conn__auth__cb.md#a2bb6c10666d111f675fd6de5ff51410a)

void(\* passkey\_confirm)(struct bt\_conn \*conn, unsigned int passkey)

Request the user to confirm a passkey.

**Definition** conn.h:1499

[bt\_conn\_auth\_cb::pairing\_accept](structbt__conn__auth__cb.md#a92391a172e158a42966f410d732424a7)

enum bt\_security\_err(\* pairing\_accept)(struct bt\_conn \*conn, const struct bt\_conn\_pairing\_feat \*const feat)

Query to proceed incoming pairing or not.

**Definition** conn.h:1408

[bt\_conn\_auth\_cb::pincode\_entry](structbt__conn__auth__cb.md#ab6df1b1505dc22dd8dae0e946546c8bb)

void(\* pincode\_entry)(struct bt\_conn \*conn, bool highsec)

Request the user to enter a passkey.

**Definition** conn.h:1573

[bt\_conn\_auth\_cb::oob\_data\_request](structbt__conn__auth__cb.md#aec9f6256607ea2cd1ce1b4cdb3052b42)

void(\* oob\_data\_request)(struct bt\_conn \*conn, struct bt\_conn\_oob\_info \*info)

Request the user to provide Out of Band (OOB) data.

**Definition** conn.h:1517

[bt\_conn\_auth\_cb::pairing\_confirm](structbt__conn__auth__cb.md#af4f7d3ee570b3472ee79b014be01f76e)

void(\* pairing\_confirm)(struct bt\_conn \*conn)

Request confirmation for an incoming pairing.

**Definition** conn.h:1552

[bt\_conn\_auth\_cb::cancel](structbt__conn__auth__cb.md#af6eb01c252ba3e32ff8bf583aa6ca0a4)

void(\* cancel)(struct bt\_conn \*conn)

Cancel the ongoing user request.

**Definition** conn.h:1532

[bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md)

Authenticated pairing information callback structure.

**Definition** conn.h:1578

[bt\_conn\_auth\_info\_cb::pairing\_failed](structbt__conn__auth__info__cb.md#ae7228bb82889eacebf67e1d4b3b23375)

void(\* pairing\_failed)(struct bt\_conn \*conn, enum bt\_security\_err reason)

notify that pairing process has failed.

**Definition** conn.h:1595

[bt\_conn\_auth\_info\_cb::pairing\_complete](structbt__conn__auth__info__cb.md#aea737700f2760de1ed26a721b5e860d2)

void(\* pairing\_complete)(struct bt\_conn \*conn, bool bonded)

notify that pairing procedure was complete.

**Definition** conn.h:1588

[bt\_conn\_auth\_info\_cb::bond\_deleted](structbt__conn__auth__info__cb.md#af20b0d7fc5fd8399ad9368b3ef7067f8)

void(\* bond\_deleted)(uint8\_t id, const bt\_addr\_le\_t \*peer)

Notify that bond has been deleted.

**Definition** conn.h:1606

[bt\_conn\_auth\_info\_cb::node](structbt__conn__auth__info__cb.md#afde62f2cdfb40b4154208f3c1c3dadc1)

sys\_snode\_t node

Internally used field for list handling.

**Definition** conn.h:1609

[bt\_conn\_br\_info](structbt__conn__br__info.md)

BR/EDR Connection Info Structure.

**Definition** conn.h:331

[bt\_conn\_br\_info::dst](structbt__conn__br__info.md#aeef49f711872ccfec5dd558c4552b71e)

const bt\_addr\_t \* dst

Destination (Remote) BR/EDR address.

**Definition** conn.h:332

[bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md)

BR/EDR Connection Remote Info structure.

**Definition** conn.h:420

[bt\_conn\_br\_remote\_info::num\_pages](structbt__conn__br__remote__info.md#a798c179c803e709182a1b0c3594f4a0a)

uint8\_t num\_pages

Number of pages in the remote feature set.

**Definition** conn.h:426

[bt\_conn\_br\_remote\_info::features](structbt__conn__br__remote__info.md#afa19f7db400bb0de234e8cda61f3deaf)

const uint8\_t \* features

Remote feature set (pages of bitmasks).

**Definition** conn.h:423

[bt\_conn\_cb](structbt__conn__cb.md)

Connection callback structure.

**Definition** conn.h:957

[bt\_conn\_cb::le\_param\_updated](structbt__conn__cb.md#a01582ed3e3801e10c665534eaa991454)

void(\* le\_param\_updated)(struct bt\_conn \*conn, uint16\_t interval, uint16\_t latency, uint16\_t timeout)

The parameters for an LE connection have been updated.

**Definition** conn.h:1054

[bt\_conn\_cb::le\_data\_len\_updated](structbt__conn__cb.md#a1142d1861cc0b0058f68ecf537d0cec3)

void(\* le\_data\_len\_updated)(struct bt\_conn \*conn, struct bt\_conn\_le\_data\_len\_info \*info)

The data length parameters of the connection has changed.

**Definition** conn.h:1126

[bt\_conn\_cb::recycled](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b)

void(\* recycled)(void)

A connection object has been returned to the pool.

**Definition** conn.h:1015

[bt\_conn\_cb::le\_param\_req](structbt__conn__cb.md#a2c52c2e2798062708c373fae9610fadd)

bool(\* le\_param\_req)(struct bt\_conn \*conn, struct bt\_le\_conn\_param \*param)

LE connection parameter update request.

**Definition** conn.h:1041

[bt\_conn\_cb::disconnected](structbt__conn__cb.md#a8b8983b5b5b05c9e2dae242485b6c914)

void(\* disconnected)(struct bt\_conn \*conn, uint8\_t reason)

A connection has been disconnected.

**Definition** conn.h:1001

[bt\_conn\_cb::connected](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69)

void(\* connected)(struct bt\_conn \*conn, uint8\_t err)

A new connection has been established.

**Definition** conn.h:982

[bt\_conn\_cb::le\_phy\_updated](structbt__conn__cb.md#ae02a23d823954a747f8f474fb19276d7)

void(\* le\_phy\_updated)(struct bt\_conn \*conn, struct bt\_conn\_le\_phy\_info \*param)

The PHY of the connection has changed.

**Definition** conn.h:1113

[bt\_conn\_cb::security\_changed](structbt__conn__cb.md#ae454d5bc2664e90ba2b1e0c867db374e)

void(\* security\_changed)(struct bt\_conn \*conn, bt\_security\_t level, enum bt\_security\_err err)

The security level of a connection has changed.

**Definition** conn.h:1087

[bt\_conn\_cb::identity\_resolved](structbt__conn__cb.md#aea9b62ab1a1469be97a207a8e07d2f14)

void(\* identity\_resolved)(struct bt\_conn \*conn, const bt\_addr\_le\_t \*rpa, const bt\_addr\_le\_t \*identity)

Remote Identity Address has been resolved.

**Definition** conn.h:1066

[bt\_conn\_cb::remote\_info\_available](structbt__conn__cb.md#af726f004c06b86f770ece263ed6c9ca4)

void(\* remote\_info\_available)(struct bt\_conn \*conn, struct bt\_conn\_remote\_info \*remote\_info)

Remote information procedures has completed.

**Definition** conn.h:1100

[bt\_conn\_info](structbt__conn__info.md)

Connection Info Structure.

**Definition** conn.h:392

[bt\_conn\_info::id](structbt__conn__info.md#a3a4e24519b5d3ba547423e53c4d92a5c)

uint8\_t id

Which local identity the connection was created with.

**Definition** conn.h:398

[bt\_conn\_info::le](structbt__conn__info.md#a6b536e7732dcf7b77a7bc05116dca548)

struct bt\_conn\_le\_info le

LE Connection specific Info.

**Definition** conn.h:402

[bt\_conn\_info::type](structbt__conn__info.md#a7995e1291be494b5bdf860eceea0cad1)

enum bt\_conn\_type type

Connection Type.

**Definition** conn.h:394

[bt\_conn\_info::br](structbt__conn__info.md#a799e59d3a85625799a32ac3f0b3d67d1)

struct bt\_conn\_br\_info br

BR/EDR Connection specific Info.

**Definition** conn.h:404

[bt\_conn\_info::role](structbt__conn__info.md#a8237b8c1bb9a97a174d04cbe13dca7c7)

uint8\_t role

Connection Role.

**Definition** conn.h:396

[bt\_conn\_info::security](structbt__conn__info.md#ae4405f1b4f3fe2ff6253453964860931)

struct bt\_security\_info security

Security specific info.

**Definition** conn.h:409

[bt\_conn\_info::state](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc)

enum bt\_conn\_state state

Connection state.

**Definition** conn.h:407

[bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md)

**Definition** conn.h:684

[bt\_conn\_le\_create\_param::interval\_coded](structbt__conn__le__create__param.md#a2bc978ac97435fe5f87c6e01692f2910)

uint16\_t interval\_coded

Scan interval LE Coded PHY (N \* 0.625 MS).

**Definition** conn.h:699

[bt\_conn\_le\_create\_param::window](structbt__conn__le__create__param.md#a339b99f65c5029ada6cdf453ab1f258e)

uint16\_t window

Scan window (N \* 0.625 ms).

**Definition** conn.h:693

[bt\_conn\_le\_create\_param::options](structbt__conn__le__create__param.md#a4b1e26c0976d9c900b831c886c77b055)

uint32\_t options

Bit-field of create connection options.

**Definition** conn.h:687

[bt\_conn\_le\_create\_param::timeout](structbt__conn__le__create__param.md#a59f05bfb9468779d02f8d0beeb7a35c1)

uint16\_t timeout

Connection initiation timeout (N \* 10 MS).

**Definition** conn.h:714

[bt\_conn\_le\_create\_param::interval](structbt__conn__le__create__param.md#a5cfae677f924534dc5bc7b38c457a7af)

uint16\_t interval

Scan interval (N \* 0.625 ms).

**Definition** conn.h:690

[bt\_conn\_le\_create\_param::window\_coded](structbt__conn__le__create__param.md#ae62491837d35d95e32016b793edf8c96)

uint16\_t window\_coded

Scan window LE Coded PHY (N \* 0.625 MS).

**Definition** conn.h:705

[bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md)

**Definition** conn.h:785

[bt\_conn\_le\_create\_synced\_param::peer](structbt__conn__le__create__synced__param.md#ac5872dda4042e3ba6c161dce60784b70)

const bt\_addr\_le\_t \* peer

Remote address.

**Definition** conn.h:792

[bt\_conn\_le\_create\_synced\_param::subevent](structbt__conn__le__create__synced__param.md#ac7b4e4144aaf914bdef1dc305b5e297f)

uint8\_t subevent

The subevent where the connection will be initiated.

**Definition** conn.h:795

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

**Definition** conn.h:290

[bt\_conn\_le\_info::dst](structbt__conn__le__info.md#a1f78e1c0ed3482ce6eec9ce6eeda4769)

const bt\_addr\_le\_t \* dst

Destination (Remote) Identity Address or remote Resolvable Private Address (RPA) before identity has ...

**Definition** conn.h:296

[bt\_conn\_le\_info::phy](structbt__conn__le__info.md#a215d39c6cd7da1ac033529b5541cbfc1)

const struct bt\_conn\_le\_phy\_info \* phy

**Definition** conn.h:306

[bt\_conn\_le\_info::remote](structbt__conn__le__info.md#a236d1c97c735c7cfaead0b1a3672d512)

const bt\_addr\_le\_t \* remote

Remote device address used during connection setup.

**Definition** conn.h:300

[bt\_conn\_le\_info::local](structbt__conn__le__info.md#a3be5df0deb0af08f84843eb3c6a5e5ae)

const bt\_addr\_le\_t \* local

Local device address used during connection setup.

**Definition** conn.h:298

[bt\_conn\_le\_info::src](structbt__conn__le__info.md#a5f1eacec82f31182460d6d5359a8b295)

const bt\_addr\_le\_t \* src

Source (Local) Identity Address.

**Definition** conn.h:292

[bt\_conn\_le\_info::interval](structbt__conn__le__info.md#a95a1f635e53f16d5839cdd58f4bda962)

uint16\_t interval

Connection interval.

**Definition** conn.h:301

[bt\_conn\_le\_info::latency](structbt__conn__le__info.md#acd83835fe5ec0878fd653b87cb570a49)

uint16\_t latency

Connection peripheral latency.

**Definition** conn.h:302

[bt\_conn\_le\_info::data\_len](structbt__conn__le__info.md#ae309f390c8d7b33a4de55791af235ab0)

const struct bt\_conn\_le\_data\_len\_info \* data\_len

**Definition** conn.h:311

[bt\_conn\_le\_info::timeout](structbt__conn__le__info.md#afb4dc594d063fbbad2bcd4acf047f716)

uint16\_t timeout

Connection supervision timeout.

**Definition** conn.h:303

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

**Definition** conn.h:413

[bt\_conn\_le\_remote\_info::features](structbt__conn__le__remote__info.md#a4ff434f6c501dc60db5c4b776be46b3b)

const uint8\_t \* features

Remote LE feature set (bitmask).

**Definition** conn.h:416

[bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md)

LE Transmit Power Reporting Structure.

**Definition** conn.h:484

[bt\_conn\_le\_tx\_power\_report::phy](structbt__conn__le__tx__power__report.md#a5b1f67537fbe945f2f258b47082723b4)

enum bt\_conn\_le\_tx\_power\_phy phy

Phy of Transmit power reporting.

**Definition** conn.h:492

[bt\_conn\_le\_tx\_power\_report::delta](structbt__conn__le__tx__power__report.md#a7c681c7b9f77d994b2de1febea7c5dc9)

int8\_t delta

Change in transmit power level.

**Definition** conn.h:515

[bt\_conn\_le\_tx\_power\_report::reason](structbt__conn__le__tx__power__report.md#aa5606925229784af8ae90542432cf200)

uint8\_t reason

Reason for Transmit power reporting, as documented in Core Spec.

**Definition** conn.h:489

[bt\_conn\_le\_tx\_power\_report::tx\_power\_level](structbt__conn__le__tx__power__report.md#ace830ddb7ae662c9759babed87f1b6f3)

int8\_t tx\_power\_level

Transmit power level.

**Definition** conn.h:502

[bt\_conn\_le\_tx\_power\_report::tx\_power\_level\_flag](structbt__conn__le__tx__power__report.md#ae7a4f77c6f7af1a459896d25cf661eb8)

uint8\_t tx\_power\_level\_flag

Bit 0: Transmit power level is at minimum level.

**Definition** conn.h:507

[bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md)

LE Transmit Power Level Structure.

**Definition** conn.h:470

[bt\_conn\_le\_tx\_power::max\_level](structbt__conn__le__tx__power.md#a1674247c511906fa6f0193653ed0b71a)

int8\_t max\_level

Output: maximum transmit power level.

**Definition** conn.h:479

[bt\_conn\_le\_tx\_power::current\_level](structbt__conn__le__tx__power.md#a6d2e5a5215fa5d60630e74928a67fc04)

int8\_t current\_level

Output: current transmit power level.

**Definition** conn.h:476

[bt\_conn\_le\_tx\_power::phy](structbt__conn__le__tx__power.md#a8702c4ff5082b8f90decdfabfb8253fe)

uint8\_t phy

Input: 1M, 2M, Coded S2 or Coded S8.

**Definition** conn.h:473

[bt\_conn\_oob\_info](structbt__conn__oob__info.md)

Info Structure for OOB pairing.

**Definition** conn.h:1315

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_LE\_LEGACY](structbt__conn__oob__info.md#a433c4a8e1efcb663ad369d018d999b0ea4c33ea839306256a198c29ea783c659b)

@ BT\_CONN\_OOB\_LE\_LEGACY

LE legacy pairing.

**Definition** conn.h:1319

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_LE\_SC](structbt__conn__oob__info.md#a433c4a8e1efcb663ad369d018d999b0eacd02773beb42df3fb6cbaa2fa2abda1e)

@ BT\_CONN\_OOB\_LE\_SC

LE SC pairing.

**Definition** conn.h:1322

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_NO\_DATA](structbt__conn__oob__info.md#a71bf295d82fbc647b3816bfba6fa0ae7)

@ BT\_CONN\_OOB\_NO\_DATA

No OOB data requested.

**Definition** conn.h:1340

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_LOCAL\_ONLY](structbt__conn__oob__info.md#a72a749120c0a55a8dc9bd078921277e5)

@ BT\_CONN\_OOB\_LOCAL\_ONLY

Local OOB data requested.

**Definition** conn.h:1331

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_REMOTE\_ONLY](structbt__conn__oob__info.md#a7506049b35ac63602452b087d1d60fa2)

@ BT\_CONN\_OOB\_REMOTE\_ONLY

Remote OOB data requested.

**Definition** conn.h:1334

[bt\_conn\_oob\_info::BT\_CONN\_OOB\_BOTH\_PEERS](structbt__conn__oob__info.md#a99685ad84ac991e0540855cab5546ff8)

@ BT\_CONN\_OOB\_BOTH\_PEERS

Both local and remote OOB data requested.

**Definition** conn.h:1337

[bt\_conn\_oob\_info::oob\_config](structbt__conn__oob__info.md#aa20bbff037e6878216d7dd45938bca76)

enum bt\_conn\_oob\_info::@143143115062310336126347360141254141124170204126::@037057234300046321114030012274214022016020174371::@130100253371055064164065265224242172250032310014 oob\_config

OOB data configuration.

[bt\_conn\_oob\_info::type](structbt__conn__oob__info.md#aa793302d7c6c41a1b714ab219a1f14c9)

enum bt\_conn\_oob\_info::@071154206266322234333176322374364375362306302210 type

Type of OOB pairing method.

[bt\_conn\_oob\_info::lesc](structbt__conn__oob__info.md#ad721c4bbe51bec994362b35944579240)

struct bt\_conn\_oob\_info::@143143115062310336126347360141254141124170204126::@037057234300046321114030012274214022016020174371 lesc

LE Secure Connections OOB pairing parameters.

[bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md)

Pairing request and pairing response info structure.

**Definition** conn.h:1353

[bt\_conn\_pairing\_feat::resp\_key\_dist](structbt__conn__pairing__feat.md#a49f9f02e232e91f7f7a530aa7f226cba)

uint8\_t resp\_key\_dist

Responder Key Distribution/Generation, Core Spec.

**Definition** conn.h:1374

[bt\_conn\_pairing\_feat::io\_capability](structbt__conn__pairing__feat.md#a68005cea273c8e76c086502001b258b0)

uint8\_t io\_capability

IO Capability, Core Spec.

**Definition** conn.h:1355

[bt\_conn\_pairing\_feat::init\_key\_dist](structbt__conn__pairing__feat.md#a70adc125b875348ec8d273dea3b470d8)

uint8\_t init\_key\_dist

Initiator Key Distribution/Generation, Core Spec.

**Definition** conn.h:1369

[bt\_conn\_pairing\_feat::max\_enc\_key\_size](structbt__conn__pairing__feat.md#abe1d7d4bd9f4b551a2d0c69adc75bd40)

uint8\_t max\_enc\_key\_size

Maximum Encryption Key Size, Core Spec.

**Definition** conn.h:1364

[bt\_conn\_pairing\_feat::auth\_req](structbt__conn__pairing__feat.md#af9a977b1e0f9d4eada26a82d92eaec54)

uint8\_t auth\_req

AuthReq, Core Spec.

**Definition** conn.h:1361

[bt\_conn\_pairing\_feat::oob\_data\_flag](structbt__conn__pairing__feat.md#afb03164960db62b4b4cf70d3f0134099)

uint8\_t oob\_data\_flag

OOB data flag, Core Spec.

**Definition** conn.h:1358

[bt\_conn\_remote\_info](structbt__conn__remote__info.md)

Connection Remote Info Structure.

**Definition** conn.h:434

[bt\_conn\_remote\_info::version](structbt__conn__remote__info.md#a2664f6ed3bd22f9a011126daf5d81376)

uint8\_t version

Remote Link Layer version.

**Definition** conn.h:439

[bt\_conn\_remote\_info::subversion](structbt__conn__remote__info.md#a360979a15c958706157fc630fd55cbca)

uint16\_t subversion

Per-manufacturer unique revision.

**Definition** conn.h:445

[bt\_conn\_remote\_info::manufacturer](structbt__conn__remote__info.md#a47cc5a4b8888a0b8faaf6880c37418b8)

uint16\_t manufacturer

Remote manufacturer identifier.

**Definition** conn.h:442

[bt\_conn\_remote\_info::type](structbt__conn__remote__info.md#a8bb514196bde5df561dbf76b68060729)

uint8\_t type

Connection Type.

**Definition** conn.h:436

[bt\_conn\_remote\_info::br](structbt__conn__remote__info.md#ab73365f09cdb5ce870272546543bcfeb)

struct bt\_conn\_br\_remote\_info br

BR/EDR connection remote info.

**Definition** conn.h:452

[bt\_conn\_remote\_info::le](structbt__conn__remote__info.md#ae75530b09c6dea416630a4a19a1d64cc)

struct bt\_conn\_le\_remote\_info le

LE connection remote info.

**Definition** conn.h:449

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

**Definition** bluetooth.h:2331

[bt\_security\_info](structbt__security__info.md)

Security Info Structure.

**Definition** conn.h:378

[bt\_security\_info::enc\_key\_size](structbt__security__info.md#a6567ffb82b7fa8093cc57ef4662873ba)

uint8\_t enc\_key\_size

Encryption Key Size.

**Definition** conn.h:382

[bt\_security\_info::level](structbt__security__info.md#a7b18849fad25b3f2da6b8c85a56d86e1)

bt\_security\_t level

Security Level.

**Definition** conn.h:380

[bt\_security\_info::flags](structbt__security__info.md#a99cb4af08bfa1dab182821d956368526)

enum bt\_security\_flag flags

Flags.

**Definition** conn.h:384

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [conn.h](conn_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
