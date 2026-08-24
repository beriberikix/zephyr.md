---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/coap__service_8h_source.html
original_path: doxygen/html/coap__service_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_service.h

[Go to the documentation of this file.](coap__service_8h.md)

1/\*

2 \* Copyright (c) 2023 Basalte bv

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_COAP\_SERVICE\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_COAP\_SERVICE\_H\_

15

16#include <[zephyr/net/coap.h](coap_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

32

38

[ 40](group__coap__service.md#gaf5799a7fbf309f8963d22039a6fe2fbb)#define COAP\_SERVICE\_AUTOSTART BIT(0)

41

43

45

46struct coap\_service\_data {

47 int sock\_fd;

48 struct [coap\_observer](structcoap__observer.md) observers[CONFIG\_COAP\_SERVICE\_OBSERVERS];

49 struct [coap\_pending](structcoap__pending.md) pending[CONFIG\_COAP\_SERVICE\_PENDING\_MESSAGES];

50};

51

52struct coap\_service {

53 const char \*name;

54 const char \*host;

55 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*port;

56 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

57 struct coap\_resource \*res\_begin;

58 struct coap\_resource \*res\_end;

59 struct coap\_service\_data \*data;

60#if defined(CONFIG\_NET\_SOCKETS\_ENABLE\_DTLS)

61 const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \*sec\_tag\_list;

62 size\_t sec\_tag\_list\_size;

63#endif

64};

65

66#if defined(CONFIG\_NET\_SOCKETS\_ENABLE\_DTLS)

67#define \_\_z\_coap\_service\_secure(\_sec\_tag\_list, \_sec\_tag\_list\_size) \

68 .sec\_tag\_list = \_sec\_tag\_list, \

69 .sec\_tag\_list\_size = \_sec\_tag\_list\_size,

70#else

71#define \_\_z\_coap\_service\_secure(...)

72#endif

73

74#define \_\_z\_coap\_service\_define(\_name, \_host, \_port, \_flags, \_res\_begin, \_res\_end, \

75 \_sec\_tag\_list, \_sec\_tag\_list\_size) \

76 static struct coap\_service\_data \_CONCAT(coap\_service\_data\_, \_name) = { \

77 .sock\_fd = -1, \

78 }; \

79 const STRUCT\_SECTION\_ITERABLE(coap\_service, \_name) = { \

80 .name = STRINGIFY(\_name), \

81 .host = \_host, \

82 .port = (uint16\_t \*)(\_port), \

83 .flags = \_flags, \

84 .res\_begin = (\_res\_begin), \

85 .res\_end = (\_res\_end), \

86 .data = &\_CONCAT(coap\_service\_data\_, \_name), \

87 \_\_z\_coap\_service\_secure(\_sec\_tag\_list, \_sec\_tag\_list\_size) \

88 }

89

91

[ 128](group__coap__service.md#gaef40d300170926ad131d06ce62c63d6a)#define COAP\_RESOURCE\_DEFINE(\_name, \_service, ...) \

129 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(\_CONCAT(coap\_resource\_, \_service), coap\_resource, \

130 \_name) = \_\_VA\_ARGS\_\_

131

[ 149](group__coap__service.md#ga8dc5473755efd48548ec4cb6ac2584ec)#define COAP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_flags) \

150 extern struct coap\_resource \_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_start)[]; \

151 extern struct coap\_resource \_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_end)[]; \

152 \_\_z\_coap\_service\_define(\_name, \_host, \_port, \_flags, \

153 &\_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_start)[0], \

154 &\_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_end)[0], \

155 NULL, 0)

156

[ 178](group__coap__service.md#ga1ec49f2bc2c378431c4721080a13d11d)#define COAPS\_SERVICE\_DEFINE(\_name, \_host, \_port, \_flags, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

179 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_ENABLE\_DTLS), \

180 "DTLS is required for CoAP secure (CONFIG\_NET\_SOCKETS\_ENABLE\_DTLS)"); \

181 extern struct coap\_resource \_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_start)[]; \

182 extern struct coap\_resource \_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_end)[]; \

183 \_\_z\_coap\_service\_define(\_name, \_host, \_port, \_flags, \

184 &\_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_start)[0], \

185 &\_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_end)[0], \

186 \_sec\_tag\_list, \_sec\_tag\_list\_size)

187

[ 193](group__coap__service.md#ga1f0c3bf81baa9da11197a74415d3a9ae)#define COAP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(coap\_service, \_dst)

194

[ 200](group__coap__service.md#gade9e9a55968a5ad6b3addbb08f2ccb6f)#define COAP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

201

[ 208](group__coap__service.md#gaf01cb4d11b18272eb27be93cb1a7197b)#define COAP\_SERVICE\_HAS\_RESOURCE(\_service, \_resource) \

209 ((\_service)->res\_begin <= \_resource && \_resource < (\_service)->res\_end)

210

[ 216](group__coap__service.md#gab4d154d5b02235a83c7a2c681b1e22e7)#define COAP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(coap\_service, \_it)

217

[ 226](group__coap__service.md#gac3e92107fa12b111771d56987a242b1a)#define COAP\_RESOURCE\_FOREACH(\_service, \_it) \

227 STRUCT\_SECTION\_FOREACH\_ALTERNATE(\_CONCAT(coap\_resource\_, \_service), coap\_resource, \_it)

228

[ 237](group__coap__service.md#gaaca92287c495f4afb79e584c47316037)#define COAP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

238 for (struct coap\_resource \*\_it = (\_service)->res\_begin; ({ \

239 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

240 \_it < (\_service)->res\_end; \

241 }); \_it++)

242

[ 253](group__coap__service.md#gad1e64f8fe2c6ae32730a9a61f8351bab)int [coap\_service\_start](group__coap__service.md#gad1e64f8fe2c6ae32730a9a61f8351bab)(const struct coap\_service \*service);

254

[ 264](group__coap__service.md#ga58bc31fc4d53ebce9c18ccbc5aab72ce)int [coap\_service\_stop](group__coap__service.md#ga58bc31fc4d53ebce9c18ccbc5aab72ce)(const struct coap\_service \*service);

265

[ 276](group__coap__service.md#ga08638f2001ca2f807489c12ff426784c)int [coap\_service\_is\_running](group__coap__service.md#ga08638f2001ca2f807489c12ff426784c)(const struct coap\_service \*service);

277

[ 290](group__coap__service.md#gad4254ddb71400026211fe8a6da05b2be)int [coap\_service\_send](group__coap__service.md#gad4254ddb71400026211fe8a6da05b2be)(const struct coap\_service \*service, const struct [coap\_packet](structcoap__packet.md) \*cpkt,

291 const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len,

292 const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

293

[ 306](group__coap__service.md#ga67e2cebcfa83f6d11dc335de5dc51a47)int [coap\_resource\_send](group__coap__service.md#ga67e2cebcfa83f6d11dc335de5dc51a47)(const struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*cpkt,

307 const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len,

308 const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

309

[ 323](group__coap__service.md#ga098e08b3bc809499b789b890b67cacd5)int [coap\_resource\_parse\_observe](group__coap__service.md#ga098e08b3bc809499b789b890b67cacd5)(struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*request,

324 const struct [sockaddr](structsockaddr.md) \*addr);

325

[ 335](group__coap__service.md#ga8d9ab0bf6b1ea15408f1c80c45aae16b)int [coap\_resource\_remove\_observer\_by\_addr](group__coap__service.md#ga8d9ab0bf6b1ea15408f1c80c45aae16b)(struct [coap\_resource](structcoap__resource.md) \*resource,

336 const struct [sockaddr](structsockaddr.md) \*addr);

337

[ 348](group__coap__service.md#gad575a7209a56874002c540eb3f8c0733)int [coap\_resource\_remove\_observer\_by\_token](group__coap__service.md#gad575a7209a56874002c540eb3f8c0733)(struct [coap\_resource](structcoap__resource.md) \*resource,

349 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len);

350

354

355#ifdef \_\_cplusplus

356}

357#endif

358

359#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_SERVICE\_H\_ \*/

[coap.h](coap_8h.md)

CoAP implementation for Zephyr.

[coap\_service\_is\_running](group__coap__service.md#ga08638f2001ca2f807489c12ff426784c)

int coap\_service\_is\_running(const struct coap\_service \*service)

Query the provided service running state.

[coap\_resource\_parse\_observe](group__coap__service.md#ga098e08b3bc809499b789b890b67cacd5)

int coap\_resource\_parse\_observe(struct coap\_resource \*resource, const struct coap\_packet \*request, const struct sockaddr \*addr)

Parse a CoAP observe request for the provided resource .

[coap\_service\_stop](group__coap__service.md#ga58bc31fc4d53ebce9c18ccbc5aab72ce)

int coap\_service\_stop(const struct coap\_service \*service)

Stop the provided service .

[coap\_resource\_send](group__coap__service.md#ga67e2cebcfa83f6d11dc335de5dc51a47)

int coap\_resource\_send(const struct coap\_resource \*resource, const struct coap\_packet \*cpkt, const struct sockaddr \*addr, socklen\_t addr\_len, const struct coap\_transmission\_parameters \*params)

Send a CoAP message from the provided resource .

[coap\_resource\_remove\_observer\_by\_addr](group__coap__service.md#ga8d9ab0bf6b1ea15408f1c80c45aae16b)

int coap\_resource\_remove\_observer\_by\_addr(struct coap\_resource \*resource, const struct sockaddr \*addr)

Lookup an observer by address and remove it from the resource .

[coap\_service\_start](group__coap__service.md#gad1e64f8fe2c6ae32730a9a61f8351bab)

int coap\_service\_start(const struct coap\_service \*service)

Start the provided service .

[coap\_service\_send](group__coap__service.md#gad4254ddb71400026211fe8a6da05b2be)

int coap\_service\_send(const struct coap\_service \*service, const struct coap\_packet \*cpkt, const struct sockaddr \*addr, socklen\_t addr\_len, const struct coap\_transmission\_parameters \*params)

Send a CoAP message from the provided service .

[coap\_resource\_remove\_observer\_by\_token](group__coap__service.md#gad575a7209a56874002c540eb3f8c0733)

int coap\_resource\_remove\_observer\_by\_token(struct coap\_resource \*resource, const uint8\_t \*token, uint8\_t token\_len)

Lookup an observer by token and remove it from the resource .

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:80

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[coap\_observer](structcoap__observer.md)

Represents a remote device that is observing a local resource.

**Definition** coap.h:298

[coap\_packet](structcoap__packet.md)

Representation of a CoAP Packet.

**Definition** coap.h:312

[coap\_pending](structcoap__pending.md)

Represents a request awaiting for an acknowledgment (ACK).

**Definition** coap.h:376

[coap\_resource](structcoap__resource.md)

Description of CoAP resource.

**Definition** coap.h:280

[coap\_transmission\_parameters](structcoap__transmission__parameters.md)

CoAP transmission parameters.

**Definition** coap.h:357

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:410

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_service.h](coap__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
