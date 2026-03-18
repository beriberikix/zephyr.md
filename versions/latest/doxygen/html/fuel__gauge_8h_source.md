---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fuel__gauge_8h_source.html
original_path: doxygen/html/fuel__gauge_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fuel\_gauge.h

[Go to the documentation of this file.](fuel__gauge_8h.md)

1/\*

2 \* Copyright 2022 Google LLC

3 \* Copyright 2023 Microsoft Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_BATTERY\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_BATTERY\_H\_

10

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif /\* \_\_cplusplus \*/

21

22#include <[errno.h](errno_8h.md)>

23#include <[stdbool.h](stdbool_8h.md)>

24#include <stddef.h>

25#include <[stdint.h](stdint_8h.md)>

26

27#include <[zephyr/device.h](device_8h.md)>

28

[ 29](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171)enum [fuel\_gauge\_prop\_type](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171) {

[ 37](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396) [FUEL\_GAUGE\_AVG\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396) = 0,

38

[ 40](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f) [FUEL\_GAUGE\_BATTERY\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f),

[ 42](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354) [FUEL\_GAUGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354),

[ 44](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f) [FUEL\_GAUGE\_CHARGE\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f),

[ 46](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984) [FUEL\_GAUGE\_CYCLE\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984),

[ 48](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d) [FUEL\_GAUGE\_CONNECT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d),

[ 50](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c) [FUEL\_GAUGE\_FLAGS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c),

[ 52](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9) [FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9),

[ 54](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b) [FUEL\_GAUGE\_PRESENT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b),

[ 56](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4) [FUEL\_GAUGE\_REMAINING\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4),

[ 58](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd) [FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd),

[ 60](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399) [FUEL\_GAUGE\_RUNTIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399),

[ 62](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd) [FUEL\_GAUGE\_SBS\_MFR\_ACCESS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd),

[ 64](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee) [FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee),

[ 66](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b) [FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b),

[ 68](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009) [FUEL\_GAUGE\_TEMPERATURE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009),

[ 70](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71) [FUEL\_GAUGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71),

[ 72](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae) [FUEL\_GAUGE\_SBS\_MODE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae),

[ 74](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e) [FUEL\_GAUGE\_CHARGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e),

[ 76](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920) [FUEL\_GAUGE\_CHARGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920),

[ 78](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40) [FUEL\_GAUGE\_STATUS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40),

[ 80](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67) [FUEL\_GAUGE\_DESIGN\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67),

[ 82](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf) [FUEL\_GAUGE\_DESIGN\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf),

[ 84](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58) [FUEL\_GAUGE\_SBS\_ATRATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58),

[ 86](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70) [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70),

[ 88](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0) [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0),

[ 90](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec) [FUEL\_GAUGE\_SBS\_ATRATE\_OK](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec),

[ 92](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2) [FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2),

[ 94](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a) [FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a),

[ 96](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8) [FUEL\_GAUGE\_MANUFACTURER\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8),

[ 98](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10) [FUEL\_GAUGE\_DEVICE\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10),

[ 100](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9) [FUEL\_GAUGE\_DEVICE\_CHEMISTRY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9),

101

[ 103](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815) [FUEL\_GAUGE\_COMMON\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815),

[ 108](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584) [FUEL\_GAUGE\_CUSTOM\_BEGIN](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584),

109

[ 111](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81) [FUEL\_GAUGE\_PROP\_MAX](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81) = [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602),

112};

113

[ 114](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806);

115

[ 117](unionfuel__gauge__prop__val.md)union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) {

118 /\* Fields have the format: \*/

119 /\* FUEL\_GAUGE\_PROPERTY\_FIELD \*/

120 /\* type property\_field; \*/

121

122 /\* Dynamic Battery Info \*/

[ 124](unionfuel__gauge__prop__val.md#ad96f07db337c038466dd17401c076d38) int [avg\_current](unionfuel__gauge__prop__val.md#ad96f07db337c038466dd17401c076d38);

[ 126](unionfuel__gauge__prop__val.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a) bool [cutoff](unionfuel__gauge__prop__val.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a);

[ 128](unionfuel__gauge__prop__val.md#a9bed3247063f069bb92b2902cc5ff468) int [current](unionfuel__gauge__prop__val.md#a9bed3247063f069bb92b2902cc5ff468);

[ 130](unionfuel__gauge__prop__val.md#ac27ae67a315a7204cea6e88962758587) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cycle\_count](unionfuel__gauge__prop__val.md#ac27ae67a315a7204cea6e88962758587);

[ 132](unionfuel__gauge__prop__val.md#adeb93ed2120e808aac815dcbdf69067f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](unionfuel__gauge__prop__val.md#adeb93ed2120e808aac815dcbdf69067f);

[ 134](unionfuel__gauge__prop__val.md#aa29f7163a1637b6aa8cd6a15dc99d55b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [full\_charge\_capacity](unionfuel__gauge__prop__val.md#aa29f7163a1637b6aa8cd6a15dc99d55b);

[ 136](unionfuel__gauge__prop__val.md#adecf57aa90e2b5d483cfd889ec512400) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [remaining\_capacity](unionfuel__gauge__prop__val.md#adecf57aa90e2b5d483cfd889ec512400);

[ 138](unionfuel__gauge__prop__val.md#ae716bdf1346dc7767d98526db6083008) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [runtime\_to\_empty](unionfuel__gauge__prop__val.md#ae716bdf1346dc7767d98526db6083008);

[ 140](unionfuel__gauge__prop__val.md#a2c77e8de7fa40fadfa13dfd4c94df804) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [runtime\_to\_full](unionfuel__gauge__prop__val.md#a2c77e8de7fa40fadfa13dfd4c94df804);

[ 142](unionfuel__gauge__prop__val.md#a957025a2a9fb7709e2bf478f15fd31a0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_mfr\_access\_word](unionfuel__gauge__prop__val.md#a957025a2a9fb7709e2bf478f15fd31a0);

[ 144](unionfuel__gauge__prop__val.md#a33297ff5bf70b510272eddf77ced411e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [absolute\_state\_of\_charge](unionfuel__gauge__prop__val.md#a33297ff5bf70b510272eddf77ced411e);

[ 146](unionfuel__gauge__prop__val.md#a45b20c5118f7ee408d507b94e6cae1dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [relative\_state\_of\_charge](unionfuel__gauge__prop__val.md#a45b20c5118f7ee408d507b94e6cae1dc);

[ 148](unionfuel__gauge__prop__val.md#a36528b111568bd1c90859e454610fd9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [temperature](unionfuel__gauge__prop__val.md#a36528b111568bd1c90859e454610fd9f);

[ 150](unionfuel__gauge__prop__val.md#abec5cadefa09e088620a9598dec9c473) int [voltage](unionfuel__gauge__prop__val.md#abec5cadefa09e088620a9598dec9c473);

[ 152](unionfuel__gauge__prop__val.md#a7fc0551e303de56e0eb6bdac1ecaccd0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_mode](unionfuel__gauge__prop__val.md#a7fc0551e303de56e0eb6bdac1ecaccd0);

[ 154](unionfuel__gauge__prop__val.md#a6f74626deef4debbd8dfe6c188984d1b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [chg\_current](unionfuel__gauge__prop__val.md#a6f74626deef4debbd8dfe6c188984d1b);

[ 156](unionfuel__gauge__prop__val.md#a8743f7e7a05919b5469e39527b697e62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [chg\_voltage](unionfuel__gauge__prop__val.md#a8743f7e7a05919b5469e39527b697e62);

[ 158](unionfuel__gauge__prop__val.md#a65607bb9ba43022c9c566646d4763aac) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fg\_status](unionfuel__gauge__prop__val.md#a65607bb9ba43022c9c566646d4763aac);

[ 160](unionfuel__gauge__prop__val.md#a20aa5736b0ac3c5adda10152660de275) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [design\_cap](unionfuel__gauge__prop__val.md#a20aa5736b0ac3c5adda10152660de275);

[ 162](unionfuel__gauge__prop__val.md#a11626713aef0445ad613a5976401d09e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [design\_volt](unionfuel__gauge__prop__val.md#a11626713aef0445ad613a5976401d09e);

[ 164](unionfuel__gauge__prop__val.md#aa5529fea5cfe765be9b66f5fad96ab2f) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [sbs\_at\_rate](unionfuel__gauge__prop__val.md#aa5529fea5cfe765be9b66f5fad96ab2f);

[ 166](unionfuel__gauge__prop__val.md#aeeeddb48f22b54f90c603d58e9ffa9a5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_at\_rate\_time\_to\_full](unionfuel__gauge__prop__val.md#aeeeddb48f22b54f90c603d58e9ffa9a5);

[ 168](unionfuel__gauge__prop__val.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_at\_rate\_time\_to\_empty](unionfuel__gauge__prop__val.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8);

[ 170](unionfuel__gauge__prop__val.md#a9b5015878c9a77d9c8330139f94843b7) bool [sbs\_at\_rate\_ok](unionfuel__gauge__prop__val.md#a9b5015878c9a77d9c8330139f94843b7);

[ 172](unionfuel__gauge__prop__val.md#a818ab7faf8f51d4d1a5c5f070d54b997) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_remaining\_capacity\_alarm](unionfuel__gauge__prop__val.md#a818ab7faf8f51d4d1a5c5f070d54b997);

[ 174](unionfuel__gauge__prop__val.md#aa0e46c727bb31acb5d41ce4bc6d5b106) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_remaining\_time\_alarm](unionfuel__gauge__prop__val.md#aa0e46c727bb31acb5d41ce4bc6d5b106);

175};

176

[ 180](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)#define SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE 20

[ 181](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)#define SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE 20

[ 182](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)#define SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE 4

183

[ 184](structsbs__gauge__manufacturer__name.md)struct [sbs\_gauge\_manufacturer\_name](structsbs__gauge__manufacturer__name.md) {

[ 185](structsbs__gauge__manufacturer__name.md#a13a5902df94842f7a69a8028b8708ced) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [manufacturer\_name\_length](structsbs__gauge__manufacturer__name.md#a13a5902df94842f7a69a8028b8708ced);

[ 186](structsbs__gauge__manufacturer__name.md#a40af61fe30263b21e9b9c92383562b0d) char [manufacturer\_name](structsbs__gauge__manufacturer__name.md#a40af61fe30263b21e9b9c92383562b0d)[[SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)];

187} \_\_packed;

188

[ 189](structsbs__gauge__device__name.md)struct [sbs\_gauge\_device\_name](structsbs__gauge__device__name.md) {

[ 190](structsbs__gauge__device__name.md#a5e599e923ccbdc7eb89ab6f7e1d3a662) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device\_name\_length](structsbs__gauge__device__name.md#a5e599e923ccbdc7eb89ab6f7e1d3a662);

[ 191](structsbs__gauge__device__name.md#a6699e048a1ca5feb2cadb05169bcfa5f) char [device\_name](structsbs__gauge__device__name.md#a6699e048a1ca5feb2cadb05169bcfa5f)[[SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)];

192} \_\_packed;

193

[ 194](structsbs__gauge__device__chemistry.md)struct [sbs\_gauge\_device\_chemistry](structsbs__gauge__device__chemistry.md) {

[ 195](structsbs__gauge__device__chemistry.md#a340cfddcc1ad7a758f75208b38208df4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device\_chemistry\_length](structsbs__gauge__device__chemistry.md#a340cfddcc1ad7a758f75208b38208df4);

[ 196](structsbs__gauge__device__chemistry.md#a2a3990be7618165d88790e53ac7b4e72) char [device\_chemistry](structsbs__gauge__device__chemistry.md#a2a3990be7618165d88790e53ac7b4e72)[[SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)];

197} \_\_packed;

198

[ 205](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568)typedef int (\*[fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568))(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

206 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val);

207

[ 214](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)typedef int (\*[fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9))(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

215 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val);

216

[ 223](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)typedef int (\*[fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69))(const struct [device](structdevice.md) \*dev,

224 [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type,

225 void \*dst, size\_t dst\_len);

226

[ 233](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7)typedef int (\*[fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7))(const struct [device](structdevice.md) \*dev);

234

235/\* Caching is entirely on the onus of the client \*/

236

[ 237](structfuel__gauge__driver__api.md)\_\_subsystem struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) {

[ 244](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91) [fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568) [get\_property](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91);

[ 245](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223) [fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9) [set\_property](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223);

[ 246](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570) [fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69) [get\_buffer\_property](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570);

[ 247](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c) [fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7) [battery\_cutoff](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c);

248};

249

[ 259](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1)\_\_syscall int [fuel\_gauge\_get\_prop](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

260 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val);

261

262static inline int z\_impl\_fuel\_gauge\_get\_prop(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

263 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val)

264{

265 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

266

267 if (api->get\_property == NULL) {

268 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

269 }

270

271 return api->get\_property(dev, prop, val);

272}

273

288

[ 289](group__fuel__gauge__interface.md#gac721c19bc2c9714c11ede5e6d86fd0b0)\_\_syscall int [fuel\_gauge\_get\_props](group__fuel__gauge__interface.md#gac721c19bc2c9714c11ede5e6d86fd0b0)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

290 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len);

291static inline int z\_impl\_fuel\_gauge\_get\_props(const struct [device](structdevice.md) \*dev,

292 [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

293 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len)

294{

295 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

296

297 for (int i = 0; i < len; i++) {

298 int ret = api->[get\_property](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91)(dev, props[i], vals + i);

299

300 if (ret) {

301 return ret;

302 }

303 }

304

305 return 0;

306}

307

[ 317](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)\_\_syscall int [fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

318 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val);

319

320static inline int z\_impl\_fuel\_gauge\_set\_prop(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

321 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val)

322{

323 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

324

325 if (api->[set\_property](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223) == NULL) {

326 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

327 }

328

329 return api->[set\_property](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223)(dev, prop, val);

330}

[ 343](group__fuel__gauge__interface.md#ga55bb2be9c9eae7c3a8d01df051178d01)\_\_syscall int [fuel\_gauge\_set\_props](group__fuel__gauge__interface.md#ga55bb2be9c9eae7c3a8d01df051178d01)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

344 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len);

345

346static inline int z\_impl\_fuel\_gauge\_set\_props(const struct [device](structdevice.md) \*dev,

347 [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

348 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len)

349{

350 for (int i = 0; i < len; i++) {

351 int ret = [fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)(dev, props[i], vals[i]);

352

353 if (ret) {

354 return ret;

355 }

356 }

357

358 return 0;

359}

360

371

[ 372](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c)\_\_syscall int [fuel\_gauge\_get\_buffer\_prop](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type,

373 void \*dst, size\_t dst\_len);

374

375static inline int z\_impl\_fuel\_gauge\_get\_buffer\_prop(const struct [device](structdevice.md) \*dev,

376 [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type,

377 void \*dst, size\_t dst\_len)

378{

379 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

380

381 if (api->[get\_buffer\_property](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570) == NULL) {

382 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

383 }

384

385 return api->[get\_buffer\_property](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570)(dev, prop\_type, dst, dst\_len);

386}

387

[ 396](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc)\_\_syscall int [fuel\_gauge\_battery\_cutoff](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc)(const struct [device](structdevice.md) \*dev);

397

398static inline int z\_impl\_fuel\_gauge\_battery\_cutoff(const struct [device](structdevice.md) \*dev)

399{

400 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

401

402 if (api->[battery\_cutoff](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c) == NULL) {

403 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

404 }

405

406 return api->[battery\_cutoff](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c)(dev);

407}

408

412

413#ifdef \_\_cplusplus

414}

415#endif /\* \_\_cplusplus \*/

416

417#include <syscalls/fuel\_gauge.h>

418

419#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BATTERY\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)

#define SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE

**Definition** fuel\_gauge.h:181

[fuel\_gauge\_set\_props](group__fuel__gauge__interface.md#ga55bb2be9c9eae7c3a8d01df051178d01)

int fuel\_gauge\_set\_props(const struct device \*dev, fuel\_gauge\_prop\_t \*props, union fuel\_gauge\_prop\_val \*vals, size\_t len)

Set a battery fuel-gauge property.

[fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806)

uint16\_t fuel\_gauge\_prop\_t

**Definition** fuel\_gauge.h:114

[fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7)

int(\* fuel\_gauge\_battery\_cutoff\_t)(const struct device \*dev)

Callback API for doing a battery cutoff.

**Definition** fuel\_gauge.h:233

[fuel\_gauge\_battery\_cutoff](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc)

int fuel\_gauge\_battery\_cutoff(const struct device \*dev)

Have fuel gauge cutoff its associated battery.

[fuel\_gauge\_get\_buffer\_prop](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c)

int fuel\_gauge\_get\_buffer\_prop(const struct device \*dev, fuel\_gauge\_prop\_t prop\_type, void \*dst, size\_t dst\_len)

Fetch a battery fuel-gauge buffer property.

[SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)

#define SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE

Data structures for reading SBS buffer properties.

**Definition** fuel\_gauge.h:180

[fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)

int fuel\_gauge\_set\_prop(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val val)

Set a battery fuel-gauge property.

[fuel\_gauge\_get\_prop](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1)

int fuel\_gauge\_get\_prop(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val \*val)

Fetch a battery fuel-gauge property.

[fuel\_gauge\_get\_props](group__fuel__gauge__interface.md#gac721c19bc2c9714c11ede5e6d86fd0b0)

int fuel\_gauge\_get\_props(const struct device \*dev, fuel\_gauge\_prop\_t \*props, union fuel\_gauge\_prop\_val \*vals, size\_t len)

Fetch multiple battery fuel-gauge properies.

[fuel\_gauge\_prop\_type](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171)

fuel\_gauge\_prop\_type

**Definition** fuel\_gauge.h:29

[fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)

int(\* fuel\_gauge\_set\_property\_t)(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val val)

Callback API for setting a fuel\_gauge property.

**Definition** fuel\_gauge.h:214

[fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568)

int(\* fuel\_gauge\_get\_property\_t)(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val \*val)

Callback API for getting a fuel\_gauge property.

**Definition** fuel\_gauge.h:205

[fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)

int(\* fuel\_gauge\_get\_buffer\_property\_t)(const struct device \*dev, fuel\_gauge\_prop\_t prop\_type, void \*dst, size\_t dst\_len)

Callback API for getting a fuel\_gauge buffer property.

**Definition** fuel\_gauge.h:223

[SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)

#define SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE

**Definition** fuel\_gauge.h:182

[FUEL\_GAUGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354)

@ FUEL\_GAUGE\_CURRENT

Battery current (uA); negative=discharging.

**Definition** fuel\_gauge.h:42

[FUEL\_GAUGE\_STATUS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40)

@ FUEL\_GAUGE\_STATUS

Alarm, Status and Error codes (flags).

**Definition** fuel\_gauge.h:78

[FUEL\_GAUGE\_SBS\_MFR\_ACCESS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd)

@ FUEL\_GAUGE\_SBS\_MFR\_ACCESS

Retrieve word from SBS1.1 ManufactuerAccess.

**Definition** fuel\_gauge.h:62

[FUEL\_GAUGE\_CONNECT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d)

@ FUEL\_GAUGE\_CONNECT\_STATE

Connect state of battery.

**Definition** fuel\_gauge.h:48

[FUEL\_GAUGE\_FLAGS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c)

@ FUEL\_GAUGE\_FLAGS

General Error/Runtime Flags.

**Definition** fuel\_gauge.h:50

[FUEL\_GAUGE\_CYCLE\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984)

@ FUEL\_GAUGE\_CYCLE\_COUNT

Cycle count in 1/100ths (number of charge/discharge cycles).

**Definition** fuel\_gauge.h:46

[FUEL\_GAUGE\_COMMON\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815)

@ FUEL\_GAUGE\_COMMON\_COUNT

Reserved to demark end of common fuel gauge properties.

**Definition** fuel\_gauge.h:103

[FUEL\_GAUGE\_MANUFACTURER\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8)

@ FUEL\_GAUGE\_MANUFACTURER\_NAME

Manufacturer of pack (1 byte length + 20 bytes data).

**Definition** fuel\_gauge.h:96

[FUEL\_GAUGE\_SBS\_MODE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae)

@ FUEL\_GAUGE\_SBS\_MODE

Battery Mode (flags).

**Definition** fuel\_gauge.h:72

[FUEL\_GAUGE\_SBS\_ATRATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58)

@ FUEL\_GAUGE\_SBS\_ATRATE

AtRate (mA or 10 mW).

**Definition** fuel\_gauge.h:84

[FUEL\_GAUGE\_DESIGN\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf)

@ FUEL\_GAUGE\_DESIGN\_VOLTAGE

Design Voltage (mV).

**Definition** fuel\_gauge.h:82

[FUEL\_GAUGE\_AVG\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396)

@ FUEL\_GAUGE\_AVG\_CURRENT

Runtime Dynamic Battery Parameters.

**Definition** fuel\_gauge.h:37

[FUEL\_GAUGE\_RUNTIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399)

@ FUEL\_GAUGE\_RUNTIME\_TO\_FULL

Remaining time in minutes until battery reaches full charge.

**Definition** fuel\_gauge.h:60

[FUEL\_GAUGE\_CHARGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e)

@ FUEL\_GAUGE\_CHARGE\_CURRENT

Battery desired Max Charging Current (uA).

**Definition** fuel\_gauge.h:74

[FUEL\_GAUGE\_CUSTOM\_BEGIN](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584)

@ FUEL\_GAUGE\_CUSTOM\_BEGIN

Reserved to demark downstream custom properties - use this value as the actual value may change over ...

**Definition** fuel\_gauge.h:108

[FUEL\_GAUGE\_DEVICE\_CHEMISTRY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9)

@ FUEL\_GAUGE\_DEVICE\_CHEMISTRY

Chemistry (1 byte length + 4 bytes data).

**Definition** fuel\_gauge.h:100

[FUEL\_GAUGE\_PROP\_MAX](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81)

@ FUEL\_GAUGE\_PROP\_MAX

Reserved to demark end of valid enum properties.

**Definition** fuel\_gauge.h:111

[FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0)

@ FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY

AtRateTimeToEmpty (minutes).

**Definition** fuel\_gauge.h:88

[FUEL\_GAUGE\_DESIGN\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67)

@ FUEL\_GAUGE\_DESIGN\_CAPACITY

Design Capacity (mAh or 10mWh).

**Definition** fuel\_gauge.h:80

[FUEL\_GAUGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71)

@ FUEL\_GAUGE\_VOLTAGE

Battery voltage (uV).

**Definition** fuel\_gauge.h:70

[FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a)

@ FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM

Remaining Time Alarm (minutes).

**Definition** fuel\_gauge.h:94

[FUEL\_GAUGE\_CHARGE\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f)

@ FUEL\_GAUGE\_CHARGE\_CUTOFF

Whether the battery underlying the fuel-gauge is cut off from charge.

**Definition** fuel\_gauge.h:44

[FUEL\_GAUGE\_CHARGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920)

@ FUEL\_GAUGE\_CHARGE\_VOLTAGE

Battery desired Max Charging Voltage (uV).

**Definition** fuel\_gauge.h:76

[FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee)

@ FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE

Absolute state of charge (percent, 0-100) - expressed as % of design capacity.

**Definition** fuel\_gauge.h:64

[FUEL\_GAUGE\_DEVICE\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10)

@ FUEL\_GAUGE\_DEVICE\_NAME

Name of pack (1 byte length + 20 bytes data).

**Definition** fuel\_gauge.h:98

[FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70)

@ FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL

AtRateTimeToFull (minutes).

**Definition** fuel\_gauge.h:86

[FUEL\_GAUGE\_TEMPERATURE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009)

@ FUEL\_GAUGE\_TEMPERATURE

Temperature in 0.1 K.

**Definition** fuel\_gauge.h:68

[FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9)

@ FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY

Full Charge Capacity in uAh (might change in some implementations to determine wear).

**Definition** fuel\_gauge.h:52

[FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd)

@ FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY

Remaining battery life time in minutes.

**Definition** fuel\_gauge.h:58

[FUEL\_GAUGE\_PRESENT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b)

@ FUEL\_GAUGE\_PRESENT\_STATE

Is the battery physically present.

**Definition** fuel\_gauge.h:54

[FUEL\_GAUGE\_REMAINING\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4)

@ FUEL\_GAUGE\_REMAINING\_CAPACITY

Remaining capacity in uAh.

**Definition** fuel\_gauge.h:56

[FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2)

@ FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM

Remaining Capacity Alarm (mAh or 10mWh).

**Definition** fuel\_gauge.h:92

[FUEL\_GAUGE\_BATTERY\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f)

@ FUEL\_GAUGE\_BATTERY\_CUTOFF

Used to cutoff the battery from the system - useful for storage/shipping of devices.

**Definition** fuel\_gauge.h:40

[FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b)

@ FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE

Relative state of charge (percent, 0-100) - expressed as % of full charge capacity.

**Definition** fuel\_gauge.h:66

[FUEL\_GAUGE\_SBS\_ATRATE\_OK](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec)

@ FUEL\_GAUGE\_SBS\_ATRATE\_OK

AtRateOK (boolean).

**Definition** fuel\_gauge.h:90

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602)

#define UINT16\_MAX

**Definition** stdint.h:28

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md)

**Definition** fuel\_gauge.h:237

[fuel\_gauge\_driver\_api::battery\_cutoff](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c)

fuel\_gauge\_battery\_cutoff\_t battery\_cutoff

**Definition** fuel\_gauge.h:247

[fuel\_gauge\_driver\_api::set\_property](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223)

fuel\_gauge\_set\_property\_t set\_property

**Definition** fuel\_gauge.h:245

[fuel\_gauge\_driver\_api::get\_property](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91)

fuel\_gauge\_get\_property\_t get\_property

Note: Historically this API allowed drivers to implement a custom multi-get/set property function,...

**Definition** fuel\_gauge.h:244

[fuel\_gauge\_driver\_api::get\_buffer\_property](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570)

fuel\_gauge\_get\_buffer\_property\_t get\_buffer\_property

**Definition** fuel\_gauge.h:246

[sbs\_gauge\_device\_chemistry](structsbs__gauge__device__chemistry.md)

**Definition** fuel\_gauge.h:194

[sbs\_gauge\_device\_chemistry::device\_chemistry](structsbs__gauge__device__chemistry.md#a2a3990be7618165d88790e53ac7b4e72)

char device\_chemistry[4]

**Definition** fuel\_gauge.h:196

[sbs\_gauge\_device\_chemistry::device\_chemistry\_length](structsbs__gauge__device__chemistry.md#a340cfddcc1ad7a758f75208b38208df4)

uint8\_t device\_chemistry\_length

**Definition** fuel\_gauge.h:195

[sbs\_gauge\_device\_name](structsbs__gauge__device__name.md)

**Definition** fuel\_gauge.h:189

[sbs\_gauge\_device\_name::device\_name\_length](structsbs__gauge__device__name.md#a5e599e923ccbdc7eb89ab6f7e1d3a662)

uint8\_t device\_name\_length

**Definition** fuel\_gauge.h:190

[sbs\_gauge\_device\_name::device\_name](structsbs__gauge__device__name.md#a6699e048a1ca5feb2cadb05169bcfa5f)

char device\_name[20]

**Definition** fuel\_gauge.h:191

[sbs\_gauge\_manufacturer\_name](structsbs__gauge__manufacturer__name.md)

**Definition** fuel\_gauge.h:184

[sbs\_gauge\_manufacturer\_name::manufacturer\_name\_length](structsbs__gauge__manufacturer__name.md#a13a5902df94842f7a69a8028b8708ced)

uint8\_t manufacturer\_name\_length

**Definition** fuel\_gauge.h:185

[sbs\_gauge\_manufacturer\_name::manufacturer\_name](structsbs__gauge__manufacturer__name.md#a40af61fe30263b21e9b9c92383562b0d)

char manufacturer\_name[20]

**Definition** fuel\_gauge.h:186

[fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md)

Property field to value/type union.

**Definition** fuel\_gauge.h:117

[fuel\_gauge\_prop\_val::design\_volt](unionfuel__gauge__prop__val.md#a11626713aef0445ad613a5976401d09e)

uint16\_t design\_volt

FUEL\_GAUGE\_DESIGN\_VOLTAGE.

**Definition** fuel\_gauge.h:162

[fuel\_gauge\_prop\_val::design\_cap](unionfuel__gauge__prop__val.md#a20aa5736b0ac3c5adda10152660de275)

uint16\_t design\_cap

FUEL\_GAUGE\_DESIGN\_CAPACITY.

**Definition** fuel\_gauge.h:160

[fuel\_gauge\_prop\_val::runtime\_to\_full](unionfuel__gauge__prop__val.md#a2c77e8de7fa40fadfa13dfd4c94df804)

uint32\_t runtime\_to\_full

FUEL\_GAUGE\_RUNTIME\_TO\_FULL.

**Definition** fuel\_gauge.h:140

[fuel\_gauge\_prop\_val::absolute\_state\_of\_charge](unionfuel__gauge__prop__val.md#a33297ff5bf70b510272eddf77ced411e)

uint8\_t absolute\_state\_of\_charge

FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE.

**Definition** fuel\_gauge.h:144

[fuel\_gauge\_prop\_val::temperature](unionfuel__gauge__prop__val.md#a36528b111568bd1c90859e454610fd9f)

uint16\_t temperature

FUEL\_GAUGE\_TEMPERATURE.

**Definition** fuel\_gauge.h:148

[fuel\_gauge\_prop\_val::relative\_state\_of\_charge](unionfuel__gauge__prop__val.md#a45b20c5118f7ee408d507b94e6cae1dc)

uint8\_t relative\_state\_of\_charge

FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE.

**Definition** fuel\_gauge.h:146

[fuel\_gauge\_prop\_val::fg\_status](unionfuel__gauge__prop__val.md#a65607bb9ba43022c9c566646d4763aac)

uint16\_t fg\_status

FUEL\_GAUGE\_STATUS.

**Definition** fuel\_gauge.h:158

[fuel\_gauge\_prop\_val::chg\_current](unionfuel__gauge__prop__val.md#a6f74626deef4debbd8dfe6c188984d1b)

uint32\_t chg\_current

FUEL\_GAUGE\_CHARGE\_CURRENT.

**Definition** fuel\_gauge.h:154

[fuel\_gauge\_prop\_val::sbs\_at\_rate\_time\_to\_empty](unionfuel__gauge__prop__val.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8)

uint16\_t sbs\_at\_rate\_time\_to\_empty

FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY.

**Definition** fuel\_gauge.h:168

[fuel\_gauge\_prop\_val::sbs\_mode](unionfuel__gauge__prop__val.md#a7fc0551e303de56e0eb6bdac1ecaccd0)

uint16\_t sbs\_mode

FUEL\_GAUGE\_SBS\_MODE.

**Definition** fuel\_gauge.h:152

[fuel\_gauge\_prop\_val::sbs\_remaining\_capacity\_alarm](unionfuel__gauge__prop__val.md#a818ab7faf8f51d4d1a5c5f070d54b997)

uint16\_t sbs\_remaining\_capacity\_alarm

FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM.

**Definition** fuel\_gauge.h:172

[fuel\_gauge\_prop\_val::chg\_voltage](unionfuel__gauge__prop__val.md#a8743f7e7a05919b5469e39527b697e62)

uint32\_t chg\_voltage

FUEL\_GAUGE\_CHARGE\_VOLTAGE.

**Definition** fuel\_gauge.h:156

[fuel\_gauge\_prop\_val::sbs\_mfr\_access\_word](unionfuel__gauge__prop__val.md#a957025a2a9fb7709e2bf478f15fd31a0)

uint16\_t sbs\_mfr\_access\_word

FUEL\_GAUGE\_SBS\_MFR\_ACCESS.

**Definition** fuel\_gauge.h:142

[fuel\_gauge\_prop\_val::sbs\_at\_rate\_ok](unionfuel__gauge__prop__val.md#a9b5015878c9a77d9c8330139f94843b7)

bool sbs\_at\_rate\_ok

FUEL\_GAUGE\_SBS\_ATRATE\_OK.

**Definition** fuel\_gauge.h:170

[fuel\_gauge\_prop\_val::current](unionfuel__gauge__prop__val.md#a9bed3247063f069bb92b2902cc5ff468)

int current

FUEL\_GAUGE\_CURRENT.

**Definition** fuel\_gauge.h:128

[fuel\_gauge\_prop\_val::sbs\_remaining\_time\_alarm](unionfuel__gauge__prop__val.md#aa0e46c727bb31acb5d41ce4bc6d5b106)

uint16\_t sbs\_remaining\_time\_alarm

FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM.

**Definition** fuel\_gauge.h:174

[fuel\_gauge\_prop\_val::full\_charge\_capacity](unionfuel__gauge__prop__val.md#aa29f7163a1637b6aa8cd6a15dc99d55b)

uint32\_t full\_charge\_capacity

FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY.

**Definition** fuel\_gauge.h:134

[fuel\_gauge\_prop\_val::sbs\_at\_rate](unionfuel__gauge__prop__val.md#aa5529fea5cfe765be9b66f5fad96ab2f)

int16\_t sbs\_at\_rate

FUEL\_GAUGE\_SBS\_ATRATE.

**Definition** fuel\_gauge.h:164

[fuel\_gauge\_prop\_val::voltage](unionfuel__gauge__prop__val.md#abec5cadefa09e088620a9598dec9c473)

int voltage

FUEL\_GAUGE\_VOLTAGE.

**Definition** fuel\_gauge.h:150

[fuel\_gauge\_prop\_val::cycle\_count](unionfuel__gauge__prop__val.md#ac27ae67a315a7204cea6e88962758587)

uint32\_t cycle\_count

FUEL\_GAUGE\_CYCLE\_COUNT.

**Definition** fuel\_gauge.h:130

[fuel\_gauge\_prop\_val::cutoff](unionfuel__gauge__prop__val.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a)

bool cutoff

FUEL\_GAUGE\_CHARGE\_CUTOFF.

**Definition** fuel\_gauge.h:126

[fuel\_gauge\_prop\_val::avg\_current](unionfuel__gauge__prop__val.md#ad96f07db337c038466dd17401c076d38)

int avg\_current

FUEL\_GAUGE\_AVG\_CURRENT.

**Definition** fuel\_gauge.h:124

[fuel\_gauge\_prop\_val::flags](unionfuel__gauge__prop__val.md#adeb93ed2120e808aac815dcbdf69067f)

uint32\_t flags

FUEL\_GAUGE\_FLAGS.

**Definition** fuel\_gauge.h:132

[fuel\_gauge\_prop\_val::remaining\_capacity](unionfuel__gauge__prop__val.md#adecf57aa90e2b5d483cfd889ec512400)

uint32\_t remaining\_capacity

FUEL\_GAUGE\_REMAINING\_CAPACITY.

**Definition** fuel\_gauge.h:136

[fuel\_gauge\_prop\_val::runtime\_to\_empty](unionfuel__gauge__prop__val.md#ae716bdf1346dc7767d98526db6083008)

uint32\_t runtime\_to\_empty

FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY.

**Definition** fuel\_gauge.h:138

[fuel\_gauge\_prop\_val::sbs\_at\_rate\_time\_to\_full](unionfuel__gauge__prop__val.md#aeeeddb48f22b54f90c603d58e9ffa9a5)

uint16\_t sbs\_at\_rate\_time\_to\_full

FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL.

**Definition** fuel\_gauge.h:166

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [fuel\_gauge.h](fuel__gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
