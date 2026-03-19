---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/service_8h_source.html
original_path: doxygen/html/service_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

service.h

[Go to the documentation of this file.](service_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_

8#define ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_

9

21

22#include <[stdint.h](stdint_8h.md)>

23#include <stddef.h>

24

25#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

26#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

27#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 34](structhttp__resource__desc.md)struct [http\_resource\_desc](structhttp__resource__desc.md) {

[ 36](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605) const char \*[resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605);

[ 38](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498) void \*[detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498);

39};

40

[ 58](group__http__service.md#gab177436ac7a8d6589dcfbd416ffd9200)#define HTTP\_RESOURCE\_DEFINE(\_name, \_service, \_resource, \_detail) \

59 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \

60 \_name) = { \

61 .resource = \_resource, \

62 .detail = (void \*)(\_detail), \

63 }

64

66

67struct http\_service\_desc {

68 const char \*host;

69 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*port;

70 void \*detail;

71 size\_t concurrent;

72 size\_t backlog;

73 struct [http\_resource\_desc](structhttp__resource__desc.md) \*res\_begin;

74 struct [http\_resource\_desc](structhttp__resource__desc.md) \*res\_end;

75#if defined(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)

76 const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \*sec\_tag\_list;

77 size\_t sec\_tag\_list\_size;

78#endif

79};

80

81#define \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_res\_begin, \

82 \_res\_end, ...) \

83 static const STRUCT\_SECTION\_ITERABLE(http\_service\_desc, \_name) = { \

84 .host = \_host, \

85 .port = (uint16\_t \*)(\_port), \

86 .detail = (void \*)(\_detail), \

87 .concurrent = (\_concurrent), \

88 .backlog = (\_backlog), \

89 .res\_begin = (\_res\_begin), \

90 .res\_end = (\_res\_end), \

91 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

92 (.sec\_tag\_list = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (NULL), \

93 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))),), ()) \

94 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

95 (.sec\_tag\_list\_size = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (0),\

96 (GET\_ARG\_N(1, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))), ())\

97 }

98

100

[ 120](group__http__service.md#gaa146bcb3349e5f476b520113f74969ab)#define HTTP\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) \

121 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL)

122

[ 144](group__http__service.md#ga5d43ce4203d9459189262c2c6b9d69de)#define HTTPS\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

145 \_sec\_tag\_list, \_sec\_tag\_list\_size) \

146 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL, \

147 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

148 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

149 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

150

[ 170](group__http__service.md#ga38d08c32ea0e082cb39ed2a8d1a3dcc3)#define HTTP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) \

171 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

172 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

173 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

174 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

175 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0])

176

[ 198](group__http__service.md#ga3bfac63b6f6e0224157f82da90bc7e50)#define HTTPS\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

199 \_sec\_tag\_list, \_sec\_tag\_list\_size) \

200 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

201 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

202 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

203 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

204 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0], \

205 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

206 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

207 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

208

[ 214](group__http__service.md#ga09fa08b24156d4a9540dbb525986d8cb)#define HTTP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(http\_service\_desc, \_dst)

215

[ 221](group__http__service.md#gacadf010a47812c29313c914492774921)#define HTTP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

222

[ 228](group__http__service.md#ga6144750de0b60baa3ae9c195a06622e7)#define HTTP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_service\_desc, \_it)

229

[ 238](group__http__service.md#ga450271e3a0a7098d5942539e1482605f)#define HTTP\_RESOURCE\_FOREACH(\_service, \_it) \

239 STRUCT\_SECTION\_FOREACH\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \_it)

240

[ 250](group__http__service.md#ga97f21c80270bb79f32cf4d891e6c3eba)#define HTTP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

251 for (struct http\_resource\_desc \*\_it = (\_service)->res\_begin; ({ \

252 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

253 \_it < (\_service)->res\_end; \

254 }); \

255 \_it++)

256

257#ifdef \_\_cplusplus

258}

259#endif

260

264

265#endif /\* ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_ \*/

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:74

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_resource\_desc](structhttp__resource__desc.md)

HTTP resource description.

**Definition** service.h:34

[http\_resource\_desc::resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605)

const char \* resource

Resource name.

**Definition** service.h:36

[http\_resource\_desc::detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498)

void \* detail

Detail associated with this resource.

**Definition** service.h:38

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [service.h](service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
