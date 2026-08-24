---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/log__frontend__stmesp__demux_8h_source.html
original_path: doxygen/html/log__frontend__stmesp__demux_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux.h

[Go to the documentation of this file.](log__frontend__stmesp__demux_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_FRONTEND\_STMESP\_DEMUX\_H\_

8#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_FRONTEND\_STMESP\_DEMUX\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/sys/mpsc\_packet.h](mpsc__packet_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

26

[ 28](group__log__frontend__stpesp__demux__apis.md#ga33581c39a57eca7f96fea9c29386a3e3)#define LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS 3

29

[ 31](group__log__frontend__stpesp__demux__apis.md#gaf2b7019394d33a082fec5ab2d2785257)#define LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS 3

32

[ 34](group__log__frontend__stpesp__demux__apis.md#gaeaf76dcb74836740115c9b6e3fece73b)#define LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS 16

35

[ 37](group__log__frontend__stpesp__demux__apis.md#ga56ad2b8067d56b9ccedefd57ad5aa0c2)#define LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS 10

38

[ 40](group__log__frontend__stpesp__demux__apis.md#ga8f23994b914214a2c83d2e9aa63f0cb5)#define LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_MAX BIT(LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS)

41

[ 43](group__log__frontend__stpesp__demux__apis.md#ga0f6129f8e757a6ef4b02779e57ff58f7)#define LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_LOG 0

44

[ 46](group__log__frontend__stpesp__demux__apis.md#ga7a428120f117a62a5d649f18111364c2)#define LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_TRACE\_POINT 1

47

[ 49](group__log__frontend__stpesp__demux__apis.md#ga67cbf7c7892b76c7347b229a0452bfa3)#define LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_HW\_EVENT 2

50

[ 52](structlog__frontend__stmesp__demux__log__header.md)struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) {

[ 54](structlog__frontend__stmesp__demux__log__header.md#acec1720948196deb1f09ab1ea443ecb9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [major](structlog__frontend__stmesp__demux__log__header.md#acec1720948196deb1f09ab1ea443ecb9) : [LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS](group__log__frontend__stpesp__demux__apis.md#ga33581c39a57eca7f96fea9c29386a3e3);

55

[ 57](structlog__frontend__stmesp__demux__log__header.md#a3b1474632ab446d8c9d590fb4bd8e420) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [level](structlog__frontend__stmesp__demux__log__header.md#a3b1474632ab446d8c9d590fb4bd8e420) : [LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS](group__log__frontend__stpesp__demux__apis.md#gaf2b7019394d33a082fec5ab2d2785257);

58

[ 60](structlog__frontend__stmesp__demux__log__header.md#a138b653d76c50c0454210b7a1d7ec60b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [total\_len](structlog__frontend__stmesp__demux__log__header.md#a138b653d76c50c0454210b7a1d7ec60b) : [LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS](group__log__frontend__stpesp__demux__apis.md#gaeaf76dcb74836740115c9b6e3fece73b);

61

[ 63](structlog__frontend__stmesp__demux__log__header.md#a0a378b7740a3def454bf34fe54927aa1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [package\_len](structlog__frontend__stmesp__demux__log__header.md#a0a378b7740a3def454bf34fe54927aa1) : [LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS](group__log__frontend__stpesp__demux__apis.md#ga56ad2b8067d56b9ccedefd57ad5aa0c2);

64};

65

[ 67](unionlog__frontend__stmesp__demux__header.md)union [log\_frontend\_stmesp\_demux\_header](unionlog__frontend__stmesp__demux__header.md) {

[ 69](unionlog__frontend__stmesp__demux__header.md#ae94bab609a4f5c51eef7886db712420d) struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) [log](unionlog__frontend__stmesp__demux__header.md#ae94bab609a4f5c51eef7886db712420d);

70

[ 72](unionlog__frontend__stmesp__demux__header.md#ae868e8f2e8b0623781d3f9377490c72a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw](unionlog__frontend__stmesp__demux__header.md#ae868e8f2e8b0623781d3f9377490c72a);

73};

74

[ 76](structlog__frontend__stmesp__demux__packet__generic.md)struct [log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md) {

[ 78](structlog__frontend__stmesp__demux__packet__generic.md#ac202cf6bc5bc8699a858e10de2c0c492) [MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__packet__generic.md#ac202cf6bc5bc8699a858e10de2c0c492);

79

[ 81](structlog__frontend__stmesp__demux__packet__generic.md#a7a86c5de5e5b33830d963add116c1feb) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [type](structlog__frontend__stmesp__demux__packet__generic.md#a7a86c5de5e5b33830d963add116c1feb): 2;

82

[ 84](structlog__frontend__stmesp__demux__packet__generic.md#a42d6b5192e0f9ba897a2986d645c6a6c) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [content\_invalid](structlog__frontend__stmesp__demux__packet__generic.md#a42d6b5192e0f9ba897a2986d645c6a6c): 1;

85};

86

[ 88](structlog__frontend__stmesp__demux__log.md)struct [log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md) {

[ 90](structlog__frontend__stmesp__demux__log.md#ad25f0378c2c3ba3d153a58a843704033) [MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__log.md#ad25f0378c2c3ba3d153a58a843704033);

91

[ 93](structlog__frontend__stmesp__demux__log.md#adb1b61bdca3a97df2c8ba2b34fc2ebff) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [type](structlog__frontend__stmesp__demux__log.md#adb1b61bdca3a97df2c8ba2b34fc2ebff): 2;

94

[ 96](structlog__frontend__stmesp__demux__log.md#a84cf9f64d96e87cfd2bb9d859fed3886) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [content\_invalid](structlog__frontend__stmesp__demux__log.md#a84cf9f64d96e87cfd2bb9d859fed3886): 1;

97

[ 99](structlog__frontend__stmesp__demux__log.md#af2b9820efce6f58d655b08a306c8d8d1) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timestamp](structlog__frontend__stmesp__demux__log.md#af2b9820efce6f58d655b08a306c8d8d1): 59;

100

[ 102](structlog__frontend__stmesp__demux__log.md#aa5b7175e05dbdcc41d75c5412ce30b15) struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) [hdr](structlog__frontend__stmesp__demux__log.md#aa5b7175e05dbdcc41d75c5412ce30b15);

103

[ 105](structlog__frontend__stmesp__demux__log.md#ab063e3ed4d81cbdb4ec417508c55bd13) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [padding](structlog__frontend__stmesp__demux__log.md#ab063e3ed4d81cbdb4ec417508c55bd13);

106

[ 108](structlog__frontend__stmesp__demux__log.md#ae8c62ffd8a11fbcebce29ed934f52597) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structlog__frontend__stmesp__demux__log.md#ae8c62ffd8a11fbcebce29ed934f52597)[];

109};

110

[ 112](structlog__frontend__stmesp__demux__trace__point.md)struct [log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md) {

[ 114](structlog__frontend__stmesp__demux__trace__point.md#ae3e776e4a470ccb3abd8f6a73ce7b21b) [MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__trace__point.md#ae3e776e4a470ccb3abd8f6a73ce7b21b);

115

[ 117](structlog__frontend__stmesp__demux__trace__point.md#ab250b6782df720df3d1cdb37ab25a024) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [type](structlog__frontend__stmesp__demux__trace__point.md#ab250b6782df720df3d1cdb37ab25a024): 2;

118

[ 120](structlog__frontend__stmesp__demux__trace__point.md#a300adc8bd0882810ae4a5759a76857ce) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [content\_invalid](structlog__frontend__stmesp__demux__trace__point.md#a300adc8bd0882810ae4a5759a76857ce): 1;

121

[ 123](structlog__frontend__stmesp__demux__trace__point.md#a0bdc2a3e1afb5748e08e68617f2ccbb6) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [has\_data](structlog__frontend__stmesp__demux__trace__point.md#a0bdc2a3e1afb5748e08e68617f2ccbb6): 1;

124

[ 126](structlog__frontend__stmesp__demux__trace__point.md#a6e1892f15fa3149f8161a1792420ba73) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timestamp](structlog__frontend__stmesp__demux__trace__point.md#a6e1892f15fa3149f8161a1792420ba73): 54;

127

[ 129](structlog__frontend__stmesp__demux__trace__point.md#acfa056769b9ba00b945e1ff7d1e4cdb9) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [major](structlog__frontend__stmesp__demux__trace__point.md#acfa056769b9ba00b945e1ff7d1e4cdb9): 4;

130

[ 132](structlog__frontend__stmesp__demux__trace__point.md#a0ca97d4ffd9bae1d640b8f99c8bd5ace) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [source\_id](structlog__frontend__stmesp__demux__trace__point.md#a0ca97d4ffd9bae1d640b8f99c8bd5ace);

133

[ 135](structlog__frontend__stmesp__demux__trace__point.md#aeb86bfae01245a4778d08ac9c1ee138a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structlog__frontend__stmesp__demux__trace__point.md#aeb86bfae01245a4778d08ac9c1ee138a);

136

[ 138](structlog__frontend__stmesp__demux__trace__point.md#ada954ed2971c2fc720a1d1f2634c0e2a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structlog__frontend__stmesp__demux__trace__point.md#ada954ed2971c2fc720a1d1f2634c0e2a);

139};

140

[ 142](structlog__frontend__stmesp__demux__hw__event.md)struct [log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md) {

[ 144](structlog__frontend__stmesp__demux__hw__event.md#a6a060e7fbda81c47eaa8088f3e45052a) [MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__hw__event.md#a6a060e7fbda81c47eaa8088f3e45052a);

145

[ 147](structlog__frontend__stmesp__demux__hw__event.md#a5a781f1b681ef2499bf9ba2635261d4f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [type](structlog__frontend__stmesp__demux__hw__event.md#a5a781f1b681ef2499bf9ba2635261d4f): 2;

148

[ 150](structlog__frontend__stmesp__demux__hw__event.md#ae6872dcd7e11eeb431e3d990ccdad243) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [content\_invalid](structlog__frontend__stmesp__demux__hw__event.md#ae6872dcd7e11eeb431e3d990ccdad243): 1;

151

[ 153](structlog__frontend__stmesp__demux__hw__event.md#a0766f3aa6163ea1a197d674eac00305b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timestamp](structlog__frontend__stmesp__demux__hw__event.md#a0766f3aa6163ea1a197d674eac00305b): 59;

154

[ 156](structlog__frontend__stmesp__demux__hw__event.md#a090039b38d646812a292510476d16644) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt](structlog__frontend__stmesp__demux__hw__event.md#a090039b38d646812a292510476d16644);

157};

158

[ 160](unionlog__frontend__stmesp__demux__packet.md)union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) {

[ 162](unionlog__frontend__stmesp__demux__packet.md#ac712f4dc2ca645e2ba6f6c638b41bf10) const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*[rgeneric](unionlog__frontend__stmesp__demux__packet.md#ac712f4dc2ca645e2ba6f6c638b41bf10);

163

[ 165](unionlog__frontend__stmesp__demux__packet.md#a71d8ecb5afa1ac2cd64aaf21916119c5) union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*generic;

166

[ 168](unionlog__frontend__stmesp__demux__packet.md#ac75deeb2f665aeb5dcfd94090aa1a1cf) struct [log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md) \*[log](unionlog__frontend__stmesp__demux__packet.md#ac75deeb2f665aeb5dcfd94090aa1a1cf);

169

[ 171](unionlog__frontend__stmesp__demux__packet.md#aa68b1022f97c8806ee430a541190fc82) struct [log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md) \*[trace\_point](unionlog__frontend__stmesp__demux__packet.md#aa68b1022f97c8806ee430a541190fc82);

172

[ 174](unionlog__frontend__stmesp__demux__packet.md#ae764f7a3b04e66af22c52aa1d52a441e) struct [log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md) \*[hw\_event](unionlog__frontend__stmesp__demux__packet.md#ae764f7a3b04e66af22c52aa1d52a441e);

175

[ 177](unionlog__frontend__stmesp__demux__packet.md#a30d3cfc6071bebc1614f2f67c8a950c7) struct [log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md) \*[generic\_packet](unionlog__frontend__stmesp__demux__packet.md#a30d3cfc6071bebc1614f2f67c8a950c7);

178};

179

[ 181](structlog__frontend__stmesp__demux__config.md)struct [log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md) {

[ 183](structlog__frontend__stmesp__demux__config.md#ada2f243b112324e99a53b831211cabce) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[m\_ids](structlog__frontend__stmesp__demux__config.md#ada2f243b112324e99a53b831211cabce);

184

[ 186](structlog__frontend__stmesp__demux__config.md#ad248eabec1eee58f5ef689004d5c7017) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [m\_ids\_cnt](structlog__frontend__stmesp__demux__config.md#ad248eabec1eee58f5ef689004d5c7017);

187

[ 189](structlog__frontend__stmesp__demux__config.md#aca85e1b671127e8803423f22b2d45a33) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[source\_id\_buf](structlog__frontend__stmesp__demux__config.md#aca85e1b671127e8803423f22b2d45a33);

190

[ 192](structlog__frontend__stmesp__demux__config.md#a643b5bd780342bf1944e5a63274aa305) size\_t [source\_id\_buf\_len](structlog__frontend__stmesp__demux__config.md#a643b5bd780342bf1944e5a63274aa305);

193};

194

[ 202](group__log__frontend__stpesp__demux__apis.md#ga97f9ac1d7b459e9d3d715b5367e29a31)int [log\_frontend\_stmesp\_demux\_init](group__log__frontend__stpesp__demux__apis.md#ga97f9ac1d7b459e9d3d715b5367e29a31)(const struct [log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md) \*config);

203

[ 208](group__log__frontend__stpesp__demux__apis.md#ga8be4ca332fa9145fad72a6b45245a9ff)void [log\_frontend\_stmesp\_demux\_major](group__log__frontend__stpesp__demux__apis.md#ga8be4ca332fa9145fad72a6b45245a9ff)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

209

[ 214](group__log__frontend__stpesp__demux__apis.md#ga4f86c0cfb38fa05389462045019a6650)void [log\_frontend\_stmesp\_demux\_channel](group__log__frontend__stpesp__demux__apis.md#ga4f86c0cfb38fa05389462045019a6650)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

215

[ 221](group__log__frontend__stpesp__demux__apis.md#gaed29a1869e710cd95c19c48c67a36aa8)int [log\_frontend\_stmesp\_demux\_packet\_start](group__log__frontend__stpesp__demux__apis.md#gaed29a1869e710cd95c19c48c67a36aa8)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts);

222

[ 228](group__log__frontend__stpesp__demux__apis.md#ga6a25dd796a8759009e14b5770f7653a9)int [log\_frontend\_stmesp\_demux\_log0](group__log__frontend__stpesp__demux__apis.md#ga6a25dd796a8759009e14b5770f7653a9)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts);

229

[ 234](group__log__frontend__stpesp__demux__apis.md#gae5925a640c401cc09dd744945eafd51c)void [log\_frontend\_stmesp\_demux\_source\_id](group__log__frontend__stpesp__demux__apis.md#gae5925a640c401cc09dd744945eafd51c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id);

235

[ 243](group__log__frontend__stpesp__demux__apis.md#ga184cc4d266a010aa094a45aba0fad638)void [log\_frontend\_stmesp\_demux\_timestamp](group__log__frontend__stpesp__demux__apis.md#ga184cc4d266a010aa094a45aba0fad638)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ts);

244

[ 250](group__log__frontend__stpesp__demux__apis.md#ga235c0d680cb674b6e99d886497f257d5)void [log\_frontend\_stmesp\_demux\_data](group__log__frontend__stpesp__demux__apis.md#ga235c0d680cb674b6e99d886497f257d5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

251

[ 253](group__log__frontend__stpesp__demux__apis.md#ga38e05a234824b0adbeca16cb3e21cc75)void [log\_frontend\_stmesp\_demux\_packet\_end](group__log__frontend__stpesp__demux__apis.md#ga38e05a234824b0adbeca16cb3e21cc75)(void);

254

[ 261](group__log__frontend__stpesp__demux__apis.md#gaa624af8e67b4be013f0ec1507d805c34)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_frontend\_stmesp\_demux\_get\_dropped](group__log__frontend__stpesp__demux__apis.md#gaa624af8e67b4be013f0ec1507d805c34)(void);

262

[ 270](group__log__frontend__stpesp__demux__apis.md#gaf7b66578311278e6d58312ea239c9c0c)union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) [log\_frontend\_stmesp\_demux\_claim](group__log__frontend__stpesp__demux__apis.md#gaf7b66578311278e6d58312ea239c9c0c)(void);

271

[ 278](group__log__frontend__stpesp__demux__apis.md#gad9c13b59d1e09a240ed35b03b04b1a96)void [log\_frontend\_stmesp\_demux\_free](group__log__frontend__stpesp__demux__apis.md#gad9c13b59d1e09a240ed35b03b04b1a96)(union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) packet);

279

[ 293](group__log__frontend__stpesp__demux__apis.md#ga10621a1e4c5b875650b3ff89b3e97297)const char \*[log\_frontend\_stmesp\_demux\_sname\_get](group__log__frontend__stpesp__demux__apis.md#ga10621a1e4c5b875650b3ff89b3e97297)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) m\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) s\_id);

[ 294](group__log__frontend__stpesp__demux__apis.md#ga7c692b9d84aedfb30673a58959465ccf)const char \*[log\_frontend\_stmesp\_demux\_str\_get](group__log__frontend__stpesp__demux__apis.md#ga7c692b9d84aedfb30673a58959465ccf)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) m\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) s\_id);

295

[ 301](group__log__frontend__stpesp__demux__apis.md#ga1d693b8936666f7b352fd7e25535ac16)bool [log\_frontend\_stmesp\_demux\_is\_idle](group__log__frontend__stpesp__demux__apis.md#ga1d693b8936666f7b352fd7e25535ac16)(void);

302

[ 304](group__log__frontend__stpesp__demux__apis.md#ga487c9163e6477a879136350d4c109641)void [log\_frontend\_stmesp\_demux\_reset](group__log__frontend__stpesp__demux__apis.md#ga487c9163e6477a879136350d4c109641)(void);

305

[ 311](group__log__frontend__stpesp__demux__apis.md#ga7be93bc9ad1ecfe37f5af64adf029f39)int [log\_frontend\_stmesp\_demux\_max\_utilization](group__log__frontend__stpesp__demux__apis.md#ga7be93bc9ad1ecfe37f5af64adf029f39)(void);

312

316

317#ifdef \_\_cplusplus

318}

319#endif

320

321#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_FRONTEND\_STMESP\_DEMUX\_H\_ \*/

[log\_frontend\_stmesp\_demux\_sname\_get](group__log__frontend__stpesp__demux__apis.md#ga10621a1e4c5b875650b3ff89b3e97297)

const char \* log\_frontend\_stmesp\_demux\_sname\_get(uint32\_t m\_id, uint16\_t s\_id)

Get source name for a turbo log message.

[log\_frontend\_stmesp\_demux\_timestamp](group__log__frontend__stpesp__demux__apis.md#ga184cc4d266a010aa094a45aba0fad638)

void log\_frontend\_stmesp\_demux\_timestamp(uint64\_t ts)

Indicate timestamp.

[log\_frontend\_stmesp\_demux\_is\_idle](group__log__frontend__stpesp__demux__apis.md#ga1d693b8936666f7b352fd7e25535ac16)

bool log\_frontend\_stmesp\_demux\_is\_idle(void)

Check if there are any started but not completed log messages.

[log\_frontend\_stmesp\_demux\_data](group__log__frontend__stpesp__demux__apis.md#ga235c0d680cb674b6e99d886497f257d5)

void log\_frontend\_stmesp\_demux\_data(uint8\_t \*data, size\_t len)

Indicate data.

[LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS](group__log__frontend__stpesp__demux__apis.md#ga33581c39a57eca7f96fea9c29386a3e3)

#define LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS

Bits used to store major index.

**Definition** log\_frontend\_stmesp\_demux.h:28

[log\_frontend\_stmesp\_demux\_packet\_end](group__log__frontend__stpesp__demux__apis.md#ga38e05a234824b0adbeca16cb3e21cc75)

void log\_frontend\_stmesp\_demux\_packet\_end(void)

Indicate packet end (Flag).

[log\_frontend\_stmesp\_demux\_reset](group__log__frontend__stpesp__demux__apis.md#ga487c9163e6477a879136350d4c109641)

void log\_frontend\_stmesp\_demux\_reset(void)

Close any opened messages and mark them as invalid.

[log\_frontend\_stmesp\_demux\_channel](group__log__frontend__stpesp__demux__apis.md#ga4f86c0cfb38fa05389462045019a6650)

void log\_frontend\_stmesp\_demux\_channel(uint16\_t id)

Indicate channel opcode in the STPv2 stream.

[LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS](group__log__frontend__stpesp__demux__apis.md#ga56ad2b8067d56b9ccedefd57ad5aa0c2)

#define LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS

Bits used to store package length.

**Definition** log\_frontend\_stmesp\_demux.h:37

[log\_frontend\_stmesp\_demux\_log0](group__log__frontend__stpesp__demux__apis.md#ga6a25dd796a8759009e14b5770f7653a9)

int log\_frontend\_stmesp\_demux\_log0(uint16\_t source\_id, uint64\_t \*ts)

Indicate optimized log message with no arguments.

[log\_frontend\_stmesp\_demux\_max\_utilization](group__log__frontend__stpesp__demux__apis.md#ga7be93bc9ad1ecfe37f5af64adf029f39)

int log\_frontend\_stmesp\_demux\_max\_utilization(void)

Get maximum buffer utilization.

[log\_frontend\_stmesp\_demux\_str\_get](group__log__frontend__stpesp__demux__apis.md#ga7c692b9d84aedfb30673a58959465ccf)

const char \* log\_frontend\_stmesp\_demux\_str\_get(uint32\_t m\_id, uint16\_t s\_id)

[log\_frontend\_stmesp\_demux\_major](group__log__frontend__stpesp__demux__apis.md#ga8be4ca332fa9145fad72a6b45245a9ff)

void log\_frontend\_stmesp\_demux\_major(uint16\_t id)

Indicate major opcode in the STPv2 stream.

[log\_frontend\_stmesp\_demux\_init](group__log__frontend__stpesp__demux__apis.md#ga97f9ac1d7b459e9d3d715b5367e29a31)

int log\_frontend\_stmesp\_demux\_init(const struct log\_frontend\_stmesp\_demux\_config \*config)

Initialize the demultiplexer.

[log\_frontend\_stmesp\_demux\_get\_dropped](group__log__frontend__stpesp__demux__apis.md#gaa624af8e67b4be013f0ec1507d805c34)

uint32\_t log\_frontend\_stmesp\_demux\_get\_dropped(void)

Get number of dropped messages and reset the counter.

[log\_frontend\_stmesp\_demux\_free](group__log__frontend__stpesp__demux__apis.md#gad9c13b59d1e09a240ed35b03b04b1a96)

void log\_frontend\_stmesp\_demux\_free(union log\_frontend\_stmesp\_demux\_packet packet)

Free previously claimed packet.

[log\_frontend\_stmesp\_demux\_source\_id](group__log__frontend__stpesp__demux__apis.md#gae5925a640c401cc09dd744945eafd51c)

void log\_frontend\_stmesp\_demux\_source\_id(uint16\_t source\_id)

Indicate source ID.

[LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS](group__log__frontend__stpesp__demux__apis.md#gaeaf76dcb74836740115c9b6e3fece73b)

#define LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS

Bits used to store total length.

**Definition** log\_frontend\_stmesp\_demux.h:34

[log\_frontend\_stmesp\_demux\_packet\_start](group__log__frontend__stpesp__demux__apis.md#gaed29a1869e710cd95c19c48c67a36aa8)

int log\_frontend\_stmesp\_demux\_packet\_start(uint32\_t \*data, uint64\_t \*ts)

Indicate detected packet start (DMTS).

[LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS](group__log__frontend__stpesp__demux__apis.md#gaf2b7019394d33a082fec5ab2d2785257)

#define LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS

Bits used to store severity level.

**Definition** log\_frontend\_stmesp\_demux.h:31

[log\_frontend\_stmesp\_demux\_claim](group__log__frontend__stpesp__demux__apis.md#gaf7b66578311278e6d58312ea239c9c0c)

union log\_frontend\_stmesp\_demux\_packet log\_frontend\_stmesp\_demux\_claim(void)

Claim packet.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mpsc\_packet.h](mpsc__packet_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md)

Demultiplexer configuration.

**Definition** log\_frontend\_stmesp\_demux.h:181

[log\_frontend\_stmesp\_demux\_config::source\_id\_buf\_len](structlog__frontend__stmesp__demux__config.md#a643b5bd780342bf1944e5a63274aa305)

size\_t source\_id\_buf\_len

It must be multiple of number of major ID's count.

**Definition** log\_frontend\_stmesp\_demux.h:192

[log\_frontend\_stmesp\_demux\_config::source\_id\_buf](structlog__frontend__stmesp__demux__config.md#aca85e1b671127e8803423f22b2d45a33)

uint32\_t \* source\_id\_buf

Buffer for storing source ID's.

**Definition** log\_frontend\_stmesp\_demux.h:189

[log\_frontend\_stmesp\_demux\_config::m\_ids\_cnt](structlog__frontend__stmesp__demux__config.md#ad248eabec1eee58f5ef689004d5c7017)

uint32\_t m\_ids\_cnt

Array length.

**Definition** log\_frontend\_stmesp\_demux.h:186

[log\_frontend\_stmesp\_demux\_config::m\_ids](structlog__frontend__stmesp__demux__config.md#ada2f243b112324e99a53b831211cabce)

const uint16\_t \* m\_ids

Array with expected major ID's.

**Definition** log\_frontend\_stmesp\_demux.h:183

[log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md)

Packet with HW event.

**Definition** log\_frontend\_stmesp\_demux.h:142

[log\_frontend\_stmesp\_demux\_hw\_event::timestamp](structlog__frontend__stmesp__demux__hw__event.md#a0766f3aa6163ea1a197d674eac00305b)

uint64\_t timestamp

Timestamp.

**Definition** log\_frontend\_stmesp\_demux.h:153

[log\_frontend\_stmesp\_demux\_hw\_event::evt](structlog__frontend__stmesp__demux__hw__event.md#a090039b38d646812a292510476d16644)

uint8\_t evt

HW event ID.

**Definition** log\_frontend\_stmesp\_demux.h:156

[log\_frontend\_stmesp\_demux\_hw\_event::type](structlog__frontend__stmesp__demux__hw__event.md#a5a781f1b681ef2499bf9ba2635261d4f)

uint64\_t type

Type.

**Definition** log\_frontend\_stmesp\_demux.h:147

[log\_frontend\_stmesp\_demux\_hw\_event::MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__hw__event.md#a6a060e7fbda81c47eaa8088f3e45052a)

MPSC\_PBUF\_HDR

Data for MPSC packet handling.

**Definition** log\_frontend\_stmesp\_demux.h:144

[log\_frontend\_stmesp\_demux\_hw\_event::content\_invalid](structlog__frontend__stmesp__demux__hw__event.md#ae6872dcd7e11eeb431e3d990ccdad243)

uint64\_t content\_invalid

Flag indicating if packet is valid.

**Definition** log\_frontend\_stmesp\_demux.h:150

[log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md)

Logging message header.

**Definition** log\_frontend\_stmesp\_demux.h:52

[log\_frontend\_stmesp\_demux\_log\_header::package\_len](structlog__frontend__stmesp__demux__log__header.md#a0a378b7740a3def454bf34fe54927aa1)

uint32\_t package\_len

Hexdump data length.

**Definition** log\_frontend\_stmesp\_demux.h:63

[log\_frontend\_stmesp\_demux\_log\_header::total\_len](structlog__frontend__stmesp__demux__log__header.md#a138b653d76c50c0454210b7a1d7ec60b)

uint32\_t total\_len

Total length excluding this header.

**Definition** log\_frontend\_stmesp\_demux.h:60

[log\_frontend\_stmesp\_demux\_log\_header::level](structlog__frontend__stmesp__demux__log__header.md#a3b1474632ab446d8c9d590fb4bd8e420)

uint32\_t level

Severity level.

**Definition** log\_frontend\_stmesp\_demux.h:57

[log\_frontend\_stmesp\_demux\_log\_header::major](structlog__frontend__stmesp__demux__log__header.md#acec1720948196deb1f09ab1ea443ecb9)

uint32\_t major

Major index.

**Definition** log\_frontend\_stmesp\_demux.h:54

[log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md)

Packet with logging message.

**Definition** log\_frontend\_stmesp\_demux.h:88

[log\_frontend\_stmesp\_demux\_log::content\_invalid](structlog__frontend__stmesp__demux__log.md#a84cf9f64d96e87cfd2bb9d859fed3886)

uint64\_t content\_invalid

Flag indicating if packet is valid.

**Definition** log\_frontend\_stmesp\_demux.h:96

[log\_frontend\_stmesp\_demux\_log::hdr](structlog__frontend__stmesp__demux__log.md#aa5b7175e05dbdcc41d75c5412ce30b15)

struct log\_frontend\_stmesp\_demux\_log\_header hdr

Logging header.

**Definition** log\_frontend\_stmesp\_demux.h:102

[log\_frontend\_stmesp\_demux\_log::padding](structlog__frontend__stmesp__demux__log.md#ab063e3ed4d81cbdb4ec417508c55bd13)

uint32\_t padding

Padding so that data is 8 bytes aligned.

**Definition** log\_frontend\_stmesp\_demux.h:105

[log\_frontend\_stmesp\_demux\_log::MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__log.md#ad25f0378c2c3ba3d153a58a843704033)

MPSC\_PBUF\_HDR

Data for MPSC packet handling.

**Definition** log\_frontend\_stmesp\_demux.h:90

[log\_frontend\_stmesp\_demux\_log::type](structlog__frontend__stmesp__demux__log.md#adb1b61bdca3a97df2c8ba2b34fc2ebff)

uint64\_t type

Type.

**Definition** log\_frontend\_stmesp\_demux.h:93

[log\_frontend\_stmesp\_demux\_log::data](structlog__frontend__stmesp__demux__log.md#ae8c62ffd8a11fbcebce29ed934f52597)

uint8\_t data[]

Content.

**Definition** log\_frontend\_stmesp\_demux.h:108

[log\_frontend\_stmesp\_demux\_log::timestamp](structlog__frontend__stmesp__demux__log.md#af2b9820efce6f58d655b08a306c8d8d1)

uint64\_t timestamp

Timestamp.

**Definition** log\_frontend\_stmesp\_demux.h:99

[log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md)

Generic STP demux packet.

**Definition** log\_frontend\_stmesp\_demux.h:76

[log\_frontend\_stmesp\_demux\_packet\_generic::content\_invalid](structlog__frontend__stmesp__demux__packet__generic.md#a42d6b5192e0f9ba897a2986d645c6a6c)

uint64\_t content\_invalid

Flag indicating if packet is valid.

**Definition** log\_frontend\_stmesp\_demux.h:84

[log\_frontend\_stmesp\_demux\_packet\_generic::type](structlog__frontend__stmesp__demux__packet__generic.md#a7a86c5de5e5b33830d963add116c1feb)

uint64\_t type

Type.

**Definition** log\_frontend\_stmesp\_demux.h:81

[log\_frontend\_stmesp\_demux\_packet\_generic::MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__packet__generic.md#ac202cf6bc5bc8699a858e10de2c0c492)

MPSC\_PBUF\_HDR

Data for MPSC packet handling.

**Definition** log\_frontend\_stmesp\_demux.h:78

[log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md)

Packet with trace point.

**Definition** log\_frontend\_stmesp\_demux.h:112

[log\_frontend\_stmesp\_demux\_trace\_point::has\_data](structlog__frontend__stmesp__demux__trace__point.md#a0bdc2a3e1afb5748e08e68617f2ccbb6)

uint64\_t has\_data

Flag indicating if trace point includes data.

**Definition** log\_frontend\_stmesp\_demux.h:123

[log\_frontend\_stmesp\_demux\_trace\_point::source\_id](structlog__frontend__stmesp__demux__trace__point.md#a0ca97d4ffd9bae1d640b8f99c8bd5ace)

uint16\_t source\_id

Source ID - used for compressed logging.

**Definition** log\_frontend\_stmesp\_demux.h:132

[log\_frontend\_stmesp\_demux\_trace\_point::content\_invalid](structlog__frontend__stmesp__demux__trace__point.md#a300adc8bd0882810ae4a5759a76857ce)

uint64\_t content\_invalid

Flag indicating if packet is valid.

**Definition** log\_frontend\_stmesp\_demux.h:120

[log\_frontend\_stmesp\_demux\_trace\_point::timestamp](structlog__frontend__stmesp__demux__trace__point.md#a6e1892f15fa3149f8161a1792420ba73)

uint64\_t timestamp

Timestamp.

**Definition** log\_frontend\_stmesp\_demux.h:126

[log\_frontend\_stmesp\_demux\_trace\_point::type](structlog__frontend__stmesp__demux__trace__point.md#ab250b6782df720df3d1cdb37ab25a024)

uint64\_t type

Type.

**Definition** log\_frontend\_stmesp\_demux.h:117

[log\_frontend\_stmesp\_demux\_trace\_point::major](structlog__frontend__stmesp__demux__trace__point.md#acfa056769b9ba00b945e1ff7d1e4cdb9)

uint64\_t major

Major ID.

**Definition** log\_frontend\_stmesp\_demux.h:129

[log\_frontend\_stmesp\_demux\_trace\_point::data](structlog__frontend__stmesp__demux__trace__point.md#ada954ed2971c2fc720a1d1f2634c0e2a)

uint32\_t data

Content.

**Definition** log\_frontend\_stmesp\_demux.h:138

[log\_frontend\_stmesp\_demux\_trace\_point::MPSC\_PBUF\_HDR](structlog__frontend__stmesp__demux__trace__point.md#ae3e776e4a470ccb3abd8f6a73ce7b21b)

MPSC\_PBUF\_HDR

Data for MPSC packet handling.

**Definition** log\_frontend\_stmesp\_demux.h:114

[log\_frontend\_stmesp\_demux\_trace\_point::id](structlog__frontend__stmesp__demux__trace__point.md#aeb86bfae01245a4778d08ac9c1ee138a)

uint16\_t id

ID.

**Definition** log\_frontend\_stmesp\_demux.h:135

[log\_frontend\_stmesp\_demux\_header](unionlog__frontend__stmesp__demux__header.md)

Union for writing raw data to the logging message header.

**Definition** log\_frontend\_stmesp\_demux.h:67

[log\_frontend\_stmesp\_demux\_header::raw](unionlog__frontend__stmesp__demux__header.md#ae868e8f2e8b0623781d3f9377490c72a)

uint32\_t raw

Raw word.

**Definition** log\_frontend\_stmesp\_demux.h:72

[log\_frontend\_stmesp\_demux\_header::log](unionlog__frontend__stmesp__demux__header.md#ae94bab609a4f5c51eef7886db712420d)

struct log\_frontend\_stmesp\_demux\_log\_header log

Log header structure.

**Definition** log\_frontend\_stmesp\_demux.h:69

[log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md)

Union of all packet types.

**Definition** log\_frontend\_stmesp\_demux.h:160

[log\_frontend\_stmesp\_demux\_packet::generic\_packet](unionlog__frontend__stmesp__demux__packet.md#a30d3cfc6071bebc1614f2f67c8a950c7)

struct log\_frontend\_stmesp\_demux\_packet\_generic \* generic\_packet

Pointer to the generic log\_frontend\_stmesp\_demux packet.

**Definition** log\_frontend\_stmesp\_demux.h:177

[log\_frontend\_stmesp\_demux\_packet::trace\_point](unionlog__frontend__stmesp__demux__packet.md#aa68b1022f97c8806ee430a541190fc82)

struct log\_frontend\_stmesp\_demux\_trace\_point \* trace\_point

Pointer to the trace point message.

**Definition** log\_frontend\_stmesp\_demux.h:171

[log\_frontend\_stmesp\_demux\_packet::rgeneric](unionlog__frontend__stmesp__demux__packet.md#ac712f4dc2ca645e2ba6f6c638b41bf10)

const union mpsc\_pbuf\_generic \* rgeneric

Pointer to generic mpsc\_pbuf const packet.

**Definition** log\_frontend\_stmesp\_demux.h:162

[log\_frontend\_stmesp\_demux\_packet::log](unionlog__frontend__stmesp__demux__packet.md#ac75deeb2f665aeb5dcfd94090aa1a1cf)

struct log\_frontend\_stmesp\_demux\_log \* log

Pointer to the log message.

**Definition** log\_frontend\_stmesp\_demux.h:168

[log\_frontend\_stmesp\_demux\_packet::hw\_event](unionlog__frontend__stmesp__demux__packet.md#ae764f7a3b04e66af22c52aa1d52a441e)

struct log\_frontend\_stmesp\_demux\_hw\_event \* hw\_event

Pointer to the HW event message.

**Definition** log\_frontend\_stmesp\_demux.h:174

[mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)

Generic packet header.

**Definition** mpsc\_packet.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
