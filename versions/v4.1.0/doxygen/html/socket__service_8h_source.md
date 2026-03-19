---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socket__service_8h_source.html
original_path: doxygen/html/socket__service_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_service.h

[Go to the documentation of this file.](socket__service_8h.md)

1

8

9/\*

10 \* Copyright (c) 2023 Nordic Semiconductor ASA

11 \*

12 \* SPDX-License-Identifier: Apache-2.0

13 \*/

14

15#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_SERVICE\_H\_

16#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_SERVICE\_H\_

17

26

27#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29#include <[zephyr/net/socket.h](net_2socket_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35struct [net\_socket\_service\_event](structnet__socket__service__event.md);

36

[ 43](group__bsd__socket__service.md#ga5d9495470c1ade51791df56c59cfb1f5)typedef void (\*[net\_socket\_service\_handler\_t](group__bsd__socket__service.md#ga5d9495470c1ade51791df56c59cfb1f5))(struct [net\_socket\_service\_event](structnet__socket__service__event.md) \*pev);

44

[ 49](structnet__socket__service__event.md)struct [net\_socket\_service\_event](structnet__socket__service__event.md) {

[ 51](structnet__socket__service__event.md#a82695b0eaa7c563033fce4afde33cab9) [net\_socket\_service\_handler\_t](group__bsd__socket__service.md#ga5d9495470c1ade51791df56c59cfb1f5) [callback](structnet__socket__service__event.md#a82695b0eaa7c563033fce4afde33cab9);

[ 53](structnet__socket__service__event.md#a8246a87e2171474eb214bb8f909cb9bf) struct [zsock\_pollfd](structzsock__pollfd.md) [event](structnet__socket__service__event.md#a8246a87e2171474eb214bb8f909cb9bf);

[ 55](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638) void \*[user\_data](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638);

[ 57](structnet__socket__service__event.md#a7052fad6a65c5a1b610a69e16fc72785) struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*[svc](structnet__socket__service__event.md#a7052fad6a65c5a1b610a69e16fc72785);

58};

59

[ 70](structnet__socket__service__desc.md)struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) {

71#if CONFIG\_NET\_SOCKETS\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

[ 76](structnet__socket__service__desc.md#a08da5714fafa3f678771ea3d5204971a) const char \*[owner](structnet__socket__service__desc.md#a08da5714fafa3f678771ea3d5204971a);

77#endif

[ 79](structnet__socket__service__desc.md#a62104a9136d2abd88c25480eee2b187a) struct [net\_socket\_service\_event](structnet__socket__service__event.md) \*[pev](structnet__socket__service__desc.md#a62104a9136d2abd88c25480eee2b187a);

[ 81](structnet__socket__service__desc.md#a5c958339cbc98e7c4490952ce1e9fbc9) int [pev\_len](structnet__socket__service__desc.md#a5c958339cbc98e7c4490952ce1e9fbc9);

[ 83](structnet__socket__service__desc.md#a480b960a8d130ded4668f355a8e5fd83) int \*[idx](structnet__socket__service__desc.md#a480b960a8d130ded4668f355a8e5fd83);

84};

85

87

88#define \_\_z\_net\_socket\_svc\_get\_name(\_svc\_id) \_\_z\_net\_socket\_service\_##\_svc\_id

89#define \_\_z\_net\_socket\_svc\_get\_idx(\_svc\_id) \_\_z\_net\_socket\_service\_idx\_##\_svc\_id

90#define \_\_z\_net\_socket\_svc\_get\_owner \_\_FILE\_\_ ":" STRINGIFY(\_\_LINE\_\_)

91

92#if CONFIG\_NET\_SOCKETS\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

93#define NET\_SOCKET\_SERVICE\_OWNER .owner = \_\_z\_net\_socket\_svc\_get\_owner,

94#else

95#define NET\_SOCKET\_SERVICE\_OWNER

96#endif

97

98#define \_\_z\_net\_socket\_service\_define(\_name, \_cb, \_count, ...) \

99 static int \_\_z\_net\_socket\_svc\_get\_idx(\_name); \

100 static struct net\_socket\_service\_event \

101 \_\_z\_net\_socket\_svc\_get\_name(\_name)[\_count] = { \

102 [0 ... ((\_count) - 1)] = { \

103 .event.fd = -1, /\* Invalid socket \*/ \

104 .callback = \_cb, \

105 } \

106 }; \

107 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (), \_\_VA\_ARGS\_\_) \

108 const STRUCT\_SECTION\_ITERABLE(net\_socket\_service\_desc, \_name) = { \

109 NET\_SOCKET\_SERVICE\_OWNER \

110 .pev = \_\_z\_net\_socket\_svc\_get\_name(\_name), \

111 .pev\_len = (\_count), \

112 .idx = &\_\_z\_net\_socket\_svc\_get\_idx(\_name), \

113 }

114

116

[ 135](group__bsd__socket__service.md#ga424f319f9ccc675f8eeca23cb2c91bc4)#define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE(name, cb, count) \

136 \_\_z\_net\_socket\_service\_define(name, cb, count)

137

[ 148](group__bsd__socket__service.md#gadee4c786ebf89706a6b0151244b55cc3)#define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC(name, cb, count) \

149 \_\_z\_net\_socket\_service\_define(name, cb, count, static)

150

[ 163](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)\_\_syscall int [net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service,

164 struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int len, void \*[user\_data](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638));

165

[ 175](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6)static inline int [net\_socket\_service\_unregister](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6)(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service)

176{

177 return [net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)(service, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

178}

179

[ 187](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd)typedef void (\*[net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd))(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*svc,

188 void \*user\_data);

189

[ 196](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097)void [net\_socket\_service\_foreach](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097)([net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd) cb, void \*user\_data);

197

198#ifdef \_\_cplusplus

199}

200#endif

201

202#include <zephyr/syscalls/socket\_service.h>

203

207

208#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_SERVICE\_H\_ \*/

[net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd)

void(\* net\_socket\_service\_cb\_t)(const struct net\_socket\_service\_desc \*svc, void \*user\_data)

Callback used while iterating over socket services.

**Definition** socket\_service.h:187

[net\_socket\_service\_handler\_t](group__bsd__socket__service.md#ga5d9495470c1ade51791df56c59cfb1f5)

void(\* net\_socket\_service\_handler\_t)(struct net\_socket\_service\_event \*pev)

The signature for a net socket service handler function.

**Definition** socket\_service.h:43

[net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)

int net\_socket\_service\_register(const struct net\_socket\_service\_desc \*service, struct zsock\_pollfd \*fds, int len, void \*user\_data)

Register pollable sockets.

[net\_socket\_service\_foreach](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097)

void net\_socket\_service\_foreach(net\_socket\_service\_cb\_t cb, void \*user\_data)

Go through all the socket services and call callback for each service.

[net\_socket\_service\_unregister](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6)

static int net\_socket\_service\_unregister(const struct net\_socket\_service\_desc \*service)

Unregister pollable sockets.

**Definition** socket\_service.h:175

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_socket\_service\_desc](structnet__socket__service__desc.md)

Main structure holding socket service configuration information.

**Definition** socket\_service.h:70

[net\_socket\_service\_desc::owner](structnet__socket__service__desc.md#a08da5714fafa3f678771ea3d5204971a)

const char \* owner

Owner name.

**Definition** socket\_service.h:76

[net\_socket\_service\_desc::idx](structnet__socket__service__desc.md#a480b960a8d130ded4668f355a8e5fd83)

int \* idx

Where are my pollfd entries in the global list.

**Definition** socket\_service.h:83

[net\_socket\_service\_desc::pev\_len](structnet__socket__service__desc.md#a5c958339cbc98e7c4490952ce1e9fbc9)

int pev\_len

Length of the pollable socket array for this service.

**Definition** socket\_service.h:81

[net\_socket\_service\_desc::pev](structnet__socket__service__desc.md#a62104a9136d2abd88c25480eee2b187a)

struct net\_socket\_service\_event \* pev

Pointer to the list of services that we are listening.

**Definition** socket\_service.h:79

[net\_socket\_service\_event](structnet__socket__service__event.md)

This struct contains information which socket triggered calls to the callback function.

**Definition** socket\_service.h:49

[net\_socket\_service\_event::svc](structnet__socket__service__event.md#a7052fad6a65c5a1b610a69e16fc72785)

struct net\_socket\_service\_desc \* svc

Service back pointer.

**Definition** socket\_service.h:57

[net\_socket\_service\_event::event](structnet__socket__service__event.md#a8246a87e2171474eb214bb8f909cb9bf)

struct zsock\_pollfd event

Socket information that triggered this event.

**Definition** socket\_service.h:53

[net\_socket\_service\_event::callback](structnet__socket__service__event.md#a82695b0eaa7c563033fce4afde33cab9)

net\_socket\_service\_handler\_t callback

Callback to be called for desired socket activity.

**Definition** socket\_service.h:51

[net\_socket\_service\_event::user\_data](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638)

void \* user\_data

User data.

**Definition** socket\_service.h:55

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_service.h](socket__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
