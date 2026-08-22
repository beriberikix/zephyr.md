---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/server_8h_source.html
original_path: doxygen/html/server_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

server.h

[Go to the documentation of this file.](server_8h.md)

1/\*

2 \* Copyright (c) 2023, Emna Rekik

3 \* Copyright (c) 2024 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVER\_H\_

9#define ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVER\_H\_

10

22

23#include <[stdint.h](stdint_8h.md)>

24

25#include <[zephyr/kernel.h](kernel_8h.md)>

26#include <[zephyr/net/http/parser.h](parser_8h.md)>

27#include <[zephyr/net/http/hpack.h](hpack_8h.md)>

28#include <[zephyr/net/http/status.h](status_8h.md)>

29#include <[zephyr/net/socket.h](net_2socket_8h.md)>

30#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

37

38#if defined(CONFIG\_HTTP\_SERVER)

39#define HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE CONFIG\_HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE

40#define HTTP\_SERVER\_MAX\_STREAMS CONFIG\_HTTP\_SERVER\_MAX\_STREAMS

41#define HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN CONFIG\_HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LENGTH

42#define HTTP\_SERVER\_MAX\_URL\_LENGTH CONFIG\_HTTP\_SERVER\_MAX\_URL\_LENGTH

43#define HTTP\_SERVER\_MAX\_HEADER\_LEN CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN

44#else

45#define HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE 0

46#define HTTP\_SERVER\_MAX\_STREAMS 0

47#define HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN 0

48#define HTTP\_SERVER\_MAX\_URL\_LENGTH 0

49#define HTTP\_SERVER\_MAX\_HEADER\_LEN 0

50#endif

51

52#if defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS)

53#define HTTP\_SERVER\_CAPTURE\_HEADER\_BUFFER\_SIZE CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADER\_BUFFER\_SIZE

54#define HTTP\_SERVER\_CAPTURE\_HEADER\_COUNT CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADER\_COUNT

55#else

56#define HTTP\_SERVER\_CAPTURE\_HEADER\_BUFFER\_SIZE 0

57#define HTTP\_SERVER\_CAPTURE\_HEADER\_COUNT 0

58#endif

59

60#define HTTP2\_PREFACE "PRI \* HTTP/2.0\r\n\r\nSM\r\n\r\n"

61

63

[ 67](group__http__server.md#ga23d0077fb99827b25491111bd74d00af)enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) {

[ 69](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) [HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248),

70

[ 72](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e) [HTTP\_RESOURCE\_TYPE\_STATIC\_FS](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e),

73

[ 77](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) [HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e),

78

[ 82](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866),

83};

84

[ 88](structhttp__resource__detail.md)struct [http\_resource\_detail](structhttp__resource__detail.md) {

[ 90](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bitmask\_of\_supported\_http\_methods](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817);

91

[ 93](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68) enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) [type](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68);

94

[ 96](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860) int [path\_len](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860);

97

[ 99](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4) const char \*[content\_encoding](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4);

100

[ 102](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084) const char \*[content\_type](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084);

103};

104

106BUILD\_ASSERT([NUM\_BITS](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)(

107 sizeof(((struct [http\_resource\_detail](structhttp__resource__detail.md) \*)0)->bitmask\_of\_supported\_http\_methods))

108 >= (HTTP\_METHOD\_END\_VALUE - 1));

110

[ 114](structhttp__resource__detail__static.md)struct [http\_resource\_detail\_static](structhttp__resource__detail__static.md) {

[ 116](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725);

117

[ 119](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9) const void \*[static\_data](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9);

120

[ 122](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484) size\_t [static\_data\_len](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484);

123};

124

126/\* Make sure that the common is the first in the struct. \*/

127BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_static](structhttp__resource__detail__static.md), common) == 0);

129

[ 133](structhttp__resource__detail__static__fs.md)struct [http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md) {

[ 135](structhttp__resource__detail__static__fs.md#a3cb3f688d0070ad3316f33bc05a78f78) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__static__fs.md#a3cb3f688d0070ad3316f33bc05a78f78);

136

[ 138](structhttp__resource__detail__static__fs.md#a5b25a03b953313b392096bab2faa3be8) const char \*[fs\_path](structhttp__resource__detail__static__fs.md#a5b25a03b953313b392096bab2faa3be8);

139};

140

[ 142](group__http__server.md#gaf124b6ddd491dd6075b9c68db6686607)enum [http\_compression](group__http__server.md#gaf124b6ddd491dd6075b9c68db6686607) {

[ 143](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202) [HTTP\_NONE](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202) = 0,

[ 144](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8) [HTTP\_GZIP](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8) = 1,

[ 145](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50) [HTTP\_COMPRESS](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50) = 2,

[ 146](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43) [HTTP\_DEFLATE](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43) = 3,

[ 147](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569) [HTTP\_BR](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569) = 4,

[ 148](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0) [HTTP\_ZSTD](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0) = 5

149};

150

152/\* Make sure that the common is the first in the struct. \*/

153BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md), common) == 0);

155

[ 156](structhttp__content__type.md)struct [http\_content\_type](structhttp__content__type.md) {

[ 157](structhttp__content__type.md#afe5cc6179e38766a3ee7a97a0e981cdd) const char \*[extension](structhttp__content__type.md#afe5cc6179e38766a3ee7a97a0e981cdd);

[ 158](structhttp__content__type.md#a9235678c39a82386df70ad5efdcc33ab) size\_t [extension\_len](structhttp__content__type.md#a9235678c39a82386df70ad5efdcc33ab);

[ 159](structhttp__content__type.md#a78e378def414fd5d9ad9df45df9144fe) const char \*[content\_type](structhttp__content__type.md#a78e378def414fd5d9ad9df45df9144fe);

160};

161

[ 162](group__http__server.md#ga709ddfe3f5ae5605b3399687f8be8c47)#define HTTP\_SERVER\_CONTENT\_TYPE(\_extension, \_content\_type) \

163 const STRUCT\_SECTION\_ITERABLE(http\_content\_type, \_extension) = { \

164 .extension = STRINGIFY(\_extension), \

165 .extension\_len = sizeof(STRINGIFY(\_extension)) - 1, \

166 .content\_type = \_content\_type, \

167 };

168

[ 169](group__http__server.md#gad1ee2e803d6e38d54c344180a45a25c2)#define HTTP\_SERVER\_CONTENT\_TYPE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_content\_type, \_it)

170

171struct [http\_client\_ctx](structhttp__client__ctx.md);

172

[ 174](group__http__server.md#ga496accfe23add03417bdc98369d32ea8)enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) {

[ 176](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) [HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1,

[ 178](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) [HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0,

[ 180](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) [HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1,

181};

182

[ 184](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3)enum [http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) {

[ 185](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec) [HTTP\_HEADER\_STATUS\_OK](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec),

[ 186](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621) [HTTP\_HEADER\_STATUS\_DROPPED](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621),

[ 187](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed) [HTTP\_HEADER\_STATUS\_NONE](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed),

188};

189

[ 191](structhttp__header.md)struct [http\_header](structhttp__header.md) {

[ 192](structhttp__header.md#afc8e4fa57f957f1fd34ce570c98537f5) const char \*[name](structhttp__header.md#afc8e4fa57f957f1fd34ce570c98537f5);

[ 193](structhttp__header.md#acac6fa1c3ca33cd67119209dc981e5f9) const char \*[value](structhttp__header.md#acac6fa1c3ca33cd67119209dc981e5f9);

194};

195

[ 197](structhttp__request__ctx.md)struct [http\_request\_ctx](structhttp__request__ctx.md) {

[ 198](structhttp__request__ctx.md#aae773946b597bb7ca70d071daadf3c1d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structhttp__request__ctx.md#aae773946b597bb7ca70d071daadf3c1d);

[ 199](structhttp__request__ctx.md#a4de5c3114220bef60bcd587f4796603e) size\_t [data\_len](structhttp__request__ctx.md#a4de5c3114220bef60bcd587f4796603e);

[ 200](structhttp__request__ctx.md#a9500727563dd6f33663c0a26299a16a6) struct [http\_header](structhttp__header.md) \*[headers](structhttp__request__ctx.md#a9500727563dd6f33663c0a26299a16a6);

[ 201](structhttp__request__ctx.md#a404ff7f9946f162dc0ef6c0a872bf88b) size\_t [header\_count](structhttp__request__ctx.md#a404ff7f9946f162dc0ef6c0a872bf88b);

[ 202](structhttp__request__ctx.md#a312cc4db494a0415a2c0342183b3a3c6) enum [http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) [headers\_status](structhttp__request__ctx.md#a312cc4db494a0415a2c0342183b3a3c6);

203};

204

[ 206](structhttp__response__ctx.md)struct [http\_response\_ctx](structhttp__response__ctx.md) {

[ 207](structhttp__response__ctx.md#ada151e7a981885622a79a5ae1f12b2e9) enum [http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d) [status](structhttp__response__ctx.md#ada151e7a981885622a79a5ae1f12b2e9);

[ 208](structhttp__response__ctx.md#a63acf00d5ff891ab51107458c545399d) const struct [http\_header](structhttp__header.md) \*[headers](structhttp__response__ctx.md#a63acf00d5ff891ab51107458c545399d);

[ 209](structhttp__response__ctx.md#a7a7b446baf1a1ab343437ee527ddde95) size\_t [header\_count](structhttp__response__ctx.md#a7a7b446baf1a1ab343437ee527ddde95);

[ 210](structhttp__response__ctx.md#aa027d1577dd19db43a17cdd0959b8e39) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[body](structhttp__response__ctx.md#aa027d1577dd19db43a17cdd0959b8e39);

[ 211](structhttp__response__ctx.md#a88b128e354c85f574409abd55633d2e2) size\_t [body\_len](structhttp__response__ctx.md#a88b128e354c85f574409abd55633d2e2);

[ 212](structhttp__response__ctx.md#a53162ff65b66567b31ec323558bc1fe2) bool [final\_chunk](structhttp__response__ctx.md#a53162ff65b66567b31ec323558bc1fe2);

213};

214

[ 229](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f)typedef int (\*[http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f))(struct [http\_client\_ctx](structhttp__client__ctx.md) \*client,

230 enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) status,

231 const struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx,

232 struct [http\_response\_ctx](structhttp__response__ctx.md) \*response\_ctx,

233 void \*user\_data);

234

[ 238](structhttp__resource__detail__dynamic.md)struct [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md) {

[ 240](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab);

241

[ 245](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7) [http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f) [cb](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7);

246

[ 250](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856) struct [http\_client\_ctx](structhttp__client__ctx.md) \*[holder](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856);

251

[ 253](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4) void \*[user\_data](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4);

254};

255

257BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md), common) == 0);

259

[ 275](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93)typedef int (\*[http\_resource\_websocket\_cb\_t](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93))(int ws\_socket, struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx,

276 void \*user\_data);

277

[ 279](structhttp__resource__detail__websocket.md)struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md) {

[ 281](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee);

282

[ 284](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8) int [ws\_sock](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8);

285

[ 289](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0) [http\_resource\_websocket\_cb\_t](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93) [cb](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0);

290

[ 294](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_buffer](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c);

295

[ 297](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117) size\_t [data\_buffer\_len](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117);

298

[ 300](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8) void \*[user\_data](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8);

301};

302

304BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md), common) == 0);

306

308

309enum http2\_stream\_state {

310 HTTP2\_STREAM\_IDLE,

311 HTTP2\_STREAM\_RESERVED\_LOCAL,

312 HTTP2\_STREAM\_RESERVED\_REMOTE,

313 HTTP2\_STREAM\_OPEN,

314 HTTP2\_STREAM\_HALF\_CLOSED\_LOCAL,

315 HTTP2\_STREAM\_HALF\_CLOSED\_REMOTE,

316 HTTP2\_STREAM\_CLOSED

317};

318

319enum http\_server\_state {

320 HTTP\_SERVER\_FRAME\_HEADER\_STATE,

321 HTTP\_SERVER\_PREFACE\_STATE,

322 HTTP\_SERVER\_REQUEST\_STATE,

323 HTTP\_SERVER\_FRAME\_DATA\_STATE,

324 HTTP\_SERVER\_FRAME\_HEADERS\_STATE,

325 HTTP\_SERVER\_FRAME\_SETTINGS\_STATE,

326 HTTP\_SERVER\_FRAME\_PRIORITY\_STATE,

327 HTTP\_SERVER\_FRAME\_WINDOW\_UPDATE\_STATE,

328 HTTP\_SERVER\_FRAME\_CONTINUATION\_STATE,

329 HTTP\_SERVER\_FRAME\_PING\_STATE,

330 HTTP\_SERVER\_FRAME\_RST\_STREAM\_STATE,

331 HTTP\_SERVER\_FRAME\_GOAWAY\_STATE,

332 HTTP\_SERVER\_FRAME\_PADDING\_STATE,

333 HTTP\_SERVER\_DONE\_STATE,

334};

335

336enum http1\_parser\_state {

337 HTTP1\_INIT\_HEADER\_STATE,

338 HTTP1\_WAITING\_HEADER\_STATE,

339 HTTP1\_RECEIVING\_HEADER\_STATE,

340 HTTP1\_RECEIVED\_HEADER\_STATE,

341 HTTP1\_RECEIVING\_DATA\_STATE,

342 HTTP1\_MESSAGE\_COMPLETE\_STATE,

343};

344

345#define HTTP\_SERVER\_INITIAL\_WINDOW\_SIZE 65536

346#define HTTP\_SERVER\_WS\_MAX\_SEC\_KEY\_LEN 32

347

349

[ 351](structhttp2__stream__ctx.md)struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) {

[ 352](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7) int [stream\_id](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7);

[ 353](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa) enum http2\_stream\_state [stream\_state](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa);

[ 354](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279) int [window\_size](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279);

355

[ 357](structhttp2__stream__ctx.md#ad1dd959dcbc4096aa7c3486b50409540) struct [http\_resource\_detail](structhttp__resource__detail.md) \*[current\_detail](structhttp2__stream__ctx.md#ad1dd959dcbc4096aa7c3486b50409540);

358

[ 360](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b) bool [headers\_sent](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b) : 1;

361

[ 363](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6) bool [end\_stream\_sent](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6) : 1;

364};

365

[ 367](structhttp2__frame.md)struct [http2\_frame](structhttp2__frame.md) {

[ 368](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [length](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a);

[ 369](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stream\_identifier](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543);

[ 370](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59);

[ 371](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c);

[ 372](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding\_len](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528);

373};

374

377struct http\_header\_capture\_ctx {

379 unsigned char buffer[HTTP\_SERVER\_CAPTURE\_HEADER\_BUFFER\_SIZE];

380

382 struct [http\_header](structhttp__header.md) headers[HTTP\_SERVER\_CAPTURE\_HEADER\_COUNT];

383

385 enum [http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3) status;

386

388 size\_t count;

389

391 size\_t cursor;

392

394 struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) \*current\_stream;

395

397 bool store\_next\_value;

398};

400

[ 402](structhttp__header__name.md)struct [http\_header\_name](structhttp__header__name.md) {

[ 403](structhttp__header__name.md#a643c7da4121fad12b0f25ea18fc709d0) const char \*[name](structhttp__header__name.md#a643c7da4121fad12b0f25ea18fc709d0);

404};

405

[ 409](structhttp__client__ctx.md)struct [http\_client\_ctx](structhttp__client__ctx.md) {

[ 411](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5) int [fd](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5);

412

[ 414](structhttp__client__ctx.md#aea8cfd5353abc7b6bd50acde9d2c8c23) const struct http\_service\_desc \*[service](structhttp__client__ctx.md#aea8cfd5353abc7b6bd50acde9d2c8c23);

415

[ 417](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63) unsigned char [buffer](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63)[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE];

418

[ 420](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376) unsigned char \*[cursor](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376);

421

[ 423](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167) size\_t [data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167);

424

[ 426](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d) int [window\_size](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d);

427

[ 429](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd) enum http\_server\_state [server\_state](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd);

430

[ 432](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406) struct [http2\_frame](structhttp2__frame.md) [current\_frame](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406);

433

[ 435](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314) struct [http\_resource\_detail](structhttp__resource__detail.md) \*[current\_detail](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314);

436

[ 438](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448) struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) \*[current\_stream](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448);

439

[ 441](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62) struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) [header\_field](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62);

442

[ 444](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138) struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) [streams](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138)[HTTP\_SERVER\_MAX\_STREAMS];

445

[ 447](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98) struct [http\_parser\_settings](structhttp__parser__settings.md) [parser\_settings](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98);

448

[ 450](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847) struct [http\_parser](structhttp__parser.md) [parser](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847);

451

[ 453](structhttp__client__ctx.md#af278d2f02f617d49c54639a29317b758) struct http\_header\_capture\_ctx [header\_capture\_ctx](structhttp__client__ctx.md#af278d2f02f617d49c54639a29317b758);

454

[ 456](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1) unsigned char [url\_buffer](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1)[HTTP\_SERVER\_MAX\_URL\_LENGTH];

457

[ 459](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4) unsigned char [content\_type](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4)[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN];

460

[ 462](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5) unsigned char [header\_buffer](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5)[HTTP\_SERVER\_MAX\_HEADER\_LEN];

463

[ 465](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959) size\_t [content\_len](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959);

466

[ 468](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15) enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) [method](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15);

469

[ 471](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0) enum http1\_parser\_state [parser\_state](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0);

472

[ 476](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49) int [http1\_frag\_data\_len](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49);

477

[ 481](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac) struct [k\_work\_delayable](structk__work__delayable.md) [inactivity\_timer](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac);

482

485 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_WEBSOCKET, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ws\_sec\_key[HTTP\_SERVER\_WS\_MAX\_SEC\_KEY\_LEN]));

487

490 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_HTTP\_SERVER\_COMPRESSION, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) supported\_compression));

492

[ 494](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1) bool [preface\_sent](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1) : 1;

495

[ 497](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2) bool [http1\_headers\_sent](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2) : 1;

498

[ 500](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9) bool [has\_upgrade\_header](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9) : 1;

501

[ 503](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55) bool [http2\_upgrade](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55) : 1;

504

[ 506](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1) bool [websocket\_upgrade](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1) : 1;

507

[ 509](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6) bool [websocket\_sec\_key\_next](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6) : 1;

510

[ 512](structhttp__client__ctx.md#afc21ace1fba336e739eb4181e9b8d55e) [IF\_ENABLED](structhttp__client__ctx.md#afc21ace1fba336e739eb4181e9b8d55e)(CONFIG\_HTTP\_SERVER\_COMPRESSION, (bool accept\_encoding\_next: 1));

513

[ 515](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620) bool [expect\_continuation](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620) : 1;

516};

517

[ 524](group__http__server.md#gae1710786f10729930cc6c220a19e2071)#define HTTP\_SERVER\_REGISTER\_HEADER\_CAPTURE(\_id, \_header) \

525 BUILD\_ASSERT(sizeof(\_header) <= CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN, \

526 "Header is too long to be captured, try increasing " \

527 "CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN"); \

528 static const char \*const \_id##\_str = \_header; \

529 static const STRUCT\_SECTION\_ITERABLE(http\_header\_name, \_id) = { \

530 .name = \_id##\_str, \

531 }

532

[ 539](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)int [http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)(void);

540

[ 545](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)int [http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)(void);

546

547#ifdef \_\_cplusplus

548}

549#endif

550

554

555#endif

[http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

http\_method

HTTP Request Methods.

**Definition** method.h:28

[http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af)

http\_resource\_type

HTTP server resource type.

**Definition** server.h:67

[http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8)

http\_data\_status

Indicates the status of the currently processed piece of data.

**Definition** server.h:174

[http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f)

int(\* http\_resource\_dynamic\_cb\_t)(struct http\_client\_ctx \*client, enum http\_data\_status status, const struct http\_request\_ctx \*request\_ctx, struct http\_response\_ctx \*response\_ctx, void \*user\_data)

Callback used when data is received.

**Definition** server.h:229

[http\_header\_status](group__http__server.md#ga6c15e872ece1b9a740b6dca3974101b3)

http\_header\_status

Status of captured request headers.

**Definition** server.h:184

[http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)

int http\_server\_stop(void)

Stop the HTTP2 server.

[http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)

int http\_server\_start(void)

Start the HTTP2 server.

[http\_resource\_websocket\_cb\_t](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93)

int(\* http\_resource\_websocket\_cb\_t)(int ws\_socket, struct http\_request\_ctx \*request\_ctx, void \*user\_data)

Callback used when a Websocket connection is setup.

**Definition** server.h:275

[http\_compression](group__http__server.md#gaf124b6ddd491dd6075b9c68db6686607)

http\_compression

HTTP compressions.

**Definition** server.h:142

[HTTP\_RESOURCE\_TYPE\_STATIC\_FS](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e)

@ HTTP\_RESOURCE\_TYPE\_STATIC\_FS

serves static gzipped files from a filesystem

**Definition** server.h:72

[HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)

@ HTTP\_RESOURCE\_TYPE\_STATIC

Static resource, cannot be modified on runtime.

**Definition** server.h:69

[HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)

@ HTTP\_RESOURCE\_TYPE\_WEBSOCKET

Websocket resource, application takes control over Websocket connection after and upgrade.

**Definition** server.h:82

[HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)

@ HTTP\_RESOURCE\_TYPE\_DYNAMIC

Dynamic resource, server interacts with the application via registered http\_resource\_dynamic\_cb\_t.

**Definition** server.h:77

[HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a)

@ HTTP\_SERVER\_DATA\_FINAL

Final data fragment in current transaction.

**Definition** server.h:180

[HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231)

@ HTTP\_SERVER\_DATA\_MORE

Transaction incomplete, more data expected.

**Definition** server.h:178

[HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc)

@ HTTP\_SERVER\_DATA\_ABORTED

Transaction aborted, data incomplete.

**Definition** server.h:176

[HTTP\_HEADER\_STATUS\_DROPPED](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3a3f41dca87eecce1ac499389e72285621)

@ HTTP\_HEADER\_STATUS\_DROPPED

One or more headers were dropped due to lack of space.

**Definition** server.h:186

[HTTP\_HEADER\_STATUS\_NONE](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ac01b170099c3ea7fafa5d22f164930ed)

@ HTTP\_HEADER\_STATUS\_NONE

No header status is available.

**Definition** server.h:187

[HTTP\_HEADER\_STATUS\_OK](group__http__server.md#gga6c15e872ece1b9a740b6dca3974101b3ad4ad497a135cc5855573cc0211e7b7ec)

@ HTTP\_HEADER\_STATUS\_OK

All available headers were successfully captured.

**Definition** server.h:185

[HTTP\_NONE](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a1a4a25c52411b1a87abca823223c7202)

@ HTTP\_NONE

NONE.

**Definition** server.h:143

[HTTP\_GZIP](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a39d987341b53034e236ecc0a48f40ae8)

@ HTTP\_GZIP

GZIP.

**Definition** server.h:144

[HTTP\_ZSTD](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607a710e784f734d4a574c302dc86f587aa0)

@ HTTP\_ZSTD

ZSTD.

**Definition** server.h:148

[HTTP\_DEFLATE](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607aa260077f859491f95c6ccb781a492e43)

@ HTTP\_DEFLATE

DEFLATE.

**Definition** server.h:146

[HTTP\_COMPRESS](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607ad7f9cc84c671c70f15bff03a2cf92c50)

@ HTTP\_COMPRESS

COMPRESS.

**Definition** server.h:145

[HTTP\_BR](group__http__server.md#ggaf124b6ddd491dd6075b9c68db6686607ae0de360c2162dab5adddd76f47f55569)

@ HTTP\_BR

BR.

**Definition** server.h:147

[http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d)

http\_status

HTTP response status codes.

**Definition** status.h:36

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:247

[hpack.h](hpack_8h.md)

HTTP HPACK.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[parser.h](parser_8h.md)

[status.h](status_8h.md)

HTTP response status codes.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[http2\_frame](structhttp2__frame.md)

HTTP/2 frame representation.

**Definition** server.h:367

[http2\_frame::stream\_identifier](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543)

uint32\_t stream\_identifier

Stream ID the frame belongs to.

**Definition** server.h:369

[http2\_frame::type](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59)

uint8\_t type

Frame type.

**Definition** server.h:370

[http2\_frame::flags](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c)

uint8\_t flags

Frame flags.

**Definition** server.h:371

[http2\_frame::padding\_len](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528)

uint8\_t padding\_len

Frame padding length.

**Definition** server.h:372

[http2\_frame::length](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a)

uint32\_t length

Frame payload length.

**Definition** server.h:368

[http2\_stream\_ctx](structhttp2__stream__ctx.md)

HTTP/2 stream representation.

**Definition** server.h:351

[http2\_stream\_ctx::headers\_sent](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b)

bool headers\_sent

Flag indicating that headers were sent in the reply.

**Definition** server.h:360

[http2\_stream\_ctx::stream\_state](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa)

enum http2\_stream\_state stream\_state

Stream state.

**Definition** server.h:353

[http2\_stream\_ctx::window\_size](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279)

int window\_size

Stream-level window size.

**Definition** server.h:354

[http2\_stream\_ctx::stream\_id](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7)

int stream\_id

Stream identifier.

**Definition** server.h:352

[http2\_stream\_ctx::current\_detail](structhttp2__stream__ctx.md#ad1dd959dcbc4096aa7c3486b50409540)

struct http\_resource\_detail \* current\_detail

Currently processed resource detail.

**Definition** server.h:357

[http2\_stream\_ctx::end\_stream\_sent](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6)

bool end\_stream\_sent

Flag indicating that END\_STREAM flag was sent.

**Definition** server.h:363

[http\_client\_ctx](structhttp__client__ctx.md)

Representation of an HTTP client connected to the server.

**Definition** server.h:409

[http\_client\_ctx::streams](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138)

struct http2\_stream\_ctx streams[HTTP\_SERVER\_MAX\_STREAMS]

HTTP/2 streams context.

**Definition** server.h:444

[http\_client\_ctx::inactivity\_timer](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac)

struct k\_work\_delayable inactivity\_timer

Client inactivity timer.

**Definition** server.h:481

[http\_client\_ctx::parser\_settings](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98)

struct http\_parser\_settings parser\_settings

HTTP/1 parser configuration.

**Definition** server.h:447

[http\_client\_ctx::cursor](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376)

unsigned char \* cursor

Cursor indicating currently processed byte.

**Definition** server.h:420

[http\_client\_ctx::window\_size](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d)

int window\_size

Connection-level window size.

**Definition** server.h:426

[http\_client\_ctx::parser\_state](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0)

enum http1\_parser\_state parser\_state

HTTP/1 parser state.

**Definition** server.h:471

[http\_client\_ctx::expect\_continuation](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620)

bool expect\_continuation

The next frame on the stream is expectd to be a continuation frame.

**Definition** server.h:515

[http\_client\_ctx::parser](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847)

struct http\_parser parser

HTTP/1 parser context.

**Definition** server.h:450

[http\_client\_ctx::http1\_frag\_data\_len](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49)

int http1\_frag\_data\_len

Length of the payload length in the currently processed request fragment (HTTP/1 only).

**Definition** server.h:476

[http\_client\_ctx::websocket\_sec\_key\_next](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6)

bool websocket\_sec\_key\_next

Flag indicating Websocket key is being processed.

**Definition** server.h:509

[http\_client\_ctx::server\_state](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd)

enum http\_server\_state server\_state

Server state for the associated client.

**Definition** server.h:429

[http\_client\_ctx::header\_field](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62)

struct http\_hpack\_header\_buf header\_field

HTTP/2 header parser context.

**Definition** server.h:441

[http\_client\_ctx::current\_detail](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314)

struct http\_resource\_detail \* current\_detail

Currently processed resource detail.

**Definition** server.h:435

[http\_client\_ctx::url\_buffer](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1)

unsigned char url\_buffer[HTTP\_SERVER\_MAX\_URL\_LENGTH]

Request URL.

**Definition** server.h:456

[http\_client\_ctx::header\_buffer](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5)

unsigned char header\_buffer[HTTP\_SERVER\_MAX\_HEADER\_LEN]

Temp buffer for currently processed header (HTTP/1 only).

**Definition** server.h:462

[http\_client\_ctx::content\_type](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4)

unsigned char content\_type[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN]

Request content type.

**Definition** server.h:459

[http\_client\_ctx::preface\_sent](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1)

bool preface\_sent

Flag indicating that HTTP2 preface was sent.

**Definition** server.h:494

[http\_client\_ctx::method](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15)

enum http\_method method

Request method.

**Definition** server.h:468

[http\_client\_ctx::fd](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5)

int fd

Socket descriptor associated with the server.

**Definition** server.h:411

[http\_client\_ctx::http1\_headers\_sent](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2)

bool http1\_headers\_sent

Flag indicating that HTTP1 headers were sent.

**Definition** server.h:497

[http\_client\_ctx::content\_len](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959)

size\_t content\_len

Request content length.

**Definition** server.h:465

[http\_client\_ctx::buffer](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63)

unsigned char buffer[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE]

Client data buffer.

**Definition** server.h:417

[http\_client\_ctx::current\_frame](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406)

struct http2\_frame current\_frame

Currently processed HTTP/2 frame.

**Definition** server.h:432

[http\_client\_ctx::current\_stream](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448)

struct http2\_stream\_ctx \* current\_stream

Currently processed stream.

**Definition** server.h:438

[http\_client\_ctx::websocket\_upgrade](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1)

bool websocket\_upgrade

Flag indicating Websocket upgrade takes place.

**Definition** server.h:506

[http\_client\_ctx::has\_upgrade\_header](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9)

bool has\_upgrade\_header

Flag indicating that upgrade header was present in the request.

**Definition** server.h:500

[http\_client\_ctx::service](structhttp__client__ctx.md#aea8cfd5353abc7b6bd50acde9d2c8c23)

const struct http\_service\_desc \* service

HTTP service on which the client is connected.

**Definition** server.h:414

[http\_client\_ctx::header\_capture\_ctx](structhttp__client__ctx.md#af278d2f02f617d49c54639a29317b758)

struct http\_header\_capture\_ctx header\_capture\_ctx

Header capture context.

**Definition** server.h:453

[http\_client\_ctx::IF\_ENABLED](structhttp__client__ctx.md#afc21ace1fba336e739eb4181e9b8d55e)

IF\_ENABLED(CONFIG\_HTTP\_SERVER\_COMPRESSION,(bool accept\_encoding\_next:1))

Flag indicating accept encoding is being processed.

[http\_client\_ctx::http2\_upgrade](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55)

bool http2\_upgrade

Flag indicating HTTP/2 upgrade takes place.

**Definition** server.h:503

[http\_client\_ctx::data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167)

size\_t data\_len

Data left to process in the buffer.

**Definition** server.h:423

[http\_content\_type](structhttp__content__type.md)

**Definition** server.h:156

[http\_content\_type::content\_type](structhttp__content__type.md#a78e378def414fd5d9ad9df45df9144fe)

const char \* content\_type

**Definition** server.h:159

[http\_content\_type::extension\_len](structhttp__content__type.md#a9235678c39a82386df70ad5efdcc33ab)

size\_t extension\_len

**Definition** server.h:158

[http\_content\_type::extension](structhttp__content__type.md#afe5cc6179e38766a3ee7a97a0e981cdd)

const char \* extension

**Definition** server.h:157

[http\_header\_name](structhttp__header__name.md)

HTTP header name representation.

**Definition** server.h:402

[http\_header\_name::name](structhttp__header__name.md#a643c7da4121fad12b0f25ea18fc709d0)

const char \* name

Pointer to header name NULL-terminated string.

**Definition** server.h:403

[http\_header](structhttp__header.md)

HTTP header representation.

**Definition** server.h:191

[http\_header::value](structhttp__header.md#acac6fa1c3ca33cd67119209dc981e5f9)

const char \* value

Pointer to header value NULL-terminated string.

**Definition** server.h:193

[http\_header::name](structhttp__header.md#afc8e4fa57f957f1fd34ce570c98537f5)

const char \* name

Pointer to header name NULL-terminated string.

**Definition** server.h:192

[http\_hpack\_header\_buf](structhttp__hpack__header__buf.md)

HTTP2 header field with decoding buffer.

**Definition** hpack.h:110

[http\_parser\_settings](structhttp__parser__settings.md)

**Definition** parser.h:200

[http\_parser](structhttp__parser.md)

**Definition** parser.h:155

[http\_request\_ctx](structhttp__request__ctx.md)

HTTP request context.

**Definition** server.h:197

[http\_request\_ctx::headers\_status](structhttp__request__ctx.md#a312cc4db494a0415a2c0342183b3a3c6)

enum http\_header\_status headers\_status

Status of HTTP request headers.

**Definition** server.h:202

[http\_request\_ctx::header\_count](structhttp__request__ctx.md#a404ff7f9946f162dc0ef6c0a872bf88b)

size\_t header\_count

Array length of HTTP request headers.

**Definition** server.h:201

[http\_request\_ctx::data\_len](structhttp__request__ctx.md#a4de5c3114220bef60bcd587f4796603e)

size\_t data\_len

Length of HTTP request data.

**Definition** server.h:199

[http\_request\_ctx::headers](structhttp__request__ctx.md#a9500727563dd6f33663c0a26299a16a6)

struct http\_header \* headers

Array of HTTP request headers.

**Definition** server.h:200

[http\_request\_ctx::data](structhttp__request__ctx.md#aae773946b597bb7ca70d071daadf3c1d)

uint8\_t \* data

HTTP request data.

**Definition** server.h:198

[http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md)

Representation of a dynamic server resource.

**Definition** server.h:238

[http\_resource\_detail\_dynamic::user\_data](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4)

void \* user\_data

A pointer to the user data registered by the application.

**Definition** server.h:253

[http\_resource\_detail\_dynamic::cb](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7)

http\_resource\_dynamic\_cb\_t cb

Resource callback used by the server to interact with the application.

**Definition** server.h:245

[http\_resource\_detail\_dynamic::holder](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856)

struct http\_client\_ctx \* holder

A pointer to the client currently processing resource, used to prevent concurrent access to the resou...

**Definition** server.h:250

[http\_resource\_detail\_dynamic::common](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:240

[http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md)

Representation of a static filesystem server resource.

**Definition** server.h:133

[http\_resource\_detail\_static\_fs::common](structhttp__resource__detail__static__fs.md#a3cb3f688d0070ad3316f33bc05a78f78)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:135

[http\_resource\_detail\_static\_fs::fs\_path](structhttp__resource__detail__static__fs.md#a5b25a03b953313b392096bab2faa3be8)

const char \* fs\_path

Path in the local filesystem.

**Definition** server.h:138

[http\_resource\_detail\_static](structhttp__resource__detail__static.md)

Representation of a static server resource.

**Definition** server.h:114

[http\_resource\_detail\_static::static\_data\_len](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484)

size\_t static\_data\_len

Size of the static resource.

**Definition** server.h:122

[http\_resource\_detail\_static::static\_data](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9)

const void \* static\_data

Content of the static resource.

**Definition** server.h:119

[http\_resource\_detail\_static::common](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:116

[http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md)

Representation of a websocket server resource.

**Definition** server.h:279

[http\_resource\_detail\_websocket::data\_buffer\_len](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117)

size\_t data\_buffer\_len

Length of the data in the data buffer.

**Definition** server.h:297

[http\_resource\_detail\_websocket::user\_data](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8)

void \* user\_data

A pointer to the user data registered by the application.

**Definition** server.h:300

[http\_resource\_detail\_websocket::common](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:281

[http\_resource\_detail\_websocket::cb](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0)

http\_resource\_websocket\_cb\_t cb

Resource callback used by the server to interact with the application.

**Definition** server.h:289

[http\_resource\_detail\_websocket::ws\_sock](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8)

int ws\_sock

Websocket socket value.

**Definition** server.h:284

[http\_resource\_detail\_websocket::data\_buffer](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c)

uint8\_t \* data\_buffer

Data buffer used to exchanged data between server and the, application.

**Definition** server.h:294

[http\_resource\_detail](structhttp__resource__detail.md)

Representation of a server resource, common for all resource types.

**Definition** server.h:88

[http\_resource\_detail::path\_len](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860)

int path\_len

Length of the URL path.

**Definition** server.h:96

[http\_resource\_detail::content\_type](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084)

const char \* content\_type

Content type of the resource.

**Definition** server.h:102

[http\_resource\_detail::bitmask\_of\_supported\_http\_methods](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817)

uint32\_t bitmask\_of\_supported\_http\_methods

Bitmask of supported HTTP methods (http\_method).

**Definition** server.h:90

[http\_resource\_detail::content\_encoding](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4)

const char \* content\_encoding

Content encoding of the resource.

**Definition** server.h:99

[http\_resource\_detail::type](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68)

enum http\_resource\_type type

Resource type.

**Definition** server.h:93

[http\_response\_ctx](structhttp__response__ctx.md)

HTTP response context.

**Definition** server.h:206

[http\_response\_ctx::final\_chunk](structhttp__response__ctx.md#a53162ff65b66567b31ec323558bc1fe2)

bool final\_chunk

Flag set to true when the application has no more data to send.

**Definition** server.h:212

[http\_response\_ctx::headers](structhttp__response__ctx.md#a63acf00d5ff891ab51107458c545399d)

const struct http\_header \* headers

Array of HTTP headers.

**Definition** server.h:208

[http\_response\_ctx::header\_count](structhttp__response__ctx.md#a7a7b446baf1a1ab343437ee527ddde95)

size\_t header\_count

Length of headers array.

**Definition** server.h:209

[http\_response\_ctx::body\_len](structhttp__response__ctx.md#a88b128e354c85f574409abd55633d2e2)

size\_t body\_len

Length of body data.

**Definition** server.h:211

[http\_response\_ctx::body](structhttp__response__ctx.md#aa027d1577dd19db43a17cdd0959b8e39)

const uint8\_t \* body

Pointer to body data.

**Definition** server.h:210

[http\_response\_ctx::status](structhttp__response__ctx.md#ada151e7a981885622a79a5ae1f12b2e9)

enum http\_status status

HTTP status code to include in response.

**Definition** server.h:207

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4101

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[NUM\_BITS](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)

#define NUM\_BITS(t)

Number of bits that make up a type.

**Definition** util.h:34

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [server.h](server_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
