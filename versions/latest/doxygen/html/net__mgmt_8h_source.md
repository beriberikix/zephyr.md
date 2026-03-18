---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__mgmt_8h_source.html
original_path: doxygen/html/net__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

30

31struct [net\_if](structnet__if.md);

32

37#define NET\_MGMT\_EVENT\_MASK 0x80000000

38#define NET\_MGMT\_ON\_IFACE\_MASK 0x40000000

39#define NET\_MGMT\_LAYER\_MASK 0x30000000

40#define NET\_MGMT\_SYNC\_EVENT\_MASK 0x08000000

41#define NET\_MGMT\_LAYER\_CODE\_MASK 0x07FF0000

42#define NET\_MGMT\_COMMAND\_MASK 0x0000FFFF

43

44#define NET\_MGMT\_EVENT\_BIT BIT(31)

45#define NET\_MGMT\_IFACE\_BIT BIT(30)

46#define NET\_MGMT\_SYNC\_EVENT\_BIT BIT(27)

47

48#define NET\_MGMT\_LAYER(\_layer) (\_layer << 28)

49#define NET\_MGMT\_LAYER\_CODE(\_code) (\_code << 16)

50

51#define NET\_MGMT\_EVENT(mgmt\_request) \

52 (mgmt\_request & NET\_MGMT\_EVENT\_MASK)

53

54#define NET\_MGMT\_ON\_IFACE(mgmt\_request) \

55 (mgmt\_request & NET\_MGMT\_ON\_IFACE\_MASK)

56

57#define NET\_MGMT\_EVENT\_SYNCHRONOUS(mgmt\_request) \

58 (mgmt\_request & NET\_MGMT\_SYNC\_EVENT\_MASK)

59

60#define NET\_MGMT\_GET\_LAYER(mgmt\_request) \

61 ((mgmt\_request & NET\_MGMT\_LAYER\_MASK) >> 28)

62

63#define NET\_MGMT\_GET\_LAYER\_CODE(mgmt\_request) \

64 ((mgmt\_request & NET\_MGMT\_LAYER\_CODE\_MASK) >> 16)

65

66#define NET\_MGMT\_GET\_COMMAND(mgmt\_request) \

67 (mgmt\_request & NET\_MGMT\_COMMAND\_MASK)

68

69

70/\* Useful generic definitions \*/

71#define NET\_MGMT\_LAYER\_L2 1

72#define NET\_MGMT\_LAYER\_L3 2

73#define NET\_MGMT\_LAYER\_L4 3

74

76

77

[ 89](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056)typedef int (\*[net\_mgmt\_request\_handler\_t](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request,

90 struct [net\_if](structnet__if.md) \*iface,

91 void \*data, size\_t len);

92

[ 93](group__net__mgmt.md#ga40e0f9fc86812ad9f6fe174b4c3804e6)#define net\_mgmt(\_mgmt\_request, \_iface, \_data, \_len) \

94 net\_mgmt\_##\_mgmt\_request(\_mgmt\_request, \_iface, \_data, \_len)

95

[ 96](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request) \

97 extern int net\_mgmt\_##\_mgmt\_request(uint32\_t mgmt\_request, \

98 struct net\_if \*iface, \

99 void \*data, size\_t len)

100

[ 101](group__net__mgmt.md#gab67d09d1e65b806ec1957451cbf60501)#define NET\_MGMT\_REGISTER\_REQUEST\_HANDLER(\_mgmt\_request, \_func) \

102 FUNC\_ALIAS(\_func, net\_mgmt\_##\_mgmt\_request, int)

103

104struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md);

105

[ 114](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f)typedef void (\*[net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f))(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb,

115 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event,

116 struct [net\_if](structnet__if.md) \*iface);

117

[ 124](structnet__mgmt__event__callback.md)struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) {

[ 128](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea);

129

130 union {

[ 133](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2) [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f) [handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2);

[ 137](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3) struct k\_sem \*[sync\_call](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3);

138 };

139

140#ifdef CONFIG\_NET\_MGMT\_EVENT\_INFO

141 const void \*info;

142 size\_t info\_length;

143#endif

144

150 union {

[ 159](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [event\_mask](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589);

[ 163](structnet__mgmt__event__callback.md#a7c92da4524db9294d9a157606b85c497) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raised\_event](structnet__mgmt__event__callback.md#a7c92da4524db9294d9a157606b85c497);

164 };

165};

166

[ 178](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c)typedef void (\*[net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event,

179 struct [net\_if](structnet__if.md) \*iface,

180 void \*info, size\_t info\_length,

181 void \*user\_data);

182

184

185/\* Structure for event handler registered at compile time \*/

186struct net\_mgmt\_event\_static\_handler {

187 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_mask;

188 [net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c) handler;

189 void \*user\_data;

190};

191

193

[ 207](group__net__mgmt.md#ga3a6ca8a72ab12afd4f9b0461253eaa12)#define NET\_MGMT\_REGISTER\_EVENT\_HANDLER(\_name, \_event\_mask, \_func, \_user\_data) \

208 const STRUCT\_SECTION\_ITERABLE(net\_mgmt\_event\_static\_handler, \_name) = { \

209 .event\_mask = \_event\_mask, \

210 .handler = \_func, \

211 .user\_data = (void \*)\_user\_data, \

212 }

213

220#ifdef CONFIG\_NET\_MGMT\_EVENT

221static inline

[ 222](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0)void [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb,

223 [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f) handler,

224 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask)

225{

226 \_\_ASSERT(cb, "Callback pointer should not be NULL");

227 \_\_ASSERT(handler, "Handler pointer should not be NULL");

228

229 cb->[handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2) = handler;

230 cb->[event\_mask](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589) = mgmt\_event\_mask;

231};

232#else

233#define net\_mgmt\_init\_event\_callback(...)

234#endif

235

240#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 241](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)void [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb);

242#else

243#define net\_mgmt\_add\_event\_callback(...)

244#endif

245

250#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 251](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)void [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb);

252#else

253#define net\_mgmt\_del\_event\_callback(...)

254#endif

255

269#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 270](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)void [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface,

271 const void \*info, size\_t length);

272

[ 273](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)static inline void [net\_mgmt\_event\_notify](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event,

274 struct [net\_if](structnet__if.md) \*iface)

275{

276 [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)(mgmt\_event, iface, NULL, 0);

277}

278#else

279#define net\_mgmt\_event\_notify(...)

280#define net\_mgmt\_event\_notify\_with\_info(...)

281#endif

282

303#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 304](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)int [net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

305 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

306 struct [net\_if](structnet__if.md) \*\*iface,

307 const void \*\*info,

308 size\_t \*info\_length,

309 [k\_timeout\_t](structk__timeout__t.md) timeout);

310#else

311static inline int [net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

312 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

313 struct [net\_if](structnet__if.md) \*\*iface,

314 const void \*\*info,

315 size\_t \*info\_length,

316 [k\_timeout\_t](structk__timeout__t.md) timeout)

317{

318 return 0;

319}

320#endif

321

341#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 342](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)int [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)(struct [net\_if](structnet__if.md) \*iface,

343 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

344 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

345 const void \*\*info,

346 size\_t \*info\_length,

347 [k\_timeout\_t](structk__timeout__t.md) timeout);

348#else

349static inline int [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)(struct [net\_if](structnet__if.md) \*iface,

350 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask,

351 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event,

352 const void \*\*info,

353 size\_t \*info\_length,

354 [k\_timeout\_t](structk__timeout__t.md) timeout)

355{

356 return 0;

357}

358#endif

359

364#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 365](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)void [net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)(void);

366#else

367#define net\_mgmt\_event\_init(...)

368#endif /\* CONFIG\_NET\_MGMT\_EVENT \*/

369

373

374#ifdef \_\_cplusplus

375}

376#endif

377

378#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d)

int net\_mgmt\_event\_wait\_on\_iface(struct net\_if \*iface, uint32\_t mgmt\_event\_mask, uint32\_t \*raised\_event, const void \*\*info, size\_t \*info\_length, k\_timeout\_t timeout)

Used to wait synchronously on an event mask for a specific iface.

[net\_mgmt\_event\_notify](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0)

static void net\_mgmt\_event\_notify(uint32\_t mgmt\_event, struct net\_if \*iface)

**Definition** net\_mgmt.h:273

[net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d)

void net\_mgmt\_event\_notify\_with\_info(uint32\_t mgmt\_event, struct net\_if \*iface, const void \*info, size\_t length)

Used by the system to notify an event.

[net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c)

void(\* net\_mgmt\_event\_static\_handler\_t)(uint32\_t mgmt\_event, struct net\_if \*iface, void \*info, size\_t info\_length, void \*user\_data)

Define the user's callback handler function signature.

**Definition** net\_mgmt.h:178

[net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)

void net\_mgmt\_del\_event\_callback(struct net\_mgmt\_event\_callback \*cb)

Delete a user callback.

[net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0)

static void net\_mgmt\_init\_event\_callback(struct net\_mgmt\_event\_callback \*cb, net\_mgmt\_event\_handler\_t handler, uint32\_t mgmt\_event\_mask)

Helper to initialize a struct net\_mgmt\_event\_callback properly.

**Definition** net\_mgmt.h:222

[net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)

void net\_mgmt\_event\_init(void)

Used by the core of the network stack to initialize the network event processing.

[net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17)

int net\_mgmt\_event\_wait(uint32\_t mgmt\_event\_mask, uint32\_t \*raised\_event, struct net\_if \*\*iface, const void \*\*info, size\_t \*info\_length, k\_timeout\_t timeout)

Used to wait synchronously on an event mask.

[net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f)

void(\* net\_mgmt\_event\_handler\_t)(struct net\_mgmt\_event\_callback \*cb, uint32\_t mgmt\_event, struct net\_if \*iface)

Define the user's callback handler function signature.

**Definition** net\_mgmt.h:114

[net\_mgmt\_request\_handler\_t](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056)

int(\* net\_mgmt\_request\_handler\_t)(uint32\_t mgmt\_request, struct net\_if \*iface, void \*data, size\_t len)

Signature which all Net MGMT request handler need to follow.

**Definition** net\_mgmt.h:89

[net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)

void net\_mgmt\_add\_event\_callback(struct net\_mgmt\_event\_callback \*cb)

Add a user callback.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

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

**Definition** net\_if.h:615

[net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md)

Network Management event callback structure Used to register a callback into the network management e...

**Definition** net\_mgmt.h:124

[net\_mgmt\_event\_callback::node](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea)

sys\_snode\_t node

Meant to be used internally, to insert the callback into a list.

**Definition** net\_mgmt.h:128

[net\_mgmt\_event\_callback::sync\_call](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3)

struct k\_sem \* sync\_call

Semaphore meant to be used internally for the synchronous net\_mgmt\_event\_wait() function.

**Definition** net\_mgmt.h:137

[net\_mgmt\_event\_callback::raised\_event](structnet__mgmt__event__callback.md#a7c92da4524db9294d9a157606b85c497)

uint32\_t raised\_event

Internal place holder when a synchronous event wait is successfully unlocked on a event.

**Definition** net\_mgmt.h:163

[net\_mgmt\_event\_callback::event\_mask](structnet__mgmt__event__callback.md#acd2d06e59f71b30e6d9089c165c4a589)

uint32\_t event\_mask

A mask of network events on which the above handler should be called in case those events come.

**Definition** net\_mgmt.h:159

[net\_mgmt\_event\_callback::handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2)

net\_mgmt\_event\_handler\_t handler

Actual callback function being used to notify the owner.

**Definition** net\_mgmt.h:133

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_mgmt.h](net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
