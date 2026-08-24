---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/crc_8h_source.html
original_path: doxygen/html/crc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

8 \* Copyright (c) 2024 Intercreate, Inc.

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

15

16#ifndef ZEPHYR\_INCLUDE\_SYS\_CRC\_H\_

17#define ZEPHYR\_INCLUDE\_SYS\_CRC\_H\_

18

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[stdbool.h](stdbool_8h.md)>

21#include <stddef.h>

22

23#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29/\* Initial value expected to be used at the beginning of the crc8\_ccitt

30 \* computation.

31 \*/

[ 32](crc_8h.md#a95b298c826cf96507e7b11a49c75b2cf)#define CRC8\_CCITT\_INITIAL\_VALUE 0xFF

[ 33](crc_8h.md#a81e9e87b5f1705b252429981f49608ee)#define CRC8\_ROHC\_INITIAL\_VALUE 0xFF

34

35/\* Initial value expected to be used at the beginning of the OpenPGP CRC-24 computation. \*/

[ 36](crc_8h.md#a0f92c37af2ac3af5cbea2c2f259d0639)#define CRC24\_PGP\_INITIAL\_VALUE 0x00B704CEU

37/\*

38 \* The CRC-24 value is stored on a 32-bit value, only the 3 least significant bytes

39 \* are meaningful. Use the following mask to only keep the CRC-24 value.

40 \*/

[ 41](crc_8h.md#a9075e7134000a6fd75ea81b0c2b0218b)#define CRC24\_FINAL\_VALUE\_MASK 0x00FFFFFFU

42

47

53

[ 59](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd)enum [crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) {

[ 60](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) [CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22),

[ 61](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f) [CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f),

[ 62](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a) [CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a),

[ 63](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) [CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8),

[ 64](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb) [CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb),

[ 65](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5) [CRC8\_ROHC](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5),

[ 66](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) [CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11),

[ 67](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) [CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6),

[ 68](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30) [CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30),

[ 69](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c) [CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c),

[ 70](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43) [CRC24\_PGP](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43),

[ 71](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148) [CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148),

[ 72](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8) [CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8),

[ 73](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b) [CRC32\_K\_4\_2](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b),

74};

75

[ 95](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

96

[ 125](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

[ 141](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value,

142 bool reversed);

143

[ 175](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

176

[ 212](group__crc.md#ga5502729e443496719de338e8b6692ac1)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

213

[ 225](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [crc16\_ansi](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len)

226{

227 return [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)(0xA001, 0xffff, src, len);

228}

229

[ 239](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

240

[ 251](group__crc.md#ga17476d4af14603e322986ef603ce8530)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_ieee\_update](group__crc.md#ga17476d4af14603e322986ef603ce8530)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

252

[ 265](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_c](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

266 size\_t len, bool first\_pkt, bool last\_pkt);

267

[ 292](group__crc.md#gaba2e753d07e6b17b5330ee56aa48962d)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc32\_k\_4\_2\_update](group__crc.md#gaba2e753d07e6b17b5330ee56aa48962d)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

293

[ 305](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc8\_ccitt](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, size\_t len);

306

[ 319](group__crc.md#ga7a8f4387a2d0163165557446d018f041)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc8\_rohc](group__crc.md#ga7a8f4387a2d0163165557446d018f041)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, size\_t len);

320

[ 334](group__crc.md#ga1169005fd900b2787035044eeea38af1)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc7\_be](group__crc.md#ga1169005fd900b2787035044eeea38af1)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

335

[ 349](group__crc.md#ga322365098ec65bde3d55b0c059896668)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc4\_ti](group__crc.md#ga322365098ec65bde3d55b0c059896668)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len);

350

[ 368](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc4](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value,

369 bool reversed);

370

[ 379](group__crc.md#gaebe7a9494dec69568b4f5cc95bf0fac2)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc24\_pgp](group__crc.md#gaebe7a9494dec69568b4f5cc95bf0fac2)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

380

[ 392](group__crc.md#ga4523b3cf8dbc05ea44258d1652fbb969)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc24\_pgp\_update](group__crc.md#ga4523b3cf8dbc05ea44258d1652fbb969)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

393

[ 416](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crc\_by\_type](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33)(enum [crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, size\_t len,

417 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seed, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) poly, bool reflect, bool first,

418 bool last)

419{

420 switch (type) {

421 case [CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22):

422 return [crc4](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456)(src, len, poly, seed, reflect);

423 case [CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f):

424 return [crc4\_ti](group__crc.md#ga322365098ec65bde3d55b0c059896668)(seed, src, len);

425 case [CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a):

426 return [crc7\_be](group__crc.md#ga1169005fd900b2787035044eeea38af1)(seed, src, len);

427 case [CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8):

428 return [crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6)(src, len, poly, seed, reflect);

429 case [CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb):

430 return [crc8\_ccitt](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5)(seed, src, len);

431 case [CRC8\_ROHC](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5):

432 return [crc8\_rohc](group__crc.md#ga7a8f4387a2d0163165557446d018f041)(seed, src, len);

433 case [CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11):

434 if (reflect) {

435 return [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)(poly, seed, src, len);

436 } else {

437 return [crc16](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c)(poly, seed, src, len);

438 }

439 case [CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6):

440 return [crc16\_ansi](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a)(src, len);

441 case [CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30):

442 return [crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)(seed, src, len);

443 case [CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c):

444 return [crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1)(seed, src, len);

445 case [CRC24\_PGP](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43): {

446 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc = [crc24\_pgp\_update](group__crc.md#ga4523b3cf8dbc05ea44258d1652fbb969)(seed, src, len);

447

448 if (last) {

449 crc &= [CRC24\_FINAL\_VALUE\_MASK](crc_8h.md#a9075e7134000a6fd75ea81b0c2b0218b);

450 }

451 return crc;

452 }

453 case [CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148):

454 return [crc32\_c](group__crc.md#ga88d510b3958aee0990ca345aba260bc1)(seed, src, len, first, last);

455 case [CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8):

456 return [crc32\_ieee\_update](group__crc.md#ga17476d4af14603e322986ef603ce8530)(seed, src, len);

457 case [CRC32\_K\_4\_2](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b):

458 return [crc32\_k\_4\_2\_update](group__crc.md#gaba2e753d07e6b17b5330ee56aa48962d)(seed, src, len);

459 default:

460 break;

461 }

462

463 \_\_ASSERT\_NO\_MSG(false);

464 return -1;

465}

466

470

471#ifdef \_\_cplusplus

472}

473#endif

474

475#endif

[\_\_assert.h](____assert_8h.md)

[CRC24\_FINAL\_VALUE\_MASK](crc_8h.md#a9075e7134000a6fd75ea81b0c2b0218b)

#define CRC24\_FINAL\_VALUE\_MASK

**Definition** crc.h:41

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

[crc24\_pgp\_update](group__crc.md#ga4523b3cf8dbc05ea44258d1652fbb969)

uint32\_t crc24\_pgp\_update(uint32\_t crc, const uint8\_t \*data, size\_t len)

Update an OpenPGP CRC-24 checksum.

[crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1)

uint16\_t crc16\_itu\_t(uint16\_t seed, const uint8\_t \*src, size\_t len)

Compute the checksum of a buffer with polynomial 0x1021, no reflection of input or output.

[crc\_by\_type](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33)

static uint32\_t crc\_by\_type(enum crc\_type type, const uint8\_t \*src, size\_t len, uint32\_t seed, uint32\_t poly, bool reflect, bool first, bool last)

Compute a CRC checksum, in a generic way.

**Definition** crc.h:416

[crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c)

uint16\_t crc16\_ccitt(uint16\_t seed, const uint8\_t \*src, size\_t len)

Compute the checksum of a buffer with polynomial 0x1021, reflecting input and output.

[crc8\_rohc](group__crc.md#ga7a8f4387a2d0163165557446d018f041)

uint8\_t crc8\_rohc(uint8\_t initial\_value, const void \*buf, size\_t len)

Compute ROHC variant of CRC 8.

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

**Definition** crc.h:225

[crc32\_k\_4\_2\_update](group__crc.md#gaba2e753d07e6b17b5330ee56aa48962d)

uint32\_t crc32\_k\_4\_2\_update(uint32\_t crc, const uint8\_t \*data, size\_t len)

Update a CRC-32K/4.2 (\*op) (Koopman) checksum.

[crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd)

crc\_type

CRC algorithm enumeration.

**Definition** crc.h:59

[crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914)

uint16\_t crc16\_reflect(uint16\_t poly, uint16\_t seed, const uint8\_t \*src, size\_t len)

Generic function for computing a CRC-16 with input and output reflection.

[crc24\_pgp](group__crc.md#gaebe7a9494dec69568b4f5cc95bf0fac2)

uint32\_t crc24\_pgp(const uint8\_t \*data, size\_t len)

Generate an OpenPGP CRC-24 checksum as defined in RFC 4880 section 6.1.

[crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982)

uint32\_t crc32\_ieee(const uint8\_t \*data, size\_t len)

Generate IEEE conform CRC32 checksum.

[CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a)

@ CRC7\_BE

Use crc7\_be.

**Definition** crc.h:62

[CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11)

@ CRC16

Use crc16.

**Definition** crc.h:66

[CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f)

@ CRC4\_TI

Use crc4\_ti.

**Definition** crc.h:61

[CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c)

@ CRC16\_ITU\_T

Use crc16\_itu\_t.

**Definition** crc.h:69

[CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148)

@ CRC32\_C

Use crc32\_c.

**Definition** crc.h:71

[CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6)

@ CRC16\_ANSI

Use crc16\_ansi.

**Definition** crc.h:67

[CRC32\_K\_4\_2](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b)

@ CRC32\_K\_4\_2

Use crc32\_k\_4\_2\_update.

**Definition** crc.h:73

[CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8)

@ CRC8

Use crc8.

**Definition** crc.h:63

[CRC24\_PGP](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43)

@ CRC24\_PGP

Use crc24\_pgp.

**Definition** crc.h:70

[CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30)

@ CRC16\_CCITT

Use crc16\_ccitt.

**Definition** crc.h:68

[CRC8\_ROHC](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5)

@ CRC8\_ROHC

Use crc8\_rohc.

**Definition** crc.h:65

[CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb)

@ CRC8\_CCITT

Use crc8\_ccitt.

**Definition** crc.h:64

[CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8)

@ CRC32\_IEEE

Use crc32\_ieee.

**Definition** crc.h:72

[CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22)

@ CRC4

Use crc4.

**Definition** crc.h:60

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
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
