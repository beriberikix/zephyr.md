---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socket__service_8h_source.html
original_path: doxygen/html/socket__service_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

24

25#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/net/socket.h](net_2socket_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 37](structnet__socket__service__event.md)struct [net\_socket\_service\_event](structnet__socket__service__event.md) {

[ 39](structnet__socket__service__event.md#a0bf2c9e1fc2b8125db3fd907ed6ea27c) struct [k\_work](structk__work.md) [work](structnet__socket__service__event.md#a0bf2c9e1fc2b8125db3fd907ed6ea27c);

[ 41](structnet__socket__service__event.md#a1af4ca9e8076f0725d90f535fbbb94c4) [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) [callback](structnet__socket__service__event.md#a1af4ca9e8076f0725d90f535fbbb94c4);

[ 43](structnet__socket__service__event.md#a8246a87e2171474eb214bb8f909cb9bf) struct [zsock\_pollfd](structzsock__pollfd.md) [event](structnet__socket__service__event.md#a8246a87e2171474eb214bb8f909cb9bf);

[ 45](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638) void \*[user\_data](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638);

[ 47](structnet__socket__service__event.md#a7052fad6a65c5a1b610a69e16fc72785) struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*[svc](structnet__socket__service__event.md#a7052fad6a65c5a1b610a69e16fc72785);

48};

49

[ 60](structnet__socket__service__desc.md)struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) {

61#if CONFIG\_NET\_SOCKETS\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

[ 66](structnet__socket__service__desc.md#a08da5714fafa3f678771ea3d5204971a) const char \*[owner](structnet__socket__service__desc.md#a08da5714fafa3f678771ea3d5204971a);

67#endif

[ 69](structnet__socket__service__desc.md#a6cabae5e1fa0fd56c626932c7c1beca3) struct [k\_work\_q](structk__work__q.md) \*[work\_q](structnet__socket__service__desc.md#a6cabae5e1fa0fd56c626932c7c1beca3);

[ 71](structnet__socket__service__desc.md#a62104a9136d2abd88c25480eee2b187a) struct [net\_socket\_service\_event](structnet__socket__service__event.md) \*[pev](structnet__socket__service__desc.md#a62104a9136d2abd88c25480eee2b187a);

[ 73](structnet__socket__service__desc.md#a5c958339cbc98e7c4490952ce1e9fbc9) int [pev\_len](structnet__socket__service__desc.md#a5c958339cbc98e7c4490952ce1e9fbc9);

[ 75](structnet__socket__service__desc.md#a480b960a8d130ded4668f355a8e5fd83) int \*[idx](structnet__socket__service__desc.md#a480b960a8d130ded4668f355a8e5fd83);

76};

77

78#define \_\_z\_net\_socket\_svc\_get\_name(\_svc\_id) \_\_z\_net\_socket\_service\_##\_svc\_id

79#define \_\_z\_net\_socket\_svc\_get\_idx(\_svc\_id) \_\_z\_net\_socket\_service\_idx\_##\_svc\_id

80#define \_\_z\_net\_socket\_svc\_get\_owner \_\_FILE\_\_ ":" STRINGIFY(\_\_LINE\_\_)

81

[ 82](group__bsd__socket__service.md#gabc4e886434f991cf2602cb9a02b01def)extern void [net\_socket\_service\_callback](group__bsd__socket__service.md#gabc4e886434f991cf2602cb9a02b01def)(struct [k\_work](structk__work.md) \*[work](structnet__socket__service__event.md#a0bf2c9e1fc2b8125db3fd907ed6ea27c));

83

84#if CONFIG\_NET\_SOCKETS\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

[ 85](group__bsd__socket__service.md#gaace6e67354416068761145713ab96ba8)#define NET\_SOCKET\_SERVICE\_OWNER .owner = \_\_z\_net\_socket\_svc\_get\_owner,

86#else

87#define NET\_SOCKET\_SERVICE\_OWNER

88#endif

89

[ 90](group__bsd__socket__service.md#ga1839e4e6640eadccb3538b71420920b3)#define NET\_SOCKET\_SERVICE\_CALLBACK\_MODE(\_flag) \

91 IF\_ENABLED(\_flag, \

92 (.work = Z\_WORK\_INITIALIZER(net\_socket\_service\_callback),))

93

94#define \_\_z\_net\_socket\_service\_define(\_name, \_work\_q, \_cb, \_count, \_async, ...) \

95 static int \_\_z\_net\_socket\_svc\_get\_idx(\_name); \

96 static struct net\_socket\_service\_event \

97 \_\_z\_net\_socket\_svc\_get\_name(\_name)[\_count] = { \

98 [0 ... ((\_count) - 1)] = { \

99 .event.fd = -1, /\* Invalid socket \*/ \

100 NET\_SOCKET\_SERVICE\_CALLBACK\_MODE(\_async) \

101 .callback = \_cb, \

102 } \

103 }; \

104 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (), \_\_VA\_ARGS\_\_) \

105 const STRUCT\_SECTION\_ITERABLE(net\_socket\_service\_desc, \_name) = { \

106 NET\_SOCKET\_SERVICE\_OWNER \

107 .work\_q = (\_work\_q), \

108 .pev = \_\_z\_net\_socket\_svc\_get\_name(\_name), \

109 .pev\_len = (\_count), \

110 .idx = &\_\_z\_net\_socket\_svc\_get\_idx(\_name), \

111 }

112

[ 133](group__bsd__socket__service.md#ga9f5934aa42f360d1ec67369eec82b358)#define NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE(name, work\_q, cb, count) \

134 \_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 1)

135

[ 148](group__bsd__socket__service.md#ga3fa2f4f552534d61c1699575c7c8e13d)#define NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE\_STATIC(name, work\_q, cb, count) \

149 \_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 1, static)

150

[ 171](group__bsd__socket__service.md#gac30346044fa5a7b97a0c347edeb989b2)#define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE(name, work\_q, cb, count) \

172 \_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 0)

173

[ 186](group__bsd__socket__service.md#gac80104c4c86380194d847089d31d9acf)#define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC(name, work\_q, cb, count) \

187 \_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 0, static)

188

[ 201](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)\_\_syscall int [net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service,

202 struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int len, void \*[user\_data](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638));

203

[ 213](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6)static inline int [net\_socket\_service\_unregister](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6)(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service)

214{

215 return [net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)(service, NULL, 0, NULL);

216}

217

[ 225](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd)typedef void (\*[net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd))(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*svc,

226 void \*user\_data);

227

[ 234](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097)void [net\_socket\_service\_foreach](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097)([net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd) cb, void \*user\_data);

235

236#ifdef \_\_cplusplus

237}

238#endif

239

240#include <syscalls/socket\_service.h>

241

245

246#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_SERVICE\_H\_ \*/

[net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd)

void(\* net\_socket\_service\_cb\_t)(const struct net\_socket\_service\_desc \*svc, void \*user\_data)

Callback used while iterating over socket services.

**Definition** socket\_service.h:225

[net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091)

int net\_socket\_service\_register(const struct net\_socket\_service\_desc \*service, struct zsock\_pollfd \*fds, int len, void \*user\_data)

Register pollable sockets.

[net\_socket\_service\_callback](group__bsd__socket__service.md#gabc4e886434f991cf2602cb9a02b01def)

void net\_socket\_service\_callback(struct k\_work \*work)

[net\_socket\_service\_foreach](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097)

void net\_socket\_service\_foreach(net\_socket\_service\_cb\_t cb, void \*user\_data)

Go through all the socket services and call callback for each service.

[net\_socket\_service\_unregister](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6)

static int net\_socket\_service\_unregister(const struct net\_socket\_service\_desc \*service)

Unregister pollable sockets.

**Definition** socket\_service.h:213

[k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)

void(\* k\_work\_handler\_t)(struct k\_work \*work)

The signature for a work item handler function.

**Definition** kernel.h:3262

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[k\_work\_q](structk__work__q.md)

A structure used to hold work until it can be processed.

**Definition** kernel.h:4008

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[net\_socket\_service\_desc](structnet__socket__service__desc.md)

Main structure holding socket service configuration information.

**Definition** socket\_service.h:60

[net\_socket\_service\_desc::owner](structnet__socket__service__desc.md#a08da5714fafa3f678771ea3d5204971a)

const char \* owner

Owner name.

**Definition** socket\_service.h:66

[net\_socket\_service\_desc::idx](structnet__socket__service__desc.md#a480b960a8d130ded4668f355a8e5fd83)

int \* idx

Where are my pollfd entries in the global list.

**Definition** socket\_service.h:75

[net\_socket\_service\_desc::pev\_len](structnet__socket__service__desc.md#a5c958339cbc98e7c4490952ce1e9fbc9)

int pev\_len

Length of the pollable socket array for this service.

**Definition** socket\_service.h:73

[net\_socket\_service\_desc::pev](structnet__socket__service__desc.md#a62104a9136d2abd88c25480eee2b187a)

struct net\_socket\_service\_event \* pev

Pointer to the list of services that we are listening.

**Definition** socket\_service.h:71

[net\_socket\_service\_desc::work\_q](structnet__socket__service__desc.md#a6cabae5e1fa0fd56c626932c7c1beca3)

struct k\_work\_q \* work\_q

Workqueue where the work is submitted.

**Definition** socket\_service.h:69

[net\_socket\_service\_event](structnet__socket__service__event.md)

This struct contains information which socket triggered calls to the callback function.

**Definition** socket\_service.h:37

[net\_socket\_service\_event::work](structnet__socket__service__event.md#a0bf2c9e1fc2b8125db3fd907ed6ea27c)

struct k\_work work

k\_work that is done when there is desired activity in file descriptor.

**Definition** socket\_service.h:39

[net\_socket\_service\_event::callback](structnet__socket__service__event.md#a1af4ca9e8076f0725d90f535fbbb94c4)

k\_work\_handler\_t callback

Callback to be called for desired socket activity.

**Definition** socket\_service.h:41

[net\_socket\_service\_event::svc](structnet__socket__service__event.md#a7052fad6a65c5a1b610a69e16fc72785)

struct net\_socket\_service\_desc \* svc

Service back pointer.

**Definition** socket\_service.h:47

[net\_socket\_service\_event::event](structnet__socket__service__event.md#a8246a87e2171474eb214bb8f909cb9bf)

struct zsock\_pollfd event

Socket information that triggered this event.

**Definition** socket\_service.h:43

[net\_socket\_service\_event::user\_data](structnet__socket__service__event.md#aa11bb43a2cc48d167bf8995d860fd638)

void \* user\_data

User data.

**Definition** socket\_service.h:45

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket.h:43

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_service.h](socket__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
