---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/state_8h_source.html
original_path: doxygen/html/state_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

state.h

[Go to the documentation of this file.](state_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PM\_STATE\_H\_

8#define ZEPHYR\_INCLUDE\_PM\_STATE\_H\_

9

10#include <[zephyr/sys/util.h](util_8h.md)>

11#include <[zephyr/devicetree.h](devicetree_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 27](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) {

[ 35](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743) [PM\_STATE\_ACTIVE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743),

[ 46](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19) [PM\_STATE\_RUNTIME\_IDLE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19),

[ 58](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0) [PM\_STATE\_SUSPEND\_TO\_IDLE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0),

[ 70](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429) [PM\_STATE\_STANDBY](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429),

[ 82](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00) [PM\_STATE\_SUSPEND\_TO\_RAM](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00),

[ 95](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695) [PM\_STATE\_SUSPEND\_TO\_DISK](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695),

[ 106](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01) [PM\_STATE\_SOFT\_OFF](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01),

[ 108](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737) [PM\_STATE\_COUNT](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737),

109};

110

[ 114](structpm__state__info.md)struct [pm\_state\_info](structpm__state__info.md) {

[ 115](structpm__state__info.md#aed57fc8a935951aa2687614b954c7225) enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](structpm__state__info.md#aed57fc8a935951aa2687614b954c7225);

116

[ 142](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445);

143

[ 151](structpm__state__info.md#ac0a5ee091648225ba25ea34c75163814) bool [pm\_device\_disabled](structpm__state__info.md#ac0a5ee091648225ba25ea34c75163814);

152

[ 159](structpm__state__info.md#a442654715d3872de1b7b0dcf08bffb8b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_residency\_us](structpm__state__info.md#a442654715d3872de1b7b0dcf08bffb8b);

160

[ 166](structpm__state__info.md#a6fc8e0a78df78c7a28a0bc2a27292818) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [exit\_latency\_us](structpm__state__info.md#a6fc8e0a78df78c7a28a0bc2a27292818);

167};

168

[ 172](structpm__state__constraint.md)struct [pm\_state\_constraint](structpm__state__constraint.md) {

[ 178](structpm__state__constraint.md#aabbdf004f6cbf8a5464f03cb63bb518e) enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](structpm__state__constraint.md#aabbdf004f6cbf8a5464f03cb63bb518e);

[ 184](structpm__state__constraint.md#a1007d7769f3529bb91db30fc503964ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [substate\_id](structpm__state__constraint.md#a1007d7769f3529bb91db30fc503964ad);

185};

186

188

196#define Z\_DT\_PHANDLE\_01(node\_id, prop, idx) \

197 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx), okay), \

198 (1), (0))

199

209#define Z\_PM\_STATE\_INFO\_FROM\_DT\_CPU(i, node\_id) \

210 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(DT\_PHANDLE\_BY\_IDX(node\_id, cpu\_power\_states, i), okay), \

211 (PM\_STATE\_INFO\_DT\_INIT(DT\_PHANDLE\_BY\_IDX(node\_id, cpu\_power\_states, i)),), ())

212

222#define Z\_PM\_STATE\_FROM\_DT\_CPU(i, node\_id) \

223 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(DT\_PHANDLE\_BY\_IDX(node\_id, cpu\_power\_states, i), okay), \

224 (PM\_STATE\_DT\_INIT(DT\_PHANDLE\_BY\_IDX(node\_id, cpu\_power\_states, i)),), ())

225

227

[ 234](group__subsys__pm__states.md#ga1e77683479b589093f06cca9b1d142b9)#define PM\_STATE\_INFO\_DT\_INIT(node\_id) \

235 { \

236 .state = PM\_STATE\_DT\_INIT(node\_id), \

237 .substate\_id = DT\_PROP\_OR(node\_id, substate\_id, 0), \

238 .min\_residency\_us = DT\_PROP\_OR(node\_id, min\_residency\_us, 0), \

239 .exit\_latency\_us = DT\_PROP\_OR(node\_id, exit\_latency\_us, 0), \

240 .pm\_device\_disabled = DT\_PROP(node\_id, zephyr\_pm\_device\_disabled), \

241 }

242

[ 249](group__subsys__pm__states.md#gadd0dca42aef0a021fed9ca2d588ce393)#define PM\_STATE\_DT\_INIT(node\_id) \

250 DT\_ENUM\_IDX(node\_id, power\_state\_name)

251

[ 259](group__subsys__pm__states.md#ga70e4a8cbc3b0e9427f4bf67ee31b3edd)#define DT\_NUM\_CPU\_POWER\_STATES(node\_id) \

260 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, cpu\_power\_states), \

261 (DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, cpu\_power\_states, Z\_DT\_PHANDLE\_01, (+))), \

262 (0))

263

[ 308](group__subsys__pm__states.md#ga2846f402e20570fc61118b8545cdbe12)#define PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU(node\_id) \

309 { \

310 LISTIFY(DT\_PROP\_LEN\_OR(node\_id, cpu\_power\_states, 0), \

311 Z\_PM\_STATE\_INFO\_FROM\_DT\_CPU, (), node\_id) \

312 }

313

[ 355](group__subsys__pm__states.md#ga8248587108fcb76adefb50a360bc5db7)#define PM\_STATE\_LIST\_FROM\_DT\_CPU(node\_id) \

356 { \

357 LISTIFY(DT\_PROP\_LEN\_OR(node\_id, cpu\_power\_states, 0), \

358 Z\_PM\_STATE\_FROM\_DT\_CPU, (), node\_id) \

359 }

360

361

362#if defined(CONFIG\_PM) || defined(\_\_DOXYGEN\_\_)

[ 371](group__subsys__pm__states.md#ga682f75eb5324455ce95a5c7d4c2d6242)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pm\_state\_cpu\_get\_all](group__subsys__pm__states.md#ga682f75eb5324455ce95a5c7d4c2d6242)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*\*states);

372

376

377#else /\* CONFIG\_PM \*/

378

379static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pm\_state\_cpu\_get\_all](group__subsys__pm__states.md#ga682f75eb5324455ce95a5c7d4c2d6242)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*\*states)

380{

381 ARG\_UNUSED(cpu);

382 ARG\_UNUSED(states);

383

384 return 0;

385}

386

387#endif /\* CONFIG\_PM \*/

388

389#ifdef \_\_cplusplus

390}

391#endif

392

393#endif

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)

pm\_state

Power management state.

**Definition** state.h:27

[pm\_state\_cpu\_get\_all](group__subsys__pm__states.md#ga682f75eb5324455ce95a5c7d4c2d6242)

uint8\_t pm\_state\_cpu\_get\_all(uint8\_t cpu, const struct pm\_state\_info \*\*states)

Obtain information about all supported states by a CPU.

[PM\_STATE\_SOFT\_OFF](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01)

@ PM\_STATE\_SOFT\_OFF

Soft off state.

**Definition** state.h:106

[PM\_STATE\_STANDBY](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429)

@ PM\_STATE\_STANDBY

Standby state.

**Definition** state.h:70

[PM\_STATE\_SUSPEND\_TO\_RAM](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00)

@ PM\_STATE\_SUSPEND\_TO\_RAM

Suspend to ram state.

**Definition** state.h:82

[PM\_STATE\_ACTIVE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743)

@ PM\_STATE\_ACTIVE

Runtime active state.

**Definition** state.h:35

[PM\_STATE\_RUNTIME\_IDLE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19)

@ PM\_STATE\_RUNTIME\_IDLE

Runtime idle state.

**Definition** state.h:46

[PM\_STATE\_SUSPEND\_TO\_IDLE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0)

@ PM\_STATE\_SUSPEND\_TO\_IDLE

Suspend to idle state.

**Definition** state.h:58

[PM\_STATE\_COUNT](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737)

@ PM\_STATE\_COUNT

Number of power management states (internal use).

**Definition** state.h:108

[PM\_STATE\_SUSPEND\_TO\_DISK](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695)

@ PM\_STATE\_SUSPEND\_TO\_DISK

Suspend to disk state.

**Definition** state.h:95

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[pm\_state\_constraint](structpm__state__constraint.md)

Power state information needed to lock a power state.

**Definition** state.h:172

[pm\_state\_constraint::substate\_id](structpm__state__constraint.md#a1007d7769f3529bb91db30fc503964ad)

uint8\_t substate\_id

Power management sub-state.

**Definition** state.h:184

[pm\_state\_constraint::state](structpm__state__constraint.md#aabbdf004f6cbf8a5464f03cb63bb518e)

enum pm\_state state

Power management state.

**Definition** state.h:178

[pm\_state\_info](structpm__state__info.md)

Information about a power management state.

**Definition** state.h:114

[pm\_state\_info::substate\_id](structpm__state__info.md#a422bc0c9aedc107dbfa57c3ac8eb2445)

uint8\_t substate\_id

Some platforms have multiple states that map to one Zephyr power state.

**Definition** state.h:142

[pm\_state\_info::min\_residency\_us](structpm__state__info.md#a442654715d3872de1b7b0dcf08bffb8b)

uint32\_t min\_residency\_us

Minimum residency duration in microseconds.

**Definition** state.h:159

[pm\_state\_info::exit\_latency\_us](structpm__state__info.md#a6fc8e0a78df78c7a28a0bc2a27292818)

uint32\_t exit\_latency\_us

Worst case latency in microseconds required to exit the idle state.

**Definition** state.h:166

[pm\_state\_info::pm\_device\_disabled](structpm__state__info.md#ac0a5ee091648225ba25ea34c75163814)

bool pm\_device\_disabled

Whether or not this state triggers device power management.

**Definition** state.h:151

[pm\_state\_info::state](structpm__state__info.md#aed57fc8a935951aa2687614b954c7225)

enum pm\_state state

**Definition** state.h:115

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [state.h](state_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
