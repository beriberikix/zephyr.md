---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/heap__listener_8h_source.html
original_path: doxygen/html/heap__listener_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

heap\_listener.h

[Go to the documentation of this file.](heap__listener_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_HEAP\_LISTENER\_H

8#define ZEPHYR\_INCLUDE\_SYS\_HEAP\_LISTENER\_H

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#include <[zephyr/sys/slist.h](slist_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#if defined(CONFIG\_HEAP\_LISTENER) || defined(\_\_DOXYGEN\_\_)

19

25

[ 26](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510)enum [heap\_event\_types](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510) {

27 /\*

28 \* Dummy event so an un-initialized but zero-ed listener node

29 \* will not trigger any callbacks.

30 \*/

[ 31](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510ae82b3e0225bde5553f472c5f00985b18) [HEAP\_EVT\_UNKNOWN](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510ae82b3e0225bde5553f472c5f00985b18) = 0,

32

[ 33](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408) [HEAP\_RESIZE](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408),

[ 34](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008) [HEAP\_ALLOC](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008),

[ 35](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80) [HEAP\_FREE](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80),

[ 36](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510aa64f229b21eedbca9a581b60e3da5a50) [HEAP\_REALLOC](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510aa64f229b21eedbca9a581b60e3da5a50),

37

[ 38](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510afb3a6f56a29d74c35db90fbeaa61a3b6) [HEAP\_MAX\_EVENTS](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510afb3a6f56a29d74c35db90fbeaa61a3b6)

39};

40

[ 51](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce)typedef void (\*[heap\_listener\_resize\_cb\_t](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce))([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id,

52 void \*old\_heap\_end,

53 void \*new\_heap\_end);

54

[ 71](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6)typedef void (\*[heap\_listener\_alloc\_cb\_t](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6))([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id,

72 void \*mem, size\_t bytes);

73

[ 90](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f)typedef void (\*[heap\_listener\_free\_cb\_t](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f))([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id,

91 void \*mem, size\_t bytes);

92

[ 93](structheap__listener.md)struct [heap\_listener](structheap__listener.md) {

[ 95](structheap__listener.md#ab0f3071d7828856bcbee55ff9791a27c) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structheap__listener.md#ab0f3071d7828856bcbee55ff9791a27c);

96

[ 103](structheap__listener.md#a9b13bffbb860ea78207b4ebe7c61b768) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [heap\_id](structheap__listener.md#a9b13bffbb860ea78207b4ebe7c61b768);

104

[ 108](structheap__listener.md#a1ef2db791f5422fa7e6bb17c2b6bf247) enum [heap\_event\_types](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510) [event](structheap__listener.md#a1ef2db791f5422fa7e6bb17c2b6bf247);

109

110 union {

[ 111](structheap__listener.md#a34a982da6ecc3564ef2194f045eea646) [heap\_listener\_alloc\_cb\_t](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6) [alloc\_cb](structheap__listener.md#a34a982da6ecc3564ef2194f045eea646);

[ 112](structheap__listener.md#a46a7f4856397851c64ce07c95b1d9b19) [heap\_listener\_free\_cb\_t](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f) [free\_cb](structheap__listener.md#a46a7f4856397851c64ce07c95b1d9b19);

[ 113](structheap__listener.md#a0dcba80daeebe0be96d5e75051cbf287) [heap\_listener\_resize\_cb\_t](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce) [resize\_cb](structheap__listener.md#a0dcba80daeebe0be96d5e75051cbf287);

114 };

115};

116

[ 125](group__heap__listener__apis.md#ga63d5470d9ca312ccc80d35c7f8dea200)void [heap\_listener\_register](group__heap__listener__apis.md#ga63d5470d9ca312ccc80d35c7f8dea200)(struct [heap\_listener](structheap__listener.md) \*listener);

126

[ 136](group__heap__listener__apis.md#ga872e123af0a5349e45fcedfd8b83b508)void [heap\_listener\_unregister](group__heap__listener__apis.md#ga872e123af0a5349e45fcedfd8b83b508)(struct [heap\_listener](structheap__listener.md) \*listener);

137

[ 148](group__heap__listener__apis.md#gaebe49e01cba6d327c635da4795e37e22)void [heap\_listener\_notify\_alloc](group__heap__listener__apis.md#gaebe49e01cba6d327c635da4795e37e22)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, size\_t bytes);

149

[ 160](group__heap__listener__apis.md#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc)void [heap\_listener\_notify\_free](group__heap__listener__apis.md#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, size\_t bytes);

161

[ 172](group__heap__listener__apis.md#ga9d3062fbcdc10edc3839193e8ea79654)void [heap\_listener\_notify\_resize](group__heap__listener__apis.md#ga9d3062fbcdc10edc3839193e8ea79654)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end);

173

[ 182](group__heap__listener__apis.md#ga77e603053a5b69caae2a49e441a525c0)#define HEAP\_ID\_FROM\_POINTER(heap\_pointer) ((uintptr\_t)heap\_pointer)

183

[ 189](group__heap__listener__apis.md#ga7627d1b500bb7e833770c99071f9255d)#define HEAP\_ID\_LIBC ((uintptr\_t)0)

190

[ 208](group__heap__listener__apis.md#ga1854b23cbd41dec0d8262e8f122ebd5d)#define HEAP\_LISTENER\_ALLOC\_DEFINE(name, \_heap\_id, \_alloc\_cb) \

209 struct heap\_listener name = { \

210 .heap\_id = \_heap\_id, \

211 .event = HEAP\_ALLOC, \

212 { \

213 .alloc\_cb = \_alloc\_cb \

214 }, \

215 }

216

[ 234](group__heap__listener__apis.md#ga7e5822ebd4c08235b01cf99cd6fe10e8)#define HEAP\_LISTENER\_FREE\_DEFINE(name, \_heap\_id, \_free\_cb) \

235 struct heap\_listener name = { \

236 .heap\_id = \_heap\_id, \

237 .event = HEAP\_FREE, \

238 { \

239 .free\_cb = \_free\_cb \

240 }, \

241 }

242

[ 260](group__heap__listener__apis.md#gaa4fa9685749e050ca06e7cdc99b7c970)#define HEAP\_LISTENER\_RESIZE\_DEFINE(name, \_heap\_id, \_resize\_cb) \

261 struct heap\_listener name = { \

262 .heap\_id = \_heap\_id, \

263 .event = HEAP\_RESIZE, \

264 { \

265 .resize\_cb = \_resize\_cb \

266 }, \

267 }

268

270

271#else /\* CONFIG\_HEAP\_LISTENER \*/

272

273#define HEAP\_ID\_FROM\_POINTER(heap\_pointer) ((uintptr\_t)NULL)

274

275static inline void [heap\_listener\_notify\_alloc](group__heap__listener__apis.md#gaebe49e01cba6d327c635da4795e37e22)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, size\_t bytes)

276{

277 ARG\_UNUSED(heap\_id);

278 ARG\_UNUSED(mem);

279 ARG\_UNUSED(bytes);

280}

281

282static inline void [heap\_listener\_notify\_free](group__heap__listener__apis.md#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, size\_t bytes)

283{

284 ARG\_UNUSED(heap\_id);

285 ARG\_UNUSED(mem);

286 ARG\_UNUSED(bytes);

287}

288

289static inline void [heap\_listener\_notify\_resize](group__heap__listener__apis.md#ga9d3062fbcdc10edc3839193e8ea79654)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end,

290 void \*new\_heap\_end)

291{

292 ARG\_UNUSED(heap\_id);

293 ARG\_UNUSED(old\_heap\_end);

294 ARG\_UNUSED(new\_heap\_end);

295}

296

297#endif /\* CONFIG\_HEAP\_LISTENER \*/

298

299#ifdef \_\_cplusplus

300}

301#endif

302

303#endif /\* ZEPHYR\_INCLUDE\_SYS\_HEAP\_LISTENER\_H \*/

[heap\_listener\_alloc\_cb\_t](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6)

void(\* heap\_listener\_alloc\_cb\_t)(uintptr\_t heap\_id, void \*mem, size\_t bytes)

Callback used when there is heap allocation.

**Definition** heap\_listener.h:71

[heap\_listener\_register](group__heap__listener__apis.md#ga63d5470d9ca312ccc80d35c7f8dea200)

void heap\_listener\_register(struct heap\_listener \*listener)

Register heap event listener.

[heap\_listener\_unregister](group__heap__listener__apis.md#ga872e123af0a5349e45fcedfd8b83b508)

void heap\_listener\_unregister(struct heap\_listener \*listener)

Unregister heap event listener.

[heap\_listener\_free\_cb\_t](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f)

void(\* heap\_listener\_free\_cb\_t)(uintptr\_t heap\_id, void \*mem, size\_t bytes)

Callback used when memory is freed from heap.

**Definition** heap\_listener.h:90

[heap\_listener\_notify\_free](group__heap__listener__apis.md#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc)

void heap\_listener\_notify\_free(uintptr\_t heap\_id, void \*mem, size\_t bytes)

Notify listeners of heap free event.

[heap\_event\_types](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510)

heap\_event\_types

**Definition** heap\_listener.h:26

[heap\_listener\_notify\_resize](group__heap__listener__apis.md#ga9d3062fbcdc10edc3839193e8ea79654)

void heap\_listener\_notify\_resize(uintptr\_t heap\_id, void \*old\_heap\_end, void \*new\_heap\_end)

Notify listeners of heap resize event.

[heap\_listener\_resize\_cb\_t](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce)

void(\* heap\_listener\_resize\_cb\_t)(uintptr\_t heap\_id, void \*old\_heap\_end, void \*new\_heap\_end)

Callback used when heap is resized.

**Definition** heap\_listener.h:51

[heap\_listener\_notify\_alloc](group__heap__listener__apis.md#gaebe49e01cba6d327c635da4795e37e22)

void heap\_listener\_notify\_alloc(uintptr\_t heap\_id, void \*mem, size\_t bytes)

Notify listeners of heap allocation event.

[HEAP\_RESIZE](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408)

@ HEAP\_RESIZE

**Definition** heap\_listener.h:33

[HEAP\_ALLOC](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008)

@ HEAP\_ALLOC

**Definition** heap\_listener.h:34

[HEAP\_FREE](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80)

@ HEAP\_FREE

**Definition** heap\_listener.h:35

[HEAP\_REALLOC](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510aa64f229b21eedbca9a581b60e3da5a50)

@ HEAP\_REALLOC

**Definition** heap\_listener.h:36

[HEAP\_EVT\_UNKNOWN](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510ae82b3e0225bde5553f472c5f00985b18)

@ HEAP\_EVT\_UNKNOWN

**Definition** heap\_listener.h:31

[HEAP\_MAX\_EVENTS](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510afb3a6f56a29d74c35db90fbeaa61a3b6)

@ HEAP\_MAX\_EVENTS

**Definition** heap\_listener.h:38

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[heap\_listener](structheap__listener.md)

**Definition** heap\_listener.h:93

[heap\_listener::resize\_cb](structheap__listener.md#a0dcba80daeebe0be96d5e75051cbf287)

heap\_listener\_resize\_cb\_t resize\_cb

**Definition** heap\_listener.h:113

[heap\_listener::event](structheap__listener.md#a1ef2db791f5422fa7e6bb17c2b6bf247)

enum heap\_event\_types event

The heap event to be notified.

**Definition** heap\_listener.h:108

[heap\_listener::alloc\_cb](structheap__listener.md#a34a982da6ecc3564ef2194f045eea646)

heap\_listener\_alloc\_cb\_t alloc\_cb

**Definition** heap\_listener.h:111

[heap\_listener::free\_cb](structheap__listener.md#a46a7f4856397851c64ce07c95b1d9b19)

heap\_listener\_free\_cb\_t free\_cb

**Definition** heap\_listener.h:112

[heap\_listener::heap\_id](structheap__listener.md#a9b13bffbb860ea78207b4ebe7c61b768)

uintptr\_t heap\_id

Identifier of the heap whose events are listened.

**Definition** heap\_listener.h:103

[heap\_listener::node](structheap__listener.md#ab0f3071d7828856bcbee55ff9791a27c)

sys\_snode\_t node

Singly linked list node.

**Definition** heap\_listener.h:95

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [heap\_listener.h](heap__listener_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
