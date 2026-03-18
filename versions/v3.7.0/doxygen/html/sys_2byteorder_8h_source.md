---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sys_2byteorder_8h_source.html
original_path: doxygen/html/sys_2byteorder_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

16#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

17#include <[zephyr/toolchain.h](toolchain_8h.md)>

18

[ 19](sys_2byteorder_8h.md#ab2cc6513b37ec58689c48cec167d3485)#define BSWAP\_16(x) ((uint16\_t) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8)))

[ 20](sys_2byteorder_8h.md#a0f16b3ee6b8adca36048becb05ff7393)#define BSWAP\_24(x) ((uint32\_t) ((((x) >> 16) & 0xff) | \

21 (((x)) & 0xff00) | \

22 (((x) & 0xff) << 16)))

[ 23](sys_2byteorder_8h.md#accb24612c7ee9b52e4006eced1b45ff3)#define BSWAP\_32(x) ((uint32\_t) ((((x) >> 24) & 0xff) | \

24 (((x) >> 8) & 0xff00) | \

25 (((x) & 0xff00) << 8) | \

26 (((x) & 0xff) << 24)))

[ 27](sys_2byteorder_8h.md#a9220598b1562f6458a1f3cdace730086)#define BSWAP\_40(x) ((uint64\_t) ((((x) >> 32) & 0xff) | \

28 (((x) >> 16) & 0xff00) | \

29 (((x)) & 0xff0000) | \

30 (((x) & 0xff00) << 16) | \

31 (((x) & 0xff) << 32)))

[ 32](sys_2byteorder_8h.md#acdd30009239c79bd4b997fa1dcbd555f)#define BSWAP\_48(x) ((uint64\_t) ((((x) >> 40) & 0xff) | \

33 (((x) >> 24) & 0xff00) | \

34 (((x) >> 8) & 0xff0000) | \

35 (((x) & 0xff0000) << 8) | \

36 (((x) & 0xff00) << 24) | \

37 (((x) & 0xff) << 40)))

[ 38](sys_2byteorder_8h.md#adcf23836f6eaeff620cb63f43042e546)#define BSWAP\_64(x) ((uint64\_t) ((((x) >> 56) & 0xff) | \

39 (((x) >> 40) & 0xff00) | \

40 (((x) >> 24) & 0xff0000) | \

41 (((x) >> 8) & 0xff000000) | \

42 (((x) & 0xff000000) << 8) | \

43 (((x) & 0xff0000) << 24) | \

44 (((x) & 0xff00) << 40) | \

45 (((x) & 0xff) << 56)))

46

54

62

70

78

86

94

102

110

118

126

134

142

150

158

166

174

187

201

217

218#ifdef CONFIG\_LITTLE\_ENDIAN

219#define sys\_le16\_to\_cpu(val) (val)

220#define sys\_cpu\_to\_le16(val) (val)

221#define sys\_le24\_to\_cpu(val) (val)

222#define sys\_cpu\_to\_le24(val) (val)

223#define sys\_le32\_to\_cpu(val) (val)

224#define sys\_cpu\_to\_le32(val) (val)

225#define sys\_le40\_to\_cpu(val) (val)

226#define sys\_cpu\_to\_le40(val) (val)

227#define sys\_le48\_to\_cpu(val) (val)

228#define sys\_cpu\_to\_le48(val) (val)

229#define sys\_le64\_to\_cpu(val) (val)

230#define sys\_cpu\_to\_le64(val) (val)

231#define sys\_be16\_to\_cpu(val) BSWAP\_16(val)

232#define sys\_cpu\_to\_be16(val) BSWAP\_16(val)

233#define sys\_be24\_to\_cpu(val) BSWAP\_24(val)

234#define sys\_cpu\_to\_be24(val) BSWAP\_24(val)

235#define sys\_be32\_to\_cpu(val) BSWAP\_32(val)

236#define sys\_cpu\_to\_be32(val) BSWAP\_32(val)

237#define sys\_be40\_to\_cpu(val) BSWAP\_40(val)

238#define sys\_cpu\_to\_be40(val) BSWAP\_40(val)

239#define sys\_be48\_to\_cpu(val) BSWAP\_48(val)

240#define sys\_cpu\_to\_be48(val) BSWAP\_48(val)

241#define sys\_be64\_to\_cpu(val) BSWAP\_64(val)

242#define sys\_cpu\_to\_be64(val) BSWAP\_64(val)

243

244#define sys\_uint16\_to\_array(val) { \

245 ((val) & 0xff), \

246 (((val) >> 8) & 0xff)}

247

248#define sys\_uint32\_to\_array(val) { \

249 ((val) & 0xff), \

250 (((val) >> 8) & 0xff), \

251 (((val) >> 16) & 0xff), \

252 (((val) >> 24) & 0xff)}

253

254#define sys\_uint64\_to\_array(val) { \

255 ((val) & 0xff), \

256 (((val) >> 8) & 0xff), \

257 (((val) >> 16) & 0xff), \

258 (((val) >> 24) & 0xff), \

259 (((val) >> 32) & 0xff), \

260 (((val) >> 40) & 0xff), \

261 (((val) >> 48) & 0xff), \

262 (((val) >> 56) & 0xff)}

263

264#else

[ 265](sys_2byteorder_8h.md#ae4176f3e082f21488dedcd02b406cb43)#define sys\_le16\_to\_cpu(val) BSWAP\_16(val)

[ 266](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)#define sys\_cpu\_to\_le16(val) BSWAP\_16(val)

[ 267](sys_2byteorder_8h.md#a0e7342005eb6840186a59c006a719c0d)#define sys\_le24\_to\_cpu(val) BSWAP\_24(val)

[ 268](sys_2byteorder_8h.md#a85bae5c9bd6e58923d97ef41b7fd2055)#define sys\_cpu\_to\_le24(val) BSWAP\_24(val)

[ 269](sys_2byteorder_8h.md#aa713ea0f2e2c64c05bd4a3596e44ce4e)#define sys\_le32\_to\_cpu(val) BSWAP\_32(val)

[ 270](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)#define sys\_cpu\_to\_le32(val) BSWAP\_32(val)

[ 271](sys_2byteorder_8h.md#a7a60d7b88a76e722e6b7f6f790c9d6ba)#define sys\_le40\_to\_cpu(val) BSWAP\_40(val)

[ 272](sys_2byteorder_8h.md#af1b10bdf8927f7d089e9e5241b1c280f)#define sys\_cpu\_to\_le40(val) BSWAP\_40(val)

[ 273](sys_2byteorder_8h.md#ae34388c412959f7af9e233dbe81fbbe0)#define sys\_le48\_to\_cpu(val) BSWAP\_48(val)

[ 274](sys_2byteorder_8h.md#ad9f886d1a9ffe95fc5e1e9eb4e39c532)#define sys\_cpu\_to\_le48(val) BSWAP\_48(val)

[ 275](sys_2byteorder_8h.md#a3d4737fab89f1762e518630090db8368)#define sys\_le64\_to\_cpu(val) BSWAP\_64(val)

[ 276](sys_2byteorder_8h.md#a8730241a4c5701f689ac0ac1255331c7)#define sys\_cpu\_to\_le64(val) BSWAP\_64(val)

[ 277](sys_2byteorder_8h.md#a840037a5fd3d36817dc92a44469df704)#define sys\_be16\_to\_cpu(val) (val)

[ 278](sys_2byteorder_8h.md#a9e2c7b19bbba5343ee8c5f9740484a56)#define sys\_cpu\_to\_be16(val) (val)

[ 279](sys_2byteorder_8h.md#afbe8be1a0842354ab076b2530ef9a041)#define sys\_be24\_to\_cpu(val) (val)

[ 280](sys_2byteorder_8h.md#ab441316429ce3604ec359f2a20c76431)#define sys\_cpu\_to\_be24(val) (val)

[ 281](sys_2byteorder_8h.md#aee4cefae7f089197e77c487faafda269)#define sys\_be32\_to\_cpu(val) (val)

[ 282](sys_2byteorder_8h.md#a508d3b125adf1d30e8411381827c4f05)#define sys\_cpu\_to\_be32(val) (val)

[ 283](sys_2byteorder_8h.md#aa0d7790b5838d6df8c5483dcdfd7882b)#define sys\_be40\_to\_cpu(val) (val)

[ 284](sys_2byteorder_8h.md#af91f379aa31af2094ed46281e1097f73)#define sys\_cpu\_to\_be40(val) (val)

[ 285](sys_2byteorder_8h.md#a93e948095f79ab51368f193472d5b030)#define sys\_be48\_to\_cpu(val) (val)

[ 286](sys_2byteorder_8h.md#abb089029e2e84ce70bee82b18341273d)#define sys\_cpu\_to\_be48(val) (val)

[ 287](sys_2byteorder_8h.md#abb4d263f2b9b1cbf1c8fbaec714fc411)#define sys\_be64\_to\_cpu(val) (val)

[ 288](sys_2byteorder_8h.md#a6ac423744c21c1e40aabd7ecb9b9e8d5)#define sys\_cpu\_to\_be64(val) (val)

289

[ 290](sys_2byteorder_8h.md#aa85342d9fd48f33f91bf0c37d993b120)#define sys\_uint16\_to\_array(val) { \

291 (((val) >> 8) & 0xff), \

292 ((val) & 0xff)}

293

[ 294](sys_2byteorder_8h.md#a0cd4ca8ebebe4b3759252b936a3fdd3f)#define sys\_uint32\_to\_array(val) { \

295 (((val) >> 24) & 0xff), \

296 (((val) >> 16) & 0xff), \

297 (((val) >> 8) & 0xff), \

298 ((val) & 0xff)}

299

[ 300](sys_2byteorder_8h.md#a96ac1537a710d9fd88a5280bce3b5a04)#define sys\_uint64\_to\_array(val) { \

301 (((val) >> 56) & 0xff), \

302 (((val) >> 48) & 0xff), \

303 (((val) >> 40) & 0xff), \

304 (((val) >> 32) & 0xff), \

305 (((val) >> 24) & 0xff), \

306 (((val) >> 16) & 0xff), \

307 (((val) >> 8) & 0xff), \

308 ((val) & 0xff)}

309

310#endif

311

[ 321](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)static inline void [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[2])

322{

323 dst[0] = val >> 8;

324 dst[1] = val;

325}

326

[ 336](sys_2byteorder_8h.md#a7aa82f69d08ebde8077fc3d2ebfbc53b)static inline void [sys\_put\_be24](sys_2byteorder_8h.md#a7aa82f69d08ebde8077fc3d2ebfbc53b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[3])

337{

338 dst[0] = val >> 16;

339 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val, &dst[1]);

340}

341

[ 351](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)static inline void [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4])

352{

353 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val >> 16, dst);

354 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val, &dst[2]);

355}

356

[ 365](sys_2byteorder_8h.md#ae08c9ac9238729a6a4449fa375f0f701)static inline void [sys\_put\_be40](sys_2byteorder_8h.md#ae08c9ac9238729a6a4449fa375f0f701)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[5])

366{

367 dst[0] = val >> 32;

368 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val, &dst[1]);

369}

370

[ 380](sys_2byteorder_8h.md#abe8d617e8a5469c303a512fe94a55443)static inline void [sys\_put\_be48](sys_2byteorder_8h.md#abe8d617e8a5469c303a512fe94a55443)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[6])

381{

382 [sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)(val >> 32, dst);

383 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val, &dst[2]);

384}

385

[ 395](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)static inline void [sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[8])

396{

397 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val >> 32, dst);

398 [sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)(val, &dst[4]);

399}

400

[ 410](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)static inline void [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[2])

411{

412 dst[0] = val;

413 dst[1] = val >> 8;

414}

415

[ 425](sys_2byteorder_8h.md#a10bdc6fccf288e1d5215dba9c031c730)static inline void [sys\_put\_le24](sys_2byteorder_8h.md#a10bdc6fccf288e1d5215dba9c031c730)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[3])

426{

427 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val, dst);

428 dst[2] = val >> 16;

429}

430

[ 440](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)static inline void [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4])

441{

442 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val, dst);

443 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val >> 16, &dst[2]);

444}

445

[ 455](sys_2byteorder_8h.md#aba15200a89744a6799040d230241263d)static inline void [sys\_put\_le40](sys_2byteorder_8h.md#aba15200a89744a6799040d230241263d)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[5])

456{

457 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val, dst);

458 dst[4] = val >> 32;

459}

460

[ 470](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)static inline void [sys\_put\_le48](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[6])

471{

472 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val, dst);

473 [sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)(val >> 32, &dst[4]);

474}

475

[ 485](sys_2byteorder_8h.md#a7d89d4b4b278fefa3e65fc6c3894a70c)static inline void [sys\_put\_le64](sys_2byteorder_8h.md#a7d89d4b4b278fefa3e65fc6c3894a70c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[8])

486{

487 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val, dst);

488 [sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)(val >> 32, &dst[4]);

489}

490

[ 501](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[2])

502{

503 return (([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))src[0] << 8) | src[1];

504}

505

[ 516](sys_2byteorder_8h.md#ac65e83f46ef042862b675995f74fcd9b)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_be24](sys_2byteorder_8h.md#ac65e83f46ef042862b675995f74fcd9b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[3])

517{

518 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))src[0] << 16) | [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[1]);

519}

520

[ 531](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[4])

532{

533 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[0]) << 16) | [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[2]);

534}

535

[ 546](sys_2byteorder_8h.md#a9004452841790b59b4cdc3579b1f583d)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_be40](sys_2byteorder_8h.md#a9004452841790b59b4cdc3579b1f583d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[5])

547{

548 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[0]) << 8) | src[4];

549}

550

[ 561](sys_2byteorder_8h.md#acf0fa9761998529910e022b80126ff6b)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_be48](sys_2byteorder_8h.md#acf0fa9761998529910e022b80126ff6b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[6])

562{

563 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[0]) << 16) | [sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)(&src[4]);

564}

565

[ 576](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[8])

577{

578 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[0]) << 32) | [sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)(&src[4]);

579}

580

[ 591](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[2])

592{

593 return (([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))src[1] << 8) | src[0];

594}

595

[ 606](sys_2byteorder_8h.md#aa75ded65c52f8308de46670b78339b7c)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_le24](sys_2byteorder_8h.md#aa75ded65c52f8308de46670b78339b7c)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[3])

607{

608 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))src[2] << 16) | [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[0]);

609}

610

[ 621](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[4])

622{

623 return (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))[sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[2]) << 16) | [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[0]);

624}

625

[ 636](sys_2byteorder_8h.md#a080573b0bfb1328111fd16ba9926280b)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_le40](sys_2byteorder_8h.md#a080573b0bfb1328111fd16ba9926280b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[5])

637{

638 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[1]) << 8) | src[0];

639}

640

[ 651](sys_2byteorder_8h.md#a601c3cefbdfd8befa336339a87fd70fd)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_le48](sys_2byteorder_8h.md#a601c3cefbdfd8befa336339a87fd70fd)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[6])

652{

653 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[2]) << 16) | [sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)(&src[0]);

654}

655

[ 666](sys_2byteorder_8h.md#a678b08370e157ce5eb7117832aa86408)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_get\_le64](sys_2byteorder_8h.md#a678b08370e157ce5eb7117832aa86408)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[8])

667{

668 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[4]) << 32) | [sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)(&src[0]);

669}

670

[ 684](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)static inline void [sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)(void \*dst, const void \*src, size\_t length)

685{

686 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pdst = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)dst;

687 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*psrc = (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)src;

688

689 \_\_ASSERT(((psrc < pdst && (psrc + length) <= pdst) ||

690 (psrc > pdst && (pdst + length) <= psrc)),

691 "Source and destination buffers must not overlap");

692

693 psrc += length - 1;

694

695 for (; length > 0; length--) {

696 \*pdst++ = \*psrc--;

697 }

698}

699

[ 710](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)static inline void [sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)(void \*buf, size\_t length)

711{

712 size\_t i;

713

714 for (i = 0; i < (length/2); i++) {

715 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tmp = (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[i];

716

717 (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[i] = (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[length - 1 - i];

718 (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf)[length - 1 - i] = tmp;

719 }

720}

721

722#endif /\* ZEPHYR\_INCLUDE\_SYS\_BYTEORDER\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

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

[sys\_memcpy\_swap](sys_2byteorder_8h.md#a00935c7276235df4c16dd0f9ef524e67)

static void sys\_memcpy\_swap(void \*dst, const void \*src, size\_t length)

Swap one buffer content into another.

**Definition** byteorder.h:684

[sys\_get\_le40](sys_2byteorder_8h.md#a080573b0bfb1328111fd16ba9926280b)

static uint64\_t sys\_get\_le40(const uint8\_t src[5])

Get a 40-bit integer stored in little-endian format.

**Definition** byteorder.h:636

[sys\_put\_le24](sys_2byteorder_8h.md#a10bdc6fccf288e1d5215dba9c031c730)

static void sys\_put\_le24(uint32\_t val, uint8\_t dst[3])

Put a 24-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:425

[sys\_put\_be32](sys_2byteorder_8h.md#a21f25ff68591217034f3414594425286)

static void sys\_put\_be32(uint32\_t val, uint8\_t dst[4])

Put a 32-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:351

[sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)

static void sys\_put\_be64(uint64\_t val, uint8\_t dst[8])

Put a 64-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:395

[sys\_get\_be32](sys_2byteorder_8h.md#a4db31229c7a8a80dace3870664b6442d)

static uint32\_t sys\_get\_be32(const uint8\_t src[4])

Get a 32-bit integer stored in big-endian format.

**Definition** byteorder.h:531

[sys\_get\_le16](sys_2byteorder_8h.md#a5c2c537b960a29bdd29133f902a67f6a)

static uint16\_t sys\_get\_le16(const uint8\_t src[2])

Get a 16-bit integer stored in little-endian format.

**Definition** byteorder.h:591

[sys\_get\_le48](sys_2byteorder_8h.md#a601c3cefbdfd8befa336339a87fd70fd)

static uint64\_t sys\_get\_le48(const uint8\_t src[6])

Get a 48-bit integer stored in little-endian format.

**Definition** byteorder.h:651

[sys\_get\_le64](sys_2byteorder_8h.md#a678b08370e157ce5eb7117832aa86408)

static uint64\_t sys\_get\_le64(const uint8\_t src[8])

Get a 64-bit integer stored in little-endian format.

**Definition** byteorder.h:666

[sys\_put\_be16](sys_2byteorder_8h.md#a68df8f14dfc0d8715d16ac87dd4c73d2)

static void sys\_put\_be16(uint16\_t val, uint8\_t dst[2])

Put a 16-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:321

[sys\_put\_be24](sys_2byteorder_8h.md#a7aa82f69d08ebde8077fc3d2ebfbc53b)

static void sys\_put\_be24(uint32\_t val, uint8\_t dst[3])

Put a 24-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:336

[sys\_put\_le64](sys_2byteorder_8h.md#a7d89d4b4b278fefa3e65fc6c3894a70c)

static void sys\_put\_le64(uint64\_t val, uint8\_t dst[8])

Put a 64-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:485

[sys\_get\_be40](sys_2byteorder_8h.md#a9004452841790b59b4cdc3579b1f583d)

static uint64\_t sys\_get\_be40(const uint8\_t src[5])

Get a 40-bit integer stored in big-endian format.

**Definition** byteorder.h:546

[sys\_get\_be16](sys_2byteorder_8h.md#a91fae25b12126c2b35d240f56866184d)

static uint16\_t sys\_get\_be16(const uint8\_t src[2])

Get a 16-bit integer stored in big-endian format.

**Definition** byteorder.h:501

[sys\_put\_le48](sys_2byteorder_8h.md#aa6950654cc7fd67ab4f83235da59665a)

static void sys\_put\_le48(uint64\_t val, uint8\_t dst[6])

Put a 48-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:470

[sys\_get\_le32](sys_2byteorder_8h.md#aa7422f922db351d2da1d52195d43b8a4)

static uint32\_t sys\_get\_le32(const uint8\_t src[4])

Get a 32-bit integer stored in little-endian format.

**Definition** byteorder.h:621

[sys\_get\_le24](sys_2byteorder_8h.md#aa75ded65c52f8308de46670b78339b7c)

static uint32\_t sys\_get\_le24(const uint8\_t src[3])

Get a 24-bit integer stored in little-endian format.

**Definition** byteorder.h:606

[sys\_put\_le40](sys_2byteorder_8h.md#aba15200a89744a6799040d230241263d)

static void sys\_put\_le40(uint64\_t val, uint8\_t dst[5])

Put a 40-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:455

[sys\_put\_be48](sys_2byteorder_8h.md#abe8d617e8a5469c303a512fe94a55443)

static void sys\_put\_be48(uint64\_t val, uint8\_t dst[6])

Put a 48-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:380

[sys\_get\_be24](sys_2byteorder_8h.md#ac65e83f46ef042862b675995f74fcd9b)

static uint32\_t sys\_get\_be24(const uint8\_t src[3])

Get a 24-bit integer stored in big-endian format.

**Definition** byteorder.h:516

[sys\_get\_be48](sys_2byteorder_8h.md#acf0fa9761998529910e022b80126ff6b)

static uint64\_t sys\_get\_be48(const uint8\_t src[6])

Get a 48-bit integer stored in big-endian format.

**Definition** byteorder.h:561

[sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)

static uint64\_t sys\_get\_be64(const uint8\_t src[8])

Get a 64-bit integer stored in big-endian format.

**Definition** byteorder.h:576

[sys\_put\_be40](sys_2byteorder_8h.md#ae08c9ac9238729a6a4449fa375f0f701)

static void sys\_put\_be40(uint64\_t val, uint8\_t dst[5])

Put a 40-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:365

[sys\_mem\_swap](sys_2byteorder_8h.md#ae86b6050e71ec755abb284be3a02d28a)

static void sys\_mem\_swap(void \*buf, size\_t length)

Swap buffer content.

**Definition** byteorder.h:710

[sys\_put\_le16](sys_2byteorder_8h.md#af8f30219c861bb07d097374204d386dd)

static void sys\_put\_le16(uint16\_t val, uint8\_t dst[2])

Put a 16-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:410

[sys\_put\_le32](sys_2byteorder_8h.md#aff60d0dcda6a48df4ea248f898a92de0)

static void sys\_put\_le32(uint32\_t val, uint8\_t dst[4])

Put a 32-bit integer as little-endian to arbitrary location.

**Definition** byteorder.h:440

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [byteorder.h](sys_2byteorder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
