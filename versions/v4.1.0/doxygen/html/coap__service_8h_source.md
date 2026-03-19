---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/coap__service_8h_source.html
original_path: doxygen/html/coap__service_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

37

[ 39](group__coap__service.md#gaf5799a7fbf309f8963d22039a6fe2fbb)#define COAP\_SERVICE\_AUTOSTART BIT(0)

40

42

44

45struct coap\_service\_data {

46 int sock\_fd;

47 struct [coap\_observer](structcoap__observer.md) observers[CONFIG\_COAP\_SERVICE\_OBSERVERS];

48 struct [coap\_pending](structcoap__pending.md) pending[CONFIG\_COAP\_SERVICE\_PENDING\_MESSAGES];

49};

50

51struct coap\_service {

52 const char \*name;

53 const char \*host;

54 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*port;

55 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

56 struct coap\_resource \*res\_begin;

57 struct coap\_resource \*res\_end;

58 struct coap\_service\_data \*data;

59};

60

61#define \_\_z\_coap\_service\_define(\_name, \_host, \_port, \_flags, \_res\_begin, \_res\_end) \

62 static struct coap\_service\_data \_CONCAT(coap\_service\_data\_, \_name) = { \

63 .sock\_fd = -1, \

64 }; \

65 const STRUCT\_SECTION\_ITERABLE(coap\_service, \_name) = { \

66 .name = STRINGIFY(\_name), \

67 .host = \_host, \

68 .port = (uint16\_t \*)(\_port), \

69 .flags = \_flags, \

70 .res\_begin = (\_res\_begin), \

71 .res\_end = (\_res\_end), \

72 .data = &\_CONCAT(coap\_service\_data\_, \_name), \

73 }

74

76

[ 113](group__coap__service.md#gaef40d300170926ad131d06ce62c63d6a)#define COAP\_RESOURCE\_DEFINE(\_name, \_service, ...) \

114 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(\_CONCAT(coap\_resource\_, \_service), coap\_resource, \

115 \_name) = \_\_VA\_ARGS\_\_

116

[ 134](group__coap__service.md#ga8dc5473755efd48548ec4cb6ac2584ec)#define COAP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_flags) \

135 extern struct coap\_resource \_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_start)[]; \

136 extern struct coap\_resource \_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_end)[]; \

137 \_\_z\_coap\_service\_define(\_name, \_host, \_port, \_flags, \

138 &\_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_start)[0], \

139 &\_CONCAT(\_CONCAT(\_coap\_resource\_, \_name), \_list\_end)[0])

140

[ 146](group__coap__service.md#ga1f0c3bf81baa9da11197a74415d3a9ae)#define COAP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(coap\_service, \_dst)

147

[ 153](group__coap__service.md#gade9e9a55968a5ad6b3addbb08f2ccb6f)#define COAP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

154

[ 161](group__coap__service.md#gaf01cb4d11b18272eb27be93cb1a7197b)#define COAP\_SERVICE\_HAS\_RESOURCE(\_service, \_resource) \

162 ((\_service)->res\_begin <= \_resource && \_resource < (\_service)->res\_end)

163

[ 169](group__coap__service.md#gab4d154d5b02235a83c7a2c681b1e22e7)#define COAP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(coap\_service, \_it)

170

[ 179](group__coap__service.md#gac3e92107fa12b111771d56987a242b1a)#define COAP\_RESOURCE\_FOREACH(\_service, \_it) \

180 STRUCT\_SECTION\_FOREACH\_ALTERNATE(\_CONCAT(coap\_resource\_, \_service), coap\_resource, \_it)

181

[ 190](group__coap__service.md#gaaca92287c495f4afb79e584c47316037)#define COAP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

191 for (struct coap\_resource \*\_it = (\_service)->res\_begin; ({ \

192 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

193 \_it < (\_service)->res\_end; \

194 }); \_it++)

195

[ 206](group__coap__service.md#gad1e64f8fe2c6ae32730a9a61f8351bab)int [coap\_service\_start](group__coap__service.md#gad1e64f8fe2c6ae32730a9a61f8351bab)(const struct coap\_service \*service);

207

[ 217](group__coap__service.md#ga58bc31fc4d53ebce9c18ccbc5aab72ce)int [coap\_service\_stop](group__coap__service.md#ga58bc31fc4d53ebce9c18ccbc5aab72ce)(const struct coap\_service \*service);

218

[ 229](group__coap__service.md#ga08638f2001ca2f807489c12ff426784c)int [coap\_service\_is\_running](group__coap__service.md#ga08638f2001ca2f807489c12ff426784c)(const struct coap\_service \*service);

230

[ 243](group__coap__service.md#gad4254ddb71400026211fe8a6da05b2be)int [coap\_service\_send](group__coap__service.md#gad4254ddb71400026211fe8a6da05b2be)(const struct coap\_service \*service, const struct [coap\_packet](structcoap__packet.md) \*cpkt,

244 const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len,

245 const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

246

[ 259](group__coap__service.md#ga67e2cebcfa83f6d11dc335de5dc51a47)int [coap\_resource\_send](group__coap__service.md#ga67e2cebcfa83f6d11dc335de5dc51a47)(const struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*cpkt,

260 const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len,

261 const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

262

[ 276](group__coap__service.md#ga098e08b3bc809499b789b890b67cacd5)int [coap\_resource\_parse\_observe](group__coap__service.md#ga098e08b3bc809499b789b890b67cacd5)(struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*request,

277 const struct [sockaddr](structsockaddr.md) \*addr);

278

[ 288](group__coap__service.md#ga8d9ab0bf6b1ea15408f1c80c45aae16b)int [coap\_resource\_remove\_observer\_by\_addr](group__coap__service.md#ga8d9ab0bf6b1ea15408f1c80c45aae16b)(struct [coap\_resource](structcoap__resource.md) \*resource,

289 const struct [sockaddr](structsockaddr.md) \*addr);

290

[ 301](group__coap__service.md#gad575a7209a56874002c540eb3f8c0733)int [coap\_resource\_remove\_observer\_by\_token](group__coap__service.md#gad575a7209a56874002c540eb3f8c0733)(struct [coap\_resource](structcoap__resource.md) \*resource,

302 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len);

303

307

308#ifdef \_\_cplusplus

309}

310#endif

311

312#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_SERVICE\_H\_ \*/

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

**Definition** net\_ip.h:408

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_service.h](coap__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
