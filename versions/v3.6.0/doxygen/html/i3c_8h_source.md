---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/i3c_8h_source.html
original_path: doxygen/html/i3c_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/device.h](device_8h.md)>

20

21#include <[zephyr/drivers/i3c/addresses.h](addresses_8h.md)>

22#include <[zephyr/drivers/i3c/ccc.h](ccc_8h.md)>

23#include <[zephyr/drivers/i3c/devicetree.h](drivers_2i3c_2devicetree_8h.md)>

24#include <[zephyr/drivers/i3c/ibi.h](ibi_8h.md)>

25#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

70

[ 77](group__i3c__interface.md#ga91ebe41a421dc05ae7f1de1ce2dd314f)#define I3C\_BCR\_MAX\_DATA\_SPEED\_LIMIT BIT(0)

78

[ 80](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)#define I3C\_BCR\_IBI\_REQUEST\_CAPABLE BIT(1)

81

[ 89](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)#define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE BIT(2)

90

[ 97](group__i3c__interface.md#ga7b9fea89457022d8012ac25133bf63db)#define I3C\_BCR\_OFFLINE\_CAPABLE BIT(3)

98

[ 105](group__i3c__interface.md#ga69dc4a5004da568684a3c72046bba870)#define I3C\_BCR\_VIRTUAL\_TARGET BIT(4)

106

[ 114](group__i3c__interface.md#ga07018705794753d0d0d65131f011e097)#define I3C\_BCR\_ADV\_CAPABILITIES BIT(5)

115

[ 117](group__i3c__interface.md#ga867b4b12b23c803b86b57dcc86b9e604)#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_TARGET 0U

118

[ 120](group__i3c__interface.md#ga0e64c8aa6717b96bcf9dad6c9ec7f852)#define I3C\_BCR\_DEVICE\_ROLE\_I3C\_CONTROLLER\_CAPABLE 1U

121

[ 123](group__i3c__interface.md#ga09bda29f6c4b71cd4d5d7ba98c677706)#define I3C\_BCR\_DEVICE\_ROLE\_SHIFT 6U

124

[ 126](group__i3c__interface.md#ga25721c9963040c84b7f5bbb48bb87b44)#define I3C\_BCR\_DEVICE\_ROLE\_MASK (0x03U << I3C\_BCR\_DEVICE\_ROLE\_SHIFT)

127

[ 135](group__i3c__interface.md#ga90988b26dc2f388ec7c65387a24f05af)#define I3C\_BCR\_DEVICE\_ROLE(bcr) \

136 (((bcr) & I3C\_BCR\_DEVICE\_ROLE\_MASK) >> I3C\_BCR\_DEVICE\_ROLE\_SHIFT)

137

139

158

[ 160](group__i3c__interface.md#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)#define I3C\_LVR\_I2C\_FM\_PLUS\_MODE 0

161

[ 163](group__i3c__interface.md#ga053945f5f67ee3c681de2c9362e69c39)#define I3C\_LVR\_I2C\_FM\_MODE 1

164

[ 166](group__i3c__interface.md#gafc35b1fdf105ebd3bc1835ad38fa4229)#define I3C\_LVR\_I2C\_MODE\_SHIFT 4

167

[ 169](group__i3c__interface.md#gaf073cc9ea1a68c57663c36de12554876)#define I3C\_LVR\_I2C\_MODE\_MASK BIT(4)

170

[ 178](group__i3c__interface.md#gaaf759805bb5824a89612b292a4439982)#define I3C\_LVR\_I2C\_MODE(lvr) \

179 (((lvr) & I3C\_LVR\_I2C\_MODE\_MASK) >> I3C\_LVR\_I2C\_MODE\_SHIFT)

180

[ 187](group__i3c__interface.md#ga4319835ddb6b5984b21f5a5a2f14ae75)#define I3C\_LVR\_I2C\_DEV\_IDX\_0 0

188

[ 195](group__i3c__interface.md#ga02a21af4c679a81b8290beea30c8ef40)#define I3C\_LVR\_I2C\_DEV\_IDX\_1 1

196

[ 203](group__i3c__interface.md#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)#define I3C\_LVR\_I2C\_DEV\_IDX\_2 2

204

[ 206](group__i3c__interface.md#gadb583c049cb0b212836115b6cfa5a569)#define I3C\_LVR\_I2C\_DEV\_IDX\_SHIFT 5

207

[ 209](group__i3c__interface.md#ga50fa249b36b91d56e49004548a1c7520)#define I3C\_LVR\_I2C\_DEV\_IDX\_MASK (0x07U << I3C\_LVR\_I2C\_DEV\_IDX\_SHIFT)

210

[ 218](group__i3c__interface.md#gae7afa509b1d63374c551bcdaf84c5dd1)#define I3C\_LVR\_I2C\_DEV\_IDX(lvr) \

219 (((lvr) & I3C\_LVR\_I2C\_DEV\_IDX\_MASK) >> I3C\_LVR\_I2C\_DEV\_IDX\_SHIFT)

220

222

[ 226](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90)enum [i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90) {

[ 228](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445) [I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445),

229

[ 234](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434) [I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434),

235

[ 241](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722) [I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722),

242

[ 248](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a) [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a),

249

[ 250](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) [I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697) = [I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a),

[ 251](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c) [I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c),

252};

253

[ 259](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6)enum [i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6) {

[ 261](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1) [I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1),

262

[ 264](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea) [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea),

265

[ 266](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) [I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967) = [I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea),

[ 267](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4) [I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4),

268};

269

[ 275](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073)enum [i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073) {

[ 277](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9) [I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9),

278

[ 280](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301) [I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301),

281

[ 283](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590) [I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590),

284

[ 286](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d) [I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d),

287

[ 289](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed) [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed),

290

[ 291](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) [I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725) = [I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed),

[ 292](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a) [I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a),

293};

294

[ 305](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870)enum [i3c\_sdr\_controller\_error\_codes](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870) {

[ 307](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282) [I3C\_ERROR\_CE0](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282),

308

[ 310](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb) [I3C\_ERROR\_CE1](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb),

311

[ 313](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574) [I3C\_ERROR\_CE2](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574),

314

[ 316](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f) [I3C\_ERROR\_CE3](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f),

317

[ 319](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502) [I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502),

320

[ 322](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707) [I3C\_ERROR\_CE\_NONE](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707),

323

[ 324](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7) [I3C\_ERROR\_CE\_MAX](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7) = [I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502),

[ 325](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0) [I3C\_ERROR\_CE\_INVALID](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0),

326};

327

[ 338](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c)enum [i3c\_sdr\_target\_error\_codes](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c) {

[ 343](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a) [I3C\_ERROR\_TE0](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a),

344

[ 346](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe) [I3C\_ERROR\_TE1](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe),

347

[ 349](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e) [I3C\_ERROR\_TE2](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e),

350

[ 352](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3) [I3C\_ERROR\_TE3](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3),

353

[ 355](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd) [I3C\_ERROR\_TE4](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd),

356

[ 358](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f) [I3C\_ERROR\_TE5](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f),

359

[ 361](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e) [I3C\_ERROR\_TE6](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e),

362

[ 364](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285) [I3C\_ERROR\_DBR](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285),

365

[ 367](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791) [I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791),

368

[ 370](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a) [I3C\_ERROR\_TE\_NONE](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a),

371

[ 372](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7) [I3C\_ERROR\_TE\_MAX](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7) = [I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791),

[ 373](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a) [I3C\_ERROR\_TE\_INVALID](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a),

374};

375

381

382/\*

383 \* I3C\_MSG\_\* are I3C Message flags.

384 \*/

385

[ 387](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)#define I3C\_MSG\_WRITE (0U << 0U)

388

[ 390](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)#define I3C\_MSG\_READ BIT(0)

391

393#define I3C\_MSG\_RW\_MASK BIT(0)

395

[ 397](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)#define I3C\_MSG\_STOP BIT(1)

398

[ 408](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)#define I3C\_MSG\_RESTART BIT(2)

409

[ 411](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38)#define I3C\_MSG\_HDR BIT(3)

412

[ 414](group__i3c__transfer__api.md#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)#define I3C\_MSG\_NBCH BIT(4)

415

[ 417](group__i3c__transfer__api.md#ga18aac0862826869f94e5a71670debcb0)#define I3C\_MSG\_HDR\_MODE0 BIT(0)

418

[ 420](group__i3c__transfer__api.md#ga8eb3dc48237dfdb25fde40a1efa03241)#define I3C\_MSG\_HDR\_MODE1 BIT(1)

421

[ 423](group__i3c__transfer__api.md#ga15cbd61e7d509c28b22fbc9e0844cb23)#define I3C\_MSG\_HDR\_MODE2 BIT(2)

424

[ 426](group__i3c__transfer__api.md#ga162fb9ab0e4ed7f8feb0e91d183a88e7)#define I3C\_MSG\_HDR\_MODE3 BIT(3)

427

[ 429](group__i3c__transfer__api.md#gabe45532238bc15672f6454dac70d20cf)#define I3C\_MSG\_HDR\_MODE4 BIT(4)

430

[ 432](group__i3c__transfer__api.md#gac712daa606d0c51ce523d7a687821282)#define I3C\_MSG\_HDR\_MODE5 BIT(5)

433

[ 435](group__i3c__transfer__api.md#ga7654c1947e13c019c24bf12712b0773b)#define I3C\_MSG\_HDR\_MODE6 BIT(6)

436

[ 438](group__i3c__transfer__api.md#ga08df1d8df82226d1f23b4cc923584672)#define I3C\_MSG\_HDR\_MODE7 BIT(7)

439

[ 441](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a)#define I3C\_MSG\_HDR\_DDR I3C\_MSG\_HDR\_MODE0

442

[ 444](group__i3c__transfer__api.md#gaa61322f770db296b5ab718c48ab960d3)#define I3C\_MSG\_HDR\_TSP I3C\_MSG\_HDR\_MODE1

445

[ 447](group__i3c__transfer__api.md#gac43a2d266f3a23fd6dfa11405f3fd6f3)#define I3C\_MSG\_HDR\_TSL I3C\_MSG\_HDR\_MODE2

448

[ 450](group__i3c__transfer__api.md#ga8b2fdcb827cbd3325f124a1c615698e7)#define I3C\_MSG\_HDR\_BT I3C\_MSG\_HDR\_MODE3

451

453

458

[ 473](structi3c__msg.md)struct [i3c\_msg](structi3c__msg.md) {

[ 475](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

476

[ 478](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0);

479

[ 487](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_xfer](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5);

488

[ 490](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217);

491

[ 498](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9);

499};

500

502

[ 506](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) {

[ 507](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5) [I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5),

[ 508](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00) [I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00),

[ 509](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017) [I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017),

510};

511

[ 515](structi3c__config__controller.md)struct [i3c\_config\_controller](structi3c__config__controller.md) {

[ 520](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36) bool [is\_secondary](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36);

521

522 struct {

[ 524](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i3c](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b);

525

[ 527](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd);

[ 528](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b) } [scl](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b);

529

[ 536](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_hdr](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d);

537};

538

[ 547](structi3c__config__custom.md)struct [i3c\_config\_custom](structi3c__config__custom.md) {

[ 549](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31);

550

551 union {

[ 553](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [val](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340);

554

[ 561](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd) void \*[ptr](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd);

562 };

563};

564

571struct [i3c\_device\_desc](structi3c__device__desc.md);

572struct [i3c\_device\_id](structi3c__device__id.md);

573struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md);

574struct [i3c\_target\_config](structi3c__target__config.md);

575

576\_\_subsystem struct i3c\_driver\_api {

584 struct i2c\_driver\_api i2c\_api;

585

598 int (\*configure)(const struct device \*dev,

599 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config);

600

613 int (\*config\_get)(const struct device \*dev,

614 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config);

615

627 int (\*recover\_bus)(const struct device \*dev);

628

642 int (\*attach\_i3c\_device)(const struct device \*dev,

643 struct i3c\_device\_desc \*target,

644 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

645

659 int (\*reattach\_i3c\_device)(const struct device \*dev,

660 struct i3c\_device\_desc \*target,

661 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr);

662

675 int (\*detach\_i3c\_device)(const struct device \*dev,

676 struct i3c\_device\_desc \*target);

677

690 int (\*attach\_i2c\_device)(const struct device \*dev,

691 struct i3c\_i2c\_device\_desc \*target);

692

705 int (\*detach\_i2c\_device)(const struct device \*dev,

706 struct i3c\_i2c\_device\_desc \*target);

707

719 int (\*do\_daa)(const struct device \*dev);

720

733 int (\*do\_ccc)(const struct device \*dev,

734 struct i3c\_ccc\_payload \*payload);

735

748 int (\*i3c\_xfers)(const struct device \*dev,

749 struct i3c\_device\_desc \*target,

750 struct i3c\_msg \*msgs,

751 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

752

766 struct i3c\_device\_desc \*(\*i3c\_device\_find)(const struct device \*dev,

767 const struct i3c\_device\_id \*id);

768

781 int (\*ibi\_raise)(const struct device \*dev,

782 struct i3c\_ibi \*request);

783

796 int (\*ibi\_enable)(const struct device \*dev,

797 struct i3c\_device\_desc \*target);

798

811 int (\*ibi\_disable)(const struct device \*dev,

812 struct i3c\_device\_desc \*target);

813

829 int (\*target\_register)(const struct device \*dev,

830 struct i3c\_target\_config \*cfg);

831

847 int (\*target\_unregister)(const struct device \*dev,

848 struct i3c\_target\_config \*cfg);

849

865 int (\*target\_tx\_write)(const struct device \*dev,

866 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

867};

868

872

[ 876](structi3c__device__id.md)struct [i3c\_device\_id](structi3c__device__id.md) {

[ 878](structi3c__device__id.md#a254a43360f3eb8be2f62ed0ae48b8637) const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__device__id.md#a254a43360f3eb8be2f62ed0ae48b8637):48;

879};

880

[ 889](group__i3c__interface.md#gaed0df9802cc9b268abcfe4e877ebf498)#define I3C\_DEVICE\_ID(pid) \

890 { \

891 .pid = pid \

892 }

893

[ 911](structi3c__device__desc.md)struct [i3c\_device\_desc](structi3c__device__desc.md) {

917 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

919

[ 921](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803) const struct [device](structdevice.md) \* const [bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803);

922

[ 924](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b) const struct [device](structdevice.md) \* const [dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b);

925

[ 927](structi3c__device__desc.md#ac82bd8eccc52a98df76506bd2bed3961) const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__device__desc.md#ac82bd8eccc52a98df76506bd2bed3961):48;

928

[ 941](structi3c__device__desc.md#a105221381d47f690219aa09a20936ae1) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__device__desc.md#a105221381d47f690219aa09a20936ae1);

942

[ 952](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5);

953

[ 967](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0);

968

969#if defined(CONFIG\_I3C\_USE\_GROUP\_ADDR) || defined(\_\_DOXYGEN\_\_)

[ 977](structi3c__device__desc.md#a260730aef8862b2898ef6f65cf4956c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [group\_addr](structi3c__device__desc.md#a260730aef8862b2898ef6f65cf4956c4);

978#endif /\* CONFIG\_I3C\_USE\_GROUP\_ADDR \*/

979

[ 1009](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21);

1010

[ 1017](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c);

1018

1019 struct {

[ 1021](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxrd](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523);

1022

[ 1024](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maxwr](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9);

1025

[ 1027](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_read\_turnaround](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb);

[ 1028](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500) } [data\_speed](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500);

1029

1030 struct {

[ 1032](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mrl](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e);

1033

[ 1035](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mwl](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed);

1036

[ 1038](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_ibi](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9);

[ 1039](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835) } [data\_length](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835);

1040

1046 void \*controller\_priv;

1048

1049#if defined(CONFIG\_I3C\_USE\_IBI) || defined(\_\_DOXYGEN\_\_)

[ 1053](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265) [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) [ibi\_cb](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265);

1054#endif /\* CONFIG\_I3C\_USE\_IBI \*/

1055};

1056

[ 1070](structi3c__i2c__device__desc.md)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) {

1076 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

1078

[ 1080](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2) const struct [device](structdevice.md) \*[bus](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2);

1081

[ 1083](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d);

1084

[ 1099](structi3c__i2c__device__desc.md#a672aca260630deed5d8cdf90896d1115) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [lvr](structi3c__i2c__device__desc.md#a672aca260630deed5d8cdf90896d1115);

1100

1106 void \*controller\_priv;

1108};

1109

[ 1118](structi3c__dev__attached__list.md)struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) {

[ 1125](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474) struct [i3c\_addr\_slots](structi3c__addr__slots.md) [addr\_slots](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474);

1126

1127 struct {

[ 1131](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [i3c](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad);

1132

[ 1136](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [i2c](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a);

[ 1137](structi3c__dev__attached__list.md#ae4af4796da989c2f2bdd258d06e10c30) } [devices](structi3c__dev__attached__list.md#ae4af4796da989c2f2bdd258d06e10c30);

1138};

1139

[ 1148](structi3c__dev__list.md)struct [i3c\_dev\_list](structi3c__dev__list.md) {

[ 1152](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce) struct [i3c\_device\_desc](structi3c__device__desc.md) \* const [i3c](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce);

1153

[ 1157](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e) struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \* const [i2c](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e);

1158

[ 1162](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_i3c](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985);

1163

[ 1167](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_i2c](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318);

1168};

1169

[ 1175](structi3c__driver__config.md)struct [i3c\_driver\_config](structi3c__driver__config.md) {

[ 1177](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193) struct [i3c\_dev\_list](structi3c__dev__list.md) [dev\_list](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193);

1178};

1179

[ 1184](structi3c__driver__data.md)struct [i3c\_driver\_data](structi3c__driver__data.md) {

[ 1186](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb) struct [i3c\_config\_controller](structi3c__config__controller.md) [ctrl\_config](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb);

1187

[ 1189](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901) struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) [attached\_dev](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901);

1190};

1191

[ 1204](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)(const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list,

1205 const struct [i3c\_device\_id](structi3c__device__id.md) \*id);

1206

[ 1219](group__i3c__interface.md#gaa9d6c8bcded72a85b80a98a019d90461)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#gaa9d6c8bcded72a85b80a98a019d90461)(struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) \*dev\_list,

1220 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

1221

[ 1234](group__i3c__interface.md#ga959da8f875822bb94c9c5e72fdc9fbdb)struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*[i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#ga959da8f875822bb94c9c5e72fdc9fbdb)(struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) \*dev\_list,

1235 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d));

1236

[ 1250](group__i3c__interface.md#ga61bed94233fd977f539f1f51c75e98a6)int [i3c\_determine\_default\_addr](group__i3c__interface.md#ga61bed94233fd977f539f1f51c75e98a6)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d));

1251

[ 1303](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)int [i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)(struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots,

1304 const struct [i3c\_dev\_list](structi3c__dev__list.md) \*dev\_list,

1305 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pid, bool must\_match,

1306 bool assigned\_okay,

1307 struct [i3c\_device\_desc](structi3c__device__desc.md) \*\*target,

1308 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d));

1309

[ 1323](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)static inline int [i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)(const struct [device](structdevice.md) \*dev,

1324 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config)

1325{

1326 const struct i3c\_driver\_api \*api =

1327 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1328

1329 if (api->configure == NULL) {

1330 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1331 }

1332

1333 return api->configure(dev, type, config);

1334}

1335

[ 1356](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)static inline int [i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)(const struct [device](structdevice.md) \*dev,

1357 enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config)

1358{

1359 const struct i3c\_driver\_api \*api =

1360 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1361

1362 if (api->config\_get == NULL) {

1363 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1364 }

1365

1366 return api->config\_get(dev, type, config);

1367}

1368

[ 1379](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)static inline int [i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)(const struct [device](structdevice.md) \*dev)

1380{

1381 const struct i3c\_driver\_api \*api =

1382 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1383

1384 if (api->recover\_bus == NULL) {

1385 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1386 }

1387

1388 return api->recover\_bus(dev);

1389}

1390

[ 1410](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)int [i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1411

[ 1436](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)int [i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_dyn\_addr);

1437

[ 1457](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)int [i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

1458

[ 1477](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)int [i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target);

1478

[ 1496](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)int [i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)(struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md) \*target);

1497

[ 1521](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)static inline int [i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)(const struct [device](structdevice.md) \*dev)

1522{

1523 const struct i3c\_driver\_api \*api =

1524 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1525

1526 if (api->do\_daa == NULL) {

1527 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1528 }

1529

1530 return api->do\_daa(dev);

1531}

1532

[ 1546](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)\_\_syscall int [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)(const struct [device](structdevice.md) \*dev,

1547 struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload);

1548

1549static inline int z\_impl\_i3c\_do\_ccc(const struct [device](structdevice.md) \*dev,

1550 struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload)

1551{

1552 const struct i3c\_driver\_api \*api =

1553 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1554

1555 if (api->do\_ccc == NULL) {

1556 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1557 }

1558

1559 return api->do\_ccc(dev, payload);

1560}

1561

1566

[ 1593](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)\_\_syscall int [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1594 struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

1595

1596static inline int z\_impl\_i3c\_transfer(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1597 struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs)

1598{

1599 const struct i3c\_driver\_api \*api =

1600 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1601

1602 return api->i3c\_xfers(target->bus, target, msgs, num\_msgs);

1603}

1604

1606

1621static inline

[ 1622](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)(const struct [device](structdevice.md) \*[dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b),

1623 const struct [i3c\_device\_id](structi3c__device__id.md) \*id)

1624{

1625 const struct i3c\_driver\_api \*api =

1626 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1627

1628 if (api->i3c\_device\_find == NULL) {

1629 return NULL;

1630 }

1631

1632 return api->i3c\_device\_find(dev, id);

1633}

1634

1639

[ 1651](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)static inline int [i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)(const struct [device](structdevice.md) \*dev,

1652 struct [i3c\_ibi](structi3c__ibi.md) \*request)

1653{

1654 const struct i3c\_driver\_api \*api =

1655 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1656

1657 if (api->ibi\_raise == NULL) {

1658 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1659 }

1660

1661 return api->ibi\_raise(dev, request);

1662}

1663

[ 1678](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)static inline int [i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1679{

1680 const struct i3c\_driver\_api \*api =

1681 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1682

1683 if (api->ibi\_enable == NULL) {

1684 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1685 }

1686

1687 return api->ibi\_enable(target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803), target);

1688}

1689

[ 1702](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)static inline int [i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1703{

1704 const struct i3c\_driver\_api \*api =

1705 (const struct i3c\_driver\_api \*)target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1706

1707 if (api->ibi\_disable == NULL) {

1708 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1709 }

1710

1711 return api->ibi\_disable(target->[bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803), target);

1712}

1713

[ 1725](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)static inline int [i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1726{

1727 return (target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) & [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838))

1728 == [I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838);

1729}

1730

[ 1742](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)static inline int [i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target)

1743{

1744 return (target->[bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21) & [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f))

1745 == [I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f);

1746}

1747

1749

1754

[ 1768](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)static inline int [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1769 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1770{

1771 struct [i3c\_msg](structi3c__msg.md) msg;

1772

1773 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1774 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1775 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1776

1777 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

1778}

1779

[ 1793](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)static inline int [i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1794 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1795{

1796 struct [i3c\_msg](structi3c__msg.md) msg;

1797

1798 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1799 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1800 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1801

1802 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

1803}

1804

[ 1822](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)static inline int [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1823 const void \*write\_buf, size\_t num\_write,

1824 void \*read\_buf, size\_t num\_read)

1825{

1826 struct [i3c\_msg](structi3c__msg.md) msg[2];

1827

1828 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)write\_buf;

1829 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_write;

1830 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b);

1831

1832 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)read\_buf;

1833 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_read;

1834 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295) | [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1835

1836 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

1837}

1838

[ 1856](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)static inline int [i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1857 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1858 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff),

1859 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1860{

1861 return [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(target,

1862 &start\_addr, sizeof(start\_addr),

1863 [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), num\_bytes);

1864}

1865

[ 1886](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)static inline int [i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1887 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1888 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff),

1889 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1890{

1891 struct [i3c\_msg](structi3c__msg.md) msg[2];

1892

1893 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = &start\_addr;

1894 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = 1U;

1895 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b);

1896

1897 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

1898 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

1899 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

1900

1901 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

1902}

1903

[ 1918](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)static inline int [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1919 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)

1920{

1921 return [i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)(target,

1922 &reg\_addr, sizeof(reg\_addr),

1923 value, sizeof(\*value));

1924}

1925

[ 1943](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)static inline int [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1944 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1945{

1946 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_buf[2] = {reg\_addr, value};

1947

1948 return [i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)(target, tx\_buf, 2);

1949}

1950

[ 1969](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)static inline int [i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

1970 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask,

1971 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1972{

1973 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_value, new\_value;

1974 int rc;

1975

1976 rc = [i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)(target, reg\_addr, &old\_value);

1977 if (rc != 0) {

1978 return rc;

1979 }

1980

1981 new\_value = (old\_value & ~mask) | (value & mask);

1982 if (new\_value == old\_value) {

1983 return 0;

1984 }

1985

1986 return [i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)(target, reg\_addr, new\_value);

1987}

1988

[ 2013](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)void [i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)(const char \*name, const struct [i3c\_msg](structi3c__msg.md) \*msgs,

2014 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2015

2017

[ 2033](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)int [i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)(const struct [device](structdevice.md) \*dev,

2034 const struct [i3c\_dev\_list](structi3c__dev__list.md) \*[i3c\_dev\_list](structi3c__dev__list.md));

2035

[ 2055](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)int [i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target);

2056

2057/\*

2058 \* This needs to be after declaration of struct i3c\_driver\_api,

2059 \* or else compiler complains about undefined type inside

2060 \* the static inline API wrappers.

2061 \*/

2062#include <[zephyr/drivers/i3c/target\_device.h](target__device_8h.md)>

2063

2064#ifdef \_\_cplusplus

2065}

2066#endif

2067

2071

2072#include <syscalls/i3c.h>

2073

2074#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_H\_ \*/

[addresses.h](addresses_8h.md)

[ccc.h](ccc_8h.md)

[device.h](device_8h.md)

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[devicetree.h](drivers_2i3c_2devicetree_8h.md)

[i3c\_ibi\_disable](group__i3c__ibi.md#ga037e156404324262694b4a5403821adc)

static int i3c\_ibi\_disable(struct i3c\_device\_desc \*target)

Disable IBI of a target device.

**Definition** i3c.h:1702

[i3c\_ibi\_has\_payload](group__i3c__ibi.md#ga1a23e2ca2afb7cf371f523dcbcd7724f)

static int i3c\_ibi\_has\_payload(struct i3c\_device\_desc \*target)

Check if target's IBI has payload.

**Definition** i3c.h:1725

[i3c\_ibi\_raise](group__i3c__ibi.md#ga516c656231efd07429402c37643eca66)

static int i3c\_ibi\_raise(const struct device \*dev, struct i3c\_ibi \*request)

Raise an In-Band Interrupt (IBI).

**Definition** i3c.h:1651

[i3c\_device\_is\_ibi\_capable](group__i3c__ibi.md#ga6c09d19ab1c7c19db4d085a30066345e)

static int i3c\_device\_is\_ibi\_capable(struct i3c\_device\_desc \*target)

Check if device is IBI capable.

**Definition** i3c.h:1742

[i3c\_ibi\_enable](group__i3c__ibi.md#ga7625ef0313ded1f638a6eb44395b02c0)

static int i3c\_ibi\_enable(struct i3c\_device\_desc \*target)

Enable IBI of a target device.

**Definition** i3c.h:1678

[i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c)

int(\* i3c\_target\_ibi\_cb\_t)(struct i3c\_device\_desc \*target, struct i3c\_ibi\_payload \*payload)

Function called when In-Band Interrupt received from target device.

**Definition** ibi.h:151

[i3c\_attach\_i3c\_device](group__i3c__interface.md#ga042d1a3315f040562534ce08306b329c)

int i3c\_attach\_i3c\_device(struct i3c\_device\_desc \*target)

Attach an I3C device.

[I3C\_BCR\_IBI\_REQUEST\_CAPABLE](group__i3c__interface.md#ga0c09de8a18ea1586e37d35e073ae641f)

#define I3C\_BCR\_IBI\_REQUEST\_CAPABLE

IBI Request Capable bit.

**Definition** i3c.h:80

[i3c\_device\_find](group__i3c__interface.md#ga10a3963b749cc667a03975889d618d1b)

static struct i3c\_device\_desc \* i3c\_device\_find(const struct device \*dev, const struct i3c\_device\_id \*id)

Find a registered I3C target device.

**Definition** i3c.h:1622

[i3c\_sdr\_target\_error\_codes](group__i3c__interface.md#ga1e4ea1268e4fa6feccc8fb4cbb3d144c)

i3c\_sdr\_target\_error\_codes

I3C SDR Target Error Codes.

**Definition** i3c.h:338

[i3c\_configure](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352)

static int i3c\_configure(const struct device \*dev, enum i3c\_config\_type type, void \*config)

Configure the I3C hardware.

**Definition** i3c.h:1323

[i3c\_dev\_list\_daa\_addr\_helper](group__i3c__interface.md#ga3a4dac6aa35249e6e277da8075b596a8)

int i3c\_dev\_list\_daa\_addr\_helper(struct i3c\_addr\_slots \*addr\_slots, const struct i3c\_dev\_list \*dev\_list, uint64\_t pid, bool must\_match, bool assigned\_okay, struct i3c\_device\_desc \*\*target, uint8\_t \*addr)

Helper function to find a usable address during ENTDAA.

[i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)

i3c\_config\_type

Type of configuration being passed to configure function.

**Definition** i3c.h:506

[i3c\_attach\_i2c\_device](group__i3c__interface.md#ga5e69aaed50f99418c7123f652555ae20)

int i3c\_attach\_i2c\_device(struct i3c\_i2c\_device\_desc \*target)

Attach an I2C device.

[i3c\_determine\_default\_addr](group__i3c__interface.md#ga61bed94233fd977f539f1f51c75e98a6)

int i3c\_determine\_default\_addr(struct i3c\_device\_desc \*target, uint8\_t \*addr)

Helper function to find the default address an i3c device is attached with.

[i3c\_i2c\_speed\_type](group__i3c__interface.md#ga67686f0a5d83697361c655c3fd6e61c6)

i3c\_i2c\_speed\_type

I2C bus speed under I3C bus.

**Definition** i3c.h:259

[i3c\_detach\_i3c\_device](group__i3c__interface.md#ga6db9688cc7e9d34404717ae753751579)

int i3c\_detach\_i3c\_device(struct i3c\_device\_desc \*target)

Detach I3C Device.

[i3c\_bus\_mode](group__i3c__interface.md#ga7a0d66ab45f618ca055422e2b69abe90)

i3c\_bus\_mode

I3C bus mode.

**Definition** i3c.h:226

[i3c\_recover\_bus](group__i3c__interface.md#ga7b23e08b10a09bde4e87328d6915aa25)

static int i3c\_recover\_bus(const struct device \*dev)

Attempt bus recovery on the I3C bus.

**Definition** i3c.h:1379

[i3c\_config\_get](group__i3c__interface.md#ga807877923755aeb5a065e054fb42946d)

static int i3c\_config\_get(const struct device \*dev, enum i3c\_config\_type type, void \*config)

Get configuration of the I3C hardware.

**Definition** i3c.h:1356

[i3c\_detach\_i2c\_device](group__i3c__interface.md#ga8e8de45499bff02cac4c59c1758ec0a7)

int i3c\_detach\_i2c\_device(struct i3c\_i2c\_device\_desc \*target)

Detach I2C Device.

[i3c\_dev\_list\_i2c\_addr\_find](group__i3c__interface.md#ga959da8f875822bb94c9c5e72fdc9fbdb)

struct i3c\_i2c\_device\_desc \* i3c\_dev\_list\_i2c\_addr\_find(struct i3c\_dev\_attached\_list \*dev\_list, uint16\_t addr)

Find a I2C target device descriptor by address.

[i3c\_dev\_list\_find](group__i3c__interface.md#ga9a451379bef381c6a264a22a2282fa89)

struct i3c\_device\_desc \* i3c\_dev\_list\_find(const struct i3c\_dev\_list \*dev\_list, const struct i3c\_device\_id \*id)

Find a I3C target device descriptor by ID.

[i3c\_bus\_init](group__i3c__interface.md#ga9af9191a5ab2e5e2ea0478520721171d)

int i3c\_bus\_init(const struct device \*dev, const struct i3c\_dev\_list \*i3c\_dev\_list)

Generic helper function to perform bus initialization.

[i3c\_sdr\_controller\_error\_codes](group__i3c__interface.md#ga9d2655e9bc8489dbc84bfea01d2c1870)

i3c\_sdr\_controller\_error\_codes

I3C SDR Controller Error Codes.

**Definition** i3c.h:305

[i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862)

int i3c\_do\_ccc(const struct device \*dev, struct i3c\_ccc\_payload \*payload)

Send CCC to the bus.

[i3c\_dev\_list\_i3c\_addr\_find](group__i3c__interface.md#gaa9d6c8bcded72a85b80a98a019d90461)

struct i3c\_device\_desc \* i3c\_dev\_list\_i3c\_addr\_find(struct i3c\_dev\_attached\_list \*dev\_list, uint8\_t addr)

Find a I3C target device descriptor by dynamic address.

[i3c\_device\_basic\_info\_get](group__i3c__interface.md#gaac5d10b8f42a6a069e0ac15cc7263db8)

int i3c\_device\_basic\_info\_get(struct i3c\_device\_desc \*target)

Get basic information from device and update device descriptor.

[i3c\_do\_daa](group__i3c__interface.md#gabb54c0e85d0f5e8585391f9e5c20d4b6)

static int i3c\_do\_daa(const struct device \*dev)

Perform Dynamic Address Assignment on the I3C bus.

**Definition** i3c.h:1521

[I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE](group__i3c__interface.md#gae119c230097cb8e1eab9fc45cafde838)

#define I3C\_BCR\_IBI\_PAYLOAD\_HAS\_DATA\_BYTE

IBI Payload bit.

**Definition** i3c.h:89

[i3c\_reattach\_i3c\_device](group__i3c__interface.md#gae6c8e8612368808117f4fce960e43769)

int i3c\_reattach\_i3c\_device(struct i3c\_device\_desc \*target, uint8\_t old\_dyn\_addr)

Reattach I3C device.

[i3c\_data\_rate](group__i3c__interface.md#gae9d98642c6f249ee0e6ea0dc491b5073)

i3c\_data\_rate

I3C data rate.

**Definition** i3c.h:275

[I3C\_ERROR\_TE\_UNKNOWN](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca24684b50d96bf68a5a4c6f819c393791)

@ I3C\_ERROR\_TE\_UNKNOWN

Unknown error (not official error code).

**Definition** i3c.h:367

[I3C\_ERROR\_TE6](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3f5f0fe6d716fd7df84b99df707c2a8e)

@ I3C\_ERROR\_TE6

Monitoring Error.

**Definition** i3c.h:361

[I3C\_ERROR\_TE4](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca3fd9d3a819fb1f3d79e53757aaa03dfd)

@ I3C\_ERROR\_TE4

0x7E/R missing after RESTART during Dynamic Address Arbitration

**Definition** i3c.h:355

[I3C\_ERROR\_TE3](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca4d5a837d35c5a752fee2cb4cdf761cd3)

@ I3C\_ERROR\_TE3

Assigned Address during Dynamic Address Arbitration.

**Definition** i3c.h:352

[I3C\_ERROR\_TE\_NONE](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca5bc59253e371b88471b5d9bc15cd9c3a)

@ I3C\_ERROR\_TE\_NONE

No error (not official error code).

**Definition** i3c.h:370

[I3C\_ERROR\_TE\_MAX](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144ca7e6c2b9e56fc594ca57501adb09b26c7)

@ I3C\_ERROR\_TE\_MAX

**Definition** i3c.h:372

[I3C\_ERROR\_TE1](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144caa79f8166d1c6bf18311adf11e6c612fe)

@ I3C\_ERROR\_TE1

CCC Code.

**Definition** i3c.h:346

[I3C\_ERROR\_TE5](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab014ca57d29162e7cf3116be36693c8f)

@ I3C\_ERROR\_TE5

Transaction after detecting CCC.

**Definition** i3c.h:358

[I3C\_ERROR\_DBR](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab02aee605de8820b586908bafcd8e285)

@ I3C\_ERROR\_DBR

Dead Bus Recovery.

**Definition** i3c.h:364

[I3C\_ERROR\_TE2](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cab6d0cb581f823ba39934c835eed7207e)

@ I3C\_ERROR\_TE2

Write Data.

**Definition** i3c.h:349

[I3C\_ERROR\_TE\_INVALID](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cadb9cd0b5e4c5e0ae96f941d39a4af23a)

@ I3C\_ERROR\_TE\_INVALID

**Definition** i3c.h:373

[I3C\_ERROR\_TE0](group__i3c__interface.md#gga1e4ea1268e4fa6feccc8fb4cbb3d144cae9d64998fe25f44268fc35944e23661a)

@ I3C\_ERROR\_TE0

Invalid Broadcast Address or Dynamic Address after DA assignment.

**Definition** i3c.h:343

[I3C\_CONFIG\_TARGET](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00)

@ I3C\_CONFIG\_TARGET

**Definition** i3c.h:508

[I3C\_CONFIG\_CUSTOM](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017)

@ I3C\_CONFIG\_CUSTOM

**Definition** i3c.h:509

[I3C\_CONFIG\_CONTROLLER](group__i3c__interface.md#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5)

@ I3C\_CONFIG\_CONTROLLER

**Definition** i3c.h:507

[I3C\_I2C\_SPEED\_INVALID](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4)

@ I3C\_I2C\_SPEED\_INVALID

**Definition** i3c.h:267

[I3C\_I2C\_SPEED\_MAX](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967)

@ I3C\_I2C\_SPEED\_MAX

**Definition** i3c.h:266

[I3C\_I2C\_SPEED\_FMPLUS](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea)

@ I3C\_I2C\_SPEED\_FMPLUS

I2C FM+ mode.

**Definition** i3c.h:264

[I3C\_I2C\_SPEED\_FM](group__i3c__interface.md#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1)

@ I3C\_I2C\_SPEED\_FM

I2C FM mode.

**Definition** i3c.h:261

[I3C\_BUS\_MODE\_INVALID](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)

@ I3C\_BUS\_MODE\_INVALID

**Definition** i3c.h:251

[I3C\_BUS\_MODE\_PURE](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445)

@ I3C\_BUS\_MODE\_PURE

Only I3C devices are on the bus.

**Definition** i3c.h:228

[I3C\_BUS\_MODE\_MIXED\_FAST](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434)

@ I3C\_BUS\_MODE\_MIXED\_FAST

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:234

[I3C\_BUS\_MODE\_MAX](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697)

@ I3C\_BUS\_MODE\_MAX

**Definition** i3c.h:250

[I3C\_BUS\_MODE\_MIXED\_LIMITED](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722)

@ I3C\_BUS\_MODE\_MIXED\_LIMITED

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:241

[I3C\_BUS\_MODE\_MIXED\_SLOW](group__i3c__interface.md#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a)

@ I3C\_BUS\_MODE\_MIXED\_SLOW

Both I3C and legacy I2C devices are on the bus.

**Definition** i3c.h:248

[I3C\_ERROR\_CE0](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a29a9faf9402dbad479d7c72af3074282)

@ I3C\_ERROR\_CE0

Transaction after sending CCC.

**Definition** i3c.h:307

[I3C\_ERROR\_CE2](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a46fdc1719e801fbb6a61db7b7675a574)

@ I3C\_ERROR\_CE2

No response to broadcast address (0x7E).

**Definition** i3c.h:313

[I3C\_ERROR\_CE\_INVALID](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a72a987f540981d0c0ef973cf835707a0)

@ I3C\_ERROR\_CE\_INVALID

**Definition** i3c.h:325

[I3C\_ERROR\_CE\_MAX](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a8dfdbe43a58837e87eb08da228c462e7)

@ I3C\_ERROR\_CE\_MAX

**Definition** i3c.h:324

[I3C\_ERROR\_CE\_UNKNOWN](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870a936f9c9f75c2fef25d9a3a0b6dc45502)

@ I3C\_ERROR\_CE\_UNKNOWN

Unknown error (not official error code).

**Definition** i3c.h:319

[I3C\_ERROR\_CE3](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ac18dd1126126aed36d7c4ca399133e1f)

@ I3C\_ERROR\_CE3

Failed Controller Handoff.

**Definition** i3c.h:316

[I3C\_ERROR\_CE1](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870ae60ebbf70623d022df65ce8837a5bddb)

@ I3C\_ERROR\_CE1

Monitoring Error.

**Definition** i3c.h:310

[I3C\_ERROR\_CE\_NONE](group__i3c__interface.md#gga9d2655e9bc8489dbc84bfea01d2c1870af8c1a2219f28b91b11206f7fafd12707)

@ I3C\_ERROR\_CE\_NONE

No error (not official error code).

**Definition** i3c.h:322

[I3C\_DATA\_RATE\_MAX](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725)

@ I3C\_DATA\_RATE\_MAX

**Definition** i3c.h:291

[I3C\_DATA\_RATE\_INVALID](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)

@ I3C\_DATA\_RATE\_INVALID

**Definition** i3c.h:292

[I3C\_DATA\_RATE\_HDR\_TSP](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d)

@ I3C\_DATA\_RATE\_HDR\_TSP

High Data Rate - Ternary Symbol for Pure Bus.

**Definition** i3c.h:286

[I3C\_DATA\_RATE\_HDR\_DDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301)

@ I3C\_DATA\_RATE\_HDR\_DDR

High Data Rate - Double Data Rate messaging.

**Definition** i3c.h:280

[I3C\_DATA\_RATE\_SDR](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9)

@ I3C\_DATA\_RATE\_SDR

Single Data Rate messaging.

**Definition** i3c.h:277

[I3C\_DATA\_RATE\_HDR\_TSL](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590)

@ I3C\_DATA\_RATE\_HDR\_TSL

High Data Rate - Ternary Symbol Legacy-inclusive-Bus.

**Definition** i3c.h:283

[I3C\_DATA\_RATE\_HDR\_BT](group__i3c__interface.md#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed)

@ I3C\_DATA\_RATE\_HDR\_BT

High Data Rate - Bulk Transport.

**Definition** i3c.h:289

[i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)

int i3c\_transfer(struct i3c\_device\_desc \*target, struct i3c\_msg \*msgs, uint8\_t num\_msgs)

Perform data transfer from the controller to a I3C target device.

[I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)

#define I3C\_MSG\_STOP

Send STOP after this message.

**Definition** i3c.h:397

[i3c\_write\_read](group__i3c__transfer__api.md#ga3da2e99b667eab4fd92f5c0e1b57a8ea)

static int i3c\_write\_read(struct i3c\_device\_desc \*target, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)

Write then read data from an I3C target device.

**Definition** i3c.h:1822

[i3c\_burst\_read](group__i3c__transfer__api.md#ga3e4d985a784618efad67f8550f715115)

static int i3c\_burst\_read(struct i3c\_device\_desc \*target, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)

Read multiple bytes from an internal address of an I3C target device.

**Definition** i3c.h:1856

[i3c\_reg\_update\_byte](group__i3c__transfer__api.md#ga4e0488ff21cbe99b206c115017473ed9)

static int i3c\_reg\_update\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)

Update internal register of an I3C target device.

**Definition** i3c.h:1969

[i3c\_dump\_msgs](group__i3c__transfer__api.md#ga61098371d2492a3f35c0fa779a88b348)

void i3c\_dump\_msgs(const char \*name, const struct i3c\_msg \*msgs, uint8\_t num\_msgs, struct i3c\_device\_desc \*target)

Dump out an I3C message.

[I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)

#define I3C\_MSG\_READ

Read message from I3C bus.

**Definition** i3c.h:390

[I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)

#define I3C\_MSG\_WRITE

Write message to I3C bus.

**Definition** i3c.h:387

[i3c\_reg\_read\_byte](group__i3c__transfer__api.md#ga87c1f23c94d37dfbaa22e4679fb8130a)

static int i3c\_reg\_read\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t \*value)

Read internal register of an I3C target device.

**Definition** i3c.h:1918

[i3c\_write](group__i3c__transfer__api.md#gaa3b61aa9813ccb0df80562b0829d95dd)

static int i3c\_write(struct i3c\_device\_desc \*target, const uint8\_t \*buf, uint32\_t num\_bytes)

Write a set amount of data to an I3C target device.

**Definition** i3c.h:1768

[i3c\_read](group__i3c__transfer__api.md#gaba39bd08ab50c5737ba617f4d27c3541)

static int i3c\_read(struct i3c\_device\_desc \*target, uint8\_t \*buf, uint32\_t num\_bytes)

Read a set amount of data from an I3C target device.

**Definition** i3c.h:1793

[I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)

#define I3C\_MSG\_RESTART

RESTART I3C transaction for this message.

**Definition** i3c.h:408

[i3c\_burst\_write](group__i3c__transfer__api.md#gaee773f95fcaf6cb88ced47f5c512c78c)

static int i3c\_burst\_write(struct i3c\_device\_desc \*target, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)

Write multiple bytes to an internal address of an I3C target device.

**Definition** i3c.h:1886

[i3c\_reg\_write\_byte](group__i3c__transfer__api.md#gaf7033eb93fd3779ffa98eb83e5a1a1b1)

static int i3c\_reg\_write\_byte(struct i3c\_device\_desc \*target, uint8\_t reg\_addr, uint8\_t value)

Write internal register of an I3C target device.

**Definition** i3c.h:1943

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

**Definition** errno.h:83

[ibi.h](ibi_8h.md)

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[i3c\_addr\_slots](structi3c__addr__slots.md)

Structure to keep track of addresses on I3C bus.

**Definition** addresses.h:57

[i3c\_ccc\_payload](structi3c__ccc__payload.md)

Payload structure for one CCC transaction.

**Definition** ccc.h:266

[i3c\_config\_controller](structi3c__config__controller.md)

Configuration parameters for I3C hardware to act as controller.

**Definition** i3c.h:515

[i3c\_config\_controller::i3c](structi3c__config__controller.md#ab1dfb88ea8fab83c4aa3a884fa66084b)

uint32\_t i3c

SCL frequency (in Hz) for I3C transfers.

**Definition** i3c.h:524

[i3c\_config\_controller::supported\_hdr](structi3c__config__controller.md#abb0eb210bc07911b5648eb490a92c00d)

uint8\_t supported\_hdr

Bit mask of supported HDR modes (0 - 7).

**Definition** i3c.h:536

[i3c\_config\_controller::is\_secondary](structi3c__config__controller.md#ac0d0190b6a31499097fc34eda3e27a36)

bool is\_secondary

True if the controller is to be the secondary controller of the bus.

**Definition** i3c.h:520

[i3c\_config\_controller::i2c](structi3c__config__controller.md#acd01843427b6cf53c9965885455c1dbd)

uint32\_t i2c

SCL frequency (in Hz) for I2C transfers.

**Definition** i3c.h:527

[i3c\_config\_controller::scl](structi3c__config__controller.md#aebab80b194bf7c35e15edb0466d97e1b)

struct i3c\_config\_controller::@056135366137020063162136324011126070110331100007 scl

[i3c\_config\_custom](structi3c__config__custom.md)

Custom I3C configuration parameters.

**Definition** i3c.h:547

[i3c\_config\_custom::ptr](structi3c__config__custom.md#a2bcc6334871ced958cd0358aeab38dcd)

void \* ptr

Pointer to configuration parameter.

**Definition** i3c.h:561

[i3c\_config\_custom::id](structi3c__config__custom.md#a8a9c0173d3439ed1ed10e8c7013bdb31)

uint32\_t id

ID of the configuration parameter.

**Definition** i3c.h:549

[i3c\_config\_custom::val](structi3c__config__custom.md#ae0320b4b277b1c3d4ad438cd71d98340)

uintptr\_t val

Value of configuration parameter.

**Definition** i3c.h:553

[i3c\_dev\_attached\_list](structi3c__dev__attached__list.md)

Structure for describing attached devices for a controller.

**Definition** i3c.h:1118

[i3c\_dev\_attached\_list::i3c](structi3c__dev__attached__list.md#a4cb8e85cf103f7368c2a16004baf1bad)

sys\_slist\_t i3c

Linked list of attached I3C devices.

**Definition** i3c.h:1131

[i3c\_dev\_attached\_list::i2c](structi3c__dev__attached__list.md#ab2688288f1ab550e4181ed4dc3dd057a)

sys\_slist\_t i2c

Linked list of attached I2C devices.

**Definition** i3c.h:1136

[i3c\_dev\_attached\_list::addr\_slots](structi3c__dev__attached__list.md#ab5aba9e4e47d3acedc88754946e21474)

struct i3c\_addr\_slots addr\_slots

Address slots:

**Definition** i3c.h:1125

[i3c\_dev\_attached\_list::devices](structi3c__dev__attached__list.md#ae4af4796da989c2f2bdd258d06e10c30)

struct i3c\_dev\_attached\_list::@025161371003043020356247061065002050371177151366 devices

[i3c\_dev\_list](structi3c__dev__list.md)

Structure for describing known devices for a controller.

**Definition** i3c.h:1148

[i3c\_dev\_list::i2c](structi3c__dev__list.md#a7993101f7b5fa3961773f58fd8b1985e)

struct i3c\_i2c\_device\_desc \*const i2c

Pointer to array of known I2C devices.

**Definition** i3c.h:1157

[i3c\_dev\_list::num\_i3c](structi3c__dev__list.md#ab13b77da61fc829c3f6414963f5f2985)

const uint8\_t num\_i3c

Number of I3C devices in array.

**Definition** i3c.h:1162

[i3c\_dev\_list::i3c](structi3c__dev__list.md#aba1871e32e1ee9e6a809dd11a7a44dce)

struct i3c\_device\_desc \*const i3c

Pointer to array of known I3C devices.

**Definition** i3c.h:1152

[i3c\_dev\_list::num\_i2c](structi3c__dev__list.md#ae1b33a38150098463187d4016e31b318)

const uint8\_t num\_i2c

Number of I2C devices in array.

**Definition** i3c.h:1167

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:911

[i3c\_device\_desc::maxwr](structi3c__device__desc.md#a02b3bd0d87f92ec67cb7d53e210ec8a9)

uint8\_t maxwr

Maximum Write Speed.

**Definition** i3c.h:1024

[i3c\_device\_desc::init\_dynamic\_addr](structi3c__device__desc.md#a0477ac021d81431a34f55fa1c9f04bb5)

const uint8\_t init\_dynamic\_addr

Initial dynamic address.

**Definition** i3c.h:952

[i3c\_device\_desc::max\_read\_turnaround](structi3c__device__desc.md#a0c1a3f65c20ddabc004c82527ec690bb)

uint32\_t max\_read\_turnaround

Maximum Read turnaround time in microseconds.

**Definition** i3c.h:1027

[i3c\_device\_desc::static\_addr](structi3c__device__desc.md#a105221381d47f690219aa09a20936ae1)

const uint8\_t static\_addr

Static address for this target device.

**Definition** i3c.h:941

[i3c\_device\_desc::max\_ibi](structi3c__device__desc.md#a1a895792d02e00784cc76da7ce4b60c9)

uint8\_t max\_ibi

Maximum IBI Payload Size.

**Definition** i3c.h:1038

[i3c\_device\_desc::ibi\_cb](structi3c__device__desc.md#a1f9eda89e2e28971e39aace38ddbb265)

i3c\_target\_ibi\_cb\_t ibi\_cb

Private data by the controller to aid in transactions.

**Definition** i3c.h:1053

[i3c\_device\_desc::group\_addr](structi3c__device__desc.md#a260730aef8862b2898ef6f65cf4956c4)

uint8\_t group\_addr

Group address for this target device.

**Definition** i3c.h:977

[i3c\_device\_desc::data\_length](structi3c__device__desc.md#a27f1d7ca0b4eac2d55781f3856f31835)

struct i3c\_device\_desc::@374166210137153225365322260210124156025250214226 data\_length

[i3c\_device\_desc::mwl](structi3c__device__desc.md#a29804ab89f08928f14fa4095f57e79ed)

uint16\_t mwl

Maximum Write Length.

**Definition** i3c.h:1035

[i3c\_device\_desc::dynamic\_addr](structi3c__device__desc.md#a4e4c9614871e5ea4aa08b1560ecc40d0)

uint8\_t dynamic\_addr

Dynamic Address for this target device used for communication.

**Definition** i3c.h:967

[i3c\_device\_desc::dev](structi3c__device__desc.md#a653090fd2c78794dae02a2031daddb4b)

const struct device \*const dev

Device driver instance of the I3C device.

**Definition** i3c.h:924

[i3c\_device\_desc::data\_speed](structi3c__device__desc.md#a85f1ab9b53f4c4979b78d48e485d8500)

struct i3c\_device\_desc::@011056325341036010112127327312366216151020376366 data\_speed

[i3c\_device\_desc::mrl](structi3c__device__desc.md#ac0ec89782c8df7e2e0debf061c754a7e)

uint16\_t mrl

Maximum Read Length.

**Definition** i3c.h:1032

[i3c\_device\_desc::pid](structi3c__device__desc.md#ac82bd8eccc52a98df76506bd2bed3961)

const uint64\_t pid

Device Provisioned ID.

**Definition** i3c.h:927

[i3c\_device\_desc::maxrd](structi3c__device__desc.md#ad570493d49084708bf35e9774bc99523)

uint8\_t maxrd

Maximum Read Speed.

**Definition** i3c.h:1021

[i3c\_device\_desc::bcr](structi3c__device__desc.md#ae1cff0a31d9cc5d7b18206556f8e0b21)

uint8\_t bcr

Bus Characteristic Register (BCR).

**Definition** i3c.h:1009

[i3c\_device\_desc::dcr](structi3c__device__desc.md#aee6342edbc47c478aa39b8330fab0d9c)

uint8\_t dcr

Device Characteristic Register (DCR).

**Definition** i3c.h:1017

[i3c\_device\_desc::bus](structi3c__device__desc.md#affdfa3b12a01f966ba5a6a563e669803)

const struct device \*const bus

Used to attach this node onto a linked list.

**Definition** i3c.h:921

[i3c\_device\_id](structi3c__device__id.md)

Structure used for matching I3C devices.

**Definition** i3c.h:876

[i3c\_device\_id::pid](structi3c__device__id.md#a254a43360f3eb8be2f62ed0ae48b8637)

const uint64\_t pid

Device Provisioned ID.

**Definition** i3c.h:878

[i3c\_driver\_config](structi3c__driver__config.md)

This structure is common to all I3C drivers and is expected to be the first element in the object poi...

**Definition** i3c.h:1175

[i3c\_driver\_config::dev\_list](structi3c__driver__config.md#aaa79d44e949dfdfe51e3994c08837193)

struct i3c\_dev\_list dev\_list

I3C/I2C device list struct.

**Definition** i3c.h:1177

[i3c\_driver\_data](structi3c__driver__data.md)

This structure is common to all I3C drivers and is expected to be the first element in the driver's s...

**Definition** i3c.h:1184

[i3c\_driver\_data::ctrl\_config](structi3c__driver__data.md#a00fc23f3b070cdfce304c015b4409cbb)

struct i3c\_config\_controller ctrl\_config

Controller Configuration.

**Definition** i3c.h:1186

[i3c\_driver\_data::attached\_dev](structi3c__driver__data.md#ae64e0be2d004d67900c11adf46630901)

struct i3c\_dev\_attached\_list attached\_dev

Attached I3C/I2C devices and addresses.

**Definition** i3c.h:1189

[i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md)

Structure describing a I2C device on I3C bus.

**Definition** i3c.h:1070

[i3c\_i2c\_device\_desc::bus](structi3c__i2c__device__desc.md#a2c37ea680bc4affe83f9e1bd1a1da5d2)

const struct device \* bus

Used to attach this node onto a linked list.

**Definition** i3c.h:1080

[i3c\_i2c\_device\_desc::addr](structi3c__i2c__device__desc.md#a5826aa935faccf9b9f05cf52b2fb842d)

const uint16\_t addr

Static address for this I2C device.

**Definition** i3c.h:1083

[i3c\_i2c\_device\_desc::lvr](structi3c__i2c__device__desc.md#a672aca260630deed5d8cdf90896d1115)

const uint8\_t lvr

Legacy Virtual Register (LVR).

**Definition** i3c.h:1099

[i3c\_ibi](structi3c__ibi.md)

Struct for IBI request.

**Definition** ibi.h:57

[i3c\_msg](structi3c__msg.md)

One I3C Message.

**Definition** i3c.h:473

[i3c\_msg::flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217)

uint8\_t flags

Flags for this message.

**Definition** i3c.h:490

[i3c\_msg::hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9)

uint8\_t hdr\_mode

HDR mode (I3C\_MSG\_HDR\_MODE\*) for transfer if any I3C\_MSG\_HDR\_\* is set in flags.

**Definition** i3c.h:498

[i3c\_msg::num\_xfer](structi3c__msg.md#a572d9f55461561fb9a8c31e46f0ebfe5)

uint32\_t num\_xfer

Total number of bytes transferred.

**Definition** i3c.h:487

[i3c\_msg::buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff)

uint8\_t \* buf

Data buffer in bytes.

**Definition** i3c.h:475

[i3c\_msg::len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0)

uint32\_t len

Length of buffer in bytes.

**Definition** i3c.h:478

[i3c\_target\_config](structi3c__target__config.md)

Structure describing a device that supports the I3C target API.

**Definition** target\_device.h:92

[target\_device.h](target__device_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c.h](i3c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
