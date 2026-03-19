---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bas_8h_source.html
original_path: doxygen/html/bas_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bas.h

[Go to the documentation of this file.](bas_8h.md)

1/\*

2 \* Copyright (c) 2024 Demant A/S

3 \* Copyright (c) 2018 Nordic Semiconductor ASA

4 \* Copyright (c) 2016 Intel Corporation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_BAS\_H\_

10#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_BAS\_H\_

11

21

22#include <[stdint.h](stdint_8h.md)>

23#include <[zephyr/sys/util.h](sys_2util_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 35](group__bt__bas.md#ga56d26a8cde072959e8d8b75ee4fb2819)enum [bt\_bas\_bcs\_flags](group__bt__bas.md#ga56d26a8cde072959e8d8b75ee4fb2819) {

[ 37](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5) [BT\_BAS\_BCS\_BATTERY\_CRITICAL\_STATE](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

38

[ 40](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a) [BT\_BAS\_BCS\_IMMEDIATE\_SERVICE\_REQUIRED](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

41};

42

[ 49](group__bt__bas.md#ga7c425f7fd9e908e327810f89d7645745)enum [bt\_bas\_bls\_flags](group__bt__bas.md#ga7c425f7fd9e908e327810f89d7645745) {

[ 51](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46) [BT\_BAS\_BLS\_FLAG\_IDENTIFIER\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

52

[ 54](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba) [BT\_BAS\_BLS\_FLAG\_BATTERY\_LEVEL\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

55

[ 57](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d) [BT\_BAS\_BLS\_FLAG\_ADDITIONAL\_STATUS\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

58};

59

[ 64](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f)enum [bt\_bas\_bls\_battery\_present](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f) {

[ 66](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522) [BT\_BAS\_BLS\_BATTERY\_NOT\_PRESENT](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522) = 0,

67

[ 69](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49) [BT\_BAS\_BLS\_BATTERY\_PRESENT](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49) = 1

70};

71

[ 76](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c)enum [bt\_bas\_bls\_wired\_power\_source](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c) {

[ 78](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf) [BT\_BAS\_BLS\_WIRED\_POWER\_NOT\_CONNECTED](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf) = 0,

79

[ 81](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc) [BT\_BAS\_BLS\_WIRED\_POWER\_CONNECTED](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc) = 1,

82

[ 84](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799) [BT\_BAS\_BLS\_WIRED\_POWER\_UNKNOWN](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799) = 2

85};

86

[ 91](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d)enum [bt\_bas\_bls\_wireless\_power\_source](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d) {

[ 93](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383) [BT\_BAS\_BLS\_WIRELESS\_POWER\_NOT\_CONNECTED](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383) = 0,

94

[ 96](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363) [BT\_BAS\_BLS\_WIRELESS\_POWER\_CONNECTED](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363) = 1,

97

[ 99](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8) [BT\_BAS\_BLS\_WIRELESS\_POWER\_UNKNOWN](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8) = 2

100};

101

[ 106](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313)enum [bt\_bas\_bls\_battery\_charge\_state](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313) {

[ 108](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c) [BT\_BAS\_BLS\_CHARGE\_STATE\_UNKNOWN](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c) = 0,

109

[ 111](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9) [BT\_BAS\_BLS\_CHARGE\_STATE\_CHARGING](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9) = 1,

112

[ 114](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02) [BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_ACTIVE](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02) = 2,

115

[ 117](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a) [BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_INACTIVE](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a) = 3

118};

119

[ 124](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c)enum [bt\_bas\_bls\_battery\_charge\_level](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c) {

[ 126](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58) [BT\_BAS\_BLS\_CHARGE\_LEVEL\_UNKNOWN](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58) = 0,

127

[ 129](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387) [BT\_BAS\_BLS\_CHARGE\_LEVEL\_GOOD](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387) = 1,

130

[ 132](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e) [BT\_BAS\_BLS\_CHARGE\_LEVEL\_LOW](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e) = 2,

133

[ 135](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d) [BT\_BAS\_BLS\_CHARGE\_LEVEL\_CRITICAL](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d) = 3

136};

137

[ 142](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa)enum [bt\_bas\_bls\_battery\_charge\_type](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa) {

[ 144](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64) [BT\_BAS\_BLS\_CHARGE\_TYPE\_UNKNOWN](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64) = 0,

145

[ 147](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af) [BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_CURRENT](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af) = 1,

148

[ 150](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730) [BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_VOLTAGE](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730) = 2,

151

[ 153](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda) [BT\_BAS\_BLS\_CHARGE\_TYPE\_TRICKLE](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda) = 3,

154

[ 156](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0) [BT\_BAS\_BLS\_CHARGE\_TYPE\_FLOAT](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0) = 4

157};

158

[ 163](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b)enum [bt\_bas\_bls\_charging\_fault\_reason](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b) {

[ 165](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a) [BT\_BAS\_BLS\_FAULT\_REASON\_NONE](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a) = 0,

166

[ 168](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f) [BT\_BAS\_BLS\_FAULT\_REASON\_BATTERY](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

169

[ 171](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b) [BT\_BAS\_BLS\_FAULT\_REASON\_EXTERNAL\_POWER](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

172

[ 174](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7) [BT\_BAS\_BLS\_FAULT\_REASON\_OTHER](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)

175};

176

[ 181](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d)enum [bt\_bas\_bls\_service\_required](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d) {

[ 183](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db) [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_FALSE](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db) = 0,

184

[ 186](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00) [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_TRUE](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00) = 1,

187

[ 189](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870) [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_UNKNOWN](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870) = 2

190};

191

[ 196](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee)enum [bt\_bas\_bls\_battery\_fault](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee) {

[ 198](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee) [BT\_BAS\_BLS\_BATTERY\_FAULT\_NO](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee) = 0,

199

[ 201](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f) [BT\_BAS\_BLS\_BATTERY\_FAULT\_YES](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f) = 1

202};

203

[ 210](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_bas\_get\_battery\_level](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980)(void);

211

[ 221](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba)int [bt\_bas\_set\_battery\_level](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

222

[ 228](group__bt__bas.md#ga5e0325af9dcd362dd3c1691832be5677)void [bt\_bas\_bls\_set\_battery\_present](group__bt__bas.md#ga5e0325af9dcd362dd3c1691832be5677)(enum [bt\_bas\_bls\_battery\_present](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f) present);

229

[ 235](group__bt__bas.md#ga7bf36a53494e2ecfbb5ccd218f29f51f)void [bt\_bas\_bls\_set\_wired\_external\_power\_source](group__bt__bas.md#ga7bf36a53494e2ecfbb5ccd218f29f51f)(enum [bt\_bas\_bls\_wired\_power\_source](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c) source);

236

[ 242](group__bt__bas.md#gae1cbafd30e1d78437c78d44df25aa005)void [bt\_bas\_bls\_set\_wireless\_external\_power\_source](group__bt__bas.md#gae1cbafd30e1d78437c78d44df25aa005)(enum [bt\_bas\_bls\_wireless\_power\_source](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d) source);

243

[ 249](group__bt__bas.md#ga60b153c4d291ed4b16ce1f9d2dc1b45d)void [bt\_bas\_bls\_set\_battery\_charge\_state](group__bt__bas.md#ga60b153c4d291ed4b16ce1f9d2dc1b45d)(enum [bt\_bas\_bls\_battery\_charge\_state](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

250

[ 256](group__bt__bas.md#gac8e32530f966c7699d3c28e6685bcee5)void [bt\_bas\_bls\_set\_battery\_charge\_level](group__bt__bas.md#gac8e32530f966c7699d3c28e6685bcee5)(enum [bt\_bas\_bls\_battery\_charge\_level](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c) level);

257

[ 263](group__bt__bas.md#ga3cea34f717f2df01b6f49bed80f27f44)void [bt\_bas\_bls\_set\_battery\_charge\_type](group__bt__bas.md#ga3cea34f717f2df01b6f49bed80f27f44)(enum [bt\_bas\_bls\_battery\_charge\_type](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa) type);

264

[ 270](group__bt__bas.md#ga7996edb35bcca878062360b24036b6f8)void [bt\_bas\_bls\_set\_charging\_fault\_reason](group__bt__bas.md#ga7996edb35bcca878062360b24036b6f8)(enum [bt\_bas\_bls\_charging\_fault\_reason](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b) reason);

271

[ 279](group__bt__bas.md#gafd74ef933734960a64f1ee1e80e9e335)void [bt\_bas\_bls\_set\_identifier](group__bt__bas.md#gafd74ef933734960a64f1ee1e80e9e335)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) identifier);

280

[ 288](group__bt__bas.md#gaa94f308b6e135a3957191499778275ec)void [bt\_bas\_bls\_set\_service\_required](group__bt__bas.md#gaa94f308b6e135a3957191499778275ec)(enum [bt\_bas\_bls\_service\_required](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d) value);

289

[ 297](group__bt__bas.md#ga9c50ed6a493adee208a59b17c48702f8)void [bt\_bas\_bls\_set\_battery\_fault](group__bt__bas.md#ga9c50ed6a493adee208a59b17c48702f8)(enum [bt\_bas\_bls\_battery\_fault](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee) value);

298

299#ifdef \_\_cplusplus

300}

301#endif

302

306

307#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_BAS\_H\_ \*/

[bt\_bas\_bls\_battery\_present](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f)

bt\_bas\_bls\_battery\_present

Battery Present Status.

**Definition** bas.h:64

[bt\_bas\_bls\_battery\_charge\_state](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313)

bt\_bas\_bls\_battery\_charge\_state

Battery Charge State.

**Definition** bas.h:106

[bt\_bas\_bls\_set\_battery\_charge\_type](group__bt__bas.md#ga3cea34f717f2df01b6f49bed80f27f44)

void bt\_bas\_bls\_set\_battery\_charge\_type(enum bt\_bas\_bls\_battery\_charge\_type type)

Set the battery charge type.

[bt\_bas\_bls\_wired\_power\_source](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c)

bt\_bas\_bls\_wired\_power\_source

Wired External Power Source Status.

**Definition** bas.h:76

[bt\_bas\_bcs\_flags](group__bt__bas.md#ga56d26a8cde072959e8d8b75ee4fb2819)

bt\_bas\_bcs\_flags

Battery Critical Status Characteristic flags.

**Definition** bas.h:35

[bt\_bas\_bls\_set\_battery\_present](group__bt__bas.md#ga5e0325af9dcd362dd3c1691832be5677)

void bt\_bas\_bls\_set\_battery\_present(enum bt\_bas\_bls\_battery\_present present)

Set the battery present status.

[bt\_bas\_bls\_set\_battery\_charge\_state](group__bt__bas.md#ga60b153c4d291ed4b16ce1f9d2dc1b45d)

void bt\_bas\_bls\_set\_battery\_charge\_state(enum bt\_bas\_bls\_battery\_charge\_state state)

Set the battery charge state.

[bt\_bas\_bls\_battery\_fault](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee)

bt\_bas\_bls\_battery\_fault

Battery Fault Status.

**Definition** bas.h:196

[bt\_bas\_bls\_set\_charging\_fault\_reason](group__bt__bas.md#ga7996edb35bcca878062360b24036b6f8)

void bt\_bas\_bls\_set\_charging\_fault\_reason(enum bt\_bas\_bls\_charging\_fault\_reason reason)

Set the charging fault reason.

[bt\_bas\_bls\_set\_wired\_external\_power\_source](group__bt__bas.md#ga7bf36a53494e2ecfbb5ccd218f29f51f)

void bt\_bas\_bls\_set\_wired\_external\_power\_source(enum bt\_bas\_bls\_wired\_power\_source source)

Set the wired external power source status.

[bt\_bas\_bls\_flags](group__bt__bas.md#ga7c425f7fd9e908e327810f89d7645745)

bt\_bas\_bls\_flags

Battery Level Status Characteristic flags.

**Definition** bas.h:49

[bt\_bas\_bls\_set\_battery\_fault](group__bt__bas.md#ga9c50ed6a493adee208a59b17c48702f8)

void bt\_bas\_bls\_set\_battery\_fault(enum bt\_bas\_bls\_battery\_fault value)

Set the battery fault status.

[bt\_bas\_bls\_battery\_charge\_type](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa)

bt\_bas\_bls\_battery\_charge\_type

Battery Charge Type.

**Definition** bas.h:142

[bt\_bas\_bls\_set\_service\_required](group__bt__bas.md#gaa94f308b6e135a3957191499778275ec)

void bt\_bas\_bls\_set\_service\_required(enum bt\_bas\_bls\_service\_required value)

Set the service required status.

[bt\_bas\_set\_battery\_level](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba)

int bt\_bas\_set\_battery\_level(uint8\_t level)

Update battery level value.

[bt\_bas\_bls\_set\_battery\_charge\_level](group__bt__bas.md#gac8e32530f966c7699d3c28e6685bcee5)

void bt\_bas\_bls\_set\_battery\_charge\_level(enum bt\_bas\_bls\_battery\_charge\_level level)

Set the battery charge level.

[bt\_bas\_bls\_battery\_charge\_level](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c)

bt\_bas\_bls\_battery\_charge\_level

Battery Charge Level.

**Definition** bas.h:124

[bt\_bas\_bls\_service\_required](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d)

bt\_bas\_bls\_service\_required

Service Required Status.

**Definition** bas.h:181

[bt\_bas\_bls\_charging\_fault\_reason](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b)

bt\_bas\_bls\_charging\_fault\_reason

Charging Fault Reason.

**Definition** bas.h:163

[bt\_bas\_get\_battery\_level](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980)

uint8\_t bt\_bas\_get\_battery\_level(void)

Read battery level value.

[bt\_bas\_bls\_set\_wireless\_external\_power\_source](group__bt__bas.md#gae1cbafd30e1d78437c78d44df25aa005)

void bt\_bas\_bls\_set\_wireless\_external\_power\_source(enum bt\_bas\_bls\_wireless\_power\_source source)

Set the wireless external power source status.

[bt\_bas\_bls\_wireless\_power\_source](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d)

bt\_bas\_bls\_wireless\_power\_source

Wireless External Power Source Status.

**Definition** bas.h:91

[bt\_bas\_bls\_set\_identifier](group__bt__bas.md#gafd74ef933734960a64f1ee1e80e9e335)

void bt\_bas\_bls\_set\_identifier(uint16\_t identifier)

Set the identifier of the battery.

[BT\_BAS\_BLS\_BATTERY\_PRESENT](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49)

@ BT\_BAS\_BLS\_BATTERY\_PRESENT

Battery is present.

**Definition** bas.h:69

[BT\_BAS\_BLS\_BATTERY\_NOT\_PRESENT](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522)

@ BT\_BAS\_BLS\_BATTERY\_NOT\_PRESENT

Battery is not present.

**Definition** bas.h:66

[BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_INACTIVE](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a)

@ BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_INACTIVE

Battery is discharging but inactive.

**Definition** bas.h:117

[BT\_BAS\_BLS\_CHARGE\_STATE\_CHARGING](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9)

@ BT\_BAS\_BLS\_CHARGE\_STATE\_CHARGING

Battery is currently charging.

**Definition** bas.h:111

[BT\_BAS\_BLS\_CHARGE\_STATE\_UNKNOWN](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c)

@ BT\_BAS\_BLS\_CHARGE\_STATE\_UNKNOWN

Battery charge state is unknown.

**Definition** bas.h:108

[BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_ACTIVE](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02)

@ BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_ACTIVE

Battery is discharging actively.

**Definition** bas.h:114

[BT\_BAS\_BLS\_WIRED\_POWER\_UNKNOWN](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799)

@ BT\_BAS\_BLS\_WIRED\_POWER\_UNKNOWN

Wired external power source status is unknown.

**Definition** bas.h:84

[BT\_BAS\_BLS\_WIRED\_POWER\_NOT\_CONNECTED](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf)

@ BT\_BAS\_BLS\_WIRED\_POWER\_NOT\_CONNECTED

Wired external power source is not connected.

**Definition** bas.h:78

[BT\_BAS\_BLS\_WIRED\_POWER\_CONNECTED](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc)

@ BT\_BAS\_BLS\_WIRED\_POWER\_CONNECTED

Wired external power source is connected.

**Definition** bas.h:81

[BT\_BAS\_BCS\_BATTERY\_CRITICAL\_STATE](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5)

@ BT\_BAS\_BCS\_BATTERY\_CRITICAL\_STATE

Battery Critical Status Bit 0: Critical Power State.

**Definition** bas.h:37

[BT\_BAS\_BCS\_IMMEDIATE\_SERVICE\_REQUIRED](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a)

@ BT\_BAS\_BCS\_IMMEDIATE\_SERVICE\_REQUIRED

Battery Critical Status Bit 1: Immediate Service Required.

**Definition** bas.h:40

[BT\_BAS\_BLS\_BATTERY\_FAULT\_YES](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f)

@ BT\_BAS\_BLS\_BATTERY\_FAULT\_YES

Battery fault present.

**Definition** bas.h:201

[BT\_BAS\_BLS\_BATTERY\_FAULT\_NO](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee)

@ BT\_BAS\_BLS\_BATTERY\_FAULT\_NO

No battery fault.

**Definition** bas.h:198

[BT\_BAS\_BLS\_FLAG\_IDENTIFIER\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46)

@ BT\_BAS\_BLS\_FLAG\_IDENTIFIER\_PRESENT

Bit indicating that the Battery Level Status identifier is present.

**Definition** bas.h:51

[BT\_BAS\_BLS\_FLAG\_BATTERY\_LEVEL\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba)

@ BT\_BAS\_BLS\_FLAG\_BATTERY\_LEVEL\_PRESENT

Bit indicating that the Battery Level is present.

**Definition** bas.h:54

[BT\_BAS\_BLS\_FLAG\_ADDITIONAL\_STATUS\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d)

@ BT\_BAS\_BLS\_FLAG\_ADDITIONAL\_STATUS\_PRESENT

Bit indicating that additional status information is present.

**Definition** bas.h:57

[BT\_BAS\_BLS\_CHARGE\_TYPE\_UNKNOWN](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64)

@ BT\_BAS\_BLS\_CHARGE\_TYPE\_UNKNOWN

Battery charge type is unknown or not charging.

**Definition** bas.h:144

[BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_CURRENT](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af)

@ BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_CURRENT

Battery is charged using constant current.

**Definition** bas.h:147

[BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_VOLTAGE](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730)

@ BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_VOLTAGE

Battery is charged using constant voltage.

**Definition** bas.h:150

[BT\_BAS\_BLS\_CHARGE\_TYPE\_FLOAT](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0)

@ BT\_BAS\_BLS\_CHARGE\_TYPE\_FLOAT

Battery is charged using float charge.

**Definition** bas.h:156

[BT\_BAS\_BLS\_CHARGE\_TYPE\_TRICKLE](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda)

@ BT\_BAS\_BLS\_CHARGE\_TYPE\_TRICKLE

Battery is charged using trickle charge.

**Definition** bas.h:153

[BT\_BAS\_BLS\_CHARGE\_LEVEL\_LOW](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e)

@ BT\_BAS\_BLS\_CHARGE\_LEVEL\_LOW

Battery charge level is low.

**Definition** bas.h:132

[BT\_BAS\_BLS\_CHARGE\_LEVEL\_CRITICAL](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d)

@ BT\_BAS\_BLS\_CHARGE\_LEVEL\_CRITICAL

Battery charge level is critical.

**Definition** bas.h:135

[BT\_BAS\_BLS\_CHARGE\_LEVEL\_UNKNOWN](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58)

@ BT\_BAS\_BLS\_CHARGE\_LEVEL\_UNKNOWN

Battery charge level is unknown.

**Definition** bas.h:126

[BT\_BAS\_BLS\_CHARGE\_LEVEL\_GOOD](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387)

@ BT\_BAS\_BLS\_CHARGE\_LEVEL\_GOOD

Battery charge level is good.

**Definition** bas.h:129

[BT\_BAS\_BLS\_SERVICE\_REQUIRED\_TRUE](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00)

@ BT\_BAS\_BLS\_SERVICE\_REQUIRED\_TRUE

Service is required.

**Definition** bas.h:186

[BT\_BAS\_BLS\_SERVICE\_REQUIRED\_FALSE](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db)

@ BT\_BAS\_BLS\_SERVICE\_REQUIRED\_FALSE

Service is not required.

**Definition** bas.h:183

[BT\_BAS\_BLS\_SERVICE\_REQUIRED\_UNKNOWN](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870)

@ BT\_BAS\_BLS\_SERVICE\_REQUIRED\_UNKNOWN

Service requirement is unknown.

**Definition** bas.h:189

[BT\_BAS\_BLS\_FAULT\_REASON\_EXTERNAL\_POWER](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b)

@ BT\_BAS\_BLS\_FAULT\_REASON\_EXTERNAL\_POWER

Charging fault due to external power source issue.

**Definition** bas.h:171

[BT\_BAS\_BLS\_FAULT\_REASON\_BATTERY](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f)

@ BT\_BAS\_BLS\_FAULT\_REASON\_BATTERY

Charging fault due to battery issue.

**Definition** bas.h:168

[BT\_BAS\_BLS\_FAULT\_REASON\_OTHER](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7)

@ BT\_BAS\_BLS\_FAULT\_REASON\_OTHER

Charging fault for other reasons.

**Definition** bas.h:174

[BT\_BAS\_BLS\_FAULT\_REASON\_NONE](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a)

@ BT\_BAS\_BLS\_FAULT\_REASON\_NONE

No charging fault.

**Definition** bas.h:165

[BT\_BAS\_BLS\_WIRELESS\_POWER\_CONNECTED](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363)

@ BT\_BAS\_BLS\_WIRELESS\_POWER\_CONNECTED

Wireless external power source is connected.

**Definition** bas.h:96

[BT\_BAS\_BLS\_WIRELESS\_POWER\_UNKNOWN](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8)

@ BT\_BAS\_BLS\_WIRELESS\_POWER\_UNKNOWN

Wireless external power source status is unknown.

**Definition** bas.h:99

[BT\_BAS\_BLS\_WIRELESS\_POWER\_NOT\_CONNECTED](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383)

@ BT\_BAS\_BLS\_WIRELESS\_POWER\_NOT\_CONNECTED

Wireless external power source is not connected.

**Definition** bas.h:93

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [bas.h](bas_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
