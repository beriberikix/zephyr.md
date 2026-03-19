---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/service_8h_source.html
original_path: doxygen/html/service_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

22#include "[zephyr/net/http/server.h](server_8h.md)"

23#include <[stdint.h](stdint_8h.md)>

24#include <stddef.h>

25

26#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

27#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

28#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 35](structhttp__resource__desc.md)struct [http\_resource\_desc](structhttp__resource__desc.md) {

[ 37](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605) const char \*[resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605);

[ 39](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498) void \*[detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498);

40};

41

[ 59](group__http__service.md#gab177436ac7a8d6589dcfbd416ffd9200)#define HTTP\_RESOURCE\_DEFINE(\_name, \_service, \_resource, \_detail) \

60 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \

61 \_name) = { \

62 .resource = \_resource, \

63 .detail = (void \*)(\_detail), \

64 }

65

67

68struct http\_service\_desc {

69 const char \*host;

70 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*port;

71 int \*fd;

72 void \*detail;

73 size\_t concurrent;

74 size\_t backlog;

75 struct [http\_resource\_desc](structhttp__resource__desc.md) \*res\_begin;

76 struct [http\_resource\_desc](structhttp__resource__desc.md) \*res\_end;

77 struct [http\_resource\_detail](structhttp__resource__detail.md) \*res\_fallback;

78#if defined(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)

79 const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \*sec\_tag\_list;

80 size\_t sec\_tag\_list\_size;

81#endif

82};

83

84#define \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

85 \_res\_fallback, \_res\_begin, \

86 \_res\_end, ...) \

87 static int \_name##\_fd = -1; \

88 const STRUCT\_SECTION\_ITERABLE(http\_service\_desc, \_name) = { \

89 .host = \_host, \

90 .port = (uint16\_t \*)(\_port), \

91 .fd = &\_name##\_fd, \

92 .detail = (void \*)(\_detail), \

93 .concurrent = (\_concurrent), \

94 .backlog = (\_backlog), \

95 .res\_begin = (\_res\_begin), \

96 .res\_end = (\_res\_end), \

97 .res\_fallback = (\_res\_fallback), \

98 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

99 (.sec\_tag\_list = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (NULL), \

100 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))),), ()) \

101 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

102 (.sec\_tag\_list\_size = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (0),\

103 (GET\_ARG\_N(1, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))), ())\

104 }

105

107

[ 128](group__http__service.md#ga8cfc7d2be962a1b0f44e389856097ac1)#define HTTP\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

129 \_res\_fallback) \

130 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

131 \_res\_fallback, NULL, NULL)

132

[ 155](group__http__service.md#ga4ec55524f40ac76a0abdcac3818dfa80)#define HTTPS\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

156 \_res\_fallback, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

157 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

158 \_res\_fallback, NULL, NULL, \

159 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

160 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

161 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

162

[ 183](group__http__service.md#ga1aa8efe3622b5c9421a6257140c5d2c5)#define HTTP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_res\_fallback) \

184 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

185 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

186 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

187 \_res\_fallback, \

188 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

189 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0])

190

[ 213](group__http__service.md#gad8468a96fd46ad7d8aaf48667d7ef092)#define HTTPS\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

214 \_res\_fallback, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

215 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

216 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

217 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

218 \_res\_fallback, \

219 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

220 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0], \

221 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

222 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

223 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

224

[ 230](group__http__service.md#ga09fa08b24156d4a9540dbb525986d8cb)#define HTTP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(http\_service\_desc, \_dst)

231

[ 237](group__http__service.md#gacadf010a47812c29313c914492774921)#define HTTP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

238

[ 244](group__http__service.md#ga6144750de0b60baa3ae9c195a06622e7)#define HTTP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_service\_desc, \_it)

245

[ 254](group__http__service.md#ga450271e3a0a7098d5942539e1482605f)#define HTTP\_RESOURCE\_FOREACH(\_service, \_it) \

255 STRUCT\_SECTION\_FOREACH\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \_it)

256

[ 266](group__http__service.md#ga97f21c80270bb79f32cf4d891e6c3eba)#define HTTP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

267 for (struct http\_resource\_desc \*\_it = (\_service)->res\_begin; ({ \

268 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

269 \_it < (\_service)->res\_end; \

270 }); \

271 \_it++)

272

273#ifdef \_\_cplusplus

274}

275#endif

276

280

281#endif /\* ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_ \*/

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:74

[server.h](server_8h.md)

HTTP server API.

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_resource\_desc](structhttp__resource__desc.md)

HTTP resource description.

**Definition** service.h:35

[http\_resource\_desc::resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605)

const char \* resource

Resource name.

**Definition** service.h:37

[http\_resource\_desc::detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498)

void \* detail

Detail associated with this resource.

**Definition** service.h:39

[http\_resource\_detail](structhttp__resource__detail.md)

Representation of a server resource, common for all resource types.

**Definition** server.h:88

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
