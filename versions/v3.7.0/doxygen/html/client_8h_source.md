---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/client_8h_source.html
original_path: doxygen/html/client_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

client.h

[Go to the documentation of this file.](client_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_CLIENT\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_HTTP\_CLIENT\_H\_

15

24

25#include <[zephyr/kernel.h](kernel_8h.md)>

26#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

27#include <[zephyr/net/http/parser.h](parser_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

34

35#if !defined(HTTP\_CRLF)

36#define HTTP\_CRLF "\r\n"

37#endif

38

39#if !defined(HTTP\_STATUS\_STR\_SIZE)

40#define HTTP\_STATUS\_STR\_SIZE 32

41#endif

42

44

[ 46](group__http__client.md#ga04fc31de51404e35b3dfab6261bb8e6d)enum [http\_final\_call](group__http__client.md#ga04fc31de51404e35b3dfab6261bb8e6d) {

[ 47](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359) [HTTP\_DATA\_MORE](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359) = 0,

[ 48](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61) [HTTP\_DATA\_FINAL](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61) = 1,

49};

50

51struct [http\_request](structhttp__request.md);

52struct [http\_response](structhttp__response.md);

53

[ 67](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed)typedef int (\*[http\_payload\_cb\_t](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed))(int sock,

68 struct [http\_request](structhttp__request.md) \*req,

69 void \*user\_data);

70

[ 85](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4)typedef int (\*[http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4))(int sock,

86 struct [http\_request](structhttp__request.md) \*req,

87 void \*user\_data);

88

[ 98](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a)typedef void (\*[http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a))(struct [http\_response](structhttp__response.md) \*rsp,

99 enum [http\_final\_call](group__http__client.md#ga04fc31de51404e35b3dfab6261bb8e6d) final\_data,

100 void \*user\_data);

101

[ 105](structhttp__response.md)struct [http\_response](structhttp__response.md) {

[ 107](structhttp__response.md#af306ff4c8424b5abad76037abbfe2833) const struct [http\_parser\_settings](structhttp__parser__settings.md) \*[http\_cb](structhttp__response.md#af306ff4c8424b5abad76037abbfe2833);

108

[ 113](structhttp__response.md#a1936119331645bb421d4a5dc0d3fffb5) [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a) [cb](structhttp__response.md#a1936119331645bb421d4a5dc0d3fffb5);

114

[ 144](structhttp__response.md#a45c8596746f5a359a1e18c95838b59d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[body\_frag\_start](structhttp__response.md#a45c8596746f5a359a1e18c95838b59d9);

145

[ 147](structhttp__response.md#a58405582a11aa86892b80133f8b4fa43) size\_t [body\_frag\_len](structhttp__response.md#a58405582a11aa86892b80133f8b4fa43);

148

[ 152](structhttp__response.md#aa16de8f3485062bf01b0536e64f58b46) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[recv\_buf](structhttp__response.md#aa16de8f3485062bf01b0536e64f58b46);

153

[ 155](structhttp__response.md#a7454c5963b7bb1c5311f77971d0d1d2f) size\_t [recv\_buf\_len](structhttp__response.md#a7454c5963b7bb1c5311f77971d0d1d2f);

156

[ 167](structhttp__response.md#a4208cf209674441a25231732aad91f89) size\_t [data\_len](structhttp__response.md#a4208cf209674441a25231732aad91f89);

168

[ 172](structhttp__response.md#aedcb476d4055a7ba04516cc7a8ef800f) size\_t [content\_length](structhttp__response.md#aedcb476d4055a7ba04516cc7a8ef800f);

173

[ 179](structhttp__response.md#a0eb2181115c753a3e1676a18d9a3ed59) size\_t [processed](structhttp__response.md#a0eb2181115c753a3e1676a18d9a3ed59);

180

[ 191](structhttp__response.md#a6bf553c9399385afeb921f6abef9a875) char [http\_status](structhttp__response.md#a6bf553c9399385afeb921f6abef9a875)[HTTP\_STATUS\_STR\_SIZE];

192

[ 198](structhttp__response.md#a94cd246204b04992712deefe51fc0c26) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [http\_status\_code](structhttp__response.md#a94cd246204b04992712deefe51fc0c26);

199

[ 200](structhttp__response.md#a0d28b200a74c150e98b5fc18c61638cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cl\_present](structhttp__response.md#a0d28b200a74c150e98b5fc18c61638cc) : 1;

[ 201](structhttp__response.md#ac713af14995e36c1889291d12803ca18) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [body\_found](structhttp__response.md#ac713af14995e36c1889291d12803ca18) : 1;

[ 202](structhttp__response.md#a4f107746bfff244a841b950dd84b8162) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [message\_complete](structhttp__response.md#a4f107746bfff244a841b950dd84b8162) : 1;

203};

204

[ 207](structhttp__client__internal__data.md)struct [http\_client\_internal\_data](structhttp__client__internal__data.md) {

[ 209](structhttp__client__internal__data.md#a1620ae6631414c3ba5e462d97deca157) struct [http\_parser](structhttp__parser.md) [parser](structhttp__client__internal__data.md#a1620ae6631414c3ba5e462d97deca157);

210

[ 212](structhttp__client__internal__data.md#a19876ea20cdca3a016d6e260e2795e83) struct [http\_parser\_settings](structhttp__parser__settings.md) [parser\_settings](structhttp__client__internal__data.md#a19876ea20cdca3a016d6e260e2795e83);

213

[ 217](structhttp__client__internal__data.md#aa132cb0366969c04250f64075866227c) struct [http\_response](structhttp__response.md) [response](structhttp__client__internal__data.md#aa132cb0366969c04250f64075866227c);

218

[ 220](structhttp__client__internal__data.md#a330102d665b6601949eb7331ab45d517) void \*[user\_data](structhttp__client__internal__data.md#a330102d665b6601949eb7331ab45d517);

221

[ 223](structhttp__client__internal__data.md#a8486d8e8b64474e75cadeb9fb166a4a5) int [sock](structhttp__client__internal__data.md#a8486d8e8b64474e75cadeb9fb166a4a5);

224};

225

[ 230](structhttp__request.md)struct [http\_request](structhttp__request.md) {

[ 232](structhttp__request.md#abb86ccd0e0801c278ef37a78a4b7a958) struct [http\_client\_internal\_data](structhttp__client__internal__data.md) [internal](structhttp__request.md#abb86ccd0e0801c278ef37a78a4b7a958);

233

234 /\* User should fill in following parameters \*/

235

[ 237](structhttp__request.md#adbfcd3bcaf57205360bad957a13999e6) enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) [method](structhttp__request.md#adbfcd3bcaf57205360bad957a13999e6);

238

[ 242](structhttp__request.md#aba8bf528f3e279d55662eedc9168d25c) [http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a) [response](structhttp__request.md#aba8bf528f3e279d55662eedc9168d25c);

243

[ 248](structhttp__request.md#afbe0c199a4a58029bf2d83a0b463639c) const struct [http\_parser\_settings](structhttp__parser__settings.md) \*[http\_cb](structhttp__request.md#afbe0c199a4a58029bf2d83a0b463639c);

249

[ 251](structhttp__request.md#abaabd58d149720720ffd61025d58e4a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[recv\_buf](structhttp__request.md#abaabd58d149720720ffd61025d58e4a9);

252

[ 254](structhttp__request.md#a9da5216bbd27ad54fd11368897ed660f) size\_t [recv\_buf\_len](structhttp__request.md#a9da5216bbd27ad54fd11368897ed660f);

255

[ 257](structhttp__request.md#a6a7573252e31fddb5cad5a6764c486c1) const char \*[url](structhttp__request.md#a6a7573252e31fddb5cad5a6764c486c1);

258

[ 260](structhttp__request.md#a38cad3f92ed5b712f749851bbeed9a2f) const char \*[protocol](structhttp__request.md#a38cad3f92ed5b712f749851bbeed9a2f);

261

[ 268](structhttp__request.md#a2d2f8be2634eb89d0b877b989307ac7b) const char \*\*[header\_fields](structhttp__request.md#a2d2f8be2634eb89d0b877b989307ac7b);

269

[ 271](structhttp__request.md#a1e610f06e9a8ec05cb0de382163a8c79) const char \*[content\_type\_value](structhttp__request.md#a1e610f06e9a8ec05cb0de382163a8c79);

272

[ 274](structhttp__request.md#a3ed1146d59f33e9042fae421619df27c) const char \*[host](structhttp__request.md#a3ed1146d59f33e9042fae421619df27c);

275

[ 277](structhttp__request.md#abe9fdaab40cac6afb16acc2560dfe7e7) const char \*[port](structhttp__request.md#abe9fdaab40cac6afb16acc2560dfe7e7);

278

[ 285](structhttp__request.md#a15551f2e8c772479fb7acac20765fa12) [http\_payload\_cb\_t](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed) [payload\_cb](structhttp__request.md#a15551f2e8c772479fb7acac20765fa12);

286

[ 288](structhttp__request.md#af201ae38024233307ed2c87684ea70d3) const char \*[payload](structhttp__request.md#af201ae38024233307ed2c87684ea70d3);

289

[ 293](structhttp__request.md#a589615592c6c14bdecc03553c395c12f) size\_t [payload\_len](structhttp__request.md#a589615592c6c14bdecc03553c395c12f);

294

[ 301](structhttp__request.md#ab6fe0ec09c24302279124043e82f17ff) [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4) [optional\_headers\_cb](structhttp__request.md#ab6fe0ec09c24302279124043e82f17ff);

302

[ 312](structhttp__request.md#aa29c2bcb70011c9776c959667e10bcf5) const char \*\*[optional\_headers](structhttp__request.md#aa29c2bcb70011c9776c959667e10bcf5);

313};

314

[ 330](group__http__client.md#gaa38b6efb03f88d6959273a41b6acac81)int [http\_client\_req](group__http__client.md#gaa38b6efb03f88d6959273a41b6acac81)(int sock, struct [http\_request](structhttp__request.md) \*req,

331 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout, void \*user\_data);

332

333#ifdef \_\_cplusplus

334}

335#endif

336

340

341#endif /\* ZEPHYR\_INCLUDE\_NET\_HTTP\_CLIENT\_H\_ \*/

[http\_final\_call](group__http__client.md#ga04fc31de51404e35b3dfab6261bb8e6d)

http\_final\_call

Is there more data to come.

**Definition** client.h:46

[http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4)

int(\* http\_header\_cb\_t)(int sock, struct http\_request \*req, void \*user\_data)

Callback can be used if application wants to construct additional HTTP headers when the HTTP request ...

**Definition** client.h:85

[http\_response\_cb\_t](group__http__client.md#ga9e079c737c325ee21a57e615b641f21a)

void(\* http\_response\_cb\_t)(struct http\_response \*rsp, enum http\_final\_call final\_data, void \*user\_data)

Callback used when data is received from the server.

**Definition** client.h:98

[http\_client\_req](group__http__client.md#gaa38b6efb03f88d6959273a41b6acac81)

int http\_client\_req(int sock, struct http\_request \*req, int32\_t timeout, void \*user\_data)

Do a HTTP request.

[http\_payload\_cb\_t](group__http__client.md#gaf46ede77bdc83602c84b9342dd8d30ed)

int(\* http\_payload\_cb\_t)(int sock, struct http\_request \*req, void \*user\_data)

Callback used when data needs to be sent to the server.

**Definition** client.h:67

[HTTP\_DATA\_MORE](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359)

@ HTTP\_DATA\_MORE

More data will come.

**Definition** client.h:47

[HTTP\_DATA\_FINAL](group__http__client.md#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61)

@ HTTP\_DATA\_FINAL

End of data.

**Definition** client.h:48

[http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8)

http\_method

HTTP Request Methods.

**Definition** method.h:26

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[parser.h](parser_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_client\_internal\_data](structhttp__client__internal__data.md)

HTTP client internal data that the application should not touch.

**Definition** client.h:207

[http\_client\_internal\_data::parser](structhttp__client__internal__data.md#a1620ae6631414c3ba5e462d97deca157)

struct http\_parser parser

HTTP parser context.

**Definition** client.h:209

[http\_client\_internal\_data::parser\_settings](structhttp__client__internal__data.md#a19876ea20cdca3a016d6e260e2795e83)

struct http\_parser\_settings parser\_settings

HTTP parser settings.

**Definition** client.h:212

[http\_client\_internal\_data::user\_data](structhttp__client__internal__data.md#a330102d665b6601949eb7331ab45d517)

void \* user\_data

User data.

**Definition** client.h:220

[http\_client\_internal\_data::sock](structhttp__client__internal__data.md#a8486d8e8b64474e75cadeb9fb166a4a5)

int sock

HTTP socket.

**Definition** client.h:223

[http\_client\_internal\_data::response](structhttp__client__internal__data.md#aa132cb0366969c04250f64075866227c)

struct http\_response response

HTTP response specific data (filled by http\_client\_req() when data is received).

**Definition** client.h:217

[http\_parser\_settings](structhttp__parser__settings.md)

**Definition** parser.h:190

[http\_parser](structhttp__parser.md)

**Definition** parser.h:147

[http\_request](structhttp__request.md)

HTTP client request.

**Definition** client.h:230

[http\_request::payload\_cb](structhttp__request.md#a15551f2e8c772479fb7acac20765fa12)

http\_payload\_cb\_t payload\_cb

User supplied callback function to call when payload needs to be sent.

**Definition** client.h:285

[http\_request::content\_type\_value](structhttp__request.md#a1e610f06e9a8ec05cb0de382163a8c79)

const char \* content\_type\_value

The value of the Content-Type header field, may be NULL.

**Definition** client.h:271

[http\_request::header\_fields](structhttp__request.md#a2d2f8be2634eb89d0b877b989307ac7b)

const char \*\* header\_fields

The HTTP header fields (application specific) The Content-Type may be specified here or in the next f...

**Definition** client.h:268

[http\_request::protocol](structhttp__request.md#a38cad3f92ed5b712f749851bbeed9a2f)

const char \* protocol

The HTTP protocol, for example "HTTP/1.1".

**Definition** client.h:260

[http\_request::host](structhttp__request.md#a3ed1146d59f33e9042fae421619df27c)

const char \* host

Hostname to be used in the request.

**Definition** client.h:274

[http\_request::payload\_len](structhttp__request.md#a589615592c6c14bdecc03553c395c12f)

size\_t payload\_len

Payload length is used to calculate Content-Length.

**Definition** client.h:293

[http\_request::url](structhttp__request.md#a6a7573252e31fddb5cad5a6764c486c1)

const char \* url

The URL for this request, for example: /index.html.

**Definition** client.h:257

[http\_request::recv\_buf\_len](structhttp__request.md#a9da5216bbd27ad54fd11368897ed660f)

size\_t recv\_buf\_len

Length of the user supplied receive buffer.

**Definition** client.h:254

[http\_request::optional\_headers](structhttp__request.md#aa29c2bcb70011c9776c959667e10bcf5)

const char \*\* optional\_headers

A NULL terminated list of any optional headers that should be added to the HTTP request.

**Definition** client.h:312

[http\_request::optional\_headers\_cb](structhttp__request.md#ab6fe0ec09c24302279124043e82f17ff)

http\_header\_cb\_t optional\_headers\_cb

User supplied callback function to call when optional headers need to be sent.

**Definition** client.h:301

[http\_request::response](structhttp__request.md#aba8bf528f3e279d55662eedc9168d25c)

http\_response\_cb\_t response

User supplied callback function to call when response is received.

**Definition** client.h:242

[http\_request::recv\_buf](structhttp__request.md#abaabd58d149720720ffd61025d58e4a9)

uint8\_t \* recv\_buf

User supplied buffer where received data is stored.

**Definition** client.h:251

[http\_request::internal](structhttp__request.md#abb86ccd0e0801c278ef37a78a4b7a958)

struct http\_client\_internal\_data internal

HTTP client request internal data.

**Definition** client.h:232

[http\_request::port](structhttp__request.md#abe9fdaab40cac6afb16acc2560dfe7e7)

const char \* port

Port number to be used in the request.

**Definition** client.h:277

[http\_request::method](structhttp__request.md#adbfcd3bcaf57205360bad957a13999e6)

enum http\_method method

The HTTP method: GET, HEAD, OPTIONS, POST, ...

**Definition** client.h:237

[http\_request::payload](structhttp__request.md#af201ae38024233307ed2c87684ea70d3)

const char \* payload

Payload, may be NULL.

**Definition** client.h:288

[http\_request::http\_cb](structhttp__request.md#afbe0c199a4a58029bf2d83a0b463639c)

const struct http\_parser\_settings \* http\_cb

User supplied list of HTTP callback functions if the calling application wants to know the parsing st...

**Definition** client.h:248

[http\_response](structhttp__response.md)

HTTP response from the server.

**Definition** client.h:105

[http\_response::cl\_present](structhttp__response.md#a0d28b200a74c150e98b5fc18c61638cc)

uint8\_t cl\_present

Is Content-Length field present.

**Definition** client.h:200

[http\_response::processed](structhttp__response.md#a0eb2181115c753a3e1676a18d9a3ed59)

size\_t processed

Amount of data given to the response callback so far, including the current data given to the callbac...

**Definition** client.h:179

[http\_response::cb](structhttp__response.md#a1936119331645bb421d4a5dc0d3fffb5)

http\_response\_cb\_t cb

User provided HTTP response callback which is called when a response is received to a sent HTTP reque...

**Definition** client.h:113

[http\_response::data\_len](structhttp__response.md#a4208cf209674441a25231732aad91f89)

size\_t data\_len

Length of the data in the result buf.

**Definition** client.h:167

[http\_response::body\_frag\_start](structhttp__response.md#a45c8596746f5a359a1e18c95838b59d9)

uint8\_t \* body\_frag\_start

Start address of the body fragment contained in the recv\_buf.

**Definition** client.h:144

[http\_response::message\_complete](structhttp__response.md#a4f107746bfff244a841b950dd84b8162)

uint8\_t message\_complete

Is HTTP message parsing complete.

**Definition** client.h:202

[http\_response::body\_frag\_len](structhttp__response.md#a58405582a11aa86892b80133f8b4fa43)

size\_t body\_frag\_len

Length of the body fragment contained in the recv\_buf.

**Definition** client.h:147

[http\_response::http\_status](structhttp__response.md#a6bf553c9399385afeb921f6abef9a875)

char http\_status[HTTP\_STATUS\_STR\_SIZE]

See https://tools.ietf.org/html/rfc7230#section-3.1.2 for more information.

**Definition** client.h:191

[http\_response::recv\_buf\_len](structhttp__response.md#a7454c5963b7bb1c5311f77971d0d1d2f)

size\_t recv\_buf\_len

Response buffer maximum length.

**Definition** client.h:155

[http\_response::http\_status\_code](structhttp__response.md#a94cd246204b04992712deefe51fc0c26)

uint16\_t http\_status\_code

Numeric HTTP status code which corresponds to the textual description.

**Definition** client.h:198

[http\_response::recv\_buf](structhttp__response.md#aa16de8f3485062bf01b0536e64f58b46)

uint8\_t \* recv\_buf

Where the response is stored, this is to be provided by the user.

**Definition** client.h:152

[http\_response::body\_found](structhttp__response.md#ac713af14995e36c1889291d12803ca18)

uint8\_t body\_found

Is message body found.

**Definition** client.h:201

[http\_response::content\_length](structhttp__response.md#aedcb476d4055a7ba04516cc7a8ef800f)

size\_t content\_length

HTTP Content-Length field value.

**Definition** client.h:172

[http\_response::http\_cb](structhttp__response.md#af306ff4c8424b5abad76037abbfe2833)

const struct http\_parser\_settings \* http\_cb

HTTP parser settings for the application usage.

**Definition** client.h:107

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [client.h](client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
