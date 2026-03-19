---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/policy_8h_source.html
original_path: doxygen/html/policy_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

13#include <[zephyr/device.h](device_8h.md)>

14#include <[zephyr/pm/state.h](state_8h.md)>

15#include <[zephyr/sys/slist.h](slist_8h.md)>

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 36](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267)typedef void (\*[pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267))([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) latency);

37

[ 43](structpm__policy__latency__subscription.md)struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) {

45 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

46 [pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267) cb;

48};

49

[ 55](structpm__policy__latency__request.md)struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) {

57 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

58 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us;

60};

61

[ 67](structpm__policy__event.md)struct [pm\_policy\_event](structpm__policy__event.md) {

69 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

70 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) uptime\_ticks;

72};

73

75

89const struct [pm\_state\_info](structpm__state__info.md) \*pm\_policy\_next\_state([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks);

90

92

[ 94](group__subsys__pm__sys__policy.md#gab241e40f9282a1c8ebc602997fbb3190)#define PM\_ALL\_SUBSTATES (UINT8\_MAX)

95

96#if defined(CONFIG\_PM) || defined(\_\_DOXYGEN\_\_)

[ 115](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)void [pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

116

[ 126](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)void [pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

127

[ 138](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)bool [pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

139

[ 158](group__subsys__pm__sys__policy.md#ga4e66c09a5c8694e48b7be6b61667aeca)void [pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#ga4e66c09a5c8694e48b7be6b61667aeca)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) uptime\_ticks);

159

[ 171](group__subsys__pm__sys__policy.md#ga059074d867befbe9c6b7afc170ee09b3)void [pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga059074d867befbe9c6b7afc170ee09b3)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) uptime\_ticks);

172

[ 180](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)void [pm\_policy\_event\_unregister](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt);

181

[ 193](group__subsys__pm__sys__policy.md#ga708b7d2f8cb5f09738e3c6e5937c475e)void [pm\_policy\_device\_power\_lock\_get](group__subsys__pm__sys__policy.md#ga708b7d2f8cb5f09738e3c6e5937c475e)(const struct [device](structdevice.md) \*dev);

194

[ 206](group__subsys__pm__sys__policy.md#gafb90036c42bce2cc44466427b2907a81)void [pm\_policy\_device\_power\_lock\_put](group__subsys__pm__sys__policy.md#gafb90036c42bce2cc44466427b2907a81)(const struct [device](structdevice.md) \*dev);

207

[ 218](group__subsys__pm__sys__policy.md#gae2680fcc323e161362e4a5aa5339ac12)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [pm\_policy\_next\_event\_ticks](group__subsys__pm__sys__policy.md#gae2680fcc323e161362e4a5aa5339ac12)(void);

219

220#else

221static inline void [pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445))

222{

223 ARG\_UNUSED([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

224 ARG\_UNUSED([substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

225}

226

227static inline void [pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445))

228{

229 ARG\_UNUSED([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

230 ARG\_UNUSED([substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

231}

232

233static inline bool [pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445))

234{

235 ARG\_UNUSED([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

236 ARG\_UNUSED([substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445));

237

238 return false;

239}

240

241static inline void [pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#ga4e66c09a5c8694e48b7be6b61667aeca)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycle)

242{

243 ARG\_UNUSED(evt);

244 ARG\_UNUSED(cycle);

245}

246

247static inline void [pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga059074d867befbe9c6b7afc170ee09b3)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycle)

248{

249 ARG\_UNUSED(evt);

250 ARG\_UNUSED(cycle);

251}

252

253static inline void [pm\_policy\_event\_unregister](group__subsys__pm__sys__policy.md#ga9448e31e1bd1a8b02defe6d1427197ff)(struct [pm\_policy\_event](structpm__policy__event.md) \*evt)

254{

255 ARG\_UNUSED(evt);

256}

257

258static inline void [pm\_policy\_device\_power\_lock\_get](group__subsys__pm__sys__policy.md#ga708b7d2f8cb5f09738e3c6e5937c475e)(const struct [device](structdevice.md) \*dev)

259{

260 ARG\_UNUSED(dev);

261}

262

263static inline void [pm\_policy\_device\_power\_lock\_put](group__subsys__pm__sys__policy.md#gafb90036c42bce2cc44466427b2907a81)(const struct [device](structdevice.md) \*dev)

264{

265 ARG\_UNUSED(dev);

266}

267

268static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [pm\_policy\_next\_event\_ticks](group__subsys__pm__sys__policy.md#gae2680fcc323e161362e4a5aa5339ac12)(void)

269{

270 return -1;

271}

272

273#endif /\* CONFIG\_PM \*/

274

275#if defined(CONFIG\_PM) || defined(CONFIG\_PM\_POLICY\_LATENCY\_STANDALONE) || defined(\_\_DOXYGEN\_\_)

[ 285](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)void [pm\_policy\_latency\_request\_add](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)(struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req,

286 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us);

287

[ 294](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)void [pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)(struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req,

295 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us);

296

[ 302](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)void [pm\_policy\_latency\_request\_remove](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)(struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req);

303

[ 310](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b)void [pm\_policy\_latency\_changed\_subscribe](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b)(struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req,

311 [pm\_policy\_latency\_changed\_cb\_t](group__subsys__pm__sys__policy.md#gab2a0a73416b3fcb535fa54a1f3b4c267) cb);

312

[ 318](group__subsys__pm__sys__policy.md#ga8ca62cfeef8d4ebb58800e3ac6b645ee)void [pm\_policy\_latency\_changed\_unsubscribe](group__subsys__pm__sys__policy.md#ga8ca62cfeef8d4ebb58800e3ac6b645ee)(struct [pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md) \*req);

319#else

320static inline void [pm\_policy\_latency\_request\_add](group__subsys__pm__sys__policy.md#ga848627f6d143ece582711a16cab5442a)(

321 struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us)

322{

323 ARG\_UNUSED(req);

324 ARG\_UNUSED(value\_us);

325}

326

327static inline void [pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)(

328 struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value\_us)

329{

330 ARG\_UNUSED(req);

331 ARG\_UNUSED(value\_us);

332}

333

334static inline void [pm\_policy\_latency\_request\_remove](group__subsys__pm__sys__policy.md#gaadcb851b1bfb312ea0960918dc9f869e)(

335 struct [pm\_policy\_latency\_request](structpm__policy__latency__request.md) \*req)

336{

337 ARG\_UNUSED(req);

338}

339#endif /\* CONFIG\_PM CONFIG\_PM\_POLICY\_LATENCY\_STANDALONE \*/

340

344

345#ifdef \_\_cplusplus

346}

347#endif

348

349#endif /\* ZEPHYR\_INCLUDE\_PM\_POLICY\_H\_ \*/

[device.h](device_8h.md)

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)

pm\_state

Power management state.

**Definition** state.h:27

[pm\_policy\_event\_update](group__subsys__pm__sys__policy.md#ga059074d867befbe9c6b7afc170ee09b3)

void pm\_policy\_event\_update(struct pm\_policy\_event \*evt, int64\_t uptime\_ticks)

Update an event.

[pm\_policy\_state\_lock\_put](group__subsys__pm__sys__policy.md#ga12f4d121aa8be0eb66381713b481a8b1)

void pm\_policy\_state\_lock\_put(enum pm\_state state, uint8\_t substate\_id)

Decrease a power state lock counter.

[pm\_policy\_state\_lock\_is\_active](group__subsys__pm__sys__policy.md#ga39f14c8509dee55ed084b4111584b766)

bool pm\_policy\_state\_lock\_is\_active(enum pm\_state state, uint8\_t substate\_id)

Check if a power state lock is active (not allowed).

[pm\_policy\_event\_register](group__subsys__pm__sys__policy.md#ga4e66c09a5c8694e48b7be6b61667aeca)

void pm\_policy\_event\_register(struct pm\_policy\_event \*evt, int64\_t uptime\_ticks)

Register an event.

[pm\_policy\_latency\_request\_update](group__subsys__pm__sys__policy.md#ga6483bd320881d697de27493b4f2d92d1)

void pm\_policy\_latency\_request\_update(struct pm\_policy\_latency\_request \*req, uint32\_t value\_us)

Update a latency requirement.

[pm\_policy\_device\_power\_lock\_get](group__subsys__pm__sys__policy.md#ga708b7d2f8cb5f09738e3c6e5937c475e)

void pm\_policy\_device\_power\_lock\_get(const struct device \*dev)

Increase power state locks.

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

**Definition** policy.h:36

[pm\_policy\_state\_lock\_get](group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d)

void pm\_policy\_state\_lock\_get(enum pm\_state state, uint8\_t substate\_id)

Increase a power state lock counter.

[pm\_policy\_latency\_changed\_subscribe](group__subsys__pm__sys__policy.md#gacf77adf6eaf5258e03ce1923d685ed3b)

void pm\_policy\_latency\_changed\_subscribe(struct pm\_policy\_latency\_subscription \*req, pm\_policy\_latency\_changed\_cb\_t cb)

Subscribe to maximum latency changes.

[pm\_policy\_next\_event\_ticks](group__subsys__pm__sys__policy.md#gae2680fcc323e161362e4a5aa5339ac12)

int64\_t pm\_policy\_next\_event\_ticks(void)

Returns the ticks until the next event.

[pm\_policy\_device\_power\_lock\_put](group__subsys__pm__sys__policy.md#gafb90036c42bce2cc44466427b2907a81)

void pm\_policy\_device\_power\_lock\_put(const struct device \*dev)

Decrease power state locks.

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

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[pm\_policy\_event](structpm__policy__event.md)

Event.

**Definition** policy.h:67

[pm\_policy\_latency\_request](structpm__policy__latency__request.md)

Latency request.

**Definition** policy.h:55

[pm\_policy\_latency\_subscription](structpm__policy__latency__subscription.md)

Latency change subscription.

**Definition** policy.h:43

[pm\_state\_info](structpm__state__info.md)

Information about a power management state.

**Definition** state.h:114

[pm\_state\_info::substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445)

uint8\_t substate\_id

Some platforms have multiple states that map to one Zephyr power state.

**Definition** state.h:142

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [policy.h](policy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
