---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/i3c_8h_source.html
original_path: doxygen/html/i3c_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c.h

[Go to the documentation of this file.](i3c_8h.md)

1/\*

2 \* Copyright 2022 Intel Corporation

3 \* Copyright 2023 Meta Platforms, Inc. and its affiliates

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_H\_

10

19

20#include <[errno.h](errno_8h.md)>

21#include <[stdint.h](stdint_8h.md)>

22#include <stddef.h>

23

24#include <[zephyr/device.h](device_8h.md)>

25#include <[zephyr/drivers/i3c/addresses.h](addresses_8h.md)>

26#include <[zephyr/drivers/i3c/error\_types.h](error__types_8h.md)>

27#include <[zephyr/drivers/i3c/ccc.h](ccc_8h.md)>

28#include <[zephyr/drivers/i3c/devicetree.h](drivers_2i3c_2devicetree_8h.md)>

29#include <[zephyr/drivers/i3c/ibi.h](ibi_8h.md)>

30#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

31#include <[zephyr/sys/slist.h](slist_8h.md)>

32#include <[zephyr/sys/util.h](sys_2util_8h.md)>

33#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

79

[ 86](group__i3c__interface.md#ga91ebe41a421dc05ae7f1de1ce2dd314f)#define I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT BIT(0)

87

[ 89](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)#define I3C\_BCR\_IBI\_REQUEST\_CAPABLE BIT(1)

90

[ 98](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)#define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE BIT(2)

99

[ 106](group__i3c__interface.md#ga7b9fea89457022d8012ac25133bf63db)#define I3C\_BCR\_OFFLINE\_CAPABLE BIT(3)

107

[ 114](group__i3c__interface.md#ga69dc4a5004da568684a3c72046bba870)#define I3C\_BCR\_VIRTUAL\_TARGET BIT(4)

115

[ 123](group__i3c__interface.md#ga07018705794753d0d0d65131f011e097)#define I3C\_BCR\_ADV\_CAPABILITIES BIT(5)

124

[ 126](group__i3c__interface.md#ga867b4b12b23c803b86b57dcc86b9e604)#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET 0U

127

[ 129](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852)#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE 1U

130

[ 132](group__i3c__interface.md#ga25721c9963040c84b7f5bbb48bb87b44)#define I3C\_BCR\_DEVICE\_ROLE\_MASK GENMASK(7U, 6U)

133

[ 141](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)#define I3C\_BCR\_DEVICE\_ROLE(bcr) \

142 FIELD\_GET(I3C\_BCR\_DEVICE\_ROLE\_MASK, (bcr))

143

145

165

[ 167](group__i3c__interface.md#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)#define I3C\_LVR\_I2C\_FM\_PLUS\_MODE 0

168

[ 170](group__i3c__interface.md#ga053945f5f67ee3c681de2c9362e69c39)#define I3C\_LVR\_I2C\_FM\_MODE 1

171

[ 173](group__i3c__interface.md#gaf073cc9ea1a68c57663c36de12554876)#define I3C\_LVR\_I2C\_MODE\_MASK BIT(4)

174

[ 182](group__i3c__interface.md#gaaf759805bb5824a89612b292a4439982)#define I3C\_LVR\_I2C\_MODE(lvr) \

183 FIELD\_GET(I3C\_LVR\_I2C\_MODE\_MASK, (lvr))

184

[ 191](group__i3c__interface.md#ga4319835ddb6b5984b21f5a5a2f14ae75)#define I3C\_LVR\_I2C\_DEV\_IDX\_0 0

192

[ 199](group__i3c__interface.md#ga02a21af4c679a81b8290beea30c8ef40)#define I3C\_LVR\_I2C\_DEV\_IDX\_1 1

200

[ 207](group__i3c__interface.md#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)#define I3C\_LVR\_I2C\_DEV\_IDX\_2 2

208

[ 210](group__i3c__interface.md#ga50fa249b36b91d56e49004548a1c7520)#define I3C\_LVR\_I2C\_DEV\_IDX\_MASK GENMASK(7U, 5U)

211

[ 219](group__i3c__interface.md#gae7afa509b1d63374c551bcdaf84c5dd1)#define I3C\_LVR\_I2C\_DEV\_IDX(lvr) \

220 FIELD\_GET(I3C\_LVR\_I2C\_DEV\_IDX\_MASK, (lvr))

221

223

[ 227](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90)enum [i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90) {

[ 229](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445) [I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445),

230

[ 235](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434) [I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434),

236

[ 242](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722) [I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722),

243

[ 249](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a) [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a),

250

[ 251](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) [I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) = [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a),

[ 252](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c) [I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c),

253};

254

[ 260](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6)enum [i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6) {

[ 262](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1) [I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1),

263

[ 265](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea) [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea),

266

[ 267](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) [I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) = [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea),

[ 268](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4) [I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4),

269};

270

[ 276](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073)enum [i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073) {

[ 278](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9) [I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9),

279

[ 281](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301) [I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301),

282

[ 284](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590) [I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590),

285

[ 287](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d) [I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d),

288

[ 290](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed) [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed),

291

[ 292](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) [I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) = [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed),

[ 293](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a) [I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a),

294};

295

301

302/\*

303 \* I3C\_MSG\_\* are I3C Message flags.

304 \*/

305

[ 307](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)#define I3C\_MSG\_WRITE (0U << 0U)

308

[ 310](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)#define I3C\_MSG\_READ BIT(0)

311

313#define I3C\_MSG\_RW\_MASK BIT(0)

315

[ 317](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)#define I3C\_MSG\_STOP BIT(1)

318

[ 328](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)#define I3C\_MSG\_RESTART BIT(2)

329

[ 331](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38)#define I3C\_MSG\_HDR BIT(3)

332

[ 334](group__i3c__transfer__api.md#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)#define I3C\_MSG\_NBCH BIT(4)

335

[ 337](group__i3c__transfer__api.md#ga18aac0862826869f94e5a71670debcb0)#define I3C\_MSG\_HDR\_MODE0 BIT(0)

338

[ 340](group__i3c__transfer__api.md#ga8eb3dc48237dfdb25fde40a1efa03241)#define I3C\_MSG\_HDR\_MODE1 BIT(1)

341

[ 343](group__i3c__transfer__api.md#ga15cbd61e7d509c28b22fbc9e0844cb23)#define I3C\_MSG\_HDR\_MODE2 BIT(2)

344

[ 346](group__i3c__transfer__api.md#ga162fb9ab0e4ed7f8feb0e91d183a88e7)#define I3C\_MSG\_HDR\_MODE3 BIT(3)

347

[ 349](group__i3c__transfer__api.md#gabe45532238bc15672f6454dac70d20cf)#define I3C\_MSG\_HDR\_MODE4 BIT(4)

350

[ 352](group__i3c__transfer__api.md#gac712daa606d0c51ce523d7a687821282)#define I3C\_MSG\_HDR\_MODE5 BIT(5)

353

[ 355](group__i3c__transfer__api.md#ga7654c1947e13c019c24bf12712b0773b)#define I3C\_MSG\_HDR\_MODE6 BIT(6)

356

[ 358](group__i3c__transfer__api.md#ga08df1d8df82226d1f23b4cc923584672)#define I3C\_MSG\_HDR\_MODE7 BIT(7)

359

[ 361](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a)#define I3C\_MSG\_HDR\_DDR I3C\_MSG\_HDR\_MODE0

362

[ 364](group__i3c__transfer__api.md#gaa61322f770db296b5ab718c48ab960d3)#define I3C\_MSG\_HDR\_TSP I3C\_MSG\_HDR\_MODE1

365

[ 367](group__i3c__transfer__api.md#gac43a2d266f3a23fd6dfa11405f3fd6f3)#define I3C\_MSG\_HDR\_TSL I3C\_MSG\_HDR\_MODE2

368

[ 370](group__i3c__transfer__api.md#ga8b2fdcb827cbd3325f124a1c615698e7)#define I3C\_MSG\_HDR\_BT I3C\_MSG\_HDR\_MODE3

371

373

378

[ 393](structi3c__msg.md)struct [i3c\_msg](structi3c__msg.md) {

[ 395](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

396

[ 398](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0);

399

[ 407](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_xfer](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5);

408

[ 415](structi3c__msg.md#ae43cb150bcdec5f0bf654c794757f756) enum [i3c\_sdr\_controller\_error\_types](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0) [err](structi3c__msg.md#ae43cb150bcdec5f0bf654c794757f756);

416

[ 418](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217);

419

[ 426](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9);

427

[ 429](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b);

430};

431

433

[ 437](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) {

[ 438](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5) [I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5),

[ 439](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00) [I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00),

[ 440](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017) [I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017),

441};

442

[ 446](structi3c__config__controller.md)struct [i3c\_config\_controller](structi3c__config__controller.md) {

[ 451](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36) bool [is\_secondary](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36);

452

453 struct {

[ 455](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i3c](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b);

456

[ 458](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd);

[ 459](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b) } [scl](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b);

460

[ 467](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_hdr](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d);

468};

469

[ 478](structi3c__config__custom.md)struct [i3c\_config\_custom](structi3c__config__custom.md) {

[ 480](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31);

481

482 union {

[ 484](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [val](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340);

485

[ 492](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd) void \*[ptr](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd);

493 };

494};

495

502struct [i3c\_device\_desc](structi3c__device__desc.md);

503struct [i3c\_device\_id](structi3c__device__id.md);

504struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md);

505struct [i3c\_target\_config](structi3c__target__config.md);

506struct [i3c\_config\_target](structi3c__config__target.md);

507

508\_\_subsystem struct i3c\_driver\_api {

518 struct i2c\_driver\_api i2c\_api;

519

532 int (\*configure)(const struct device \*dev,

533 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config);

534

547 int (\*config\_get)(const struct device \*dev,

548 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config);

549#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

561 int (\*recover\_bus)(const struct device \*dev);

562

575 int (\*attach\_i3c\_device)(const struct device \*dev,

576 struct i3c\_device\_desc \*target);

577

591 int (\*reattach\_i3c\_device)(const struct device \*dev,

592 struct i3c\_device\_desc \*target,

593 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr);

594

607 int (\*detach\_i3c\_device)(const struct device \*dev,

608 struct i3c\_device\_desc \*target);

609

622 int (\*attach\_i2c\_device)(const struct device \*dev,

623 struct i3c\_i2c\_device\_desc \*target);

624

637 int (\*detach\_i2c\_device)(const struct device \*dev,

638 struct i3c\_i2c\_device\_desc \*target);

639

651 int (\*do\_daa)(const struct device \*dev);

652

665 int (\*do\_ccc)(const struct device \*dev,

666 struct i3c\_ccc\_payload \*payload);

667

680 int (\*i3c\_xfers)(const struct device \*dev,

681 struct i3c\_device\_desc \*target,

682 struct i3c\_msg \*msgs,

683 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

684

698 struct i3c\_device\_desc \*(\*i3c\_device\_find)(const struct device \*dev,

699 const struct i3c\_device\_id \*id);

700#endif /\* CONFIG\_I3C\_CONTROLLER \*/

701#ifdef CONFIG\_I3C\_USE\_IBI

702#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

715 int (\*ibi\_raise)(const struct device \*dev,

716 struct i3c\_ibi \*request);

717#endif /\* CONFIG\_I3C\_TARGET \*/

718#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

729 int (\*ibi\_hj\_response)(const struct device \*dev,

730 bool ack);

731

744 int (\*ibi\_enable)(const struct device \*dev,

745 struct i3c\_device\_desc \*target);

746

759 int (\*ibi\_disable)(const struct device \*dev,

760 struct i3c\_device\_desc \*target);

761#endif /\* CONFIG\_I3C\_CONTROLLER \*/

762#endif /\* CONFIG\_I3C\_USE\_IBI \*/

763#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

779 int (\*target\_register)(const struct device \*dev,

780 struct i3c\_target\_config \*cfg);

781

797 int (\*target\_unregister)(const struct device \*dev,

798 struct i3c\_target\_config \*cfg);

799

816 int (\*target\_tx\_write)(const struct device \*dev,

817 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hdr\_mode);

818

834 int (\*target\_controller\_handoff)(const struct device \*dev,

835 bool [accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864));

836#endif /\* CONFIG\_I3C\_TARGET \*/

837#if defined(CONFIG\_I3C\_RTIO) || defined(\_\_DOXYGEN\_\_)

848 void (\*iodev\_submit)(const struct device \*dev,

849 struct rtio\_iodev\_sqe \*iodev\_sqe);

850#endif /\* CONFIG\_I3C\_RTIO \*/

851};

852

856

[ 860](structi3c__device__id.md)struct [i3c\_device\_id](structi3c__device__id.md) {

[ 862](structi3c__device__id.md#a78a8fb4cda85690d866a8e03b982666f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__device__id.md#a78a8fb4cda85690d866a8e03b982666f):48;

863};

864

[ 873](group__i3c__interface.md#gaed0df9802cc9b268abcfe4e877ebf498)#define I3C\_DEVICE\_ID(pid) \

874 { \

875 .pid = pid \

876 }

877

[ 894](structi3c__device__desc.md)struct [i3c\_device\_desc](structi3c__device__desc.md) {

[ 895](structi3c__device__desc.md#a965edbd5d74c06773e190a14d4f6e3cd) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__device__desc.md#a965edbd5d74c06773e190a14d4f6e3cd);

896

[ 898](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809) const struct [device](structdevice.md) \*[bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809);

899

[ 901](structi3c__device__desc.md#af0466893f56f9aebdaa7677a9a0076ed) const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#af0466893f56f9aebdaa7677a9a0076ed);

902

[ 904](structi3c__device__desc.md#a153ff108d8cf523d60aad3534d06f88e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__device__desc.md#a153ff108d8cf523d60aad3534d06f88e);

905

[ 918](structi3c__device__desc.md#a078901f1dc853dabf6503407d78735c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__device__desc.md#a078901f1dc853dabf6503407d78735c0);

919

[ 929](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5);

930

[ 938](structi3c__device__desc.md#a5cc5f0ffdd173478275a6b5f651d86a3) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi3c__device__desc.md#a5cc5f0ffdd173478275a6b5f651d86a3);

939

[ 953](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0);

954

[ 959](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21);

960

[ 967](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c);

968

969 struct {

[ 971](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523);

972

[ 974](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9);

975

[ 977](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_read\_turnaround](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb);

[ 978](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500) } [data\_speed](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500);

979

980 struct {

[ 982](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mrl](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e);

983

[ 985](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mwl](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed);

986

[ 988](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ibi](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9);

[ 989](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835) } [data\_length](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835);

990

[ 992](structi3c__device__desc.md#a3fc3b3f1cf396eaf164612e7b667b37a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crhdly1](structi3c__device__desc.md#a3fc3b3f1cf396eaf164612e7b667b37a);

993

995 struct {

996 union {

[ 1004](structi3c__device__desc.md#ae01bc68ac8154238d85bbf44dc06dfb7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gethdrcap](structi3c__device__desc.md#ae01bc68ac8154238d85bbf44dc06dfb7);

1005

[ 1014](structi3c__device__desc.md#a062f86dec32de3b9e899b096df47d828) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap1](structi3c__device__desc.md#a062f86dec32de3b9e899b096df47d828);

1015 };

1016

[ 1024](structi3c__device__desc.md#a089da4f6eaf2b80fc689bb89d527d330) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap2](structi3c__device__desc.md#a089da4f6eaf2b80fc689bb89d527d330);

1025

[ 1037](structi3c__device__desc.md#a47af0b36448dfec8307b25a31712428e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap3](structi3c__device__desc.md#a47af0b36448dfec8307b25a31712428e);

1038

[ 1043](structi3c__device__desc.md#a1314218c6f6a429ccedb9975b9e02a90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap4](structi3c__device__desc.md#a1314218c6f6a429ccedb9975b9e02a90);

[ 1044](structi3c__device__desc.md#a7e44bedd1aa032d661335f8ec0a0d2e2) } [getcaps](structi3c__device__desc.md#a7e44bedd1aa032d661335f8ec0a0d2e2);

1045

1046 /\* Describes Controller Feature Capabilities \*/

1047 struct {

[ 1055](structi3c__device__desc.md#a5ab881cf948d10cfa9e1542b4b5a0f34) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crcaps1](structi3c__device__desc.md#a5ab881cf948d10cfa9e1542b4b5a0f34);

1056

[ 1065](structi3c__device__desc.md#a08e4524060eddc0dc15c985c1c59b9f1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crcaps2](structi3c__device__desc.md#a08e4524060eddc0dc15c985c1c59b9f1);

[ 1066](structi3c__device__desc.md#a5dcad2306094a3ee32a20051f7eafa9a) } [crcaps](structi3c__device__desc.md#a5dcad2306094a3ee32a20051f7eafa9a);

1067

1072 void \*controller\_priv;

1074

1075#if defined(CONFIG\_I3C\_USE\_IBI) || defined(\_\_DOXYGEN\_\_)

[ 1080](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265) [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) [ibi\_cb](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265);

1081#endif /\* CONFIG\_I3C\_USE\_IBI \*/

1082};

1083

[ 1097](structi3c__i2c__device__desc.md)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) {

[ 1098](structi3c__i2c__device__desc.md#acfcf72db311b19e479e9147ce5257245) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__i2c__device__desc.md#acfcf72db311b19e479e9147ce5257245);

1099

[ 1101](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2) const struct [device](structdevice.md) \*[bus](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2);

1102

[ 1104](structi3c__i2c__device__desc.md#a6148be0b55e526b31cb493d697075670) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi3c__i2c__device__desc.md#a6148be0b55e526b31cb493d697075670);

1105

[ 1110](structi3c__i2c__device__desc.md#a610c28ac5e56b540415d48dfabe46dad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lvr](structi3c__i2c__device__desc.md#a610c28ac5e56b540415d48dfabe46dad);

1111

1116 void \*controller\_priv;

1118};

1119

[ 1128](structi3c__dev__attached__list.md)struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) {

[ 1135](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474) struct [i3c\_addr\_slots](structi3c__addr__slots.md) [addr\_slots](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474);

1136

1137 struct {

[ 1141](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [i3c](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad);

1142

[ 1146](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [i2c](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a);

[ 1147](structi3c__dev__attached__list.md#adf700818ee21cf60f84e2aa6946d19f4) } [devices](structi3c__dev__attached__list.md#adf700818ee21cf60f84e2aa6946d19f4);

1148};

1149

[ 1158](structi3c__dev__list.md)struct [i3c\_dev\_list](structi3c__dev__list.md) {

[ 1162](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce) struct [i3c\_device\_desc](structi3c__device__desc.md) \* const [i3c](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce);

1163

[ 1167](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e) struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* const [i2c](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e);

1168

[ 1172](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_i3c](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985);

1173

[ 1177](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_i2c](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318);

1178};

1179

[ 1185](structi3c__driver__config.md)struct [i3c\_driver\_config](structi3c__driver__config.md) {

1186#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1188](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193) struct [i3c\_dev\_list](structi3c__dev__list.md) [dev\_list](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193);

1189

[ 1191](structi3c__driver__config.md#a52b9e5a36b65fbadc7fd2369ff184271) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [primary\_controller\_da](structi3c__driver__config.md#a52b9e5a36b65fbadc7fd2369ff184271);

1192#elif defined(CONFIG\_CPP)

1193 /\* Empty struct has size 0 in C, size 1 in C++. Force them to be the same. \*/

1194 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unused\_cpp\_size\_compatibility;

1195#endif

1196};

1197

1198#if defined(CONFIG\_CPP)

1199BUILD\_ASSERT(sizeof(struct [i3c\_driver\_config](structi3c__driver__config.md)) >= 1);

1200#endif

1201

[ 1206](structi3c__driver__data.md)struct [i3c\_driver\_data](structi3c__driver__data.md) {

[ 1208](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb) struct [i3c\_config\_controller](structi3c__config__controller.md) [ctrl\_config](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb);

1209#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1211](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901) struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) [attached\_dev](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901);

1212#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

[ 1214](structi3c__driver__data.md#a1f1e3c1017b6214486474078b7d948f7) struct [i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md) \*[deftgts](structi3c__driver__data.md#a1f1e3c1017b6214486474078b7d948f7);

1215

[ 1217](structi3c__driver__data.md#a968fe84e8de0ac443228ebd20493c49c) bool [deftgts\_refreshed](structi3c__driver__data.md#a968fe84e8de0ac443228ebd20493c49c);

1218#endif /\* CONFIG\_I3C\_TARGET \*/

1219#endif /\* CONFIG\_I3C\_CONTROLLER \*/

1220};

1221#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1229](group__i3c__interface.md#ga42cb4edf6a099d586df14456fd98c873)#define I3C\_BUS\_FOR\_EACH\_I3CDEV(bus, desc) \

1230 SYS\_SLIST\_FOR\_EACH\_CONTAINER( \

1231 &((struct i3c\_driver\_data \*)(bus->data))->attached\_dev.devices.i3c, desc, node)

1232

[ 1240](group__i3c__interface.md#ga450ba9021d1080f890c32624f20ba2b8)#define I3C\_BUS\_FOR\_EACH\_I2CDEV(bus, desc) \

1241 SYS\_SLIST\_FOR\_EACH\_CONTAINER( \

1242 &((struct i3c\_driver\_data \*)(bus->data))->attached\_dev.devices.i2c, desc, node)

1243

[ 1256](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)(const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list,

1257 const struct [i3c\_device\_id](structi3c__device__id.md) \*id);

1258

[ 1271](group__i3c__interface.md#ga0e83c5a26b18acfbe7d532825a8fd54c)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#ga0e83c5a26b18acfbe7d532825a8fd54c)(const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#af0466893f56f9aebdaa7677a9a0076ed),

1272 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

1273

[ 1286](group__i3c__interface.md#gaecbb16ce8edcd9ad7a7afcfb1251aa76)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_i3c\_static\_addr\_find](group__i3c__interface.md#gaecbb16ce8edcd9ad7a7afcfb1251aa76)(const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#af0466893f56f9aebdaa7677a9a0076ed),

1287 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

1288

[ 1301](group__i3c__interface.md#gafac78dca571ff7daa34fca0cfa7cc3b1)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*[i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#gafac78dca571ff7daa34fca0cfa7cc3b1)(const struct [device](structdevice.md) \*dev,

1302 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi3c__i2c__device__desc.md#a6148be0b55e526b31cb493d697075670));

1303

[ 1355](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)int [i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

1356 const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list,

1357 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pid, bool must\_match,

1358 bool assigned\_okay,

1359 struct [i3c\_device\_desc](structi3c__device__desc.md) \*\*target,

1360 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structi3c__i2c__device__desc.md#a6148be0b55e526b31cb493d697075670));

1361#endif /\* CONFIG\_I3C\_CONTROLLER \*/

[ 1375](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)static inline int [i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)(const struct [device](structdevice.md) \*dev,

1376 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config)

1377{

1378 const struct i3c\_driver\_api \*api =

1379 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1380

1381 if (api->configure == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1382 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1383 }

1384

1385 return api->configure(dev, type, config);

1386}

1387#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1403](group__i3c__interface.md#gaeca24930774ecc2dcbf2240d48ae19c5)static inline int [i3c\_configure\_controller](group__i3c__interface.md#gaeca24930774ecc2dcbf2240d48ae19c5)(const struct [device](structdevice.md) \*dev,

1404 struct [i3c\_config\_controller](structi3c__config__controller.md) \*config)

1405{

1406 return [i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)(dev, [I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5), config);

1407}

1408#endif /\* CONFIG\_I3C\_CONTROLLER \*/

1409#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

[ 1425](group__i3c__interface.md#ga7dfa33c7bdbe7e6607af61fe04bcb985)static inline int [i3c\_configure\_target](group__i3c__interface.md#ga7dfa33c7bdbe7e6607af61fe04bcb985)(const struct [device](structdevice.md) \*dev,

1426 struct [i3c\_config\_target](structi3c__config__target.md) \*config)

1427{

1428 return [i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)(dev, [I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00), config);

1429}

1430#endif /\* CONFIG\_I3C\_TARGET \*/

[ 1451](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)static inline int [i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)(const struct [device](structdevice.md) \*dev,

1452 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config)

1453{

1454 const struct i3c\_driver\_api \*api =

1455 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1456

1457 if (api->config\_get == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1458 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1459 }

1460

1461 return api->config\_get(dev, type, config);

1462}

1463#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1479](group__i3c__interface.md#ga96cd903b4a676c5943c43cc7b27af867)static inline int [i3c\_config\_get\_controller](group__i3c__interface.md#ga96cd903b4a676c5943c43cc7b27af867)(const struct [device](structdevice.md) \*dev,

1480 struct [i3c\_config\_controller](structi3c__config__controller.md) \*config)

1481{

1482 return [i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)(dev, [I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5), config);

1483}

1484#endif /\* CONFIG\_I3C\_CONTROLLER \*/

1485#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

[ 1501](group__i3c__interface.md#ga8ef11af673e94646806e093504cfb01f)static inline int [i3c\_config\_get\_target](group__i3c__interface.md#ga8ef11af673e94646806e093504cfb01f)(const struct [device](structdevice.md) \*dev,

1502 struct [i3c\_config\_target](structi3c__config__target.md) \*config)

1503{

1504 return [i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)(dev, [I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00), config);

1505}

1506#endif /\* CONFIG\_I3C\_TARGET \*/

1507#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1518](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)static inline int [i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)(const struct [device](structdevice.md) \*dev)

1519{

1520 const struct i3c\_driver\_api \*api =

1521 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1522

1523 if (api->recover\_bus == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1524 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1525 }

1526

1527 return api->recover\_bus(dev);

1528}

1529

[ 1549](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)int [i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1550

[ 1575](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)int [i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr);

1576

[ 1596](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)int [i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1597

[ 1616](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)int [i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target);

1617

[ 1635](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)int [i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target);

1636

[ 1660](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)static inline int [i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)(const struct [device](structdevice.md) \*dev)

1661{

1662 const struct i3c\_driver\_api \*api =

1663 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1664

1665 if (api->do\_daa == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1666 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1667 }

1668

1669 return api->do\_daa(dev);

1670}

1671

[ 1685](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)\_\_syscall int [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)(const struct [device](structdevice.md) \*dev,

1686 struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload);

1687

1688static inline int z\_impl\_i3c\_do\_ccc(const struct [device](structdevice.md) \*dev,

1689 struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload)

1690{

1691 const struct i3c\_driver\_api \*api =

1692 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1693

1694 if (api->do\_ccc == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1695 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1696 }

1697

1698 return api->do\_ccc(dev, payload);

1699}

1700

1705

[ 1732](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)\_\_syscall int [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1733 struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

1734

1735static inline int z\_impl\_i3c\_transfer(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1736 struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs)

1737{

1738 const struct i3c\_driver\_api \*api =

1739 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1740

1741 return api->i3c\_xfers(target->bus, target, msgs, num\_msgs);

1742}

1743

1745

1760static inline

[ 1761](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)(const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#af0466893f56f9aebdaa7677a9a0076ed),

1762 const struct [i3c\_device\_id](structi3c__device__id.md) \*id)

1763{

1764 const struct i3c\_driver\_api \*api =

1765 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1766

1767 if (api->i3c\_device\_find == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1768 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1769 }

1770

1771 return api->i3c\_device\_find(dev, id);

1772}

1773#endif /\* CONFIG\_I3C\_CONTROLLER \*/

1774#if defined(CONFIG\_I3C\_USE\_IBI) || defined(\_\_DOXYGEN\_\_)

1779

1780#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1793](group__i3c__ibi.md#gac8c77e43fc7c06701437e799739507ee)static inline int [i3c\_ibi\_hj\_response](group__i3c__ibi.md#gac8c77e43fc7c06701437e799739507ee)(const struct [device](structdevice.md) \*dev,

1794 bool ack)

1795{

1796 const struct i3c\_driver\_api \*api =

1797 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1798

1799 if (api->ibi\_hj\_response == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1800 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1801 }

1802

1803 return api->ibi\_hj\_response(dev, ack);

1804}

1805#endif /\* CONFIG\_I3C\_CONTROLLER \*/

1806#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

[ 1818](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)static inline int [i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)(const struct [device](structdevice.md) \*dev,

1819 struct [i3c\_ibi](structi3c__ibi.md) \*request)

1820{

1821 const struct i3c\_driver\_api \*api =

1822 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1823

1824 if (api->ibi\_raise == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1825 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1826 }

1827

1828 return api->ibi\_raise(dev, request);

1829}

1830#endif /\* CONFIG\_I3C\_TARGET \*/

1831#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

[ 1846](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)static inline int [i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1847{

1848 const struct i3c\_driver\_api \*api =

1849 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1850

1851 if (api->ibi\_enable == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1852 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1853 }

1854

1855 return api->ibi\_enable(target->[bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809), target);

1856}

1857

[ 1870](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)static inline int [i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1871{

1872 const struct i3c\_driver\_api \*api =

1873 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1874

1875 if (api->ibi\_disable == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1876 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1877 }

1878

1879 return api->ibi\_disable(target->[bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809), target);

1880}

1881#endif /\* CONFIG\_I3C\_CONTROLLER \*/

1882#endif /\* CONFIG\_I3C\_USE\_IBI \*/

[ 1894](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)static inline int [i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1895{

1896 return (target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) & [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838))

1897 == [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838);

1898}

1899

[ 1911](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)static inline int [i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1912{

1913 return (target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) & [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f))

1914 == [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f);

1915}

1916

[ 1928](group__i3c__ibi.md#ga537c1e2dafe3df1a5758e535beb323ea)static inline int [i3c\_device\_is\_controller\_capable](group__i3c__ibi.md#ga537c1e2dafe3df1a5758e535beb323ea)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1929{

1930 return [I3C\_BCR\_DEVICE\_ROLE](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)(target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21))

1931 == [I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852);

1932}

1933

1935#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

1940

[ 1954](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)static inline int [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1955 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1956{

1957 struct [i3c\_msg](structi3c__msg.md) msg;

1958

1959 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1960 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1961 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1962 msg.[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1963 msg.[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1964

1965 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

1966}

1967

[ 1981](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)static inline int [i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1982 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1983{

1984 struct [i3c\_msg](structi3c__msg.md) msg;

1985

1986 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1987 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1988 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1989 msg.[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1990 msg.[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1991

1992 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

1993}

1994

[ 2012](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)static inline int [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2013 const void \*write\_buf, size\_t num\_write,

2014 void \*read\_buf, size\_t num\_read)

2015{

2016 struct [i3c\_msg](structi3c__msg.md) msg[2];

2017

2018 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)write\_buf;

2019 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_write;

2020 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b);

2021 msg[0].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

2022 msg[0].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

2023

2024 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)read\_buf;

2025 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_read;

2026 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295) | [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

2027 msg[1].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

2028 msg[1].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

2029

2030 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

2031}

2032

[ 2050](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)static inline int [i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2051 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

2052 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff),

2053 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

2054{

2055 return [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(target,

2056 &start\_addr, sizeof(start\_addr),

2057 [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), num\_bytes);

2058}

2059

[ 2080](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)static inline int [i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2081 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

2082 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff),

2083 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

2084{

2085 struct [i3c\_msg](structi3c__msg.md) msg[2];

2086

2087 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = &start\_addr;

2088 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = 1U;

2089 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b);

2090 msg[0].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

2091 msg[0].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

2092

2093 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

2094 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

2095 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

2096 msg[1].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

2097 msg[1].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

2098

2099 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

2100}

2101

[ 2116](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)static inline int [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2117 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)

2118{

2119 return [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(target,

2120 &reg\_addr, sizeof(reg\_addr),

2121 value, sizeof(\*value));

2122}

2123

[ 2141](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)static inline int [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2142 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

2143{

2144 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_buf[2] = {reg\_addr, value};

2145

2146 return [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)(target, tx\_buf, 2);

2147}

2148

[ 2167](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)static inline int [i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2168 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask,

2169 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

2170{

2171 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_value, new\_value;

2172 int rc;

2173

2174 rc = [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)(target, reg\_addr, &old\_value);

2175 if (rc != 0) {

2176 return rc;

2177 }

2178

2179 new\_value = (old\_value & ~mask) | (value & mask);

2180 if (new\_value == old\_value) {

2181 return 0;

2182 }

2183

2184 return [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)(target, reg\_addr, new\_value);

2185}

2186

[ 2211](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)void [i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)(const char \*name, const struct [i3c\_msg](structi3c__msg.md) \*msgs,

2212 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2213

2215

[ 2231](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)int [i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)(const struct [device](structdevice.md) \*dev,

2232 const struct [i3c\_dev\_list](structi3c__dev__list.md) \*[i3c\_dev\_list](structi3c__dev__list.md));

2233

[ 2251](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)int [i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2252

[ 2275](group__i3c__interface.md#ga4e4a7e9408bd2f43602367bc9fe4f81e)int [i3c\_device\_adv\_info\_get](group__i3c__interface.md#ga4e4a7e9408bd2f43602367bc9fe4f81e)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2276

[ 2298](group__i3c__interface.md#ga39a760d8ba759f9443689fc954eb3d4b)static inline int [i3c\_device\_info\_get](group__i3c__interface.md#ga39a760d8ba759f9443689fc954eb3d4b)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

2299{

2300 int rc;

2301

2302 rc = [i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)(target);

2303 if (rc != 0) {

2304 return rc;

2305 }

2306

2307 return [i3c\_device\_adv\_info\_get](group__i3c__interface.md#ga4e4a7e9408bd2f43602367bc9fe4f81e)(target);

2308}

2309

[ 2320](group__i3c__interface.md#ga149d70b1c2e02e19782aa21a94b13684)bool [i3c\_bus\_has\_sec\_controller](group__i3c__interface.md#ga149d70b1c2e02e19782aa21a94b13684)(const struct [device](structdevice.md) \*dev);

2321

[ 2332](group__i3c__interface.md#ga14ec397e1c82b79302f7eff6022660ae)int [i3c\_bus\_rstdaa\_all](group__i3c__interface.md#ga14ec397e1c82b79302f7eff6022660ae)(const struct [device](structdevice.md) \*dev);

2333

[ 2346](group__i3c__interface.md#ga2ae8b79140ddceebd071e0891a0ac824)int [i3c\_bus\_setdasa](group__i3c__interface.md#ga2ae8b79140ddceebd071e0891a0ac824)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dynamic\_addr);

2347

[ 2360](group__i3c__interface.md#ga55ba4babddb31ed83ad3fab5adce2f18)int [i3c\_bus\_setnewda](group__i3c__interface.md#ga55ba4babddb31ed83ad3fab5adce2f18)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dynamic\_addr);

2361

[ 2372](group__i3c__interface.md#gab6735824952836a1ac06745b21e2b534)int [i3c\_bus\_setaasa](group__i3c__interface.md#gab6735824952836a1ac06745b21e2b534)(const struct [device](structdevice.md) \*dev);

2373

[ 2384](group__i3c__interface.md#gac8c0ec6eb11030183be10fb541e1e561)int [i3c\_bus\_getbcr](group__i3c__interface.md#gac8c0ec6eb11030183be10fb541e1e561)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2385

[ 2396](group__i3c__interface.md#gaab2801ccc00e9891269709ecc34f4f7c)int [i3c\_bus\_getdcr](group__i3c__interface.md#gaab2801ccc00e9891269709ecc34f4f7c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2397

[ 2408](group__i3c__interface.md#ga129bab2c352fd08b62c352d916c7307c)int [i3c\_bus\_getpid](group__i3c__interface.md#ga129bab2c352fd08b62c352d916c7307c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2409

[ 2420](group__i3c__interface.md#ga5483ce25f70cae032ed5935483102c0f)int [i3c\_bus\_getmrl](group__i3c__interface.md#ga5483ce25f70cae032ed5935483102c0f)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2421

[ 2432](group__i3c__interface.md#ga8d4da712075ee05896bcd7dde49cd827)int [i3c\_bus\_getmwl](group__i3c__interface.md#ga8d4da712075ee05896bcd7dde49cd827)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2433

[ 2446](group__i3c__interface.md#ga6fbb9bec228b7dc310c5724c3530bebd)int [i3c\_bus\_setmrl](group__i3c__interface.md#ga6fbb9bec228b7dc310c5724c3530bebd)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mrl, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ibi\_len);

2447

[ 2459](group__i3c__interface.md#ga8002de8239c4a0d1178fba27092a1254)int [i3c\_bus\_setmwl](group__i3c__interface.md#ga8002de8239c4a0d1178fba27092a1254)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mwl);

2460

[ 2474](group__i3c__interface.md#ga28278e90417b01d7cb18a301f906f6ae)int [i3c\_bus\_setmrl\_all](group__i3c__interface.md#ga28278e90417b01d7cb18a301f906f6ae)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mrl, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ibi\_len, bool has\_ibi\_size);

2475

[ 2487](group__i3c__interface.md#gad3a4bf3cfc1b150c19ff1186cc8e3e2a)int [i3c\_bus\_setmwl\_all](group__i3c__interface.md#gad3a4bf3cfc1b150c19ff1186cc8e3e2a)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mwl);

2488

2489#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

[ 2500](group__i3c__interface.md#ga8d4356b56d8414e62b5a9931ffc7ab8b)int [i3c\_bus\_getacccr](group__i3c__interface.md#ga8d4356b56d8414e62b5a9931ffc7ab8b)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2501

[ 2513](group__i3c__interface.md#ga554e0c4fa3e6855f431521ae42313216)int [i3c\_bus\_deftgts](group__i3c__interface.md#ga554e0c4fa3e6855f431521ae42313216)(const struct [device](structdevice.md) \*dev);

2514#endif /\* CONFIG\_I3C\_TARGET \*/

2515

[ 2525](group__i3c__interface.md#gaaf7736a8895de826f7fac1a9ecf0d7ea)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [i3c\_odd\_parity](group__i3c__interface.md#gaaf7736a8895de826f7fac1a9ecf0d7ea)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) p);

2526

[ 2541](group__i3c__interface.md#gaedf58fdd96f38f103f8defe221427b6f)int [i3c\_device\_controller\_handoff](group__i3c__interface.md#gaedf58fdd96f38f103f8defe221427b6f)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, bool requested);

2542#endif /\* CONFIG\_I3C\_CONTROLLER \*/

2543

2544#if defined(CONFIG\_I3C\_USE\_IBI) || defined(\_\_DOXYGEN\_\_)

2545#if (defined(CONFIG\_I3C\_CONTROLLER) && defined(CONFIG\_I3C\_TARGET)) || defined(\_\_DOXYGEN\_\_)

[ 2557](group__i3c__interface.md#ga221ab7abe735ddee881c002b934ee138)void [i3c\_sec\_handoffed](group__i3c__interface.md#ga221ab7abe735ddee881c002b934ee138)(struct [k\_work](structk__work.md) \*work);

2558#endif /\* CONFIG\_I3C\_CONTROLLER && CONFIG\_I3C\_TARGET \*/

2559#endif /\* CONFIG\_I3C\_USE\_IBI \*/

2560

2561#if (defined(CONFIG\_I3C\_NUM\_OF\_DESC\_MEM\_SLABS) && CONFIG\_I3C\_NUM\_OF\_DESC\_MEM\_SLABS > 0) || \

2562 defined(\_\_DOXYGEN\_\_)

2563

[ 2572](group__i3c__interface.md#gab8e12d10528686040707f4aae502df98)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_device\_desc\_alloc](group__i3c__interface.md#gab8e12d10528686040707f4aae502df98)(void);

2573

[ 2581](group__i3c__interface.md#ga25bfef54bb7bdc387ce0997ed0120739)void [i3c\_device\_desc\_free](group__i3c__interface.md#ga25bfef54bb7bdc387ce0997ed0120739)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2582

[ 2592](group__i3c__interface.md#gaf2c8afec987322be8dfd4fb053fac61b)bool [i3c\_device\_desc\_in\_pool](group__i3c__interface.md#gaf2c8afec987322be8dfd4fb053fac61b)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

2593

2594#else

2595

2596static inline struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_device\_desc\_alloc](group__i3c__interface.md#gab8e12d10528686040707f4aae502df98)(void)

2597{

2598 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2599}

2600

2601static inline void [i3c\_device\_desc\_free](group__i3c__interface.md#ga25bfef54bb7bdc387ce0997ed0120739)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc)

2602{

2603 ARG\_UNUSED(desc);

2604}

2605

2606static inline bool [i3c\_device\_desc\_in\_pool](group__i3c__interface.md#gaf2c8afec987322be8dfd4fb053fac61b)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc)

2607{

2608 ARG\_UNUSED(desc);

2609 return false;

2610}

2611

2612#endif /\* CONFIG\_I3C\_NUM\_OF\_DESC\_MEM\_SLABS > 0 \*/

2613

2614#if (defined(CONFIG\_I3C\_I2C\_NUM\_OF\_DESC\_MEM\_SLABS) && CONFIG\_I3C\_I2C\_NUM\_OF\_DESC\_MEM\_SLABS > 0) || \

2615 defined(\_\_DOXYGEN\_\_)

2616

[ 2625](group__i3c__interface.md#ga16b9ba6480ac807ff8b9268d6cffa577)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*[i3c\_i2c\_device\_desc\_alloc](group__i3c__interface.md#ga16b9ba6480ac807ff8b9268d6cffa577)(void);

2626

[ 2634](group__i3c__interface.md#ga61ead89539fe3556f5e6e30eae5e71a3)void [i3c\_i2c\_device\_desc\_free](group__i3c__interface.md#ga61ead89539fe3556f5e6e30eae5e71a3)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*desc);

2635

[ 2645](group__i3c__interface.md#gabfebceaa3e6f6f255352b8dcc3e7f9b1)bool [i3c\_i2c\_device\_desc\_in\_pool](group__i3c__interface.md#gabfebceaa3e6f6f255352b8dcc3e7f9b1)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*desc);

2646

2647#else

2648

2649static inline struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*[i3c\_i2c\_device\_desc\_alloc](group__i3c__interface.md#ga16b9ba6480ac807ff8b9268d6cffa577)(void)

2650{

2651 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

2652}

2653

2654static inline void [i3c\_i2c\_device\_desc\_free](group__i3c__interface.md#ga61ead89539fe3556f5e6e30eae5e71a3)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*desc)

2655{

2656 ARG\_UNUSED(desc);

2657}

2658

2659static inline bool [i3c\_i2c\_device\_desc\_in\_pool](group__i3c__interface.md#gabfebceaa3e6f6f255352b8dcc3e7f9b1)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*desc)

2660{

2661 ARG\_UNUSED(desc);

2662 return false;

2663}

2664

2665#endif /\* CONFIG\_I3C\_I2C\_NUM\_OF\_DESC\_MEM\_SLABS > 0 \*/

2666

2667#if defined(CONFIG\_I3C\_RTIO) || defined(\_\_DOXYGEN\_\_)

2668

[ 2669](structi3c__iodev__data.md)struct [i3c\_iodev\_data](structi3c__iodev__data.md) {

[ 2670](structi3c__iodev__data.md#a22c368ac3cd8b7b8a8770de3b37afb07) const struct [device](structdevice.md) \*[bus](structi3c__iodev__data.md#a22c368ac3cd8b7b8a8770de3b37afb07);

[ 2671](structi3c__iodev__data.md#a3d4146137def71cbb84d1ae3cef67c55) const struct [i3c\_device\_id](structi3c__device__id.md) [dev\_id](structi3c__iodev__data.md#a3d4146137def71cbb84d1ae3cef67c55);

2672};

2673

[ 2684](group__i3c__interface.md#ga909d531941cd81850f4a05c51646690d)void [i3c\_iodev\_submit\_fallback](group__i3c__interface.md#ga909d531941cd81850f4a05c51646690d)(const struct [device](structdevice.md) \*dev, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

2685

[ 2692](group__i3c__interface.md#ga3b612267e71202094fb4adab64ffd61c)static inline void [i3c\_iodev\_submit](group__i3c__interface.md#ga3b612267e71202094fb4adab64ffd61c)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

2693{

2694 const struct [i3c\_iodev\_data](structi3c__iodev__data.md) \*data =

2695 (const struct [i3c\_iodev\_data](structi3c__iodev__data.md) \*)iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

2696 const struct i3c\_driver\_api \*api = (const struct i3c\_driver\_api \*)data->[bus](structi3c__iodev__data.md#a22c368ac3cd8b7b8a8770de3b37afb07)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

2697

2698 if (api->iodev\_submit == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

2699 [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(iodev\_sqe, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

2700 return;

2701 }

2702 api->iodev\_submit(data->[bus](structi3c__iodev__data.md#a22c368ac3cd8b7b8a8770de3b37afb07), iodev\_sqe);

2703}

2704

2705extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) [i3c\_iodev\_api](group__i3c__interface.md#gace1f8f10af2d87bb5a17441645030833);

2706

[ 2716](group__i3c__interface.md#gabec5796b92d4582761bc3de456f1df27)#define I3C\_DT\_IODEV\_DEFINE(name, node\_id) \

2717 const struct i3c\_iodev\_data \_i3c\_iodev\_data\_##name = { \

2718 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

2719 .dev\_id = I3C\_DEVICE\_ID\_DT(node\_id), \

2720 }; \

2721 RTIO\_IODEV\_DEFINE(name, &i3c\_iodev\_api, (void \*)&\_i3c\_iodev\_data\_##name)

2722

[ 2734](group__i3c__interface.md#gab46a231442a7bf60e7e28ca2f52d25fc)struct [rtio\_sqe](structrtio__sqe.md) \*[i3c\_rtio\_copy](group__i3c__interface.md#gab46a231442a7bf60e7e28ca2f52d25fc)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

2735 struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc),

2736 const struct [i3c\_msg](structi3c__msg.md) \*msgs,

2737 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

2738

2739#endif /\* CONFIG\_I3C\_RTIO \*/

2740

2741#if defined(CONFIG\_I3C\_TARGET) || defined(\_\_DOXYGEN\_\_)

2742/\*

2743 \* This needs to be after declaration of struct i3c\_driver\_api,

2744 \* or else compiler complains about undefined type inside

2745 \* the static inline API wrappers.

2746 \*/

2747#include <[zephyr/drivers/i3c/target\_device.h](target__device_8h.md)>

2748#endif /\* CONFIG\_I3C\_TARGET \*/

2749

2750#if defined(CONFIG\_I3C\_CONTROLLER) || defined(\_\_DOXYGEN\_\_)

2751/\*

2752 \* Include High-Data-Rate (HDR) inline helper functions

2753 \*/

2754#include <[zephyr/drivers/i3c/hdr\_ddr.h](hdr__ddr_8h.md)>

2755#endif /\* CONFIG\_I3C\_CONTROLLER \*/

2756

2757#ifdef \_\_cplusplus

2758}

2759#endif

2760

2764

2765#include <zephyr/syscalls/i3c.h>

2766

2767#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_H\_ \*/

[addresses.h](addresses_8h.md)

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[ccc.h](ccc_8h.md)

[device.h](device_8h.md)

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[devicetree.h](drivers_2i3c_2devicetree_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[error\_types.h](error__types_8h.md)

[i3c\_sdr\_controller\_error\_types](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0)

i3c\_sdr\_controller\_error\_types

I3C SDR Controller Error Types.

**Definition** error\_types.h:24

[i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)

static int i3c\_ibi\_disable(struct i3c\_device\_desc \*target)

Disable IBI of a target device.

**Definition** i3c.h:1870

[i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)

static int i3c\_ibi\_has\_payload(struct i3c\_device\_desc \*target)

Check if target's IBI has payload.

**Definition** i3c.h:1894

[i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)

static int i3c\_ibi\_raise(const struct device \*dev, struct i3c\_ibi \*request)

Raise an In-Band Interrupt (IBI).

**Definition** i3c.h:1818

[i3c\_device\_is\_controller\_capable](group__i3c__ibi.md#ga537c1e2dafe3df1a5758e535beb323ea)

static int i3c\_device\_is\_controller\_capable(struct i3c\_device\_desc \*target)

Check if the target is controller capable.

**Definition** i3c.h:1928

[i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)

static int i3c\_device\_is\_ibi\_capable(struct i3c\_device\_desc \*target)

Check if device is IBI capable.

**Definition** i3c.h:1911

[i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)

static int i3c\_ibi\_enable(struct i3c\_device\_desc \*target)

Enable IBI of a target device.

**Definition** i3c.h:1846

[i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c)

int(\* i3c\_target\_ibi\_cb\_t)(struct i3c\_device\_desc \*target, struct i3c\_ibi\_payload \*payload)

Function called when In-Band Interrupt received from target device.

**Definition** ibi.h:146

[i3c\_ibi\_hj\_response](group__i3c__ibi.md#gac8c77e43fc7c06701437e799739507ee)

static int i3c\_ibi\_hj\_response(const struct device \*dev, bool ack)

ACK or NACK IBI HJ Requests.

**Definition** i3c.h:1793

[i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)

int i3c\_attach\_i3c\_device(struct i3c\_device\_desc \*target)

Attach an I3C device.

[I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)

#define I3C\_BCR\_IBI\_REQUEST\_CAPABLE

IBI Request Capable bit.

**Definition** i3c.h:89

[I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852)

#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE

Device Role - I3C Controller Capable.

**Definition** i3c.h:129

[i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#ga0e83c5a26b18acfbe7d532825a8fd54c)

struct i3c\_device\_desc \* i3c\_dev\_list\_i3c\_addr\_find(const struct device \*dev, uint8\_t addr)

Find a I3C target device descriptor by dynamic address.

[i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)

static struct i3c\_device\_desc \* i3c\_device\_find(const struct device \*dev, const struct i3c\_device\_id \*id)

Find a registered I3C target device.

**Definition** i3c.h:1761

[i3c\_bus\_getpid](group__i3c__interface.md#ga129bab2c352fd08b62c352d916c7307c)

int i3c\_bus\_getpid(struct i3c\_device\_desc \*desc)

Retrieve the Provisional ID (PID) of a device.

[i3c\_bus\_has\_sec\_controller](group__i3c__interface.md#ga149d70b1c2e02e19782aa21a94b13684)

bool i3c\_bus\_has\_sec\_controller(const struct device \*dev)

Check if the bus has a secondary controller.

[i3c\_bus\_rstdaa\_all](group__i3c__interface.md#ga14ec397e1c82b79302f7eff6022660ae)

int i3c\_bus\_rstdaa\_all(const struct device \*dev)

Reset all devices on the bus and clear their dynamic addresses.

[i3c\_i2c\_device\_desc\_alloc](group__i3c__interface.md#ga16b9ba6480ac807ff8b9268d6cffa577)

struct i3c\_i2c\_device\_desc \* i3c\_i2c\_device\_desc\_alloc(void)

Allocate memory for a i3c i2c device descriptor.

[i3c\_sec\_handoffed](group__i3c__interface.md#ga221ab7abe735ddee881c002b934ee138)

void i3c\_sec\_handoffed(struct k\_work \*work)

Call back for when Controllership is Handoffed to itself.

[i3c\_device\_desc\_free](group__i3c__interface.md#ga25bfef54bb7bdc387ce0997ed0120739)

void i3c\_device\_desc\_free(struct i3c\_device\_desc \*desc)

Free memory from a i3c device descriptor.

[i3c\_bus\_setmrl\_all](group__i3c__interface.md#ga28278e90417b01d7cb18a301f906f6ae)

int i3c\_bus\_setmrl\_all(const struct device \*dev, uint16\_t mrl, uint8\_t ibi\_len, bool has\_ibi\_size)

Set the Maximum Read Length (MRL) for all devices on the bus.

[i3c\_bus\_setdasa](group__i3c__interface.md#ga2ae8b79140ddceebd071e0891a0ac824)

int i3c\_bus\_setdasa(struct i3c\_device\_desc \*desc, uint8\_t dynamic\_addr)

Assign a dynamic address to a device using its static address.

[i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)

static int i3c\_configure(const struct device \*dev, enum i3c\_config\_type type, void \*config)

Configure the I3C hardware.

**Definition** i3c.h:1375

[i3c\_device\_info\_get](group__i3c__interface.md#ga39a760d8ba759f9443689fc954eb3d4b)

static int i3c\_device\_info\_get(struct i3c\_device\_desc \*target)

Get all information from device and update device descriptor.

**Definition** i3c.h:2298

[i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)

int i3c\_dev\_list\_daa\_addr\_helper(struct i3c\_addr\_slots \*addr\_slots, const struct i3c\_dev\_list \*dev\_list, uint64\_t pid, bool must\_match, bool assigned\_okay, struct i3c\_device\_desc \*\*target, uint8\_t \*addr)

Helper function to find a usable address during ENTDAA.

[i3c\_iodev\_submit](group__i3c__interface.md#ga3b612267e71202094fb4adab64ffd61c)

static void i3c\_iodev\_submit(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit request(s) to an I3C device with RTIO.

**Definition** i3c.h:2692

[i3c\_device\_adv\_info\_get](group__i3c__interface.md#ga4e4a7e9408bd2f43602367bc9fe4f81e)

int i3c\_device\_adv\_info\_get(struct i3c\_device\_desc \*target)

Get advanced information from device and update device descriptor.

[i3c\_bus\_getmrl](group__i3c__interface.md#ga5483ce25f70cae032ed5935483102c0f)

int i3c\_bus\_getmrl(struct i3c\_device\_desc \*desc)

Retrieve the Maximum Read Length (MRL) of a device.

[i3c\_bus\_deftgts](group__i3c__interface.md#ga554e0c4fa3e6855f431521ae42313216)

int i3c\_bus\_deftgts(const struct device \*dev)

Send the CCC DEFTGTS.

[i3c\_bus\_setnewda](group__i3c__interface.md#ga55ba4babddb31ed83ad3fab5adce2f18)

int i3c\_bus\_setnewda(struct i3c\_device\_desc \*desc, uint8\_t dynamic\_addr)

Assign a new dynamic address to a device.

[i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)

i3c\_config\_type

Type of configuration being passed to configure function.

**Definition** i3c.h:437

[i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)

int i3c\_attach\_i2c\_device(struct i3c\_i2c\_device\_desc \*target)

Attach an I2C device.

[i3c\_i2c\_device\_desc\_free](group__i3c__interface.md#ga61ead89539fe3556f5e6e30eae5e71a3)

void i3c\_i2c\_device\_desc\_free(struct i3c\_i2c\_device\_desc \*desc)

Free memory from a i3c i2c device descriptor.

[i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6)

i3c\_i2c\_speed\_type

I2C bus speed under I3C bus.

**Definition** i3c.h:260

[i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)

int i3c\_detach\_i3c\_device(struct i3c\_device\_desc \*target)

Detach I3C Device.

[i3c\_bus\_setmrl](group__i3c__interface.md#ga6fbb9bec228b7dc310c5724c3530bebd)

int i3c\_bus\_setmrl(struct i3c\_device\_desc \*desc, uint16\_t mrl, uint8\_t ibi\_len)

Set the Maximum Read Length (MRL) for a device.

[i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90)

i3c\_bus\_mode

I3C bus mode.

**Definition** i3c.h:227

[i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)

static int i3c\_recover\_bus(const struct device \*dev)

Attempt bus recovery on the I3C bus.

**Definition** i3c.h:1518

[i3c\_configure\_target](group__i3c__interface.md#ga7dfa33c7bdbe7e6607af61fe04bcb985)

static int i3c\_configure\_target(const struct device \*dev, struct i3c\_config\_target \*config)

Get the target device configuration for an I3C device.

**Definition** i3c.h:1425

[i3c\_bus\_setmwl](group__i3c__interface.md#ga8002de8239c4a0d1178fba27092a1254)

int i3c\_bus\_setmwl(struct i3c\_device\_desc \*desc, uint16\_t mwl)

Set the Maximum Write Length (MWL) for a device.

[i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)

static int i3c\_config\_get(const struct device \*dev, enum i3c\_config\_type type, void \*config)

Get configuration of the I3C hardware.

**Definition** i3c.h:1451

[i3c\_bus\_getacccr](group__i3c__interface.md#ga8d4356b56d8414e62b5a9931ffc7ab8b)

int i3c\_bus\_getacccr(struct i3c\_device\_desc \*desc)

Retrieve the Active Controller's Dynamic Address (ACCCR).

[i3c\_bus\_getmwl](group__i3c__interface.md#ga8d4da712075ee05896bcd7dde49cd827)

int i3c\_bus\_getmwl(struct i3c\_device\_desc \*desc)

Retrieve the Maximum Write Length (MWL) of a device.

[i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)

int i3c\_detach\_i2c\_device(struct i3c\_i2c\_device\_desc \*target)

Detach I2C Device.

[i3c\_config\_get\_target](group__i3c__interface.md#ga8ef11af673e94646806e093504cfb01f)

static int i3c\_config\_get\_target(const struct device \*dev, struct i3c\_config\_target \*config)

Get the target device configuration for an I3C device.

**Definition** i3c.h:1501

[I3C\_BCR\_DEVICE\_ROLE](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)

#define I3C\_BCR\_DEVICE\_ROLE(bcr)

Device Role.

**Definition** i3c.h:141

[i3c\_iodev\_submit\_fallback](group__i3c__interface.md#ga909d531941cd81850f4a05c51646690d)

void i3c\_iodev\_submit\_fallback(const struct device \*dev, struct rtio\_iodev\_sqe \*iodev\_sqe)

Fallback submit implementation.

[i3c\_config\_get\_controller](group__i3c__interface.md#ga96cd903b4a676c5943c43cc7b27af867)

static int i3c\_config\_get\_controller(const struct device \*dev, struct i3c\_config\_controller \*config)

Get the controller device configuration for an I3C device.

**Definition** i3c.h:1479

[i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)

struct i3c\_device\_desc \* i3c\_dev\_list\_find(const struct i3c\_dev\_list \*dev\_list, const struct i3c\_device\_id \*id)

Find a I3C target device descriptor by ID.

[i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)

int i3c\_bus\_init(const struct device \*dev, const struct i3c\_dev\_list \*i3c\_dev\_list)

Generic helper function to perform bus initialization.

[i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)

int i3c\_do\_ccc(const struct device \*dev, struct i3c\_ccc\_payload \*payload)

Send CCC to the bus.

[i3c\_bus\_getdcr](group__i3c__interface.md#gaab2801ccc00e9891269709ecc34f4f7c)

int i3c\_bus\_getdcr(struct i3c\_device\_desc \*desc)

Retrieve the Device Characteristics Register (DCR) of a device.

[i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)

int i3c\_device\_basic\_info\_get(struct i3c\_device\_desc \*target)

Get basic information from device and update device descriptor.

[i3c\_odd\_parity](group__i3c__interface.md#gaaf7736a8895de826f7fac1a9ecf0d7ea)

uint8\_t i3c\_odd\_parity(uint8\_t p)

Calculate odd parity.

[i3c\_rtio\_copy](group__i3c__interface.md#gab46a231442a7bf60e7e28ca2f52d25fc)

struct rtio\_sqe \* i3c\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct i3c\_msg \*msgs, uint8\_t num\_msgs)

Copy the i3c\_msgs into a set of RTIO requests.

[i3c\_bus\_setaasa](group__i3c__interface.md#gab6735824952836a1ac06745b21e2b534)

int i3c\_bus\_setaasa(const struct device \*dev)

Assign static addresses as dynamic addresses for all devices on the bus.

[i3c\_device\_desc\_alloc](group__i3c__interface.md#gab8e12d10528686040707f4aae502df98)

struct i3c\_device\_desc \* i3c\_device\_desc\_alloc(void)

Allocate memory for a i3c device descriptor.

[i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)

static int i3c\_do\_daa(const struct device \*dev)

Perform Dynamic Address Assignment on the I3C bus.

**Definition** i3c.h:1660

[i3c\_i2c\_device\_desc\_in\_pool](group__i3c__interface.md#gabfebceaa3e6f6f255352b8dcc3e7f9b1)

bool i3c\_i2c\_device\_desc\_in\_pool(struct i3c\_i2c\_device\_desc \*desc)

Report if the i3c i2c device descriptor was from a mem slab.

[i3c\_bus\_getbcr](group__i3c__interface.md#gac8c0ec6eb11030183be10fb541e1e561)

int i3c\_bus\_getbcr(struct i3c\_device\_desc \*desc)

Retrieve the Bus Characteristics Register (BCR) of a device.

[i3c\_iodev\_api](group__i3c__interface.md#gace1f8f10af2d87bb5a17441645030833)

const struct rtio\_iodev\_api i3c\_iodev\_api

[i3c\_bus\_setmwl\_all](group__i3c__interface.md#gad3a4bf3cfc1b150c19ff1186cc8e3e2a)

int i3c\_bus\_setmwl\_all(const struct device \*dev, uint16\_t mwl)

Set the Maximum Write Length (MWL) for all devices on the bus.

[I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)

#define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE

IBI Payload bit.

**Definition** i3c.h:98

[i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)

int i3c\_reattach\_i3c\_device(struct i3c\_device\_desc \*target, uint8\_t old\_dyn\_addr)

Reattach I3C device.

[i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073)

i3c\_data\_rate

I3C data rate.

**Definition** i3c.h:276

[i3c\_configure\_controller](group__i3c__interface.md#gaeca24930774ecc2dcbf2240d48ae19c5)

static int i3c\_configure\_controller(const struct device \*dev, struct i3c\_config\_controller \*config)

Get the controller device configuration for an I3C device.

**Definition** i3c.h:1403

[i3c\_dev\_list\_i3c\_static\_addr\_find](group__i3c__interface.md#gaecbb16ce8edcd9ad7a7afcfb1251aa76)

struct i3c\_device\_desc \* i3c\_dev\_list\_i3c\_static\_addr\_find(const struct device \*dev, uint8\_t addr)

Find a I3C target device descriptor by static address.

[i3c\_device\_controller\_handoff](group__i3c__interface.md#gaedf58fdd96f38f103f8defe221427b6f)

int i3c\_device\_controller\_handoff(struct i3c\_device\_desc \*target, bool requested)

Perform Controller Handoff.

[i3c\_device\_desc\_in\_pool](group__i3c__interface.md#gaf2c8afec987322be8dfd4fb053fac61b)

bool i3c\_device\_desc\_in\_pool(struct i3c\_device\_desc \*desc)

Report if the i3c device descriptor was from a mem slab.

[i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#gafac78dca571ff7daa34fca0cfa7cc3b1)

struct i3c\_i2c\_device\_desc \* i3c\_dev\_list\_i2c\_addr\_find(const struct device \*dev, uint16\_t addr)

Find a I2C target device descriptor by address.

[I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00)

@ I3C\_CONFIG\_TARGET

**Definition** i3c.h:439

[I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017)

@ I3C\_CONFIG\_CUSTOM

**Definition** i3c.h:440

[I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5)

@ I3C\_CONFIG\_CONTROLLER

**Definition** i3c.h:438

[I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4)

@ I3C\_I2C\_SPEED\_INVALID

**Definition** i3c.h:268

[I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967)

@ I3C\_I2C\_SPEED\_MAX

**Definition** i3c.h:267

[I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea)

@ I3C\_I2C\_SPEED\_FMPLUS

I2C FM+ mode.

**Definition** i3c.h:265

[I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1)

@ I3C\_I2C\_SPEED\_FM

I2C FM mode.

**Definition** i3c.h:262

[I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)

@ I3C\_BUS\_MODE\_INVALID

**Definition** i3c.h:252

[I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445)

@ I3C\_BUS\_MODE\_PURE

Only I3C devices are on the bus.

**Definition** i3c.h:229

[I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434)

@ I3C\_BUS\_MODE\_MIXED\_FAST

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:235

[I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697)

@ I3C\_BUS\_MODE\_MAX

**Definition** i3c.h:251

[I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722)

@ I3C\_BUS\_MODE\_MIXED\_LIMITED

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:242

[I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a)

@ I3C\_BUS\_MODE\_MIXED\_SLOW

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:249

[I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725)

@ I3C\_DATA\_RATE\_MAX

**Definition** i3c.h:292

[I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)

@ I3C\_DATA\_RATE\_INVALID

**Definition** i3c.h:293

[I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d)

@ I3C\_DATA\_RATE\_HDR\_TSP

High Data Rate - Ternary Symbol for Pure Bus.

**Definition** i3c.h:287

[I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301)

@ I3C\_DATA\_RATE\_HDR\_DDR

High Data Rate - Double Data Rate messaging.

**Definition** i3c.h:281

[I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9)

@ I3C\_DATA\_RATE\_SDR

Single Data Rate messaging.

**Definition** i3c.h:278

[I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590)

@ I3C\_DATA\_RATE\_HDR\_TSL

High Data Rate - Ternary Symbol Legacy-inclusive-Bus.

**Definition** i3c.h:284

[I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed)

@ I3C\_DATA\_RATE\_HDR\_BT

High Data Rate - Bulk Transport.

**Definition** i3c.h:290

[i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)

int i3c\_transfer(struct i3c\_device\_desc \*target, struct i3c\_msg \*msgs, uint8\_t num\_msgs)

Perform data transfer from the controller to a I3C target device.

[I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)

#define I3C\_MSG\_STOP

Send STOP after this message.

**Definition** i3c.h:317

[i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)

static int i3c\_write\_read(struct i3c\_device\_desc \*target, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)

Write then read data from an I3C target device.

**Definition** i3c.h:2012

[i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)

static int i3c\_burst\_read(struct i3c\_device\_desc \*target, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)

Read multiple bytes from an internal address of an I3C target device.

**Definition** i3c.h:2050

[i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)

static int i3c\_reg\_update\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)

Update internal register of an I3C target device.

**Definition** i3c.h:2167

[i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)

void i3c\_dump\_msgs(const char \*name, const struct i3c\_msg \*msgs, uint8\_t num\_msgs, struct i3c\_device\_desc \*target)

Dump out an I3C message.

[I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)

#define I3C\_MSG\_READ

Read message from I3C bus.

**Definition** i3c.h:310

[I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)

#define I3C\_MSG\_WRITE

Write message to I3C bus.

**Definition** i3c.h:307

[i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)

static int i3c\_reg\_read\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t \*value)

Read internal register of an I3C target device.

**Definition** i3c.h:2116

[i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)

static int i3c\_write(struct i3c\_device\_desc \*target, const uint8\_t \*buf, uint32\_t num\_bytes)

Write a set amount of data to an I3C target device.

**Definition** i3c.h:1954

[i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)

static int i3c\_read(struct i3c\_device\_desc \*target, uint8\_t \*buf, uint32\_t num\_bytes)

Read a set amount of data from an I3C target device.

**Definition** i3c.h:1981

[I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)

#define I3C\_MSG\_RESTART

RESTART I3C transaction for this message.

**Definition** i3c.h:328

[i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)

static int i3c\_burst\_write(struct i3c\_device\_desc \*target, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)

Write multiple bytes to an internal address of an I3C target device.

**Definition** i3c.h:2080

[i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)

static int i3c\_reg\_write\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t value)

Write internal register of an I3C target device.

**Definition** i3c.h:2141

[rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)

static void rtio\_iodev\_sqe\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submissions completion with error.

**Definition** rtio.h:1285

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[hdr\_ddr.h](hdr__ddr_8h.md)

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[ibi.h](ibi_8h.md)

[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)

int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[slist.h](slist_8h.md)

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

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[i3c\_addr\_slots](structi3c__addr__slots.md)

Structure to keep track of addresses on I3C bus.

**Definition** addresses.h:58

[i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md)

Payload for DEFTGTS CCC (Define List of Targets).

**Definition** ccc.h:477

[i3c\_ccc\_payload](structi3c__ccc__payload.md)

Payload structure for one CCC transaction.

**Definition** ccc.h:283

[i3c\_config\_controller](structi3c__config__controller.md)

Configuration parameters for I3C hardware to act as controller.

**Definition** i3c.h:446

[i3c\_config\_controller::i3c](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b)

uint32\_t i3c

SCL frequency (in Hz) for I3C transfers.

**Definition** i3c.h:455

[i3c\_config\_controller::supported\_hdr](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d)

uint8\_t supported\_hdr

Bit mask of supported HDR modes (0 - 7).

**Definition** i3c.h:467

[i3c\_config\_controller::is\_secondary](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36)

bool is\_secondary

True if the controller is to be the secondary controller of the bus.

**Definition** i3c.h:451

[i3c\_config\_controller::i2c](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd)

uint32\_t i2c

SCL frequency (in Hz) for I2C transfers.

**Definition** i3c.h:458

[i3c\_config\_controller::scl](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b)

struct i3c\_config\_controller::@056135366137020063162136324011126070110331100007 scl

[i3c\_config\_custom](structi3c__config__custom.md)

Custom I3C configuration parameters.

**Definition** i3c.h:478

[i3c\_config\_custom::ptr](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd)

void \* ptr

Pointer to configuration parameter.

**Definition** i3c.h:492

[i3c\_config\_custom::id](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31)

uint32\_t id

ID of the configuration parameter.

**Definition** i3c.h:480

[i3c\_config\_custom::val](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340)

uintptr\_t val

Value of configuration parameter.

**Definition** i3c.h:484

[i3c\_config\_target](structi3c__config__target.md)

Configuration parameters for I3C hardware to act as target device.

**Definition** target\_device.h:36

[i3c\_dev\_attached\_list](structi3c__dev__attached__list.md)

Structure for describing attached devices for a controller.

**Definition** i3c.h:1128

[i3c\_dev\_attached\_list::i3c](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad)

sys\_slist\_t i3c

Linked list of attached I3C devices.

**Definition** i3c.h:1141

[i3c\_dev\_attached\_list::i2c](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a)

sys\_slist\_t i2c

Linked list of attached I2C devices.

**Definition** i3c.h:1146

[i3c\_dev\_attached\_list::addr\_slots](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474)

struct i3c\_addr\_slots addr\_slots

Address slots:

**Definition** i3c.h:1135

[i3c\_dev\_attached\_list::devices](structi3c__dev__attached__list.md#adf700818ee21cf60f84e2aa6946d19f4)

struct i3c\_dev\_attached\_list::@246075137236124205333215212253313057323215125055 devices

[i3c\_dev\_list](structi3c__dev__list.md)

Structure for describing known devices for a controller.

**Definition** i3c.h:1158

[i3c\_dev\_list::i2c](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e)

struct i3c\_i2c\_device\_desc \*const i2c

Pointer to array of known I2C devices.

**Definition** i3c.h:1167

[i3c\_dev\_list::num\_i3c](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985)

const uint8\_t num\_i3c

Number of I3C devices in array.

**Definition** i3c.h:1172

[i3c\_dev\_list::i3c](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce)

struct i3c\_device\_desc \*const i3c

Pointer to array of known I3C devices.

**Definition** i3c.h:1162

[i3c\_dev\_list::num\_i2c](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318)

const uint8\_t num\_i2c

Number of I2C devices in array.

**Definition** i3c.h:1177

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:894

[i3c\_device\_desc::maxwr](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9)

uint8\_t maxwr

Maximum Write Speed.

**Definition** i3c.h:974

[i3c\_device\_desc::init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5)

const uint8\_t init\_dynamic\_addr

Initial dynamic address.

**Definition** i3c.h:929

[i3c\_device\_desc::getcap1](structi3c__device__desc.md#a062f86dec32de3b9e899b096df47d828)

uint8\_t getcap1

I3C v1.1+ GETCAPS1 (I3C\_CCC\_GETCAPS1\_\*).

**Definition** i3c.h:1014

[i3c\_device\_desc::static\_addr](structi3c__device__desc.md#a078901f1dc853dabf6503407d78735c0)

uint8\_t static\_addr

Static address for this target device.

**Definition** i3c.h:918

[i3c\_device\_desc::getcap2](structi3c__device__desc.md#a089da4f6eaf2b80fc689bb89d527d330)

uint8\_t getcap2

GETCAPS2 (I3C\_CCC\_GETCAPS2\_\*).

**Definition** i3c.h:1024

[i3c\_device\_desc::crcaps2](structi3c__device__desc.md#a08e4524060eddc0dc15c985c1c59b9f1)

uint8\_t crcaps2

CRCAPS2.

**Definition** i3c.h:1065

[i3c\_device\_desc::max\_read\_turnaround](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb)

uint32\_t max\_read\_turnaround

Maximum Read turnaround time in microseconds.

**Definition** i3c.h:977

[i3c\_device\_desc::getcap4](structi3c__device__desc.md#a1314218c6f6a429ccedb9975b9e02a90)

uint8\_t getcap4

GETCAPS4.

**Definition** i3c.h:1043

[i3c\_device\_desc::pid](structi3c__device__desc.md#a153ff108d8cf523d60aad3534d06f88e)

uint64\_t pid

Device Provisioned ID.

**Definition** i3c.h:904

[i3c\_device\_desc::max\_ibi](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9)

uint8\_t max\_ibi

Maximum IBI Payload Size.

**Definition** i3c.h:988

[i3c\_device\_desc::ibi\_cb](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265)

i3c\_target\_ibi\_cb\_t ibi\_cb

In-Band Interrupt (IBI) callback.

**Definition** i3c.h:1080

[i3c\_device\_desc::data\_length](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835)

struct i3c\_device\_desc::@374166210137153225365322260210124156025250214226 data\_length

[i3c\_device\_desc::mwl](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed)

uint16\_t mwl

Maximum Write Length.

**Definition** i3c.h:985

[i3c\_device\_desc::crhdly1](structi3c__device__desc.md#a3fc3b3f1cf396eaf164612e7b667b37a)

uint8\_t crhdly1

Controller Handoff Delay Parameters.

**Definition** i3c.h:992

[i3c\_device\_desc::getcap3](structi3c__device__desc.md#a47af0b36448dfec8307b25a31712428e)

uint8\_t getcap3

GETCAPS3 (I3C\_CCC\_GETCAPS3\_\*).

**Definition** i3c.h:1037

[i3c\_device\_desc::dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0)

uint8\_t dynamic\_addr

Dynamic Address for this target device used for communication.

**Definition** i3c.h:953

[i3c\_device\_desc::crcaps1](structi3c__device__desc.md#a5ab881cf948d10cfa9e1542b4b5a0f34)

uint8\_t crcaps1

CRCAPS1.

**Definition** i3c.h:1055

[i3c\_device\_desc::flags](structi3c__device__desc.md#a5cc5f0ffdd173478275a6b5f651d86a3)

const uint8\_t flags

Device Flags.

**Definition** i3c.h:938

[i3c\_device\_desc::crcaps](structi3c__device__desc.md#a5dcad2306094a3ee32a20051f7eafa9a)

struct i3c\_device\_desc::@171122044300150030070232076155234262120067102161 crcaps

[i3c\_device\_desc::getcaps](structi3c__device__desc.md#a7e44bedd1aa032d661335f8ec0a0d2e2)

struct i3c\_device\_desc::@025161371003043020356247061065002050371177151366 getcaps

Describes advanced (Target) capabilities and features.

[i3c\_device\_desc::data\_speed](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500)

struct i3c\_device\_desc::@011056325341036010112127327312366216151020376366 data\_speed

[i3c\_device\_desc::node](structi3c__device__desc.md#a965edbd5d74c06773e190a14d4f6e3cd)

sys\_snode\_t node

**Definition** i3c.h:895

[i3c\_device\_desc::bus](structi3c__device__desc.md#aaa1a96e29bf98028ad6ee4c1aae79809)

const struct device \* bus

I3C bus to which this target device is attached.

**Definition** i3c.h:898

[i3c\_device\_desc::mrl](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e)

uint16\_t mrl

Maximum Read Length.

**Definition** i3c.h:982

[i3c\_device\_desc::maxrd](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523)

uint8\_t maxrd

Maximum Read Speed.

**Definition** i3c.h:971

[i3c\_device\_desc::gethdrcap](structi3c__device__desc.md#ae01bc68ac8154238d85bbf44dc06dfb7)

uint8\_t gethdrcap

I3C v1.0 HDR Capabilities (I3C\_CCC\_GETCAPS1\_\*).

**Definition** i3c.h:1004

[i3c\_device\_desc::bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21)

uint8\_t bcr

Bus Characteristic Register (BCR).

**Definition** i3c.h:959

[i3c\_device\_desc::dcr](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c)

uint8\_t dcr

Device Characteristic Register (DCR).

**Definition** i3c.h:967

[i3c\_device\_desc::dev](structi3c__device__desc.md#af0466893f56f9aebdaa7677a9a0076ed)

const struct device \* dev

Device driver instance of the I3C device.

**Definition** i3c.h:901

[i3c\_device\_id](structi3c__device__id.md)

Structure used for matching I3C devices.

**Definition** i3c.h:860

[i3c\_device\_id::pid](structi3c__device__id.md#a78a8fb4cda85690d866a8e03b982666f)

uint64\_t pid

Device Provisioned ID.

**Definition** i3c.h:862

[i3c\_driver\_config](structi3c__driver__config.md)

This structure is common to all I3C drivers and is expected to be the first element in the object poi...

**Definition** i3c.h:1185

[i3c\_driver\_config::primary\_controller\_da](structi3c__driver__config.md#a52b9e5a36b65fbadc7fd2369ff184271)

uint8\_t primary\_controller\_da

I3C Primary Controller Dynamic Address.

**Definition** i3c.h:1191

[i3c\_driver\_config::dev\_list](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193)

struct i3c\_dev\_list dev\_list

I3C/I2C device list struct.

**Definition** i3c.h:1188

[i3c\_driver\_data](structi3c__driver__data.md)

This structure is common to all I3C drivers and is expected to be the first element in the driver's s...

**Definition** i3c.h:1206

[i3c\_driver\_data::ctrl\_config](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb)

struct i3c\_config\_controller ctrl\_config

Controller Configuration.

**Definition** i3c.h:1208

[i3c\_driver\_data::deftgts](structi3c__driver__data.md#a1f1e3c1017b6214486474078b7d948f7)

struct i3c\_ccc\_deftgts \* deftgts

Received DEFTGTS Pointer.

**Definition** i3c.h:1214

[i3c\_driver\_data::deftgts\_refreshed](structi3c__driver__data.md#a968fe84e8de0ac443228ebd20493c49c)

bool deftgts\_refreshed

DEFTGTS refreshed.

**Definition** i3c.h:1217

[i3c\_driver\_data::attached\_dev](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901)

struct i3c\_dev\_attached\_list attached\_dev

Attached I3C/I2C devices and addresses.

**Definition** i3c.h:1211

[i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md)

Structure describing a I2C device on I3C bus.

**Definition** i3c.h:1097

[i3c\_i2c\_device\_desc::bus](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2)

const struct device \* bus

I3C bus to which this I2C device is attached.

**Definition** i3c.h:1101

[i3c\_i2c\_device\_desc::lvr](structi3c__i2c__device__desc.md#a610c28ac5e56b540415d48dfabe46dad)

uint8\_t lvr

Legacy Virtual Register (LVR).

**Definition** i3c.h:1110

[i3c\_i2c\_device\_desc::addr](structi3c__i2c__device__desc.md#a6148be0b55e526b31cb493d697075670)

uint16\_t addr

Static address for this I2C device.

**Definition** i3c.h:1104

[i3c\_i2c\_device\_desc::node](structi3c__i2c__device__desc.md#acfcf72db311b19e479e9147ce5257245)

sys\_snode\_t node

**Definition** i3c.h:1098

[i3c\_ibi](structi3c__ibi.md)

Struct for IBI request.

**Definition** ibi.h:58

[i3c\_iodev\_data](structi3c__iodev__data.md)

**Definition** i3c.h:2669

[i3c\_iodev\_data::bus](structi3c__iodev__data.md#a22c368ac3cd8b7b8a8770de3b37afb07)

const struct device \* bus

**Definition** i3c.h:2670

[i3c\_iodev\_data::dev\_id](structi3c__iodev__data.md#a3d4146137def71cbb84d1ae3cef67c55)

const struct i3c\_device\_id dev\_id

**Definition** i3c.h:2671

[i3c\_msg](structi3c__msg.md)

One I3C Message.

**Definition** i3c.h:393

[i3c\_msg::flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217)

uint8\_t flags

Flags for this message.

**Definition** i3c.h:418

[i3c\_msg::hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9)

uint8\_t hdr\_mode

HDR mode (I3C\_MSG\_HDR\_MODE\*) for transfer if any I3C\_MSG\_HDR\_\* is set in flags.

**Definition** i3c.h:426

[i3c\_msg::num\_xfer](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5)

uint32\_t num\_xfer

Total number of bytes transferred.

**Definition** i3c.h:407

[i3c\_msg::buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff)

uint8\_t \* buf

Data buffer in bytes.

**Definition** i3c.h:395

[i3c\_msg::hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b)

uint8\_t hdr\_cmd\_code

HDR command code field (7-bit) for HDR-DDR, HDR-TSP and HDR-TSL.

**Definition** i3c.h:429

[i3c\_msg::len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0)

uint32\_t len

Length of buffer in bytes.

**Definition** i3c.h:398

[i3c\_msg::err](structi3c__msg.md#ae43cb150bcdec5f0bf654c794757f756)

enum i3c\_sdr\_controller\_error\_types err

SDR Error Type.

**Definition** i3c.h:415

[i3c\_target\_config](structi3c__target__config.md)

Structure describing a device that supports the I3C target API.

**Definition** target\_device.h:102

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4073

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:524

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:514

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:515

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:539

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:544

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:295

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:304

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:418

[util.h](sys_2util_8h.md)

Misc utilities.

[target\_device.h](target__device_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c.h](i3c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
