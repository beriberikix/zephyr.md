---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/crc_8h_source.html
original_path: doxygen/html/crc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crc.h

[Go to the documentation of this file.](crc_8h.md)

1/\*

2 \* Copyright (c) 2018 Workaround GmbH.

3 \* Copyright (c) 2017 Intel Corporation.

4 \* Copyright (c) 2017 Nordic Semiconductor ASA

5 \* Copyright (c) 2015 Runtime Inc

6 \* Copyright (c) 2018 Google LLC.

7 \* Copyright (c) 2022 Meta

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

14

15#ifndef ZEPHYR\_INCLUDE\_SYS\_CRC\_H\_

16#define ZEPHYR\_INCLUDE\_SYS\_CRC\_H\_

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[stdbool.h](stdbool_8h.md)>

20#include <stddef.h>

21

22#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28/\* Initial value expected to be used at the beginning of the crc8\_ccitt

29 \* computation.

30 \*/

[ 31](crc_8h.md#a95b298c826cf96507e7b11a49c75b2cf)#define CRC8\_CCITT\_INITIAL\_VALUE 0xFF

32

37

43

[ 49](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd)enum [crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) {

[ 50](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) [CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22),

[ 51](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f) [CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f),

[ 52](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a) [CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a),

[ 53](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) [CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8),

[ 54](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb) [CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb),

[ 55](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) [CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11),

[ 56](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) [CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6),

[ 57](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30) [CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30),

[ 58](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c) [CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c),

[ 59](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148) [CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148),

[ 60](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8) [CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8),

61};

62

[ 82](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

83

[ 112](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

[ 128](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value,

129 bool reversed);

130

[ 162](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

163

[ 199](group__crc.md#ga5502729e443496719de338e8b6692ac1)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

200

[ 212](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_ansi](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len)

213{

214 return [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)(0xA001, 0xffff, src, len);

215}

216

[ 226](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

227

[ 238](group__crc.md#ga17476d4af14603e322986ef603ce8530)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_ieee\_update](group__crc.md#ga17476d4af14603e322986ef603ce8530)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

239

[ 252](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_c](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

253 size\_t len, bool first\_pkt, bool last\_pkt);

254

[ 266](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc8\_ccitt](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, size\_t len);

267

[ 281](group__crc.md#ga1169005fd900b2787035044eeea38af1)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc7\_be](group__crc.md#ga1169005fd900b2787035044eeea38af1)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

282

[ 296](group__crc.md#ga322365098ec65bde3d55b0c059896668)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc4\_ti](group__crc.md#ga322365098ec65bde3d55b0c059896668)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

297

[ 315](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc4](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value,

316 bool reversed);

317

[ 340](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc\_by\_type](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33)(enum [crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len,

341 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seed, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) poly, bool reflect, bool first,

342 bool last)

343{

344 switch (type) {

345 case [CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22):

346 return [crc4](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)(src, len, poly, seed, reflect);

347 case [CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f):

348 return [crc4\_ti](group__crc.md#ga322365098ec65bde3d55b0c059896668)(seed, src, len);

349 case [CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a):

350 return [crc7\_be](group__crc.md#ga1169005fd900b2787035044eeea38af1)(seed, src, len);

351 case [CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8):

352 return [crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)(src, len, poly, seed, reflect);

353 case [CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb):

354 return [crc8\_ccitt](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)(seed, src, len);

355 case [CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11):

356 if (reflect) {

357 return [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)(poly, seed, src, len);

358 } else {

359 return [crc16](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)(poly, seed, src, len);

360 }

361 case [CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6):

362 return [crc16\_ansi](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)(src, len);

363 case [CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30):

364 return [crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)(seed, src, len);

365 case [CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c):

366 return [crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1)(seed, src, len);

367 case [CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148):

368 return [crc32\_c](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)(seed, src, len, first, last);

369 case [CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8):

370 return [crc32\_ieee\_update](group__crc.md#ga17476d4af14603e322986ef603ce8530)(seed, src, len);

371 default:

372 break;

373 }

374

375 \_\_ASSERT\_NO\_MSG(false);

376 return -1;

377}

378

382

383#ifdef \_\_cplusplus

384}

385#endif

386

387#endif

[\_\_assert.h](____assert_8h.md)

[crc7\_be](group__crc.md#ga1169005fd900b2787035044eeea38af1)

uint8\_t crc7\_be(uint8\_t seed, const uint8\_t \*src, size\_t len)

Compute the CRC-7 checksum of a buffer.

[crc32\_ieee\_update](group__crc.md#ga17476d4af14603e322986ef603ce8530)

uint32\_t crc32\_ieee\_update(uint32\_t crc, const uint8\_t \*data, size\_t len)

Update an IEEE conforming CRC32 checksum.

[crc16](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)

uint16\_t crc16(uint16\_t poly, uint16\_t seed, const uint8\_t \*src, size\_t len)

Generic function for computing a CRC-16 without input or output reflection.

[crc4\_ti](group__crc.md#ga322365098ec65bde3d55b0c059896668)

uint8\_t crc4\_ti(uint8\_t seed, const uint8\_t \*src, size\_t len)

Compute the CRC-4 checksum of a buffer.

[crc4](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)

uint8\_t crc4(const uint8\_t \*src, size\_t len, uint8\_t polynomial, uint8\_t initial\_value, bool reversed)

Generic function for computing CRC 4.

[crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1)

uint16\_t crc16\_itu\_t(uint16\_t seed, const uint8\_t \*src, size\_t len)

Compute the checksum of a buffer with polynomial 0x1021, no reflection of input or output.

[crc\_by\_type](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33)

static uint32\_t crc\_by\_type(enum crc\_type type, const uint8\_t \*src, size\_t len, uint32\_t seed, uint32\_t poly, bool reflect, bool first, bool last)

Compute a CRC checksum, in a generic way.

**Definition** crc.h:340

[crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)

uint16\_t crc16\_ccitt(uint16\_t seed, const uint8\_t \*src, size\_t len)

Compute the checksum of a buffer with polynomial 0x1021, reflecting input and output.

[crc32\_c](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)

uint32\_t crc32\_c(uint32\_t crc, const uint8\_t \*data, size\_t len, bool first\_pkt, bool last\_pkt)

Calculate CRC32C (Castagnoli) checksum.

[crc8\_ccitt](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)

uint8\_t crc8\_ccitt(uint8\_t initial\_value, const void \*buf, size\_t len)

Compute CCITT variant of CRC 8.

[crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)

uint8\_t crc8(const uint8\_t \*src, size\_t len, uint8\_t polynomial, uint8\_t initial\_value, bool reversed)

Generic function for computing CRC 8.

[crc16\_ansi](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)

static uint16\_t crc16\_ansi(const uint8\_t \*src, size\_t len)

Compute the ANSI (or Modbus) variant of CRC-16.

**Definition** crc.h:212

[crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd)

crc\_type

CRC algorithm enumeration.

**Definition** crc.h:49

[crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)

uint16\_t crc16\_reflect(uint16\_t poly, uint16\_t seed, const uint8\_t \*src, size\_t len)

Generic function for computing a CRC-16 with input and output reflection.

[crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)

uint32\_t crc32\_ieee(const uint8\_t \*data, size\_t len)

Generate IEEE conform CRC32 checksum.

[CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a)

@ CRC7\_BE

Use crc7\_be.

**Definition** crc.h:52

[CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11)

@ CRC16

Use crc16.

**Definition** crc.h:55

[CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f)

@ CRC4\_TI

Use crc4\_ti.

**Definition** crc.h:51

[CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c)

@ CRC16\_ITU\_T

Use crc16\_itu\_t.

**Definition** crc.h:58

[CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148)

@ CRC32\_C

Use crc32\_c.

**Definition** crc.h:59

[CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6)

@ CRC16\_ANSI

Use crc16\_ansi.

**Definition** crc.h:56

[CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8)

@ CRC8

Use crc8.

**Definition** crc.h:53

[CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30)

@ CRC16\_CCITT

Use crc16\_ccitt.

**Definition** crc.h:57

[CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb)

@ CRC8\_CCITT

Use crc8\_ccitt.

**Definition** crc.h:54

[CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8)

@ CRC32\_IEEE

Use crc32\_ieee.

**Definition** crc.h:60

[CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22)

@ CRC4

Use crc4.

**Definition** crc.h:50

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [crc.h](crc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
