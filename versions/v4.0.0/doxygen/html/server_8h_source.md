---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/server_8h_source.html
original_path: doxygen/html/server_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

52#define HTTP2\_PREFACE "PRI \* HTTP/2.0\r\n\r\nSM\r\n\r\n"

53

55

[ 59](group__http__server.md#ga23d0077fb99827b25491111bd74d00af)enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) {

[ 61](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) [HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248),

62

[ 64](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e) [HTTP\_RESOURCE\_TYPE\_STATIC\_FS](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e),

65

[ 69](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) [HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e),

70

[ 74](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866),

75};

76

[ 80](structhttp__resource__detail.md)struct [http\_resource\_detail](structhttp__resource__detail.md) {

[ 82](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bitmask\_of\_supported\_http\_methods](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817);

83

[ 85](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68) enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) [type](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68);

86

[ 88](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860) int [path\_len](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860);

89

[ 91](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4) const char \*[content\_encoding](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4);

92

[ 94](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084) const char \*[content\_type](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084);

95};

96

98BUILD\_ASSERT([NUM\_BITS](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)(

99 sizeof(((struct [http\_resource\_detail](structhttp__resource__detail.md) \*)0)->bitmask\_of\_supported\_http\_methods))

100 >= (HTTP\_METHOD\_END\_VALUE - 1));

102

[ 106](structhttp__resource__detail__static.md)struct [http\_resource\_detail\_static](structhttp__resource__detail__static.md) {

[ 108](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725);

109

[ 111](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9) const void \*[static\_data](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9);

112

[ 114](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484) size\_t [static\_data\_len](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484);

115};

116

118/\* Make sure that the common is the first in the struct. \*/

119BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_static](structhttp__resource__detail__static.md), common) == 0);

121

[ 125](structhttp__resource__detail__static__fs.md)struct [http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md) {

[ 127](structhttp__resource__detail__static__fs.md#a3cb3f688d0070ad3316f33bc05a78f78) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__static__fs.md#a3cb3f688d0070ad3316f33bc05a78f78);

128

[ 130](structhttp__resource__detail__static__fs.md#a5b25a03b953313b392096bab2faa3be8) const char \*[fs\_path](structhttp__resource__detail__static__fs.md#a5b25a03b953313b392096bab2faa3be8);

131};

132

134/\* Make sure that the common is the first in the struct. \*/

135BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md), common) == 0);

137

[ 138](structhttp__content__type.md)struct [http\_content\_type](structhttp__content__type.md) {

[ 139](structhttp__content__type.md#afe5cc6179e38766a3ee7a97a0e981cdd) const char \*[extension](structhttp__content__type.md#afe5cc6179e38766a3ee7a97a0e981cdd);

[ 140](structhttp__content__type.md#a9235678c39a82386df70ad5efdcc33ab) size\_t [extension\_len](structhttp__content__type.md#a9235678c39a82386df70ad5efdcc33ab);

[ 141](structhttp__content__type.md#a78e378def414fd5d9ad9df45df9144fe) const char \*[content\_type](structhttp__content__type.md#a78e378def414fd5d9ad9df45df9144fe);

142};

143

[ 144](group__http__server.md#ga709ddfe3f5ae5605b3399687f8be8c47)#define HTTP\_SERVER\_CONTENT\_TYPE(\_extension, \_content\_type) \

145 const STRUCT\_SECTION\_ITERABLE(http\_content\_type, \_extension) = { \

146 .extension = STRINGIFY(\_extension), \

147 .extension\_len = sizeof(STRINGIFY(\_extension)) - 1, \

148 .content\_type = \_content\_type, \

149 };

150

[ 151](group__http__server.md#gad1ee2e803d6e38d54c344180a45a25c2)#define HTTP\_SERVER\_CONTENT\_TYPE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_content\_type, \_it)

152

153struct [http\_client\_ctx](structhttp__client__ctx.md);

154

[ 156](group__http__server.md#ga496accfe23add03417bdc98369d32ea8)enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) {

[ 158](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) [HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1,

[ 160](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) [HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0,

[ 162](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) [HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1,

163};

164

[ 166](structhttp__header.md)struct [http\_header](structhttp__header.md) {

[ 167](structhttp__header.md#afc8e4fa57f957f1fd34ce570c98537f5) const char \*[name](structhttp__header.md#afc8e4fa57f957f1fd34ce570c98537f5);

[ 168](structhttp__header.md#acac6fa1c3ca33cd67119209dc981e5f9) const char \*[value](structhttp__header.md#acac6fa1c3ca33cd67119209dc981e5f9);

169};

170

[ 172](structhttp__response__ctx.md)struct [http\_response\_ctx](structhttp__response__ctx.md) {

[ 173](structhttp__response__ctx.md#ada151e7a981885622a79a5ae1f12b2e9) enum [http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d) [status](structhttp__response__ctx.md#ada151e7a981885622a79a5ae1f12b2e9);

[ 174](structhttp__response__ctx.md#a63acf00d5ff891ab51107458c545399d) const struct [http\_header](structhttp__header.md) \*[headers](structhttp__response__ctx.md#a63acf00d5ff891ab51107458c545399d);

[ 175](structhttp__response__ctx.md#a7a7b446baf1a1ab343437ee527ddde95) size\_t [header\_count](structhttp__response__ctx.md#a7a7b446baf1a1ab343437ee527ddde95);

[ 176](structhttp__response__ctx.md#aa027d1577dd19db43a17cdd0959b8e39) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[body](structhttp__response__ctx.md#aa027d1577dd19db43a17cdd0959b8e39);

[ 177](structhttp__response__ctx.md#a88b128e354c85f574409abd55633d2e2) size\_t [body\_len](structhttp__response__ctx.md#a88b128e354c85f574409abd55633d2e2);

[ 178](structhttp__response__ctx.md#a53162ff65b66567b31ec323558bc1fe2) bool [final\_chunk](structhttp__response__ctx.md#a53162ff65b66567b31ec323558bc1fe2);

179};

180

[ 198](group__http__server.md#ga5766e9b6ed0108e202a4615e5b0d8e33)typedef int (\*[http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5766e9b6ed0108e202a4615e5b0d8e33))(struct [http\_client\_ctx](structhttp__client__ctx.md) \*client,

199 enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) status,

200 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buffer,

201 size\_t [data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167),

202 struct [http\_response\_ctx](structhttp__response__ctx.md) \*response\_ctx,

203 void \*user\_data);

204

[ 208](structhttp__resource__detail__dynamic.md)struct [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md) {

[ 210](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab);

211

[ 215](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7) [http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5766e9b6ed0108e202a4615e5b0d8e33) [cb](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7);

216

[ 220](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856) struct [http\_client\_ctx](structhttp__client__ctx.md) \*[holder](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856);

221

[ 223](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4) void \*[user\_data](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4);

224};

225

227BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md), common) == 0);

229

[ 244](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c)typedef int (\*[http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c))(int ws\_socket,

245 void \*user\_data);

246

[ 248](structhttp__resource__detail__websocket.md)struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md) {

[ 250](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee);

251

[ 253](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8) int [ws\_sock](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8);

254

[ 258](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0) [http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c) [cb](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0);

259

[ 263](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_buffer](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c);

264

[ 266](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117) size\_t [data\_buffer\_len](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117);

267

[ 269](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8) void \*[user\_data](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8);

270};

271

273BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md), common) == 0);

275

277

278enum http2\_stream\_state {

279 HTTP2\_STREAM\_IDLE,

280 HTTP2\_STREAM\_RESERVED\_LOCAL,

281 HTTP2\_STREAM\_RESERVED\_REMOTE,

282 HTTP2\_STREAM\_OPEN,

283 HTTP2\_STREAM\_HALF\_CLOSED\_LOCAL,

284 HTTP2\_STREAM\_HALF\_CLOSED\_REMOTE,

285 HTTP2\_STREAM\_CLOSED

286};

287

288enum http\_server\_state {

289 HTTP\_SERVER\_FRAME\_HEADER\_STATE,

290 HTTP\_SERVER\_PREFACE\_STATE,

291 HTTP\_SERVER\_REQUEST\_STATE,

292 HTTP\_SERVER\_FRAME\_DATA\_STATE,

293 HTTP\_SERVER\_FRAME\_HEADERS\_STATE,

294 HTTP\_SERVER\_FRAME\_SETTINGS\_STATE,

295 HTTP\_SERVER\_FRAME\_PRIORITY\_STATE,

296 HTTP\_SERVER\_FRAME\_WINDOW\_UPDATE\_STATE,

297 HTTP\_SERVER\_FRAME\_CONTINUATION\_STATE,

298 HTTP\_SERVER\_FRAME\_PING\_STATE,

299 HTTP\_SERVER\_FRAME\_RST\_STREAM\_STATE,

300 HTTP\_SERVER\_FRAME\_GOAWAY\_STATE,

301 HTTP\_SERVER\_FRAME\_PADDING\_STATE,

302 HTTP\_SERVER\_DONE\_STATE,

303};

304

305enum http1\_parser\_state {

306 HTTP1\_INIT\_HEADER\_STATE,

307 HTTP1\_WAITING\_HEADER\_STATE,

308 HTTP1\_RECEIVING\_HEADER\_STATE,

309 HTTP1\_RECEIVED\_HEADER\_STATE,

310 HTTP1\_RECEIVING\_DATA\_STATE,

311 HTTP1\_MESSAGE\_COMPLETE\_STATE,

312};

313

314#define HTTP\_SERVER\_INITIAL\_WINDOW\_SIZE 65536

315#define HTTP\_SERVER\_WS\_MAX\_SEC\_KEY\_LEN 32

316

318

[ 320](structhttp2__stream__ctx.md)struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) {

[ 321](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7) int [stream\_id](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7);

[ 322](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa) enum http2\_stream\_state [stream\_state](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa);

[ 323](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279) int [window\_size](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279);

324

[ 326](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b) bool [headers\_sent](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b) : 1;

327

[ 329](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6) bool [end\_stream\_sent](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6) : 1;

330};

331

[ 333](structhttp2__frame.md)struct [http2\_frame](structhttp2__frame.md) {

[ 334](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [length](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a);

[ 335](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stream\_identifier](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543);

[ 336](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59);

[ 337](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c);

[ 338](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding\_len](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528);

339};

340

341#if defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS)

343enum http\_header\_status {

344 HTTP\_HEADER\_STATUS\_OK,

345 HTTP\_HEADER\_STATUS\_DROPPED,

346};

347

349struct http\_header\_capture\_ctx {

351 unsigned char buffer[CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADER\_BUFFER\_SIZE];

352

354 struct http\_header headers[CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADER\_COUNT];

355

357 enum http\_header\_status status;

358

360 size\_t count;

361

363 size\_t cursor;

364

366 bool store\_next\_value;

367};

368

370struct http\_header\_name {

371 const char \*name;

372};

373#endif /\* defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS) \*/

374

[ 378](structhttp__client__ctx.md)struct [http\_client\_ctx](structhttp__client__ctx.md) {

[ 380](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5) int [fd](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5);

381

[ 383](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63) unsigned char [buffer](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63)[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE];

384

[ 386](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376) unsigned char \*[cursor](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376);

387

[ 389](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167) size\_t [data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167);

390

[ 392](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d) int [window\_size](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d);

393

[ 395](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd) enum http\_server\_state [server\_state](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd);

396

[ 398](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406) struct [http2\_frame](structhttp2__frame.md) [current\_frame](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406);

399

[ 401](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314) struct [http\_resource\_detail](structhttp__resource__detail.md) \*[current\_detail](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314);

402

[ 404](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448) struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) \*[current\_stream](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448);

405

[ 407](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62) struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) [header\_field](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62);

408

[ 410](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138) struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) [streams](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138)[HTTP\_SERVER\_MAX\_STREAMS];

411

[ 413](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98) struct [http\_parser\_settings](structhttp__parser__settings.md) [parser\_settings](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98);

414

[ 416](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847) struct [http\_parser](structhttp__parser.md) [parser](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847);

417

418#if defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS)

420 struct http\_header\_capture\_ctx header\_capture\_ctx;

421#endif /\* defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS) \*/

422

[ 424](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1) unsigned char [url\_buffer](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1)[HTTP\_SERVER\_MAX\_URL\_LENGTH];

425

[ 427](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4) unsigned char [content\_type](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4)[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN];

428

[ 430](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5) unsigned char [header\_buffer](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5)[HTTP\_SERVER\_MAX\_HEADER\_LEN];

431

[ 433](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959) size\_t [content\_len](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959);

434

[ 436](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15) enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) [method](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15);

437

[ 439](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0) enum http1\_parser\_state [parser\_state](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0);

440

[ 444](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49) int [http1\_frag\_data\_len](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49);

445

[ 449](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac) struct [k\_work\_delayable](structk__work__delayable.md) [inactivity\_timer](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac);

450

453 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_WEBSOCKET, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ws\_sec\_key[HTTP\_SERVER\_WS\_MAX\_SEC\_KEY\_LEN]));

455

[ 457](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1) bool [preface\_sent](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1) : 1;

458

[ 460](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2) bool [http1\_headers\_sent](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2) : 1;

461

[ 463](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9) bool [has\_upgrade\_header](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9) : 1;

464

[ 466](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55) bool [http2\_upgrade](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55) : 1;

467

[ 469](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1) bool [websocket\_upgrade](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1) : 1;

470

[ 472](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6) bool [websocket\_sec\_key\_next](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6) : 1;

473

[ 475](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620) bool [expect\_continuation](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620) : 1;

476};

477

478#if defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS)

485#define HTTP\_SERVER\_REGISTER\_HEADER\_CAPTURE(\_id, \_header) \

486 BUILD\_ASSERT(sizeof(\_header) <= CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN, \

487 "Header is too long to be captured, try increasing " \

488 "CONFIG\_HTTP\_SERVER\_MAX\_HEADER\_LEN"); \

489 static const char \*const \_id##\_str = \_header; \

490 static const STRUCT\_SECTION\_ITERABLE(http\_header\_name, \_id) = { \

491 .name = \_id##\_str, \

492 }

493#endif /\* defined(CONFIG\_HTTP\_SERVER\_CAPTURE\_HEADERS) \*/

494

[ 501](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)int [http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)(void);

502

[ 507](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)int [http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)(void);

508

509#ifdef \_\_cplusplus

510}

511#endif

512

516

517#endif

[http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

http\_method

HTTP Request Methods.

**Definition** method.h:28

[http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af)

http\_resource\_type

HTTP server resource type.

**Definition** server.h:59

[http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8)

http\_data\_status

Indicates the status of the currently processed piece of data.

**Definition** server.h:156

[http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5766e9b6ed0108e202a4615e5b0d8e33)

int(\* http\_resource\_dynamic\_cb\_t)(struct http\_client\_ctx \*client, enum http\_data\_status status, uint8\_t \*data\_buffer, size\_t data\_len, struct http\_response\_ctx \*response\_ctx, void \*user\_data)

Callback used when data is received.

**Definition** server.h:198

[http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c)

int(\* http\_resource\_websocket\_cb\_t)(int ws\_socket, void \*user\_data)

Callback used when a Websocket connection is setup.

**Definition** server.h:244

[http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)

int http\_server\_stop(void)

Stop the HTTP2 server.

[http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)

int http\_server\_start(void)

Start the HTTP2 server.

[HTTP\_RESOURCE\_TYPE\_STATIC\_FS](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa05a9e5c3c4c1cce4894e6250220fea6e)

@ HTTP\_RESOURCE\_TYPE\_STATIC\_FS

serves static gzipped files from a filesystem

**Definition** server.h:64

[HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)

@ HTTP\_RESOURCE\_TYPE\_STATIC

Static resource, cannot be modified on runtime.

**Definition** server.h:61

[HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)

@ HTTP\_RESOURCE\_TYPE\_WEBSOCKET

Websocket resource, application takes control over Websocket connection after and upgrade.

**Definition** server.h:74

[HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)

@ HTTP\_RESOURCE\_TYPE\_DYNAMIC

Dynamic resource, server interacts with the application via registered http\_resource\_dynamic\_cb\_t.

**Definition** server.h:69

[HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a)

@ HTTP\_SERVER\_DATA\_FINAL

Final data fragment in current transaction.

**Definition** server.h:162

[HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231)

@ HTTP\_SERVER\_DATA\_MORE

Transaction incomplete, more data expected.

**Definition** server.h:160

[HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc)

@ HTTP\_SERVER\_DATA\_ABORTED

Transaction aborted, data incomplete.

**Definition** server.h:158

[http\_status](group__http__status__codes.md#gabc3b93f68c8bdd857ad32913628dfa8d)

http\_status

HTTP response status codes.

**Definition** status.h:36

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:239

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

**Definition** server.h:333

[http2\_frame::stream\_identifier](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543)

uint32\_t stream\_identifier

Stream ID the frame belongs to.

**Definition** server.h:335

[http2\_frame::type](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59)

uint8\_t type

Frame type.

**Definition** server.h:336

[http2\_frame::flags](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c)

uint8\_t flags

Frame flags.

**Definition** server.h:337

[http2\_frame::padding\_len](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528)

uint8\_t padding\_len

Frame padding length.

**Definition** server.h:338

[http2\_frame::length](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a)

uint32\_t length

Frame payload length.

**Definition** server.h:334

[http2\_stream\_ctx](structhttp2__stream__ctx.md)

HTTP/2 stream representation.

**Definition** server.h:320

[http2\_stream\_ctx::headers\_sent](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b)

bool headers\_sent

Flag indicating that headers were sent in the reply.

**Definition** server.h:326

[http2\_stream\_ctx::stream\_state](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa)

enum http2\_stream\_state stream\_state

Stream state.

**Definition** server.h:322

[http2\_stream\_ctx::window\_size](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279)

int window\_size

Stream-level window size.

**Definition** server.h:323

[http2\_stream\_ctx::stream\_id](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7)

int stream\_id

Stream identifier.

**Definition** server.h:321

[http2\_stream\_ctx::end\_stream\_sent](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6)

bool end\_stream\_sent

Flag indicating that END\_STREAM flag was sent.

**Definition** server.h:329

[http\_client\_ctx](structhttp__client__ctx.md)

Representation of an HTTP client connected to the server.

**Definition** server.h:378

[http\_client\_ctx::streams](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138)

struct http2\_stream\_ctx streams[HTTP\_SERVER\_MAX\_STREAMS]

HTTP/2 streams context.

**Definition** server.h:410

[http\_client\_ctx::inactivity\_timer](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac)

struct k\_work\_delayable inactivity\_timer

Client inactivity timer.

**Definition** server.h:449

[http\_client\_ctx::parser\_settings](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98)

struct http\_parser\_settings parser\_settings

HTTP/1 parser configuration.

**Definition** server.h:413

[http\_client\_ctx::cursor](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376)

unsigned char \* cursor

Cursor indicating currently processed byte.

**Definition** server.h:386

[http\_client\_ctx::window\_size](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d)

int window\_size

Connection-level window size.

**Definition** server.h:392

[http\_client\_ctx::parser\_state](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0)

enum http1\_parser\_state parser\_state

HTTP/1 parser state.

**Definition** server.h:439

[http\_client\_ctx::expect\_continuation](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620)

bool expect\_continuation

The next frame on the stream is expectd to be a continuation frame.

**Definition** server.h:475

[http\_client\_ctx::parser](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847)

struct http\_parser parser

HTTP/1 parser context.

**Definition** server.h:416

[http\_client\_ctx::http1\_frag\_data\_len](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49)

int http1\_frag\_data\_len

Length of the payload length in the currently processed request fragment (HTTP/1 only).

**Definition** server.h:444

[http\_client\_ctx::websocket\_sec\_key\_next](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6)

bool websocket\_sec\_key\_next

Flag indicating Websocket key is being processed.

**Definition** server.h:472

[http\_client\_ctx::server\_state](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd)

enum http\_server\_state server\_state

Server state for the associated client.

**Definition** server.h:395

[http\_client\_ctx::header\_field](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62)

struct http\_hpack\_header\_buf header\_field

HTTP/2 header parser context.

**Definition** server.h:407

[http\_client\_ctx::current\_detail](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314)

struct http\_resource\_detail \* current\_detail

Currently processed resource detail.

**Definition** server.h:401

[http\_client\_ctx::url\_buffer](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1)

unsigned char url\_buffer[HTTP\_SERVER\_MAX\_URL\_LENGTH]

Request URL.

**Definition** server.h:424

[http\_client\_ctx::header\_buffer](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5)

unsigned char header\_buffer[HTTP\_SERVER\_MAX\_HEADER\_LEN]

Temp buffer for currently processed header (HTTP/1 only).

**Definition** server.h:430

[http\_client\_ctx::content\_type](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4)

unsigned char content\_type[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN]

Request content type.

**Definition** server.h:427

[http\_client\_ctx::preface\_sent](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1)

bool preface\_sent

Flag indicating that HTTP2 preface was sent.

**Definition** server.h:457

[http\_client\_ctx::method](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15)

enum http\_method method

Request method.

**Definition** server.h:436

[http\_client\_ctx::fd](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5)

int fd

Socket descriptor associated with the server.

**Definition** server.h:380

[http\_client\_ctx::http1\_headers\_sent](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2)

bool http1\_headers\_sent

Flag indicating that HTTP1 headers were sent.

**Definition** server.h:460

[http\_client\_ctx::content\_len](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959)

size\_t content\_len

Request content length.

**Definition** server.h:433

[http\_client\_ctx::buffer](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63)

unsigned char buffer[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE]

Client data buffer.

**Definition** server.h:383

[http\_client\_ctx::current\_frame](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406)

struct http2\_frame current\_frame

Currently processed HTTP/2 frame.

**Definition** server.h:398

[http\_client\_ctx::current\_stream](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448)

struct http2\_stream\_ctx \* current\_stream

Currently processed stream.

**Definition** server.h:404

[http\_client\_ctx::websocket\_upgrade](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1)

bool websocket\_upgrade

Flag indicating Websocket upgrade takes place.

**Definition** server.h:469

[http\_client\_ctx::has\_upgrade\_header](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9)

bool has\_upgrade\_header

Flag indicating that upgrade header was present in the request.

**Definition** server.h:463

[http\_client\_ctx::http2\_upgrade](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55)

bool http2\_upgrade

Flag indicating HTTP/2 upgrade takes place.

**Definition** server.h:466

[http\_client\_ctx::data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167)

size\_t data\_len

Data left to process in the buffer.

**Definition** server.h:389

[http\_content\_type](structhttp__content__type.md)

**Definition** server.h:138

[http\_content\_type::content\_type](structhttp__content__type.md#a78e378def414fd5d9ad9df45df9144fe)

const char \* content\_type

**Definition** server.h:141

[http\_content\_type::extension\_len](structhttp__content__type.md#a9235678c39a82386df70ad5efdcc33ab)

size\_t extension\_len

**Definition** server.h:140

[http\_content\_type::extension](structhttp__content__type.md#afe5cc6179e38766a3ee7a97a0e981cdd)

const char \* extension

**Definition** server.h:139

[http\_header](structhttp__header.md)

HTTP header representation.

**Definition** server.h:166

[http\_header::value](structhttp__header.md#acac6fa1c3ca33cd67119209dc981e5f9)

const char \* value

Pointer to header value NULL-terminated string.

**Definition** server.h:168

[http\_header::name](structhttp__header.md#afc8e4fa57f957f1fd34ce570c98537f5)

const char \* name

Pointer to header name NULL-terminated string.

**Definition** server.h:167

[http\_hpack\_header\_buf](structhttp__hpack__header__buf.md)

HTTP2 header field with decoding buffer.

**Definition** hpack.h:110

[http\_parser\_settings](structhttp__parser__settings.md)

**Definition** parser.h:190

[http\_parser](structhttp__parser.md)

**Definition** parser.h:147

[http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md)

Representation of a dynamic server resource.

**Definition** server.h:208

[http\_resource\_detail\_dynamic::user\_data](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4)

void \* user\_data

A pointer to the user data registered by the application.

**Definition** server.h:223

[http\_resource\_detail\_dynamic::cb](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7)

http\_resource\_dynamic\_cb\_t cb

Resource callback used by the server to interact with the application.

**Definition** server.h:215

[http\_resource\_detail\_dynamic::holder](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856)

struct http\_client\_ctx \* holder

A pointer to the client currently processing resource, used to prevent concurrent access to the resou...

**Definition** server.h:220

[http\_resource\_detail\_dynamic::common](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:210

[http\_resource\_detail\_static\_fs](structhttp__resource__detail__static__fs.md)

Representation of a static filesystem server resource.

**Definition** server.h:125

[http\_resource\_detail\_static\_fs::common](structhttp__resource__detail__static__fs.md#a3cb3f688d0070ad3316f33bc05a78f78)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:127

[http\_resource\_detail\_static\_fs::fs\_path](structhttp__resource__detail__static__fs.md#a5b25a03b953313b392096bab2faa3be8)

const char \* fs\_path

Path in the local filesystem.

**Definition** server.h:130

[http\_resource\_detail\_static](structhttp__resource__detail__static.md)

Representation of a static server resource.

**Definition** server.h:106

[http\_resource\_detail\_static::static\_data\_len](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484)

size\_t static\_data\_len

Size of the static resource.

**Definition** server.h:114

[http\_resource\_detail\_static::static\_data](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9)

const void \* static\_data

Content of the static resource.

**Definition** server.h:111

[http\_resource\_detail\_static::common](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:108

[http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md)

Representation of a websocket server resource.

**Definition** server.h:248

[http\_resource\_detail\_websocket::data\_buffer\_len](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117)

size\_t data\_buffer\_len

Length of the data in the data buffer.

**Definition** server.h:266

[http\_resource\_detail\_websocket::user\_data](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8)

void \* user\_data

A pointer to the user data registered by the application.

**Definition** server.h:269

[http\_resource\_detail\_websocket::common](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:250

[http\_resource\_detail\_websocket::cb](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0)

http\_resource\_websocket\_cb\_t cb

Resource callback used by the server to interact with the application.

**Definition** server.h:258

[http\_resource\_detail\_websocket::ws\_sock](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8)

int ws\_sock

Websocket socket value.

**Definition** server.h:253

[http\_resource\_detail\_websocket::data\_buffer](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c)

uint8\_t \* data\_buffer

Data buffer used to exchanged data between server and the, application.

**Definition** server.h:263

[http\_resource\_detail](structhttp__resource__detail.md)

Representation of a server resource, common for all resource types.

**Definition** server.h:80

[http\_resource\_detail::path\_len](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860)

int path\_len

Length of the URL path.

**Definition** server.h:88

[http\_resource\_detail::content\_type](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084)

const char \* content\_type

Content type of the resource.

**Definition** server.h:94

[http\_resource\_detail::bitmask\_of\_supported\_http\_methods](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817)

uint32\_t bitmask\_of\_supported\_http\_methods

Bitmask of supported HTTP methods (http\_method).

**Definition** server.h:82

[http\_resource\_detail::content\_encoding](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4)

const char \* content\_encoding

Content encoding of the resource.

**Definition** server.h:91

[http\_resource\_detail::type](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68)

enum http\_resource\_type type

Resource type.

**Definition** server.h:85

[http\_response\_ctx](structhttp__response__ctx.md)

HTTP response context.

**Definition** server.h:172

[http\_response\_ctx::final\_chunk](structhttp__response__ctx.md#a53162ff65b66567b31ec323558bc1fe2)

bool final\_chunk

Length of body data.

**Definition** server.h:178

[http\_response\_ctx::headers](structhttp__response__ctx.md#a63acf00d5ff891ab51107458c545399d)

const struct http\_header \* headers

HTTP status code to include in response.

**Definition** server.h:174

[http\_response\_ctx::header\_count](structhttp__response__ctx.md#a7a7b446baf1a1ab343437ee527ddde95)

size\_t header\_count

Array of HTTP headers.

**Definition** server.h:175

[http\_response\_ctx::body\_len](structhttp__response__ctx.md#a88b128e354c85f574409abd55633d2e2)

size\_t body\_len

Pointer to body data.

**Definition** server.h:177

[http\_response\_ctx::body](structhttp__response__ctx.md#aa027d1577dd19db43a17cdd0959b8e39)

const uint8\_t \* body

Length of headers array.

**Definition** server.h:176

[http\_response\_ctx::status](structhttp__response__ctx.md#ada151e7a981885622a79a5ae1f12b2e9)

enum http\_status status

**Definition** server.h:173

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[NUM\_BITS](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)

#define NUM\_BITS(t)

Number of bits that make up a type.

**Definition** util.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [server.h](server_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
