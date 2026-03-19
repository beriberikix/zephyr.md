---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/phy_8h_source.html
original_path: doxygen/html/phy_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 95](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)typedef void (\*[phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4))(const struct [device](structdevice.md) \*dev,

96 struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

97 void \*user\_data);

98

105\_\_subsystem struct ethphy\_driver\_api {

107 int (\*get\_link)(const struct [device](structdevice.md) \*dev,

108 struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

109

111 int (\*cfg\_link)(const struct [device](structdevice.md) \*dev,

112 enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) adv\_speeds);

113

115 int (\*link\_cb\_set)(const struct [device](structdevice.md) \*dev, [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) cb,

116 void \*user\_data);

117

119 int (\*read)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

120 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

121

123 int (\*write)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

124 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

125};

129

[ 142](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80)static inline int [phy\_configure\_link](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80)(const struct [device](structdevice.md) \*dev,

143 enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) speeds)

144{

145 const struct ethphy\_driver\_api \*api =

146 (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

147

148 return api->cfg\_link(dev, speeds);

149}

150

[ 164](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)static inline int [phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)(const struct [device](structdevice.md) \*dev,

165 struct [phy\_link\_state](structphy__link__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

166{

167 const struct ethphy\_driver\_api \*api =

168 (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

169

170 return api->get\_link(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

171}

172

[ 187](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)static inline int [phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)(const struct [device](structdevice.md) \*dev,

188 [phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4) callback,

189 void \*user\_data)

190{

191 const struct ethphy\_driver\_api \*api =

192 (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

193

194 return api->link\_cb\_set(dev, callback, user\_data);

195}

196

[ 209](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)static inline int [phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

210 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value)

211{

212 const struct ethphy\_driver\_api \*api =

213 (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

214

215 return api->read(dev, reg\_addr, value);

216}

217

[ 230](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)static inline int [phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr,

231 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

232{

233 const struct ethphy\_driver\_api \*api =

234 (const struct ethphy\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

235

236 return api->write(dev, reg\_addr, value);

237}

238

239

240#ifdef \_\_cplusplus

241}

242#endif

243

247

248#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PHY\_H\_ \*/

[device.h](device_8h.md)

[phy\_link\_callback\_set](group__ethernet__phy.md#ga0ede85fdd6efd8c3520d7baf18d04a68)

static int phy\_link\_callback\_set(const struct device \*dev, phy\_callback\_t callback, void \*user\_data)

Set link state change callback.

**Definition** phy.h:187

[phy\_callback\_t](group__ethernet__phy.md#ga3ee3db4ac48395f07d0de536b313dfa4)

void(\* phy\_callback\_t)(const struct device \*dev, struct phy\_link\_state \*state, void \*user\_data)

Define the callback function signature for phy\_link\_callback\_set() function.

**Definition** phy.h:95

[phy\_read](group__ethernet__phy.md#ga3fcca53d29981e23426b43d5340d8651)

static int phy\_read(const struct device \*dev, uint16\_t reg\_addr, uint32\_t \*value)

Read PHY registers.

**Definition** phy.h:209

[phy\_get\_link\_state](group__ethernet__phy.md#ga4d073c152ad4b6f5745db4f6d8477345)

static int phy\_get\_link\_state(const struct device \*dev, struct phy\_link\_state \*state)

Get PHY link state.

**Definition** phy.h:164

[phy\_write](group__ethernet__phy.md#ga520c049d830051ffa48708bb0dea429f)

static int phy\_write(const struct device \*dev, uint16\_t reg\_addr, uint32\_t value)

Write PHY register.

**Definition** phy.h:230

[phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68)

phy\_link\_speed

Ethernet link speeds.

**Definition** phy.h:32

[phy\_configure\_link](group__ethernet__phy.md#gacb1e5d12f51106d481159d4b3e593e80)

static int phy\_configure\_link(const struct device \*dev, enum phy\_link\_speed speeds)

Configure PHY link.

**Definition** phy.h:142

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [phy.h](phy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
