---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/phy_8h_source.html
original_path: doxygen/html/phy_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_

15

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 32](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68)enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) {

[ 34](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a3010bbc6bde6ae12b39393ab34ed6c99) [LINK\_HALF\_10BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a3010bbc6bde6ae12b39393ab34ed6c99) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 36](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a96d36b5ff474b1919288602cc1927842) [LINK\_FULL\_10BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a96d36b5ff474b1919288602cc1927842) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 38](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a165dfc46d79c06755d315c2d4033b629) [LINK\_HALF\_100BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a165dfc46d79c06755d315c2d4033b629) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 40](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa2b3167b8fb31ccbe3cd314aa82cf213) [LINK\_FULL\_100BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa2b3167b8fb31ccbe3cd314aa82cf213) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 42](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ad2b4a4c3ff8358685316c5f056a73d04) [LINK\_HALF\_1000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ad2b4a4c3ff8358685316c5f056a73d04) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 44](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a72eec6d30279ddb51d7e9d6d7dabb611) [LINK\_FULL\_1000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a72eec6d30279ddb51d7e9d6d7dabb611) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 46](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a2f02a79486c5ee930f74e67e60bde377) [LINK\_FULL\_2500BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a2f02a79486c5ee930f74e67e60bde377) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 48](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a584f66dc8dde26f1377cc4596038e2c9) [LINK\_FULL\_5000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a584f66dc8dde26f1377cc4596038e2c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

49};

50

[ 58](group__ethernet__phy.md#ga7dcf0d74db291bf0922c8ceb34307558)#define PHY\_LINK\_IS\_FULL\_DUPLEX(x) (x & (BIT(1) | BIT(3) | BIT(5) | BIT(6) | BIT(7)))

59

[ 67](group__ethernet__phy.md#ga49f0673ace36bb3bac3e0c820a1f4de0)#define PHY\_LINK\_IS\_SPEED\_1000M(x) (x & (BIT(4) | BIT(5)))

68

[ 76](group__ethernet__phy.md#ga35acfd5ebec25784cc1c5b6be7be6a05)#define PHY\_LINK\_IS\_SPEED\_100M(x) (x & (BIT(2) | BIT(3)))

77

[ 79](structphy__link__state.md)struct [phy\_link\_state](structphy__link__state.md) {

[ 81](structphy__link__state.md#ab47802265dcf47b0aa815f4579467b6f) enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) [speed](structphy__link__state.md#ab47802265dcf47b0aa815f4579467b6f);

[ 83](structphy__link__state.md#aaced7164c07c5f964c952c2b04d68395) bool [is\_up](structphy__link__state.md#aaced7164c07c5f964c952c2b04d68395);

84};

85

[ 87](structphy__plca__cfg.md)struct [phy\_plca\_cfg](structphy__plca__cfg.md) {

[ 89](structphy__plca__cfg.md#a2c5eafc46d4869f11336094657978879) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structphy__plca__cfg.md#a2c5eafc46d4869f11336094657978879);

[ 91](structphy__plca__cfg.md#a3f8580797874684e64fed0bd9bf25a94) bool [enable](structphy__plca__cfg.md#a3f8580797874684e64fed0bd9bf25a94);

[ 93](structphy__plca__cfg.md#a7b98e4e26e7571aa7e4d1a99d81ea84a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_id](structphy__plca__cfg.md#a7b98e4e26e7571aa7e4d1a99d81ea84a);

[ 95](structphy__plca__cfg.md#a22346f28e7959b87038e938b169e670a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [node\_count](structphy__plca__cfg.md#a22346f28e7959b87038e938b169e670a);

[ 97](structphy__plca__cfg.md#a841b0ab053ea1903e8d0756f2ec6be87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_count](structphy__plca__cfg.md#a841b0ab053ea1903e8d0756f2ec6be87);

[ 99](structphy__plca__cfg.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_timer](structphy__plca__cfg.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca);

[ 101](structphy__plca__cfg.md#a0be4e9b562c9baabff0fb8c91868e549) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [to\_timer](structphy__plca__cfg.md#a0be4e9b562c9baabff0fb8c91868e549);

102};

103

[ 115](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f)int [genphy\_get\_plca\_cfg](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

116

[ 128](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca)int [genphy\_set\_plca\_cfg](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

129

[ 141](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722)int [genphy\_get\_plca\_sts](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722)(const struct [device](structdevice.md) \*dev, bool \*plca\_status);

142

[ 152](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)typedef void (\*[phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4))(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

153 void \*user\_data);

154

161\_\_subsystem struct ethphy\_driver\_api {

163 int (\*get\_link)(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

164

166 int (\*cfg\_link)(const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) adv\_speeds);

167

169 int (\*link\_cb\_set)(const struct [device](structdevice.md) \*dev, [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) cb, void \*user\_data);

170

172 int (\*read)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

173

175 int (\*write)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

176

178 int (\*read\_c45)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

179

181 int (\*write\_c45)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

182

183 /\* Set PLCA settings \*/

184 int (\*set\_plca\_cfg)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

185

186 /\* Get PLCA settings \*/

187 int (\*get\_plca\_cfg)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg);

188

189 /\* Get PLCA status \*/

190 int (\*get\_plca\_sts)(const struct [device](structdevice.md) \*dev, bool \*plca\_sts);

191};

195

[ 208](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80)static inline int [phy\_configure\_link](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80)(const struct [device](structdevice.md) \*dev, enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) speeds)

209{

210 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

211

212 return api->cfg\_link(dev, speeds);

213}

214

[ 228](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)static inline int [phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)(const struct [device](structdevice.md) \*dev, struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

229{

230 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

231

232 return api->get\_link(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

233}

234

[ 249](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)static inline int [phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)(const struct [device](structdevice.md) \*dev, [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) callback,

250 void \*user\_data)

251{

252 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

253

254 return api->link\_cb\_set(dev, callback, user\_data);

255}

256

[ 269](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)static inline int [phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value)

270{

271 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272

273 return api->read(dev, reg\_addr, value);

274}

275

[ 288](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)static inline int [phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

289{

290 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

291

292 return api->write(dev, reg\_addr, value);

293}

294

[ 308](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796)static inline int [phy\_read\_c45](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

309 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data)

310{

311 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

312

313 return api->read\_c45(dev, devad, regad, data);

314}

315

[ 329](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3)static inline int [phy\_write\_c45](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

330 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

331{

332 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

333

334 return api->write\_c45(dev, devad, regad, data);

335}

336

[ 348](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc)static inline int [phy\_set\_plca\_cfg](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg)

349{

350 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

351

352 return api->set\_plca\_cfg(dev, plca\_cfg);

353}

354

[ 366](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f)static inline int [phy\_get\_plca\_cfg](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f)(const struct [device](structdevice.md) \*dev, struct [phy\_plca\_cfg](structphy__plca__cfg.md) \*plca\_cfg)

367{

368 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

369

370 return api->get\_plca\_cfg(dev, plca\_cfg);

371}

372

[ 384](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312)static inline int [phy\_get\_plca\_sts](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312)(const struct [device](structdevice.md) \*dev, bool \*plca\_status)

385{

386 const struct ethphy\_driver\_api \*api = (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

387

388 return api->get\_plca\_sts(dev, plca\_status);

389}

390

391#ifdef \_\_cplusplus

392}

393#endif

394

398

399#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_ \*/

[device.h](device_8h.md)

[phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)

static int phy\_link\_callback\_set(const struct device \*dev, phy\_callback\_t callback, void \*user\_data)

Set link state change callback.

**Definition** phy.h:249

[genphy\_get\_plca\_cfg](group__ethernet__phy.md#ga2c723ef30447db60252a86cd9d72e44f)

int genphy\_get\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Write PHY PLCA configuration.

[phy\_set\_plca\_cfg](group__ethernet__phy.md#ga312638eb2d6c515988f783320742fdbc)

static int phy\_set\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Write PHY PLCA configuration.

**Definition** phy.h:348

[phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)

void(\* phy\_callback\_t)(const struct device \*dev, struct phy\_link\_state \*state, void \*user\_data)

Define the callback function signature for phy\_link\_callback\_set() function.

**Definition** phy.h:152

[phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)

static int phy\_read(const struct device \*dev, uint16\_t reg\_addr, uint32\_t \*value)

Read PHY registers.

**Definition** phy.h:269

[phy\_write\_c45](group__ethernet__phy.md#ga492c16dd8b5f2708d9e702ce8906ffd3)

static int phy\_write\_c45(const struct device \*dev, uint8\_t devad, uint16\_t regad, uint16\_t data)

Write PHY C45 register.

**Definition** phy.h:329

[phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)

static int phy\_get\_link\_state(const struct device \*dev, struct phy\_link\_state \*state)

Get PHY link state.

**Definition** phy.h:228

[phy\_read\_c45](group__ethernet__phy.md#ga4fa30627b96c9a1d02b43c8e799f2796)

static int phy\_read\_c45(const struct device \*dev, uint8\_t devad, uint16\_t regad, uint16\_t \*data)

Read PHY C45 register.

**Definition** phy.h:308

[phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)

static int phy\_write(const struct device \*dev, uint16\_t reg\_addr, uint32\_t value)

Write PHY register.

**Definition** phy.h:288

[phy\_get\_plca\_sts](group__ethernet__phy.md#ga692d77e273fb795091dbdd103ac43312)

static int phy\_get\_plca\_sts(const struct device \*dev, bool \*plca\_status)

Read PHY PLCA status.

**Definition** phy.h:384

[genphy\_set\_plca\_cfg](group__ethernet__phy.md#ga6b00c2872e5c7da17f49ee50089edcca)

int genphy\_set\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Read PHY PLCA configuration.

[phy\_get\_plca\_cfg](group__ethernet__phy.md#ga79f1b9b5a732eddbc2c2ced219e8582f)

static int phy\_get\_plca\_cfg(const struct device \*dev, struct phy\_plca\_cfg \*plca\_cfg)

Read PHY PLCA configuration.

**Definition** phy.h:366

[phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68)

phy\_link\_speed

Ethernet link speeds.

**Definition** phy.h:32

[phy\_configure\_link](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80)

static int phy\_configure\_link(const struct device \*dev, enum phy\_link\_speed speeds)

Configure PHY link.

**Definition** phy.h:208

[genphy\_get\_plca\_sts](group__ethernet__phy.md#gaf7d932210a5933479fb3010f28f6d722)

int genphy\_get\_plca\_sts(const struct device \*dev, bool \*plca\_status)

Read PHY PLCA status.

[LINK\_HALF\_100BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a165dfc46d79c06755d315c2d4033b629)

@ LINK\_HALF\_100BASE\_T

100Base-T Half-Duplex

**Definition** phy.h:38

[LINK\_FULL\_2500BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a2f02a79486c5ee930f74e67e60bde377)

@ LINK\_FULL\_2500BASE\_T

2.5GBase-T Full-Duplex

**Definition** phy.h:46

[LINK\_HALF\_10BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a3010bbc6bde6ae12b39393ab34ed6c99)

@ LINK\_HALF\_10BASE\_T

10Base-T Half-Duplex

**Definition** phy.h:34

[LINK\_FULL\_5000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a584f66dc8dde26f1377cc4596038e2c9)

@ LINK\_FULL\_5000BASE\_T

5GBase-T Full-Duplex

**Definition** phy.h:48

[LINK\_FULL\_1000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a72eec6d30279ddb51d7e9d6d7dabb611)

@ LINK\_FULL\_1000BASE\_T

1000Base-T Full-Duplex

**Definition** phy.h:44

[LINK\_FULL\_10BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a96d36b5ff474b1919288602cc1927842)

@ LINK\_FULL\_10BASE\_T

10Base-T Full-Duplex

**Definition** phy.h:36

[LINK\_FULL\_100BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa2b3167b8fb31ccbe3cd314aa82cf213)

@ LINK\_FULL\_100BASE\_T

100Base-T Full-Duplex

**Definition** phy.h:40

[LINK\_HALF\_1000BASE\_T](group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ad2b4a4c3ff8358685316c5f056a73d04)

@ LINK\_HALF\_1000BASE\_T

1000Base-T Half-Duplex

**Definition** phy.h:42

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[phy\_link\_state](structphy__link__state.md)

Link state.

**Definition** phy.h:79

[phy\_link\_state::is\_up](structphy__link__state.md#aaced7164c07c5f964c952c2b04d68395)

bool is\_up

When true the link is active and connected.

**Definition** phy.h:83

[phy\_link\_state::speed](structphy__link__state.md#ab47802265dcf47b0aa815f4579467b6f)

enum phy\_link\_speed speed

Link speed.

**Definition** phy.h:81

[phy\_plca\_cfg](structphy__plca__cfg.md)

PLCA (Physical Layer Collision Avoidance) Reconciliation Sublayer configurations.

**Definition** phy.h:87

[phy\_plca\_cfg::to\_timer](structphy__plca__cfg.md#a0be4e9b562c9baabff0fb8c91868e549)

uint8\_t to\_timer

PLCA to\_timer in bit-times, which determines the PLCA transmit opportunity.

**Definition** phy.h:101

[phy\_plca\_cfg::node\_count](structphy__plca__cfg.md#a22346f28e7959b87038e938b169e670a)

uint8\_t node\_count

PLCA node count.

**Definition** phy.h:95

[phy\_plca\_cfg::version](structphy__plca__cfg.md#a2c5eafc46d4869f11336094657978879)

uint8\_t version

PLCA register map version.

**Definition** phy.h:89

[phy\_plca\_cfg::enable](structphy__plca__cfg.md#a3f8580797874684e64fed0bd9bf25a94)

bool enable

PLCA configured mode (enable/disable).

**Definition** phy.h:91

[phy\_plca\_cfg::node\_id](structphy__plca__cfg.md#a7b98e4e26e7571aa7e4d1a99d81ea84a)

uint8\_t node\_id

PLCA local node identifier.

**Definition** phy.h:93

[phy\_plca\_cfg::burst\_count](structphy__plca__cfg.md#a841b0ab053ea1903e8d0756f2ec6be87)

uint8\_t burst\_count

Additional frames a node is allowed to send in single transmit opportunity (TO).

**Definition** phy.h:97

[phy\_plca\_cfg::burst\_timer](structphy__plca__cfg.md#aed0ad2e0da7dd1f7fb9e90dcd9d206ca)

uint8\_t burst\_timer

Wait time for the MAC to send a new frame before interrupting the burst.

**Definition** phy.h:99

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [phy.h](phy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
