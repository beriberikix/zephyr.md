---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ots_8h_source.html
original_path: doxygen/html/ots_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ots.h

[Go to the documentation of this file.](ots_8h.md)

1/\*

2 \* Copyright (c) 2020-2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_OTS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_OTS\_H\_

9

19

20#include <[stdbool.h](stdbool_8h.md)>

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

24

25#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

26#include <[zephyr/sys/util.h](sys_2util_8h.md)>

27#include <[zephyr/sys/crc.h](crc_8h.md)>

28#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

29#include <[zephyr/bluetooth/uuid.h](uuid_8h.md)>

30#include <[zephyr/bluetooth/gatt.h](gatt_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 37](group__bt__ots.md#gad5e4a66f017facc2a185ee0a55a0c3ee)#define BT\_OTS\_OBJ\_ID\_SIZE 6

38

[ 40](group__bt__ots.md#ga79110fa56a524754d74bf20ac6a766aa)#define BT\_OTS\_OBJ\_ID\_MIN 0x000000000100ULL

41

[ 43](group__bt__ots.md#gabd777e7a1b7adaaacfec3e084c3a9bfe)#define BT\_OTS\_OBJ\_ID\_MAX 0xFFFFFFFFFFFFULL

44

[ 46](group__bt__ots.md#ga4a6a0b0a3c8d10f3668e61c9dee0e05e)#define OTS\_OBJ\_ID\_DIR\_LIST 0x000000000000ULL

47

[ 49](group__bt__ots.md#gabe3d54a6dfa0d52a97826c140c603d78)#define BT\_OTS\_OBJ\_ID\_MASK BIT64\_MASK(48)

50

[ 52](group__bt__ots.md#ga2754eeb7418ed762a3119fc56871d37e)#define BT\_OTS\_OBJ\_ID\_STR\_LEN 15

53

[ 55](structbt__ots__obj__type.md)struct [bt\_ots\_obj\_type](structbt__ots__obj__type.md) {

56 union {

57 /\* Used to indicate UUID type \*/

[ 58](structbt__ots__obj__type.md#a89a8dbe566579422df503dd577ea8d42) struct [bt\_uuid](structbt__uuid.md) [uuid](structbt__ots__obj__type.md#a89a8dbe566579422df503dd577ea8d42);

59

60 /\* 16-bit UUID value \*/

[ 61](structbt__ots__obj__type.md#ae39b7a368314d1a771cf3573d2077095) struct [bt\_uuid\_16](structbt__uuid__16.md) [uuid\_16](structbt__ots__obj__type.md#ae39b7a368314d1a771cf3573d2077095);

62

63 /\* 128-bit UUID value \*/

[ 64](structbt__ots__obj__type.md#aedf0e5d45f6f4912a8eeae077eda17be) struct [bt\_uuid\_128](structbt__uuid__128.md) [uuid\_128](structbt__ots__obj__type.md#aedf0e5d45f6f4912a8eeae077eda17be);

65 };

66};

67

69enum {

[ 71](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) [BT\_OTS\_OBJ\_PROP\_DELETE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) = 0,

72

[ 74](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) [BT\_OTS\_OBJ\_PROP\_EXECUTE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) = 1,

75

[ 77](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) [BT\_OTS\_OBJ\_PROP\_READ](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) = 2,

78

[ 80](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) [BT\_OTS\_OBJ\_PROP\_WRITE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) = 3,

81

[ 86](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) [BT\_OTS\_OBJ\_PROP\_APPEND](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) = 4,

87

[ 89](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) [BT\_OTS\_OBJ\_PROP\_TRUNCATE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) = 5,

90

[ 96](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) [BT\_OTS\_OBJ\_PROP\_PATCH](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) = 6,

97

[ 99](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) [BT\_OTS\_OBJ\_PROP\_MARKED](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) = 7,

100};

101

[ 106](group__bt__ots.md#ga6ad37ee172d6518e7316b4e0ec8f27c7)#define BT\_OTS\_OBJ\_SET\_PROP\_DELETE(prop) \

107 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_DELETE, 1)

108

[ 113](group__bt__ots.md#ga2342f00ef480b279d737bcddc8e2faf0)#define BT\_OTS\_OBJ\_SET\_PROP\_EXECUTE(prop) \

114 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_EXECUTE, 1)

115

[ 120](group__bt__ots.md#gaba26016beff74b1b6ec75ba083cf808d)#define BT\_OTS\_OBJ\_SET\_PROP\_READ(prop) \

121 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_READ, 1)

122

[ 127](group__bt__ots.md#gaeb1a5a907478fd668199a27e20fc2173)#define BT\_OTS\_OBJ\_SET\_PROP\_WRITE(prop) \

128 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_WRITE, 1)

129

[ 134](group__bt__ots.md#gaa1eff1b4ee05fb91d87dcb85dd7469e1)#define BT\_OTS\_OBJ\_SET\_PROP\_APPEND(prop) \

135 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_APPEND, 1)

136

[ 141](group__bt__ots.md#ga8f99514414958d031a4e9985c8cc976b)#define BT\_OTS\_OBJ\_SET\_PROP\_TRUNCATE(prop) \

142 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_TRUNCATE, 1)

143

[ 148](group__bt__ots.md#gac36c68dfeb21bf705f87f11e847c5aed)#define BT\_OTS\_OBJ\_SET\_PROP\_PATCH(prop) \

149 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_PATCH, 1)

150

[ 155](group__bt__ots.md#gae21e599a85549d5cd4462c0f36c291ac)#define BT\_OTS\_OBJ\_SET\_PROP\_MARKED(prop) \

156 WRITE\_BIT(prop, BT\_OTS\_OBJ\_PROP\_MARKED, 1)

157

[ 162](group__bt__ots.md#ga7a735cf89c9986624e34b183282a65ee)#define BT\_OTS\_OBJ\_GET\_PROP\_DELETE(prop) \

163 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_DELETE))

164

[ 169](group__bt__ots.md#ga90619bdcf5ec9a942f7d81f6c87465fc)#define BT\_OTS\_OBJ\_GET\_PROP\_EXECUTE(prop) \

170 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_EXECUTE))

171

[ 176](group__bt__ots.md#gae846afdc9f6c40b2bf6d2ae67deb8eef)#define BT\_OTS\_OBJ\_GET\_PROP\_READ(prop) \

177 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_READ))

178

[ 183](group__bt__ots.md#ga9769628cbe2c81161607c6518d3d4798)#define BT\_OTS\_OBJ\_GET\_PROP\_WRITE(prop) \

184 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_WRITE))

185

[ 190](group__bt__ots.md#gaccbf81f9a9ebcc70801739a4a8fafcd8)#define BT\_OTS\_OBJ\_GET\_PROP\_APPEND(prop) \

191 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_APPEND))

192

[ 197](group__bt__ots.md#gac7b6632aac554db5b4d5b9f3e8bf78b4)#define BT\_OTS\_OBJ\_GET\_PROP\_TRUNCATE(prop) \

198 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_TRUNCATE))

199

[ 204](group__bt__ots.md#ga6c8ccb5f8919f062b1b44e1b4981907d)#define BT\_OTS\_OBJ\_GET\_PROP\_PATCH(prop) \

205 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_PATCH))

206

[ 211](group__bt__ots.md#gaeffab993f4fbe15090a7a626cd56f034)#define BT\_OTS\_OBJ\_GET\_PROP\_MARKED(prop) \

212 ((prop) & BIT(BT\_OTS\_OBJ\_PROP\_MARKED))

213

[ 215](structbt__ots__obj__size.md)struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) {

[ 217](structbt__ots__obj__size.md#a217290f0fae68a54046eef50ac2a3773) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cur](structbt__ots__obj__size.md#a217290f0fae68a54046eef50ac2a3773);

218

[ 220](structbt__ots__obj__size.md#a86a5675532eae69d40b3305436e81cfb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [alloc](structbt__ots__obj__size.md#a86a5675532eae69d40b3305436e81cfb);

221} \_\_packed;

222

224enum {

[ 226](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) [BT\_OTS\_OACP\_FEAT\_CREATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) = 0,

227

[ 229](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) [BT\_OTS\_OACP\_FEAT\_DELETE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) = 1,

230

[ 232](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) [BT\_OTS\_OACP\_FEAT\_CHECKSUM](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) = 2,

233

[ 235](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) [BT\_OTS\_OACP\_FEAT\_EXECUTE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) = 3,

236

[ 238](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) [BT\_OTS\_OACP\_FEAT\_READ](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) = 4,

239

[ 241](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) [BT\_OTS\_OACP\_FEAT\_WRITE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) = 5,

242

[ 244](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) [BT\_OTS\_OACP\_FEAT\_APPEND](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) = 6,

245

[ 247](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) [BT\_OTS\_OACP\_FEAT\_TRUNCATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) = 7,

248

[ 250](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) [BT\_OTS\_OACP\_FEAT\_PATCH](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) = 8,

251

[ 253](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) [BT\_OTS\_OACP\_FEAT\_ABORT](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) = 9,

254};

255

256/\*

257 \* @enum bt\_ots\_oacp\_write\_op\_mode

258 \* @brief Mode Parameter for OACP Write Op Code.

259 \*/

[ 260](group__bt__ots.md#gaebdd2b8a80948d1050d42fa3963cc863)enum [bt\_ots\_oacp\_write\_op\_mode](group__bt__ots.md#gaebdd2b8a80948d1050d42fa3963cc863) {

[ 261](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab) [BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab) = 0,

[ 262](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a) [BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

263};

264

[ 269](group__bt__ots.md#ga8cc851f268de24fe3445a9a0c3af6abf)#define BT\_OTS\_OACP\_SET\_FEAT\_CREATE(feat) \

270 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_CREATE, 1)

271

[ 276](group__bt__ots.md#ga9306e9a2b8ea468f28eb73b7d412032e)#define BT\_OTS\_OACP\_SET\_FEAT\_DELETE(feat) \

277 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_DELETE, 1)

278

[ 283](group__bt__ots.md#gaba4d7e446212dc6c2139c324d22edc10)#define BT\_OTS\_OACP\_SET\_FEAT\_CHECKSUM(feat) \

284 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_CHECKSUM, 1)

285

[ 290](group__bt__ots.md#ga4b19d199947053e7b2f93b64ea83c29a)#define BT\_OTS\_OACP\_SET\_FEAT\_EXECUTE(feat) \

291 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_EXECUTE, 1)

292

[ 297](group__bt__ots.md#ga5508cf6698e2927333f31cb0cffce831)#define BT\_OTS\_OACP\_SET\_FEAT\_READ(feat) \

298 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_READ, 1)

299

[ 304](group__bt__ots.md#gac035cb71a2caabd16bb64d27b56e32c7)#define BT\_OTS\_OACP\_SET\_FEAT\_WRITE(feat) \

305 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_WRITE, 1)

306

[ 311](group__bt__ots.md#gaabae304227bed27796ad2a346963fa86)#define BT\_OTS\_OACP\_SET\_FEAT\_APPEND(feat) \

312 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_APPEND, 1)

313

[ 318](group__bt__ots.md#gae5f0e14f685d40782952345ebe50eb3d)#define BT\_OTS\_OACP\_SET\_FEAT\_TRUNCATE(feat) \

319 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_TRUNCATE, 1)

320

[ 325](group__bt__ots.md#gabca8354bc176bd819005ca213a148b87)#define BT\_OTS\_OACP\_SET\_FEAT\_PATCH(feat) \

326 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_PATCH, 1)

327

[ 332](group__bt__ots.md#ga3bb8eb9f732947daf289dfe40e171248)#define BT\_OTS\_OACP\_SET\_FEAT\_ABORT(feat) \

333 WRITE\_BIT(feat, BT\_OTS\_OACP\_FEAT\_ABORT, 1)

334

[ 339](group__bt__ots.md#ga058d8d1fb255ca66057c1edfc547def4)#define BT\_OTS\_OACP\_GET\_FEAT\_CREATE(feat) \

340 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_CREATE))

341

[ 346](group__bt__ots.md#ga815632fc160921a074bec60250df47f2)#define BT\_OTS\_OACP\_GET\_FEAT\_DELETE(feat) \

347 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_DELETE))

348

[ 353](group__bt__ots.md#gabbc141c9a7d5614971b87b727cbf01af)#define BT\_OTS\_OACP\_GET\_FEAT\_CHECKSUM(feat) \

354 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_CHECKSUM))

355

[ 360](group__bt__ots.md#ga2ac0d82e8fab9fa22b5dc3396c8641ad)#define BT\_OTS\_OACP\_GET\_FEAT\_EXECUTE(feat) \

361 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_EXECUTE))

362

[ 367](group__bt__ots.md#gac53739b9fd65124f601e92b29b9123cd)#define BT\_OTS\_OACP\_GET\_FEAT\_READ(feat) \

368 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_READ))

369

[ 374](group__bt__ots.md#ga390d957c514b2f182ff3d1d0c2221822)#define BT\_OTS\_OACP\_GET\_FEAT\_WRITE(feat) \

375 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_WRITE))

376

[ 381](group__bt__ots.md#ga36f5cc04fce18390bf1cde3e0e8a6184)#define BT\_OTS\_OACP\_GET\_FEAT\_APPEND(feat) \

382 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_APPEND))

383

[ 388](group__bt__ots.md#ga9ca79d43292354f1558943f944dd53a7)#define BT\_OTS\_OACP\_GET\_FEAT\_TRUNCATE(feat) \

389 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_TRUNCATE))

390

[ 395](group__bt__ots.md#gaca6591a0c7e8650fa827a7a43fcca81e)#define BT\_OTS\_OACP\_GET\_FEAT\_PATCH(feat) \

396 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_PATCH))

397

[ 402](group__bt__ots.md#ga196a2aceeecd620baacf0727e1427341)#define BT\_OTS\_OACP\_GET\_FEAT\_ABORT(feat) \

403 ((feat) & BIT(BT\_OTS\_OACP\_FEAT\_ABORT))

404

406enum {

[ 408](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) [BT\_OTS\_OLCP\_FEAT\_GO\_TO](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) = 0,

409

[ 411](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) [BT\_OTS\_OLCP\_FEAT\_ORDER](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) = 1,

412

[ 414](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) = 2,

415

[ 417](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) [BT\_OTS\_OLCP\_FEAT\_CLEAR](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) = 3,

418};

419

[ 424](group__bt__ots.md#gafe219709f2bd318af66cad4e118df658)#define BT\_OTS\_OLCP\_SET\_FEAT\_GO\_TO(feat) \

425 WRITE\_BIT(feat, BT\_OTS\_OLCP\_FEAT\_GO\_TO, 1)

426

[ 431](group__bt__ots.md#ga1248c694ff2d9ded862f37d03d98e2f0)#define BT\_OTS\_OLCP\_SET\_FEAT\_ORDER(feat) \

432 WRITE\_BIT(feat, BT\_OTS\_OLCP\_FEAT\_ORDER, 1)

433

[ 438](group__bt__ots.md#ga1cee6e1affdff27aa0ba6a655c9bf09c)#define BT\_OTS\_OLCP\_SET\_FEAT\_NUM\_REQ(feat) \

439 WRITE\_BIT(feat, BT\_OTS\_OLCP\_FEAT\_NUM\_REQ, 1)

440

[ 445](group__bt__ots.md#ga7a3f8d3b725c8c31d5e3062d46db4438)#define BT\_OTS\_OLCP\_SET\_FEAT\_CLEAR(feat) \

446 WRITE\_BIT(feat, BT\_OTS\_OLCP\_FEAT\_CLEAR, 1)

447

[ 452](group__bt__ots.md#ga7ec49843849613ee3f8f72209cae68c2)#define BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO(feat) \

453 ((feat) & BIT(BT\_OTS\_OLCP\_FEAT\_GO\_TO))

454

[ 459](group__bt__ots.md#gad4393e56c94c2484cd344b48cb54b255)#define BT\_OTS\_OLCP\_GET\_FEAT\_ORDER(feat) \

460 ((feat) & BIT(BT\_OTS\_OLCP\_FEAT\_ORDER))

461

[ 466](group__bt__ots.md#ga2a1a62e410586b1117fd3571e42363d8)#define BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ(feat) \

467 ((feat) & BIT(BT\_OTS\_OLCP\_FEAT\_NUM\_REQ))

468

[ 473](group__bt__ots.md#ga0f57d172615d1c6ea857506dc0c10e55)#define BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR(feat) \

474 ((feat) & BIT(BT\_OTS\_OLCP\_FEAT\_CLEAR))

475

[ 477](structbt__ots__feat.md)struct [bt\_ots\_feat](structbt__ots__feat.md) {

478 /\* OACP Features \*/

[ 479](structbt__ots__feat.md#a714abba341b1f4a50edfa73dd5048f28) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [oacp](structbt__ots__feat.md#a714abba341b1f4a50edfa73dd5048f28);

480

481 /\* OLCP Features \*/

[ 482](structbt__ots__feat.md#a309b3e38a0f15c49c06a5ffeb873cef3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [olcp](structbt__ots__feat.md#a309b3e38a0f15c49c06a5ffeb873cef3);

483} \_\_packed;

484

486enum {

[ 488](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb) [BT\_OTS\_METADATA\_REQ\_NAME](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 490](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9) [BT\_OTS\_METADATA\_REQ\_TYPE](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 492](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5) [BT\_OTS\_METADATA\_REQ\_SIZE](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 494](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095) [BT\_OTS\_METADATA\_REQ\_CREATED](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 496](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e) [BT\_OTS\_METADATA\_REQ\_MODIFIED](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 498](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2) [BT\_OTS\_METADATA\_REQ\_ID](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 500](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f) [BT\_OTS\_METADATA\_REQ\_PROPS](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 502](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf) [BT\_OTS\_METADATA\_REQ\_ALL](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf) = 0x7F,

503};

504

[ 506](structbt__ots__date__time.md)struct [bt\_ots\_date\_time](structbt__ots__date__time.md) {

[ 507](structbt__ots__date__time.md#af348ad2613ba309de6a93d357bcce3bc) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [year](structbt__ots__date__time.md#af348ad2613ba309de6a93d357bcce3bc);

[ 508](structbt__ots__date__time.md#ac3959eac8188df6114d70aed1ccbf3f4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month](structbt__ots__date__time.md#ac3959eac8188df6114d70aed1ccbf3f4);

[ 509](structbt__ots__date__time.md#a09ca928752dc844e89de3957d1baae3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [day](structbt__ots__date__time.md#a09ca928752dc844e89de3957d1baae3c);

[ 510](structbt__ots__date__time.md#ae139a310b4d17078f52bfbe7707e185a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hours](structbt__ots__date__time.md#ae139a310b4d17078f52bfbe7707e185a);

[ 511](structbt__ots__date__time.md#acc118b311bfdcb3c2f7801121831fcd6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minutes](structbt__ots__date__time.md#acc118b311bfdcb3c2f7801121831fcd6);

[ 512](structbt__ots__date__time.md#a4eb6899dbce61478b97025958c62f586) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [seconds](structbt__ots__date__time.md#a4eb6899dbce61478b97025958c62f586);

513};

[ 514](group__bt__ots.md#ga56cd1131414fa19e3ec30e2a1a241689)#define BT\_OTS\_DATE\_TIME\_FIELD\_SIZE 7

515

[ 521](structbt__ots__obj__metadata.md)struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) {

522

523#if defined(CONFIG\_BT\_OTS)

525 char \*name;

526#endif /\* CONFIG\_BT\_OTS \*/

527

528#if defined(CONFIG\_BT\_OTS\_CLIENT)

529 /\* TODO: Unify client/server name \*/

531 char name\_c[CONFIG\_BT\_OTS\_OBJ\_MAX\_NAME\_LEN + 1];

532#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

533

[ 535](structbt__ots__obj__metadata.md#aee93aef1932e9c8b4cb0c8055e5cb055) struct [bt\_ots\_obj\_type](structbt__ots__obj__type.md) [type](structbt__ots__obj__metadata.md#aee93aef1932e9c8b4cb0c8055e5cb055);

536

[ 538](structbt__ots__obj__metadata.md#afd451a3b531250db1d45eb6ddb4d9b0f) struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) [size](structbt__ots__obj__metadata.md#afd451a3b531250db1d45eb6ddb4d9b0f);

539

540#if defined(CONFIG\_BT\_OTS\_CLIENT)

542 struct [bt\_ots\_date\_time](structbt__ots__date__time.md) first\_created;

543

545 struct [bt\_ots\_date\_time](structbt__ots__date__time.md) modified;

546

548 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id;

549#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

550

[ 552](structbt__ots__obj__metadata.md#aa4ffe00ede40ff23ab5788c82ec2ac38) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [props](structbt__ots__obj__metadata.md#aa4ffe00ede40ff23ab5788c82ec2ac38);

553};

554

556struct bt\_ots;

557

[ 559](structbt__ots__obj__add__param.md)struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) {

[ 561](structbt__ots__obj__add__param.md#a721734439b43e40324c3a548b5a4eb34) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structbt__ots__obj__add__param.md#a721734439b43e40324c3a548b5a4eb34);

562

[ 564](structbt__ots__obj__add__param.md#afdbaf218850d4bf3f40f7a9e8d7b0595) struct [bt\_ots\_obj\_type](structbt__ots__obj__type.md) [type](structbt__ots__obj__add__param.md#afdbaf218850d4bf3f40f7a9e8d7b0595);

565};

566

[ 573](structbt__ots__obj__created__desc.md)struct [bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md) {

[ 583](structbt__ots__obj__created__desc.md#af69db0a3c56c6d3085f20fbb405b436e) char \*[name](structbt__ots__obj__created__desc.md#af69db0a3c56c6d3085f20fbb405b436e);

584

[ 594](structbt__ots__obj__created__desc.md#adb52cffa29c08ee1131415faeaf13cda) struct [bt\_ots\_obj\_size](structbt__ots__obj__size.md) [size](structbt__ots__obj__created__desc.md#adb52cffa29c08ee1131415faeaf13cda);

595

[ 597](structbt__ots__obj__created__desc.md#a50b2b2ae0b87690d1995187bae577e8c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [props](structbt__ots__obj__created__desc.md#a50b2b2ae0b87690d1995187bae577e8c);

598};

599

[ 601](structbt__ots__cb.md)struct [bt\_ots\_cb](structbt__ots__cb.md) {

[ 624](structbt__ots__cb.md#a0c95b2bc382474be3c1ae849936a8206) int (\*[obj\_created](structbt__ots__cb.md#a0c95b2bc382474be3c1ae849936a8206))(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id,

625 const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \*add\_param,

626 struct [bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md) \*created\_desc);

627

[ 649](structbt__ots__cb.md#a2fd78b43691e83c1faa86c1748ab2359) int (\*[obj\_deleted](structbt__ots__cb.md#a2fd78b43691e83c1faa86c1748ab2359))(struct bt\_ots \*ots, struct bt\_conn \*conn,

650 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

651

[ 660](structbt__ots__cb.md#ae8602aef0fd001d6768dc20c8873742d) void (\*[obj\_selected](structbt__ots__cb.md#ae8602aef0fd001d6768dc20c8873742d))(struct bt\_ots \*ots, struct bt\_conn \*conn,

661 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

662

[ 683](structbt__ots__cb.md#ab67ca0032b8b2fd9b8fbe6c117c186dd) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[obj\_read](structbt__ots__cb.md#ab67ca0032b8b2fd9b8fbe6c117c186dd))(struct bt\_ots \*ots, struct bt\_conn \*conn,

684 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, void \*\*data, size\_t len,

685 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset);

686

[ 713](structbt__ots__cb.md#ae31da190c9c6bee086e4d7f8fcd6fbb5) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[obj\_write](structbt__ots__cb.md#ae31da190c9c6bee086e4d7f8fcd6fbb5))(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id,

714 const void \*data, size\_t len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

715 size\_t rem);

716

[ 729](structbt__ots__cb.md#a600fa13a97f39e3bd53c524039e2733c) void (\*[obj\_name\_written](structbt__ots__cb.md#a600fa13a97f39e3bd53c524039e2733c))(struct bt\_ots \*ots, struct bt\_conn \*conn,

730 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const char \*cur\_name, const char \*new\_name);

731

[ 747](structbt__ots__cb.md#a2ef2245c017015b81c0f276f00fd6f79) int (\*[obj\_cal\_checksum](structbt__ots__cb.md#a2ef2245c017015b81c0f276f00fd6f79))(struct bt\_ots \*ots, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id,

748 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t len, void \*\*data);

749};

750

[ 752](structbt__ots__init__param.md)struct [bt\_ots\_init\_param](structbt__ots__init__param.md) {

753 /\* OTS features \*/

[ 754](structbt__ots__init__param.md#a563c25963aa84726630252eb5aca7cc6) struct [bt\_ots\_feat](structbt__ots__feat.md) [features](structbt__ots__init__param.md#a563c25963aa84726630252eb5aca7cc6);

755

756 /\* Callbacks \*/

[ 757](structbt__ots__init__param.md#a22887673f03decf840470cb555f2b7f0) struct [bt\_ots\_cb](structbt__ots__cb.md) \*[cb](structbt__ots__init__param.md#a22887673f03decf840470cb555f2b7f0);

758};

759

[ 772](group__bt__ots.md#gabf59844edd0ffd434acd94bad9a7b52c)int [bt\_ots\_obj\_add](group__bt__ots.md#gabf59844edd0ffd434acd94bad9a7b52c)(struct bt\_ots \*ots, const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \*param);

773

[ 786](group__bt__ots.md#ga872ba5a73fa4e617b9d48e7361af74c7)int [bt\_ots\_obj\_delete](group__bt__ots.md#ga872ba5a73fa4e617b9d48e7361af74c7)(struct bt\_ots \*ots, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

787

[ 797](group__bt__ots.md#gabe637ba9febb514f7346d71696b70c73)void \*[bt\_ots\_svc\_decl\_get](group__bt__ots.md#gabe637ba9febb514f7346d71696b70c73)(struct bt\_ots \*ots);

798

[ 806](group__bt__ots.md#ga1c9dcb35c8f07432fd9249a34e597819)int [bt\_ots\_init](group__bt__ots.md#ga1c9dcb35c8f07432fd9249a34e597819)(struct bt\_ots \*ots, struct [bt\_ots\_init\_param](structbt__ots__init__param.md) \*ots\_init);

807

[ 812](group__bt__ots.md#gafc71de8fd65212045fa26b2a81e3876d)struct bt\_ots \*[bt\_ots\_free\_instance\_get](group__bt__ots.md#gafc71de8fd65212045fa26b2a81e3876d)(void);

813

[ 814](group__bt__ots.md#ga4f18ea10855379414dd8a70b6c119d6b)#define BT\_OTS\_STOP 0

[ 815](group__bt__ots.md#ga8ccd0dec55069aa01bb9740a6520fd51)#define BT\_OTS\_CONTINUE 1

816

817/\* TODO: Merge server and client instance as opaque type \*/

[ 819](structbt__ots__client.md)struct [bt\_ots\_client](structbt__ots__client.md) {

[ 820](structbt__ots__client.md#a39818a4d776056212e82c4ba0626d0f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__ots__client.md#a39818a4d776056212e82c4ba0626d0f1);

[ 821](structbt__ots__client.md#a99727a6d064d79c3078a04b1d6d046db) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__ots__client.md#a99727a6d064d79c3078a04b1d6d046db);

[ 822](structbt__ots__client.md#a65608146d1a3e141635a015eb5092ab1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [feature\_handle](structbt__ots__client.md#a65608146d1a3e141635a015eb5092ab1);

[ 823](structbt__ots__client.md#ae902c29051540141852869dd94edf7e0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_name\_handle](structbt__ots__client.md#ae902c29051540141852869dd94edf7e0);

[ 824](structbt__ots__client.md#ae2eebd727fd908ef2b2074c9c0b2ab4f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_type\_handle](structbt__ots__client.md#ae2eebd727fd908ef2b2074c9c0b2ab4f);

[ 825](structbt__ots__client.md#a83c5d653692dc3d7dbcfd5c8e2361f96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_size\_handle](structbt__ots__client.md#a83c5d653692dc3d7dbcfd5c8e2361f96);

[ 826](structbt__ots__client.md#aabd4a625a341b4f7bdcdcff03e7ae76f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_properties\_handle](structbt__ots__client.md#aabd4a625a341b4f7bdcdcff03e7ae76f);

[ 827](structbt__ots__client.md#aff756cfa5f9431ed288563a95877cb53) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_created\_handle](structbt__ots__client.md#aff756cfa5f9431ed288563a95877cb53);

[ 828](structbt__ots__client.md#a83cf53f6f7737620ea39dccbebe26dd4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_modified\_handle](structbt__ots__client.md#a83cf53f6f7737620ea39dccbebe26dd4);

[ 829](structbt__ots__client.md#a6ff62fb7570269358888c9ab865a5ec6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_id\_handle](structbt__ots__client.md#a6ff62fb7570269358888c9ab865a5ec6);

[ 830](structbt__ots__client.md#ad56aaee2630d75a1bb5faf0f56486c0a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [oacp\_handle](structbt__ots__client.md#ad56aaee2630d75a1bb5faf0f56486c0a);

[ 831](structbt__ots__client.md#aa98ae5a468c46f1ffbfd08a6e82f420d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [olcp\_handle](structbt__ots__client.md#aa98ae5a468c46f1ffbfd08a6e82f420d);

832

[ 833](structbt__ots__client.md#a98a75a8ed52a2b97be1ea273a21b8775) struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) [oacp\_sub\_params](structbt__ots__client.md#a98a75a8ed52a2b97be1ea273a21b8775);

[ 834](structbt__ots__client.md#a8913d240d90b77ea72612ddbf816f528) struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) [oacp\_sub\_disc\_params](structbt__ots__client.md#a8913d240d90b77ea72612ddbf816f528);

[ 835](structbt__ots__client.md#a787b4851389e5da47a93969db6b3edcf) struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) [olcp\_sub\_params](structbt__ots__client.md#a787b4851389e5da47a93969db6b3edcf);

[ 836](structbt__ots__client.md#acbee05e7b1cd5c325a6982c6b32a732d) struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) [olcp\_sub\_disc\_params](structbt__ots__client.md#acbee05e7b1cd5c325a6982c6b32a732d);

837

[ 838](structbt__ots__client.md#a0e6a0d97a1b8edc7a282aec12d95b0dc) struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) [write\_params](structbt__ots__client.md#a0e6a0d97a1b8edc7a282aec12d95b0dc);

[ 839](structbt__ots__client.md#a87d273e283941a3b9f1402e2b514134b) struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) [read\_proc](structbt__ots__client.md#a87d273e283941a3b9f1402e2b514134b);

[ 840](structbt__ots__client.md#a3aded7f58deb7f13c1c5adaa073f45f8) struct [bt\_ots\_client\_cb](structbt__ots__client__cb.md) \*[cb](structbt__ots__client.md#a3aded7f58deb7f13c1c5adaa073f45f8);

841

[ 842](structbt__ots__client.md#a8a6d138d506a5e2732f4c51971533ce9) struct [bt\_ots\_feat](structbt__ots__feat.md) [features](structbt__ots__client.md#a8a6d138d506a5e2732f4c51971533ce9);

843

[ 844](structbt__ots__client.md#ac0fac55db40bf66aff358ce906fc8172) struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) [cur\_object](structbt__ots__client.md#ac0fac55db40bf66aff358ce906fc8172);

845};

846

[ 848](structbt__ots__client__cb.md)struct [bt\_ots\_client\_cb](structbt__ots__client__cb.md) {

[ 860](structbt__ots__client__cb.md#ace98d27220e394b0990a8274bbd43026) void (\*[obj\_selected](structbt__ots__client__cb.md#ace98d27220e394b0990a8274bbd43026))(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst,

861 struct bt\_conn \*conn, int err);

862

863

[ 880](structbt__ots__client__cb.md#ae95f3b85758c04279ada801c001086bc) int (\*[obj\_data\_read](structbt__ots__client__cb.md#ae95f3b85758c04279ada801c001086bc))(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst,

881 struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset,

882 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_p, bool is\_complete);

883

[ 897](structbt__ots__client__cb.md#ab6c03b98fc5c68aa8c76ada23b7dff1c) void (\*[obj\_metadata\_read](structbt__ots__client__cb.md#ab6c03b98fc5c68aa8c76ada23b7dff1c))(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst,

898 struct bt\_conn \*conn, int err,

899 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata\_read);

900

[ 910](structbt__ots__client__cb.md#a2baaf13c8de4ade034f2b58896225e0d) void (\*[obj\_data\_written](structbt__ots__client__cb.md#a2baaf13c8de4ade034f2b58896225e0d))(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst,

911 struct bt\_conn \*conn, size\_t len);

912

[ 924](structbt__ots__client__cb.md#ad5537da9ced98a15620a7fb1e77b0218) void (\*[obj\_checksum\_calculated](structbt__ots__client__cb.md#ad5537da9ced98a15620a7fb1e77b0218))(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst, struct bt\_conn \*conn,

925 int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) checksum);

926};

927

[ 938](group__bt__ots.md#gadefd2ccb46a686a4aa2999da5851184b)int [bt\_ots\_client\_register](group__bt__ots.md#gadefd2ccb46a686a4aa2999da5851184b)(struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst);

939

[ 949](group__bt__ots.md#gabba031c38c7503c1f434a761d9f65df4)int [bt\_ots\_client\_unregister](group__bt__ots.md#gabba031c38c7503c1f434a761d9f65df4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

950

[ 962](group__bt__ots.md#gac270137f15596777287f68b3d6a6a11c)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_ots\_client\_indicate\_handler](group__bt__ots.md#gac270137f15596777287f68b3d6a6a11c)(struct bt\_conn \*conn,

963 struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params,

964 const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

965

[ 973](group__bt__ots.md#gaf11589afc37efe18dcac122835a4c95d)int [bt\_ots\_client\_read\_feature](group__bt__ots.md#gaf11589afc37efe18dcac122835a4c95d)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

974 struct bt\_conn \*conn);

975

[ 984](group__bt__ots.md#ga5f2d0b0e4d54e00a1a96157fcfaf172b)int [bt\_ots\_client\_select\_id](group__bt__ots.md#ga5f2d0b0e4d54e00a1a96157fcfaf172b)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

985 struct bt\_conn \*conn,

986 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id);

987

[ 995](group__bt__ots.md#ga70cae251cf40a5c3c8d2a8c7e1f1e181)int [bt\_ots\_client\_select\_first](group__bt__ots.md#ga70cae251cf40a5c3c8d2a8c7e1f1e181)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

996 struct bt\_conn \*conn);

997

[ 1005](group__bt__ots.md#ga89fc03d68725de0b5f306c899452b1a8)int [bt\_ots\_client\_select\_last](group__bt__ots.md#ga89fc03d68725de0b5f306c899452b1a8)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

1006 struct bt\_conn \*conn);

1007

[ 1015](group__bt__ots.md#ga81997ab2f1718c6856e676eb9b3f72bb)int [bt\_ots\_client\_select\_next](group__bt__ots.md#ga81997ab2f1718c6856e676eb9b3f72bb)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

1016 struct bt\_conn \*conn);

1017

[ 1025](group__bt__ots.md#gac84ed7f16fa86d87531d04e2957568f9)int [bt\_ots\_client\_select\_prev](group__bt__ots.md#gac84ed7f16fa86d87531d04e2957568f9)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

1026 struct bt\_conn \*conn);

1027

[ 1039](group__bt__ots.md#ga936f392c880c9d1a73f2bd632e5b63e0)int [bt\_ots\_client\_read\_object\_metadata](group__bt__ots.md#ga936f392c880c9d1a73f2bd632e5b63e0)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

1040 struct bt\_conn \*conn,

1041 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata);

1042

[ 1055](group__bt__ots.md#ga8ad1c53325c1b77271307507317a5965)int [bt\_ots\_client\_read\_object\_data](group__bt__ots.md#ga8ad1c53325c1b77271307507317a5965)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst,

1056 struct bt\_conn \*conn);

1057

[ 1074](group__bt__ots.md#ga9444b064c616718dae1577b21540fb9a)int [bt\_ots\_client\_write\_object\_data](group__bt__ots.md#ga9444b064c616718dae1577b21540fb9a)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn,

1075 const void \*buf, size\_t len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

1076 enum [bt\_ots\_oacp\_write\_op\_mode](group__bt__ots.md#gaebdd2b8a80948d1050d42fa3963cc863) mode);

1077

[ 1093](group__bt__ots.md#ga9cfd057d39ce3fe9bbecaa103ec44f77)int [bt\_ots\_client\_get\_object\_checksum](group__bt__ots.md#ga9cfd057d39ce3fe9bbecaa103ec44f77)(struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn,

1094 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t len);

1095

[ 1106](group__bt__ots.md#gaa1a9db6e8aa6ee716e4fdd2e34157f46)typedef int (\*[bt\_ots\_client\_dirlisting\_cb](group__bt__ots.md#gaa1a9db6e8aa6ee716e4fdd2e34157f46))(struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*meta);

1107

[ 1117](group__bt__ots.md#gabe485816a2e536758a7ce85c593ea486)int [bt\_ots\_client\_decode\_dirlisting](group__bt__ots.md#gabe485816a2e536758a7ce85c593ea486)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

1118 [bt\_ots\_client\_dirlisting\_cb](group__bt__ots.md#gaa1a9db6e8aa6ee716e4fdd2e34157f46) cb);

1119

[ 1131](group__bt__ots.md#gac9be2770fc7f2932ea2e31392d956f0a)static inline int [bt\_ots\_obj\_id\_to\_str](group__bt__ots.md#gac9be2770fc7f2932ea2e31392d956f0a)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id, char \*str, size\_t len)

1132{

1133 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id[6];

1134

1135 [sys\_put\_le48](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)(obj\_id, id);

1136

1137 return [snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)(str, len, "0x%02X%02X%02X%02X%02X%02X",

1138 id[5], id[4], id[3], id[2], id[1], id[0]);

1139}

1140

[ 1146](group__bt__ots.md#ga8324cc14e8812648cc3663144591af89)void [bt\_ots\_metadata\_display](group__bt__ots.md#ga8324cc14e8812648cc3663144591af89)(struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*metadata,

1147 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) count);

1148

1160#if defined(CONFIG\_BT\_OTS\_OACP\_CHECKSUM\_SUPPORT)

1161static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_ots\_client\_calc\_checksum(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len)

1162{

1163 return [crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)(data, len);

1164}

1165#endif

1166

1167#ifdef \_\_cplusplus

1168}

1169#endif

1170

1174

1175#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_OTS\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[crc.h](crc_8h.md)

CRC computation function.

[gatt.h](gatt_8h.md)

Generic Attribute Profile handling.

[bt\_ots\_init](group__bt__ots.md#ga1c9dcb35c8f07432fd9249a34e597819)

int bt\_ots\_init(struct bt\_ots \*ots, struct bt\_ots\_init\_param \*ots\_init)

Initialize the OTS instance.

[bt\_ots\_client\_select\_id](group__bt__ots.md#ga5f2d0b0e4d54e00a1a96157fcfaf172b)

int bt\_ots\_client\_select\_id(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn, uint64\_t obj\_id)

Select an object by its Object ID.

[bt\_ots\_client\_select\_first](group__bt__ots.md#ga70cae251cf40a5c3c8d2a8c7e1f1e181)

int bt\_ots\_client\_select\_first(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn)

Select the first object.

[bt\_ots\_client\_select\_next](group__bt__ots.md#ga81997ab2f1718c6856e676eb9b3f72bb)

int bt\_ots\_client\_select\_next(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn)

Select the next object.

[bt\_ots\_metadata\_display](group__bt__ots.md#ga8324cc14e8812648cc3663144591af89)

void bt\_ots\_metadata\_display(struct bt\_ots\_obj\_metadata \*metadata, uint16\_t count)

Displays one or more object metadata as text with LOG\_INF.

[bt\_ots\_obj\_delete](group__bt__ots.md#ga872ba5a73fa4e617b9d48e7361af74c7)

int bt\_ots\_obj\_delete(struct bt\_ots \*ots, uint64\_t id)

Delete an object from the OTS instance.

[bt\_ots\_client\_select\_last](group__bt__ots.md#ga89fc03d68725de0b5f306c899452b1a8)

int bt\_ots\_client\_select\_last(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn)

Select the last object.

[bt\_ots\_client\_read\_object\_data](group__bt__ots.md#ga8ad1c53325c1b77271307507317a5965)

int bt\_ots\_client\_read\_object\_data(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn)

Read the data of the current selected object.

[bt\_ots\_client\_read\_object\_metadata](group__bt__ots.md#ga936f392c880c9d1a73f2bd632e5b63e0)

int bt\_ots\_client\_read\_object\_metadata(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn, uint8\_t metadata)

Read the metadata of the current object.

[bt\_ots\_client\_write\_object\_data](group__bt__ots.md#ga9444b064c616718dae1577b21540fb9a)

int bt\_ots\_client\_write\_object\_data(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn, const void \*buf, size\_t len, off\_t offset, enum bt\_ots\_oacp\_write\_op\_mode mode)

Write the data of the current selected object.

[bt\_ots\_client\_get\_object\_checksum](group__bt__ots.md#ga9cfd057d39ce3fe9bbecaa103ec44f77)

int bt\_ots\_client\_get\_object\_checksum(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn, off\_t offset, size\_t len)

Get the checksum of the current selected object.

[bt\_ots\_client\_dirlisting\_cb](group__bt__ots.md#gaa1a9db6e8aa6ee716e4fdd2e34157f46)

int(\* bt\_ots\_client\_dirlisting\_cb)(struct bt\_ots\_obj\_metadata \*meta)

Directory listing object metadata callback.

**Definition** ots.h:1106

[bt\_ots\_client\_unregister](group__bt__ots.md#gabba031c38c7503c1f434a761d9f65df4)

int bt\_ots\_client\_unregister(uint8\_t index)

Unregister an Object Transfer Service Instance.

[bt\_ots\_client\_decode\_dirlisting](group__bt__ots.md#gabe485816a2e536758a7ce85c593ea486)

int bt\_ots\_client\_decode\_dirlisting(uint8\_t \*data, uint16\_t length, bt\_ots\_client\_dirlisting\_cb cb)

Decode Directory Listing object into object metadata.

[bt\_ots\_svc\_decl\_get](group__bt__ots.md#gabe637ba9febb514f7346d71696b70c73)

void \* bt\_ots\_svc\_decl\_get(struct bt\_ots \*ots)

Get the service declaration attribute.

[bt\_ots\_obj\_add](group__bt__ots.md#gabf59844edd0ffd434acd94bad9a7b52c)

int bt\_ots\_obj\_add(struct bt\_ots \*ots, const struct bt\_ots\_obj\_add\_param \*param)

Add an object to the OTS instance.

[bt\_ots\_client\_indicate\_handler](group__bt__ots.md#gac270137f15596777287f68b3d6a6a11c)

uint8\_t bt\_ots\_client\_indicate\_handler(struct bt\_conn \*conn, struct bt\_gatt\_subscribe\_params \*params, const void \*data, uint16\_t length)

OTS Indicate Handler function.

[bt\_ots\_client\_select\_prev](group__bt__ots.md#gac84ed7f16fa86d87531d04e2957568f9)

int bt\_ots\_client\_select\_prev(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn)

Select the previous object.

[bt\_ots\_obj\_id\_to\_str](group__bt__ots.md#gac9be2770fc7f2932ea2e31392d956f0a)

static int bt\_ots\_obj\_id\_to\_str(uint64\_t obj\_id, char \*str, size\_t len)

Converts binary OTS Object ID to string.

**Definition** ots.h:1131

[bt\_ots\_client\_register](group__bt__ots.md#gadefd2ccb46a686a4aa2999da5851184b)

int bt\_ots\_client\_register(struct bt\_ots\_client \*ots\_inst)

Register an Object Transfer Service Instance.

[bt\_ots\_oacp\_write\_op\_mode](group__bt__ots.md#gaebdd2b8a80948d1050d42fa3963cc863)

bt\_ots\_oacp\_write\_op\_mode

**Definition** ots.h:260

[bt\_ots\_client\_read\_feature](group__bt__ots.md#gaf11589afc37efe18dcac122835a4c95d)

int bt\_ots\_client\_read\_feature(struct bt\_ots\_client \*otc\_inst, struct bt\_conn \*conn)

Read the OTS feature characteristic.

[bt\_ots\_free\_instance\_get](group__bt__ots.md#gafc71de8fd65212045fa26b2a81e3876d)

struct bt\_ots \* bt\_ots\_free\_instance\_get(void)

Get a free instance of OTS from the pool.

[BT\_OTS\_OACP\_FEAT\_ABORT](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440)

@ BT\_OTS\_OACP\_FEAT\_ABORT

Bit 9 OACP Abort Op Code Supported.

**Definition** ots.h:253

[BT\_OTS\_OACP\_FEAT\_DELETE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee)

@ BT\_OTS\_OACP\_FEAT\_DELETE

Bit 1 OACP Delete Op Code Supported.

**Definition** ots.h:229

[BT\_OTS\_OACP\_FEAT\_APPEND](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b)

@ BT\_OTS\_OACP\_FEAT\_APPEND

Bit 6 Appending Additional Data to Objects Supported.

**Definition** ots.h:244

[BT\_OTS\_OACP\_FEAT\_READ](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465)

@ BT\_OTS\_OACP\_FEAT\_READ

Bit 4 OACP Read Op Code Supported.

**Definition** ots.h:238

[BT\_OTS\_OACP\_FEAT\_TRUNCATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225)

@ BT\_OTS\_OACP\_FEAT\_TRUNCATE

Bit 7 Truncation of Objects Supported.

**Definition** ots.h:247

[BT\_OTS\_OACP\_FEAT\_CHECKSUM](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f)

@ BT\_OTS\_OACP\_FEAT\_CHECKSUM

Bit 2 OACP Calculate Checksum Op Code Supported.

**Definition** ots.h:232

[BT\_OTS\_OACP\_FEAT\_WRITE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab)

@ BT\_OTS\_OACP\_FEAT\_WRITE

Bit 5 OACP Write Op Code Supported.

**Definition** ots.h:241

[BT\_OTS\_OACP\_FEAT\_EXECUTE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c)

@ BT\_OTS\_OACP\_FEAT\_EXECUTE

Bit 3 OACP Execute Op Code Supported.

**Definition** ots.h:235

[BT\_OTS\_OACP\_FEAT\_PATCH](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf)

@ BT\_OTS\_OACP\_FEAT\_PATCH

Bit 8 Patching of Objects Supported.

**Definition** ots.h:250

[BT\_OTS\_OACP\_FEAT\_CREATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9)

@ BT\_OTS\_OACP\_FEAT\_CREATE

Bit 0 OACP Create Op Code Supported.

**Definition** ots.h:226

[BT\_OTS\_OLCP\_FEAT\_ORDER](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d)

@ BT\_OTS\_OLCP\_FEAT\_ORDER

Bit 1 OLCP Order Op Code Supported.

**Definition** ots.h:411

[BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660)

@ BT\_OTS\_OLCP\_FEAT\_NUM\_REQ

Bit 2 OLCP Request Number of Objects Op Code Supported.

**Definition** ots.h:414

[BT\_OTS\_OLCP\_FEAT\_CLEAR](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af)

@ BT\_OTS\_OLCP\_FEAT\_CLEAR

Bit 3 OLCP Clear Marking Op Code Supported.

**Definition** ots.h:417

[BT\_OTS\_OLCP\_FEAT\_GO\_TO](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713)

@ BT\_OTS\_OLCP\_FEAT\_GO\_TO

Bit 0 OLCP Go To Op Code Supported.

**Definition** ots.h:408

[BT\_OTS\_METADATA\_REQ\_ALL](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf)

@ BT\_OTS\_METADATA\_REQ\_ALL

Request all object metadata.

**Definition** ots.h:502

[BT\_OTS\_METADATA\_REQ\_MODIFIED](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e)

@ BT\_OTS\_METADATA\_REQ\_MODIFIED

Request object last modified time.

**Definition** ots.h:496

[BT\_OTS\_METADATA\_REQ\_ID](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2)

@ BT\_OTS\_METADATA\_REQ\_ID

Request object ID.

**Definition** ots.h:498

[BT\_OTS\_METADATA\_REQ\_CREATED](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095)

@ BT\_OTS\_METADATA\_REQ\_CREATED

Request object first created time.

**Definition** ots.h:494

[BT\_OTS\_METADATA\_REQ\_SIZE](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5)

@ BT\_OTS\_METADATA\_REQ\_SIZE

Request object size.

**Definition** ots.h:492

[BT\_OTS\_METADATA\_REQ\_NAME](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb)

@ BT\_OTS\_METADATA\_REQ\_NAME

Request object name.

**Definition** ots.h:488

[BT\_OTS\_METADATA\_REQ\_PROPS](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f)

@ BT\_OTS\_METADATA\_REQ\_PROPS

Request object properties.

**Definition** ots.h:500

[BT\_OTS\_METADATA\_REQ\_TYPE](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9)

@ BT\_OTS\_METADATA\_REQ\_TYPE

Request object type.

**Definition** ots.h:490

[BT\_OTS\_OBJ\_PROP\_MARKED](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3)

@ BT\_OTS\_OBJ\_PROP\_MARKED

Bit 7 This object is a marked object.

**Definition** ots.h:99

[BT\_OTS\_OBJ\_PROP\_DELETE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10)

@ BT\_OTS\_OBJ\_PROP\_DELETE

Bit 0 Deletion of this object is permitted.

**Definition** ots.h:71

[BT\_OTS\_OBJ\_PROP\_TRUNCATE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446)

@ BT\_OTS\_OBJ\_PROP\_TRUNCATE

Bit 5 Truncation of this object is permitted.

**Definition** ots.h:89

[BT\_OTS\_OBJ\_PROP\_APPEND](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775)

@ BT\_OTS\_OBJ\_PROP\_APPEND

Bit 4 Appending data to this object is permitted.

**Definition** ots.h:86

[BT\_OTS\_OBJ\_PROP\_READ](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102)

@ BT\_OTS\_OBJ\_PROP\_READ

Bit 2 Reading this object is permitted.

**Definition** ots.h:77

[BT\_OTS\_OBJ\_PROP\_EXECUTE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad)

@ BT\_OTS\_OBJ\_PROP\_EXECUTE

Bit 1 Execution of this object is permitted.

**Definition** ots.h:74

[BT\_OTS\_OBJ\_PROP\_PATCH](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed)

@ BT\_OTS\_OBJ\_PROP\_PATCH

Bit 6 Patching this object is permitted.

**Definition** ots.h:96

[BT\_OTS\_OBJ\_PROP\_WRITE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2)

@ BT\_OTS\_OBJ\_PROP\_WRITE

Bit 3 Writing data to this object is permitted.

**Definition** ots.h:80

[BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab)

@ BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE

**Definition** ots.h:261

[BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a)

@ BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE

**Definition** ots.h:262

[crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)

uint32\_t crc32\_ieee(const uint8\_t \*data, size\_t len)

Generate IEEE conform CRC32 checksum.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[snprintk](printk_8h.md#a0b0af71688f7e9170103d771d4e1eab2)

int snprintk(char \*str, size\_t size, const char \*fmt,...)

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_gatt\_discover\_params](structbt__gatt__discover__params.md)

GATT Discover Attributes parameters.

**Definition** gatt.h:1786

[bt\_gatt\_read\_params](structbt__gatt__read__params.md)

GATT Read parameters.

**Definition** gatt.h:1876

[bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md)

GATT Subscribe parameters.

**Definition** gatt.h:2157

[bt\_gatt\_write\_params](structbt__gatt__write__params.md)

GATT Write parameters.

**Definition** gatt.h:1979

[bt\_ots\_cb](structbt__ots__cb.md)

OTS callback structure.

**Definition** ots.h:601

[bt\_ots\_cb::obj\_created](structbt__ots__cb.md#a0c95b2bc382474be3c1ae849936a8206)

int(\* obj\_created)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, const struct bt\_ots\_obj\_add\_param \*add\_param, struct bt\_ots\_obj\_created\_desc \*created\_desc)

Object created callback.

**Definition** ots.h:624

[bt\_ots\_cb::obj\_cal\_checksum](structbt__ots__cb.md#a2ef2245c017015b81c0f276f00fd6f79)

int(\* obj\_cal\_checksum)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, off\_t offset, size\_t len, void \*\*data)

Object Calculate checksum callback.

**Definition** ots.h:747

[bt\_ots\_cb::obj\_deleted](structbt__ots__cb.md#a2fd78b43691e83c1faa86c1748ab2359)

int(\* obj\_deleted)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id)

Object deleted callback.

**Definition** ots.h:649

[bt\_ots\_cb::obj\_name\_written](structbt__ots__cb.md#a600fa13a97f39e3bd53c524039e2733c)

void(\* obj\_name\_written)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, const char \*cur\_name, const char \*new\_name)

Object name written callback.

**Definition** ots.h:729

[bt\_ots\_cb::obj\_read](structbt__ots__cb.md#ab67ca0032b8b2fd9b8fbe6c117c186dd)

ssize\_t(\* obj\_read)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, void \*\*data, size\_t len, off\_t offset)

Object read callback.

**Definition** ots.h:683

[bt\_ots\_cb::obj\_write](structbt__ots__cb.md#ae31da190c9c6bee086e4d7f8fcd6fbb5)

ssize\_t(\* obj\_write)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id, const void \*data, size\_t len, off\_t offset, size\_t rem)

Object write callback.

**Definition** ots.h:713

[bt\_ots\_cb::obj\_selected](structbt__ots__cb.md#ae8602aef0fd001d6768dc20c8873742d)

void(\* obj\_selected)(struct bt\_ots \*ots, struct bt\_conn \*conn, uint64\_t id)

Object selected callback.

**Definition** ots.h:660

[bt\_ots\_client\_cb](structbt__ots__client__cb.md)

OTS client callback structure.

**Definition** ots.h:848

[bt\_ots\_client\_cb::obj\_data\_written](structbt__ots__client__cb.md#a2baaf13c8de4ade034f2b58896225e0d)

void(\* obj\_data\_written)(struct bt\_ots\_client \*ots\_inst, struct bt\_conn \*conn, size\_t len)

Callback function for the data of the write object.

**Definition** ots.h:910

[bt\_ots\_client\_cb::obj\_metadata\_read](structbt__ots__client__cb.md#ab6c03b98fc5c68aa8c76ada23b7dff1c)

void(\* obj\_metadata\_read)(struct bt\_ots\_client \*ots\_inst, struct bt\_conn \*conn, int err, uint8\_t metadata\_read)

Callback function for metadata of the selected object.

**Definition** ots.h:897

[bt\_ots\_client\_cb::obj\_selected](structbt__ots__client__cb.md#ace98d27220e394b0990a8274bbd43026)

void(\* obj\_selected)(struct bt\_ots\_client \*ots\_inst, struct bt\_conn \*conn, int err)

Callback function when a new object is selected.

**Definition** ots.h:860

[bt\_ots\_client\_cb::obj\_checksum\_calculated](structbt__ots__client__cb.md#ad5537da9ced98a15620a7fb1e77b0218)

void(\* obj\_checksum\_calculated)(struct bt\_ots\_client \*ots\_inst, struct bt\_conn \*conn, int err, uint32\_t checksum)

Callback function when checksum indication is received.

**Definition** ots.h:924

[bt\_ots\_client\_cb::obj\_data\_read](structbt__ots__client__cb.md#ae95f3b85758c04279ada801c001086bc)

int(\* obj\_data\_read)(struct bt\_ots\_client \*ots\_inst, struct bt\_conn \*conn, uint32\_t offset, uint32\_t len, uint8\_t \*data\_p, bool is\_complete)

Callback function for the data of the selected object.

**Definition** ots.h:880

[bt\_ots\_client](structbt__ots__client.md)

OTS client instance.

**Definition** ots.h:819

[bt\_ots\_client::write\_params](structbt__ots__client.md#a0e6a0d97a1b8edc7a282aec12d95b0dc)

struct bt\_gatt\_write\_params write\_params

**Definition** ots.h:838

[bt\_ots\_client::start\_handle](structbt__ots__client.md#a39818a4d776056212e82c4ba0626d0f1)

uint16\_t start\_handle

**Definition** ots.h:820

[bt\_ots\_client::cb](structbt__ots__client.md#a3aded7f58deb7f13c1c5adaa073f45f8)

struct bt\_ots\_client\_cb \* cb

**Definition** ots.h:840

[bt\_ots\_client::feature\_handle](structbt__ots__client.md#a65608146d1a3e141635a015eb5092ab1)

uint16\_t feature\_handle

**Definition** ots.h:822

[bt\_ots\_client::obj\_id\_handle](structbt__ots__client.md#a6ff62fb7570269358888c9ab865a5ec6)

uint16\_t obj\_id\_handle

**Definition** ots.h:829

[bt\_ots\_client::olcp\_sub\_params](structbt__ots__client.md#a787b4851389e5da47a93969db6b3edcf)

struct bt\_gatt\_subscribe\_params olcp\_sub\_params

**Definition** ots.h:835

[bt\_ots\_client::obj\_size\_handle](structbt__ots__client.md#a83c5d653692dc3d7dbcfd5c8e2361f96)

uint16\_t obj\_size\_handle

**Definition** ots.h:825

[bt\_ots\_client::obj\_modified\_handle](structbt__ots__client.md#a83cf53f6f7737620ea39dccbebe26dd4)

uint16\_t obj\_modified\_handle

**Definition** ots.h:828

[bt\_ots\_client::read\_proc](structbt__ots__client.md#a87d273e283941a3b9f1402e2b514134b)

struct bt\_gatt\_read\_params read\_proc

**Definition** ots.h:839

[bt\_ots\_client::oacp\_sub\_disc\_params](structbt__ots__client.md#a8913d240d90b77ea72612ddbf816f528)

struct bt\_gatt\_discover\_params oacp\_sub\_disc\_params

**Definition** ots.h:834

[bt\_ots\_client::features](structbt__ots__client.md#a8a6d138d506a5e2732f4c51971533ce9)

struct bt\_ots\_feat features

**Definition** ots.h:842

[bt\_ots\_client::oacp\_sub\_params](structbt__ots__client.md#a98a75a8ed52a2b97be1ea273a21b8775)

struct bt\_gatt\_subscribe\_params oacp\_sub\_params

**Definition** ots.h:833

[bt\_ots\_client::end\_handle](structbt__ots__client.md#a99727a6d064d79c3078a04b1d6d046db)

uint16\_t end\_handle

**Definition** ots.h:821

[bt\_ots\_client::olcp\_handle](structbt__ots__client.md#aa98ae5a468c46f1ffbfd08a6e82f420d)

uint16\_t olcp\_handle

**Definition** ots.h:831

[bt\_ots\_client::obj\_properties\_handle](structbt__ots__client.md#aabd4a625a341b4f7bdcdcff03e7ae76f)

uint16\_t obj\_properties\_handle

**Definition** ots.h:826

[bt\_ots\_client::cur\_object](structbt__ots__client.md#ac0fac55db40bf66aff358ce906fc8172)

struct bt\_ots\_obj\_metadata cur\_object

**Definition** ots.h:844

[bt\_ots\_client::olcp\_sub\_disc\_params](structbt__ots__client.md#acbee05e7b1cd5c325a6982c6b32a732d)

struct bt\_gatt\_discover\_params olcp\_sub\_disc\_params

**Definition** ots.h:836

[bt\_ots\_client::oacp\_handle](structbt__ots__client.md#ad56aaee2630d75a1bb5faf0f56486c0a)

uint16\_t oacp\_handle

**Definition** ots.h:830

[bt\_ots\_client::obj\_type\_handle](structbt__ots__client.md#ae2eebd727fd908ef2b2074c9c0b2ab4f)

uint16\_t obj\_type\_handle

**Definition** ots.h:824

[bt\_ots\_client::obj\_name\_handle](structbt__ots__client.md#ae902c29051540141852869dd94edf7e0)

uint16\_t obj\_name\_handle

**Definition** ots.h:823

[bt\_ots\_client::obj\_created\_handle](structbt__ots__client.md#aff756cfa5f9431ed288563a95877cb53)

uint16\_t obj\_created\_handle

**Definition** ots.h:827

[bt\_ots\_date\_time](structbt__ots__date__time.md)

Date and Time structure.

**Definition** ots.h:506

[bt\_ots\_date\_time::day](structbt__ots__date__time.md#a09ca928752dc844e89de3957d1baae3c)

uint8\_t day

**Definition** ots.h:509

[bt\_ots\_date\_time::seconds](structbt__ots__date__time.md#a4eb6899dbce61478b97025958c62f586)

uint8\_t seconds

**Definition** ots.h:512

[bt\_ots\_date\_time::month](structbt__ots__date__time.md#ac3959eac8188df6114d70aed1ccbf3f4)

uint8\_t month

**Definition** ots.h:508

[bt\_ots\_date\_time::minutes](structbt__ots__date__time.md#acc118b311bfdcb3c2f7801121831fcd6)

uint8\_t minutes

**Definition** ots.h:511

[bt\_ots\_date\_time::hours](structbt__ots__date__time.md#ae139a310b4d17078f52bfbe7707e185a)

uint8\_t hours

**Definition** ots.h:510

[bt\_ots\_date\_time::year](structbt__ots__date__time.md#af348ad2613ba309de6a93d357bcce3bc)

uint16\_t year

**Definition** ots.h:507

[bt\_ots\_feat](structbt__ots__feat.md)

Features of the OTS.

**Definition** ots.h:477

[bt\_ots\_feat::olcp](structbt__ots__feat.md#a309b3e38a0f15c49c06a5ffeb873cef3)

uint32\_t olcp

**Definition** ots.h:482

[bt\_ots\_feat::oacp](structbt__ots__feat.md#a714abba341b1f4a50edfa73dd5048f28)

uint32\_t oacp

**Definition** ots.h:479

[bt\_ots\_init\_param](structbt__ots__init__param.md)

Descriptor for OTS initialization.

**Definition** ots.h:752

[bt\_ots\_init\_param::cb](structbt__ots__init__param.md#a22887673f03decf840470cb555f2b7f0)

struct bt\_ots\_cb \* cb

**Definition** ots.h:757

[bt\_ots\_init\_param::features](structbt__ots__init__param.md#a563c25963aa84726630252eb5aca7cc6)

struct bt\_ots\_feat features

**Definition** ots.h:754

[bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md)

Descriptor for OTS object addition.

**Definition** ots.h:559

[bt\_ots\_obj\_add\_param::size](structbt__ots__obj__add__param.md#a721734439b43e40324c3a548b5a4eb34)

uint32\_t size

Object size to allocate.

**Definition** ots.h:561

[bt\_ots\_obj\_add\_param::type](structbt__ots__obj__add__param.md#afdbaf218850d4bf3f40f7a9e8d7b0595)

struct bt\_ots\_obj\_type type

Object type.

**Definition** ots.h:564

[bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md)

Descriptor for OTS created object.

**Definition** ots.h:573

[bt\_ots\_obj\_created\_desc::props](structbt__ots__obj__created__desc.md#a50b2b2ae0b87690d1995187bae577e8c)

uint32\_t props

Object properties.

**Definition** ots.h:597

[bt\_ots\_obj\_created\_desc::size](structbt__ots__obj__created__desc.md#adb52cffa29c08ee1131415faeaf13cda)

struct bt\_ots\_obj\_size size

Object size.

**Definition** ots.h:594

[bt\_ots\_obj\_created\_desc::name](structbt__ots__obj__created__desc.md#af69db0a3c56c6d3085f20fbb405b436e)

char \* name

Object name.

**Definition** ots.h:583

[bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md)

Metadata of an OTS object.

**Definition** ots.h:521

[bt\_ots\_obj\_metadata::props](structbt__ots__obj__metadata.md#aa4ffe00ede40ff23ab5788c82ec2ac38)

uint32\_t props

Object Properties.

**Definition** ots.h:552

[bt\_ots\_obj\_metadata::type](structbt__ots__obj__metadata.md#aee93aef1932e9c8b4cb0c8055e5cb055)

struct bt\_ots\_obj\_type type

Object Type.

**Definition** ots.h:535

[bt\_ots\_obj\_metadata::size](structbt__ots__obj__metadata.md#afd451a3b531250db1d45eb6ddb4d9b0f)

struct bt\_ots\_obj\_size size

Object Size.

**Definition** ots.h:538

[bt\_ots\_obj\_size](structbt__ots__obj__size.md)

Descriptor for OTS Object Size parameter.

**Definition** ots.h:215

[bt\_ots\_obj\_size::cur](structbt__ots__obj__size.md#a217290f0fae68a54046eef50ac2a3773)

uint32\_t cur

Current Size.

**Definition** ots.h:217

[bt\_ots\_obj\_size::alloc](structbt__ots__obj__size.md#a86a5675532eae69d40b3305436e81cfb)

uint32\_t alloc

Allocated Size.

**Definition** ots.h:220

[bt\_ots\_obj\_type](structbt__ots__obj__type.md)

Type of an OTS object.

**Definition** ots.h:55

[bt\_ots\_obj\_type::uuid](structbt__ots__obj__type.md#a89a8dbe566579422df503dd577ea8d42)

struct bt\_uuid uuid

**Definition** ots.h:58

[bt\_ots\_obj\_type::uuid\_16](structbt__ots__obj__type.md#ae39b7a368314d1a771cf3573d2077095)

struct bt\_uuid\_16 uuid\_16

**Definition** ots.h:61

[bt\_ots\_obj\_type::uuid\_128](structbt__ots__obj__type.md#aedf0e5d45f6f4912a8eeae077eda17be)

struct bt\_uuid\_128 uuid\_128

**Definition** ots.h:64

[bt\_uuid\_128](structbt__uuid__128.md)

**Definition** uuid.h:67

[bt\_uuid\_16](structbt__uuid__16.md)

**Definition** uuid.h:53

[bt\_uuid](structbt__uuid.md)

This is a 'tentative' type and should be used as a pointer only.

**Definition** uuid.h:49

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[sys\_put\_le48](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)

static void sys\_put\_le48(uint64\_t val, uint8\_t dst[6])

Put a 48-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:472

[util.h](sys_2util_8h.md)

Misc utilities.

[uuid.h](uuid_8h.md)

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [ots.h](ots_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
