---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ccc_8h_source.html
original_path: doxygen/html/ccc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccc.h

[Go to the documentation of this file.](ccc_8h.md)

1/\*

2 \* Copyright 2022 Intel Corporation

3 \* Copyright 2023 Meta Platforms, Inc. and its affiliates

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_CCC\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_CCC\_H\_

10

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/toolchain.h](toolchain_8h.md)>

21#include <[zephyr/sys/util.h](util_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)#define I3C\_CCC\_BROADCAST\_MAX\_ID 0x7FU

29

[ 35](group__i3c__ccc.md#ga06fc2296ada6198ab7a00646804ad5ed)#define I3C\_CCC\_ENEC(broadcast) ((broadcast) ? 0x00U : 0x80U)

36

[ 42](group__i3c__ccc.md#ga8798591746e72a8ae1f901e97d45b810)#define I3C\_CCC\_DISEC(broadcast) ((broadcast) ? 0x01U : 0x81U)

43

[ 50](group__i3c__ccc.md#ga213102b3a8dbd490b02c3c89843c8d2a)#define I3C\_CCC\_ENTAS(as, broadcast) (((broadcast) ? 0x02U : 0x82U) + (as))

51

[ 57](group__i3c__ccc.md#ga364ce54e30957f7871e56cd82c1f825c)#define I3C\_CCC\_ENTAS0(broadcast) I3C\_CCC\_ENTAS(0, broadcast)

58

[ 64](group__i3c__ccc.md#ga21c57ce34fe60255c9c8b28dac0a7a85)#define I3C\_CCC\_ENTAS1(broadcast) I3C\_CCC\_ENTAS(1, broadcast)

65

[ 71](group__i3c__ccc.md#ga3adea01f66748ae2b153bf7eb9eab1eb)#define I3C\_CCC\_ENTAS2(broadcast) I3C\_CCC\_ENTAS(2, broadcast)

72

[ 78](group__i3c__ccc.md#ga4dba9093fe562e3d09470610ab393f21)#define I3C\_CCC\_ENTAS3(broadcast) I3C\_CCC\_ENTAS(3, broadcast)

79

[ 81](group__i3c__ccc.md#gaed94df1e670fc3670970f261865d6f63)#define I3C\_CCC\_RSTDAA 0x06U

82

[ 84](group__i3c__ccc.md#gad6663cfa56be6bba2187a1d42d64be7b)#define I3C\_CCC\_ENTDAA 0x07U

85

[ 87](group__i3c__ccc.md#ga17e63ffe790f279a3e6eb8235c936604)#define I3C\_CCC\_DEFTGTS 0x08U

88

[ 94](group__i3c__ccc.md#gaab1ccf6cd47dfecee24811501e123802)#define I3C\_CCC\_SETMWL(broadcast) ((broadcast) ? 0x09U : 0x89U)

95

[ 101](group__i3c__ccc.md#ga97fd874b2e6c918f2e1262f7600bfd64)#define I3C\_CCC\_SETMRL(broadcast) ((broadcast) ? 0x0AU : 0x8AU)

102

[ 104](group__i3c__ccc.md#gace2b7fc835d31ade916aad3126eb0c6c)#define I3C\_CCC\_ENTTM 0x0BU

105

[ 107](group__i3c__ccc.md#gac0f85a020956e3ee1ae8da899a9e06a6)#define I3C\_CCC\_SETBUSCON 0x0CU

108

[ 114](group__i3c__ccc.md#ga4f331e7c21f15dd211a70c1a01c49738)#define I3C\_CCC\_ENDXFER(broadcast) ((broadcast) ? 0x12U : 0x92U)

115

[ 117](group__i3c__ccc.md#gae213fc68bf723d8f7aee8c41cb9156c3)#define I3C\_CCC\_ENTHDR(x) (0x20U + (x))

118

[ 120](group__i3c__ccc.md#gae88e44e9469891609ece0b8711162b9d)#define I3C\_CCC\_ENTHDR0 0x20U

121

[ 123](group__i3c__ccc.md#gae5319f3916df262579ecaac7497ed006)#define I3C\_CCC\_ENTHDR1 0x21U

124

[ 126](group__i3c__ccc.md#gaeff48ef5d76e4ea051f5aee1d1e4fc40)#define I3C\_CCC\_ENTHDR2 0x22U

127

[ 129](group__i3c__ccc.md#ga24eaa0af83a4a2223f4f84c3c67e05fe)#define I3C\_CCC\_ENTHDR3 0x23U

130

[ 132](group__i3c__ccc.md#gaf15d188164c8fa9c0bf589eb7c5622d0)#define I3C\_CCC\_ENTHDR4 0x24U

133

[ 135](group__i3c__ccc.md#gaafcad6bfacab1e42f22c8ee941ed6441)#define I3C\_CCC\_ENTHDR5 0x25U

136

[ 138](group__i3c__ccc.md#gae55615887425917b202818bb0b7c5ac5)#define I3C\_CCC\_ENTHDR6 0x26U

139

[ 141](group__i3c__ccc.md#ga9ab8c02bb5a80913024a43077fb97ffb)#define I3C\_CCC\_ENTHDR7 0x27U

142

[ 148](group__i3c__ccc.md#ga4203d5fdd9e9ca253803359934f22524)#define I3C\_CCC\_SETXTIME(broadcast) ((broadcast) ? 0x28U : 0x98U)

149

[ 151](group__i3c__ccc.md#gae995ef9e94beb26932b47136bdf89b57)#define I3C\_CCC\_SETAASA 0x29U

152

[ 158](group__i3c__ccc.md#ga424cb224727d33c1ab18e4149bbea232)#define I3C\_CCC\_RSTACT(broadcast) ((broadcast) ? 0x2AU : 0x9AU)

159

[ 161](group__i3c__ccc.md#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)#define I3C\_CCC\_DEFGRPA 0x2BU

162

[ 168](group__i3c__ccc.md#ga46611eab0c82b74c615a7a7435f79d85)#define I3C\_CCC\_RSTGRPA(broadcast) ((broadcast) ? 0x2CU : 0x9CU)

169

[ 171](group__i3c__ccc.md#ga290cc5511d95b5be31c2c4cfea929085)#define I3C\_CCC\_MLANE(broadcast) ((broadcast) ? 0x2DU : 0x9DU)

172

[ 179](group__i3c__ccc.md#gaee5fb96b2d54df3b1b7aadefd54a608d)#define I3C\_CCC\_VENDOR(broadcast, id) ((id) + ((broadcast) ? 0x61U : 0xE0U))

180

[ 182](group__i3c__ccc.md#ga134d5948b056144c83b133f93083a0f8)#define I3C\_CCC\_SETDASA 0x87U

183

[ 185](group__i3c__ccc.md#gae0d6d0047f2c6e73e49e5019ec8d9ff0)#define I3C\_CCC\_SETNEWDA 0x88U

186

[ 188](group__i3c__ccc.md#gae74935317b7ca471c09b767acf359e34)#define I3C\_CCC\_GETMWL 0x8BU

189

[ 191](group__i3c__ccc.md#ga92e89b1ba719fbb8833c6e32fe4ef1dc)#define I3C\_CCC\_GETMRL 0x8CU

192

[ 194](group__i3c__ccc.md#ga04f7386d55742e935fa4dbfeb0120124)#define I3C\_CCC\_GETPID 0x8DU

195

[ 197](group__i3c__ccc.md#ga1d7d49ab48098e4c2d5f63bd91d005e1)#define I3C\_CCC\_GETBCR 0x8EU

198

[ 200](group__i3c__ccc.md#ga04ab6d4f0b2bf9d7f195132c0959225c)#define I3C\_CCC\_GETDCR 0x8FU

201

[ 203](group__i3c__ccc.md#ga858603dfc251b684b9d049b90119993d)#define I3C\_CCC\_GETSTATUS 0x90U

204

[ 206](group__i3c__ccc.md#gaa6807d3113c9c4d19b6fd27db32b3698)#define I3C\_CCC\_GETACCCR 0x91U

207

[ 209](group__i3c__ccc.md#gab3cac5de39903cc2331a38ac66c4ff14)#define I3C\_CCC\_SETBRGTGT 0x93U

210

[ 212](group__i3c__ccc.md#ga2c078bf24e36689f34ad90979dd5c687)#define I3C\_CCC\_GETMXDS 0x94U

213

[ 215](group__i3c__ccc.md#gaa913844f97ee35405e9bf50c61a161a8)#define I3C\_CCC\_GETCAPS 0x95U

216

[ 218](group__i3c__ccc.md#ga5cf5cdb40299d4f8203b8035dacac17a)#define I3C\_CCC\_SETROUTE 0x96U

219

[ 221](group__i3c__ccc.md#gaa2d86faed4f7c36939ce754be852751a)#define I3C\_CCC\_D2DXFER 0x97U

222

[ 224](group__i3c__ccc.md#ga66bb5e8027b103298f882f413f8ee6e8)#define I3C\_CCC\_GETXTIME 0x99U

225

[ 227](group__i3c__ccc.md#gaa0bef5d42c9bf2a21e888e5d5998d5cb)#define I3C\_CCC\_SETGRPA 0x9BU

228

229struct [i3c\_device\_desc](structi3c__device__desc.md);

230

[ 234](structi3c__ccc__target__payload.md)struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md) {

[ 236](structi3c__ccc__target__payload.md#a2669978506b20ef01569357fbd3a9eef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__target__payload.md#a2669978506b20ef01569357fbd3a9eef);

237

[ 239](structi3c__ccc__target__payload.md#aa09ebbfdff5d9d97be1558a63bb3535e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rnw](structi3c__ccc__target__payload.md#aa09ebbfdff5d9d97be1558a63bb3535e):1;

240

[ 248](structi3c__ccc__target__payload.md#abc655b08df77701275038e80bfb5ba85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structi3c__ccc__target__payload.md#abc655b08df77701275038e80bfb5ba85);

249

[ 251](structi3c__ccc__target__payload.md#a5ddda39b2aeb2818b389d4df1e25ba0a) size\_t [data\_len](structi3c__ccc__target__payload.md#a5ddda39b2aeb2818b389d4df1e25ba0a);

252

[ 260](structi3c__ccc__target__payload.md#ae6091f0b1cc804f9658d941f6ab493ef) size\_t [num\_xfer](structi3c__ccc__target__payload.md#ae6091f0b1cc804f9658d941f6ab493ef);

261};

262

[ 266](structi3c__ccc__payload.md)struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) {

267 struct {

[ 271](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea);

272

[ 279](structi3c__ccc__payload.md#ac52dbf51c5d7903c02c9f149e47a1b0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structi3c__ccc__payload.md#ac52dbf51c5d7903c02c9f149e47a1b0b);

280

[ 282](structi3c__ccc__payload.md#afcc17965b8bdd0e5e26cd15cebe49cee) size\_t [data\_len](structi3c__ccc__payload.md#afcc17965b8bdd0e5e26cd15cebe49cee);

283

[ 290](structi3c__ccc__payload.md#a9d0f7efcc7774941f057c2ab0fb14439) size\_t [num\_xfer](structi3c__ccc__payload.md#a9d0f7efcc7774941f057c2ab0fb14439);

[ 291](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466) } [ccc](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466);

292

293 struct {

[ 302](structi3c__ccc__payload.md#a3dcab72bf5b627426f963df56514c38d) struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md) \*[payloads](structi3c__ccc__payload.md#a3dcab72bf5b627426f963df56514c38d);

303

[ 305](structi3c__ccc__payload.md#afc1706d47d22300e7fa44754920b2685) size\_t [num\_targets](structi3c__ccc__payload.md#afc1706d47d22300e7fa44754920b2685);

[ 306](structi3c__ccc__payload.md#aa93b97b77f8dff8e931731c1f9edcd86) } [targets](structi3c__ccc__payload.md#aa93b97b77f8dff8e931731c1f9edcd86);

307};

308

[ 312](structi3c__ccc__events.md)struct [i3c\_ccc\_events](structi3c__ccc__events.md) {

[ 322](structi3c__ccc__events.md#ac34bcdae31cdc718eb54962d6b707320) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events](structi3c__ccc__events.md#ac34bcdae31cdc718eb54962d6b707320);

323} \_\_packed;

324

[ 326](group__i3c__ccc.md#gafe40d9b2ccedca40071c47929ff66e65)#define I3C\_CCC\_ENEC\_EVT\_ENINTR BIT(0)

327

[ 329](group__i3c__ccc.md#gad73e2e9f31f3a02f52b20d77e64671ff)#define I3C\_CCC\_ENEC\_EVT\_ENCR BIT(1)

330

[ 332](group__i3c__ccc.md#ga7e705ac95643d0462ac4275eed42153a)#define I3C\_CCC\_ENEC\_EVT\_ENHJ BIT(3)

333

[ 334](group__i3c__ccc.md#ga7860289b621c4243401e1df21cd84d66)#define I3C\_CCC\_ENEC\_EVT\_ALL \

335 (I3C\_CCC\_ENEC\_EVT\_ENINTR | I3C\_CCC\_ENEC\_EVT\_ENCR | I3C\_CCC\_ENEC\_EVT\_ENHJ)

336

[ 338](group__i3c__ccc.md#gaf6da0458f1ae2d45ae7337cd4e576484)#define I3C\_CCC\_DISEC\_EVT\_DISINTR BIT(0)

339

[ 341](group__i3c__ccc.md#ga1f1612a16d2cb68b66f1ca85ba6f450a)#define I3C\_CCC\_DISEC\_EVT\_DISCR BIT(1)

342

[ 344](group__i3c__ccc.md#gac3ffda84f683f99a0d4e0ad67adfd675)#define I3C\_CCC\_DISEC\_EVT\_DISHJ BIT(3)

345

[ 346](group__i3c__ccc.md#gaf177b8fcb7412671a3b8c418336ddde4)#define I3C\_CCC\_DISEC\_EVT\_ALL \

347 (I3C\_CCC\_DISEC\_EVT\_DISINTR | I3C\_CCC\_DISEC\_EVT\_DISCR | I3C\_CCC\_DISEC\_EVT\_DISHJ)

348

349/\*

350 \* Events for both enabling and disabling since

351 \* they have the same bits.

352 \*/

353

[ 355](group__i3c__ccc.md#ga14cbf3628627f965336ac3740858aeea)#define I3C\_CCC\_EVT\_INTR BIT(0)

356

[ 358](group__i3c__ccc.md#gad515a978c4912ef0c0444f14e51d8e8f)#define I3C\_CCC\_EVT\_CR BIT(1)

359

[ 361](group__i3c__ccc.md#gaedf65a98d59de51a533ff3d2f8cf075a)#define I3C\_CCC\_EVT\_HJ BIT(3)

362

[ 364](group__i3c__ccc.md#ga8ff2055f745c4970bd41850bfd5b2aff)#define I3C\_CCC\_EVT\_ALL \

365 (I3C\_CCC\_EVT\_INTR | I3C\_CCC\_EVT\_CR | I3C\_CCC\_EVT\_HJ)

366

[ 375](structi3c__ccc__mwl.md)struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) {

[ 377](structi3c__ccc__mwl.md#a5312fa1fc7cc93dfdf88d490352cf08e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structi3c__ccc__mwl.md#a5312fa1fc7cc93dfdf88d490352cf08e);

378} \_\_packed;

379

[ 388](structi3c__ccc__mrl.md)struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) {

[ 390](structi3c__ccc__mrl.md#a381d52439049c6a13d232e4e94d17335) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structi3c__ccc__mrl.md#a381d52439049c6a13d232e4e94d17335);

391

[ 393](structi3c__ccc__mrl.md#a7480df4486c9eb8a11581e42ff3b6b67) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ibi\_len](structi3c__ccc__mrl.md#a7480df4486c9eb8a11581e42ff3b6b67);

394} \_\_packed;

395

[ 402](structi3c__ccc__deftgts__active__controller.md)struct [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) {

[ 404](structi3c__ccc__deftgts__active__controller.md#a4d7671db542bb70ef623be26804c154a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__deftgts__active__controller.md#a4d7671db542bb70ef623be26804c154a);

405

[ 407](structi3c__ccc__deftgts__active__controller.md#a7acd12fad49f565a6b8a71993b6ad5d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__ccc__deftgts__active__controller.md#a7acd12fad49f565a6b8a71993b6ad5d4);

408

[ 410](structi3c__ccc__deftgts__active__controller.md#aeb56808d9b998c51d5b30307e0212328) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__ccc__deftgts__active__controller.md#aeb56808d9b998c51d5b30307e0212328);

411

[ 413](structi3c__ccc__deftgts__active__controller.md#ae2fb1ebc28ef1f69c6114af0b25875d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__ccc__deftgts__active__controller.md#ae2fb1ebc28ef1f69c6114af0b25875d3);

414};

415

[ 422](structi3c__ccc__deftgts__target.md)struct [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) {

[ 424](structi3c__ccc__deftgts__target.md#a34a02df3d4dc456733746437b2cd983a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__deftgts__target.md#a34a02df3d4dc456733746437b2cd983a);

425

426 union {

[ 431](structi3c__ccc__deftgts__target.md#a08689c18d74fa4b74fc2ada055394e65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__ccc__deftgts__target.md#a08689c18d74fa4b74fc2ada055394e65);

432

[ 434](structi3c__ccc__deftgts__target.md#ab4fbe6aac8d5860ef90613e51b15ef83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lvr](structi3c__ccc__deftgts__target.md#ab4fbe6aac8d5860ef90613e51b15ef83);

435 };

436

[ 438](structi3c__ccc__deftgts__target.md#a7c234182e16da66c308e86d72591063d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__ccc__deftgts__target.md#a7c234182e16da66c308e86d72591063d);

439

[ 441](structi3c__ccc__deftgts__target.md#a7374dd59c060462af7ca366ae7165107) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__ccc__deftgts__target.md#a7374dd59c060462af7ca366ae7165107);

442};

443

[ 452](structi3c__ccc__deftgts.md)struct [i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md) {

[ 454](structi3c__ccc__deftgts.md#a1f59c280bd388eb7e7818eb674b5f12f) struct [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) [active\_controller](structi3c__ccc__deftgts.md#a1f59c280bd388eb7e7818eb674b5f12f);

455

[ 457](structi3c__ccc__deftgts.md#a3ead83f46d63c4dd4723ef76dba770ee) struct [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) [targets](structi3c__ccc__deftgts.md#a3ead83f46d63c4dd4723ef76dba770ee)[];

458} \_\_packed;

459

[ 473](structi3c__ccc__address.md)struct [i3c\_ccc\_address](structi3c__ccc__address.md) {

[ 488](structi3c__ccc__address.md#afc3d7db034b3fd72c6118790a18a677b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__address.md#afc3d7db034b3fd72c6118790a18a677b);

489} \_\_packed;

490

[ 494](structi3c__ccc__getpid.md)struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) {

[ 500](structi3c__ccc__getpid.md#a060023fcb180e44b39a73c0f955f02c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pid](structi3c__ccc__getpid.md#a060023fcb180e44b39a73c0f955f02c7)[6];

501} \_\_packed;

502

[ 506](structi3c__ccc__getbcr.md)struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) {

[ 508](structi3c__ccc__getbcr.md#a09df0a49b57a38b91fe2e51c4de5c334) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__ccc__getbcr.md#a09df0a49b57a38b91fe2e51c4de5c334);

509} \_\_packed;

510

[ 514](structi3c__ccc__getdcr.md)struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) {

[ 516](structi3c__ccc__getdcr.md#a0615f439c4d556b08f7ecba8dff1c007) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__ccc__getdcr.md#a0615f439c4d556b08f7ecba8dff1c007);

517} \_\_packed;

518

519

[ 523](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648)enum [i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) {

[ 525](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b) [GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b),

526

[ 528](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f) [GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f),

529};

530

[ 534](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172)enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) {

[ 536](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb) [GETSTATUS\_FORMAT\_2\_TGTSTAT](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb) = 0x00U,

537

[ 539](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877) [GETSTATUS\_FORMAT\_2\_PRECR](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877) = 0x91U,

540

[ 542](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19) [GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19) = 0x100U

543};

544

[ 548](unioni3c__ccc__getstatus.md)union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) {

549 struct {

[ 563](unioni3c__ccc__getstatus.md#a23fe55c75741457ea399a6c7074017f6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [status](unioni3c__ccc__getstatus.md#a23fe55c75741457ea399a6c7074017f6);

[ 564](unioni3c__ccc__getstatus.md#adbc4805456634d5602ab74c2cde4d903) } [fmt1](unioni3c__ccc__getstatus.md#adbc4805456634d5602ab74c2cde4d903);

565

566 union {

[ 572](unioni3c__ccc__getstatus.md#a18b3c86f3157b3dfb30dc51127de2b69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tgtstat](unioni3c__ccc__getstatus.md#a18b3c86f3157b3dfb30dc51127de2b69);

573

[ 586](unioni3c__ccc__getstatus.md#a104f75402b9ea4b07c9aafc376349d84) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [precr](unioni3c__ccc__getstatus.md#a104f75402b9ea4b07c9aafc376349d84);

587

[ 588](unioni3c__ccc__getstatus.md#ab7a174cc76dd5da060cf420de1f3093e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [raw\_u16](unioni3c__ccc__getstatus.md#ab7a174cc76dd5da060cf420de1f3093e);

[ 589](unioni3c__ccc__getstatus.md#ac3a7629c6d213beff8ab38863a366b11) } [fmt2](unioni3c__ccc__getstatus.md#ac3a7629c6d213beff8ab38863a366b11);

590} \_\_packed;

591

[ 593](group__i3c__ccc.md#gaee3dd61e9ac723a90868c610d0179b7d)#define I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR BIT(5)

594

[ 596](group__i3c__ccc.md#ga8aca4592e579411a2c17f80ad682d93f)#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT 6

597

[ 599](group__i3c__ccc.md#ga1006146ca810c06674fbee0ee1f66286)#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK \

600 (0x03U << I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT)

601

[ 610](group__i3c__ccc.md#ga660e179384e9426b498cd62da5665b15)#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE(status) \

611 (((status) & I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK) \

612 >> I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT)

613

[ 615](group__i3c__ccc.md#ga1c07ae6c80088b8336f7f2d728487606)#define I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT 0

616

[ 618](group__i3c__ccc.md#gae0bcc3ea13a34f63b073d63569d2e53a)#define I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK \

619 (0x0FU << I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT)

620

[ 629](group__i3c__ccc.md#ga1436dc4b9f71c6f61fd3e3331857f3bd)#define I3C\_CCC\_GETSTATUS\_NUM\_INT(status) \

630 (((status) & I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK) \

631 >> I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT)

632

[ 634](group__i3c__ccc.md#ga94afb0ebcfce55b85fc4a81953b4178a)#define I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED BIT(0)

635

[ 637](group__i3c__ccc.md#gadda1781cae312f4e588c3d3dcfa74f38)#define I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK BIT(1)

638

[ 642](structi3c__ccc__setbrgtgt__tgt.md)struct [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) {

[ 649](structi3c__ccc__setbrgtgt__tgt.md#a6fa24f8354e856031464aaaa2c8fd1bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__setbrgtgt__tgt.md#a6fa24f8354e856031464aaaa2c8fd1bb);

650

[ 659](structi3c__ccc__setbrgtgt__tgt.md#a1dca2717ca9502f11b300a0d9a1fc0e6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structi3c__ccc__setbrgtgt__tgt.md#a1dca2717ca9502f11b300a0d9a1fc0e6);

660} \_\_packed;

661

[ 669](structi3c__ccc__setbrgtgt.md)struct [i3c\_ccc\_setbrgtgt](structi3c__ccc__setbrgtgt.md) {

[ 671](structi3c__ccc__setbrgtgt.md#a9099e2979baca2c3fbbb7a6b781edbf3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structi3c__ccc__setbrgtgt.md#a9099e2979baca2c3fbbb7a6b781edbf3);

672

[ 674](structi3c__ccc__setbrgtgt.md#aa019eb13d7da60941382c6e43884b60d) struct [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) [targets](structi3c__ccc__setbrgtgt.md#aa019eb13d7da60941382c6e43884b60d)[];

675} \_\_packed;

676

[ 682](unioni3c__ccc__getmxds.md)union [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) {

683 struct {

[ 685](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13);

686

[ 688](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98);

[ 689](unioni3c__ccc__getmxds.md#a242470090b40e40f0b0febfba966d766) } [fmt1](unioni3c__ccc__getmxds.md#a242470090b40e40f0b0febfba966d766);

690

691 struct {

693 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13);

694

696 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98);

697

[ 703](unioni3c__ccc__getmxds.md#a3782b5dce0db847362b9413a02d90baa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrdturn](unioni3c__ccc__getmxds.md#a3782b5dce0db847362b9413a02d90baa)[3];

[ 704](unioni3c__ccc__getmxds.md#adfb70b06d5e769fccc7630a356067fcd) } [fmt2](unioni3c__ccc__getmxds.md#adfb70b06d5e769fccc7630a356067fcd);

705

706 struct {

[ 712](unioni3c__ccc__getmxds.md#a3324b594867b06b7c306decd81eed53d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [wrrdturn](unioni3c__ccc__getmxds.md#a3324b594867b06b7c306decd81eed53d);

713

[ 719](unioni3c__ccc__getmxds.md#ad55160abc13a3ad04d5d6f827714f48b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crhdly1](unioni3c__ccc__getmxds.md#ad55160abc13a3ad04d5d6f827714f48b);

[ 720](unioni3c__ccc__getmxds.md#a6bb902a7335f2244365cde9782659dce) } [fmt3](unioni3c__ccc__getmxds.md#a6bb902a7335f2244365cde9782659dce);

721} \_\_packed;

722

[ 724](group__i3c__ccc.md#ga65ed8d5c2e6f562215674217f974d608)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX 0

725

[ 727](group__i3c__ccc.md#gaac6dec9aee1e1d5a56c964a4d1fe32b1)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ 1

728

[ 730](group__i3c__ccc.md#gae1ff27ad2b8c9119e2efa88c0a696555)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ 2

731

[ 733](group__i3c__ccc.md#ga409666d6a17b53e518d702863826eb28)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ 3

734

[ 736](group__i3c__ccc.md#ga5a329b3fa12ecafd6958b05bab163a5c)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ 4

737

[ 739](group__i3c__ccc.md#gad5e417bc3cabf8a915d1e7938415125a)#define I3C\_CCC\_GETMXDS\_TSCO\_8NS 0

740

[ 742](group__i3c__ccc.md#gaaee475f82f3a3759c7d62bb48082ebc2)#define I3C\_CCC\_GETMXDS\_TSCO\_9NS 1

743

[ 745](group__i3c__ccc.md#ga5e264e39aa2d4b602ec5e3218708e2f6)#define I3C\_CCC\_GETMXDS\_TSCO\_10NS 2

746

[ 748](group__i3c__ccc.md#ga2b27c9023f447da9c474c078091cf580)#define I3C\_CCC\_GETMXDS\_TSCO\_11NS 3

749

[ 751](group__i3c__ccc.md#ga06d33d1884a30d179aace82af956d62d)#define I3C\_CCC\_GETMXDS\_TSCO\_12NS 4

752

[ 754](group__i3c__ccc.md#ga5be034f241ccfb59534ae247d2e31d85)#define I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS 7

755

[ 757](group__i3c__ccc.md#ga43fa03b6fea48cca06d07e962c5c04ef)#define I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT BIT(3)

758

[ 760](group__i3c__ccc.md#ga9bfab32baa69d2e437167afa31a6b428)#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT 0

761

[ 763](group__i3c__ccc.md#ga5f4c6dde339c3467bdb3aea0d680d01f)#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK \

764 (0x07U << I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT)

765

[ 774](group__i3c__ccc.md#gae61b18d964e575809a1ebe2189aae028)#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL(maxwr) \

775 (((maxwr) & \

776 I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK) \

777 >> I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT)

778

[ 780](group__i3c__ccc.md#gaf5b95266cc911a37a3e46565b7601970)#define I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN BIT(6)

781

[ 783](group__i3c__ccc.md#gaf9c4764b0953c28af83b4fe06df0ebc3)#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT 3

784

[ 786](group__i3c__ccc.md#ga41958f7756cc5dec1c0546e7832b764a)#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK \

787 (0x07U << I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT)

788

[ 797](group__i3c__ccc.md#ga8284130d363dd1898de44c572b3d566c)#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO(maxrd) \

798 (((maxrd) & I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK) \

799 >> I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT)

800

[ 802](group__i3c__ccc.md#ga474f4d9ec309436863bdf0d7151de95f)#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT 0

803

[ 805](group__i3c__ccc.md#gad8b14f71cc1d5c1a0daa27703ab0c774)#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK \

806 (0x07U << I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT)

807

[ 816](group__i3c__ccc.md#gaf5ac7364357e1e123adddcbfc134a0be)#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL(maxrd) \

817 (((maxrd) & \

818 I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK) \

819 >> I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT)

820

[ 822](group__i3c__ccc.md#ga9aa4eaf8a537323883d242e9ebb9a985)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE BIT(2)

823

[ 825](group__i3c__ccc.md#ga7853f150811ae69b09520628d774a033)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT 0

826

[ 828](group__i3c__ccc.md#ga9ad046b7ec49bbca3f70a5a30fb1524b)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK \

829 (0x03U << I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT)

830

[ 839](group__i3c__ccc.md#gab43a5adbcf158086d23c5d796a7e9399)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE(crhdly1) \

840 (((crhdly1) & \

841 I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK) \

842 >> I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT)

843

[ 847](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958)enum [i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) {

[ 849](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0) [GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0),

850

[ 852](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620) [GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620),

853};

854

[ 858](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2)enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) {

[ 860](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e) [GETCAPS\_FORMAT\_2\_TGTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e) = 0x00U,

861

[ 863](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740) [GETCAPS\_FORMAT\_2\_TESTPAT](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740) = 0x5AU,

864

[ 866](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484) [GETCAPS\_FORMAT\_2\_CRCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484) = 0x91U,

867

[ 869](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984) [GETCAPS\_FORMAT\_2\_VTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984) = 0x93U,

870

[ 872](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0) [GETCAPS\_FORMAT\_2\_DBGCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0) = 0xD7U,

873

[ 875](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86) [GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86) = 0x100,

876};

877

[ 885](unioni3c__ccc__getcaps.md)union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) {

886 union {

[ 894](unioni3c__ccc__getcaps.md#ac3a378ed34efc38aa2f9605208e24cef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gethdrcap](unioni3c__ccc__getcaps.md#ac3a378ed34efc38aa2f9605208e24cef);

895

[ 921](unioni3c__ccc__getcaps.md#ab16e2b0e084371a9cbf57abf518f3e7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcaps](unioni3c__ccc__getcaps.md#ab16e2b0e084371a9cbf57abf518f3e7e)[4];

[ 922](unioni3c__ccc__getcaps.md#a908096a7dc051b59b9953575f9e5bf3b) } [fmt1](unioni3c__ccc__getcaps.md#a908096a7dc051b59b9953575f9e5bf3b);

923

924 union {

[ 930](unioni3c__ccc__getcaps.md#a99f11e2283bde1d4370a792a46ef8bad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tgtcaps](unioni3c__ccc__getcaps.md#a99f11e2283bde1d4370a792a46ef8bad)[4];

931

[ 937](unioni3c__ccc__getcaps.md#afd68057c626bb954cee2b6b46350ebae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [testpat](unioni3c__ccc__getcaps.md#afd68057c626bb954cee2b6b46350ebae);

938

[ 951](unioni3c__ccc__getcaps.md#a6266e60251e02ed9f1009ce1721adef8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crcaps](unioni3c__ccc__getcaps.md#a6266e60251e02ed9f1009ce1721adef8)[2];

952

[ 964](unioni3c__ccc__getcaps.md#ae7ab28922904daa7ef7380f0ddb41cb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vtcaps](unioni3c__ccc__getcaps.md#ae7ab28922904daa7ef7380f0ddb41cb3)[2];

[ 965](unioni3c__ccc__getcaps.md#a4b09537b6b796aa2b4fb962d7a4c446d) } [fmt2](unioni3c__ccc__getcaps.md#a4b09537b6b796aa2b4fb962d7a4c446d);

966} \_\_packed;

967

[ 969](group__i3c__ccc.md#gab984c6a18a555e4a3c0552684083e330)#define I3C\_CCC\_GETCAPS1\_HDR\_DDR BIT(0)

970

[ 972](group__i3c__ccc.md#gafe33491b778aa806977a98c3bd12a339)#define I3C\_CCC\_GETCAPS1\_HDR\_TSP BIT(1)

973

[ 975](group__i3c__ccc.md#gae9b98ab62745f041e4fe6e89ecd3b0e6)#define I3C\_CCC\_GETCAPS1\_HDR\_TSL BIT(2)

976

[ 978](group__i3c__ccc.md#gaac01f085ed1af56d686a33694744081c)#define I3C\_CCC\_GETCAPS1\_HDR\_BT BIT(3)

979

[ 987](group__i3c__ccc.md#gaae9483f4d5de3ba092b870b20e6b5f4a)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE(x) BIT(x)

988

[ 990](group__i3c__ccc.md#gad1389fc52c3fec4d6206bc56566bbf5d)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE0 BIT(0)

991

[ 993](group__i3c__ccc.md#gacfd20baf528fcceca7f71719e15d5ea0)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE1 BIT(1)

994

[ 996](group__i3c__ccc.md#ga9e5581743cbbe7363bb0919b95148d85)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE2 BIT(2)

997

[ 999](group__i3c__ccc.md#ga97b146596467f410ce9f063365ac9aaf)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE3 BIT(3)

1000

[ 1002](group__i3c__ccc.md#ga0dd98eeb74f493bfb04aeb698e656772)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE4 BIT(4)

1003

[ 1005](group__i3c__ccc.md#ga99bff02c40ccb15797dcf10c6dc00e87)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE5 BIT(5)

1006

[ 1008](group__i3c__ccc.md#ga12cead0a8ceb518a5c897f22b1d3dd64)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE6 BIT(6)

1009

[ 1011](group__i3c__ccc.md#ga8b3373f18c0e3b365cc199c19ae82fb0)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE7 BIT(7)

1012

[ 1014](group__i3c__ccc.md#ga1c2ceeaa44ee641c3d05176baf7e681d)#define I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT BIT(6)

1015

[ 1017](group__i3c__ccc.md#ga8faf5ff5b2542a309f114ce4d6d11640)#define I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC BIT(7)

1018

[ 1023](group__i3c__ccc.md#ga9ad0caec4913cd9454fa4c939555ad32)#define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT 4

1024

[ 1029](group__i3c__ccc.md#ga64f58d1aaf847cf4a7811b20cca13b55)#define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK \

1030 (0x03U << I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT)

1031

[ 1040](group__i3c__ccc.md#gabeb9acdabd6dce2117e9f5830673b2ed)#define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP(getcaps2) \

1041 (((getcaps2) & \

1042 I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK) \

1043 >> I3C\_CCC\_GETCAPS\_GRPADDR\_CAP\_SHIFT)

1044

[ 1049](group__i3c__ccc.md#ga558dc49b9856d49ccd77bfac88fbfc7c)#define I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT 0

1050

[ 1055](group__i3c__ccc.md#gae0015aa7768a8d5c18426a47cdbb67f8)#define I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK \

1056 (0x0FU << I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT)

1057

[ 1067](group__i3c__ccc.md#ga093449c1cf029bddf1a25181cbfed570)#define I3C\_CCC\_GETCAPS2\_SPEC\_VER(getcaps2) \

1068 (((getcaps2) & \

1069 I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK) \

1070 >> I3C\_CCC\_GETCAPS\_SPEC\_VER\_SHIFT)

1071

[ 1076](group__i3c__ccc.md#gaf0a2358f0f5f46c5fa1c084373f09be1)#define I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT BIT(0)

1077

[ 1082](group__i3c__ccc.md#ga08cc3c3976195642282e00ba00c1b283)#define I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT BIT(1)

1083

[ 1088](group__i3c__ccc.md#ga73829cd436decbe55d2290dc750b3918)#define I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE BIT(2)

1089

[ 1094](group__i3c__ccc.md#gaf40cc6cc08619363056e9650453a9a26)#define I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT BIT(3)

1095

[ 1100](group__i3c__ccc.md#gafbf1e9c947c40d70ae1c45991d093570)#define I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT BIT(4)

1101

[ 1106](group__i3c__ccc.md#ga3575eb8aa6fc3b49f2115104dcdfaeec)#define I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT BIT(5)

1107

[ 1112](group__i3c__ccc.md#gac13d1465aa4222be0acccbf5303f3f3e)#define I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION BIT(6)

1113

[ 1118](group__i3c__ccc.md#ga541ed236f06c20ca98e32d5a17788754)#define I3C\_CCC\_GETCAPS\_TESTPAT1 0xA5

1119

[ 1124](group__i3c__ccc.md#gafdb7ed7cc72efeb7cd62435084b1b40f)#define I3C\_CCC\_GETCAPS\_TESTPAT2 0x5A

1125

[ 1130](group__i3c__ccc.md#ga1720b3f54ade943f627b6a4e7284139a)#define I3C\_CCC\_GETCAPS\_TESTPAT3 0xA5

1131

[ 1136](group__i3c__ccc.md#ga2391e23e0b17351e3c28048b85d98ea6)#define I3C\_CCC\_GETCAPS\_TESTPAT4 0x5A

1137

[ 1142](group__i3c__ccc.md#ga98ee1cc4c436219b9639c5710fa6911b)#define I3C\_CCC\_GETCAPS\_TESTPAT 0xA55AA55A

1143

[ 1148](group__i3c__ccc.md#gad833335c6edb018edb66b99e1dfc16f7)#define I3C\_CCC\_GETCAPS\_CRCAPS1\_HJ\_SUPPORT BIT(0)

1149

[ 1154](group__i3c__ccc.md#ga86b22acbba045b037b4ae14abf4b6e5c)#define I3C\_CCC\_GETCAPS\_CRCAPS1\_GRP\_MANAGEMENT\_SUPPORT BIT(1)

1155

[ 1160](group__i3c__ccc.md#ga438621df282f451083e9ab9b1b59a2e3)#define I3C\_CCC\_GETCAPS\_CRCAPS1\_ML\_SUPPORT BIT(2)

1161

[ 1166](group__i3c__ccc.md#ga5bedcb1cb3769ae69779c0b2125b4b21)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_IBI\_TIR\_SUPPORT BIT(0)

1167

[ 1172](group__i3c__ccc.md#ga3a49b8a44676888fe600aa6b42cc52c6)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_CONTROLLER\_PASSBACK BIT(1)

1173

[ 1178](group__i3c__ccc.md#gad81d9a56d02db7e8a87279d8772adbec)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_DEEP\_SLEEP\_CAPABLE BIT(2)

1179

[ 1184](group__i3c__ccc.md#gada1a84b1394d6a72dd49e1c87307fbef)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_DELAYED\_CONTROLLER\_HANDOFF BIT(3)

1185

[ 1187](group__i3c__ccc.md#ga378e451327b212275c748480ada15a31)#define I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_SHIFT 0

1188

[ 1190](group__i3c__ccc.md#ga382e8db432a701a8b2f6c8be6aba81a8)#define I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_MASK \

1191 (0x07U << I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_SHIFT)

1192

[ 1201](group__i3c__ccc.md#ga9d0153d2e0b01a045e59e4acf4446206)#define I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE(vtcap1) \

1202 (((vtcap1) & \

1203 I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_MASK) \

1204 >> I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_SHIFT)

1205

[ 1210](group__i3c__ccc.md#gaca37ffb4f223c7b723a1b2ed881d28f7)#define I3C\_CCC\_GETCAPS\_VTCAP1\_SIDE\_EFFECTS BIT(4)

1211

[ 1216](group__i3c__ccc.md#gad1c0b63bb26be245e781e5d32d75dd15)#define I3C\_CCC\_GETCAPS\_VTCAP1\_SHARED\_PERIPH\_DETECT BIT(5)

1217

[ 1219](group__i3c__ccc.md#gafbd58c1713c93692b49e06508089397c)#define I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_SHIFT 0

1220

[ 1222](group__i3c__ccc.md#gad39e1c3d38b29937166345133ad373d1)#define I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_MASK \

1223 (0x03U << I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_SHIFT)

1224

[ 1233](group__i3c__ccc.md#ga8ee2a538a2b5efa2e02540aac392c685)#define I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS(vtcap2) \

1234 (((vtcap2) & \

1235 I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_MASK) \

1236 >> I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_SHIFT)

1237

[ 1242](group__i3c__ccc.md#ga1b7562342dbf9fe443386943527d5f29)#define I3C\_CCC\_GETCAPS\_VTCAP2\_ADDRESS\_REMAPPING BIT(2)

1243

[ 1245](group__i3c__ccc.md#gadada56c704f75606cbf4548c79981756)#define I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_SHIFT 3

1246

[ 1248](group__i3c__ccc.md#gadc61e60fbc59aca1ff813098f51ca56e)#define I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_MASK \

1249 (0x03U << I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_SHIFT)

1250

[ 1259](group__i3c__ccc.md#ga56112189be57287691d64eabfaa32910)#define I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND(vtcap2) \

1260 (((vtcap2) & \

1261 I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_MASK) \

1262 >> I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_SHIFT)

1263

[ 1267](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1)enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) {

[ 1269](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2) [I3C\_CCC\_RSTACT\_NO\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2) = 0x00U,

1270

[ 1272](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476) [I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476) = 0x01U,

1273

[ 1275](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879) [I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879) = 0x02U,

1276

[ 1278](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519) [I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519) = 0x03U,

1279

[ 1281](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e) [I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e) = 0x04U,

1282};

1283

[ 1294](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25)static inline bool [i3c\_ccc\_is\_payload\_broadcast](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25)(const struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload)

1295{

1296 return (payload->[ccc](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466).[id](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea) <= [I3C\_CCC\_BROADCAST\_MAX\_ID](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2));

1297}

1298

[ 1310](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c)int [i3c\_ccc\_do\_getbcr](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1311 struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) \*bcr);

1312

[ 1324](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101)int [i3c\_ccc\_do\_getdcr](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1325 struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) \*dcr);

1326

[ 1338](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df)int [i3c\_ccc\_do\_getpid](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1339 struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) \*pid);

1340

[ 1352](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7)int [i3c\_ccc\_do\_rstact\_all](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7)(const struct [device](structdevice.md) \*controller,

1353 enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) action);

1354

[ 1364](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7)int [i3c\_ccc\_do\_rstdaa\_all](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7)(const struct [device](structdevice.md) \*controller);

1365

[ 1379](group__i3c__ccc.md#gae4be97aae166be3b6e794fd77c8be6f8)int [i3c\_ccc\_do\_setdasa](group__i3c__ccc.md#gae4be97aae166be3b6e794fd77c8be6f8)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1380

[ 1394](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec)int [i3c\_ccc\_do\_setnewda](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1395 struct [i3c\_ccc\_address](structi3c__ccc__address.md) new\_da);

1396

[ 1409](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580)int [i3c\_ccc\_do\_events\_all\_set](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580)(const struct [device](structdevice.md) \*controller,

1410 bool enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events);

1411

[ 1424](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49)int [i3c\_ccc\_do\_events\_set](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1425 bool enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events);

1426

[ 1438](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d)int [i3c\_ccc\_do\_setmwl\_all](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d)(const struct [device](structdevice.md) \*controller,

1439 const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl);

1440

[ 1452](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49)int [i3c\_ccc\_do\_setmwl](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1453 const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl);

1454

[ 1466](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507)int [i3c\_ccc\_do\_getmwl](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1467 struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl);

1468

[ 1482](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0)int [i3c\_ccc\_do\_setmrl\_all](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0)(const struct [device](structdevice.md) \*controller,

1483 const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl,

1484 bool has\_ibi\_size);

1485

[ 1500](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a)int [i3c\_ccc\_do\_setmrl](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1501 const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl);

1502

[ 1517](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485)int [i3c\_ccc\_do\_getmrl](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1518 struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl);

1519

[ 1536](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)int [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1537 union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status,

1538 enum [i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) fmt,

1539 enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) defbyte);

1540

[ 1552](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95)static inline int [i3c\_ccc\_do\_getstatus\_fmt1](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1553 union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status)

1554{

1555 return [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)(target, status,

1556 [GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b),

1557 [GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19));

1558}

1559

[ 1572](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)static inline int [i3c\_ccc\_do\_getstatus\_fmt2](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1573 union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status,

1574 enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) defbyte)

1575{

1576 return [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)(target, status,

1577 [GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f), defbyte);

1578}

1579

[ 1596](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)int [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1597 union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps,

1598 enum [i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) fmt,

1599 enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) defbyte);

1600

[ 1612](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89)static inline int [i3c\_ccc\_do\_getcaps\_fmt1](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1613 union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps)

1614{

1615 return [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)(target, caps,

1616 [GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0),

1617 [GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86));

1618}

1619

[ 1632](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd)static inline int [i3c\_ccc\_do\_getcaps\_fmt2](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1633 union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps,

1634 enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) defbyte)

1635{

1636 return [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)(target, caps,

1637 [GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620), defbyte);

1638}

1639

1640#ifdef \_\_cplusplus

1641}

1642#endif

1643

1647

1648#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_CCC\_H\_ \*/

[device.h](device_8h.md)

[i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172)

i3c\_ccc\_getstatus\_defbyte

Defining byte values for GETSTATUS Format 2.

**Definition** ccc.h:534

[i3c\_ccc\_do\_getstatus\_fmt1](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95)

static int i3c\_ccc\_do\_getstatus\_fmt1(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getstatus \*status)

Single target GETSTATUS to Get Target Status (Format 1).

**Definition** ccc.h:1552

[i3c\_ccc\_do\_setmrl\_all](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0)

int i3c\_ccc\_do\_setmrl\_all(const struct device \*controller, const struct i3c\_ccc\_mrl \*mrl, bool has\_ibi\_size)

Broadcast SETMRL to Set Maximum Read Length.

[i3c\_ccc\_do\_rstact\_all](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7)

int i3c\_ccc\_do\_rstact\_all(const struct device \*controller, enum i3c\_ccc\_rstact\_defining\_byte action)

Broadcast RSTACT to reset I3C Peripheral.

[i3c\_ccc\_do\_getstatus\_fmt2](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)

static int i3c\_ccc\_do\_getstatus\_fmt2(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getstatus \*status, enum i3c\_ccc\_getstatus\_defbyte defbyte)

Single target GETSTATUS to Get Target Status (Format 2).

**Definition** ccc.h:1572

[i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)

int i3c\_ccc\_do\_getstatus(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getstatus \*status, enum i3c\_ccc\_getstatus\_fmt fmt, enum i3c\_ccc\_getstatus\_defbyte defbyte)

Single target GETSTATUS to Get Target Status.

[i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1)

i3c\_ccc\_rstact\_defining\_byte

Enum for I3C Reset Action (RSTACT) Defining Byte Values.

**Definition** ccc.h:1267

[i3c\_ccc\_do\_setmwl\_all](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d)

int i3c\_ccc\_do\_setmwl\_all(const struct device \*controller, const struct i3c\_ccc\_mwl \*mwl)

Broadcast SETMWL to Set Maximum Write Length.

[i3c\_ccc\_do\_setnewda](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec)

int i3c\_ccc\_do\_setnewda(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_address new\_da)

Set New Dynamic Address for a target.

[i3c\_ccc\_do\_setmrl](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a)

int i3c\_ccc\_do\_setmrl(const struct i3c\_device\_desc \*target, const struct i3c\_ccc\_mrl \*mrl)

Single target SETMRL to Set Maximum Read Length.

[i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648)

i3c\_ccc\_getstatus\_fmt

Indicate which format of GETSTATUS to use.

**Definition** ccc.h:523

[i3c\_ccc\_do\_getbcr](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c)

int i3c\_ccc\_do\_getbcr(struct i3c\_device\_desc \*target, struct i3c\_ccc\_getbcr \*bcr)

Get BCR from a target.

[i3c\_ccc\_do\_getdcr](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101)

int i3c\_ccc\_do\_getdcr(struct i3c\_device\_desc \*target, struct i3c\_ccc\_getdcr \*dcr)

Get DCR from a target.

[i3c\_ccc\_do\_getpid](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df)

int i3c\_ccc\_do\_getpid(struct i3c\_device\_desc \*target, struct i3c\_ccc\_getpid \*pid)

Get PID from a target.

[i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)

int i3c\_ccc\_do\_getcaps(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getcaps \*caps, enum i3c\_ccc\_getcaps\_fmt fmt, enum i3c\_ccc\_getcaps\_defbyte defbyte)

Single target GETCAPS to Get Target Status.

[i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958)

i3c\_ccc\_getcaps\_fmt

Indicate which format of GETCAPS to use.

**Definition** ccc.h:847

[i3c\_ccc\_do\_getcaps\_fmt2](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd)

static int i3c\_ccc\_do\_getcaps\_fmt2(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getcaps \*caps, enum i3c\_ccc\_getcaps\_defbyte defbyte)

Single target GETCAPS to Get Capabilities (Format 2).

**Definition** ccc.h:1632

[i3c\_ccc\_is\_payload\_broadcast](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25)

static bool i3c\_ccc\_is\_payload\_broadcast(const struct i3c\_ccc\_payload \*payload)

Test if I3C CCC payload is for broadcast.

**Definition** ccc.h:1294

[i3c\_ccc\_do\_rstdaa\_all](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7)

int i3c\_ccc\_do\_rstdaa\_all(const struct device \*controller)

Broadcast RSTDAA to reset dynamic addresses for all targets.

[i3c\_ccc\_do\_setmwl](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49)

int i3c\_ccc\_do\_setmwl(const struct i3c\_device\_desc \*target, const struct i3c\_ccc\_mwl \*mwl)

Single target SETMWL to Set Maximum Write Length.

[i3c\_ccc\_do\_getmrl](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485)

int i3c\_ccc\_do\_getmrl(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_mrl \*mrl)

Single target GETMRL to Get Maximum Read Length.

[i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2)

i3c\_ccc\_getcaps\_defbyte

Enum for I3C Get Capabilities (GETCAPS) Format 2 Defining Byte Values.

**Definition** ccc.h:858

[i3c\_ccc\_do\_setdasa](group__i3c__ccc.md#gae4be97aae166be3b6e794fd77c8be6f8)

int i3c\_ccc\_do\_setdasa(const struct i3c\_device\_desc \*target)

Set Dynamic Address from Static Address for a target.

[i3c\_ccc\_do\_getcaps\_fmt1](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89)

static int i3c\_ccc\_do\_getcaps\_fmt1(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getcaps \*caps)

Single target GETCAPS to Get Capabilities (Format 1).

**Definition** ccc.h:1612

[i3c\_ccc\_do\_getmwl](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507)

int i3c\_ccc\_do\_getmwl(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_mwl \*mwl)

Single target GETMWL to Get Maximum Write Length.

[i3c\_ccc\_do\_events\_all\_set](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580)

int i3c\_ccc\_do\_events\_all\_set(const struct device \*controller, bool enable, struct i3c\_ccc\_events \*events)

Broadcast ENEC/DISEC to enable/disable target events.

[i3c\_ccc\_do\_events\_set](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49)

int i3c\_ccc\_do\_events\_set(struct i3c\_device\_desc \*target, bool enable, struct i3c\_ccc\_events \*events)

Direct CCC ENEC/DISEC to enable/disable target events.

[I3C\_CCC\_BROADCAST\_MAX\_ID](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)

#define I3C\_CCC\_BROADCAST\_MAX\_ID

Maximum CCC ID for broadcast.

**Definition** ccc.h:28

[GETSTATUS\_FORMAT\_2\_PRECR](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877)

@ GETSTATUS\_FORMAT\_2\_PRECR

PRECR - Alternate status format describing Controller-capable device.

**Definition** ccc.h:539

[GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19)

@ GETSTATUS\_FORMAT\_2\_INVALID

Invalid defining byte.

**Definition** ccc.h:542

[GETSTATUS\_FORMAT\_2\_TGTSTAT](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb)

@ GETSTATUS\_FORMAT\_2\_TGTSTAT

Target status.

**Definition** ccc.h:536

[I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476)

@ I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY

Reset the I3C Peripheral Only.

**Definition** ccc.h:1272

[I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519)

@ I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER

Debug Network Adapter Reset.

**Definition** ccc.h:1278

[I3C\_CCC\_RSTACT\_NO\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2)

@ I3C\_CCC\_RSTACT\_NO\_RESET

No Reset on Target Reset Pattern.

**Definition** ccc.h:1269

[I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e)

@ I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT

Virtual Target Detect.

**Definition** ccc.h:1281

[I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879)

@ I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET

Reset the Whole Target.

**Definition** ccc.h:1275

[GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f)

@ GETSTATUS\_FORMAT\_2

GETSTATUS Format 2.

**Definition** ccc.h:528

[GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b)

@ GETSTATUS\_FORMAT\_1

GETSTATUS Format 1.

**Definition** ccc.h:525

[GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0)

@ GETCAPS\_FORMAT\_1

GETCAPS Format 1.

**Definition** ccc.h:849

[GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620)

@ GETCAPS\_FORMAT\_2

GETCAPS Format 2.

**Definition** ccc.h:852

[GETCAPS\_FORMAT\_2\_CRCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484)

@ GETCAPS\_FORMAT\_2\_CRCAPS

Controller handoff capabilities and features.

**Definition** ccc.h:866

[GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86)

@ GETCAPS\_FORMAT\_2\_INVALID

Invalid defining byte.

**Definition** ccc.h:875

[GETCAPS\_FORMAT\_2\_TGTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e)

@ GETCAPS\_FORMAT\_2\_TGTCAPS

Standard Target capabilities and features.

**Definition** ccc.h:860

[GETCAPS\_FORMAT\_2\_DBGCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0)

@ GETCAPS\_FORMAT\_2\_DBGCAPS

Debug-capable Device capabilities and features.

**Definition** ccc.h:872

[GETCAPS\_FORMAT\_2\_VTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984)

@ GETCAPS\_FORMAT\_2\_VTCAPS

Virtual Target capabilities and features.

**Definition** ccc.h:869

[GETCAPS\_FORMAT\_2\_TESTPAT](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740)

@ GETCAPS\_FORMAT\_2\_TESTPAT

Fixed 32b test pattern.

**Definition** ccc.h:863

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[i3c\_ccc\_address](structi3c__ccc__address.md)

Payload for a single device address.

**Definition** ccc.h:473

[i3c\_ccc\_address::addr](structi3c__ccc__address.md#afc3d7db034b3fd72c6118790a18a677b)

uint8\_t addr

**Definition** ccc.h:488

[i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md)

The active controller part of payload for DEFTGTS CCC.

**Definition** ccc.h:402

[i3c\_ccc\_deftgts\_active\_controller::addr](structi3c__ccc__deftgts__active__controller.md#a4d7671db542bb70ef623be26804c154a)

uint8\_t addr

Dynamic Address of Active Controller.

**Definition** ccc.h:404

[i3c\_ccc\_deftgts\_active\_controller::dcr](structi3c__ccc__deftgts__active__controller.md#a7acd12fad49f565a6b8a71993b6ad5d4)

uint8\_t dcr

Device Characteristic Register of Active Controller.

**Definition** ccc.h:407

[i3c\_ccc\_deftgts\_active\_controller::static\_addr](structi3c__ccc__deftgts__active__controller.md#ae2fb1ebc28ef1f69c6114af0b25875d3)

uint8\_t static\_addr

Static Address of Active Controller.

**Definition** ccc.h:413

[i3c\_ccc\_deftgts\_active\_controller::bcr](structi3c__ccc__deftgts__active__controller.md#aeb56808d9b998c51d5b30307e0212328)

uint8\_t bcr

Bus Characteristic Register of Active Controller.

**Definition** ccc.h:410

[i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md)

The target device part of payload for DEFTGTS CCC.

**Definition** ccc.h:422

[i3c\_ccc\_deftgts\_target::dcr](structi3c__ccc__deftgts__target.md#a08689c18d74fa4b74fc2ada055394e65)

uint8\_t dcr

Device Characteristic Register of a I3C target device or a group.

**Definition** ccc.h:431

[i3c\_ccc\_deftgts\_target::addr](structi3c__ccc__deftgts__target.md#a34a02df3d4dc456733746437b2cd983a)

uint8\_t addr

Dynamic Address of a target device, or a group address.

**Definition** ccc.h:424

[i3c\_ccc\_deftgts\_target::static\_addr](structi3c__ccc__deftgts__target.md#a7374dd59c060462af7ca366ae7165107)

uint8\_t static\_addr

Static Address of a target device or a group.

**Definition** ccc.h:441

[i3c\_ccc\_deftgts\_target::bcr](structi3c__ccc__deftgts__target.md#a7c234182e16da66c308e86d72591063d)

uint8\_t bcr

Bus Characteristic Register of a target device or a group.

**Definition** ccc.h:438

[i3c\_ccc\_deftgts\_target::lvr](structi3c__ccc__deftgts__target.md#ab4fbe6aac8d5860ef90613e51b15ef83)

uint8\_t lvr

Legacy Virtual Register for legacy I2C device.

**Definition** ccc.h:434

[i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md)

Payload for DEFTGTS CCC (Define List of Targets).

**Definition** ccc.h:452

[i3c\_ccc\_deftgts::active\_controller](structi3c__ccc__deftgts.md#a1f59c280bd388eb7e7818eb674b5f12f)

struct i3c\_ccc\_deftgts\_active\_controller active\_controller

Data describing the active controller.

**Definition** ccc.h:454

[i3c\_ccc\_deftgts::targets](structi3c__ccc__deftgts.md#a3ead83f46d63c4dd4723ef76dba770ee)

struct i3c\_ccc\_deftgts\_target targets[]

Data describing the target(s) on the bus.

**Definition** ccc.h:457

[i3c\_ccc\_events](structi3c__ccc__events.md)

Payload for ENEC/DISEC CCC (Target Events Command).

**Definition** ccc.h:312

[i3c\_ccc\_events::events](structi3c__ccc__events.md#ac34bcdae31cdc718eb54962d6b707320)

uint8\_t events

Event byte:

**Definition** ccc.h:322

[i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md)

Payload for GETBCR CCC (Get Bus Characteristics Register).

**Definition** ccc.h:506

[i3c\_ccc\_getbcr::bcr](structi3c__ccc__getbcr.md#a09df0a49b57a38b91fe2e51c4de5c334)

uint8\_t bcr

Bus Characteristics Register.

**Definition** ccc.h:508

[i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md)

Payload for GETDCR CCC (Get Device Characteristics Register).

**Definition** ccc.h:514

[i3c\_ccc\_getdcr::dcr](structi3c__ccc__getdcr.md#a0615f439c4d556b08f7ecba8dff1c007)

uint8\_t dcr

Device Characteristics Register.

**Definition** ccc.h:516

[i3c\_ccc\_getpid](structi3c__ccc__getpid.md)

Payload for GETPID CCC (Get Provisioned ID).

**Definition** ccc.h:494

[i3c\_ccc\_getpid::pid](structi3c__ccc__getpid.md#a060023fcb180e44b39a73c0f955f02c7)

uint8\_t pid[6]

48-bit Provisioned ID.

**Definition** ccc.h:500

[i3c\_ccc\_mrl](structi3c__ccc__mrl.md)

Payload for SETMRL/GETMRL CCC (Set/Get Maximum Read Length).

**Definition** ccc.h:388

[i3c\_ccc\_mrl::len](structi3c__ccc__mrl.md#a381d52439049c6a13d232e4e94d17335)

uint16\_t len

Maximum Read Length.

**Definition** ccc.h:390

[i3c\_ccc\_mrl::ibi\_len](structi3c__ccc__mrl.md#a7480df4486c9eb8a11581e42ff3b6b67)

uint8\_t ibi\_len

Optional IBI Payload Size.

**Definition** ccc.h:393

[i3c\_ccc\_mwl](structi3c__ccc__mwl.md)

Payload for SETMWL/GETMWL CCC (Set/Get Maximum Write Length).

**Definition** ccc.h:375

[i3c\_ccc\_mwl::len](structi3c__ccc__mwl.md#a5312fa1fc7cc93dfdf88d490352cf08e)

uint16\_t len

Maximum Write Length.

**Definition** ccc.h:377

[i3c\_ccc\_payload](structi3c__ccc__payload.md)

Payload structure for one CCC transaction.

**Definition** ccc.h:266

[i3c\_ccc\_payload::payloads](structi3c__ccc__payload.md#a3dcab72bf5b627426f963df56514c38d)

struct i3c\_ccc\_target\_payload \* payloads

Array of struct i3c\_ccc\_target\_payload.

**Definition** ccc.h:302

[i3c\_ccc\_payload::ccc](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466)

struct i3c\_ccc\_payload::@244074337306206345253052323277302146014310207057 ccc

[i3c\_ccc\_payload::num\_xfer](structi3c__ccc__payload.md#a9d0f7efcc7774941f057c2ab0fb14439)

size\_t num\_xfer

Total number of bytes transferred.

**Definition** ccc.h:290

[i3c\_ccc\_payload::targets](structi3c__ccc__payload.md#aa93b97b77f8dff8e931731c1f9edcd86)

struct i3c\_ccc\_payload::@313273325003250135275363022311173067156230063067 targets

[i3c\_ccc\_payload::data](structi3c__ccc__payload.md#ac52dbf51c5d7903c02c9f149e47a1b0b)

uint8\_t \* data

Pointer to byte array of data for this CCC.

**Definition** ccc.h:279

[i3c\_ccc\_payload::id](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea)

uint8\_t id

The CCC ID (I3C\_CCC\_\*).

**Definition** ccc.h:271

[i3c\_ccc\_payload::num\_targets](structi3c__ccc__payload.md#afc1706d47d22300e7fa44754920b2685)

size\_t num\_targets

Number of targets.

**Definition** ccc.h:305

[i3c\_ccc\_payload::data\_len](structi3c__ccc__payload.md#afcc17965b8bdd0e5e26cd15cebe49cee)

size\_t data\_len

Length in bytes for optional data array.

**Definition** ccc.h:282

[i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md)

One Bridged Target for SETBRGTGT payload.

**Definition** ccc.h:642

[i3c\_ccc\_setbrgtgt\_tgt::id](structi3c__ccc__setbrgtgt__tgt.md#a1dca2717ca9502f11b300a0d9a1fc0e6)

uint16\_t id

16-bit ID for the bridged target.

**Definition** ccc.h:659

[i3c\_ccc\_setbrgtgt\_tgt::addr](structi3c__ccc__setbrgtgt__tgt.md#a6fa24f8354e856031464aaaa2c8fd1bb)

uint8\_t addr

Dynamic address of the bridged target.

**Definition** ccc.h:649

[i3c\_ccc\_setbrgtgt](structi3c__ccc__setbrgtgt.md)

Payload for SETBRGTGT CCC (Set Bridge Targets).

**Definition** ccc.h:669

[i3c\_ccc\_setbrgtgt::count](structi3c__ccc__setbrgtgt.md#a9099e2979baca2c3fbbb7a6b781edbf3)

uint8\_t count

Number of bridged targets.

**Definition** ccc.h:671

[i3c\_ccc\_setbrgtgt::targets](structi3c__ccc__setbrgtgt.md#aa019eb13d7da60941382c6e43884b60d)

struct i3c\_ccc\_setbrgtgt\_tgt targets[]

Array of bridged targets.

**Definition** ccc.h:674

[i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md)

Payload structure for Direct CCC to one target.

**Definition** ccc.h:234

[i3c\_ccc\_target\_payload::addr](structi3c__ccc__target__payload.md#a2669978506b20ef01569357fbd3a9eef)

uint8\_t addr

Target address.

**Definition** ccc.h:236

[i3c\_ccc\_target\_payload::data\_len](structi3c__ccc__target__payload.md#a5ddda39b2aeb2818b389d4df1e25ba0a)

size\_t data\_len

Length in bytes for data.

**Definition** ccc.h:251

[i3c\_ccc\_target\_payload::rnw](structi3c__ccc__target__payload.md#aa09ebbfdff5d9d97be1558a63bb3535e)

uint8\_t rnw

0 for Write, 1 for Read

**Definition** ccc.h:239

[i3c\_ccc\_target\_payload::data](structi3c__ccc__target__payload.md#abc655b08df77701275038e80bfb5ba85)

uint8\_t \* data

**Definition** ccc.h:248

[i3c\_ccc\_target\_payload::num\_xfer](structi3c__ccc__target__payload.md#ae6091f0b1cc804f9658d941f6ab493ef)

size\_t num\_xfer

Total number of bytes transferred.

**Definition** ccc.h:260

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:916

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md)

Payload for GETCAPS CCC (Get Optional Feature Capabilities).

**Definition** ccc.h:885

[i3c\_ccc\_getcaps::fmt2](unioni3c__ccc__getcaps.md#a4b09537b6b796aa2b4fb962d7a4c446d)

union i3c\_ccc\_getcaps::@146137206326133235367372076147075060054306320326 fmt2

[i3c\_ccc\_getcaps::crcaps](unioni3c__ccc__getcaps.md#a6266e60251e02ed9f1009ce1721adef8)

uint8\_t crcaps[2]

Defining Byte 0x91: CRCAPS Byte 1 CRCAPS1.

**Definition** ccc.h:951

[i3c\_ccc\_getcaps::fmt1](unioni3c__ccc__getcaps.md#a908096a7dc051b59b9953575f9e5bf3b)

union i3c\_ccc\_getcaps::@176040264012374126324364077104322017272005341010 fmt1

[i3c\_ccc\_getcaps::tgtcaps](unioni3c__ccc__getcaps.md#a99f11e2283bde1d4370a792a46ef8bad)

uint8\_t tgtcaps[4]

Defining Byte 0x00: TGTCAPS.

**Definition** ccc.h:930

[i3c\_ccc\_getcaps::getcaps](unioni3c__ccc__getcaps.md#ab16e2b0e084371a9cbf57abf518f3e7e)

uint8\_t getcaps[4]

I3C v1.1+ Device Capabilities Byte 1 GETCAPS1.

**Definition** ccc.h:921

[i3c\_ccc\_getcaps::gethdrcap](unioni3c__ccc__getcaps.md#ac3a378ed34efc38aa2f9605208e24cef)

uint8\_t gethdrcap

I3C v1.0 HDR Capabilities.

**Definition** ccc.h:894

[i3c\_ccc\_getcaps::vtcaps](unioni3c__ccc__getcaps.md#ae7ab28922904daa7ef7380f0ddb41cb3)

uint8\_t vtcaps[2]

Defining Byte 0x93: VTCAPS Byte 1 VTCAPS1.

**Definition** ccc.h:964

[i3c\_ccc\_getcaps::testpat](unioni3c__ccc__getcaps.md#afd68057c626bb954cee2b6b46350ebae)

uint32\_t testpat

Defining Byte 0x5A: TESTPAT.

**Definition** ccc.h:937

[i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md)

Payload for GETMXDS CCC (Get Max Data Speed).

**Definition** ccc.h:682

[i3c\_ccc\_getmxds::fmt1](unioni3c__ccc__getmxds.md#a242470090b40e40f0b0febfba966d766)

struct i3c\_ccc\_getmxds::@017052066027027356133300167277077144205177366071 fmt1

[i3c\_ccc\_getmxds::wrrdturn](unioni3c__ccc__getmxds.md#a3324b594867b06b7c306decd81eed53d)

uint8\_t wrrdturn

Defining Byte 0x00: WRRDTURN.

**Definition** ccc.h:712

[i3c\_ccc\_getmxds::maxrdturn](unioni3c__ccc__getmxds.md#a3782b5dce0db847362b9413a02d90baa)

uint8\_t maxrdturn[3]

Maximum Read Turnaround Time in microsecond.

**Definition** ccc.h:703

[i3c\_ccc\_getmxds::maxrd](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98)

uint8\_t maxrd

maxRd

**Definition** ccc.h:688

[i3c\_ccc\_getmxds::fmt3](unioni3c__ccc__getmxds.md#a6bb902a7335f2244365cde9782659dce)

struct i3c\_ccc\_getmxds::@010015006355067367227170356377125232044011313157 fmt3

[i3c\_ccc\_getmxds::maxwr](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13)

uint8\_t maxwr

maxWr

**Definition** ccc.h:685

[i3c\_ccc\_getmxds::crhdly1](unioni3c__ccc__getmxds.md#ad55160abc13a3ad04d5d6f827714f48b)

uint8\_t crhdly1

Defining Byte 0x91: CRHDLY.

**Definition** ccc.h:719

[i3c\_ccc\_getmxds::fmt2](unioni3c__ccc__getmxds.md#adfb70b06d5e769fccc7630a356067fcd)

struct i3c\_ccc\_getmxds::@275016223350235350204161354245210176063371342011 fmt2

[i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md)

Payload for GETSTATUS CCC (Get Device Status).

**Definition** ccc.h:548

[i3c\_ccc\_getstatus::precr](unioni3c__ccc__getstatus.md#a104f75402b9ea4b07c9aafc376349d84)

uint16\_t precr

Defining Byte 0x91: PRECR.

**Definition** ccc.h:586

[i3c\_ccc\_getstatus::tgtstat](unioni3c__ccc__getstatus.md#a18b3c86f3157b3dfb30dc51127de2b69)

uint16\_t tgtstat

Defining Byte 0x00: TGTSTAT.

**Definition** ccc.h:572

[i3c\_ccc\_getstatus::status](unioni3c__ccc__getstatus.md#a23fe55c75741457ea399a6c7074017f6)

uint16\_t status

Device Status.

**Definition** ccc.h:563

[i3c\_ccc\_getstatus::raw\_u16](unioni3c__ccc__getstatus.md#ab7a174cc76dd5da060cf420de1f3093e)

uint16\_t raw\_u16

**Definition** ccc.h:588

[i3c\_ccc\_getstatus::fmt2](unioni3c__ccc__getstatus.md#ac3a7629c6d213beff8ab38863a366b11)

union i3c\_ccc\_getstatus::@360213032036351112213166306142126266072045035100 fmt2

[i3c\_ccc\_getstatus::fmt1](unioni3c__ccc__getstatus.md#adbc4805456634d5602ab74c2cde4d903)

struct i3c\_ccc\_getstatus::@040236027257025211003163330350055024304173214342 fmt1

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [ccc.h](ccc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
