---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/service_8h_source.html
original_path: doxygen/html/service_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

10#include <[stdint.h](stdint_8h.md)>

11#include <stddef.h>

12

13#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](structhttp__resource__desc.md)struct [http\_resource\_desc](structhttp__resource__desc.md) {

[ 20](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605) const char \*[resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605);

[ 21](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498) void \*[detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498);

22};

23

[ 41](service_8h.md#ab177436ac7a8d6589dcfbd416ffd9200)#define HTTP\_RESOURCE\_DEFINE(\_name, \_service, \_resource, \_detail) \

42 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \

43 \_name) = { \

44 .resource = \_resource, \

45 .detail = (\_detail), \

46 }

47

[ 48](structhttp__service__desc.md)struct [http\_service\_desc](structhttp__service__desc.md) {

[ 49](structhttp__service__desc.md#a421961e470a5ca82d9d4aa1f2a8d71a5) const char \*[host](structhttp__service__desc.md#a421961e470a5ca82d9d4aa1f2a8d71a5);

[ 50](structhttp__service__desc.md#a30df63e2966f863762fe26b771206ff7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[port](structhttp__service__desc.md#a30df63e2966f863762fe26b771206ff7);

[ 51](structhttp__service__desc.md#a94935033fe14aff5afb65dffffd42f94) void \*[detail](structhttp__service__desc.md#a94935033fe14aff5afb65dffffd42f94);

[ 52](structhttp__service__desc.md#ab668b2e198c1202a9de44144b3c0de0b) size\_t [concurrent](structhttp__service__desc.md#ab668b2e198c1202a9de44144b3c0de0b);

[ 53](structhttp__service__desc.md#af151d08745b99510d7c3edb64440523d) size\_t [backlog](structhttp__service__desc.md#af151d08745b99510d7c3edb64440523d);

[ 54](structhttp__service__desc.md#a3db5d3cbb7f9014301870263849ca84c) struct [http\_resource\_desc](structhttp__resource__desc.md) \*[res\_begin](structhttp__service__desc.md#a3db5d3cbb7f9014301870263849ca84c);

[ 55](structhttp__service__desc.md#a4c0b014ca8c46fe770b24c7af43d74f6) struct [http\_resource\_desc](structhttp__resource__desc.md) \*[res\_end](structhttp__service__desc.md#a4c0b014ca8c46fe770b24c7af43d74f6);

56};

57

58#define \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_res\_begin, \

59 \_res\_end) \

60 static const STRUCT\_SECTION\_ITERABLE(http\_service\_desc, \_name) = { \

61 .host = \_host, \

62 .port = (uint16\_t \*)(\_port), \

63 .detail = (void \*)(\_detail), \

64 .concurrent = (\_concurrent), \

65 .backlog = (\_backlog), \

66 .res\_begin = (\_res\_begin), \

67 .res\_end = (\_res\_end), \

68 }

69

[ 88](service_8h.md#aa146bcb3349e5f476b520113f74969ab)#define HTTP\_SERVICE\_DEFINE\_EMPTY(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) \

89 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL)

90

[ 109](service_8h.md#a38d08c32ea0e082cb39ed2a8d1a3dcc3)#define HTTP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) \

110 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

111 extern struct http\_resource\_desc \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

112 \_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

113 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

114 &\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0])

115

[ 121](service_8h.md#a09fa08b24156d4a9540dbb525986d8cb)#define HTTP\_SERVICE\_COUNT(\_dst) STRUCT\_SECTION\_COUNT(http\_service\_desc, \_dst)

122

[ 128](service_8h.md#acadf010a47812c29313c914492774921)#define HTTP\_SERVICE\_RESOURCE\_COUNT(\_service) ((\_service)->res\_end - (\_service)->res\_begin)

129

[ 135](service_8h.md#a6144750de0b60baa3ae9c195a06622e7)#define HTTP\_SERVICE\_FOREACH(\_it) STRUCT\_SECTION\_FOREACH(http\_service\_desc, \_it)

136

[ 145](service_8h.md#a450271e3a0a7098d5942539e1482605f)#define HTTP\_RESOURCE\_FOREACH(\_service, \_it) \

146 STRUCT\_SECTION\_FOREACH\_ALTERNATE(http\_resource\_desc\_##\_service, http\_resource\_desc, \_it)

147

[ 157](service_8h.md#a97f21c80270bb79f32cf4d891e6c3eba)#define HTTP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it) \

158 for (struct http\_resource\_desc \*\_it = (\_service)->res\_begin; ({ \

159 \_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

160 \_it < (\_service)->res\_end; \

161 }); \

162 \_it++)

163

164#ifdef \_\_cplusplus

165}

166#endif

167

168#endif /\* ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVICE\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_resource\_desc](structhttp__resource__desc.md)

**Definition** service.h:19

[http\_resource\_desc::resource](structhttp__resource__desc.md#a2882314e271a09d6bc9fae3f58558605)

const char \* resource

**Definition** service.h:20

[http\_resource\_desc::detail](structhttp__resource__desc.md#afdf3332dbc4fb8c10ec8bc525cd8d498)

void \* detail

**Definition** service.h:21

[http\_service\_desc](structhttp__service__desc.md)

**Definition** service.h:48

[http\_service\_desc::port](structhttp__service__desc.md#a30df63e2966f863762fe26b771206ff7)

uint16\_t \* port

**Definition** service.h:50

[http\_service\_desc::res\_begin](structhttp__service__desc.md#a3db5d3cbb7f9014301870263849ca84c)

struct http\_resource\_desc \* res\_begin

**Definition** service.h:54

[http\_service\_desc::host](structhttp__service__desc.md#a421961e470a5ca82d9d4aa1f2a8d71a5)

const char \* host

**Definition** service.h:49

[http\_service\_desc::res\_end](structhttp__service__desc.md#a4c0b014ca8c46fe770b24c7af43d74f6)

struct http\_resource\_desc \* res\_end

**Definition** service.h:55

[http\_service\_desc::detail](structhttp__service__desc.md#a94935033fe14aff5afb65dffffd42f94)

void \* detail

**Definition** service.h:51

[http\_service\_desc::concurrent](structhttp__service__desc.md#ab668b2e198c1202a9de44144b3c0de0b)

size\_t concurrent

**Definition** service.h:52

[http\_service\_desc::backlog](structhttp__service__desc.md#af151d08745b99510d7c3edb64440523d)

size\_t backlog

**Definition** service.h:53

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [service.h](service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
