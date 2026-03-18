---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/server_8h_source.html
original_path: doxygen/html/server_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

20

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/net/http/parser.h](parser_8h.md)>

25#include <[zephyr/net/http/hpack.h](hpack_8h.md)>

26#include <[zephyr/net/socket.h](net_2socket_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

33

34#if defined(CONFIG\_HTTP\_SERVER)

35#define HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE CONFIG\_HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE

36#define HTTP\_SERVER\_MAX\_STREAMS CONFIG\_HTTP\_SERVER\_MAX\_STREAMS

37#define HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN CONFIG\_HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LENGTH

38#define HTTP\_SERVER\_MAX\_URL\_LENGTH CONFIG\_HTTP\_SERVER\_MAX\_URL\_LENGTH

39#else

40#define HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE 0

41#define HTTP\_SERVER\_MAX\_STREAMS 0

42#define HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN 0

43#define HTTP\_SERVER\_MAX\_URL\_LENGTH 0

44#endif

45

46/\* Maximum header field name / value length. This is only used to detect Upgrade and

47 \* websocket header fields and values in the http1 server so the value is quite short.

48 \*/

49#define HTTP\_SERVER\_MAX\_HEADER\_LEN 32

50

51#define HTTP2\_PREFACE "PRI \* HTTP/2.0\r\n\r\nSM\r\n\r\n"

52

54

[ 58](group__http__server.md#ga23d0077fb99827b25491111bd74d00af)enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) {

[ 60](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248) [HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248),

61

[ 65](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e) [HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e),

66

[ 70](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866) [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866),

71};

72

[ 76](structhttp__resource__detail.md)struct [http\_resource\_detail](structhttp__resource__detail.md) {

[ 78](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bitmask\_of\_supported\_http\_methods](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817);

79

[ 81](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68) enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) [type](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68);

82

[ 84](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860) int [path\_len](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860);

85

[ 87](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4) const char \*[content\_encoding](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4);

88

[ 90](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084) const char \*[content\_type](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084);

91};

92

94BUILD\_ASSERT([NUM\_BITS](util_8h.md#afa27c06d0ad6b949289431ad75f104ab)(

95 sizeof(((struct [http\_resource\_detail](structhttp__resource__detail.md) \*)0)->bitmask\_of\_supported\_http\_methods))

96 >= (HTTP\_METHOD\_END\_VALUE - 1));

98

[ 102](structhttp__resource__detail__static.md)struct [http\_resource\_detail\_static](structhttp__resource__detail__static.md) {

[ 104](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725);

105

[ 107](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9) const void \*[static\_data](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9);

108

[ 110](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484) size\_t [static\_data\_len](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484);

111};

112

114/\* Make sure that the common is the first in the struct. \*/

115BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_static](structhttp__resource__detail__static.md), common) == 0);

117

118struct [http\_client\_ctx](structhttp__client__ctx.md);

119

[ 121](group__http__server.md#ga496accfe23add03417bdc98369d32ea8)enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) {

[ 123](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) [HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc) = -1,

[ 125](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) [HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231) = 0,

[ 127](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) [HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a) = 1,

128};

129

[ 146](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2)typedef int (\*[http\_resource\_dynamic\_cb\_t](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2))(struct [http\_client\_ctx](structhttp__client__ctx.md) \*client,

147 enum [http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8) status,

148 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buffer,

149 size\_t [data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167),

150 void \*user\_data);

151

[ 155](structhttp__resource__detail__dynamic.md)struct [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md) {

[ 157](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab);

158

[ 162](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7) [http\_resource\_dynamic\_cb\_t](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2) [cb](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7);

163

[ 167](structhttp__resource__detail__dynamic.md#a42d25c2ca98ad617b7bddfa3669abbb6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_buffer](structhttp__resource__detail__dynamic.md#a42d25c2ca98ad617b7bddfa3669abbb6);

168

[ 170](structhttp__resource__detail__dynamic.md#a75cbd941e330017ca2243087d4770f76) size\_t [data\_buffer\_len](structhttp__resource__detail__dynamic.md#a75cbd941e330017ca2243087d4770f76);

171

[ 175](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856) struct [http\_client\_ctx](structhttp__client__ctx.md) \*[holder](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856);

176

[ 178](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4) void \*[user\_data](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4);

179};

180

182BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md), common) == 0);

184

[ 199](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c)typedef int (\*[http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c))(int ws\_socket,

200 void \*user\_data);

201

[ 203](structhttp__resource__detail__websocket.md)struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md) {

[ 205](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee) struct [http\_resource\_detail](structhttp__resource__detail.md) [common](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee);

206

[ 208](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8) int [ws\_sock](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8);

209

[ 213](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0) [http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c) [cb](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0);

214

[ 218](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_buffer](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c);

219

[ 221](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117) size\_t [data\_buffer\_len](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117);

222

[ 224](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8) void \*[user\_data](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8);

225};

226

228BUILD\_ASSERT(offsetof(struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md), common) == 0);

230

232

233enum http2\_stream\_state {

234 HTTP2\_STREAM\_IDLE,

235 HTTP2\_STREAM\_RESERVED\_LOCAL,

236 HTTP2\_STREAM\_RESERVED\_REMOTE,

237 HTTP2\_STREAM\_OPEN,

238 HTTP2\_STREAM\_HALF\_CLOSED\_LOCAL,

239 HTTP2\_STREAM\_HALF\_CLOSED\_REMOTE,

240 HTTP2\_STREAM\_CLOSED

241};

242

243enum http\_server\_state {

244 HTTP\_SERVER\_FRAME\_HEADER\_STATE,

245 HTTP\_SERVER\_PREFACE\_STATE,

246 HTTP\_SERVER\_REQUEST\_STATE,

247 HTTP\_SERVER\_FRAME\_DATA\_STATE,

248 HTTP\_SERVER\_FRAME\_HEADERS\_STATE,

249 HTTP\_SERVER\_FRAME\_SETTINGS\_STATE,

250 HTTP\_SERVER\_FRAME\_PRIORITY\_STATE,

251 HTTP\_SERVER\_FRAME\_WINDOW\_UPDATE\_STATE,

252 HTTP\_SERVER\_FRAME\_CONTINUATION\_STATE,

253 HTTP\_SERVER\_FRAME\_PING\_STATE,

254 HTTP\_SERVER\_FRAME\_RST\_STREAM\_STATE,

255 HTTP\_SERVER\_FRAME\_GOAWAY\_STATE,

256 HTTP\_SERVER\_FRAME\_PADDING\_STATE,

257 HTTP\_SERVER\_DONE\_STATE,

258};

259

260enum http1\_parser\_state {

261 HTTP1\_INIT\_HEADER\_STATE,

262 HTTP1\_WAITING\_HEADER\_STATE,

263 HTTP1\_RECEIVING\_HEADER\_STATE,

264 HTTP1\_RECEIVED\_HEADER\_STATE,

265 HTTP1\_RECEIVING\_DATA\_STATE,

266 HTTP1\_MESSAGE\_COMPLETE\_STATE,

267};

268

269#define HTTP\_SERVER\_INITIAL\_WINDOW\_SIZE 65536

270#define HTTP\_SERVER\_WS\_MAX\_SEC\_KEY\_LEN 32

271

273

[ 275](structhttp2__stream__ctx.md)struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) {

[ 276](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7) int [stream\_id](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7);

[ 277](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa) enum http2\_stream\_state [stream\_state](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa);

[ 278](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279) int [window\_size](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279);

279

[ 281](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b) bool [headers\_sent](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b) : 1;

282

[ 284](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6) bool [end\_stream\_sent](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6) : 1;

285};

286

[ 288](structhttp2__frame.md)struct [http2\_frame](structhttp2__frame.md) {

[ 289](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [length](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a);

[ 290](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stream\_identifier](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543);

[ 291](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59);

[ 292](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c);

[ 293](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding\_len](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528);

294};

295

[ 299](structhttp__client__ctx.md)struct [http\_client\_ctx](structhttp__client__ctx.md) {

[ 301](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5) int [fd](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5);

302

[ 304](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63) unsigned char [buffer](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63)[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE];

305

[ 307](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376) unsigned char \*[cursor](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376);

308

[ 310](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167) size\_t [data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167);

311

[ 313](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d) int [window\_size](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d);

314

[ 316](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd) enum http\_server\_state [server\_state](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd);

317

[ 319](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406) struct [http2\_frame](structhttp2__frame.md) [current\_frame](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406);

320

[ 322](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314) struct [http\_resource\_detail](structhttp__resource__detail.md) \*[current\_detail](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314);

323

[ 325](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448) struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) \*[current\_stream](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448);

326

[ 328](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62) struct [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md) [header\_field](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62);

329

[ 331](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138) struct [http2\_stream\_ctx](structhttp2__stream__ctx.md) [streams](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138)[HTTP\_SERVER\_MAX\_STREAMS];

332

[ 334](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98) struct [http\_parser\_settings](structhttp__parser__settings.md) [parser\_settings](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98);

335

[ 337](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847) struct [http\_parser](structhttp__parser.md) [parser](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847);

338

[ 340](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1) unsigned char [url\_buffer](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1)[HTTP\_SERVER\_MAX\_URL\_LENGTH];

341

[ 343](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4) unsigned char [content\_type](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4)[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN];

344

[ 346](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5) unsigned char [header\_buffer](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5)[HTTP\_SERVER\_MAX\_HEADER\_LEN];

347

[ 349](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959) size\_t [content\_len](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959);

350

[ 352](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15) enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) [method](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15);

353

[ 355](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0) enum http1\_parser\_state [parser\_state](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0);

356

[ 360](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49) int [http1\_frag\_data\_len](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49);

361

[ 365](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac) struct [k\_work\_delayable](structk__work__delayable.md) [inactivity\_timer](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac);

366

369 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_WEBSOCKET, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ws\_sec\_key[HTTP\_SERVER\_WS\_MAX\_SEC\_KEY\_LEN]));

371

[ 373](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1) bool [preface\_sent](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1) : 1;

374

[ 376](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2) bool [http1\_headers\_sent](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2) : 1;

377

[ 379](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9) bool [has\_upgrade\_header](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9) : 1;

380

[ 382](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55) bool [http2\_upgrade](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55) : 1;

383

[ 385](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1) bool [websocket\_upgrade](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1) : 1;

386

[ 388](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6) bool [websocket\_sec\_key\_next](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6) : 1;

389

[ 391](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620) bool [expect\_continuation](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620) : 1;

392};

393

[ 400](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)int [http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)(void);

401

[ 406](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)int [http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)(void);

407

408#ifdef \_\_cplusplus

409}

410#endif

411

415

416#endif

[http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

http\_method

HTTP Request Methods.

**Definition** method.h:26

[http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af)

http\_resource\_type

HTTP server resource type.

**Definition** server.h:58

[http\_data\_status](group__http__server.md#ga496accfe23add03417bdc98369d32ea8)

http\_data\_status

Indicates the status of the currently processed piece of data.

**Definition** server.h:121

[http\_resource\_websocket\_cb\_t](group__http__server.md#ga5846da152b7734dedfe4b1c026349c2c)

int(\* http\_resource\_websocket\_cb\_t)(int ws\_socket, void \*user\_data)

Callback used when a Websocket connection is setup.

**Definition** server.h:199

[http\_server\_stop](group__http__server.md#ga79f434b5bbc6d2a6ebc65a0c560730cf)

int http\_server\_stop(void)

Stop the HTTP2 server.

[http\_server\_start](group__http__server.md#ga8125ef45732f81ec1c629a8f41e4c14d)

int http\_server\_start(void)

Start the HTTP2 server.

[http\_resource\_dynamic\_cb\_t](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2)

int(\* http\_resource\_dynamic\_cb\_t)(struct http\_client\_ctx \*client, enum http\_data\_status status, uint8\_t \*data\_buffer, size\_t data\_len, void \*user\_data)

Callback used when data is received.

**Definition** server.h:146

[HTTP\_RESOURCE\_TYPE\_STATIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa1170c8c886888c5c0c5dcdc6c593a248)

@ HTTP\_RESOURCE\_TYPE\_STATIC

Static resource, cannot be modified on runtime.

**Definition** server.h:60

[HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)

@ HTTP\_RESOURCE\_TYPE\_WEBSOCKET

Websocket resource, application takes control over Websocket connection after and upgrade.

**Definition** server.h:70

[HTTP\_RESOURCE\_TYPE\_DYNAMIC](group__http__server.md#gga23d0077fb99827b25491111bd74d00afae9cdb0e1f8861de769a570399484587e)

@ HTTP\_RESOURCE\_TYPE\_DYNAMIC

Dynamic resource, server interacts with the application via registered http\_resource\_dynamic\_cb\_t.

**Definition** server.h:65

[HTTP\_SERVER\_DATA\_FINAL](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a0f462355aede2440403f907d0c6af45a)

@ HTTP\_SERVER\_DATA\_FINAL

Final data fragment in current transaction.

**Definition** server.h:127

[HTTP\_SERVER\_DATA\_MORE](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a3827f7f5876ef09332845b445cd65231)

@ HTTP\_SERVER\_DATA\_MORE

Transaction incomplete, more data expected.

**Definition** server.h:125

[HTTP\_SERVER\_DATA\_ABORTED](group__http__server.md#gga496accfe23add03417bdc98369d32ea8a85682febe2a08e3fe23eaa9b178db5dc)

@ HTTP\_SERVER\_DATA\_ABORTED

Transaction aborted, data incomplete.

**Definition** server.h:123

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:223

[hpack.h](hpack_8h.md)

HTTP HPACK.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[parser.h](parser_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[http2\_frame](structhttp2__frame.md)

HTTP/2 frame representation.

**Definition** server.h:288

[http2\_frame::stream\_identifier](structhttp2__frame.md#a0dfc83689ba3bdefe7bd27ab21bcd543)

uint32\_t stream\_identifier

Stream ID the frame belongs to.

**Definition** server.h:290

[http2\_frame::type](structhttp2__frame.md#a40d75871da54ad54c7e0038cb03afe59)

uint8\_t type

Frame type.

**Definition** server.h:291

[http2\_frame::flags](structhttp2__frame.md#a6d7bbf365456cba136bb523f513c515c)

uint8\_t flags

Frame flags.

**Definition** server.h:292

[http2\_frame::padding\_len](structhttp2__frame.md#aa2124f60dc9ab2b692359fac07002528)

uint8\_t padding\_len

Frame padding length.

**Definition** server.h:293

[http2\_frame::length](structhttp2__frame.md#ab626f6cca2d5a92ba8c6bbc24828b84a)

uint32\_t length

Frame payload length.

**Definition** server.h:289

[http2\_stream\_ctx](structhttp2__stream__ctx.md)

HTTP/2 stream representation.

**Definition** server.h:275

[http2\_stream\_ctx::headers\_sent](structhttp2__stream__ctx.md#a4b8cc2fa54a3c8161a8085bf4ec8d70b)

bool headers\_sent

Flag indicating that headers were sent in the reply.

**Definition** server.h:281

[http2\_stream\_ctx::stream\_state](structhttp2__stream__ctx.md#a61a05b72b578b1bae6806fc6ad125caa)

enum http2\_stream\_state stream\_state

Stream state.

**Definition** server.h:277

[http2\_stream\_ctx::window\_size](structhttp2__stream__ctx.md#a96a3a7ebdede35b4e925116c4d784279)

int window\_size

Stream-level window size.

**Definition** server.h:278

[http2\_stream\_ctx::stream\_id](structhttp2__stream__ctx.md#ad1b194318758f888b8218b0fd056dca7)

int stream\_id

Stream identifier.

**Definition** server.h:276

[http2\_stream\_ctx::end\_stream\_sent](structhttp2__stream__ctx.md#af94d72e8ed02699cefc08d92e58825b6)

bool end\_stream\_sent

Flag indicating that END\_STREAM flag was sent.

**Definition** server.h:284

[http\_client\_ctx](structhttp__client__ctx.md)

Representation of an HTTP client connected to the server.

**Definition** server.h:299

[http\_client\_ctx::streams](structhttp__client__ctx.md#a0695be4e93cb09472692dfc2f2e9a138)

struct http2\_stream\_ctx streams[HTTP\_SERVER\_MAX\_STREAMS]

HTTP/2 streams context.

**Definition** server.h:331

[http\_client\_ctx::inactivity\_timer](structhttp__client__ctx.md#a0c4c06035d6de735b15d8a3ce6694eac)

struct k\_work\_delayable inactivity\_timer

Client inactivity timer.

**Definition** server.h:365

[http\_client\_ctx::parser\_settings](structhttp__client__ctx.md#a1d18988c23f3207d8fcdc1f0fff8bc98)

struct http\_parser\_settings parser\_settings

HTTP/1 parser configuration.

**Definition** server.h:334

[http\_client\_ctx::cursor](structhttp__client__ctx.md#a27b7c773f250aaeff9cdcd5dab063376)

unsigned char \* cursor

Cursor indicating currently processed byte.

**Definition** server.h:307

[http\_client\_ctx::window\_size](structhttp__client__ctx.md#a35e9a23972eb02fabe6c62333bd11f0d)

int window\_size

Connection-level window size.

**Definition** server.h:313

[http\_client\_ctx::parser\_state](structhttp__client__ctx.md#a4486489bf6043c98aac83a2ff33d1bc0)

enum http1\_parser\_state parser\_state

HTTP/1 parser state.

**Definition** server.h:355

[http\_client\_ctx::expect\_continuation](structhttp__client__ctx.md#a4ae7f83d0e28944a2bcc858d096cb620)

bool expect\_continuation

The next frame on the stream is expectd to be a continuation frame.

**Definition** server.h:391

[http\_client\_ctx::parser](structhttp__client__ctx.md#a4d91f65c886527e68c1251b7eb0f3847)

struct http\_parser parser

HTTP/1 parser context.

**Definition** server.h:337

[http\_client\_ctx::http1\_frag\_data\_len](structhttp__client__ctx.md#a4fb9cbcf7c631ccf2625c8625a484b49)

int http1\_frag\_data\_len

Length of the payload length in the currently processed request fragment (HTTP/1 only).

**Definition** server.h:360

[http\_client\_ctx::websocket\_sec\_key\_next](structhttp__client__ctx.md#a56f376d84aadb40a914b1f52e1216cc6)

bool websocket\_sec\_key\_next

Flag indicating Websocket key is being processed.

**Definition** server.h:388

[http\_client\_ctx::server\_state](structhttp__client__ctx.md#a62c8f1d67b941a1e4cdc61b3a7aa9ffd)

enum http\_server\_state server\_state

Server state for the associated client.

**Definition** server.h:316

[http\_client\_ctx::header\_field](structhttp__client__ctx.md#a6d8fb0fcde6d28b9f5dccd50f2b07b62)

struct http\_hpack\_header\_buf header\_field

HTTP/2 header parser context.

**Definition** server.h:328

[http\_client\_ctx::current\_detail](structhttp__client__ctx.md#a71ee18a5fa2250a01d9c732579a72314)

struct http\_resource\_detail \* current\_detail

Currently processed resource detail.

**Definition** server.h:322

[http\_client\_ctx::url\_buffer](structhttp__client__ctx.md#a9aa78096102e35f58a14070eb9b35ac1)

unsigned char url\_buffer[HTTP\_SERVER\_MAX\_URL\_LENGTH]

Request URL.

**Definition** server.h:340

[http\_client\_ctx::header\_buffer](structhttp__client__ctx.md#a9fc3585221866815823264083b1ad2e5)

unsigned char header\_buffer[HTTP\_SERVER\_MAX\_HEADER\_LEN]

Temp buffer for currently processed header (HTTP/1 only).

**Definition** server.h:346

[http\_client\_ctx::content\_type](structhttp__client__ctx.md#aa9d3f794bc8925d378dfc8cef74d6ae4)

unsigned char content\_type[HTTP\_SERVER\_MAX\_CONTENT\_TYPE\_LEN]

Request content type.

**Definition** server.h:343

[http\_client\_ctx::preface\_sent](structhttp__client__ctx.md#aab71d232273c8bb6374b44d15614a7e1)

bool preface\_sent

Flag indicating that HTTP2 preface was sent.

**Definition** server.h:373

[http\_client\_ctx::method](structhttp__client__ctx.md#ab0695811450793361bc88ca0bb582c15)

enum http\_method method

Request method.

**Definition** server.h:352

[http\_client\_ctx::fd](structhttp__client__ctx.md#ab8d3ab7b98549e796e0ead8be60fedf5)

int fd

Socket descriptor associated with the server.

**Definition** server.h:301

[http\_client\_ctx::http1\_headers\_sent](structhttp__client__ctx.md#ac805cda657ee679d5ccbf80fcc6007b2)

bool http1\_headers\_sent

Flag indicating that HTTP1 headers were sent.

**Definition** server.h:376

[http\_client\_ctx::content\_len](structhttp__client__ctx.md#aca2c3fae568ad984d90646e6b543b959)

size\_t content\_len

Request content length.

**Definition** server.h:349

[http\_client\_ctx::buffer](structhttp__client__ctx.md#aca9893deabb995cb3b3099ba1711be63)

unsigned char buffer[HTTP\_SERVER\_CLIENT\_BUFFER\_SIZE]

Client data buffer.

**Definition** server.h:304

[http\_client\_ctx::current\_frame](structhttp__client__ctx.md#acce3d5cefa58cbeed5b96c4f4a1a0406)

struct http2\_frame current\_frame

Currently processed HTTP/2 frame.

**Definition** server.h:319

[http\_client\_ctx::current\_stream](structhttp__client__ctx.md#ad33d0a5a5b9176cf14b4115726e04448)

struct http2\_stream\_ctx \* current\_stream

Currently processed stream.

**Definition** server.h:325

[http\_client\_ctx::websocket\_upgrade](structhttp__client__ctx.md#ae20c4d4038a643bef49dbb77b497e7b1)

bool websocket\_upgrade

Flag indicating Websocket upgrade takes place.

**Definition** server.h:385

[http\_client\_ctx::has\_upgrade\_header](structhttp__client__ctx.md#ae8fe0bf1dd0e5015b077a01f01fa40e9)

bool has\_upgrade\_header

Flag indicating that upgrade header was present in the request.

**Definition** server.h:379

[http\_client\_ctx::http2\_upgrade](structhttp__client__ctx.md#afcc28f111655bab47516d2e71468bc55)

bool http2\_upgrade

Flag indicating HTTP/2 upgrade takes place.

**Definition** server.h:382

[http\_client\_ctx::data\_len](structhttp__client__ctx.md#afe23c7fb1638a7822d6c2ff6b3c9d167)

size\_t data\_len

Data left to process in the buffer.

**Definition** server.h:310

[http\_hpack\_header\_buf](structhttp__hpack__header__buf.md)

HTTP2 header field with decoding buffer.

**Definition** hpack.h:108

[http\_parser\_settings](structhttp__parser__settings.md)

**Definition** parser.h:190

[http\_parser](structhttp__parser.md)

**Definition** parser.h:147

[http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md)

Representation of a dynamic server resource.

**Definition** server.h:155

[http\_resource\_detail\_dynamic::data\_buffer](structhttp__resource__detail__dynamic.md#a42d25c2ca98ad617b7bddfa3669abbb6)

uint8\_t \* data\_buffer

Data buffer used to exchanged data between server and the, application.

**Definition** server.h:167

[http\_resource\_detail\_dynamic::data\_buffer\_len](structhttp__resource__detail__dynamic.md#a75cbd941e330017ca2243087d4770f76)

size\_t data\_buffer\_len

Length of the data in the data buffer.

**Definition** server.h:170

[http\_resource\_detail\_dynamic::user\_data](structhttp__resource__detail__dynamic.md#a8b6170c4d98efa27616d1e3132c61cd4)

void \* user\_data

A pointer to the user data registered by the application.

**Definition** server.h:178

[http\_resource\_detail\_dynamic::cb](structhttp__resource__detail__dynamic.md#a9f131e0302bbdff94ae6d5147413bec7)

http\_resource\_dynamic\_cb\_t cb

Resource callback used by the server to interact with the application.

**Definition** server.h:162

[http\_resource\_detail\_dynamic::holder](structhttp__resource__detail__dynamic.md#aa06123f6333e561d515a3d1468ec0856)

struct http\_client\_ctx \* holder

A pointer to the client currently processing resource, used to prevent concurrent access to the resou...

**Definition** server.h:175

[http\_resource\_detail\_dynamic::common](structhttp__resource__detail__dynamic.md#aed22a9df2725eab8fc1032903cecacab)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:157

[http\_resource\_detail\_static](structhttp__resource__detail__static.md)

Representation of a static server resource.

**Definition** server.h:102

[http\_resource\_detail\_static::static\_data\_len](structhttp__resource__detail__static.md#a177c212ecfd8e0320200b4ed841f0484)

size\_t static\_data\_len

Size of the static resource.

**Definition** server.h:110

[http\_resource\_detail\_static::static\_data](structhttp__resource__detail__static.md#a1ac562d11ee9b73c2cdcffe81f5a43b9)

const void \* static\_data

Content of the static resource.

**Definition** server.h:107

[http\_resource\_detail\_static::common](structhttp__resource__detail__static.md#a67e4e9166d571d44763f3f7cecd34725)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:104

[http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md)

Representation of a websocket server resource.

**Definition** server.h:203

[http\_resource\_detail\_websocket::data\_buffer\_len](structhttp__resource__detail__websocket.md#a512b5da3bdc20eca57c060160c823117)

size\_t data\_buffer\_len

Length of the data in the data buffer.

**Definition** server.h:221

[http\_resource\_detail\_websocket::user\_data](structhttp__resource__detail__websocket.md#a8f6ceaee3ccae18974fbc2c6498737c8)

void \* user\_data

A pointer to the user data registered by the application.

**Definition** server.h:224

[http\_resource\_detail\_websocket::common](structhttp__resource__detail__websocket.md#acd10efe8ca1f82fb6e0557512f18d9ee)

struct http\_resource\_detail common

Common resource details.

**Definition** server.h:205

[http\_resource\_detail\_websocket::cb](structhttp__resource__detail__websocket.md#ad3a18df78d4ab4443bba2fbf00a0cbc0)

http\_resource\_websocket\_cb\_t cb

Resource callback used by the server to interact with the application.

**Definition** server.h:213

[http\_resource\_detail\_websocket::ws\_sock](structhttp__resource__detail__websocket.md#adbfb331ad424fac889f5e53bb1240ed8)

int ws\_sock

Websocket socket value.

**Definition** server.h:208

[http\_resource\_detail\_websocket::data\_buffer](structhttp__resource__detail__websocket.md#af9c3292e2d450b70831812cb9d084e3c)

uint8\_t \* data\_buffer

Data buffer used to exchanged data between server and the, application.

**Definition** server.h:218

[http\_resource\_detail](structhttp__resource__detail.md)

Representation of a server resource, common for all resource types.

**Definition** server.h:76

[http\_resource\_detail::path\_len](structhttp__resource__detail.md#ac3aa9d4f3781a974739810af5a9e8860)

int path\_len

Length of the URL path.

**Definition** server.h:84

[http\_resource\_detail::content\_type](structhttp__resource__detail.md#acea8d8ff42d8b6ba7d451d3c4de40084)

const char \* content\_type

Content type of the resource.

**Definition** server.h:90

[http\_resource\_detail::bitmask\_of\_supported\_http\_methods](structhttp__resource__detail.md#ae391e85a5713bceef9228b93e876c817)

uint32\_t bitmask\_of\_supported\_http\_methods

Bitmask of supported HTTP methods (http\_method).

**Definition** server.h:78

[http\_resource\_detail::content\_encoding](structhttp__resource__detail.md#ae5b2415ad3e42c164c4e20fd5bb67bd4)

const char \* content\_encoding

Content encoding of the resource.

**Definition** server.h:87

[http\_resource\_detail::type](structhttp__resource__detail.md#af90b58f593a0c5c8506efc7a54a9cf68)

enum http\_resource\_type type

Resource type.

**Definition** server.h:81

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3908

[NUM\_BITS](util_8h.md#afa27c06d0ad6b949289431ad75f104ab)

#define NUM\_BITS(t)

Number of bits that make up a type.

**Definition** util.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [server.h](server_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
