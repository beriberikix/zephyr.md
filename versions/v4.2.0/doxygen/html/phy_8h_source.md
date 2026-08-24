---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/phy_8h_source.html
original_path: doxygen/html/phy_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

phy.h

[Go to the documentation of this file.](phy_8h.md)

1

6

7/\*

8 \* Copyright (c) 2021 IP-Logix Inc.

9 \* Copyright 2022 NXP

10 \* Copyright (c) 2025 Aerlync Labs Inc.

11 \*

12 \* SPDX-License-Identifier: Apache-2.0

13 \*/

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_

16

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

28#include <[errno.h](errno_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 35](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68)enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) {

[ 37](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c) [LINK\_HALF\_10BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 39](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c) [LINK\_FULL\_10BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 41](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d) [LINK\_HALF\_100BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 43](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956) [LINK\_FULL\_100BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 45](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec) [LINK\_HALF\_1000BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 47](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04) [LINK\_FULL\_1000BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 49](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e) [LINK\_FULL\_2500BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 51](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6) [LINK\_FULL\_5000BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

52};

53

[ 61](group__ethernet__phy.md#ga7dcf0d74db291bf0922c8ceb34307558)#define PHY\_LINK\_IS\_FULL\_DUPLEX(x) \

62 (x & (LINK\_FULL\_10BASE | LINK\_FULL\_100BASE | LINK\_FULL\_1000BASE | LINK\_FULL\_2500BASE | \

63 LINK\_FULL\_5000BASE))

64

[ 72](group__ethernet__phy.md#ga49f0673ace36bb3bac3e0c820a1f4de0)#define PHY\_LINK\_IS\_SPEED\_1000M(x) (x & (LINK\_HALF\_1000BASE | LINK\_FULL\_1000BASE))

73

[ 81](group__ethernet__phy.md#ga35acfd5ebec25784cc1c5b6be7be6a05)#define PHY\_LINK\_IS\_SPEED\_100M(x) (x & (LINK\_HALF\_100BASE | LINK\_FULL\_100BASE))

82

[ 90](group__ethernet__phy.md#gabee5b68903eb89190289d88ecff74de7)#define PHY\_LINK\_IS\_SPEED\_10M(x) (x & (LINK\_HALF\_10BASE | LINK\_FULL\_10BASE))

91

[ 93](structphy__link__state.md)struct [phy\_link\_state](structphy__link__state.md) {

[ 95](structphy__link__state.md#ab47802265dcf47b0aa815f4579467b6f) enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) [speed](structphy__link__state.md#ab47802265dcf47b0aa815f4579467b6f);

[ 97](structphy__link__state.md#aaced7164c07c5f964c952c2b04d68395) bool [is\_up](structphy__link__state.md#aaced7164c07c5f964c952c2b04d68395);

98};

99

[ 101](group__ethernet__phy.md#ga6221da76ffca235eafa291b90eab0d93)enum [phy\_cfg\_link\_flag](group__ethernet__phy.md#ga6221da76ffca235eafa291b90eab0d93) {

[ 103](group__ethernet__phy.md#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009) [PHY\_FLAG\_AUTO\_NEGOTIATION\_DISABLED](group__ethernet__phy.md#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

104};

105

[ 107](structphy__plca__cfg.md)struct [phy\_plca\_cfg](structphy__plca__cfg.md) {

[ 109](structphy__plca__cfg.md#a2c5eafc46d4869f11336094657978879) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structphy__plca__cfg.md#a2c5eafc46d4869f11336094657978879);

[ 111](structphy__plca__cfg.md#a3f8580797874684e64fed0bd9bf25a94) bool [enable](structphy__plca__cfg.md#a3f8580797874684e64fed0bd9bf25a94);

[ 113](structphy__plca__cfg.md#a7b98e4e26e7571aa7e4d1a99d81ea84a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_id](structphy__plca__cfg.md#a7b98e4e26e7571aa7e4d1a99d81ea84a);

[ 115](structphy__plca__cfg.md#a22346f28e7959b87038e938b169e670a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_count](structphy__plca__cfg.md#a22346f28e7959b87038e938b169e670a);

[ 117](structphy__plca__cfg.md#a841b0ab053ea1903e8d0756f2ec6be87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_count](structphy__plca__cfg.md#a841b0ab053ea1903e8d0756f2ec6be87);

[ 119](structphy__plca__cfg.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_timer](structphy__plca__cfg.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca);

[ 121](structphy__plca__cfg.md#a0be4e9b562c9baabff0fb8c91868e549) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [to\_timer](structphy__plca__cfg.md#a0be4e9b562c9baabff0fb8c91868e549);

122};

123

[ 135](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f)int [genphy\_get\_plca\_cfg](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

136

[ 148](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca)int [genphy\_set\_plca\_cfg](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

149

[ 161](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722)int [genphy\_get\_plca\_sts](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722)(const struct [device](structdevice.md) \*dev, bool \*plca\_status);

162

[ 172](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)typedef void (\*[phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4))(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

173 void \*user\_data);

174

181\_\_subsystem struct ethphy\_driver\_api {

183 int (\*get\_link)(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

184

186 int (\*cfg\_link)(const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) adv\_speeds,

187 enum [phy\_cfg\_link\_flag](group__ethernet__phy.md#ga6221da76ffca235eafa291b90eab0d93) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

188

192 int (\*link\_cb\_set)(const struct [device](structdevice.md) \*dev, [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) cb, void \*user\_data);

193

195 int (\*read)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

196

198 int (\*write)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

199

201 int (\*read\_c45)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

202

204 int (\*write\_c45)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

205

206 /\* Set PLCA settings \*/

207 int (\*set\_plca\_cfg)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

208

209 /\* Get PLCA settings \*/

210 int (\*get\_plca\_cfg)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

211

212 /\* Get PLCA status \*/

213 int (\*get\_plca\_sts)(const struct [device](structdevice.md) \*dev, bool \*plca\_sts);

214};

218

[ 233](group__ethernet__phy.md#gafce454d5da52532e4588324752c5cec3)static inline int [phy\_configure\_link](group__ethernet__phy.md#gafce454d5da52532e4588324752c5cec3)(const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) speeds,

234 enum [phy\_cfg\_link\_flag](group__ethernet__phy.md#ga6221da76ffca235eafa291b90eab0d93) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

235{

236 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->cfg\_link == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

237 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

238 }

239

240 /\* Check if only one speed is set, when auto-negotiation is disabled \*/

241 if (([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [PHY\_FLAG\_AUTO\_NEGOTIATION\_DISABLED](group__ethernet__phy.md#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009)) && ![IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(speeds)) {

242 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

243 }

244

245 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->cfg\_link(dev, speeds, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

246}

247

[ 261](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)static inline int [phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

262{

263 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->get\_link == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

264 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

265 }

266

267 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->get\_link(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

268}

269

[ 288](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)static inline int [phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)(const struct [device](structdevice.md) \*dev, [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) callback,

289 void \*user\_data)

290{

291 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->link\_cb\_set == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

292 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

293 }

294

295 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->link\_cb\_set(dev, callback, user\_data);

296}

297

[ 310](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)static inline int [phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value)

311{

312 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->read == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

313 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

314 }

315

316 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->read(dev, reg\_addr, value);

317}

318

[ 331](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)static inline int [phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

332{

333 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->write == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

334 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

335 }

336

337 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->write(dev, reg\_addr, value);

338}

339

[ 353](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796)static inline int [phy\_read\_c45](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

354 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

355{

356 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->read\_c45 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

357 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

358 }

359

360 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->read\_c45(dev, devad, regad, [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

361}

362

[ 376](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3)static inline int [phy\_write\_c45](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

377 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

378{

379 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->write\_c45 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

380 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

381 }

382

383 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->write\_c45(dev, devad, regad, [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

384}

385

[ 397](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc)static inline int [phy\_set\_plca\_cfg](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg)

398{

399 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->set\_plca\_cfg == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

400 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

401 }

402

403 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->set\_plca\_cfg(dev, plca\_cfg);

404}

405

[ 417](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f)static inline int [phy\_get\_plca\_cfg](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg)

418{

419 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->get\_plca\_cfg == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

420 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

421 }

422

423 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->get\_plca\_cfg(dev, plca\_cfg);

424}

425

[ 437](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312)static inline int [phy\_get\_plca\_sts](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312)(const struct [device](structdevice.md) \*dev, bool \*plca\_status)

438{

439 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->get\_plca\_sts == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

440 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

441 }

442

443 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(ethphy, dev)->get\_plca\_sts(dev, plca\_status);

444}

445

446#ifdef \_\_cplusplus

447}

448#endif

449

453

454#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_ \*/

[device.h](device_8h.md)

[DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)

#define DEVICE\_API\_GET(\_class, \_dev)

Expands to the pointer of a device's API for a given class.

**Definition** device.h:1350

[errno.h](errno_8h.md)

System error numbers.

[phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)

static int phy\_link\_callback\_set(const struct device \*dev, phy\_callback\_t callback, void \*user\_data)

Set link state change callback.

**Definition** phy.h:288

[genphy\_get\_plca\_cfg](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f)

int genphy\_get\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Write PHY PLCA configuration.

[phy\_set\_plca\_cfg](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc)

static int phy\_set\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Write PHY PLCA configuration.

**Definition** phy.h:397

[phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)

void(\* phy\_callback\_t)(const struct device \*dev, struct phy\_link\_state \*state, void \*user\_data)

Define the callback function signature for phy\_link\_callback\_set() function.

**Definition** phy.h:172

[phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)

static int phy\_read(const struct device \*dev, uint16\_t reg\_addr, uint32\_t \*value)

Read PHY registers.

**Definition** phy.h:310

[phy\_write\_c45](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3)

static int phy\_write\_c45(const struct device \*dev, uint8\_t devad, uint16\_t regad, uint16\_t data)

Write PHY C45 register.

**Definition** phy.h:376

[phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)

static int phy\_get\_link\_state(const struct device \*dev, struct phy\_link\_state \*state)

Get PHY link state.

**Definition** phy.h:261

[phy\_read\_c45](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796)

static int phy\_read\_c45(const struct device \*dev, uint8\_t devad, uint16\_t regad, uint16\_t \*data)

Read PHY C45 register.

**Definition** phy.h:353

[phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)

static int phy\_write(const struct device \*dev, uint16\_t reg\_addr, uint32\_t value)

Write PHY register.

**Definition** phy.h:331

[phy\_cfg\_link\_flag](group__ethernet__phy.md#ga6221da76ffca235eafa291b90eab0d93)

phy\_cfg\_link\_flag

Ethernet configure link flags.

**Definition** phy.h:101

[phy\_get\_plca\_sts](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312)

static int phy\_get\_plca\_sts(const struct device \*dev, bool \*plca\_status)

Read PHY PLCA status.

**Definition** phy.h:437

[genphy\_set\_plca\_cfg](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca)

int genphy\_set\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Read PHY PLCA configuration.

[phy\_get\_plca\_cfg](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f)

static int phy\_get\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Read PHY PLCA configuration.

**Definition** phy.h:417

[phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68)

phy\_link\_speed

Ethernet link speeds.

**Definition** phy.h:35

[genphy\_get\_plca\_sts](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722)

int genphy\_get\_plca\_sts(const struct device \*dev, bool \*plca\_status)

Read PHY PLCA status.

[phy\_configure\_link](group__ethernet__phy.md#gafce454d5da52532e4588324752c5cec3)

static int phy\_configure\_link(const struct device \*dev, enum phy\_link\_speed speeds, enum phy\_cfg\_link\_flag flags)

Configure PHY link.

**Definition** phy.h:233

[PHY\_FLAG\_AUTO\_NEGOTIATION\_DISABLED](group__ethernet__phy.md#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009)

@ PHY\_FLAG\_AUTO\_NEGOTIATION\_DISABLED

Auto-negotiation disable.

**Definition** phy.h:103

[LINK\_HALF\_10BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)

@ LINK\_HALF\_10BASE

10Base Half-Duplex

**Definition** phy.h:37

[LINK\_FULL\_2500BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)

@ LINK\_FULL\_2500BASE

2.5GBase Full-Duplex

**Definition** phy.h:49

[LINK\_FULL\_10BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)

@ LINK\_FULL\_10BASE

10Base Full-Duplex

**Definition** phy.h:39

[LINK\_HALF\_100BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)

@ LINK\_HALF\_100BASE

100Base Half-Duplex

**Definition** phy.h:41

[LINK\_FULL\_1000BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)

@ LINK\_FULL\_1000BASE

1000Base Full-Duplex

**Definition** phy.h:47

[LINK\_HALF\_1000BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)

@ LINK\_HALF\_1000BASE

1000Base Half-Duplex

**Definition** phy.h:45

[LINK\_FULL\_5000BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)

@ LINK\_FULL\_5000BASE

5GBase Full-Duplex

**Definition** phy.h:51

[LINK\_FULL\_100BASE](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)

@ LINK\_FULL\_100BASE

100Base Full-Duplex

**Definition** phy.h:43

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)

#define IS\_POWER\_OF\_TWO(x)

Check if a x is a power of two.

**Definition** util\_macro.h:77

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

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

**Definition** device.h:510

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:520

[phy\_link\_state](structphy__link__state.md)

Link state.

**Definition** phy.h:93

[phy\_link\_state::is\_up](structphy__link__state.md#aaced7164c07c5f964c952c2b04d68395)

bool is\_up

When true the link is active and connected.

**Definition** phy.h:97

[phy\_link\_state::speed](structphy__link__state.md#ab47802265dcf47b0aa815f4579467b6f)

enum phy\_link\_speed speed

Link speed.

**Definition** phy.h:95

[phy\_plca\_cfg](structphy__plca__cfg.md)

PLCA (Physical Layer Collision Avoidance) Reconciliation Sublayer configurations.

**Definition** phy.h:107

[phy\_plca\_cfg::to\_timer](structphy__plca__cfg.md#a0be4e9b562c9baabff0fb8c91868e549)

uint8\_t to\_timer

PLCA to\_timer in bit-times, which determines the PLCA transmit opportunity.

**Definition** phy.h:121

[phy\_plca\_cfg::node\_count](structphy__plca__cfg.md#a22346f28e7959b87038e938b169e670a)

uint8\_t node\_count

PLCA node count.

**Definition** phy.h:115

[phy\_plca\_cfg::version](structphy__plca__cfg.md#a2c5eafc46d4869f11336094657978879)

uint8\_t version

PLCA register map version.

**Definition** phy.h:109

[phy\_plca\_cfg::enable](structphy__plca__cfg.md#a3f8580797874684e64fed0bd9bf25a94)

bool enable

PLCA configured mode (enable/disable).

**Definition** phy.h:111

[phy\_plca\_cfg::node\_id](structphy__plca__cfg.md#a7b98e4e26e7571aa7e4d1a99d81ea84a)

uint8\_t node\_id

PLCA local node identifier.

**Definition** phy.h:113

[phy\_plca\_cfg::burst\_count](structphy__plca__cfg.md#a841b0ab053ea1903e8d0756f2ec6be87)

uint8\_t burst\_count

Additional frames a node is allowed to send in single transmit opportunity (TO).

**Definition** phy.h:117

[phy\_plca\_cfg::burst\_timer](structphy__plca__cfg.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca)

uint8\_t burst\_timer

Wait time for the MAC to send a new frame before interrupting the burst.

**Definition** phy.h:119

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [phy.h](phy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
