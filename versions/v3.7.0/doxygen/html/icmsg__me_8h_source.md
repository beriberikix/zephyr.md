---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/icmsg__me_8h_source.html
original_path: doxygen/html/icmsg__me_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg\_me.h

[Go to the documentation of this file.](icmsg__me_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_ICMSG\_ME\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_ICMSG\_ME\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/ipc/icmsg.h](icmsg_8h.md)>

13#include <[zephyr/ipc/ipc\_service.h](ipc__service_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

26

27/\* If more bytes than 1 was used for endpoint id, endianness should be

28 \* considered.

29 \*/

[ 30](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a);

31

[ 32](structicmsg__me__data__t.md)struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) {

[ 33](structicmsg__me__data__t.md#a30c97ed414ba4ac68c0fa9d5d4127f86) struct [icmsg\_data\_t](structicmsg__data__t.md) [icmsg\_data](structicmsg__me__data__t.md#a30c97ed414ba4ac68c0fa9d5d4127f86);

[ 34](structicmsg__me__data__t.md#aedeb458feb87b705f2af3464bcbc8a17) struct [ipc\_ept\_cfg](structipc__ept__cfg.md) [ept\_cfg](structicmsg__me__data__t.md#aedeb458feb87b705f2af3464bcbc8a17);

35

[ 36](structicmsg__me__data__t.md#a9507ab4a6ef840977f798c594e2a42ae) struct [k\_event](structk__event.md) [event](structicmsg__me__data__t.md#a9507ab4a6ef840977f798c594e2a42ae);

37

[ 38](structicmsg__me__data__t.md#ac0b88ca87a800867ae21a0224cc7bf59) struct [k\_mutex](structk__mutex.md) [send\_mutex](structicmsg__me__data__t.md#ac0b88ca87a800867ae21a0224cc7bf59);

[ 39](structicmsg__me__data__t.md#ae76a1543acaff158c768e726b8c460e5) const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*[epts](structicmsg__me__data__t.md#ae76a1543acaff158c768e726b8c460e5)[CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_NUM\_EP];

40

[ 41](structicmsg__me__data__t.md#a5e5809e811ff0689ab8530298490f943) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [send\_buffer](structicmsg__me__data__t.md#a5e5809e811ff0689ab8530298490f943)[CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_SEND\_BUF\_SIZE] \_\_aligned(4);

42};

43

44

[ 62](group__ipc__icmsg__me__api.md#ga12cc5855f2fbca5506f647ced473c71f)int [icmsg\_me\_init](group__ipc__icmsg__me__api.md#ga12cc5855f2fbca5506f647ced473c71f)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

63 struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data);

64

[ 90](group__ipc__icmsg__me__api.md#gabfd5487133994614cf3dd9b648279673)int [icmsg\_me\_open](group__ipc__icmsg__me__api.md#gabfd5487133994614cf3dd9b648279673)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

91 struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data,

92 const struct [ipc\_service\_cb](structipc__service__cb.md) \*[cb](structipc__ept__cfg.md#a0cd24dc49dbfe7f8cda02ee37d36529c),

93 void \*ctx);

94

[ 110](group__ipc__icmsg__me__api.md#ga0f96e65e6b0f4ef05147a4afb1dc3184)void [icmsg\_me\_wait\_for\_icmsg\_bind](group__ipc__icmsg__me__api.md#ga0f96e65e6b0f4ef05147a4afb1dc3184)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data);

111

[ 123](group__ipc__icmsg__me__api.md#ga5ddaefd30fdee07af3f80d0239e9cce0)void [icmsg\_me\_icmsg\_bound](group__ipc__icmsg__me__api.md#ga5ddaefd30fdee07af3f80d0239e9cce0)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data);

124

[ 141](group__ipc__icmsg__me__api.md#gad667798588efc1689c2eec81147a229e)void [icmsg\_me\_received\_data](group__ipc__icmsg__me__api.md#gad667798588efc1689c2eec81147a229e)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id,

142 const void \*msg, size\_t len);

143

[ 169](group__ipc__icmsg__me__api.md#ga20ac43faf9803b14ed0bacefb527ee3f)int [icmsg\_me\_set\_empty\_ept\_cfg\_slot](group__ipc__icmsg__me__api.md#ga20ac43faf9803b14ed0bacefb527ee3f)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data,

170 const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*ept\_cfg,

171 [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) \*id);

172

[ 191](group__ipc__icmsg__me__api.md#gaf04015b3666ef8e2a923d4d63c093474)int [icmsg\_me\_set\_ept\_cfg](group__ipc__icmsg__me__api.md#gaf04015b3666ef8e2a923d4d63c093474)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id,

192 const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*ept\_cfg);

193

[ 212](group__ipc__icmsg__me__api.md#ga6bece3eb1bef849200feca959fbb3d1b)int [icmsg\_me\_get\_ept\_cfg](group__ipc__icmsg__me__api.md#ga6bece3eb1bef849200feca959fbb3d1b)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id,

213 const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*\*ept\_cfg);

214

[ 227](group__ipc__icmsg__me__api.md#ga8581afc32d8c68193f597754397f8964)void [icmsg\_me\_reset\_ept\_cfg](group__ipc__icmsg__me__api.md#ga8581afc32d8c68193f597754397f8964)(struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id);

228

[ 246](group__ipc__icmsg__me__api.md#ga617f05b24cccc8557ca447e94c3f2702)int [icmsg\_me\_send](group__ipc__icmsg__me__api.md#ga617f05b24cccc8557ca447e94c3f2702)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

247 struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id,

248 const void \*msg, size\_t len);

249

253

254#ifdef \_\_cplusplus

255}

256#endif

257

258#endif /\* ZEPHYR\_INCLUDE\_IPC\_ICMSG\_ME\_H\_ \*/

[icmsg\_me\_wait\_for\_icmsg\_bind](group__ipc__icmsg__me__api.md#ga0f96e65e6b0f4ef05147a4afb1dc3184)

void icmsg\_me\_wait\_for\_icmsg\_bind(struct icmsg\_me\_data\_t \*data)

Wait until the underlying icmsg instance calls bound callback.

[icmsg\_me\_init](group__ipc__icmsg__me__api.md#ga12cc5855f2fbca5506f647ced473c71f)

int icmsg\_me\_init(const struct icmsg\_config\_t \*conf, struct icmsg\_me\_data\_t \*data)

Initialize an icmsg\_me instance.

[icmsg\_me\_set\_empty\_ept\_cfg\_slot](group__ipc__icmsg__me__api.md#ga20ac43faf9803b14ed0bacefb527ee3f)

int icmsg\_me\_set\_empty\_ept\_cfg\_slot(struct icmsg\_me\_data\_t \*data, const struct ipc\_ept\_cfg \*ept\_cfg, icmsg\_me\_ept\_id\_t \*id)

Set endpoint configuration in an empty endpoint slot.

[icmsg\_me\_icmsg\_bound](group__ipc__icmsg__me__api.md#ga5ddaefd30fdee07af3f80d0239e9cce0)

void icmsg\_me\_icmsg\_bound(struct icmsg\_me\_data\_t \*data)

Notify the icmsg\_me instance that the underlying icmsg was bound.

[icmsg\_me\_send](group__ipc__icmsg__me__api.md#ga617f05b24cccc8557ca447e94c3f2702)

int icmsg\_me\_send(const struct icmsg\_config\_t \*conf, struct icmsg\_me\_data\_t \*data, icmsg\_me\_ept\_id\_t id, const void \*msg, size\_t len)

Send a message to the remote icmsg\_me endpoint.

[icmsg\_me\_get\_ept\_cfg](group__ipc__icmsg__me__api.md#ga6bece3eb1bef849200feca959fbb3d1b)

int icmsg\_me\_get\_ept\_cfg(struct icmsg\_me\_data\_t \*data, icmsg\_me\_ept\_id\_t id, const struct ipc\_ept\_cfg \*\*ept\_cfg)

Get endpoint configuration from a selected endpoint slot.

[icmsg\_me\_reset\_ept\_cfg](group__ipc__icmsg__me__api.md#ga8581afc32d8c68193f597754397f8964)

void icmsg\_me\_reset\_ept\_cfg(struct icmsg\_me\_data\_t \*data, icmsg\_me\_ept\_id\_t id)

Reset endpoint configuration in a selected endpoint slot.

[icmsg\_me\_open](group__ipc__icmsg__me__api.md#gabfd5487133994614cf3dd9b648279673)

int icmsg\_me\_open(const struct icmsg\_config\_t \*conf, struct icmsg\_me\_data\_t \*data, const struct ipc\_service\_cb \*cb, void \*ctx)

Open an icmsg\_me instance.

[icmsg\_me\_received\_data](group__ipc__icmsg__me__api.md#gad667798588efc1689c2eec81147a229e)

void icmsg\_me\_received\_data(struct icmsg\_me\_data\_t \*data, icmsg\_me\_ept\_id\_t id, const void \*msg, size\_t len)

Notify the icmsg\_me instance that data for an endpoint was received.

[icmsg\_me\_set\_ept\_cfg](group__ipc__icmsg__me__api.md#gaf04015b3666ef8e2a923d4d63c093474)

int icmsg\_me\_set\_ept\_cfg(struct icmsg\_me\_data\_t \*data, icmsg\_me\_ept\_id\_t id, const struct ipc\_ept\_cfg \*ept\_cfg)

Set endpoint configuration in a selected endpoint slot.

[icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a)

uint8\_t icmsg\_me\_ept\_id\_t

**Definition** icmsg\_me.h:30

[icmsg.h](icmsg_8h.md)

[ipc\_service.h](ipc__service_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[icmsg\_config\_t](structicmsg__config__t.md)

**Definition** icmsg.h:35

[icmsg\_data\_t](structicmsg__data__t.md)

**Definition** icmsg.h:40

[icmsg\_me\_data\_t](structicmsg__me__data__t.md)

**Definition** icmsg\_me.h:32

[icmsg\_me\_data\_t::icmsg\_data](structicmsg__me__data__t.md#a30c97ed414ba4ac68c0fa9d5d4127f86)

struct icmsg\_data\_t icmsg\_data

**Definition** icmsg\_me.h:33

[icmsg\_me\_data\_t::send\_buffer](structicmsg__me__data__t.md#a5e5809e811ff0689ab8530298490f943)

uint8\_t send\_buffer[CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_SEND\_BUF\_SIZE]

**Definition** icmsg\_me.h:41

[icmsg\_me\_data\_t::event](structicmsg__me__data__t.md#a9507ab4a6ef840977f798c594e2a42ae)

struct k\_event event

**Definition** icmsg\_me.h:36

[icmsg\_me\_data\_t::send\_mutex](structicmsg__me__data__t.md#ac0b88ca87a800867ae21a0224cc7bf59)

struct k\_mutex send\_mutex

**Definition** icmsg\_me.h:38

[icmsg\_me\_data\_t::epts](structicmsg__me__data__t.md#ae76a1543acaff158c768e726b8c460e5)

const struct ipc\_ept\_cfg \* epts[CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_NUM\_EP]

**Definition** icmsg\_me.h:39

[icmsg\_me\_data\_t::ept\_cfg](structicmsg__me__data__t.md#aedeb458feb87b705f2af3464bcbc8a17)

struct ipc\_ept\_cfg ept\_cfg

**Definition** icmsg\_me.h:34

[ipc\_ept\_cfg](structipc__ept__cfg.md)

Endpoint configuration structure.

**Definition** ipc\_service.h:191

[ipc\_ept\_cfg::cb](structipc__ept__cfg.md#a0cd24dc49dbfe7f8cda02ee37d36529c)

struct ipc\_service\_cb cb

Event callback structure.

**Definition** ipc\_service.h:200

[ipc\_service\_cb](structipc__service__cb.md)

Event callback structure.

**Definition** ipc\_service.h:145

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2224

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [icmsg\_me.h](icmsg__me_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
