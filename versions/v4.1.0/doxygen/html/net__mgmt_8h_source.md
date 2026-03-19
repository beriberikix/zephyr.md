---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__mgmt_8h_source.html
original_path: doxygen/html/net__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_mgmt.h

[Go to the documentation of this file.](net__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_

14

15#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

16#include <[zephyr/net/net\_core.h](net__core_8h.md)>

17#include <[zephyr/net/net\_event.h](net__event_8h.md)>

18#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

32

33struct [net\_if](structnet__if.md);

34

39#define NET\_MGMT\_EVENT\_MASK 0x80000000

40#define NET\_MGMT\_ON\_IFACE\_MASK 0x40000000

41#define NET\_MGMT\_LAYER\_MASK 0x30000000

42#define NET\_MGMT\_SYNC\_EVENT\_MASK 0x08000000

43#define NET\_MGMT\_LAYER\_CODE\_MASK 0x07FF0000

44#define NET\_MGMT\_COMMAND\_MASK 0x0000FFFF

45

46#define NET\_MGMT\_EVENT\_BIT BIT(31)

47#define NET\_MGMT\_IFACE\_BIT BIT(30)

48#define NET\_MGMT\_SYNC\_EVENT\_BIT BIT(27)

49

50#define NET\_MGMT\_LAYER(\_layer) (\_layer << 28)

51#define NET\_MGMT\_LAYER\_CODE(\_code) (\_code << 16)

52

53#define NET\_MGMT\_EVENT(mgmt\_request) \

54 (mgmt\_request & NET\_MGMT\_EVENT\_MASK)

55

56#define NET\_MGMT\_ON\_IFACE(mgmt\_request) \

57 (mgmt\_request & NET\_MGMT\_ON\_IFACE\_MASK)

58

59#define NET\_MGMT\_EVENT\_SYNCHRONOUS(mgmt\_request) \

60 (mgmt\_request & NET\_MGMT\_SYNC\_EVENT\_MASK)

61

62#define NET\_MGMT\_GET\_LAYER(mgmt\_request) \

63 ((mgmt\_request & NET\_MGMT\_LAYER\_MASK) >> 28)

64

65#define NET\_MGMT\_GET\_LAYER\_CODE(mgmt\_request) \

66 ((mgmt\_request & NET\_MGMT\_LAYER\_CODE\_MASK) >> 16)

67

68#define NET\_MGMT\_GET\_COMMAND(mgmt\_request) \

69 (mgmt\_request & NET\_MGMT\_COMMAND\_MASK)

70

71

72/\* Useful generic definitions \*/

73#define NET\_MGMT\_LAYER\_L2 1

74#define NET\_MGMT\_LAYER\_L3 2

75#define NET\_MGMT\_LAYER\_L4 3

76

78

79

[ 91](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056)typedef int (\*[net\_mgmt\_request\_handler\_t](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request,

92 struct [net\_if](structnet__if.md) \*iface,

93 void \*data, size\_t len);

94

[ 103](group__net__mgmt.md#ga40e0f9fc86812ad9f6fe174b4c3804e6)#define net\_mgmt(\_mgmt\_request, \_iface, \_data, \_len) \

104 net\_mgmt\_##\_mgmt\_request(\_mgmt\_request, \_iface, \_data, \_len)

105

[ 111](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request) \

112 extern int net\_mgmt\_##\_mgmt\_request(uint32\_t mgmt\_request, \

113 struct net\_if \*iface, \

114 void \*data, size\_t len)

115

[ 122](group__net__mgmt.md#gab67d09d1e65b806ec1957451cbf60501)#define NET\_MGMT\_REGISTER\_REQUEST\_HANDLER(\_mgmt\_request, \_func) \

123 FUNC\_ALIAS(\_func, net\_mgmt\_##\_mgmt\_request, int)

124

125struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md);

126

[ 135](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f)typedef void (\*[net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f))(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb,

136 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event,

137 struct [net\_if](structnet__if.md) \*iface);

138

[ 145](structnet__mgmt__event__callback.md)struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) {

[ 149](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea);

150

151 union {

[ 154](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2) [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f) [handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2);

[ 158](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3) struct k\_sem \*[sync\_call](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3);

159 };

160

161#ifdef CONFIG\_NET\_MGMT\_EVENT\_INFO

162 const void \*info;

163 size\_t info\_length;

164#endif

165

171 union {

[ 180](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [event\_mask](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589);

[ 184](structnet__mgmt__event__callback.md#a7c92da4524db9294d9a157606b85c497) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raised\_event](structnet__mgmt__event__callback.md#a7c92da4524db9294d9a157606b85c497);

185 };

186};

187

[ 199](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c)typedef void (\*[net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event,

200 struct [net\_if](structnet__if.md) \*iface,

201 void \*info, size\_t info\_length,

202 void \*user\_data);

203

205

206/\* Structure for event handler registered at compile time \*/

207struct net\_mgmt\_event\_static\_handler {

208 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_mask;

209 [net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c) handler;

210 void \*user\_data;

211};

212

214

[ 228](group__net__mgmt.md#ga3a6ca8a72ab12afd4f9b0461253eaa12)#define NET\_MGMT\_REGISTER\_EVENT\_HANDLER(\_name, \_event\_mask, \_func, \_user\_data) \

229 const STRUCT\_SECTION\_ITERABLE(net\_mgmt\_event\_static\_handler, \_name) = { \

230 .event\_mask = \_event\_mask, \

231 .handler = \_func, \

232 .user\_data = (void \*)\_user\_data, \

233 }

234

241#ifdef CONFIG\_NET\_MGMT\_EVENT

242static inline

[ 243](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0)void [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb,

244 [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f) handler,

245 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask)

246{

247 \_\_ASSERT(cb, "Callback pointer should not be NULL");

248 \_\_ASSERT(handler, "Handler pointer should not be NULL");

249

250 cb->[handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2) = handler;

251 cb->[event\_mask](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589) = mgmt\_event\_mask;

252};

253#else

254#define net\_mgmt\_init\_event\_callback(...)

255#endif

256

261#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 262](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)void [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb);

263#else

264#define net\_mgmt\_add\_event\_callback(...)

265#endif

266

271#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 272](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)void [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb);

273#else

274#define net\_mgmt\_del\_event\_callback(...)

275#endif

276

290#if defined(CONFIG\_NET\_MGMT\_EVENT)

[ 291](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)void [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface,

292 const void \*info, size\_t length);

293#else

294#define net\_mgmt\_event\_notify\_with\_info(...)

295#endif

296

303#if defined(CONFIG\_NET\_MGMT\_EVENT)

[ 304](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)static inline void [net\_mgmt\_event\_notify](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event,

305 struct [net\_if](structnet__if.md) \*iface)

306{

307 [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)(mgmt\_event, iface, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0);

308}

309#else

310#define net\_mgmt\_event\_notify(...)

311#endif

312

333#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 334](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)int [net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

335 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

336 struct [net\_if](structnet__if.md) \*\*iface,

337 const void \*\*info,

338 size\_t \*info\_length,

339 [k\_timeout\_t](structk__timeout__t.md) timeout);

340#else

341static inline int [net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

342 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

343 struct [net\_if](structnet__if.md) \*\*iface,

344 const void \*\*info,

345 size\_t \*info\_length,

346 [k\_timeout\_t](structk__timeout__t.md) timeout)

347{

348 return 0;

349}

350#endif

351

371#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 372](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)int [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)(struct [net\_if](structnet__if.md) \*iface,

373 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

374 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

375 const void \*\*info,

376 size\_t \*info\_length,

377 [k\_timeout\_t](structk__timeout__t.md) timeout);

378#else

379static inline int [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)(struct [net\_if](structnet__if.md) \*iface,

380 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

381 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

382 const void \*\*info,

383 size\_t \*info\_length,

384 [k\_timeout\_t](structk__timeout__t.md) timeout)

385{

386 return 0;

387}

388#endif

389

394#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 395](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)void [net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)(void);

396#else

397#define net\_mgmt\_event\_init(...)

398#endif /\* CONFIG\_NET\_MGMT\_EVENT \*/

399

403

404#ifdef \_\_cplusplus

405}

406#endif

407

408#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)

int net\_mgmt\_event\_wait\_on\_iface(struct net\_if \*iface, uint32\_t mgmt\_event\_mask, uint32\_t \*raised\_event, const void \*\*info, size\_t \*info\_length, k\_timeout\_t timeout)

Used to wait synchronously on an event mask for a specific iface.

[net\_mgmt\_event\_notify](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)

static void net\_mgmt\_event\_notify(uint32\_t mgmt\_event, struct net\_if \*iface)

Used by the system to notify an event without any additional information.

**Definition** net\_mgmt.h:304

[net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)

void net\_mgmt\_event\_notify\_with\_info(uint32\_t mgmt\_event, struct net\_if \*iface, const void \*info, size\_t length)

Used by the system to notify an event.

[net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c)

void(\* net\_mgmt\_event\_static\_handler\_t)(uint32\_t mgmt\_event, struct net\_if \*iface, void \*info, size\_t info\_length, void \*user\_data)

Define the user's callback handler function signature.

**Definition** net\_mgmt.h:199

[net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)

void net\_mgmt\_del\_event\_callback(struct net\_mgmt\_event\_callback \*cb)

Delete a user callback.

[net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0)

static void net\_mgmt\_init\_event\_callback(struct net\_mgmt\_event\_callback \*cb, net\_mgmt\_event\_handler\_t handler, uint32\_t mgmt\_event\_mask)

Helper to initialize a struct net\_mgmt\_event\_callback properly.

**Definition** net\_mgmt.h:243

[net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)

void net\_mgmt\_event\_init(void)

Used by the core of the network stack to initialize the network event processing.

[net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)

int net\_mgmt\_event\_wait(uint32\_t mgmt\_event\_mask, uint32\_t \*raised\_event, struct net\_if \*\*iface, const void \*\*info, size\_t \*info\_length, k\_timeout\_t timeout)

Used to wait synchronously on an event mask.

[net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f)

void(\* net\_mgmt\_event\_handler\_t)(struct net\_mgmt\_event\_callback \*cb, uint32\_t mgmt\_event, struct net\_if \*iface)

Define the user's callback handler function signature.

**Definition** net\_mgmt.h:135

[net\_mgmt\_request\_handler\_t](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056)

int(\* net\_mgmt\_request\_handler\_t)(uint32\_t mgmt\_request, struct net\_if \*iface, void \*data, size\_t len)

Signature which all Net MGMT request handler need to follow.

**Definition** net\_mgmt.h:91

[net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)

void net\_mgmt\_add\_event\_callback(struct net\_mgmt\_event\_callback \*cb)

Add a user callback.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_event.h](net__event_8h.md)

Network Events code public header.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md)

Network Management event callback structure Used to register a callback into the network management e...

**Definition** net\_mgmt.h:145

[net\_mgmt\_event\_callback::node](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea)

sys\_snode\_t node

Meant to be used internally, to insert the callback into a list.

**Definition** net\_mgmt.h:149

[net\_mgmt\_event\_callback::sync\_call](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3)

struct k\_sem \* sync\_call

Semaphore meant to be used internally for the synchronous net\_mgmt\_event\_wait() function.

**Definition** net\_mgmt.h:158

[net\_mgmt\_event\_callback::raised\_event](structnet__mgmt__event__callback.md#a7c92da4524db9294d9a157606b85c497)

uint32\_t raised\_event

Internal place holder when a synchronous event wait is successfully unlocked on a event.

**Definition** net\_mgmt.h:184

[net\_mgmt\_event\_callback::event\_mask](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589)

uint32\_t event\_mask

A mask of network events on which the above handler should be called in case those events come.

**Definition** net\_mgmt.h:180

[net\_mgmt\_event\_callback::handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2)

net\_mgmt\_event\_handler\_t handler

Actual callback function being used to notify the owner.

**Definition** net\_mgmt.h:154

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_mgmt.h](net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
