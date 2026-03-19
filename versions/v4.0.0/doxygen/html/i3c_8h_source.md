---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/i3c_8h_source.html
original_path: doxygen/html/i3c_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

26#include <[zephyr/drivers/i3c/ccc.h](ccc_8h.md)>

27#include <[zephyr/drivers/i3c/devicetree.h](drivers_2i3c_2devicetree_8h.md)>

28#include <[zephyr/drivers/i3c/ibi.h](ibi_8h.md)>

29#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

30#include <[zephyr/sys/slist.h](slist_8h.md)>

31#include <[zephyr/sys/util.h](sys_2util_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

77

[ 84](group__i3c__interface.md#ga91ebe41a421dc05ae7f1de1ce2dd314f)#define I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT BIT(0)

85

[ 87](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)#define I3C\_BCR\_IBI\_REQUEST\_CAPABLE BIT(1)

88

[ 96](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)#define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE BIT(2)

97

[ 104](group__i3c__interface.md#ga7b9fea89457022d8012ac25133bf63db)#define I3C\_BCR\_OFFLINE\_CAPABLE BIT(3)

105

[ 112](group__i3c__interface.md#ga69dc4a5004da568684a3c72046bba870)#define I3C\_BCR\_VIRTUAL\_TARGET BIT(4)

113

[ 121](group__i3c__interface.md#ga07018705794753d0d0d65131f011e097)#define I3C\_BCR\_ADV\_CAPABILITIES BIT(5)

122

[ 124](group__i3c__interface.md#ga867b4b12b23c803b86b57dcc86b9e604)#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET 0U

125

[ 127](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852)#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE 1U

128

[ 130](group__i3c__interface.md#ga25721c9963040c84b7f5bbb48bb87b44)#define I3C\_BCR\_DEVICE\_ROLE\_MASK GENMASK(7U, 6U)

131

[ 139](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)#define I3C\_BCR\_DEVICE\_ROLE(bcr) \

140 FIELD\_GET(I3C\_BCR\_DEVICE\_ROLE\_MASK, (bcr))

141

143

163

[ 165](group__i3c__interface.md#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)#define I3C\_LVR\_I2C\_FM\_PLUS\_MODE 0

166

[ 168](group__i3c__interface.md#ga053945f5f67ee3c681de2c9362e69c39)#define I3C\_LVR\_I2C\_FM\_MODE 1

169

[ 171](group__i3c__interface.md#gaf073cc9ea1a68c57663c36de12554876)#define I3C\_LVR\_I2C\_MODE\_MASK BIT(4)

172

[ 180](group__i3c__interface.md#gaaf759805bb5824a89612b292a4439982)#define I3C\_LVR\_I2C\_MODE(lvr) \

181 FIELD\_GET(I3C\_LVR\_I2C\_MODE\_MASK, (lvr))

182

[ 189](group__i3c__interface.md#ga4319835ddb6b5984b21f5a5a2f14ae75)#define I3C\_LVR\_I2C\_DEV\_IDX\_0 0

190

[ 197](group__i3c__interface.md#ga02a21af4c679a81b8290beea30c8ef40)#define I3C\_LVR\_I2C\_DEV\_IDX\_1 1

198

[ 205](group__i3c__interface.md#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)#define I3C\_LVR\_I2C\_DEV\_IDX\_2 2

206

[ 208](group__i3c__interface.md#ga50fa249b36b91d56e49004548a1c7520)#define I3C\_LVR\_I2C\_DEV\_IDX\_MASK GENMASK(7U, 5U)

209

[ 217](group__i3c__interface.md#gae7afa509b1d63374c551bcdaf84c5dd1)#define I3C\_LVR\_I2C\_DEV\_IDX(lvr) \

218 FIELD\_GET(I3C\_LVR\_I2C\_DEV\_IDX\_MASK, (lvr))

219

221

[ 225](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90)enum [i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90) {

[ 227](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445) [I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445),

228

[ 233](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434) [I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434),

234

[ 240](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722) [I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722),

241

[ 247](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a) [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a),

248

[ 249](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) [I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) = [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a),

[ 250](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c) [I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c),

251};

252

[ 258](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6)enum [i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6) {

[ 260](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1) [I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1),

261

[ 263](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea) [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea),

264

[ 265](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) [I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) = [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea),

[ 266](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4) [I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4),

267};

268

[ 274](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073)enum [i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073) {

[ 276](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9) [I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9),

277

[ 279](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301) [I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301),

280

[ 282](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590) [I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590),

283

[ 285](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d) [I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d),

286

[ 288](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed) [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed),

289

[ 290](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) [I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) = [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed),

[ 291](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a) [I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a),

292};

293

[ 304](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870)enum [i3c\_sdr\_controller\_error\_codes](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870) {

[ 306](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282) [I3C\_ERROR\_CE0](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282),

307

[ 309](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb) [I3C\_ERROR\_CE1](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb),

310

[ 312](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574) [I3C\_ERROR\_CE2](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574),

313

[ 315](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f) [I3C\_ERROR\_CE3](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f),

316

[ 318](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502) [I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502),

319

[ 321](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707) [I3C\_ERROR\_CE\_NONE](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707),

322

[ 323](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7) [I3C\_ERROR\_CE\_MAX](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7) = [I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502),

[ 324](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0) [I3C\_ERROR\_CE\_INVALID](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0),

325};

326

[ 337](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c)enum [i3c\_sdr\_target\_error\_codes](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c) {

[ 342](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a) [I3C\_ERROR\_TE0](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a),

343

[ 345](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe) [I3C\_ERROR\_TE1](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe),

346

[ 348](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e) [I3C\_ERROR\_TE2](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e),

349

[ 351](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3) [I3C\_ERROR\_TE3](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3),

352

[ 354](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd) [I3C\_ERROR\_TE4](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd),

355

[ 357](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f) [I3C\_ERROR\_TE5](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f),

358

[ 360](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e) [I3C\_ERROR\_TE6](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e),

361

[ 363](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285) [I3C\_ERROR\_DBR](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285),

364

[ 366](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791) [I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791),

367

[ 369](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a) [I3C\_ERROR\_TE\_NONE](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a),

370

[ 371](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7) [I3C\_ERROR\_TE\_MAX](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7) = [I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791),

[ 372](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a) [I3C\_ERROR\_TE\_INVALID](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a),

373};

374

380

381/\*

382 \* I3C\_MSG\_\* are I3C Message flags.

383 \*/

384

[ 386](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)#define I3C\_MSG\_WRITE (0U << 0U)

387

[ 389](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)#define I3C\_MSG\_READ BIT(0)

390

392#define I3C\_MSG\_RW\_MASK BIT(0)

394

[ 396](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)#define I3C\_MSG\_STOP BIT(1)

397

[ 407](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)#define I3C\_MSG\_RESTART BIT(2)

408

[ 410](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38)#define I3C\_MSG\_HDR BIT(3)

411

[ 413](group__i3c__transfer__api.md#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)#define I3C\_MSG\_NBCH BIT(4)

414

[ 416](group__i3c__transfer__api.md#ga18aac0862826869f94e5a71670debcb0)#define I3C\_MSG\_HDR\_MODE0 BIT(0)

417

[ 419](group__i3c__transfer__api.md#ga8eb3dc48237dfdb25fde40a1efa03241)#define I3C\_MSG\_HDR\_MODE1 BIT(1)

420

[ 422](group__i3c__transfer__api.md#ga15cbd61e7d509c28b22fbc9e0844cb23)#define I3C\_MSG\_HDR\_MODE2 BIT(2)

423

[ 425](group__i3c__transfer__api.md#ga162fb9ab0e4ed7f8feb0e91d183a88e7)#define I3C\_MSG\_HDR\_MODE3 BIT(3)

426

[ 428](group__i3c__transfer__api.md#gabe45532238bc15672f6454dac70d20cf)#define I3C\_MSG\_HDR\_MODE4 BIT(4)

429

[ 431](group__i3c__transfer__api.md#gac712daa606d0c51ce523d7a687821282)#define I3C\_MSG\_HDR\_MODE5 BIT(5)

432

[ 434](group__i3c__transfer__api.md#ga7654c1947e13c019c24bf12712b0773b)#define I3C\_MSG\_HDR\_MODE6 BIT(6)

435

[ 437](group__i3c__transfer__api.md#ga08df1d8df82226d1f23b4cc923584672)#define I3C\_MSG\_HDR\_MODE7 BIT(7)

438

[ 440](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a)#define I3C\_MSG\_HDR\_DDR I3C\_MSG\_HDR\_MODE0

441

[ 443](group__i3c__transfer__api.md#gaa61322f770db296b5ab718c48ab960d3)#define I3C\_MSG\_HDR\_TSP I3C\_MSG\_HDR\_MODE1

444

[ 446](group__i3c__transfer__api.md#gac43a2d266f3a23fd6dfa11405f3fd6f3)#define I3C\_MSG\_HDR\_TSL I3C\_MSG\_HDR\_MODE2

447

[ 449](group__i3c__transfer__api.md#ga8b2fdcb827cbd3325f124a1c615698e7)#define I3C\_MSG\_HDR\_BT I3C\_MSG\_HDR\_MODE3

450

452

457

[ 472](structi3c__msg.md)struct [i3c\_msg](structi3c__msg.md) {

[ 474](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

475

[ 477](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0);

478

[ 486](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_xfer](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5);

487

[ 489](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217);

490

[ 497](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9);

498

[ 500](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b);

501};

502

504

[ 508](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) {

[ 509](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5) [I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5),

[ 510](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00) [I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00),

[ 511](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017) [I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017),

512};

513

[ 517](structi3c__config__controller.md)struct [i3c\_config\_controller](structi3c__config__controller.md) {

[ 522](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36) bool [is\_secondary](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36);

523

524 struct {

[ 526](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i3c](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b);

527

[ 529](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd);

[ 530](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b) } [scl](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b);

531

[ 538](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_hdr](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d);

539};

540

[ 549](structi3c__config__custom.md)struct [i3c\_config\_custom](structi3c__config__custom.md) {

[ 551](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31);

552

553 union {

[ 555](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [val](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340);

556

[ 563](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd) void \*[ptr](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd);

564 };

565};

566

573struct [i3c\_device\_desc](structi3c__device__desc.md);

574struct [i3c\_device\_id](structi3c__device__id.md);

575struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md);

576struct [i3c\_target\_config](structi3c__target__config.md);

577

578\_\_subsystem struct i3c\_driver\_api {

588 struct i2c\_driver\_api i2c\_api;

589

602 int (\*configure)(const struct device \*dev,

603 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config);

604

617 int (\*config\_get)(const struct device \*dev,

618 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config);

619

631 int (\*recover\_bus)(const struct device \*dev);

632

645 int (\*attach\_i3c\_device)(const struct device \*dev,

646 struct i3c\_device\_desc \*target);

647

661 int (\*reattach\_i3c\_device)(const struct device \*dev,

662 struct i3c\_device\_desc \*target,

663 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr);

664

677 int (\*detach\_i3c\_device)(const struct device \*dev,

678 struct i3c\_device\_desc \*target);

679

692 int (\*attach\_i2c\_device)(const struct device \*dev,

693 struct i3c\_i2c\_device\_desc \*target);

694

707 int (\*detach\_i2c\_device)(const struct device \*dev,

708 struct i3c\_i2c\_device\_desc \*target);

709

721 int (\*do\_daa)(const struct device \*dev);

722

735 int (\*do\_ccc)(const struct device \*dev,

736 struct i3c\_ccc\_payload \*payload);

737

750 int (\*i3c\_xfers)(const struct device \*dev,

751 struct i3c\_device\_desc \*target,

752 struct i3c\_msg \*msgs,

753 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

754

768 struct i3c\_device\_desc \*(\*i3c\_device\_find)(const struct device \*dev,

769 const struct i3c\_device\_id \*id);

770

783 int (\*ibi\_raise)(const struct device \*dev,

784 struct i3c\_ibi \*request);

785

798 int (\*ibi\_enable)(const struct device \*dev,

799 struct i3c\_device\_desc \*target);

800

813 int (\*ibi\_disable)(const struct device \*dev,

814 struct i3c\_device\_desc \*target);

815

831 int (\*target\_register)(const struct device \*dev,

832 struct i3c\_target\_config \*cfg);

833

849 int (\*target\_unregister)(const struct device \*dev,

850 struct i3c\_target\_config \*cfg);

851

868 int (\*target\_tx\_write)(const struct device \*dev,

869 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hdr\_mode);

870};

871

875

[ 879](structi3c__device__id.md)struct [i3c\_device\_id](structi3c__device__id.md) {

[ 881](structi3c__device__id.md#a254a43360f3eb8be2f62ed0ae48b8637) const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__device__id.md#a254a43360f3eb8be2f62ed0ae48b8637):48;

882};

883

[ 892](group__i3c__interface.md#gaed0df9802cc9b268abcfe4e877ebf498)#define I3C\_DEVICE\_ID(pid) \

893 { \

894 .pid = pid \

895 }

896

[ 913](structi3c__device__desc.md)struct [i3c\_device\_desc](structi3c__device__desc.md) {

[ 914](structi3c__device__desc.md#a965edbd5d74c06773e190a14d4f6e3cd) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__device__desc.md#a965edbd5d74c06773e190a14d4f6e3cd);

915

[ 917](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803) const struct [device](structdevice.md) \* const [bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803);

918

[ 920](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b) const struct [device](structdevice.md) \* const [dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b);

921

[ 923](structi3c__device__desc.md#ac82bd8eccc52a98df76506bd2bed3961) const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__device__desc.md#ac82bd8eccc52a98df76506bd2bed3961):48;

924

[ 937](structi3c__device__desc.md#a105221381d47f690219aa09a20936ae1) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__device__desc.md#a105221381d47f690219aa09a20936ae1);

938

[ 948](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5);

949

[ 956](structi3c__device__desc.md#af0905f27f1765c96fc3aaf601926d6ed) const bool [supports\_setaasa](structi3c__device__desc.md#af0905f27f1765c96fc3aaf601926d6ed);

957

[ 971](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0);

972

973#if defined(CONFIG\_I3C\_USE\_GROUP\_ADDR) || defined(\_\_DOXYGEN\_\_)

[ 982](structi3c__device__desc.md#a260730aef8862b2898ef6f65cf4956c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [group\_addr](structi3c__device__desc.md#a260730aef8862b2898ef6f65cf4956c4);

983#endif /\* CONFIG\_I3C\_USE\_GROUP\_ADDR \*/

984

[ 989](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21);

990

[ 997](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c);

998

999 struct {

[ 1001](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523);

1002

[ 1004](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9);

1005

[ 1007](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_read\_turnaround](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb);

[ 1008](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500) } [data\_speed](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500);

1009

1010 struct {

[ 1012](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mrl](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e);

1013

[ 1015](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mwl](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed);

1016

[ 1018](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ibi](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9);

[ 1019](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835) } [data\_length](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835);

1020

1022 struct {

1023 union {

[ 1031](structi3c__device__desc.md#ae01bc68ac8154238d85bbf44dc06dfb7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gethdrcap](structi3c__device__desc.md#ae01bc68ac8154238d85bbf44dc06dfb7);

1032

[ 1041](structi3c__device__desc.md#a062f86dec32de3b9e899b096df47d828) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap1](structi3c__device__desc.md#a062f86dec32de3b9e899b096df47d828);

1042 };

1043

[ 1051](structi3c__device__desc.md#a089da4f6eaf2b80fc689bb89d527d330) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap2](structi3c__device__desc.md#a089da4f6eaf2b80fc689bb89d527d330);

1052

[ 1064](structi3c__device__desc.md#a47af0b36448dfec8307b25a31712428e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap3](structi3c__device__desc.md#a47af0b36448dfec8307b25a31712428e);

1065

[ 1070](structi3c__device__desc.md#a1314218c6f6a429ccedb9975b9e02a90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [getcap4](structi3c__device__desc.md#a1314218c6f6a429ccedb9975b9e02a90);

[ 1071](structi3c__device__desc.md#a7e44bedd1aa032d661335f8ec0a0d2e2) } [getcaps](structi3c__device__desc.md#a7e44bedd1aa032d661335f8ec0a0d2e2);

1072

1077 void \*controller\_priv;

1079

1080#if defined(CONFIG\_I3C\_USE\_IBI) || defined(\_\_DOXYGEN\_\_)

[ 1085](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265) [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) [ibi\_cb](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265);

1086#endif /\* CONFIG\_I3C\_USE\_IBI \*/

1087};

1088

[ 1102](structi3c__i2c__device__desc.md)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) {

[ 1103](structi3c__i2c__device__desc.md#acfcf72db311b19e479e9147ce5257245) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__i2c__device__desc.md#acfcf72db311b19e479e9147ce5257245);

1104

[ 1106](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2) const struct [device](structdevice.md) \*[bus](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2);

1107

[ 1109](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d);

1110

[ 1115](structi3c__i2c__device__desc.md#a672aca260630deed5d8cdf90896d1115) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lvr](structi3c__i2c__device__desc.md#a672aca260630deed5d8cdf90896d1115);

1116

1121 void \*controller\_priv;

1123};

1124

[ 1133](structi3c__dev__attached__list.md)struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) {

[ 1140](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474) struct [i3c\_addr\_slots](structi3c__addr__slots.md) [addr\_slots](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474);

1141

1142 struct {

[ 1146](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [i3c](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad);

1147

[ 1151](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [i2c](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a);

[ 1152](structi3c__dev__attached__list.md#ad539b98ce41e781da53f1fd46b03df63) } [devices](structi3c__dev__attached__list.md#ad539b98ce41e781da53f1fd46b03df63);

1153};

1154

[ 1163](structi3c__dev__list.md)struct [i3c\_dev\_list](structi3c__dev__list.md) {

[ 1167](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce) struct [i3c\_device\_desc](structi3c__device__desc.md) \* const [i3c](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce);

1168

[ 1172](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e) struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* const [i2c](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e);

1173

[ 1177](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_i3c](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985);

1178

[ 1182](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_i2c](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318);

1183};

1184

[ 1190](structi3c__driver__config.md)struct [i3c\_driver\_config](structi3c__driver__config.md) {

[ 1192](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193) struct [i3c\_dev\_list](structi3c__dev__list.md) [dev\_list](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193);

1193};

1194

[ 1199](structi3c__driver__data.md)struct [i3c\_driver\_data](structi3c__driver__data.md) {

[ 1201](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb) struct [i3c\_config\_controller](structi3c__config__controller.md) [ctrl\_config](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb);

1202

[ 1204](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901) struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) [attached\_dev](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901);

1205};

1206

[ 1214](group__i3c__interface.md#ga42cb4edf6a099d586df14456fd98c873)#define I3C\_BUS\_FOR\_EACH\_I3CDEV(bus, desc) \

1215 SYS\_SLIST\_FOR\_EACH\_CONTAINER( \

1216 &((struct i3c\_driver\_data \*)(bus->data))->attached\_dev.devices.i3c, desc, node)

1217

[ 1225](group__i3c__interface.md#ga450ba9021d1080f890c32624f20ba2b8)#define I3C\_BUS\_FOR\_EACH\_I2CDEV(bus, desc) \

1226 SYS\_SLIST\_FOR\_EACH\_CONTAINER( \

1227 &((struct i3c\_driver\_data \*)(bus->data))->attached\_dev.devices.i2c, desc, node)

1228

[ 1241](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)(const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list,

1242 const struct [i3c\_device\_id](structi3c__device__id.md) \*id);

1243

[ 1256](group__i3c__interface.md#ga0e83c5a26b18acfbe7d532825a8fd54c)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#ga0e83c5a26b18acfbe7d532825a8fd54c)(const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b),

1257 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

1258

[ 1271](group__i3c__interface.md#gafac78dca571ff7daa34fca0cfa7cc3b1)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*[i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#gafac78dca571ff7daa34fca0cfa7cc3b1)(const struct [device](structdevice.md) \*dev,

1272 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d));

1273

[ 1325](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)int [i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

1326 const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list,

1327 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pid, bool must\_match,

1328 bool assigned\_okay,

1329 struct [i3c\_device\_desc](structi3c__device__desc.md) \*\*target,

1330 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d));

1331

[ 1345](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)static inline int [i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)(const struct [device](structdevice.md) \*dev,

1346 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config)

1347{

1348 const struct i3c\_driver\_api \*api =

1349 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1350

1351 if (api->configure == NULL) {

1352 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1353 }

1354

1355 return api->configure(dev, type, config);

1356}

1357

[ 1378](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)static inline int [i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)(const struct [device](structdevice.md) \*dev,

1379 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config)

1380{

1381 const struct i3c\_driver\_api \*api =

1382 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1383

1384 if (api->config\_get == NULL) {

1385 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1386 }

1387

1388 return api->config\_get(dev, type, config);

1389}

1390

[ 1401](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)static inline int [i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)(const struct [device](structdevice.md) \*dev)

1402{

1403 const struct i3c\_driver\_api \*api =

1404 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1405

1406 if (api->recover\_bus == NULL) {

1407 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1408 }

1409

1410 return api->recover\_bus(dev);

1411}

1412

[ 1432](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)int [i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1433

[ 1458](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)int [i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr);

1459

[ 1479](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)int [i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1480

[ 1499](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)int [i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target);

1500

[ 1518](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)int [i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target);

1519

[ 1543](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)static inline int [i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)(const struct [device](structdevice.md) \*dev)

1544{

1545 const struct i3c\_driver\_api \*api =

1546 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1547

1548 if (api->do\_daa == NULL) {

1549 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1550 }

1551

1552 return api->do\_daa(dev);

1553}

1554

[ 1568](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)\_\_syscall int [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)(const struct [device](structdevice.md) \*dev,

1569 struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload);

1570

1571static inline int z\_impl\_i3c\_do\_ccc(const struct [device](structdevice.md) \*dev,

1572 struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload)

1573{

1574 const struct i3c\_driver\_api \*api =

1575 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1576

1577 if (api->do\_ccc == NULL) {

1578 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1579 }

1580

1581 return api->do\_ccc(dev, payload);

1582}

1583

1588

[ 1615](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)\_\_syscall int [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1616 struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

1617

1618static inline int z\_impl\_i3c\_transfer(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1619 struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs)

1620{

1621 const struct i3c\_driver\_api \*api =

1622 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1623

1624 return api->i3c\_xfers(target->bus, target, msgs, num\_msgs);

1625}

1626

1628

1643static inline

[ 1644](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)(const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b),

1645 const struct [i3c\_device\_id](structi3c__device__id.md) \*id)

1646{

1647 const struct i3c\_driver\_api \*api =

1648 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1649

1650 if (api->i3c\_device\_find == NULL) {

1651 return NULL;

1652 }

1653

1654 return api->i3c\_device\_find(dev, id);

1655}

1656

1661

[ 1673](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)static inline int [i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)(const struct [device](structdevice.md) \*dev,

1674 struct [i3c\_ibi](structi3c__ibi.md) \*request)

1675{

1676 const struct i3c\_driver\_api \*api =

1677 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1678

1679 if (api->ibi\_raise == NULL) {

1680 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1681 }

1682

1683 return api->ibi\_raise(dev, request);

1684}

1685

[ 1700](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)static inline int [i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1701{

1702 const struct i3c\_driver\_api \*api =

1703 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1704

1705 if (api->ibi\_enable == NULL) {

1706 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1707 }

1708

1709 return api->ibi\_enable(target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803), target);

1710}

1711

[ 1724](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)static inline int [i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1725{

1726 const struct i3c\_driver\_api \*api =

1727 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1728

1729 if (api->ibi\_disable == NULL) {

1730 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1731 }

1732

1733 return api->ibi\_disable(target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803), target);

1734}

1735

[ 1747](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)static inline int [i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1748{

1749 return (target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) & [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838))

1750 == [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838);

1751}

1752

[ 1764](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)static inline int [i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1765{

1766 return (target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) & [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f))

1767 == [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f);

1768}

1769

[ 1781](group__i3c__ibi.md#ga537c1e2dafe3df1a5758e535beb323ea)static inline int [i3c\_device\_is\_controller\_capable](group__i3c__ibi.md#ga537c1e2dafe3df1a5758e535beb323ea)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1782{

1783 return [I3C\_BCR\_DEVICE\_ROLE](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)(target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21))

1784 == [I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852);

1785}

1786

1788

1793

[ 1807](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)static inline int [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1808 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1809{

1810 struct [i3c\_msg](structi3c__msg.md) msg;

1811

1812 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1813 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1814 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1815 msg.[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1816 msg.[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1817

1818 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

1819}

1820

[ 1834](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)static inline int [i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1835 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1836{

1837 struct [i3c\_msg](structi3c__msg.md) msg;

1838

1839 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1840 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1841 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1842 msg.[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1843 msg.[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1844

1845 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

1846}

1847

[ 1865](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)static inline int [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1866 const void \*write\_buf, size\_t num\_write,

1867 void \*read\_buf, size\_t num\_read)

1868{

1869 struct [i3c\_msg](structi3c__msg.md) msg[2];

1870

1871 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)write\_buf;

1872 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_write;

1873 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b);

1874 msg[0].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1875 msg[0].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1876

1877 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)read\_buf;

1878 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_read;

1879 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295) | [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1880 msg[1].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1881 msg[1].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1882

1883 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

1884}

1885

[ 1903](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)static inline int [i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1904 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1905 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff),

1906 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1907{

1908 return [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(target,

1909 &start\_addr, sizeof(start\_addr),

1910 [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), num\_bytes);

1911}

1912

[ 1933](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)static inline int [i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1934 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1935 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff),

1936 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1937{

1938 struct [i3c\_msg](structi3c__msg.md) msg[2];

1939

1940 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = &start\_addr;

1941 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = 1U;

1942 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b);

1943 msg[0].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1944 msg[0].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1945

1946 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1947 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1948 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1949 msg[1].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = 0;

1950 msg[1].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = 0;

1951

1952 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

1953}

1954

[ 1969](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)static inline int [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1970 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)

1971{

1972 return [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(target,

1973 &reg\_addr, sizeof(reg\_addr),

1974 value, sizeof(\*value));

1975}

1976

[ 1994](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)static inline int [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1995 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1996{

1997 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_buf[2] = {reg\_addr, value};

1998

1999 return [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)(target, tx\_buf, 2);

2000}

2001

[ 2020](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)static inline int [i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

2021 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask,

2022 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

2023{

2024 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_value, new\_value;

2025 int rc;

2026

2027 rc = [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)(target, reg\_addr, &old\_value);

2028 if (rc != 0) {

2029 return rc;

2030 }

2031

2032 new\_value = (old\_value & ~mask) | (value & mask);

2033 if (new\_value == old\_value) {

2034 return 0;

2035 }

2036

2037 return [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)(target, reg\_addr, new\_value);

2038}

2039

[ 2064](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)void [i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)(const char \*name, const struct [i3c\_msg](structi3c__msg.md) \*msgs,

2065 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2066

2068

[ 2084](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)int [i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)(const struct [device](structdevice.md) \*dev,

2085 const struct [i3c\_dev\_list](structi3c__dev__list.md) \*[i3c\_dev\_list](structi3c__dev__list.md));

2086

[ 2106](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)int [i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2107

[ 2118](group__i3c__interface.md#ga149d70b1c2e02e19782aa21a94b13684)bool [i3c\_bus\_has\_sec\_controller](group__i3c__interface.md#ga149d70b1c2e02e19782aa21a94b13684)(const struct [device](structdevice.md) \*dev);

2119

[ 2131](group__i3c__interface.md#ga554e0c4fa3e6855f431521ae42313216)int [i3c\_bus\_deftgts](group__i3c__interface.md#ga554e0c4fa3e6855f431521ae42313216)(const struct [device](structdevice.md) \*dev);

2132

2133/\*

2134 \* This needs to be after declaration of struct i3c\_driver\_api,

2135 \* or else compiler complains about undefined type inside

2136 \* the static inline API wrappers.

2137 \*/

2138#include <[zephyr/drivers/i3c/target\_device.h](target__device_8h.md)>

2139

2140/\*

2141 \* Include High-Data-Rate (HDR) inline helper functions

2142 \*/

2143#include <[zephyr/drivers/i3c/hdr\_ddr.h](hdr__ddr_8h.md)>

2144

2145#ifdef \_\_cplusplus

2146}

2147#endif

2148

2152

2153#include <zephyr/syscalls/i3c.h>

2154

2155#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_H\_ \*/

[addresses.h](addresses_8h.md)

[ccc.h](ccc_8h.md)

[device.h](device_8h.md)

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[devicetree.h](drivers_2i3c_2devicetree_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)

static int i3c\_ibi\_disable(struct i3c\_device\_desc \*target)

Disable IBI of a target device.

**Definition** i3c.h:1724

[i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)

static int i3c\_ibi\_has\_payload(struct i3c\_device\_desc \*target)

Check if target's IBI has payload.

**Definition** i3c.h:1747

[i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)

static int i3c\_ibi\_raise(const struct device \*dev, struct i3c\_ibi \*request)

Raise an In-Band Interrupt (IBI).

**Definition** i3c.h:1673

[i3c\_device\_is\_controller\_capable](group__i3c__ibi.md#ga537c1e2dafe3df1a5758e535beb323ea)

static int i3c\_device\_is\_controller\_capable(struct i3c\_device\_desc \*target)

Check if the target is controller capable.

**Definition** i3c.h:1781

[i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)

static int i3c\_device\_is\_ibi\_capable(struct i3c\_device\_desc \*target)

Check if device is IBI capable.

**Definition** i3c.h:1764

[i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)

static int i3c\_ibi\_enable(struct i3c\_device\_desc \*target)

Enable IBI of a target device.

**Definition** i3c.h:1700

[i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c)

int(\* i3c\_target\_ibi\_cb\_t)(struct i3c\_device\_desc \*target, struct i3c\_ibi\_payload \*payload)

Function called when In-Band Interrupt received from target device.

**Definition** ibi.h:146

[i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)

int i3c\_attach\_i3c\_device(struct i3c\_device\_desc \*target)

Attach an I3C device.

[I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)

#define I3C\_BCR\_IBI\_REQUEST\_CAPABLE

IBI Request Capable bit.

**Definition** i3c.h:87

[I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852)

#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE

Device Role - I3C Controller Capable.

**Definition** i3c.h:127

[i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#ga0e83c5a26b18acfbe7d532825a8fd54c)

struct i3c\_device\_desc \* i3c\_dev\_list\_i3c\_addr\_find(const struct device \*dev, uint8\_t addr)

Find a I3C target device descriptor by dynamic address.

[i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)

static struct i3c\_device\_desc \* i3c\_device\_find(const struct device \*dev, const struct i3c\_device\_id \*id)

Find a registered I3C target device.

**Definition** i3c.h:1644

[i3c\_bus\_has\_sec\_controller](group__i3c__interface.md#ga149d70b1c2e02e19782aa21a94b13684)

bool i3c\_bus\_has\_sec\_controller(const struct device \*dev)

Check if the bus has a secondary controller.

[i3c\_sdr\_target\_error\_codes](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c)

i3c\_sdr\_target\_error\_codes

I3C SDR Target Error Codes.

**Definition** i3c.h:337

[i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)

static int i3c\_configure(const struct device \*dev, enum i3c\_config\_type type, void \*config)

Configure the I3C hardware.

**Definition** i3c.h:1345

[i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)

int i3c\_dev\_list\_daa\_addr\_helper(struct i3c\_addr\_slots \*addr\_slots, const struct i3c\_dev\_list \*dev\_list, uint64\_t pid, bool must\_match, bool assigned\_okay, struct i3c\_device\_desc \*\*target, uint8\_t \*addr)

Helper function to find a usable address during ENTDAA.

[i3c\_bus\_deftgts](group__i3c__interface.md#ga554e0c4fa3e6855f431521ae42313216)

int i3c\_bus\_deftgts(const struct device \*dev)

Send the CCC DEFTGTS.

[i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)

i3c\_config\_type

Type of configuration being passed to configure function.

**Definition** i3c.h:508

[i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)

int i3c\_attach\_i2c\_device(struct i3c\_i2c\_device\_desc \*target)

Attach an I2C device.

[i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6)

i3c\_i2c\_speed\_type

I2C bus speed under I3C bus.

**Definition** i3c.h:258

[i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)

int i3c\_detach\_i3c\_device(struct i3c\_device\_desc \*target)

Detach I3C Device.

[i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90)

i3c\_bus\_mode

I3C bus mode.

**Definition** i3c.h:225

[i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)

static int i3c\_recover\_bus(const struct device \*dev)

Attempt bus recovery on the I3C bus.

**Definition** i3c.h:1401

[i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)

static int i3c\_config\_get(const struct device \*dev, enum i3c\_config\_type type, void \*config)

Get configuration of the I3C hardware.

**Definition** i3c.h:1378

[i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)

int i3c\_detach\_i2c\_device(struct i3c\_i2c\_device\_desc \*target)

Detach I2C Device.

[I3C\_BCR\_DEVICE\_ROLE](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)

#define I3C\_BCR\_DEVICE\_ROLE(bcr)

Device Role.

**Definition** i3c.h:139

[i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)

struct i3c\_device\_desc \* i3c\_dev\_list\_find(const struct i3c\_dev\_list \*dev\_list, const struct i3c\_device\_id \*id)

Find a I3C target device descriptor by ID.

[i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)

int i3c\_bus\_init(const struct device \*dev, const struct i3c\_dev\_list \*i3c\_dev\_list)

Generic helper function to perform bus initialization.

[i3c\_sdr\_controller\_error\_codes](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870)

i3c\_sdr\_controller\_error\_codes

I3C SDR Controller Error Codes.

**Definition** i3c.h:304

[i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)

int i3c\_do\_ccc(const struct device \*dev, struct i3c\_ccc\_payload \*payload)

Send CCC to the bus.

[i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)

int i3c\_device\_basic\_info\_get(struct i3c\_device\_desc \*target)

Get basic information from device and update device descriptor.

[i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)

static int i3c\_do\_daa(const struct device \*dev)

Perform Dynamic Address Assignment on the I3C bus.

**Definition** i3c.h:1543

[I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)

#define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE

IBI Payload bit.

**Definition** i3c.h:96

[i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)

int i3c\_reattach\_i3c\_device(struct i3c\_device\_desc \*target, uint8\_t old\_dyn\_addr)

Reattach I3C device.

[i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073)

i3c\_data\_rate

I3C data rate.

**Definition** i3c.h:274

[i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#gafac78dca571ff7daa34fca0cfa7cc3b1)

struct i3c\_i2c\_device\_desc \* i3c\_dev\_list\_i2c\_addr\_find(const struct device \*dev, uint16\_t addr)

Find a I2C target device descriptor by address.

[I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791)

@ I3C\_ERROR\_TE\_UNKNOWN

Unknown error (not official error code).

**Definition** i3c.h:366

[I3C\_ERROR\_TE6](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e)

@ I3C\_ERROR\_TE6

Monitoring Error.

**Definition** i3c.h:360

[I3C\_ERROR\_TE4](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd)

@ I3C\_ERROR\_TE4

0x7E/R missing after RESTART during Dynamic Address Arbitration

**Definition** i3c.h:354

[I3C\_ERROR\_TE3](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3)

@ I3C\_ERROR\_TE3

Assigned Address during Dynamic Address Arbitration.

**Definition** i3c.h:351

[I3C\_ERROR\_TE\_NONE](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a)

@ I3C\_ERROR\_TE\_NONE

No error (not official error code).

**Definition** i3c.h:369

[I3C\_ERROR\_TE\_MAX](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7)

@ I3C\_ERROR\_TE\_MAX

**Definition** i3c.h:371

[I3C\_ERROR\_TE1](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe)

@ I3C\_ERROR\_TE1

CCC Code.

**Definition** i3c.h:345

[I3C\_ERROR\_TE5](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f)

@ I3C\_ERROR\_TE5

Transaction after detecting CCC.

**Definition** i3c.h:357

[I3C\_ERROR\_DBR](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285)

@ I3C\_ERROR\_DBR

Dead Bus Recovery.

**Definition** i3c.h:363

[I3C\_ERROR\_TE2](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e)

@ I3C\_ERROR\_TE2

Write Data.

**Definition** i3c.h:348

[I3C\_ERROR\_TE\_INVALID](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a)

@ I3C\_ERROR\_TE\_INVALID

**Definition** i3c.h:372

[I3C\_ERROR\_TE0](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a)

@ I3C\_ERROR\_TE0

Invalid Broadcast Address or Dynamic Address after DA assignment.

**Definition** i3c.h:342

[I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00)

@ I3C\_CONFIG\_TARGET

**Definition** i3c.h:510

[I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017)

@ I3C\_CONFIG\_CUSTOM

**Definition** i3c.h:511

[I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5)

@ I3C\_CONFIG\_CONTROLLER

**Definition** i3c.h:509

[I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4)

@ I3C\_I2C\_SPEED\_INVALID

**Definition** i3c.h:266

[I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967)

@ I3C\_I2C\_SPEED\_MAX

**Definition** i3c.h:265

[I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea)

@ I3C\_I2C\_SPEED\_FMPLUS

I2C FM+ mode.

**Definition** i3c.h:263

[I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1)

@ I3C\_I2C\_SPEED\_FM

I2C FM mode.

**Definition** i3c.h:260

[I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)

@ I3C\_BUS\_MODE\_INVALID

**Definition** i3c.h:250

[I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445)

@ I3C\_BUS\_MODE\_PURE

Only I3C devices are on the bus.

**Definition** i3c.h:227

[I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434)

@ I3C\_BUS\_MODE\_MIXED\_FAST

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:233

[I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697)

@ I3C\_BUS\_MODE\_MAX

**Definition** i3c.h:249

[I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722)

@ I3C\_BUS\_MODE\_MIXED\_LIMITED

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:240

[I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a)

@ I3C\_BUS\_MODE\_MIXED\_SLOW

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:247

[I3C\_ERROR\_CE0](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282)

@ I3C\_ERROR\_CE0

Transaction after sending CCC.

**Definition** i3c.h:306

[I3C\_ERROR\_CE2](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574)

@ I3C\_ERROR\_CE2

No response to broadcast address (0x7E).

**Definition** i3c.h:312

[I3C\_ERROR\_CE\_INVALID](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0)

@ I3C\_ERROR\_CE\_INVALID

**Definition** i3c.h:324

[I3C\_ERROR\_CE\_MAX](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7)

@ I3C\_ERROR\_CE\_MAX

**Definition** i3c.h:323

[I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502)

@ I3C\_ERROR\_CE\_UNKNOWN

Unknown error (not official error code).

**Definition** i3c.h:318

[I3C\_ERROR\_CE3](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f)

@ I3C\_ERROR\_CE3

Failed Controller Handoff.

**Definition** i3c.h:315

[I3C\_ERROR\_CE1](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb)

@ I3C\_ERROR\_CE1

Monitoring Error.

**Definition** i3c.h:309

[I3C\_ERROR\_CE\_NONE](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707)

@ I3C\_ERROR\_CE\_NONE

No error (not official error code).

**Definition** i3c.h:321

[I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725)

@ I3C\_DATA\_RATE\_MAX

**Definition** i3c.h:290

[I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)

@ I3C\_DATA\_RATE\_INVALID

**Definition** i3c.h:291

[I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d)

@ I3C\_DATA\_RATE\_HDR\_TSP

High Data Rate - Ternary Symbol for Pure Bus.

**Definition** i3c.h:285

[I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301)

@ I3C\_DATA\_RATE\_HDR\_DDR

High Data Rate - Double Data Rate messaging.

**Definition** i3c.h:279

[I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9)

@ I3C\_DATA\_RATE\_SDR

Single Data Rate messaging.

**Definition** i3c.h:276

[I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590)

@ I3C\_DATA\_RATE\_HDR\_TSL

High Data Rate - Ternary Symbol Legacy-inclusive-Bus.

**Definition** i3c.h:282

[I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed)

@ I3C\_DATA\_RATE\_HDR\_BT

High Data Rate - Bulk Transport.

**Definition** i3c.h:288

[i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)

int i3c\_transfer(struct i3c\_device\_desc \*target, struct i3c\_msg \*msgs, uint8\_t num\_msgs)

Perform data transfer from the controller to a I3C target device.

[I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)

#define I3C\_MSG\_STOP

Send STOP after this message.

**Definition** i3c.h:396

[i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)

static int i3c\_write\_read(struct i3c\_device\_desc \*target, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)

Write then read data from an I3C target device.

**Definition** i3c.h:1865

[i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)

static int i3c\_burst\_read(struct i3c\_device\_desc \*target, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)

Read multiple bytes from an internal address of an I3C target device.

**Definition** i3c.h:1903

[i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)

static int i3c\_reg\_update\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)

Update internal register of an I3C target device.

**Definition** i3c.h:2020

[i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)

void i3c\_dump\_msgs(const char \*name, const struct i3c\_msg \*msgs, uint8\_t num\_msgs, struct i3c\_device\_desc \*target)

Dump out an I3C message.

[I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)

#define I3C\_MSG\_READ

Read message from I3C bus.

**Definition** i3c.h:389

[I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)

#define I3C\_MSG\_WRITE

Write message to I3C bus.

**Definition** i3c.h:386

[i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)

static int i3c\_reg\_read\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t \*value)

Read internal register of an I3C target device.

**Definition** i3c.h:1969

[i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)

static int i3c\_write(struct i3c\_device\_desc \*target, const uint8\_t \*buf, uint32\_t num\_bytes)

Write a set amount of data to an I3C target device.

**Definition** i3c.h:1807

[i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)

static int i3c\_read(struct i3c\_device\_desc \*target, uint8\_t \*buf, uint32\_t num\_bytes)

Read a set amount of data from an I3C target device.

**Definition** i3c.h:1834

[I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)

#define I3C\_MSG\_RESTART

RESTART I3C transaction for this message.

**Definition** i3c.h:407

[i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)

static int i3c\_burst\_write(struct i3c\_device\_desc \*target, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)

Write multiple bytes to an internal address of an I3C target device.

**Definition** i3c.h:1933

[i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)

static int i3c\_reg\_write\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t value)

Write internal register of an I3C target device.

**Definition** i3c.h:1994

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

[ibi.h](ibi_8h.md)

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

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[i3c\_addr\_slots](structi3c__addr__slots.md)

Structure to keep track of addresses on I3C bus.

**Definition** addresses.h:58

[i3c\_ccc\_payload](structi3c__ccc__payload.md)

Payload structure for one CCC transaction.

**Definition** ccc.h:267

[i3c\_config\_controller](structi3c__config__controller.md)

Configuration parameters for I3C hardware to act as controller.

**Definition** i3c.h:517

[i3c\_config\_controller::i3c](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b)

uint32\_t i3c

SCL frequency (in Hz) for I3C transfers.

**Definition** i3c.h:526

[i3c\_config\_controller::supported\_hdr](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d)

uint8\_t supported\_hdr

Bit mask of supported HDR modes (0 - 7).

**Definition** i3c.h:538

[i3c\_config\_controller::is\_secondary](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36)

bool is\_secondary

True if the controller is to be the secondary controller of the bus.

**Definition** i3c.h:522

[i3c\_config\_controller::i2c](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd)

uint32\_t i2c

SCL frequency (in Hz) for I2C transfers.

**Definition** i3c.h:529

[i3c\_config\_controller::scl](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b)

struct i3c\_config\_controller::@056135366137020063162136324011126070110331100007 scl

[i3c\_config\_custom](structi3c__config__custom.md)

Custom I3C configuration parameters.

**Definition** i3c.h:549

[i3c\_config\_custom::ptr](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd)

void \* ptr

Pointer to configuration parameter.

**Definition** i3c.h:563

[i3c\_config\_custom::id](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31)

uint32\_t id

ID of the configuration parameter.

**Definition** i3c.h:551

[i3c\_config\_custom::val](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340)

uintptr\_t val

Value of configuration parameter.

**Definition** i3c.h:555

[i3c\_dev\_attached\_list](structi3c__dev__attached__list.md)

Structure for describing attached devices for a controller.

**Definition** i3c.h:1133

[i3c\_dev\_attached\_list::i3c](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad)

sys\_slist\_t i3c

Linked list of attached I3C devices.

**Definition** i3c.h:1146

[i3c\_dev\_attached\_list::i2c](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a)

sys\_slist\_t i2c

Linked list of attached I2C devices.

**Definition** i3c.h:1151

[i3c\_dev\_attached\_list::addr\_slots](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474)

struct i3c\_addr\_slots addr\_slots

Address slots:

**Definition** i3c.h:1140

[i3c\_dev\_attached\_list::devices](structi3c__dev__attached__list.md#ad539b98ce41e781da53f1fd46b03df63)

struct i3c\_dev\_attached\_list::@233130030357247267201022070232022115366221343347 devices

[i3c\_dev\_list](structi3c__dev__list.md)

Structure for describing known devices for a controller.

**Definition** i3c.h:1163

[i3c\_dev\_list::i2c](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e)

struct i3c\_i2c\_device\_desc \*const i2c

Pointer to array of known I2C devices.

**Definition** i3c.h:1172

[i3c\_dev\_list::num\_i3c](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985)

const uint8\_t num\_i3c

Number of I3C devices in array.

**Definition** i3c.h:1177

[i3c\_dev\_list::i3c](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce)

struct i3c\_device\_desc \*const i3c

Pointer to array of known I3C devices.

**Definition** i3c.h:1167

[i3c\_dev\_list::num\_i2c](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318)

const uint8\_t num\_i2c

Number of I2C devices in array.

**Definition** i3c.h:1182

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:913

[i3c\_device\_desc::maxwr](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9)

uint8\_t maxwr

Maximum Write Speed.

**Definition** i3c.h:1004

[i3c\_device\_desc::init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5)

const uint8\_t init\_dynamic\_addr

Initial dynamic address.

**Definition** i3c.h:948

[i3c\_device\_desc::getcap1](structi3c__device__desc.md#a062f86dec32de3b9e899b096df47d828)

uint8\_t getcap1

I3C v1.1+ GETCAPS1 (I3C\_CCC\_GETCAPS1\_\*).

**Definition** i3c.h:1041

[i3c\_device\_desc::getcap2](structi3c__device__desc.md#a089da4f6eaf2b80fc689bb89d527d330)

uint8\_t getcap2

GETCAPS2 (I3C\_CCC\_GETCAPS2\_\*).

**Definition** i3c.h:1051

[i3c\_device\_desc::max\_read\_turnaround](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb)

uint32\_t max\_read\_turnaround

Maximum Read turnaround time in microseconds.

**Definition** i3c.h:1007

[i3c\_device\_desc::static\_addr](structi3c__device__desc.md#a105221381d47f690219aa09a20936ae1)

const uint8\_t static\_addr

Static address for this target device.

**Definition** i3c.h:937

[i3c\_device\_desc::getcap4](structi3c__device__desc.md#a1314218c6f6a429ccedb9975b9e02a90)

uint8\_t getcap4

GETCAPS4.

**Definition** i3c.h:1070

[i3c\_device\_desc::max\_ibi](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9)

uint8\_t max\_ibi

Maximum IBI Payload Size.

**Definition** i3c.h:1018

[i3c\_device\_desc::ibi\_cb](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265)

i3c\_target\_ibi\_cb\_t ibi\_cb

In-Band Interrupt (IBI) callback.

**Definition** i3c.h:1085

[i3c\_device\_desc::group\_addr](structi3c__device__desc.md#a260730aef8862b2898ef6f65cf4956c4)

uint8\_t group\_addr

Group address for this target device.

**Definition** i3c.h:982

[i3c\_device\_desc::data\_length](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835)

struct i3c\_device\_desc::@374166210137153225365322260210124156025250214226 data\_length

[i3c\_device\_desc::mwl](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed)

uint16\_t mwl

Maximum Write Length.

**Definition** i3c.h:1015

[i3c\_device\_desc::getcap3](structi3c__device__desc.md#a47af0b36448dfec8307b25a31712428e)

uint8\_t getcap3

GETCAPS3 (I3C\_CCC\_GETCAPS3\_\*).

**Definition** i3c.h:1064

[i3c\_device\_desc::dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0)

uint8\_t dynamic\_addr

Dynamic Address for this target device used for communication.

**Definition** i3c.h:971

[i3c\_device\_desc::dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b)

const struct device \*const dev

Device driver instance of the I3C device.

**Definition** i3c.h:920

[i3c\_device\_desc::getcaps](structi3c__device__desc.md#a7e44bedd1aa032d661335f8ec0a0d2e2)

struct i3c\_device\_desc::@025161371003043020356247061065002050371177151366 getcaps

Describes advanced (Target) capabilities and features.

[i3c\_device\_desc::data\_speed](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500)

struct i3c\_device\_desc::@011056325341036010112127327312366216151020376366 data\_speed

[i3c\_device\_desc::node](structi3c__device__desc.md#a965edbd5d74c06773e190a14d4f6e3cd)

sys\_snode\_t node

**Definition** i3c.h:914

[i3c\_device\_desc::mrl](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e)

uint16\_t mrl

Maximum Read Length.

**Definition** i3c.h:1012

[i3c\_device\_desc::pid](structi3c__device__desc.md#ac82bd8eccc52a98df76506bd2bed3961)

const uint64\_t pid

Device Provisioned ID.

**Definition** i3c.h:923

[i3c\_device\_desc::maxrd](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523)

uint8\_t maxrd

Maximum Read Speed.

**Definition** i3c.h:1001

[i3c\_device\_desc::gethdrcap](structi3c__device__desc.md#ae01bc68ac8154238d85bbf44dc06dfb7)

uint8\_t gethdrcap

I3C v1.0 HDR Capabilities (I3C\_CCC\_GETCAPS1\_\*).

**Definition** i3c.h:1031

[i3c\_device\_desc::bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21)

uint8\_t bcr

Bus Characteristic Register (BCR).

**Definition** i3c.h:989

[i3c\_device\_desc::dcr](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c)

uint8\_t dcr

Device Characteristic Register (DCR).

**Definition** i3c.h:997

[i3c\_device\_desc::supports\_setaasa](structi3c__device__desc.md#af0905f27f1765c96fc3aaf601926d6ed)

const bool supports\_setaasa

Device support for SETAASA.

**Definition** i3c.h:956

[i3c\_device\_desc::bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)

const struct device \*const bus

I3C bus to which this target device is attached.

**Definition** i3c.h:917

[i3c\_device\_id](structi3c__device__id.md)

Structure used for matching I3C devices.

**Definition** i3c.h:879

[i3c\_device\_id::pid](structi3c__device__id.md#a254a43360f3eb8be2f62ed0ae48b8637)

const uint64\_t pid

Device Provisioned ID.

**Definition** i3c.h:881

[i3c\_driver\_config](structi3c__driver__config.md)

This structure is common to all I3C drivers and is expected to be the first element in the object poi...

**Definition** i3c.h:1190

[i3c\_driver\_config::dev\_list](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193)

struct i3c\_dev\_list dev\_list

I3C/I2C device list struct.

**Definition** i3c.h:1192

[i3c\_driver\_data](structi3c__driver__data.md)

This structure is common to all I3C drivers and is expected to be the first element in the driver's s...

**Definition** i3c.h:1199

[i3c\_driver\_data::ctrl\_config](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb)

struct i3c\_config\_controller ctrl\_config

Controller Configuration.

**Definition** i3c.h:1201

[i3c\_driver\_data::attached\_dev](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901)

struct i3c\_dev\_attached\_list attached\_dev

Attached I3C/I2C devices and addresses.

**Definition** i3c.h:1204

[i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md)

Structure describing a I2C device on I3C bus.

**Definition** i3c.h:1102

[i3c\_i2c\_device\_desc::bus](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2)

const struct device \* bus

I3C bus to which this I2C device is attached.

**Definition** i3c.h:1106

[i3c\_i2c\_device\_desc::addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d)

const uint16\_t addr

Static address for this I2C device.

**Definition** i3c.h:1109

[i3c\_i2c\_device\_desc::lvr](structi3c__i2c__device__desc.md#a672aca260630deed5d8cdf90896d1115)

const uint8\_t lvr

Legacy Virtual Register (LVR).

**Definition** i3c.h:1115

[i3c\_i2c\_device\_desc::node](structi3c__i2c__device__desc.md#acfcf72db311b19e479e9147ce5257245)

sys\_snode\_t node

**Definition** i3c.h:1103

[i3c\_ibi](structi3c__ibi.md)

Struct for IBI request.

**Definition** ibi.h:58

[i3c\_msg](structi3c__msg.md)

One I3C Message.

**Definition** i3c.h:472

[i3c\_msg::flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217)

uint8\_t flags

Flags for this message.

**Definition** i3c.h:489

[i3c\_msg::hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9)

uint8\_t hdr\_mode

HDR mode (I3C\_MSG\_HDR\_MODE\*) for transfer if any I3C\_MSG\_HDR\_\* is set in flags.

**Definition** i3c.h:497

[i3c\_msg::num\_xfer](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5)

uint32\_t num\_xfer

Total number of bytes transferred.

**Definition** i3c.h:486

[i3c\_msg::buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff)

uint8\_t \* buf

Data buffer in bytes.

**Definition** i3c.h:474

[i3c\_msg::hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b)

uint8\_t hdr\_cmd\_code

HDR command code field (7-bit) for HDR-DDR, HDR-TSP and HDR-TSL.

**Definition** i3c.h:500

[i3c\_msg::len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0)

uint32\_t len

Length of buffer in bytes.

**Definition** i3c.h:477

[i3c\_target\_config](structi3c__target__config.md)

Structure describing a device that supports the I3C target API.

**Definition** target\_device.h:102

[util.h](sys_2util_8h.md)

Misc utilities.

[target\_device.h](target__device_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c.h](i3c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
