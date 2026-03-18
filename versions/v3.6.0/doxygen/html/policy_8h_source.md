---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/policy_8h_source.html
original_path: doxygen/html/policy_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

policy.h

[Go to the documentation of this file.](policy_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PM\_POLICY\_H\_

8#define ZEPHYR\_INCLUDE\_PM\_POLICY\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[stdint.h](stdint_8h.md)>

12

13#include <[zephyr/pm/state.h](state_8h.md)>

14#include <[zephyr/sys/slist.h](slist_8h.md)>

15#include <[zephyr/toolchain.h](toolchain_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 35](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267)typedef void (\*[pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267))([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) latency);

36

[ 42](structpm__policy__latency__subscription.md)struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) {

44 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

45 [pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267) cb;

47};

48

[ 54](structpm__policy__latency__request.md)struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) {

56 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us;

59};

60

[ 66](structpm__policy__event.md)struct [pm\_policy\_event](structpm__policy__event.md) {

68 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

69 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_cyc;

71};

72

74

88const struct [pm\_state\_info](structpm__state__info.md) \*pm\_policy\_next\_state([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks);

89

91

[ 93](group__subsys__pm__sys__policy.md#gab241e40f9282a1c8ebc602997fbb3190)#define PM\_ALL\_SUBSTATES (UINT8\_MAX)

94

95#if defined(CONFIG\_PM) || defined(\_\_DOXYGEN\_\_)

[ 114](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)void [pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

115

[ 125](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)void [pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

126

[ 137](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)bool [pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

138

[ 148](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)void [pm\_policy\_latency\_request\_add](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)(struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req,

149 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us);

150

[ 157](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)void [pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)(struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req,

158 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us);

159

[ 165](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)void [pm\_policy\_latency\_request\_remove](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)(struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req);

166

[ 173](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b)void [pm\_policy\_latency\_changed\_subscribe](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b)(struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req,

174 [pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267) cb);

175

[ 181](group__subsys__pm__sys__policy.md#ga8ca62cfeef8d4ebb58800e3ac6b645ee)void [pm\_policy\_latency\_changed\_unsubscribe](group__subsys__pm__sys__policy.md#ga8ca62cfeef8d4ebb58800e3ac6b645ee)(struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req);

182

[ 201](group__subsys__pm__sys__policy.md#gafab2e1484a58131a9c7cefd2b9adb3e9)void [pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#gafab2e1484a58131a9c7cefd2b9adb3e9)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us);

202

[ 211](group__subsys__pm__sys__policy.md#ga1d6d278768ed961c3856119de2fbb74b)void [pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga1d6d278768ed961c3856119de2fbb74b)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us);

212

[ 220](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)void [pm\_policy\_event\_unregister](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt);

221

222#else

223static inline void [pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445))

224{

225 ARG\_UNUSED([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

226 ARG\_UNUSED([substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

227}

228

229static inline void [pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445))

230{

231 ARG\_UNUSED([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

232 ARG\_UNUSED([substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

233}

234

235static inline bool [pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445))

236{

237 ARG\_UNUSED([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

238 ARG\_UNUSED([substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

239

240 return false;

241}

242

243static inline void [pm\_policy\_latency\_request\_add](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)(

244 struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us)

245{

246 ARG\_UNUSED(req);

247 ARG\_UNUSED(value\_us);

248}

249

250static inline void [pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)(

251 struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us)

252{

253 ARG\_UNUSED(req);

254 ARG\_UNUSED(value\_us);

255}

256

257static inline void [pm\_policy\_latency\_request\_remove](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)(

258 struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req)

259{

260 ARG\_UNUSED(req);

261}

262

263static inline void [pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#gafab2e1484a58131a9c7cefd2b9adb3e9)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt,

264 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us)

265{

266 ARG\_UNUSED(evt);

267 ARG\_UNUSED(time\_us);

268}

269

270static inline void [pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga1d6d278768ed961c3856119de2fbb74b)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt,

271 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_us)

272{

273 ARG\_UNUSED(evt);

274 ARG\_UNUSED(time\_us);

275}

276

277static inline void [pm\_policy\_event\_unregister](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt)

278{

279 ARG\_UNUSED(evt);

280}

281#endif /\* CONFIG\_PM \*/

282

286

287#ifdef \_\_cplusplus

288}

289#endif

290

291#endif /\* ZEPHYR\_INCLUDE\_PM\_POLICY\_H\_ \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)

pm\_state

Power management state.

**Definition** state.h:27

[pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)

void pm\_policy\_state\_lock\_put(enum pm\_state state, uint8\_t substate\_id)

Decrease a power state lock counter.

[pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga1d6d278768ed961c3856119de2fbb74b)

void pm\_policy\_event\_update(struct pm\_policy\_event \*evt, uint32\_t time\_us)

Update an event.

[pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)

bool pm\_policy\_state\_lock\_is\_active(enum pm\_state state, uint8\_t substate\_id)

Check if a power state lock is active (not allowed).

[pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)

void pm\_policy\_latency\_request\_update(struct pm\_policy\_latency\_request \*req, uint32\_t value\_us)

Update a latency requirement.

[pm\_policy\_latency\_request\_add](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)

void pm\_policy\_latency\_request\_add(struct pm\_policy\_latency\_request \*req, uint32\_t value\_us)

Add a new latency requirement.

[pm\_policy\_latency\_changed\_unsubscribe](group__subsys__pm__sys__policy.md#ga8ca62cfeef8d4ebb58800e3ac6b645ee)

void pm\_policy\_latency\_changed\_unsubscribe(struct pm\_policy\_latency\_subscription \*req)

Unsubscribe to maximum latency changes.

[pm\_policy\_event\_unregister](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)

void pm\_policy\_event\_unregister(struct pm\_policy\_event \*evt)

Unregister an event.

[pm\_policy\_latency\_request\_remove](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)

void pm\_policy\_latency\_request\_remove(struct pm\_policy\_latency\_request \*req)

Remove a latency requirement.

[pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267)

void(\* pm\_policy\_latency\_changed\_cb\_t)(int32\_t latency)

Callback to notify when maximum latency changes.

**Definition** policy.h:35

[pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)

void pm\_policy\_state\_lock\_get(enum pm\_state state, uint8\_t substate\_id)

Increase a power state lock counter.

[pm\_policy\_latency\_changed\_subscribe](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b)

void pm\_policy\_latency\_changed\_subscribe(struct pm\_policy\_latency\_subscription \*req, pm\_policy\_latency\_changed\_cb\_t cb)

Subscribe to maximum latency changes.

[pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#gafab2e1484a58131a9c7cefd2b9adb3e9)

void pm\_policy\_event\_register(struct pm\_policy\_event \*evt, uint32\_t time\_us)

Register an event.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[state.h](state_8h.md)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[pm\_policy\_event](structpm__policy__event.md)

Event.

**Definition** policy.h:66

[pm\_policy\_latency\_request](structpm__policy__latency__request.md)

Latency request.

**Definition** policy.h:54

[pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md)

Latency change subscription.

**Definition** policy.h:42

[pm\_state\_info](structpm__state__info.md)

Information about a power management state.

**Definition** state.h:114

[pm\_state\_info::substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445)

uint8\_t substate\_id

Some platforms have multiple states that map to one Zephyr power state.

**Definition** state.h:141

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [policy.h](policy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
