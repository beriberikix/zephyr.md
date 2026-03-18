---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/service_8h_source.html
original_path: doxygen/html/service_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

19

20#include <[stdint.h](stdint_8h.md)>

21#include <stddef.h>

22

23#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

24#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

25#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 32](structhttp__resource__desc.md)struct [http\_resource\_desc](structhttp__resource__desc.md) {

[ 34](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605) const char \*[resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605);

[ 36](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498) void \*[detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498);

37};

38

[ 56](group__http__service.md#gab177436ac7a8d6589dcfbd416ffd9200)#define HTTP\_RESOURCE\_DEFINE(\_name, \_service, \_resource, \_detail) \

57 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \

58 \_name) = { \

59 .resource = \_resource, \

60 .detail = (void \*)(\_detail), \

61 }

62

64

65struct http\_service\_desc {

66 const char \*host;

67 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*port;

68 void \*detail;

69 size\_t concurrent;

70 size\_t backlog;

71 struct [http\_resource\_desc](structhttp__resource__desc.md) \*res\_begin;

72 struct [http\_resource\_desc](structhttp__resource__desc.md) \*res\_end;

73#if defined(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)

74 const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \*sec\_tag\_list;

75 size\_t sec\_tag\_list\_size;

76#endif

77};

78

79#define \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_res\_begin, \

80 \_res\_end, ...) \

81 static const STRUCT\_SECTION\_ITERABLE(http\_service\_desc, \_name) = { \

82 .host = \_host, \

83 .port = (uint16\_t \*)(\_port), \

84 .detail = (void \*)(\_detail), \

85 .concurrent = (\_concurrent), \

86 .backlog = (\_backlog), \

87 .res\_begin = (\_res\_begin), \

88 .res\_end = (\_res\_end), \

89 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

90 (.sec\_tag\_list = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (NULL), \

91 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))),), ()) \

92 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS, \

93 (.sec\_tag\_list\_size = COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (0),\

94 (GET\_ARG\_N(1, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))), ())\

95 }

96

98

[ 117](group__http__service.md#gaa146bcb3349e5f476b520113f74969ab)#define HTTP\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) \

118 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL)

119

[ 140](group__http__service.md#ga5d43ce4203d9459189262c2c6b9d69de)#define HTTPS\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

141 \_sec\_tag\_list, \_sec\_tag\_list\_size) \

142 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL, \

143 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

144 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

145 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

146

[ 165](group__http__service.md#ga38d08c32ea0e082cb39ed2a8d1a3dcc3)#define HTTP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) \

166 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

167 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

168 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

169 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

170 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0])

171

[ 192](group__http__service.md#ga3bfac63b6f6e0224157f82da90bc7e50)#define HTTPS\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

193 \_sec\_tag\_list, \_sec\_tag\_list\_size) \

194 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

195 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

196 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

197 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

198 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0], \

199 \_sec\_tag\_list, \_sec\_tag\_list\_size); \

200 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

201 "TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

202

[ 208](group__http__service.md#ga09fa08b24156d4a9540dbb525986d8cb)#define HTTP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(http\_service\_desc, \_dst)

209

[ 215](group__http__service.md#gacadf010a47812c29313c914492774921)#define HTTP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

216

[ 222](group__http__service.md#ga6144750de0b60baa3ae9c195a06622e7)#define HTTP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_service\_desc, \_it)

223

[ 232](group__http__service.md#ga450271e3a0a7098d5942539e1482605f)#define HTTP\_RESOURCE\_FOREACH(\_service, \_it) \

233 STRUCT\_SECTION\_FOREACH\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \_it)

234

[ 244](group__http__service.md#ga97f21c80270bb79f32cf4d891e6c3eba)#define HTTP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

245 for (struct http\_resource\_desc \*\_it = (\_service)->res\_begin; ({ \

246 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

247 \_it < (\_service)->res\_end; \

248 }); \

249 \_it++)

250

251#ifdef \_\_cplusplus

252}

253#endif

254

258

259#endif /\* ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_ \*/

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:72

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_resource\_desc](structhttp__resource__desc.md)

HTTP resource description.

**Definition** service.h:32

[http\_resource\_desc::resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605)

const char \* resource

Resource name.

**Definition** service.h:34

[http\_resource\_desc::detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498)

void \* detail

Detail associated with this resource.

**Definition** service.h:36

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
