---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/service_8h_source.html
original_path: doxygen/html/service_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

68struct http\_service\_runtime\_data {

69 int num\_clients;

70};

71

72struct http\_service\_desc {

73 const char \*host;

74 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*port;

75 int \*fd;

76 void \*detail;

77 size\_t concurrent;

78 size\_t backlog;

79 struct http\_service\_runtime\_data \*data;

80 struct http\_resource\_desc \*res\_begin;

81 struct http\_resource\_desc \*res\_end;

82 struct http\_resource\_detail \*res\_fallback;

83#if defined(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)

84 const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \*sec\_tag\_list;

85 size\_t sec\_tag\_list\_size;

86#endif

87};

88

89#define \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

90 \_res\_fallback, \_res\_begin, \_res\_end, ...) \

91 BUILD\_ASSERT(\_concurrent <= CONFIG\_HTTP\_SERVER\_MAX\_CLIENTS, \

92 "can't accept more then MAX\_CLIENTS"); \

93 BUILD\_ASSERT(\_backlog > 0, "backlog can't be 0"); \

94 static int \_name##\_fd = -1; \

95 static struct http\_service\_runtime\_data \_name##\_data = {0}; \

96 const STRUCT\_SECTION\_ITERABLE(http\_service\_desc, \_name) = { \

97 .host = \_host, \

98 .port = (uint16\_t \*)(\_port), \

99 .fd = &\_name##\_fd, \

100 .detail = (void \*)(\_detail), \

101 .concurrent = (\_concurrent), \

102 .backlog = (\_backlog), \

103 .data = &\_name##\_data, \

104 .res\_begin = (\_res\_begin), \

105 .res\_end = (\_res\_end), \

106 .res\_fallback = (\_res\_fallback), \

107 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

108 (.sec\_tag\_list = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (NULL), \

109 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))),), ()) \

110 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

111 (.sec\_tag\_list\_size = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (0),\

112 (GET\_ARG\_N(1, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))), ())\

113 }

114

116

[ 137](group__http__service.md#ga8cfc7d2be962a1b0f44e389856097ac1)#define HTTP\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

138 \_res\_fallback) \

139 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

140 \_res\_fallback, NULL, NULL)

141

[ 164](group__http__service.md#ga4ec55524f40ac76a0abdcac3818dfa80)#define HTTPS\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

165 \_res\_fallback, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

166 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

167 \_res\_fallback, NULL, NULL, \

168 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

169 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

170 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

171

[ 192](group__http__service.md#ga1aa8efe3622b5c9421a6257140c5d2c5)#define HTTP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_res\_fallback) \

193 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

194 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

195 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

196 \_res\_fallback, \

197 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

198 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0]);

199

[ 222](group__http__service.md#gad8468a96fd46ad7d8aaf48667d7ef092)#define HTTPS\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

223 \_res\_fallback, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

224 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

225 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

226 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

227 \_res\_fallback, \

228 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

229 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0], \

230 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

231 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

232 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

233

[ 239](group__http__service.md#ga09fa08b24156d4a9540dbb525986d8cb)#define HTTP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(http\_service\_desc, \_dst)

240

[ 246](group__http__service.md#gacadf010a47812c29313c914492774921)#define HTTP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

247

[ 253](group__http__service.md#ga6144750de0b60baa3ae9c195a06622e7)#define HTTP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_service\_desc, \_it)

254

[ 263](group__http__service.md#ga450271e3a0a7098d5942539e1482605f)#define HTTP\_RESOURCE\_FOREACH(\_service, \_it) \

264 STRUCT\_SECTION\_FOREACH\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \_it)

265

[ 275](group__http__service.md#ga97f21c80270bb79f32cf4d891e6c3eba)#define HTTP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

276 for (struct http\_resource\_desc \*\_it = (\_service)->res\_begin; ({ \

277 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

278 \_it < (\_service)->res\_end; \

279 }); \

280 \_it++)

281

282#ifdef \_\_cplusplus

283}

284#endif

285

289

290#endif /\* ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_ \*/

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:80

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

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [service.h](service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
