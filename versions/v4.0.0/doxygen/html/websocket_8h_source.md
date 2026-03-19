---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/websocket_8h_source.html
original_path: doxygen/html/websocket_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

websocket.h

[Go to the documentation of this file.](websocket_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_WEBSOCKET\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_WEBSOCKET\_H\_

15

16#include <[zephyr/kernel.h](kernel_8h.md)>

17

18#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

19#include <[zephyr/net/http/parser.h](parser_8h.md)>

20#include <[zephyr/net/http/client.h](client_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

34

[ 36](group__websocket.md#ga002ade0e3787b6d9da82ab84af1cd354)#define WEBSOCKET\_FLAG\_FINAL 0x00000001

[ 37](group__websocket.md#ga9405e69474b48472dfe0b10017dfcd75)#define WEBSOCKET\_FLAG\_TEXT 0x00000002

[ 38](group__websocket.md#ga8616f88cb194d82da9367f2f48832842)#define WEBSOCKET\_FLAG\_BINARY 0x00000004

[ 39](group__websocket.md#gaab5fa480351106751f6482f5056b4238)#define WEBSOCKET\_FLAG\_CLOSE 0x00000008

[ 40](group__websocket.md#ga2f2ea01b18c13f38fe834f855ae0da93)#define WEBSOCKET\_FLAG\_PING 0x00000010

[ 41](group__websocket.md#ga68cdf577c5401440095dacf224541047)#define WEBSOCKET\_FLAG\_PONG 0x00000020

42

[ 44](group__websocket.md#ga207402575311103c75906143724e8c35)enum [websocket\_opcode](group__websocket.md#ga207402575311103c75906143724e8c35) {

[ 45](group__websocket.md#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35) [WEBSOCKET\_OPCODE\_CONTINUE](group__websocket.md#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35) = 0x00,

[ 46](group__websocket.md#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c) [WEBSOCKET\_OPCODE\_DATA\_TEXT](group__websocket.md#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c) = 0x01,

[ 47](group__websocket.md#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69) [WEBSOCKET\_OPCODE\_DATA\_BINARY](group__websocket.md#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69) = 0x02,

[ 48](group__websocket.md#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191) [WEBSOCKET\_OPCODE\_CLOSE](group__websocket.md#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191) = 0x08,

[ 49](group__websocket.md#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709) [WEBSOCKET\_OPCODE\_PING](group__websocket.md#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709) = 0x09,

[ 50](group__websocket.md#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90) [WEBSOCKET\_OPCODE\_PONG](group__websocket.md#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90) = 0x0A,

51};

52

[ 63](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591)typedef int (\*[websocket\_connect\_cb\_t](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591))(int ws\_sock, struct [http\_request](structhttp__request.md) \*req,

64 void \*user\_data);

65

[ 70](structwebsocket__request.md)struct [websocket\_request](structwebsocket__request.md) {

[ 72](structwebsocket__request.md#a8769d50f1a6168dc6518f2dd0c74b62a) const char \*[host](structwebsocket__request.md#a8769d50f1a6168dc6518f2dd0c74b62a);

73

[ 75](structwebsocket__request.md#a49ef6c2f4201beeb3af8992ded2bd4a3) const char \*[url](structwebsocket__request.md#a49ef6c2f4201beeb3af8992ded2bd4a3);

76

[ 83](structwebsocket__request.md#ab7a281fff2a27a52f7ec346643f55b71) [http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4) [optional\_headers\_cb](structwebsocket__request.md#ab7a281fff2a27a52f7ec346643f55b71);

84

[ 89](structwebsocket__request.md#a4cea74d6094325b218b6bbed4005b912) const char \*\*[optional\_headers](structwebsocket__request.md#a4cea74d6094325b218b6bbed4005b912);

90

[ 94](structwebsocket__request.md#a96936b68fec07f077d9e9569ef1411d1) [websocket\_connect\_cb\_t](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591) [cb](structwebsocket__request.md#a96936b68fec07f077d9e9569ef1411d1);

95

[ 102](structwebsocket__request.md#a38315d0c37bdc8cfe22cdbc6d2c8af4a) const struct [http\_parser\_settings](structhttp__parser__settings.md) \*[http\_cb](structwebsocket__request.md#a38315d0c37bdc8cfe22cdbc6d2c8af4a);

103

[ 105](structwebsocket__request.md#a939ed8e980af4bc98f30d1bad835a2d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tmp\_buf](structwebsocket__request.md#a939ed8e980af4bc98f30d1bad835a2d2);

106

[ 108](structwebsocket__request.md#a09bb3c708b51d8f86de244b3fc4a9f57) size\_t [tmp\_buf\_len](structwebsocket__request.md#a09bb3c708b51d8f86de244b3fc4a9f57);

109};

110

[ 129](group__websocket.md#ga71a43ec629929d2eb1baba4e3f13a615)int [websocket\_connect](group__websocket.md#ga71a43ec629929d2eb1baba4e3f13a615)(int http\_sock, struct [websocket\_request](structwebsocket__request.md) \*req,

130 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout, void \*user\_data);

131

[ 153](group__websocket.md#gac23c351e5020d0fc9e936933d399b187)int [websocket\_send\_msg](group__websocket.md#gac23c351e5020d0fc9e936933d399b187)(int ws\_sock, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, size\_t payload\_len,

154 enum [websocket\_opcode](group__websocket.md#ga207402575311103c75906143724e8c35) opcode, bool mask, bool final,

155 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

156

[ 177](group__websocket.md#ga0fb118f84b7631d12c1b742b75593ba6)int [websocket\_recv\_msg](group__websocket.md#ga0fb118f84b7631d12c1b742b75593ba6)(int ws\_sock, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buf\_len,

178 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*message\_type, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*remaining,

179 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

180

[ 191](group__websocket.md#gacc2f06e2c361317ff48f171abc3d1209)int [websocket\_disconnect](group__websocket.md#gacc2f06e2c361317ff48f171abc3d1209)(int ws\_sock);

192

[ 205](group__websocket.md#gabc2556e62f001f8109bf6ae9f50f3952)int [websocket\_register](group__websocket.md#gabc2556e62f001f8109bf6ae9f50f3952)(int http\_sock, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*recv\_buf, size\_t recv\_buf\_len);

206

[ 216](group__websocket.md#gaa3131d2599c8c69ab95c55c2e38e28e0)int [websocket\_unregister](group__websocket.md#gaa3131d2599c8c69ab95c55c2e38e28e0)(int ws\_sock);

217

219

220#if defined(CONFIG\_WEBSOCKET\_CLIENT)

221void websocket\_init(void);

222#else

223static inline void websocket\_init(void)

224{

225}

226#endif

227

229

230#ifdef \_\_cplusplus

231}

232#endif

233

237

238#endif /\* ZEPHYR\_INCLUDE\_NET\_WEBSOCKET\_H\_ \*/

[client.h](client_8h.md)

HTTP client API.

[http\_header\_cb\_t](group__http__client.md#ga34a431c54c52b86618ca0e27ce3862b4)

int(\* http\_header\_cb\_t)(int sock, struct http\_request \*req, void \*user\_data)

Callback can be used if application wants to construct additional HTTP headers when the HTTP request ...

**Definition** client.h:85

[websocket\_recv\_msg](group__websocket.md#ga0fb118f84b7631d12c1b742b75593ba6)

int websocket\_recv\_msg(int ws\_sock, uint8\_t \*buf, size\_t buf\_len, uint32\_t \*message\_type, uint64\_t \*remaining, int32\_t timeout)

Receive websocket msg from peer.

[websocket\_opcode](group__websocket.md#ga207402575311103c75906143724e8c35)

websocket\_opcode

Websocket option codes.

**Definition** websocket.h:44

[websocket\_connect](group__websocket.md#ga71a43ec629929d2eb1baba4e3f13a615)

int websocket\_connect(int http\_sock, struct websocket\_request \*req, int32\_t timeout, void \*user\_data)

Connect to a server that provides Websocket service.

[websocket\_unregister](group__websocket.md#gaa3131d2599c8c69ab95c55c2e38e28e0)

int websocket\_unregister(int ws\_sock)

Unregister a websocket.

[websocket\_connect\_cb\_t](group__websocket.md#gaabfd7aa30ce659214b990eabb0b6d591)

int(\* websocket\_connect\_cb\_t)(int ws\_sock, struct http\_request \*req, void \*user\_data)

Callback called after Websocket connection is established.

**Definition** websocket.h:63

[websocket\_register](group__websocket.md#gabc2556e62f001f8109bf6ae9f50f3952)

int websocket\_register(int http\_sock, uint8\_t \*recv\_buf, size\_t recv\_buf\_len)

Register a socket as websocket.

[websocket\_send\_msg](group__websocket.md#gac23c351e5020d0fc9e936933d399b187)

int websocket\_send\_msg(int ws\_sock, const uint8\_t \*payload, size\_t payload\_len, enum websocket\_opcode opcode, bool mask, bool final, int32\_t timeout)

Send websocket msg to peer.

[websocket\_disconnect](group__websocket.md#gacc2f06e2c361317ff48f171abc3d1209)

int websocket\_disconnect(int ws\_sock)

Close websocket.

[WEBSOCKET\_OPCODE\_PONG](group__websocket.md#gga207402575311103c75906143724e8c35a141c7a8d3c0864115c8bfe3248e59d90)

@ WEBSOCKET\_OPCODE\_PONG

Pong message.

**Definition** websocket.h:50

[WEBSOCKET\_OPCODE\_DATA\_TEXT](group__websocket.md#gga207402575311103c75906143724e8c35a2058fe14c900c3298affa6eed05d182c)

@ WEBSOCKET\_OPCODE\_DATA\_TEXT

Textual data.

**Definition** websocket.h:46

[WEBSOCKET\_OPCODE\_CLOSE](group__websocket.md#gga207402575311103c75906143724e8c35a291cb41ba1d8b535a1625d394c066191)

@ WEBSOCKET\_OPCODE\_CLOSE

Closing connection.

**Definition** websocket.h:48

[WEBSOCKET\_OPCODE\_CONTINUE](group__websocket.md#gga207402575311103c75906143724e8c35a8912ad4ae9a3bbbe7ecb02cd2c1a8b35)

@ WEBSOCKET\_OPCODE\_CONTINUE

Message continues.

**Definition** websocket.h:45

[WEBSOCKET\_OPCODE\_DATA\_BINARY](group__websocket.md#gga207402575311103c75906143724e8c35aa8d476ba0f4f3f892503d29fa76f1a69)

@ WEBSOCKET\_OPCODE\_DATA\_BINARY

Binary data.

**Definition** websocket.h:47

[WEBSOCKET\_OPCODE\_PING](group__websocket.md#gga207402575311103c75906143724e8c35af7a26bf82e06544e8393f17d6c074709)

@ WEBSOCKET\_OPCODE\_PING

Ping message.

**Definition** websocket.h:49

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[parser.h](parser_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[http\_parser\_settings](structhttp__parser__settings.md)

**Definition** parser.h:190

[http\_request](structhttp__request.md)

HTTP client request.

**Definition** client.h:230

[websocket\_request](structwebsocket__request.md)

Websocket client connection request.

**Definition** websocket.h:70

[websocket\_request::tmp\_buf\_len](structwebsocket__request.md#a09bb3c708b51d8f86de244b3fc4a9f57)

size\_t tmp\_buf\_len

Length of the user supplied temp buffer.

**Definition** websocket.h:108

[websocket\_request::http\_cb](structwebsocket__request.md#a38315d0c37bdc8cfe22cdbc6d2c8af4a)

const struct http\_parser\_settings \* http\_cb

User supplied list of callback functions if the calling application wants to know the parsing status ...

**Definition** websocket.h:102

[websocket\_request::url](structwebsocket__request.md#a49ef6c2f4201beeb3af8992ded2bd4a3)

const char \* url

URL of the Websocket.

**Definition** websocket.h:75

[websocket\_request::optional\_headers](structwebsocket__request.md#a4cea74d6094325b218b6bbed4005b912)

const char \*\* optional\_headers

A NULL terminated list of any optional headers that should be added to the HTTP request.

**Definition** websocket.h:89

[websocket\_request::host](structwebsocket__request.md#a8769d50f1a6168dc6518f2dd0c74b62a)

const char \* host

Host of the Websocket server when doing HTTP handshakes.

**Definition** websocket.h:72

[websocket\_request::tmp\_buf](structwebsocket__request.md#a939ed8e980af4bc98f30d1bad835a2d2)

uint8\_t \* tmp\_buf

User supplied buffer where HTTP connection data is stored.

**Definition** websocket.h:105

[websocket\_request::cb](structwebsocket__request.md#a96936b68fec07f077d9e9569ef1411d1)

websocket\_connect\_cb\_t cb

User supplied callback function to call when a connection is established.

**Definition** websocket.h:94

[websocket\_request::optional\_headers\_cb](structwebsocket__request.md#ab7a281fff2a27a52f7ec346643f55b71)

http\_header\_cb\_t optional\_headers\_cb

User supplied callback function to call when optional headers need to be sent.

**Definition** websocket.h:83

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [websocket.h](websocket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
