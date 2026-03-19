---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sys_2byteorder_8h_source.html
original_path: doxygen/html/sys_2byteorder_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

byteorder.h

[Go to the documentation of this file.](sys_2byteorder_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016, Intel Corporation.

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_SYS\_BYTEORDER\_H\_

12#define ZEPHYR\_INCLUDE\_SYS\_BYTEORDER\_H\_

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15#include <stddef.h>

16#include <[string.h](string_8h.md)>

17#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

18#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

19#include <[zephyr/toolchain.h](toolchain_8h.md)>

20

[ 21](sys_2byteorder_8h.md#ab2cc6513b37ec58689c48cec167d3485)#define BSWAP\_16(x) ((uint16\_t) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8)))

[ 22](sys_2byteorder_8h.md#a0f16b3ee6b8adca36048becb05ff7393)#define BSWAP\_24(x) ((uint32\_t) ((((x) >> 16) & 0xff) | \

23 (((x)) & 0xff00) | \

24 (((x) & 0xff) << 16)))

[ 25](sys_2byteorder_8h.md#accb24612c7ee9b52e4006eced1b45ff3)#define BSWAP\_32(x) ((uint32\_t) ((((x) >> 24) & 0xff) | \

26 (((x) >> 8) & 0xff00) | \

27 (((x) & 0xff00) << 8) | \

28 (((x) & 0xff) << 24)))

[ 29](sys_2byteorder_8h.md#a9220598b1562f6458a1f3cdace730086)#define BSWAP\_40(x) ((uint64\_t) ((((x) >> 32) & 0xff) | \

30 (((x) >> 16) & 0xff00) | \

31 (((x)) & 0xff0000) | \

32 (((x) & 0xff00) << 16) | \

33 (((x) & 0xff) << 32)))

[ 34](sys_2byteorder_8h.md#acdd30009239c79bd4b997fa1dcbd555f)#define BSWAP\_48(x) ((uint64\_t) ((((x) >> 40) & 0xff) | \

35 (((x) >> 24) & 0xff00) | \

36 (((x) >> 8) & 0xff0000) | \

37 (((x) & 0xff0000) << 8) | \

38 (((x) & 0xff00) << 24) | \

39 (((x) & 0xff) << 40)))

[ 40](sys_2byteorder_8h.md#adcf23836f6eaeff620cb63f43042e546)#define BSWAP\_64(x) ((uint64\_t) ((((x) >> 56) & 0xff) | \

41 (((x) >> 40) & 0xff00) | \

42 (((x) >> 24) & 0xff0000) | \

43 (((x) >> 8) & 0xff000000) | \

44 (((x) & 0xff000000) << 8) | \

45 (((x) & 0xff0000) << 24) | \

46 (((x) & 0xff00) << 40) | \

47 (((x) & 0xff) << 56)))

48

56

64

72

80

88

96

104

112

120

128

136

144

152

160

168

176

189

203

219

220#ifdef CONFIG\_LITTLE\_ENDIAN

221#define sys\_le16\_to\_cpu(val) (val)

222#define sys\_cpu\_to\_le16(val) (val)

223#define sys\_le24\_to\_cpu(val) (val)

224#define sys\_cpu\_to\_le24(val) (val)

225#define sys\_le32\_to\_cpu(val) (val)

226#define sys\_cpu\_to\_le32(val) (val)

227#define sys\_le40\_to\_cpu(val) (val)

228#define sys\_cpu\_to\_le40(val) (val)

229#define sys\_le48\_to\_cpu(val) (val)

230#define sys\_cpu\_to\_le48(val) (val)

231#define sys\_le64\_to\_cpu(val) (val)

232#define sys\_cpu\_to\_le64(val) (val)

233#define sys\_be16\_to\_cpu(val) BSWAP\_16(val)

234#define sys\_cpu\_to\_be16(val) BSWAP\_16(val)

235#define sys\_be24\_to\_cpu(val) BSWAP\_24(val)

236#define sys\_cpu\_to\_be24(val) BSWAP\_24(val)

237#define sys\_be32\_to\_cpu(val) BSWAP\_32(val)

238#define sys\_cpu\_to\_be32(val) BSWAP\_32(val)

239#define sys\_be40\_to\_cpu(val) BSWAP\_40(val)

240#define sys\_cpu\_to\_be40(val) BSWAP\_40(val)

241#define sys\_be48\_to\_cpu(val) BSWAP\_48(val)

242#define sys\_cpu\_to\_be48(val) BSWAP\_48(val)

243#define sys\_be64\_to\_cpu(val) BSWAP\_64(val)

244#define sys\_cpu\_to\_be64(val) BSWAP\_64(val)

245

246#define sys\_uint16\_to\_array(val) { \

247 ((val) & 0xff), \

248 (((val) >> 8) & 0xff)}

249

250#define sys\_uint32\_to\_array(val) { \

251 ((val) & 0xff), \

252 (((val) >> 8) & 0xff), \

253 (((val) >> 16) & 0xff), \

254 (((val) >> 24) & 0xff)}

255

256#define sys\_uint64\_to\_array(val) { \

257 ((val) & 0xff), \

258 (((val) >> 8) & 0xff), \

259 (((val) >> 16) & 0xff), \

260 (((val) >> 24) & 0xff), \

261 (((val) >> 32) & 0xff), \

262 (((val) >> 40) & 0xff), \

263 (((val) >> 48) & 0xff), \

264 (((val) >> 56) & 0xff)}

265

266#else

[ 267](sys_2byteorder_8h.md#ae4176f3e082f21488dedcd02b406cb43)#define sys\_le16\_to\_cpu(val) BSWAP\_16(val)

[ 268](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)#define sys\_cpu\_to\_le16(val) BSWAP\_16(val)

[ 269](sys_2byteorder_8h.md#a0e7342005eb6840186a59c006a719c0d)#define sys\_le24\_to\_cpu(val) BSWAP\_24(val)

[ 270](sys_2byteorder_8h.md#a85bae5c9bd6e58923d97ef41b7fd2055)#define sys\_cpu\_to\_le24(val) BSWAP\_24(val)

[ 271](sys_2byteorder_8h.md#aa713ea0f2e2c64c05bd4a3596e44ce4e)#define sys\_le32\_to\_cpu(val) BSWAP\_32(val)

[ 272](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)#define sys\_cpu\_to\_le32(val) BSWAP\_32(val)

[ 273](sys_2byteorder_8h.md#a7a60d7b88a76e722e6b7f6f790c9d6ba)#define sys\_le40\_to\_cpu(val) BSWAP\_40(val)

[ 274](sys_2byteorder_8h.md#af1b10bdf8927f7d089e9e5241b1c280f)#define sys\_cpu\_to\_le40(val) BSWAP\_40(val)

[ 275](sys_2byteorder_8h.md#ae34388c412959f7af9e233dbe81fbbe0)#define sys\_le48\_to\_cpu(val) BSWAP\_48(val)

[ 276](sys_2byteorder_8h.md#ad9f886d1a9ffe95fc5e1e9eb4e39c532)#define sys\_cpu\_to\_le48(val) BSWAP\_48(val)

[ 277](sys_2byteorder_8h.md#a3d4737fab89f1762e518630090db8368)#define sys\_le64\_to\_cpu(val) BSWAP\_64(val)

[ 278](sys_2byteorder_8h.md#a8730241a4c5701f689ac0ac1255331c7)#define sys\_cpu\_to\_le64(val) BSWAP\_64(val)

[ 279](sys_2byteorder_8h.md#a840037a5fd3d36817dc92a44469df704)#define sys\_be16\_to\_cpu(val) (val)

[ 280](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)#define sys\_cpu\_to\_be16(val) (val)

[ 281](sys_2byteorder_8h.md#afbe8be1a0842354ab076b2530ef9a041)#define sys\_be24\_to\_cpu(val) (val)

[ 282](sys_2byteorder_8h.md#ab441316429ce3604ec359f2a20c76431)#define sys\_cpu\_to\_be24(val) (val)

[ 283](sys_2byteorder_8h.md#aee4cefae7f089197e77c487faafda269)#define sys\_be32\_to\_cpu(val) (val)

[ 284](sys_2byteorder_8h.md#a508d3b125adf1d30e8411381827c4f05)#define sys\_cpu\_to\_be32(val) (val)

[ 285](sys_2byteorder_8h.md#aa0d7790b5838d6df8c5483dcdfd7882b)#define sys\_be40\_to\_cpu(val) (val)

[ 286](sys_2byteorder_8h.md#af91f379aa31af2094ed46281e1097f73)#define sys\_cpu\_to\_be40(val) (val)

[ 287](sys_2byteorder_8h.md#a93e948095f79ab51368f193472d5b030)#define sys\_be48\_to\_cpu(val) (val)

[ 288](sys_2byteorder_8h.md#abb089029e2e84ce70bee82b18341273d)#define sys\_cpu\_to\_be48(val) (val)

[ 289](sys_2byteorder_8h.md#abb4d263f2b9b1cbf1c8fbaec714fc411)#define sys\_be64\_to\_cpu(val) (val)

[ 290](sys_2byteorder_8h.md#a6ac423744c21c1e40aabd7ecb9b9e8d5)#define sys\_cpu\_to\_be64(val) (val)

291

[ 292](sys_2byteorder_8h.md#aa85342d9fd48f33f91bf0c37d993b120)#define sys\_uint16\_to\_array(val) { \

293 (((val) >> 8) & 0xff), \

294 ((val) & 0xff)}

295

[ 296](sys_2byteorder_8h.md#a0cd4ca8ebebe4b3759252b936a3fdd3f)#define sys\_uint32\_to\_array(val) { \

297 (((val) >> 24) & 0xff), \

298 (((val) >> 16) & 0xff), \

299 (((val) >> 8) & 0xff), \

300 ((val) & 0xff)}

301

[ 302](sys_2byteorder_8h.md#a96ac1537a710d9fd88a5280bce3b5a04)#define sys\_uint64\_to\_array(val) { \

303 (((val) >> 56) & 0xff), \

304 (((val) >> 48) & 0xff), \

305 (((val) >> 40) & 0xff), \

306 (((val) >> 32) & 0xff), \

307 (((val) >> 24) & 0xff), \

308 (((val) >> 16) & 0xff), \

309 (((val) >> 8) & 0xff), \

310 ((val) & 0xff)}

311

312#endif

313

[ 323](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)static inline void [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[2])

324{

325 dst[0] = val >> 8;

326 dst[1] = val;

327}

328

[ 338](sys_2byteorder_8h.md#a7aa82f69d08ebde8077fc3d2ebfbc53b)static inline void [sys\_put\_be24](sys_2byteorder_8h.md#a7aa82f69d08ebde8077fc3d2ebfbc53b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[3])

339{

340 dst[0] = val >> 16;

341 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val, &dst[1]);

342}

343

[ 353](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)static inline void [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4])

354{

355 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val >> 16, dst);

356 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val, &dst[2]);

357}

358

[ 367](sys_2byteorder_8h.md#ae08c9ac9238729a6a4449fa375f0f701)static inline void [sys\_put\_be40](sys_2byteorder_8h.md#ae08c9ac9238729a6a4449fa375f0f701)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[5])

368{

369 dst[0] = val >> 32;

370 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val, &dst[1]);

371}

372

[ 382](sys_2byteorder_8h.md#abe8d617e8a5469c303a512fe94a55443)static inline void [sys\_put\_be48](sys_2byteorder_8h.md#abe8d617e8a5469c303a512fe94a55443)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[6])

383{

384 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val >> 32, dst);

385 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val, &dst[2]);

386}

387

[ 397](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)static inline void [sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[8])

398{

399 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val >> 32, dst);

400 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val, &dst[4]);

401}

402

[ 412](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)static inline void [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[2])

413{

414 dst[0] = val;

415 dst[1] = val >> 8;

416}

417

[ 427](sys_2byteorder_8h.md#a10bdc6fccf288e1d5215dba9c031c730)static inline void [sys\_put\_le24](sys_2byteorder_8h.md#a10bdc6fccf288e1d5215dba9c031c730)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[3])

428{

429 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val, dst);

430 dst[2] = val >> 16;

431}

432

[ 442](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)static inline void [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4])

443{

444 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val, dst);

445 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val >> 16, &dst[2]);

446}

447

[ 457](sys_2byteorder_8h.md#aba15200a89744a6799040d230241263d)static inline void [sys\_put\_le40](sys_2byteorder_8h.md#aba15200a89744a6799040d230241263d)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[5])

458{

459 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val, dst);

460 dst[4] = val >> 32;

461}

462

[ 472](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)static inline void [sys\_put\_le48](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[6])

473{

474 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val, dst);

475 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val >> 32, &dst[4]);

476}

477

[ 487](sys_2byteorder_8h.md#a7d89d4b4b278fefa3e65fc6c3894a70c)static inline void [sys\_put\_le64](sys_2byteorder_8h.md#a7d89d4b4b278fefa3e65fc6c3894a70c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[8])

488{

489 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val, dst);

490 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val >> 32, &dst[4]);

491}

492

[ 503](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[2])

504{

505 return (([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))src[0] << 8) | src[1];

506}

507

[ 518](sys_2byteorder_8h.md#ac65e83f46ef042862b675995f74fcd9b)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_be24](sys_2byteorder_8h.md#ac65e83f46ef042862b675995f74fcd9b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[3])

519{

520 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))src[0] << 16) | [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[1]);

521}

522

[ 533](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[4])

534{

535 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[0]) << 16) | [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[2]);

536}

537

[ 548](sys_2byteorder_8h.md#a9004452841790b59b4cdc3579b1f583d)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_be40](sys_2byteorder_8h.md#a9004452841790b59b4cdc3579b1f583d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[5])

549{

550 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[0]) << 8) | src[4];

551}

552

[ 563](sys_2byteorder_8h.md#acf0fa9761998529910e022b80126ff6b)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_be48](sys_2byteorder_8h.md#acf0fa9761998529910e022b80126ff6b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[6])

564{

565 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[0]) << 16) | [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[4]);

566}

567

[ 578](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[8])

579{

580 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[0]) << 32) | [sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[4]);

581}

582

[ 593](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[2])

594{

595 return (([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))src[1] << 8) | src[0];

596}

597

[ 608](sys_2byteorder_8h.md#aa75ded65c52f8308de46670b78339b7c)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_le24](sys_2byteorder_8h.md#aa75ded65c52f8308de46670b78339b7c)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[3])

609{

610 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))src[2] << 16) | [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[0]);

611}

612

[ 623](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[4])

624{

625 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[2]) << 16) | [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[0]);

626}

627

[ 638](sys_2byteorder_8h.md#a080573b0bfb1328111fd16ba9926280b)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_le40](sys_2byteorder_8h.md#a080573b0bfb1328111fd16ba9926280b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[5])

639{

640 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[1]) << 8) | src[0];

641}

642

[ 653](sys_2byteorder_8h.md#a601c3cefbdfd8befa336339a87fd70fd)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_le48](sys_2byteorder_8h.md#a601c3cefbdfd8befa336339a87fd70fd)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[6])

654{

655 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[2]) << 16) | [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[0]);

656}

657

[ 668](sys_2byteorder_8h.md#a678b08370e157ce5eb7117832aa86408)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_le64](sys_2byteorder_8h.md#a678b08370e157ce5eb7117832aa86408)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[8])

669{

670 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[4]) << 32) | [sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[0]);

671}

672

[ 686](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)static inline void [sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)(void \*dst, const void \*src, size\_t length)

687{

688 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pdst = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)dst;

689 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*psrc = (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)src;

690

691 \_\_ASSERT(((psrc < pdst && (psrc + length) <= pdst) ||

692 (psrc > pdst && (pdst + length) <= psrc)),

693 "Source and destination buffers must not overlap");

694

695 psrc += length - 1;

696

697 for (; length > 0; length--) {

698 \*pdst++ = \*psrc--;

699 }

700}

701

[ 712](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)static inline void [sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)(void \*buf, size\_t length)

713{

714 size\_t i;

715

716 for (i = 0; i < (length/2); i++) {

717 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tmp = (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[i];

718

719 (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[i] = (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[length - 1 - i];

720 (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[length - 1 - i] = tmp;

721 }

722}

723

[ 730](sys_2byteorder_8h.md#a1dfbe1844998a2532142661e6f83cd1c)static inline void [sys\_le\_to\_cpu](sys_2byteorder_8h.md#a1dfbe1844998a2532142661e6f83cd1c)(void \*buf, size\_t length)

731{

732 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BIG\_ENDIAN)) {

733 [sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)(buf, length);

734 }

735}

736

[ 743](sys_2byteorder_8h.md#a185a92952eb93c3b4171f814382e3c6c)static inline void [sys\_cpu\_to\_le](sys_2byteorder_8h.md#a185a92952eb93c3b4171f814382e3c6c)(void \*buf, size\_t length)

744{

745 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_BIG\_ENDIAN)) {

746 [sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)(buf, length);

747 }

748}

749

[ 756](sys_2byteorder_8h.md#a56104f3f100b7d74cc3a14d82d39e766)static inline void [sys\_be\_to\_cpu](sys_2byteorder_8h.md#a56104f3f100b7d74cc3a14d82d39e766)(void \*buf, size\_t length)

757{

758 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LITTLE\_ENDIAN)) {

759 [sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)(buf, length);

760 }

761}

762

[ 769](sys_2byteorder_8h.md#a470e5adb20ee21268358d1a758b32a14)static inline void [sys\_cpu\_to\_be](sys_2byteorder_8h.md#a470e5adb20ee21268358d1a758b32a14)(void \*buf, size\_t length)

770{

771 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LITTLE\_ENDIAN)) {

772 [sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)(buf, length);

773 }

774}

775

[ 786](sys_2byteorder_8h.md#a73d878abef7674b2c0f78f37725c57dd)static inline void [sys\_put\_le](sys_2byteorder_8h.md#a73d878abef7674b2c0f78f37725c57dd)(void \*dst, const void \*src, size\_t length)

787{

788 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LITTLE\_ENDIAN)) {

789 (void)[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst, src, length);

790 } else {

791 [sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)(dst, src, length);

792 }

793}

794

[ 805](sys_2byteorder_8h.md#af6e3a1a295b4f19f10581e5b655deb26)static inline void [sys\_put\_be](sys_2byteorder_8h.md#af6e3a1a295b4f19f10581e5b655deb26)(void \*dst, const void \*src, size\_t length)

806{

807 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LITTLE\_ENDIAN)) {

808 [sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)(dst, src, length);

809 } else {

810 (void)[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst, src, length);

811 }

812}

813

[ 824](sys_2byteorder_8h.md#aebf1dd355257a635d976fbe034ec470e)static inline void [sys\_get\_le](sys_2byteorder_8h.md#aebf1dd355257a635d976fbe034ec470e)(void \*dst, const void \*src, size\_t length)

825{

826 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LITTLE\_ENDIAN)) {

827 (void)[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst, src, length);

828 } else {

829 [sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)(dst, src, length);

830 }

831}

832

[ 843](sys_2byteorder_8h.md#a0674cde757cbe634bdd100fed9aabca8)static inline void [sys\_get\_be](sys_2byteorder_8h.md#a0674cde757cbe634bdd100fed9aabca8)(void \*dst, const void \*src, size\_t length)

844{

845 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LITTLE\_ENDIAN)) {

846 [sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)(dst, src, length);

847 } else {

848 (void)[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(dst, src, length);

849 }

850}

851

852#endif /\* ZEPHYR\_INCLUDE\_SYS\_BYTEORDER\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

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

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[string.h](string_8h.md)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)

static void sys\_memcpy\_swap(void \*dst, const void \*src, size\_t length)

Swap one buffer content into another.

**Definition** byteorder.h:686

[sys\_get\_be](sys_2byteorder_8h.md#a0674cde757cbe634bdd100fed9aabca8)

static void sys\_get\_be(void \*dst, const void \*src, size\_t length)

Get a buffer stored in big-endian format.

**Definition** byteorder.h:843

[sys\_get\_le40](sys_2byteorder_8h.md#a080573b0bfb1328111fd16ba9926280b)

static uint64\_t sys\_get\_le40(const uint8\_t src[5])

Get a 40-bit integer stored in little-endian format.

**Definition** byteorder.h:638

[sys\_put\_le24](sys_2byteorder_8h.md#a10bdc6fccf288e1d5215dba9c031c730)

static void sys\_put\_le24(uint32\_t val, uint8\_t dst[3])

Put a 24-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:427

[sys\_cpu\_to\_le](sys_2byteorder_8h.md#a185a92952eb93c3b4171f814382e3c6c)

static void sys\_cpu\_to\_le(void \*buf, size\_t length)

Convert buffer from host endianness to little-endian.

**Definition** byteorder.h:743

[sys\_le\_to\_cpu](sys_2byteorder_8h.md#a1dfbe1844998a2532142661e6f83cd1c)

static void sys\_le\_to\_cpu(void \*buf, size\_t length)

Convert buffer from little-endian to host endianness.

**Definition** byteorder.h:730

[sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)

static void sys\_put\_be32(uint32\_t val, uint8\_t dst[4])

Put a 32-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:353

[sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)

static void sys\_put\_be64(uint64\_t val, uint8\_t dst[8])

Put a 64-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:397

[sys\_cpu\_to\_be](sys_2byteorder_8h.md#a470e5adb20ee21268358d1a758b32a14)

static void sys\_cpu\_to\_be(void \*buf, size\_t length)

Convert buffer from host endianness to big-endian.

**Definition** byteorder.h:769

[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)

static uint32\_t sys\_get\_be32(const uint8\_t src[4])

Get a 32-bit integer stored in big-endian format.

**Definition** byteorder.h:533

[sys\_be\_to\_cpu](sys_2byteorder_8h.md#a56104f3f100b7d74cc3a14d82d39e766)

static void sys\_be\_to\_cpu(void \*buf, size\_t length)

Convert buffer from big-endian to host endianness.

**Definition** byteorder.h:756

[sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)

static uint16\_t sys\_get\_le16(const uint8\_t src[2])

Get a 16-bit integer stored in little-endian format.

**Definition** byteorder.h:593

[sys\_get\_le48](sys_2byteorder_8h.md#a601c3cefbdfd8befa336339a87fd70fd)

static uint64\_t sys\_get\_le48(const uint8\_t src[6])

Get a 48-bit integer stored in little-endian format.

**Definition** byteorder.h:653

[sys\_get\_le64](sys_2byteorder_8h.md#a678b08370e157ce5eb7117832aa86408)

static uint64\_t sys\_get\_le64(const uint8\_t src[8])

Get a 64-bit integer stored in little-endian format.

**Definition** byteorder.h:668

[sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)

static void sys\_put\_be16(uint16\_t val, uint8\_t dst[2])

Put a 16-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:323

[sys\_put\_le](sys_2byteorder_8h.md#a73d878abef7674b2c0f78f37725c57dd)

static void sys\_put\_le(void \*dst, const void \*src, size\_t length)

Put a buffer as little-endian to arbitrary location.

**Definition** byteorder.h:786

[sys\_put\_be24](sys_2byteorder_8h.md#a7aa82f69d08ebde8077fc3d2ebfbc53b)

static void sys\_put\_be24(uint32\_t val, uint8\_t dst[3])

Put a 24-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:338

[sys\_put\_le64](sys_2byteorder_8h.md#a7d89d4b4b278fefa3e65fc6c3894a70c)

static void sys\_put\_le64(uint64\_t val, uint8\_t dst[8])

Put a 64-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:487

[sys\_get\_be40](sys_2byteorder_8h.md#a9004452841790b59b4cdc3579b1f583d)

static uint64\_t sys\_get\_be40(const uint8\_t src[5])

Get a 40-bit integer stored in big-endian format.

**Definition** byteorder.h:548

[sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)

static uint16\_t sys\_get\_be16(const uint8\_t src[2])

Get a 16-bit integer stored in big-endian format.

**Definition** byteorder.h:503

[sys\_put\_le48](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)

static void sys\_put\_le48(uint64\_t val, uint8\_t dst[6])

Put a 48-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:472

[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)

static uint32\_t sys\_get\_le32(const uint8\_t src[4])

Get a 32-bit integer stored in little-endian format.

**Definition** byteorder.h:623

[sys\_get\_le24](sys_2byteorder_8h.md#aa75ded65c52f8308de46670b78339b7c)

static uint32\_t sys\_get\_le24(const uint8\_t src[3])

Get a 24-bit integer stored in little-endian format.

**Definition** byteorder.h:608

[sys\_put\_le40](sys_2byteorder_8h.md#aba15200a89744a6799040d230241263d)

static void sys\_put\_le40(uint64\_t val, uint8\_t dst[5])

Put a 40-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:457

[sys\_put\_be48](sys_2byteorder_8h.md#abe8d617e8a5469c303a512fe94a55443)

static void sys\_put\_be48(uint64\_t val, uint8\_t dst[6])

Put a 48-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:382

[sys\_get\_be24](sys_2byteorder_8h.md#ac65e83f46ef042862b675995f74fcd9b)

static uint32\_t sys\_get\_be24(const uint8\_t src[3])

Get a 24-bit integer stored in big-endian format.

**Definition** byteorder.h:518

[sys\_get\_be48](sys_2byteorder_8h.md#acf0fa9761998529910e022b80126ff6b)

static uint64\_t sys\_get\_be48(const uint8\_t src[6])

Get a 48-bit integer stored in big-endian format.

**Definition** byteorder.h:563

[sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)

static uint64\_t sys\_get\_be64(const uint8\_t src[8])

Get a 64-bit integer stored in big-endian format.

**Definition** byteorder.h:578

[sys\_put\_be40](sys_2byteorder_8h.md#ae08c9ac9238729a6a4449fa375f0f701)

static void sys\_put\_be40(uint64\_t val, uint8\_t dst[5])

Put a 40-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:367

[sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)

static void sys\_mem\_swap(void \*buf, size\_t length)

Swap buffer content.

**Definition** byteorder.h:712

[sys\_get\_le](sys_2byteorder_8h.md#aebf1dd355257a635d976fbe034ec470e)

static void sys\_get\_le(void \*dst, const void \*src, size\_t length)

Get a buffer stored in little-endian format.

**Definition** byteorder.h:824

[sys\_put\_be](sys_2byteorder_8h.md#af6e3a1a295b4f19f10581e5b655deb26)

static void sys\_put\_be(void \*dst, const void \*src, size\_t length)

Put a buffer as big-endian to arbitrary location.

**Definition** byteorder.h:805

[sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)

static void sys\_put\_le16(uint16\_t val, uint8\_t dst[2])

Put a 16-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:412

[sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)

static void sys\_put\_le32(uint32\_t val, uint8\_t dst[4])

Put a 32-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:442

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [byteorder.h](sys_2byteorder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
