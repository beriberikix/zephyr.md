---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ccc_8h_source.html
original_path: doxygen/html/ccc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

18#include <[stdint.h](stdint_8h.md)>

19

20#include <[zephyr/device.h](device_8h.md)>

21#include <[zephyr/toolchain.h](toolchain_8h.md)>

22#include <[zephyr/sys/util.h](sys_2util_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 29](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)#define I3C\_CCC\_BROADCAST\_MAX\_ID 0x7FU

30

[ 36](group__i3c__ccc.md#ga06fc2296ada6198ab7a00646804ad5ed)#define I3C\_CCC\_ENEC(broadcast) ((broadcast) ? 0x00U : 0x80U)

37

[ 43](group__i3c__ccc.md#ga8798591746e72a8ae1f901e97d45b810)#define I3C\_CCC\_DISEC(broadcast) ((broadcast) ? 0x01U : 0x81U)

44

[ 51](group__i3c__ccc.md#ga213102b3a8dbd490b02c3c89843c8d2a)#define I3C\_CCC\_ENTAS(as, broadcast) (((broadcast) ? 0x02U : 0x82U) + (as))

52

[ 58](group__i3c__ccc.md#ga364ce54e30957f7871e56cd82c1f825c)#define I3C\_CCC\_ENTAS0(broadcast) I3C\_CCC\_ENTAS(0, broadcast)

59

[ 65](group__i3c__ccc.md#ga21c57ce34fe60255c9c8b28dac0a7a85)#define I3C\_CCC\_ENTAS1(broadcast) I3C\_CCC\_ENTAS(1, broadcast)

66

[ 72](group__i3c__ccc.md#ga3adea01f66748ae2b153bf7eb9eab1eb)#define I3C\_CCC\_ENTAS2(broadcast) I3C\_CCC\_ENTAS(2, broadcast)

73

[ 79](group__i3c__ccc.md#ga4dba9093fe562e3d09470610ab393f21)#define I3C\_CCC\_ENTAS3(broadcast) I3C\_CCC\_ENTAS(3, broadcast)

80

[ 82](group__i3c__ccc.md#gaed94df1e670fc3670970f261865d6f63)#define I3C\_CCC\_RSTDAA 0x06U

83

[ 85](group__i3c__ccc.md#gad6663cfa56be6bba2187a1d42d64be7b)#define I3C\_CCC\_ENTDAA 0x07U

86

[ 88](group__i3c__ccc.md#ga17e63ffe790f279a3e6eb8235c936604)#define I3C\_CCC\_DEFTGTS 0x08U

89

[ 95](group__i3c__ccc.md#gaab1ccf6cd47dfecee24811501e123802)#define I3C\_CCC\_SETMWL(broadcast) ((broadcast) ? 0x09U : 0x89U)

96

[ 102](group__i3c__ccc.md#ga97fd874b2e6c918f2e1262f7600bfd64)#define I3C\_CCC\_SETMRL(broadcast) ((broadcast) ? 0x0AU : 0x8AU)

103

[ 105](group__i3c__ccc.md#gace2b7fc835d31ade916aad3126eb0c6c)#define I3C\_CCC\_ENTTM 0x0BU

106

[ 108](group__i3c__ccc.md#gac0f85a020956e3ee1ae8da899a9e06a6)#define I3C\_CCC\_SETBUSCON 0x0CU

109

[ 115](group__i3c__ccc.md#ga4f331e7c21f15dd211a70c1a01c49738)#define I3C\_CCC\_ENDXFER(broadcast) ((broadcast) ? 0x12U : 0x92U)

116

[ 118](group__i3c__ccc.md#gae213fc68bf723d8f7aee8c41cb9156c3)#define I3C\_CCC\_ENTHDR(x) (0x20U + (x))

119

[ 121](group__i3c__ccc.md#gae88e44e9469891609ece0b8711162b9d)#define I3C\_CCC\_ENTHDR0 0x20U

122

[ 124](group__i3c__ccc.md#gae5319f3916df262579ecaac7497ed006)#define I3C\_CCC\_ENTHDR1 0x21U

125

[ 127](group__i3c__ccc.md#gaeff48ef5d76e4ea051f5aee1d1e4fc40)#define I3C\_CCC\_ENTHDR2 0x22U

128

[ 130](group__i3c__ccc.md#ga24eaa0af83a4a2223f4f84c3c67e05fe)#define I3C\_CCC\_ENTHDR3 0x23U

131

[ 133](group__i3c__ccc.md#gaf15d188164c8fa9c0bf589eb7c5622d0)#define I3C\_CCC\_ENTHDR4 0x24U

134

[ 136](group__i3c__ccc.md#gaafcad6bfacab1e42f22c8ee941ed6441)#define I3C\_CCC\_ENTHDR5 0x25U

137

[ 139](group__i3c__ccc.md#gae55615887425917b202818bb0b7c5ac5)#define I3C\_CCC\_ENTHDR6 0x26U

140

[ 142](group__i3c__ccc.md#ga9ab8c02bb5a80913024a43077fb97ffb)#define I3C\_CCC\_ENTHDR7 0x27U

143

[ 149](group__i3c__ccc.md#ga4203d5fdd9e9ca253803359934f22524)#define I3C\_CCC\_SETXTIME(broadcast) ((broadcast) ? 0x28U : 0x98U)

150

[ 152](group__i3c__ccc.md#gae995ef9e94beb26932b47136bdf89b57)#define I3C\_CCC\_SETAASA 0x29U

153

[ 159](group__i3c__ccc.md#ga424cb224727d33c1ab18e4149bbea232)#define I3C\_CCC\_RSTACT(broadcast) ((broadcast) ? 0x2AU : 0x9AU)

160

[ 162](group__i3c__ccc.md#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)#define I3C\_CCC\_DEFGRPA 0x2BU

163

[ 169](group__i3c__ccc.md#ga46611eab0c82b74c615a7a7435f79d85)#define I3C\_CCC\_RSTGRPA(broadcast) ((broadcast) ? 0x2CU : 0x9CU)

170

[ 172](group__i3c__ccc.md#ga290cc5511d95b5be31c2c4cfea929085)#define I3C\_CCC\_MLANE(broadcast) ((broadcast) ? 0x2DU : 0x9DU)

173

[ 180](group__i3c__ccc.md#gaee5fb96b2d54df3b1b7aadefd54a608d)#define I3C\_CCC\_VENDOR(broadcast, id) ((id) + ((broadcast) ? 0x61U : 0xE0U))

181

[ 183](group__i3c__ccc.md#ga134d5948b056144c83b133f93083a0f8)#define I3C\_CCC\_SETDASA 0x87U

184

[ 186](group__i3c__ccc.md#gae0d6d0047f2c6e73e49e5019ec8d9ff0)#define I3C\_CCC\_SETNEWDA 0x88U

187

[ 189](group__i3c__ccc.md#gae74935317b7ca471c09b767acf359e34)#define I3C\_CCC\_GETMWL 0x8BU

190

[ 192](group__i3c__ccc.md#ga92e89b1ba719fbb8833c6e32fe4ef1dc)#define I3C\_CCC\_GETMRL 0x8CU

193

[ 195](group__i3c__ccc.md#ga04f7386d55742e935fa4dbfeb0120124)#define I3C\_CCC\_GETPID 0x8DU

196

[ 198](group__i3c__ccc.md#ga1d7d49ab48098e4c2d5f63bd91d005e1)#define I3C\_CCC\_GETBCR 0x8EU

199

[ 201](group__i3c__ccc.md#ga04ab6d4f0b2bf9d7f195132c0959225c)#define I3C\_CCC\_GETDCR 0x8FU

202

[ 204](group__i3c__ccc.md#ga858603dfc251b684b9d049b90119993d)#define I3C\_CCC\_GETSTATUS 0x90U

205

[ 207](group__i3c__ccc.md#gaa6807d3113c9c4d19b6fd27db32b3698)#define I3C\_CCC\_GETACCCR 0x91U

208

[ 210](group__i3c__ccc.md#gab3cac5de39903cc2331a38ac66c4ff14)#define I3C\_CCC\_SETBRGTGT 0x93U

211

[ 213](group__i3c__ccc.md#ga2c078bf24e36689f34ad90979dd5c687)#define I3C\_CCC\_GETMXDS 0x94U

214

[ 216](group__i3c__ccc.md#gaa913844f97ee35405e9bf50c61a161a8)#define I3C\_CCC\_GETCAPS 0x95U

217

[ 219](group__i3c__ccc.md#ga5cf5cdb40299d4f8203b8035dacac17a)#define I3C\_CCC\_SETROUTE 0x96U

220

[ 222](group__i3c__ccc.md#gaa2d86faed4f7c36939ce754be852751a)#define I3C\_CCC\_D2DXFER 0x97U

223

[ 225](group__i3c__ccc.md#ga66bb5e8027b103298f882f413f8ee6e8)#define I3C\_CCC\_GETXTIME 0x99U

226

[ 228](group__i3c__ccc.md#gaa0bef5d42c9bf2a21e888e5d5998d5cb)#define I3C\_CCC\_SETGRPA 0x9BU

229

230struct [i3c\_device\_desc](structi3c__device__desc.md);

231

[ 235](structi3c__ccc__target__payload.md)struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md) {

[ 237](structi3c__ccc__target__payload.md#a2669978506b20ef01569357fbd3a9eef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__target__payload.md#a2669978506b20ef01569357fbd3a9eef);

238

[ 240](structi3c__ccc__target__payload.md#aa09ebbfdff5d9d97be1558a63bb3535e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rnw](structi3c__ccc__target__payload.md#aa09ebbfdff5d9d97be1558a63bb3535e):1;

241

[ 249](structi3c__ccc__target__payload.md#abc655b08df77701275038e80bfb5ba85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structi3c__ccc__target__payload.md#abc655b08df77701275038e80bfb5ba85);

250

[ 252](structi3c__ccc__target__payload.md#a5ddda39b2aeb2818b389d4df1e25ba0a) size\_t [data\_len](structi3c__ccc__target__payload.md#a5ddda39b2aeb2818b389d4df1e25ba0a);

253

[ 261](structi3c__ccc__target__payload.md#ae6091f0b1cc804f9658d941f6ab493ef) size\_t [num\_xfer](structi3c__ccc__target__payload.md#ae6091f0b1cc804f9658d941f6ab493ef);

262};

263

[ 267](structi3c__ccc__payload.md)struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) {

268 struct {

[ 272](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea);

273

[ 280](structi3c__ccc__payload.md#ac52dbf51c5d7903c02c9f149e47a1b0b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structi3c__ccc__payload.md#ac52dbf51c5d7903c02c9f149e47a1b0b);

281

[ 283](structi3c__ccc__payload.md#afcc17965b8bdd0e5e26cd15cebe49cee) size\_t [data\_len](structi3c__ccc__payload.md#afcc17965b8bdd0e5e26cd15cebe49cee);

284

[ 291](structi3c__ccc__payload.md#a9d0f7efcc7774941f057c2ab0fb14439) size\_t [num\_xfer](structi3c__ccc__payload.md#a9d0f7efcc7774941f057c2ab0fb14439);

[ 292](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466) } [ccc](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466);

293

294 struct {

[ 303](structi3c__ccc__payload.md#a3dcab72bf5b627426f963df56514c38d) struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md) \*[payloads](structi3c__ccc__payload.md#a3dcab72bf5b627426f963df56514c38d);

304

[ 306](structi3c__ccc__payload.md#afc1706d47d22300e7fa44754920b2685) size\_t [num\_targets](structi3c__ccc__payload.md#afc1706d47d22300e7fa44754920b2685);

[ 307](structi3c__ccc__payload.md#aa93b97b77f8dff8e931731c1f9edcd86) } [targets](structi3c__ccc__payload.md#aa93b97b77f8dff8e931731c1f9edcd86);

308};

309

[ 313](structi3c__ccc__events.md)struct [i3c\_ccc\_events](structi3c__ccc__events.md) {

[ 323](structi3c__ccc__events.md#ac34bcdae31cdc718eb54962d6b707320) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [events](structi3c__ccc__events.md#ac34bcdae31cdc718eb54962d6b707320);

324} \_\_packed;

325

[ 327](group__i3c__ccc.md#gafe40d9b2ccedca40071c47929ff66e65)#define I3C\_CCC\_ENEC\_EVT\_ENINTR BIT(0)

328

[ 330](group__i3c__ccc.md#gad73e2e9f31f3a02f52b20d77e64671ff)#define I3C\_CCC\_ENEC\_EVT\_ENCR BIT(1)

331

[ 333](group__i3c__ccc.md#ga7e705ac95643d0462ac4275eed42153a)#define I3C\_CCC\_ENEC\_EVT\_ENHJ BIT(3)

334

[ 335](group__i3c__ccc.md#ga7860289b621c4243401e1df21cd84d66)#define I3C\_CCC\_ENEC\_EVT\_ALL \

336 (I3C\_CCC\_ENEC\_EVT\_ENINTR | I3C\_CCC\_ENEC\_EVT\_ENCR | I3C\_CCC\_ENEC\_EVT\_ENHJ)

337

[ 339](group__i3c__ccc.md#gaf6da0458f1ae2d45ae7337cd4e576484)#define I3C\_CCC\_DISEC\_EVT\_DISINTR BIT(0)

340

[ 342](group__i3c__ccc.md#ga1f1612a16d2cb68b66f1ca85ba6f450a)#define I3C\_CCC\_DISEC\_EVT\_DISCR BIT(1)

343

[ 345](group__i3c__ccc.md#gac3ffda84f683f99a0d4e0ad67adfd675)#define I3C\_CCC\_DISEC\_EVT\_DISHJ BIT(3)

346

[ 347](group__i3c__ccc.md#gaf177b8fcb7412671a3b8c418336ddde4)#define I3C\_CCC\_DISEC\_EVT\_ALL \

348 (I3C\_CCC\_DISEC\_EVT\_DISINTR | I3C\_CCC\_DISEC\_EVT\_DISCR | I3C\_CCC\_DISEC\_EVT\_DISHJ)

349

350/\*

351 \* Events for both enabling and disabling since

352 \* they have the same bits.

353 \*/

354

[ 356](group__i3c__ccc.md#ga14cbf3628627f965336ac3740858aeea)#define I3C\_CCC\_EVT\_INTR BIT(0)

357

[ 359](group__i3c__ccc.md#gad515a978c4912ef0c0444f14e51d8e8f)#define I3C\_CCC\_EVT\_CR BIT(1)

360

[ 362](group__i3c__ccc.md#gaedf65a98d59de51a533ff3d2f8cf075a)#define I3C\_CCC\_EVT\_HJ BIT(3)

363

[ 365](group__i3c__ccc.md#ga8ff2055f745c4970bd41850bfd5b2aff)#define I3C\_CCC\_EVT\_ALL \

366 (I3C\_CCC\_EVT\_INTR | I3C\_CCC\_EVT\_CR | I3C\_CCC\_EVT\_HJ)

367

[ 376](structi3c__ccc__mwl.md)struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) {

[ 378](structi3c__ccc__mwl.md#a5312fa1fc7cc93dfdf88d490352cf08e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structi3c__ccc__mwl.md#a5312fa1fc7cc93dfdf88d490352cf08e);

379} \_\_packed;

380

[ 389](structi3c__ccc__mrl.md)struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) {

[ 391](structi3c__ccc__mrl.md#a381d52439049c6a13d232e4e94d17335) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structi3c__ccc__mrl.md#a381d52439049c6a13d232e4e94d17335);

392

[ 394](structi3c__ccc__mrl.md#a7480df4486c9eb8a11581e42ff3b6b67) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ibi\_len](structi3c__ccc__mrl.md#a7480df4486c9eb8a11581e42ff3b6b67);

395} \_\_packed;

396

[ 403](structi3c__ccc__deftgts__active__controller.md)struct [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) {

[ 405](structi3c__ccc__deftgts__active__controller.md#a4d7671db542bb70ef623be26804c154a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__deftgts__active__controller.md#a4d7671db542bb70ef623be26804c154a);

406

[ 408](structi3c__ccc__deftgts__active__controller.md#a7acd12fad49f565a6b8a71993b6ad5d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__ccc__deftgts__active__controller.md#a7acd12fad49f565a6b8a71993b6ad5d4);

409

[ 411](structi3c__ccc__deftgts__active__controller.md#aeb56808d9b998c51d5b30307e0212328) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__ccc__deftgts__active__controller.md#aeb56808d9b998c51d5b30307e0212328);

412

[ 414](structi3c__ccc__deftgts__active__controller.md#ae2fb1ebc28ef1f69c6114af0b25875d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__ccc__deftgts__active__controller.md#ae2fb1ebc28ef1f69c6114af0b25875d3);

415};

416

[ 423](structi3c__ccc__deftgts__target.md)struct [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) {

[ 425](structi3c__ccc__deftgts__target.md#a34a02df3d4dc456733746437b2cd983a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__deftgts__target.md#a34a02df3d4dc456733746437b2cd983a);

426

427 union {

[ 432](structi3c__ccc__deftgts__target.md#a08689c18d74fa4b74fc2ada055394e65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__ccc__deftgts__target.md#a08689c18d74fa4b74fc2ada055394e65);

433

[ 435](structi3c__ccc__deftgts__target.md#ab4fbe6aac8d5860ef90613e51b15ef83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lvr](structi3c__ccc__deftgts__target.md#ab4fbe6aac8d5860ef90613e51b15ef83);

436 };

437

[ 439](structi3c__ccc__deftgts__target.md#a7c234182e16da66c308e86d72591063d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__ccc__deftgts__target.md#a7c234182e16da66c308e86d72591063d);

440

[ 442](structi3c__ccc__deftgts__target.md#a7374dd59c060462af7ca366ae7165107) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__ccc__deftgts__target.md#a7374dd59c060462af7ca366ae7165107);

443};

444

[ 453](structi3c__ccc__deftgts.md)struct [i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md) {

[ 455](structi3c__ccc__deftgts.md#a82a12e711417111855d76171fbd008c2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structi3c__ccc__deftgts.md#a82a12e711417111855d76171fbd008c2);

456

[ 458](structi3c__ccc__deftgts.md#a1f59c280bd388eb7e7818eb674b5f12f) struct [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) [active\_controller](structi3c__ccc__deftgts.md#a1f59c280bd388eb7e7818eb674b5f12f);

459

[ 461](structi3c__ccc__deftgts.md#a3ead83f46d63c4dd4723ef76dba770ee) struct [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) [targets](structi3c__ccc__deftgts.md#a3ead83f46d63c4dd4723ef76dba770ee)[];

462} \_\_packed;

463

[ 467](group__i3c__ccc.md#ga364bcd9863f82fcc13aeb59ca7ad6504)enum [i3c\_ccc\_enttm\_defbyte](group__i3c__ccc.md#ga364bcd9863f82fcc13aeb59ca7ad6504) {

[ 469](group__i3c__ccc.md#gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207) [ENTTM\_EXIT\_TEST\_MODE](group__i3c__ccc.md#gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207) = 0x00U,

470

[ 474](group__i3c__ccc.md#gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530) [ENTTM\_VENDOR\_TEST\_MODE](group__i3c__ccc.md#gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530) = 0x01U,

475};

476

[ 490](structi3c__ccc__address.md)struct [i3c\_ccc\_address](structi3c__ccc__address.md) {

[ 505](structi3c__ccc__address.md#afc3d7db034b3fd72c6118790a18a677b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__address.md#afc3d7db034b3fd72c6118790a18a677b);

506} \_\_packed;

507

[ 511](structi3c__ccc__getpid.md)struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) {

[ 517](structi3c__ccc__getpid.md#a060023fcb180e44b39a73c0f955f02c7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pid](structi3c__ccc__getpid.md#a060023fcb180e44b39a73c0f955f02c7)[6];

518} \_\_packed;

519

[ 523](structi3c__ccc__getbcr.md)struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) {

[ 525](structi3c__ccc__getbcr.md#a09df0a49b57a38b91fe2e51c4de5c334) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__ccc__getbcr.md#a09df0a49b57a38b91fe2e51c4de5c334);

526} \_\_packed;

527

[ 531](structi3c__ccc__getdcr.md)struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) {

[ 533](structi3c__ccc__getdcr.md#a0615f439c4d556b08f7ecba8dff1c007) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__ccc__getdcr.md#a0615f439c4d556b08f7ecba8dff1c007);

534} \_\_packed;

535

536

[ 540](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648)enum [i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) {

[ 542](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b) [GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b),

543

[ 545](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f) [GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f),

546};

547

[ 551](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172)enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) {

[ 553](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb) [GETSTATUS\_FORMAT\_2\_TGTSTAT](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb) = 0x00U,

554

[ 556](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877) [GETSTATUS\_FORMAT\_2\_PRECR](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877) = 0x91U,

557

[ 559](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19) [GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19) = 0x100U

560};

561

[ 565](unioni3c__ccc__getstatus.md)union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) {

566 struct {

[ 580](unioni3c__ccc__getstatus.md#a23fe55c75741457ea399a6c7074017f6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [status](unioni3c__ccc__getstatus.md#a23fe55c75741457ea399a6c7074017f6);

[ 581](unioni3c__ccc__getstatus.md#adbc4805456634d5602ab74c2cde4d903) } [fmt1](unioni3c__ccc__getstatus.md#adbc4805456634d5602ab74c2cde4d903);

582

583 union {

[ 589](unioni3c__ccc__getstatus.md#a18b3c86f3157b3dfb30dc51127de2b69) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tgtstat](unioni3c__ccc__getstatus.md#a18b3c86f3157b3dfb30dc51127de2b69);

590

[ 603](unioni3c__ccc__getstatus.md#a104f75402b9ea4b07c9aafc376349d84) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [precr](unioni3c__ccc__getstatus.md#a104f75402b9ea4b07c9aafc376349d84);

604

[ 605](unioni3c__ccc__getstatus.md#ab7a174cc76dd5da060cf420de1f3093e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [raw\_u16](unioni3c__ccc__getstatus.md#ab7a174cc76dd5da060cf420de1f3093e);

[ 606](unioni3c__ccc__getstatus.md#ac3a7629c6d213beff8ab38863a366b11) } [fmt2](unioni3c__ccc__getstatus.md#ac3a7629c6d213beff8ab38863a366b11);

607} \_\_packed;

608

[ 610](group__i3c__ccc.md#gaee3dd61e9ac723a90868c610d0179b7d)#define I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR BIT(5)

611

[ 613](group__i3c__ccc.md#ga1006146ca810c06674fbee0ee1f66286)#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK GENMASK(7U, 6U)

614

[ 623](group__i3c__ccc.md#ga660e179384e9426b498cd62da5665b15)#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE(status) \

624 FIELD\_GET(I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK, (status))

625

[ 627](group__i3c__ccc.md#gae0bcc3ea13a34f63b073d63569d2e53a)#define I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK GENMASK(3U, 0U)

628

[ 637](group__i3c__ccc.md#ga1436dc4b9f71c6f61fd3e3331857f3bd)#define I3C\_CCC\_GETSTATUS\_NUM\_INT(status) \

638 FIELD\_GET(I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK, (status))

639

[ 641](group__i3c__ccc.md#ga94afb0ebcfce55b85fc4a81953b4178a)#define I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED BIT(0)

642

[ 644](group__i3c__ccc.md#gadda1781cae312f4e588c3d3dcfa74f38)#define I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK BIT(1)

645

[ 649](structi3c__ccc__setbrgtgt__tgt.md)struct [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) {

[ 656](structi3c__ccc__setbrgtgt__tgt.md#a6fa24f8354e856031464aaaa2c8fd1bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structi3c__ccc__setbrgtgt__tgt.md#a6fa24f8354e856031464aaaa2c8fd1bb);

657

[ 666](structi3c__ccc__setbrgtgt__tgt.md#a1dca2717ca9502f11b300a0d9a1fc0e6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structi3c__ccc__setbrgtgt__tgt.md#a1dca2717ca9502f11b300a0d9a1fc0e6);

667} \_\_packed;

668

[ 676](structi3c__ccc__setbrgtgt.md)struct [i3c\_ccc\_setbrgtgt](structi3c__ccc__setbrgtgt.md) {

[ 678](structi3c__ccc__setbrgtgt.md#a9099e2979baca2c3fbbb7a6b781edbf3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structi3c__ccc__setbrgtgt.md#a9099e2979baca2c3fbbb7a6b781edbf3);

679

[ 681](structi3c__ccc__setbrgtgt.md#aa019eb13d7da60941382c6e43884b60d) struct [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) [targets](structi3c__ccc__setbrgtgt.md#aa019eb13d7da60941382c6e43884b60d)[];

682} \_\_packed;

683

[ 687](group__i3c__ccc.md#ga1a91a7d29fc73ea18b9da614773b475f)enum [i3c\_ccc\_getmxds\_fmt](group__i3c__ccc.md#ga1a91a7d29fc73ea18b9da614773b475f) {

[ 689](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990) [GETMXDS\_FORMAT\_1](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990),

690

[ 692](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9) [GETMXDS\_FORMAT\_2](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9),

693

[ 695](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c) [GETMXDS\_FORMAT\_3](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c),

696};

697

[ 701](group__i3c__ccc.md#ga609cbfc817ec24b36c71f75092b2d4bf)enum [i3c\_ccc\_getmxds\_defbyte](group__i3c__ccc.md#ga609cbfc817ec24b36c71f75092b2d4bf) {

[ 704](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd) [GETMXDS\_FORMAT\_3\_WRRDTURN](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd) = 0x00U,

705

[ 709](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7) [GETMXDS\_FORMAT\_3\_CRHDLY](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7) = 0x91U,

710

[ 712](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6) [GETMXDS\_FORMAT\_3\_INVALID](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6) = 0x100,

713};

714

715

[ 719](unioni3c__ccc__getmxds.md)union [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) {

720 struct {

[ 722](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13);

723

[ 725](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98);

[ 726](unioni3c__ccc__getmxds.md#a242470090b40e40f0b0febfba966d766) } [fmt1](unioni3c__ccc__getmxds.md#a242470090b40e40f0b0febfba966d766);

727

728 struct {

730 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13);

731

733 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98);

734

[ 740](unioni3c__ccc__getmxds.md#a3782b5dce0db847362b9413a02d90baa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrdturn](unioni3c__ccc__getmxds.md#a3782b5dce0db847362b9413a02d90baa)[3];

[ 741](unioni3c__ccc__getmxds.md#adfb70b06d5e769fccc7630a356067fcd) } [fmt2](unioni3c__ccc__getmxds.md#adfb70b06d5e769fccc7630a356067fcd);

742

743 struct {

[ 749](unioni3c__ccc__getmxds.md#aa3c5a9fa7bc805d4cd63cb3ba774a808) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [wrrdturn](unioni3c__ccc__getmxds.md#aa3c5a9fa7bc805d4cd63cb3ba774a808)[5];

750

[ 756](unioni3c__ccc__getmxds.md#ad55160abc13a3ad04d5d6f827714f48b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crhdly1](unioni3c__ccc__getmxds.md#ad55160abc13a3ad04d5d6f827714f48b);

[ 757](unioni3c__ccc__getmxds.md#a6bb902a7335f2244365cde9782659dce) } [fmt3](unioni3c__ccc__getmxds.md#a6bb902a7335f2244365cde9782659dce);

758} \_\_packed;

759

[ 761](group__i3c__ccc.md#ga65ed8d5c2e6f562215674217f974d608)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX 0

762

[ 764](group__i3c__ccc.md#gaac6dec9aee1e1d5a56c964a4d1fe32b1)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ 1

765

[ 767](group__i3c__ccc.md#gae1ff27ad2b8c9119e2efa88c0a696555)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ 2

768

[ 770](group__i3c__ccc.md#ga409666d6a17b53e518d702863826eb28)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ 3

771

[ 773](group__i3c__ccc.md#ga5a329b3fa12ecafd6958b05bab163a5c)#define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ 4

774

[ 776](group__i3c__ccc.md#gad5e417bc3cabf8a915d1e7938415125a)#define I3C\_CCC\_GETMXDS\_TSCO\_8NS 0

777

[ 779](group__i3c__ccc.md#gaaee475f82f3a3759c7d62bb48082ebc2)#define I3C\_CCC\_GETMXDS\_TSCO\_9NS 1

780

[ 782](group__i3c__ccc.md#ga5e264e39aa2d4b602ec5e3218708e2f6)#define I3C\_CCC\_GETMXDS\_TSCO\_10NS 2

783

[ 785](group__i3c__ccc.md#ga2b27c9023f447da9c474c078091cf580)#define I3C\_CCC\_GETMXDS\_TSCO\_11NS 3

786

[ 788](group__i3c__ccc.md#ga06d33d1884a30d179aace82af956d62d)#define I3C\_CCC\_GETMXDS\_TSCO\_12NS 4

789

[ 791](group__i3c__ccc.md#ga5be034f241ccfb59534ae247d2e31d85)#define I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS 7

792

[ 794](group__i3c__ccc.md#ga43fa03b6fea48cca06d07e962c5c04ef)#define I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT BIT(3)

795

[ 797](group__i3c__ccc.md#ga5f4c6dde339c3467bdb3aea0d680d01f)#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK GENMASK(2U, 0U)

798

[ 807](group__i3c__ccc.md#gae61b18d964e575809a1ebe2189aae028)#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL(maxwr) \

808 FIELD\_GET(I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK, (maxwr))

809

[ 811](group__i3c__ccc.md#gaf5b95266cc911a37a3e46565b7601970)#define I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN BIT(6)

812

[ 814](group__i3c__ccc.md#ga41958f7756cc5dec1c0546e7832b764a)#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK GENMASK(5U, 3U)

815

[ 824](group__i3c__ccc.md#ga8284130d363dd1898de44c572b3d566c)#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO(maxrd) \

825 FIELD\_GET(I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK, (maxrd))

826

[ 828](group__i3c__ccc.md#gad8b14f71cc1d5c1a0daa27703ab0c774)#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK GENMASK(2U, 0U)

829

[ 838](group__i3c__ccc.md#gaf5ac7364357e1e123adddcbfc134a0be)#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL(maxrd) \

839 FIELD\_GET(I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK, (maxrd))

840

[ 842](group__i3c__ccc.md#ga9aa4eaf8a537323883d242e9ebb9a985)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE BIT(2)

843

[ 845](group__i3c__ccc.md#ga9ad046b7ec49bbca3f70a5a30fb1524b)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK GENMASK(1U, 0U)

846

[ 855](group__i3c__ccc.md#gab43a5adbcf158086d23c5d796a7e9399)#define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE(crhdly1) \

856 FIELD\_GET(I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK, (chrdly1))

857

[ 861](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958)enum [i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) {

[ 863](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0) [GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0),

864

[ 866](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620) [GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620),

867};

868

[ 872](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2)enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) {

[ 874](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e) [GETCAPS\_FORMAT\_2\_TGTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e) = 0x00U,

875

[ 877](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740) [GETCAPS\_FORMAT\_2\_TESTPAT](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740) = 0x5AU,

878

[ 880](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484) [GETCAPS\_FORMAT\_2\_CRCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484) = 0x91U,

881

[ 883](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984) [GETCAPS\_FORMAT\_2\_VTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984) = 0x93U,

884

[ 886](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0) [GETCAPS\_FORMAT\_2\_DBGCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0) = 0xD7U,

887

[ 889](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86) [GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86) = 0x100,

890};

891

[ 899](unioni3c__ccc__getcaps.md)union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) {

900 union {

[ 908](unioni3c__ccc__getcaps.md#ac3a378ed34efc38aa2f9605208e24cef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gethdrcap](unioni3c__ccc__getcaps.md#ac3a378ed34efc38aa2f9605208e24cef);

909

[ 935](unioni3c__ccc__getcaps.md#ab16e2b0e084371a9cbf57abf518f3e7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcaps](unioni3c__ccc__getcaps.md#ab16e2b0e084371a9cbf57abf518f3e7e)[4];

[ 936](unioni3c__ccc__getcaps.md#a908096a7dc051b59b9953575f9e5bf3b) } [fmt1](unioni3c__ccc__getcaps.md#a908096a7dc051b59b9953575f9e5bf3b);

937

938 union {

[ 944](unioni3c__ccc__getcaps.md#a99f11e2283bde1d4370a792a46ef8bad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tgtcaps](unioni3c__ccc__getcaps.md#a99f11e2283bde1d4370a792a46ef8bad)[4];

945

[ 951](unioni3c__ccc__getcaps.md#afd68057c626bb954cee2b6b46350ebae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [testpat](unioni3c__ccc__getcaps.md#afd68057c626bb954cee2b6b46350ebae);

952

[ 965](unioni3c__ccc__getcaps.md#a6266e60251e02ed9f1009ce1721adef8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crcaps](unioni3c__ccc__getcaps.md#a6266e60251e02ed9f1009ce1721adef8)[2];

966

[ 978](unioni3c__ccc__getcaps.md#ae7ab28922904daa7ef7380f0ddb41cb3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vtcaps](unioni3c__ccc__getcaps.md#ae7ab28922904daa7ef7380f0ddb41cb3)[2];

[ 979](unioni3c__ccc__getcaps.md#a4b09537b6b796aa2b4fb962d7a4c446d) } [fmt2](unioni3c__ccc__getcaps.md#a4b09537b6b796aa2b4fb962d7a4c446d);

980} \_\_packed;

981

[ 983](group__i3c__ccc.md#gab984c6a18a555e4a3c0552684083e330)#define I3C\_CCC\_GETCAPS1\_HDR\_DDR BIT(0)

984

[ 986](group__i3c__ccc.md#gafe33491b778aa806977a98c3bd12a339)#define I3C\_CCC\_GETCAPS1\_HDR\_TSP BIT(1)

987

[ 989](group__i3c__ccc.md#gae9b98ab62745f041e4fe6e89ecd3b0e6)#define I3C\_CCC\_GETCAPS1\_HDR\_TSL BIT(2)

990

[ 992](group__i3c__ccc.md#gaac01f085ed1af56d686a33694744081c)#define I3C\_CCC\_GETCAPS1\_HDR\_BT BIT(3)

993

[ 1001](group__i3c__ccc.md#gaae9483f4d5de3ba092b870b20e6b5f4a)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE(x) BIT(x)

1002

[ 1004](group__i3c__ccc.md#gad1389fc52c3fec4d6206bc56566bbf5d)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE0 BIT(0)

1005

[ 1007](group__i3c__ccc.md#gacfd20baf528fcceca7f71719e15d5ea0)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE1 BIT(1)

1008

[ 1010](group__i3c__ccc.md#ga9e5581743cbbe7363bb0919b95148d85)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE2 BIT(2)

1011

[ 1013](group__i3c__ccc.md#ga97b146596467f410ce9f063365ac9aaf)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE3 BIT(3)

1014

[ 1016](group__i3c__ccc.md#ga0dd98eeb74f493bfb04aeb698e656772)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE4 BIT(4)

1017

[ 1019](group__i3c__ccc.md#ga99bff02c40ccb15797dcf10c6dc00e87)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE5 BIT(5)

1020

[ 1022](group__i3c__ccc.md#ga12cead0a8ceb518a5c897f22b1d3dd64)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE6 BIT(6)

1023

[ 1025](group__i3c__ccc.md#ga8b3373f18c0e3b365cc199c19ae82fb0)#define I3C\_CCC\_GETCAPS1\_HDR\_MODE7 BIT(7)

1026

[ 1028](group__i3c__ccc.md#ga1c2ceeaa44ee641c3d05176baf7e681d)#define I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT BIT(6)

1029

[ 1031](group__i3c__ccc.md#ga8faf5ff5b2542a309f114ce4d6d11640)#define I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC BIT(7)

1032

[ 1037](group__i3c__ccc.md#ga64f58d1aaf847cf4a7811b20cca13b55)#define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK GENMASK(5U, 4U)

1038

[ 1047](group__i3c__ccc.md#gabeb9acdabd6dce2117e9f5830673b2ed)#define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP(getcaps2) \

1048 FIELD\_GET(I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK, (getcaps2))

1049

[ 1054](group__i3c__ccc.md#gae0015aa7768a8d5c18426a47cdbb67f8)#define I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK GENMASK(3U, 0U)

1055

[ 1065](group__i3c__ccc.md#ga093449c1cf029bddf1a25181cbfed570)#define I3C\_CCC\_GETCAPS2\_SPEC\_VER(getcaps2) \

1066 FIELD\_GET(I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK, (getcaps2))

1067

[ 1072](group__i3c__ccc.md#gaf0a2358f0f5f46c5fa1c084373f09be1)#define I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT BIT(0)

1073

[ 1078](group__i3c__ccc.md#ga08cc3c3976195642282e00ba00c1b283)#define I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT BIT(1)

1079

[ 1084](group__i3c__ccc.md#ga73829cd436decbe55d2290dc750b3918)#define I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE BIT(2)

1085

[ 1090](group__i3c__ccc.md#gaf40cc6cc08619363056e9650453a9a26)#define I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT BIT(3)

1091

[ 1096](group__i3c__ccc.md#gafbf1e9c947c40d70ae1c45991d093570)#define I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT BIT(4)

1097

[ 1102](group__i3c__ccc.md#ga3575eb8aa6fc3b49f2115104dcdfaeec)#define I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT BIT(5)

1103

[ 1108](group__i3c__ccc.md#gac13d1465aa4222be0acccbf5303f3f3e)#define I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION BIT(6)

1109

[ 1114](group__i3c__ccc.md#ga541ed236f06c20ca98e32d5a17788754)#define I3C\_CCC\_GETCAPS\_TESTPAT1 0xA5

1115

[ 1120](group__i3c__ccc.md#gafdb7ed7cc72efeb7cd62435084b1b40f)#define I3C\_CCC\_GETCAPS\_TESTPAT2 0x5A

1121

[ 1126](group__i3c__ccc.md#ga1720b3f54ade943f627b6a4e7284139a)#define I3C\_CCC\_GETCAPS\_TESTPAT3 0xA5

1127

[ 1132](group__i3c__ccc.md#ga2391e23e0b17351e3c28048b85d98ea6)#define I3C\_CCC\_GETCAPS\_TESTPAT4 0x5A

1133

[ 1138](group__i3c__ccc.md#ga98ee1cc4c436219b9639c5710fa6911b)#define I3C\_CCC\_GETCAPS\_TESTPAT 0xA55AA55A

1139

[ 1144](group__i3c__ccc.md#gad833335c6edb018edb66b99e1dfc16f7)#define I3C\_CCC\_GETCAPS\_CRCAPS1\_HJ\_SUPPORT BIT(0)

1145

[ 1150](group__i3c__ccc.md#ga86b22acbba045b037b4ae14abf4b6e5c)#define I3C\_CCC\_GETCAPS\_CRCAPS1\_GRP\_MANAGEMENT\_SUPPORT BIT(1)

1151

[ 1156](group__i3c__ccc.md#ga438621df282f451083e9ab9b1b59a2e3)#define I3C\_CCC\_GETCAPS\_CRCAPS1\_ML\_SUPPORT BIT(2)

1157

[ 1162](group__i3c__ccc.md#ga5bedcb1cb3769ae69779c0b2125b4b21)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_IBI\_TIR\_SUPPORT BIT(0)

1163

[ 1168](group__i3c__ccc.md#ga3a49b8a44676888fe600aa6b42cc52c6)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_CONTROLLER\_PASSBACK BIT(1)

1169

[ 1174](group__i3c__ccc.md#gad81d9a56d02db7e8a87279d8772adbec)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_DEEP\_SLEEP\_CAPABLE BIT(2)

1175

[ 1180](group__i3c__ccc.md#gada1a84b1394d6a72dd49e1c87307fbef)#define I3C\_CCC\_GETCAPS\_CRCAPS2\_DELAYED\_CONTROLLER\_HANDOFF BIT(3)

1181

[ 1183](group__i3c__ccc.md#ga382e8db432a701a8b2f6c8be6aba81a8)#define I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_MASK GENMASK(2U, 0U)

1184

[ 1193](group__i3c__ccc.md#ga9d0153d2e0b01a045e59e4acf4446206)#define I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE(vtcap1) \

1194 FIELD\_GET(I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_MASK, (vtcap1))

1195

[ 1200](group__i3c__ccc.md#gaca37ffb4f223c7b723a1b2ed881d28f7)#define I3C\_CCC\_GETCAPS\_VTCAP1\_SIDE\_EFFECTS BIT(4)

1201

[ 1206](group__i3c__ccc.md#gad1c0b63bb26be245e781e5d32d75dd15)#define I3C\_CCC\_GETCAPS\_VTCAP1\_SHARED\_PERIPH\_DETECT BIT(5)

1207

[ 1209](group__i3c__ccc.md#gad39e1c3d38b29937166345133ad373d1)#define I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_MASK GENMASK(1U, 0U)

1210

[ 1219](group__i3c__ccc.md#ga8ee2a538a2b5efa2e02540aac392c685)#define I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS(vtcap2) \

1220 FIELD\_GET(I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_MASK, (vtcap2))

1221

[ 1226](group__i3c__ccc.md#ga1b7562342dbf9fe443386943527d5f29)#define I3C\_CCC\_GETCAPS\_VTCAP2\_ADDRESS\_REMAPPING BIT(2)

1227

[ 1229](group__i3c__ccc.md#gadc61e60fbc59aca1ff813098f51ca56e)#define I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_MASK GENMASK(4U, 3U)

1230

[ 1239](group__i3c__ccc.md#ga56112189be57287691d64eabfaa32910)#define I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND(vtcap2) \

1240 FIELD\_GET(I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_MASK, (vtcap2))

1241

[ 1245](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1)enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) {

[ 1247](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2) [I3C\_CCC\_RSTACT\_NO\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2) = 0x00U,

1248

[ 1250](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476) [I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476) = 0x01U,

1251

[ 1253](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879) [I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879) = 0x02U,

1254

[ 1256](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519) [I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519) = 0x03U,

1257

[ 1259](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e) [I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e) = 0x04U,

1260

[ 1262](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454) [I3C\_CCC\_RSTACT\_RETURN\_TIME\_TO\_RESET\_PERIPHERAL](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454) = 0x81U,

1263

[ 1265](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95) [I3C\_CCC\_RSTACT\_RETURN\_TIME\_TO\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95) = 0x82U,

1266

[ 1268](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024) [I3C\_CCC\_RSTACT\_RETURN\_TIME\_FOR\_DEBUG\_NETWORK\_ADAPTER\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024) = 0x83U,

1269

[ 1271](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4) [I3C\_CCC\_RSTACT\_RETURN\_VIRTUAL\_TARGET\_INDICATION](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4) = 0x84U,

1272};

1273

1300

[ 1302](group__i3c__ccc.md#gae61d6a25793e701524a5cf82c2593fce)#define I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_MINOR\_VER\_MASK GENMASK(3U, 0U)

1303

[ 1311](group__i3c__ccc.md#gaadcfe82c6f945d2233a4a459bb3d0ec1)#define I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_MINOR\_VER(y) \

1312 FIELD\_PREP(I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_MINOR\_VER\_MASK, (y))

1313

[ 1315](group__i3c__ccc.md#gadcd0edb4744d934d9336d82cadd24240)#define I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_I3C\_SPEC 0

1316

[ 1318](group__i3c__ccc.md#gadde2bf9d69060283b0ed8ef0a5482739)#define I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_I3C\_BASIC\_SPEC BIT(4)

1319

[ 1321](group__i3c__ccc.md#ga8f3f783e104f897cfe0eb13481fc12e3)#define I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_I3C\_SPEC\_EDITORIAL\_1\_Y\_0 0

1322

[ 1324](group__i3c__ccc.md#ga99a1d9182e5aeeaa7f95c9bbdca377c0)#define I3C\_CCC\_SETBUSCON\_I3C\_SPEC\_I3C\_SPEC\_EDITORIAL\_1\_Y\_1 BIT(5)

1325

1327

1334

[ 1340](group__i3c__ccc.md#ga2d2a926414495bab0eae4f4284a8663b)#define I3C\_CCC\_SETBUSCON\_OTHER\_STANDARDS\_JEDEC\_SIDEBAND 128

1341

[ 1349](group__i3c__ccc.md#ga7c876c18b2fac71a0377dbb043980644)#define I3C\_CCC\_SETBUSCON\_OTHER\_STANDARDS\_MCTP 129

1350

[ 1357](group__i3c__ccc.md#gaeeb4eea07b5c6c2afea64cf2e09a2d06)#define I3C\_CCC\_SETBUSCON\_OTHER\_STANDARDS\_ETSI 130

1358

1360

[ 1371](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25)static inline bool [i3c\_ccc\_is\_payload\_broadcast](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25)(const struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload)

1372{

1373 return (payload->[ccc](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466).[id](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea) <= [I3C\_CCC\_BROADCAST\_MAX\_ID](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2));

1374}

1375

[ 1387](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c)int [i3c\_ccc\_do\_getbcr](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1388 struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) \*bcr);

1389

[ 1401](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101)int [i3c\_ccc\_do\_getdcr](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1402 struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) \*dcr);

1403

[ 1415](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df)int [i3c\_ccc\_do\_getpid](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1416 struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) \*pid);

1417

[ 1429](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7)int [i3c\_ccc\_do\_rstact\_all](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7)(const struct [device](structdevice.md) \*controller,

1430 enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) action);

1431

[ 1445](group__i3c__ccc.md#ga8a74bb1b461c6a4cad12220db55d6d7a)int [i3c\_ccc\_do\_rstact](group__i3c__ccc.md#ga8a74bb1b461c6a4cad12220db55d6d7a)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1446 enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) action,

1447 bool get,

1448 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

1449

[ 1461](group__i3c__ccc.md#gad8a5fcaa2dd494f20795ee716ebf0895)static inline int [i3c\_ccc\_do\_rstact\_fmt2](group__i3c__ccc.md#gad8a5fcaa2dd494f20795ee716ebf0895)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1462 enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) action)

1463{

1464 return [i3c\_ccc\_do\_rstact](group__i3c__ccc.md#ga8a74bb1b461c6a4cad12220db55d6d7a)(target, action, false, NULL);

1465}

1466

[ 1479](group__i3c__ccc.md#gaf26a8d605ec5d0e95d6ee1f90571946d)static inline int [i3c\_ccc\_do\_rstact\_fmt3](group__i3c__ccc.md#gaf26a8d605ec5d0e95d6ee1f90571946d)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1480 enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) action,

1481 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

1482{

1483 return [i3c\_ccc\_do\_rstact](group__i3c__ccc.md#ga8a74bb1b461c6a4cad12220db55d6d7a)(target, action, true, data);

1484}

1485

[ 1495](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7)int [i3c\_ccc\_do\_rstdaa\_all](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7)(const struct [device](structdevice.md) \*controller);

1496

[ 1511](group__i3c__ccc.md#gaf4836548527c1a7fe54767c2a7e2ebb9)int [i3c\_ccc\_do\_setdasa](group__i3c__ccc.md#gaf4836548527c1a7fe54767c2a7e2ebb9)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1512 struct [i3c\_ccc\_address](structi3c__ccc__address.md) da);

1513

[ 1527](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec)int [i3c\_ccc\_do\_setnewda](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1528 struct [i3c\_ccc\_address](structi3c__ccc__address.md) new\_da);

1529

[ 1542](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580)int [i3c\_ccc\_do\_events\_all\_set](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580)(const struct [device](structdevice.md) \*controller,

1543 bool enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events);

1544

[ 1557](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49)int [i3c\_ccc\_do\_events\_set](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1558 bool enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events);

1559

[ 1571](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)int [i3c\_ccc\_do\_entas](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4));

1572

[ 1583](group__i3c__ccc.md#gab5bb29579181747c1b7e1eafa98160e6)static inline int [i3c\_ccc\_do\_entas0](group__i3c__ccc.md#gab5bb29579181747c1b7e1eafa98160e6)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1584{

1585 return [i3c\_ccc\_do\_entas](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)(target, 0);

1586}

1587

[ 1598](group__i3c__ccc.md#ga600409049ad66072d94d39623977c137)static inline int [i3c\_ccc\_do\_entas1](group__i3c__ccc.md#ga600409049ad66072d94d39623977c137)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1599{

1600 return [i3c\_ccc\_do\_entas](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)(target, 1);

1601}

1602

[ 1613](group__i3c__ccc.md#gaeb58d2e7c779ae8e07b185f9fa290a9b)static inline int [i3c\_ccc\_do\_entas2](group__i3c__ccc.md#gaeb58d2e7c779ae8e07b185f9fa290a9b)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1614{

1615 return [i3c\_ccc\_do\_entas](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)(target, 2);

1616}

1617

[ 1628](group__i3c__ccc.md#ga35bf3fe8816d9fce44d70c8a3c8f69cb)static inline int [i3c\_ccc\_do\_entas3](group__i3c__ccc.md#ga35bf3fe8816d9fce44d70c8a3c8f69cb)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1629{

1630 return [i3c\_ccc\_do\_entas](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)(target, 3);

1631}

1632

[ 1643](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)int [i3c\_ccc\_do\_entas\_all](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)(const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4));

1644

[ 1654](group__i3c__ccc.md#ga0d4c999391fca23598a4339b6c9d4ad6)static inline int [i3c\_ccc\_do\_entas0\_all](group__i3c__ccc.md#ga0d4c999391fca23598a4339b6c9d4ad6)(const struct [device](structdevice.md) \*controller)

1655{

1656 return [i3c\_ccc\_do\_entas\_all](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)(controller, 0);

1657}

1658

[ 1668](group__i3c__ccc.md#ga93b5f2cf21cf7a201bf76e3d665fc40f)static inline int [i3c\_ccc\_do\_entas1\_all](group__i3c__ccc.md#ga93b5f2cf21cf7a201bf76e3d665fc40f)(const struct [device](structdevice.md) \*controller)

1669{

1670 return [i3c\_ccc\_do\_entas\_all](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)(controller, 1);

1671}

1672

[ 1682](group__i3c__ccc.md#gacf89ee65aafdcab713f30c8e2675e58b)static inline int [i3c\_ccc\_do\_entas2\_all](group__i3c__ccc.md#gacf89ee65aafdcab713f30c8e2675e58b)(const struct [device](structdevice.md) \*controller)

1683{

1684 return [i3c\_ccc\_do\_entas\_all](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)(controller, 2);

1685}

1686

[ 1696](group__i3c__ccc.md#gaeecb153a2cb3bdc196d00fb60c3e3b24)static inline int [i3c\_ccc\_do\_entas3\_all](group__i3c__ccc.md#gaeecb153a2cb3bdc196d00fb60c3e3b24)(const struct [device](structdevice.md) \*controller)

1697{

1698 return [i3c\_ccc\_do\_entas\_all](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)(controller, 3);

1699}

1700

[ 1712](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d)int [i3c\_ccc\_do\_setmwl\_all](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d)(const struct [device](structdevice.md) \*controller,

1713 const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl);

1714

[ 1726](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49)int [i3c\_ccc\_do\_setmwl](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1727 const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl);

1728

[ 1740](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507)int [i3c\_ccc\_do\_getmwl](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1741 struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl);

1742

[ 1756](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0)int [i3c\_ccc\_do\_setmrl\_all](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0)(const struct [device](structdevice.md) \*controller,

1757 const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl,

1758 bool has\_ibi\_size);

1759

[ 1774](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a)int [i3c\_ccc\_do\_setmrl](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1775 const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl);

1776

[ 1791](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485)int [i3c\_ccc\_do\_getmrl](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1792 struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl);

1793

[ 1804](group__i3c__ccc.md#ga5c1b2aa3b5915db2540a1affb17a4f10)int [i3c\_ccc\_do\_enttm](group__i3c__ccc.md#ga5c1b2aa3b5915db2540a1affb17a4f10)(const struct [device](structdevice.md) \*controller,

1805 enum [i3c\_ccc\_enttm\_defbyte](group__i3c__ccc.md#ga364bcd9863f82fcc13aeb59ca7ad6504) defbyte);

1806

[ 1823](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)int [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1824 union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status,

1825 enum [i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) fmt,

1826 enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) defbyte);

1827

[ 1839](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95)static inline int [i3c\_ccc\_do\_getstatus\_fmt1](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1840 union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status)

1841{

1842 return [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)(target, status,

1843 [GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b),

1844 [GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19));

1845}

1846

[ 1859](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)static inline int [i3c\_ccc\_do\_getstatus\_fmt2](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1860 union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status,

1861 enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) defbyte)

1862{

1863 return [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)(target, status,

1864 [GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f), defbyte);

1865}

1866

[ 1883](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)int [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1884 union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps,

1885 enum [i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) fmt,

1886 enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) defbyte);

1887

[ 1899](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89)static inline int [i3c\_ccc\_do\_getcaps\_fmt1](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1900 union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps)

1901{

1902 return [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)(target, caps,

1903 [GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0),

1904 [GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86));

1905}

1906

[ 1919](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd)static inline int [i3c\_ccc\_do\_getcaps\_fmt2](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1920 union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps,

1921 enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) defbyte)

1922{

1923 return [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)(target, caps,

1924 [GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620), defbyte);

1925}

1926

[ 1940](group__i3c__ccc.md#ga72e76917e96f8ac572c42c6598f3bce4)int [i3c\_ccc\_do\_setvendor](group__i3c__ccc.md#ga72e76917e96f8ac572c42c6598f3bce4)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1941 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

1942 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload,

1943 size\_t len);

1944

[ 1959](group__i3c__ccc.md#ga2a1786ee4a809b50dad7e1d42c9afb0b)int [i3c\_ccc\_do\_getvendor](group__i3c__ccc.md#ga2a1786ee4a809b50dad7e1d42c9afb0b)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1960 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

1961 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload,

1962 size\_t len,

1963 size\_t \*num\_xfer);

1964

[ 1981](group__i3c__ccc.md#ga4cbdcbc2d991bc1e542a562fdbc2563c)int [i3c\_ccc\_do\_getvendor\_defbyte](group__i3c__ccc.md#ga4cbdcbc2d991bc1e542a562fdbc2563c)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1982 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

1983 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) defbyte,

1984 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload,

1985 size\_t len,

1986 size\_t \*num\_xfer);

1987

[ 2000](group__i3c__ccc.md#ga7ce52b4e19f3721e3b054455be42e3d0)int [i3c\_ccc\_do\_setvendor\_all](group__i3c__ccc.md#ga7ce52b4e19f3721e3b054455be42e3d0)(const struct [device](structdevice.md) \*controller,

2001 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

2002 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload,

2003 size\_t len);

2004

[ 2016](group__i3c__ccc.md#gab3c93ba0a6e606508a59e65c931dd144)int [i3c\_ccc\_do\_setaasa\_all](group__i3c__ccc.md#gab3c93ba0a6e606508a59e65c931dd144)(const struct [device](structdevice.md) \*controller);

2017

[ 2034](group__i3c__ccc.md#ga6949426eaf9c3a30dc402e2e11da1dcd)int [i3c\_ccc\_do\_getmxds](group__i3c__ccc.md#ga6949426eaf9c3a30dc402e2e11da1dcd)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2035 union [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) \*caps,

2036 enum [i3c\_ccc\_getmxds\_fmt](group__i3c__ccc.md#ga1a91a7d29fc73ea18b9da614773b475f) fmt,

2037 enum [i3c\_ccc\_getmxds\_defbyte](group__i3c__ccc.md#ga609cbfc817ec24b36c71f75092b2d4bf) defbyte);

2038

[ 2050](group__i3c__ccc.md#gaa58e1bff5cc9b9e4a32ae4159494125b)static inline int [i3c\_ccc\_do\_getmxds\_fmt1](group__i3c__ccc.md#gaa58e1bff5cc9b9e4a32ae4159494125b)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2051 union [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) \*caps)

2052{

2053 return [i3c\_ccc\_do\_getmxds](group__i3c__ccc.md#ga6949426eaf9c3a30dc402e2e11da1dcd)(target, caps,

2054 [GETMXDS\_FORMAT\_1](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990),

2055 [GETMXDS\_FORMAT\_3\_INVALID](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6));

2056}

2057

[ 2069](group__i3c__ccc.md#ga5a111a0e9ba5037861585d5356d4e950)static inline int [i3c\_ccc\_do\_getmxds\_fmt2](group__i3c__ccc.md#ga5a111a0e9ba5037861585d5356d4e950)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2070 union [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) \*caps)

2071{

2072 return [i3c\_ccc\_do\_getmxds](group__i3c__ccc.md#ga6949426eaf9c3a30dc402e2e11da1dcd)(target, caps,

2073 [GETMXDS\_FORMAT\_2](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9),

2074 [GETMXDS\_FORMAT\_3\_INVALID](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6));

2075}

2076

[ 2089](group__i3c__ccc.md#ga58a37d7bb50937a936923e3e6b74fc96)static inline int [i3c\_ccc\_do\_getmxds\_fmt3](group__i3c__ccc.md#ga58a37d7bb50937a936923e3e6b74fc96)(const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2090 union [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) \*caps,

2091 enum [i3c\_ccc\_getmxds\_defbyte](group__i3c__ccc.md#ga609cbfc817ec24b36c71f75092b2d4bf) defbyte)

2092{

2093 return [i3c\_ccc\_do\_getmxds](group__i3c__ccc.md#ga6949426eaf9c3a30dc402e2e11da1dcd)(target, caps,

2094 [GETMXDS\_FORMAT\_3](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c), defbyte);

2095}

2096

[ 2105](group__i3c__ccc.md#ga0f04a73d8b26b93091108fc55d7a54d3)int [i3c\_ccc\_do\_deftgts\_all](group__i3c__ccc.md#ga0f04a73d8b26b93091108fc55d7a54d3)(const struct [device](structdevice.md) \*controller,

2106 struct [i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md) \*deftgts);

2107

[ 2119](group__i3c__ccc.md#ga71e5cbf818b17eb35196ef773b992ed5)int [i3c\_ccc\_do\_setbuscon](group__i3c__ccc.md#ga71e5cbf818b17eb35196ef773b992ed5)(const struct [device](structdevice.md) \*controller,

2120 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*context, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

2121

2122#ifdef \_\_cplusplus

2123}

2124#endif

2125

2129

2130#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_CCC\_H\_ \*/

[as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4)

irp nz macro MOVR cc s mov cc s endm endr irp as

**Definition** asm-macro-32-bit-gnu.h:16

[device.h](device_8h.md)

[i3c\_ccc\_do\_entas0\_all](group__i3c__ccc.md#ga0d4c999391fca23598a4339b6c9d4ad6)

static int i3c\_ccc\_do\_entas0\_all(const struct device \*controller)

Broadcast ENTAS0.

**Definition** ccc.h:1654

[i3c\_ccc\_do\_deftgts\_all](group__i3c__ccc.md#ga0f04a73d8b26b93091108fc55d7a54d3)

int i3c\_ccc\_do\_deftgts\_all(const struct device \*controller, struct i3c\_ccc\_deftgts \*deftgts)

Broadcast DEFTGTS.

[i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172)

i3c\_ccc\_getstatus\_defbyte

Defining byte values for GETSTATUS Format 2.

**Definition** ccc.h:551

[i3c\_ccc\_getmxds\_fmt](group__i3c__ccc.md#ga1a91a7d29fc73ea18b9da614773b475f)

i3c\_ccc\_getmxds\_fmt

Indicate which format of getmxds to use.

**Definition** ccc.h:687

[i3c\_ccc\_do\_getstatus\_fmt1](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95)

static int i3c\_ccc\_do\_getstatus\_fmt1(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getstatus \*status)

Single target GETSTATUS to Get Target Status (Format 1).

**Definition** ccc.h:1839

[i3c\_ccc\_do\_setmrl\_all](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0)

int i3c\_ccc\_do\_setmrl\_all(const struct device \*controller, const struct i3c\_ccc\_mrl \*mrl, bool has\_ibi\_size)

Broadcast SETMRL to Set Maximum Read Length.

[i3c\_ccc\_do\_getvendor](group__i3c__ccc.md#ga2a1786ee4a809b50dad7e1d42c9afb0b)

int i3c\_ccc\_do\_getvendor(const struct i3c\_device\_desc \*target, uint8\_t id, uint8\_t \*payload, size\_t len, size\_t \*num\_xfer)

Single target to Get Vendor / Standard Extension CCC.

[i3c\_ccc\_do\_entas3](group__i3c__ccc.md#ga35bf3fe8816d9fce44d70c8a3c8f69cb)

static int i3c\_ccc\_do\_entas3(const struct i3c\_device\_desc \*target)

Direct ENTAS3.

**Definition** ccc.h:1628

[i3c\_ccc\_enttm\_defbyte](group__i3c__ccc.md#ga364bcd9863f82fcc13aeb59ca7ad6504)

i3c\_ccc\_enttm\_defbyte

Defining byte values for ENTTM.

**Definition** ccc.h:467

[i3c\_ccc\_do\_rstact\_all](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7)

int i3c\_ccc\_do\_rstact\_all(const struct device \*controller, enum i3c\_ccc\_rstact\_defining\_byte action)

Broadcast RSTACT to reset I3C Peripheral (Format 1).

[i3c\_ccc\_do\_getvendor\_defbyte](group__i3c__ccc.md#ga4cbdcbc2d991bc1e542a562fdbc2563c)

int i3c\_ccc\_do\_getvendor\_defbyte(const struct i3c\_device\_desc \*target, uint8\_t id, uint8\_t defbyte, uint8\_t \*payload, size\_t len, size\_t \*num\_xfer)

Single target to Get Vendor / Standard Extension CCC with a defining byte.

[i3c\_ccc\_do\_getstatus\_fmt2](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)

static int i3c\_ccc\_do\_getstatus\_fmt2(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getstatus \*status, enum i3c\_ccc\_getstatus\_defbyte defbyte)

Single target GETSTATUS to Get Target Status (Format 2).

**Definition** ccc.h:1859

[i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe)

int i3c\_ccc\_do\_getstatus(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getstatus \*status, enum i3c\_ccc\_getstatus\_fmt fmt, enum i3c\_ccc\_getstatus\_defbyte defbyte)

Single target GETSTATUS to Get Target Status.

[i3c\_ccc\_do\_getmxds\_fmt3](group__i3c__ccc.md#ga58a37d7bb50937a936923e3e6b74fc96)

static int i3c\_ccc\_do\_getmxds\_fmt3(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getmxds \*caps, enum i3c\_ccc\_getmxds\_defbyte defbyte)

Single target GETMXDS to Get Max Data Speed (Format 3).

**Definition** ccc.h:2089

[i3c\_ccc\_do\_getmxds\_fmt2](group__i3c__ccc.md#ga5a111a0e9ba5037861585d5356d4e950)

static int i3c\_ccc\_do\_getmxds\_fmt2(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getmxds \*caps)

Single target GETMXDS to Get Max Data Speed (Format 2).

**Definition** ccc.h:2069

[i3c\_ccc\_do\_enttm](group__i3c__ccc.md#ga5c1b2aa3b5915db2540a1affb17a4f10)

int i3c\_ccc\_do\_enttm(const struct device \*controller, enum i3c\_ccc\_enttm\_defbyte defbyte)

Broadcast ENTTM.

[i3c\_ccc\_do\_entas1](group__i3c__ccc.md#ga600409049ad66072d94d39623977c137)

static int i3c\_ccc\_do\_entas1(const struct i3c\_device\_desc \*target)

Direct ENTAS1.

**Definition** ccc.h:1598

[i3c\_ccc\_getmxds\_defbyte](group__i3c__ccc.md#ga609cbfc817ec24b36c71f75092b2d4bf)

i3c\_ccc\_getmxds\_defbyte

Enum for I3C Get Max Data Speed (GETMXDS) Format 3 Defining Byte Values.

**Definition** ccc.h:701

[i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1)

i3c\_ccc\_rstact\_defining\_byte

Enum for I3C Reset Action (RSTACT) Defining Byte Values.

**Definition** ccc.h:1245

[i3c\_ccc\_do\_setmwl\_all](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d)

int i3c\_ccc\_do\_setmwl\_all(const struct device \*controller, const struct i3c\_ccc\_mwl \*mwl)

Broadcast SETMWL to Set Maximum Write Length.

[i3c\_ccc\_do\_entas](group__i3c__ccc.md#ga66ffb47bf3dcf53c31fbbf6fd451a221)

int i3c\_ccc\_do\_entas(const struct i3c\_device\_desc \*target, uint8\_t as)

Direct ENTAS to set the Activity State.

[i3c\_ccc\_do\_getmxds](group__i3c__ccc.md#ga6949426eaf9c3a30dc402e2e11da1dcd)

int i3c\_ccc\_do\_getmxds(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getmxds \*caps, enum i3c\_ccc\_getmxds\_fmt fmt, enum i3c\_ccc\_getmxds\_defbyte defbyte)

Single target GETMXDS to Get Max Data Speed.

[i3c\_ccc\_do\_setnewda](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec)

int i3c\_ccc\_do\_setnewda(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_address new\_da)

Set New Dynamic Address for a target.

[i3c\_ccc\_do\_setmrl](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a)

int i3c\_ccc\_do\_setmrl(const struct i3c\_device\_desc \*target, const struct i3c\_ccc\_mrl \*mrl)

Single target SETMRL to Set Maximum Read Length.

[i3c\_ccc\_do\_setbuscon](group__i3c__ccc.md#ga71e5cbf818b17eb35196ef773b992ed5)

int i3c\_ccc\_do\_setbuscon(const struct device \*controller, uint8\_t \*context, uint16\_t length)

Broadcast SETBUSCON to set the bus context.

[i3c\_ccc\_do\_setvendor](group__i3c__ccc.md#ga72e76917e96f8ac572c42c6598f3bce4)

int i3c\_ccc\_do\_setvendor(const struct i3c\_device\_desc \*target, uint8\_t id, uint8\_t \*payload, size\_t len)

Single target to Set Vendor / Standard Extension CCC.

[i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648)

i3c\_ccc\_getstatus\_fmt

Indicate which format of GETSTATUS to use.

**Definition** ccc.h:540

[i3c\_ccc\_do\_setvendor\_all](group__i3c__ccc.md#ga7ce52b4e19f3721e3b054455be42e3d0)

int i3c\_ccc\_do\_setvendor\_all(const struct device \*controller, uint8\_t id, uint8\_t \*payload, size\_t len)

Broadcast Set Vendor / Standard Extension CCC.

[i3c\_ccc\_do\_getbcr](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c)

int i3c\_ccc\_do\_getbcr(struct i3c\_device\_desc \*target, struct i3c\_ccc\_getbcr \*bcr)

Get BCR from a target.

[i3c\_ccc\_do\_getdcr](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101)

int i3c\_ccc\_do\_getdcr(struct i3c\_device\_desc \*target, struct i3c\_ccc\_getdcr \*dcr)

Get DCR from a target.

[i3c\_ccc\_do\_rstact](group__i3c__ccc.md#ga8a74bb1b461c6a4cad12220db55d6d7a)

int i3c\_ccc\_do\_rstact(const struct i3c\_device\_desc \*target, enum i3c\_ccc\_rstact\_defining\_byte action, bool get, uint8\_t \*data)

Single target RSTACT to reset I3C Peripheral.

[i3c\_ccc\_do\_entas1\_all](group__i3c__ccc.md#ga93b5f2cf21cf7a201bf76e3d665fc40f)

static int i3c\_ccc\_do\_entas1\_all(const struct device \*controller)

Broadcast ENTAS1.

**Definition** ccc.h:1668

[i3c\_ccc\_do\_getpid](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df)

int i3c\_ccc\_do\_getpid(struct i3c\_device\_desc \*target, struct i3c\_ccc\_getpid \*pid)

Get PID from a target.

[i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e)

int i3c\_ccc\_do\_getcaps(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getcaps \*caps, enum i3c\_ccc\_getcaps\_fmt fmt, enum i3c\_ccc\_getcaps\_defbyte defbyte)

Single target GETCAPS to Get Target Status.

[i3c\_ccc\_do\_entas\_all](group__i3c__ccc.md#gaa14442ecb3768cb4c3c435c0c1138778)

int i3c\_ccc\_do\_entas\_all(const struct device \*controller, uint8\_t as)

Broadcast ENTAS to set the Activity State.

[i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958)

i3c\_ccc\_getcaps\_fmt

Indicate which format of GETCAPS to use.

**Definition** ccc.h:861

[i3c\_ccc\_do\_getmxds\_fmt1](group__i3c__ccc.md#gaa58e1bff5cc9b9e4a32ae4159494125b)

static int i3c\_ccc\_do\_getmxds\_fmt1(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getmxds \*caps)

Single target GETMXDS to Get Max Data Speed (Format 1).

**Definition** ccc.h:2050

[i3c\_ccc\_do\_getcaps\_fmt2](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd)

static int i3c\_ccc\_do\_getcaps\_fmt2(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getcaps \*caps, enum i3c\_ccc\_getcaps\_defbyte defbyte)

Single target GETCAPS to Get Capabilities (Format 2).

**Definition** ccc.h:1919

[i3c\_ccc\_is\_payload\_broadcast](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25)

static bool i3c\_ccc\_is\_payload\_broadcast(const struct i3c\_ccc\_payload \*payload)

Test if I3C CCC payload is for broadcast.

**Definition** ccc.h:1371

[i3c\_ccc\_do\_rstdaa\_all](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7)

int i3c\_ccc\_do\_rstdaa\_all(const struct device \*controller)

Broadcast RSTDAA to reset dynamic addresses for all targets.

[i3c\_ccc\_do\_setaasa\_all](group__i3c__ccc.md#gab3c93ba0a6e606508a59e65c931dd144)

int i3c\_ccc\_do\_setaasa\_all(const struct device \*controller)

Broadcast SETAASA to set all target's dynamic address to their static address.

[i3c\_ccc\_do\_setmwl](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49)

int i3c\_ccc\_do\_setmwl(const struct i3c\_device\_desc \*target, const struct i3c\_ccc\_mwl \*mwl)

Single target SETMWL to Set Maximum Write Length.

[i3c\_ccc\_do\_entas0](group__i3c__ccc.md#gab5bb29579181747c1b7e1eafa98160e6)

static int i3c\_ccc\_do\_entas0(const struct i3c\_device\_desc \*target)

Direct ENTAS0.

**Definition** ccc.h:1583

[i3c\_ccc\_do\_getmrl](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485)

int i3c\_ccc\_do\_getmrl(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_mrl \*mrl)

Single target GETMRL to Get Maximum Read Length.

[i3c\_ccc\_do\_entas2\_all](group__i3c__ccc.md#gacf89ee65aafdcab713f30c8e2675e58b)

static int i3c\_ccc\_do\_entas2\_all(const struct device \*controller)

Broadcast ENTAS2.

**Definition** ccc.h:1682

[i3c\_ccc\_do\_rstact\_fmt2](group__i3c__ccc.md#gad8a5fcaa2dd494f20795ee716ebf0895)

static int i3c\_ccc\_do\_rstact\_fmt2(const struct i3c\_device\_desc \*target, enum i3c\_ccc\_rstact\_defining\_byte action)

Single target RSTACT to reset I3C Peripheral (Format 2).

**Definition** ccc.h:1461

[i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2)

i3c\_ccc\_getcaps\_defbyte

Enum for I3C Get Capabilities (GETCAPS) Format 2 Defining Byte Values.

**Definition** ccc.h:872

[i3c\_ccc\_do\_entas2](group__i3c__ccc.md#gaeb58d2e7c779ae8e07b185f9fa290a9b)

static int i3c\_ccc\_do\_entas2(const struct i3c\_device\_desc \*target)

Direct ENTAS2.

**Definition** ccc.h:1613

[i3c\_ccc\_do\_getcaps\_fmt1](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89)

static int i3c\_ccc\_do\_getcaps\_fmt1(const struct i3c\_device\_desc \*target, union i3c\_ccc\_getcaps \*caps)

Single target GETCAPS to Get Capabilities (Format 1).

**Definition** ccc.h:1899

[i3c\_ccc\_do\_entas3\_all](group__i3c__ccc.md#gaeecb153a2cb3bdc196d00fb60c3e3b24)

static int i3c\_ccc\_do\_entas3\_all(const struct device \*controller)

Broadcast ENTAS3.

**Definition** ccc.h:1696

[i3c\_ccc\_do\_getmwl](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507)

int i3c\_ccc\_do\_getmwl(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_mwl \*mwl)

Single target GETMWL to Get Maximum Write Length.

[i3c\_ccc\_do\_rstact\_fmt3](group__i3c__ccc.md#gaf26a8d605ec5d0e95d6ee1f90571946d)

static int i3c\_ccc\_do\_rstact\_fmt3(const struct i3c\_device\_desc \*target, enum i3c\_ccc\_rstact\_defining\_byte action, uint8\_t \*data)

Single target RSTACT to reset I3C Peripheral (Format 3).

**Definition** ccc.h:1479

[i3c\_ccc\_do\_setdasa](group__i3c__ccc.md#gaf4836548527c1a7fe54767c2a7e2ebb9)

int i3c\_ccc\_do\_setdasa(const struct i3c\_device\_desc \*target, struct i3c\_ccc\_address da)

Set Dynamic Address from Static Address for a target.

[i3c\_ccc\_do\_events\_all\_set](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580)

int i3c\_ccc\_do\_events\_all\_set(const struct device \*controller, bool enable, struct i3c\_ccc\_events \*events)

Broadcast ENEC/DISEC to enable/disable target events.

[i3c\_ccc\_do\_events\_set](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49)

int i3c\_ccc\_do\_events\_set(struct i3c\_device\_desc \*target, bool enable, struct i3c\_ccc\_events \*events)

Direct CCC ENEC/DISEC to enable/disable target events.

[I3C\_CCC\_BROADCAST\_MAX\_ID](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)

#define I3C\_CCC\_BROADCAST\_MAX\_ID

Maximum CCC ID for broadcast.

**Definition** ccc.h:29

[GETSTATUS\_FORMAT\_2\_PRECR](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877)

@ GETSTATUS\_FORMAT\_2\_PRECR

PRECR - Alternate status format describing Controller-capable device.

**Definition** ccc.h:556

[GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19)

@ GETSTATUS\_FORMAT\_2\_INVALID

Invalid defining byte.

**Definition** ccc.h:559

[GETSTATUS\_FORMAT\_2\_TGTSTAT](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb)

@ GETSTATUS\_FORMAT\_2\_TGTSTAT

Target status.

**Definition** ccc.h:553

[GETMXDS\_FORMAT\_2](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9)

@ GETMXDS\_FORMAT\_2

GETMXDS Format 2.

**Definition** ccc.h:692

[GETMXDS\_FORMAT\_1](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990)

@ GETMXDS\_FORMAT\_1

GETMXDS Format 1.

**Definition** ccc.h:689

[GETMXDS\_FORMAT\_3](group__i3c__ccc.md#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c)

@ GETMXDS\_FORMAT\_3

GETMXDS Format 3.

**Definition** ccc.h:695

[ENTTM\_EXIT\_TEST\_MODE](group__i3c__ccc.md#gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207)

@ ENTTM\_EXIT\_TEST\_MODE

Remove all I3C Devices from Test Mode.

**Definition** ccc.h:469

[ENTTM\_VENDOR\_TEST\_MODE](group__i3c__ccc.md#gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530)

@ ENTTM\_VENDOR\_TEST\_MODE

Indicates that I3C Devices shall return a random 32-bit value in the PID during the Dynamic Address A...

**Definition** ccc.h:474

[GETMXDS\_FORMAT\_3\_INVALID](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6)

@ GETMXDS\_FORMAT\_3\_INVALID

Invalid defining byte.

**Definition** ccc.h:712

[GETMXDS\_FORMAT\_3\_CRHDLY](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7)

@ GETMXDS\_FORMAT\_3\_CRHDLY

Delay parameters for a Controller-capable Device, and it's expected Activity State during a Controlle...

**Definition** ccc.h:709

[GETMXDS\_FORMAT\_3\_WRRDTURN](group__i3c__ccc.md#gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd)

@ GETMXDS\_FORMAT\_3\_WRRDTURN

Standard Target Write/Read speed parameters, and optional Maximum Read Turnaround Time.

**Definition** ccc.h:704

[I3C\_CCC\_RSTACT\_RETURN\_VIRTUAL\_TARGET\_INDICATION](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4)

@ I3C\_CCC\_RSTACT\_RETURN\_VIRTUAL\_TARGET\_INDICATION

Return Virtual Target Indication.

**Definition** ccc.h:1271

[I3C\_CCC\_RSTACT\_RETURN\_TIME\_TO\_RESET\_PERIPHERAL](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454)

@ I3C\_CCC\_RSTACT\_RETURN\_TIME\_TO\_RESET\_PERIPHERAL

Return Time to Reset Peripheral.

**Definition** ccc.h:1262

[I3C\_CCC\_RSTACT\_RETURN\_TIME\_TO\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95)

@ I3C\_CCC\_RSTACT\_RETURN\_TIME\_TO\_WHOLE\_TARGET

Return Time to Reset Whole Target.

**Definition** ccc.h:1265

[I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476)

@ I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY

Reset the I3C Peripheral Only.

**Definition** ccc.h:1250

[I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519)

@ I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER

Debug Network Adapter Reset.

**Definition** ccc.h:1256

[I3C\_CCC\_RSTACT\_NO\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2)

@ I3C\_CCC\_RSTACT\_NO\_RESET

No Reset on Target Reset Pattern.

**Definition** ccc.h:1247

[I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e)

@ I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT

Virtual Target Detect.

**Definition** ccc.h:1259

[I3C\_CCC\_RSTACT\_RETURN\_TIME\_FOR\_DEBUG\_NETWORK\_ADAPTER\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024)

@ I3C\_CCC\_RSTACT\_RETURN\_TIME\_FOR\_DEBUG\_NETWORK\_ADAPTER\_RESET

Return Time for Debug Network Adapter Reset.

**Definition** ccc.h:1268

[I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879)

@ I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET

Reset the Whole Target.

**Definition** ccc.h:1253

[GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f)

@ GETSTATUS\_FORMAT\_2

GETSTATUS Format 2.

**Definition** ccc.h:545

[GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b)

@ GETSTATUS\_FORMAT\_1

GETSTATUS Format 1.

**Definition** ccc.h:542

[GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0)

@ GETCAPS\_FORMAT\_1

GETCAPS Format 1.

**Definition** ccc.h:863

[GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620)

@ GETCAPS\_FORMAT\_2

GETCAPS Format 2.

**Definition** ccc.h:866

[GETCAPS\_FORMAT\_2\_CRCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484)

@ GETCAPS\_FORMAT\_2\_CRCAPS

Controller handoff capabilities and features.

**Definition** ccc.h:880

[GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86)

@ GETCAPS\_FORMAT\_2\_INVALID

Invalid defining byte.

**Definition** ccc.h:889

[GETCAPS\_FORMAT\_2\_TGTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e)

@ GETCAPS\_FORMAT\_2\_TGTCAPS

Standard Target capabilities and features.

**Definition** ccc.h:874

[GETCAPS\_FORMAT\_2\_DBGCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0)

@ GETCAPS\_FORMAT\_2\_DBGCAPS

Debug-capable Device capabilities and features.

**Definition** ccc.h:886

[GETCAPS\_FORMAT\_2\_VTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984)

@ GETCAPS\_FORMAT\_2\_VTCAPS

Virtual Target capabilities and features.

**Definition** ccc.h:883

[GETCAPS\_FORMAT\_2\_TESTPAT](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740)

@ GETCAPS\_FORMAT\_2\_TESTPAT

Fixed 32b test pattern.

**Definition** ccc.h:877

[stdint.h](stdint_8h.md)

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

**Definition** device.h:412

[i3c\_ccc\_address](structi3c__ccc__address.md)

Payload for a single device address.

**Definition** ccc.h:490

[i3c\_ccc\_address::addr](structi3c__ccc__address.md#afc3d7db034b3fd72c6118790a18a677b)

uint8\_t addr

**Definition** ccc.h:505

[i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md)

The active controller part of payload for DEFTGTS CCC.

**Definition** ccc.h:403

[i3c\_ccc\_deftgts\_active\_controller::addr](structi3c__ccc__deftgts__active__controller.md#a4d7671db542bb70ef623be26804c154a)

uint8\_t addr

Dynamic Address of Active Controller.

**Definition** ccc.h:405

[i3c\_ccc\_deftgts\_active\_controller::dcr](structi3c__ccc__deftgts__active__controller.md#a7acd12fad49f565a6b8a71993b6ad5d4)

uint8\_t dcr

Device Characteristic Register of Active Controller.

**Definition** ccc.h:408

[i3c\_ccc\_deftgts\_active\_controller::static\_addr](structi3c__ccc__deftgts__active__controller.md#ae2fb1ebc28ef1f69c6114af0b25875d3)

uint8\_t static\_addr

Static Address of Active Controller.

**Definition** ccc.h:414

[i3c\_ccc\_deftgts\_active\_controller::bcr](structi3c__ccc__deftgts__active__controller.md#aeb56808d9b998c51d5b30307e0212328)

uint8\_t bcr

Bus Characteristic Register of Active Controller.

**Definition** ccc.h:411

[i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md)

The target device part of payload for DEFTGTS CCC.

**Definition** ccc.h:423

[i3c\_ccc\_deftgts\_target::dcr](structi3c__ccc__deftgts__target.md#a08689c18d74fa4b74fc2ada055394e65)

uint8\_t dcr

Device Characteristic Register of a I3C target device or a group.

**Definition** ccc.h:432

[i3c\_ccc\_deftgts\_target::addr](structi3c__ccc__deftgts__target.md#a34a02df3d4dc456733746437b2cd983a)

uint8\_t addr

Dynamic Address of a target device, or a group address.

**Definition** ccc.h:425

[i3c\_ccc\_deftgts\_target::static\_addr](structi3c__ccc__deftgts__target.md#a7374dd59c060462af7ca366ae7165107)

uint8\_t static\_addr

Static Address of a target device or a group.

**Definition** ccc.h:442

[i3c\_ccc\_deftgts\_target::bcr](structi3c__ccc__deftgts__target.md#a7c234182e16da66c308e86d72591063d)

uint8\_t bcr

Bus Characteristic Register of a target device or a group.

**Definition** ccc.h:439

[i3c\_ccc\_deftgts\_target::lvr](structi3c__ccc__deftgts__target.md#ab4fbe6aac8d5860ef90613e51b15ef83)

uint8\_t lvr

Legacy Virtual Register for legacy I2C device.

**Definition** ccc.h:435

[i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md)

Payload for DEFTGTS CCC (Define List of Targets).

**Definition** ccc.h:453

[i3c\_ccc\_deftgts::active\_controller](structi3c__ccc__deftgts.md#a1f59c280bd388eb7e7818eb674b5f12f)

struct i3c\_ccc\_deftgts\_active\_controller active\_controller

Data describing the active controller.

**Definition** ccc.h:458

[i3c\_ccc\_deftgts::targets](structi3c__ccc__deftgts.md#a3ead83f46d63c4dd4723ef76dba770ee)

struct i3c\_ccc\_deftgts\_target targets[]

Data describing the target(s) on the bus.

**Definition** ccc.h:461

[i3c\_ccc\_deftgts::count](structi3c__ccc__deftgts.md#a82a12e711417111855d76171fbd008c2)

uint8\_t count

Number of Targets (and Groups) present on the I3C Bus.

**Definition** ccc.h:455

[i3c\_ccc\_events](structi3c__ccc__events.md)

Payload for ENEC/DISEC CCC (Target Events Command).

**Definition** ccc.h:313

[i3c\_ccc\_events::events](structi3c__ccc__events.md#ac34bcdae31cdc718eb54962d6b707320)

uint8\_t events

Event byte:

**Definition** ccc.h:323

[i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md)

Payload for GETBCR CCC (Get Bus Characteristics Register).

**Definition** ccc.h:523

[i3c\_ccc\_getbcr::bcr](structi3c__ccc__getbcr.md#a09df0a49b57a38b91fe2e51c4de5c334)

uint8\_t bcr

Bus Characteristics Register.

**Definition** ccc.h:525

[i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md)

Payload for GETDCR CCC (Get Device Characteristics Register).

**Definition** ccc.h:531

[i3c\_ccc\_getdcr::dcr](structi3c__ccc__getdcr.md#a0615f439c4d556b08f7ecba8dff1c007)

uint8\_t dcr

Device Characteristics Register.

**Definition** ccc.h:533

[i3c\_ccc\_getpid](structi3c__ccc__getpid.md)

Payload for GETPID CCC (Get Provisioned ID).

**Definition** ccc.h:511

[i3c\_ccc\_getpid::pid](structi3c__ccc__getpid.md#a060023fcb180e44b39a73c0f955f02c7)

uint8\_t pid[6]

48-bit Provisioned ID.

**Definition** ccc.h:517

[i3c\_ccc\_mrl](structi3c__ccc__mrl.md)

Payload for SETMRL/GETMRL CCC (Set/Get Maximum Read Length).

**Definition** ccc.h:389

[i3c\_ccc\_mrl::len](structi3c__ccc__mrl.md#a381d52439049c6a13d232e4e94d17335)

uint16\_t len

Maximum Read Length.

**Definition** ccc.h:391

[i3c\_ccc\_mrl::ibi\_len](structi3c__ccc__mrl.md#a7480df4486c9eb8a11581e42ff3b6b67)

uint8\_t ibi\_len

Optional IBI Payload Size.

**Definition** ccc.h:394

[i3c\_ccc\_mwl](structi3c__ccc__mwl.md)

Payload for SETMWL/GETMWL CCC (Set/Get Maximum Write Length).

**Definition** ccc.h:376

[i3c\_ccc\_mwl::len](structi3c__ccc__mwl.md#a5312fa1fc7cc93dfdf88d490352cf08e)

uint16\_t len

Maximum Write Length.

**Definition** ccc.h:378

[i3c\_ccc\_payload](structi3c__ccc__payload.md)

Payload structure for one CCC transaction.

**Definition** ccc.h:267

[i3c\_ccc\_payload::payloads](structi3c__ccc__payload.md#a3dcab72bf5b627426f963df56514c38d)

struct i3c\_ccc\_target\_payload \* payloads

Array of struct i3c\_ccc\_target\_payload.

**Definition** ccc.h:303

[i3c\_ccc\_payload::ccc](structi3c__ccc__payload.md#a45b2f35955bbb2bcaf89077e5abf3466)

struct i3c\_ccc\_payload::@244074337306206345253052323277302146014310207057 ccc

[i3c\_ccc\_payload::num\_xfer](structi3c__ccc__payload.md#a9d0f7efcc7774941f057c2ab0fb14439)

size\_t num\_xfer

Total number of bytes transferred.

**Definition** ccc.h:291

[i3c\_ccc\_payload::targets](structi3c__ccc__payload.md#aa93b97b77f8dff8e931731c1f9edcd86)

struct i3c\_ccc\_payload::@313273325003250135275363022311173067156230063067 targets

[i3c\_ccc\_payload::data](structi3c__ccc__payload.md#ac52dbf51c5d7903c02c9f149e47a1b0b)

uint8\_t \* data

Pointer to byte array of data for this CCC.

**Definition** ccc.h:280

[i3c\_ccc\_payload::id](structi3c__ccc__payload.md#ae6aa0a3465af855872ae0006def29fea)

uint8\_t id

The CCC ID (I3C\_CCC\_\*).

**Definition** ccc.h:272

[i3c\_ccc\_payload::num\_targets](structi3c__ccc__payload.md#afc1706d47d22300e7fa44754920b2685)

size\_t num\_targets

Number of targets.

**Definition** ccc.h:306

[i3c\_ccc\_payload::data\_len](structi3c__ccc__payload.md#afcc17965b8bdd0e5e26cd15cebe49cee)

size\_t data\_len

Length in bytes for optional data array.

**Definition** ccc.h:283

[i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md)

One Bridged Target for SETBRGTGT payload.

**Definition** ccc.h:649

[i3c\_ccc\_setbrgtgt\_tgt::id](structi3c__ccc__setbrgtgt__tgt.md#a1dca2717ca9502f11b300a0d9a1fc0e6)

uint16\_t id

16-bit ID for the bridged target.

**Definition** ccc.h:666

[i3c\_ccc\_setbrgtgt\_tgt::addr](structi3c__ccc__setbrgtgt__tgt.md#a6fa24f8354e856031464aaaa2c8fd1bb)

uint8\_t addr

Dynamic address of the bridged target.

**Definition** ccc.h:656

[i3c\_ccc\_setbrgtgt](structi3c__ccc__setbrgtgt.md)

Payload for SETBRGTGT CCC (Set Bridge Targets).

**Definition** ccc.h:676

[i3c\_ccc\_setbrgtgt::count](structi3c__ccc__setbrgtgt.md#a9099e2979baca2c3fbbb7a6b781edbf3)

uint8\_t count

Number of bridged targets.

**Definition** ccc.h:678

[i3c\_ccc\_setbrgtgt::targets](structi3c__ccc__setbrgtgt.md#aa019eb13d7da60941382c6e43884b60d)

struct i3c\_ccc\_setbrgtgt\_tgt targets[]

Array of bridged targets.

**Definition** ccc.h:681

[i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md)

Payload structure for Direct CCC to one target.

**Definition** ccc.h:235

[i3c\_ccc\_target\_payload::addr](structi3c__ccc__target__payload.md#a2669978506b20ef01569357fbd3a9eef)

uint8\_t addr

Target address.

**Definition** ccc.h:237

[i3c\_ccc\_target\_payload::data\_len](structi3c__ccc__target__payload.md#a5ddda39b2aeb2818b389d4df1e25ba0a)

size\_t data\_len

Length in bytes for data.

**Definition** ccc.h:252

[i3c\_ccc\_target\_payload::rnw](structi3c__ccc__target__payload.md#aa09ebbfdff5d9d97be1558a63bb3535e)

uint8\_t rnw

0 for Write, 1 for Read

**Definition** ccc.h:240

[i3c\_ccc\_target\_payload::data](structi3c__ccc__target__payload.md#abc655b08df77701275038e80bfb5ba85)

uint8\_t \* data

**Definition** ccc.h:249

[i3c\_ccc\_target\_payload::num\_xfer](structi3c__ccc__target__payload.md#ae6091f0b1cc804f9658d941f6ab493ef)

size\_t num\_xfer

Total number of bytes transferred.

**Definition** ccc.h:261

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:913

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md)

Payload for GETCAPS CCC (Get Optional Feature Capabilities).

**Definition** ccc.h:899

[i3c\_ccc\_getcaps::fmt2](unioni3c__ccc__getcaps.md#a4b09537b6b796aa2b4fb962d7a4c446d)

union i3c\_ccc\_getcaps::@146137206326133235367372076147075060054306320326 fmt2

[i3c\_ccc\_getcaps::crcaps](unioni3c__ccc__getcaps.md#a6266e60251e02ed9f1009ce1721adef8)

uint8\_t crcaps[2]

Defining Byte 0x91: CRCAPS Byte 1 CRCAPS1.

**Definition** ccc.h:965

[i3c\_ccc\_getcaps::fmt1](unioni3c__ccc__getcaps.md#a908096a7dc051b59b9953575f9e5bf3b)

union i3c\_ccc\_getcaps::@176040264012374126324364077104322017272005341010 fmt1

[i3c\_ccc\_getcaps::tgtcaps](unioni3c__ccc__getcaps.md#a99f11e2283bde1d4370a792a46ef8bad)

uint8\_t tgtcaps[4]

Defining Byte 0x00: TGTCAPS.

**Definition** ccc.h:944

[i3c\_ccc\_getcaps::getcaps](unioni3c__ccc__getcaps.md#ab16e2b0e084371a9cbf57abf518f3e7e)

uint8\_t getcaps[4]

I3C v1.1+ Device Capabilities Byte 1 GETCAPS1.

**Definition** ccc.h:935

[i3c\_ccc\_getcaps::gethdrcap](unioni3c__ccc__getcaps.md#ac3a378ed34efc38aa2f9605208e24cef)

uint8\_t gethdrcap

I3C v1.0 HDR Capabilities.

**Definition** ccc.h:908

[i3c\_ccc\_getcaps::vtcaps](unioni3c__ccc__getcaps.md#ae7ab28922904daa7ef7380f0ddb41cb3)

uint8\_t vtcaps[2]

Defining Byte 0x93: VTCAPS Byte 1 VTCAPS1.

**Definition** ccc.h:978

[i3c\_ccc\_getcaps::testpat](unioni3c__ccc__getcaps.md#afd68057c626bb954cee2b6b46350ebae)

uint32\_t testpat

Defining Byte 0x5A: TESTPAT.

**Definition** ccc.h:951

[i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md)

Payload for GETMXDS CCC (Get Max Data Speed).

**Definition** ccc.h:719

[i3c\_ccc\_getmxds::fmt1](unioni3c__ccc__getmxds.md#a242470090b40e40f0b0febfba966d766)

struct i3c\_ccc\_getmxds::@017052066027027356133300167277077144205177366071 fmt1

[i3c\_ccc\_getmxds::maxrdturn](unioni3c__ccc__getmxds.md#a3782b5dce0db847362b9413a02d90baa)

uint8\_t maxrdturn[3]

Maximum Read Turnaround Time in microsecond.

**Definition** ccc.h:740

[i3c\_ccc\_getmxds::maxrd](unioni3c__ccc__getmxds.md#a668e1ed30b96a40534d96e4b56ce7e98)

uint8\_t maxrd

maxRd

**Definition** ccc.h:725

[i3c\_ccc\_getmxds::fmt3](unioni3c__ccc__getmxds.md#a6bb902a7335f2244365cde9782659dce)

struct i3c\_ccc\_getmxds::@010015006355067367227170356377125232044011313157 fmt3

[i3c\_ccc\_getmxds::maxwr](unioni3c__ccc__getmxds.md#a9307643fd53554053b38cda5a0663a13)

uint8\_t maxwr

maxWr

**Definition** ccc.h:722

[i3c\_ccc\_getmxds::wrrdturn](unioni3c__ccc__getmxds.md#aa3c5a9fa7bc805d4cd63cb3ba774a808)

uint8\_t wrrdturn[5]

Defining Byte 0x00: WRRDTURN.

**Definition** ccc.h:749

[i3c\_ccc\_getmxds::crhdly1](unioni3c__ccc__getmxds.md#ad55160abc13a3ad04d5d6f827714f48b)

uint8\_t crhdly1

Defining Byte 0x91: CRHDLY.

**Definition** ccc.h:756

[i3c\_ccc\_getmxds::fmt2](unioni3c__ccc__getmxds.md#adfb70b06d5e769fccc7630a356067fcd)

struct i3c\_ccc\_getmxds::@275016223350235350204161354245210176063371342011 fmt2

[i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md)

Payload for GETSTATUS CCC (Get Device Status).

**Definition** ccc.h:565

[i3c\_ccc\_getstatus::precr](unioni3c__ccc__getstatus.md#a104f75402b9ea4b07c9aafc376349d84)

uint16\_t precr

Defining Byte 0x91: PRECR.

**Definition** ccc.h:603

[i3c\_ccc\_getstatus::tgtstat](unioni3c__ccc__getstatus.md#a18b3c86f3157b3dfb30dc51127de2b69)

uint16\_t tgtstat

Defining Byte 0x00: TGTSTAT.

**Definition** ccc.h:589

[i3c\_ccc\_getstatus::status](unioni3c__ccc__getstatus.md#a23fe55c75741457ea399a6c7074017f6)

uint16\_t status

Device Status.

**Definition** ccc.h:580

[i3c\_ccc\_getstatus::raw\_u16](unioni3c__ccc__getstatus.md#ab7a174cc76dd5da060cf420de1f3093e)

uint16\_t raw\_u16

**Definition** ccc.h:605

[i3c\_ccc\_getstatus::fmt2](unioni3c__ccc__getstatus.md#ac3a7629c6d213beff8ab38863a366b11)

union i3c\_ccc\_getstatus::@360213032036351112213166306142126266072045035100 fmt2

[i3c\_ccc\_getstatus::fmt1](unioni3c__ccc__getstatus.md#adbc4805456634d5602ab74c2cde4d903)

struct i3c\_ccc\_getstatus::@040236027257025211003163330350055024304173214342 fmt1

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [ccc.h](ccc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
